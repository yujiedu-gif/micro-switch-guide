from __future__ import annotations

import argparse
import fcntl
import json
import os
import signal
import sqlite3
import subprocess
import sys
import time
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


TERMINAL_BATCH_STATES = {"completed", "failed", "expired", "cancelled"}
ACTIVE_BATCH_STATES = {"validating", "in_progress", "finalizing", "cancelling"}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def atomic_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.chmod(temporary, 0o600)
    os.replace(temporary, path)


def read_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise RuntimeError(f"supervisor profile does not exist: {path}; run configure first")
    return json.loads(path.read_text(encoding="utf-8"))


@contextmanager
def exclusive_lock(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a+") as handle:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise RuntimeError("another supervisor process is already operating on this profile") from exc
        yield


class Supervisor:
    def __init__(self, root: Path, name: str):
        self.root = root.resolve()
        self.name = name
        self.pipeline = self.root / "bin" / "content-pipeline"
        self.base = self.root / "pipeline" / "state" / "supervisor" / name
        self.profile_path = self.base / "profile.json"
        self.lock_path = self.base / "profile.lock"
        self.log_path = self.base / "supervisor.log"
        self.db_path = self.root / "pipeline" / "state" / "content-pipeline.db"

    def load(self) -> dict[str, Any]:
        return read_json(self.profile_path)

    def save(self, profile: dict[str, Any]) -> None:
        profile["updated_at"] = now_iso()
        atomic_json(self.profile_path, profile)

    def event(self, profile: dict[str, Any], action: str, detail: Any) -> None:
        item = {"at": now_iso(), "action": action, "detail": detail}
        profile.setdefault("events", []).append(item)
        profile["events"] = profile["events"][-100:]
        self.base.mkdir(parents=True, exist_ok=True)
        with self.log_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")

    def command(self, *args: str, allow_failure: bool = False) -> tuple[int, str]:
        completed = subprocess.run(
            [str(self.pipeline), *args], cwd=self.root, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        output = completed.stdout.strip()
        if completed.returncode and not allow_failure:
            raise RuntimeError(f"content-pipeline {' '.join(args)} failed ({completed.returncode}):\n{output[-4000:]}")
        return completed.returncode, output

    @staticmethod
    def output_json(output: str) -> dict[str, Any]:
        lines = [line for line in output.splitlines() if line.strip()]
        for start in range(len(lines) - 1, -1, -1):
            try:
                value = json.loads("\n".join(lines[start:]))
                if isinstance(value, dict):
                    return value
            except json.JSONDecodeError:
                continue
        raise RuntimeError(f"command did not return a JSON object: {output[-1000:]}")

    def counts(self, profile: dict[str, Any]) -> dict[str, int]:
        with sqlite3.connect(self.db_path) as connection:
            rows = connection.execute(
                "SELECT status,COUNT(*) FROM content_jobs WHERE created_run_id=? GROUP BY status ORDER BY status",
                (profile["run_id"],),
            ).fetchall()
        return {status: count for status, count in rows}

    def next_action(self, profile: dict[str, Any], counts: dict[str, int]) -> str:
        tracked = profile.get("tracked_batches", [])
        active = [item for item in tracked if item.get("status") not in TERMINAL_BATCH_STATES]
        if active:
            counts = active[-1].get("request_counts") or {}
            return (
                f"OpenAI Batch 排队/执行中：{counts.get('completed', 0)}/{counts.get('total', '?')} 完成；"
                f"本机 watcher 正常，每 {profile['poll_seconds'] // 60} 分钟查询"
            )
        if counts.get("awaiting_semantic_review", 0):
            return "先执行 audit；再执行 prepare --kind review"
        if counts.get("semantic_review_failed", 0):
            return "执行 prepare-repair（每篇最多一次修改）"
        accepted = counts.get("validated", 0) + counts.get("rendered", 0) + counts.get("published", 0)
        if accepted >= profile["target"]:
            return "执行 finalize；验收通过后可手动 publish --create-pr"
        if counts.get("planned", 0):
            return "执行 prepare --kind article"
        if counts.get("queued_for_plan", 0):
            return "执行 prepare --kind plan"
        return "当前没有可自动推进的任务；检查拒绝项或补充候选文章"

    def status(self) -> dict[str, Any]:
        profile = self.load()
        counts = self.counts(profile)
        tracked = [
            {key: item.get(key) for key in ("batch_id", "kind", "status", "request_counts", "last_checked_at", "input")}
            for item in profile.get("tracked_batches", [])
        ]
        return {
            "name": self.name,
            "run_id": profile["run_id"],
            "target": profile["target"],
            "paused": profile.get("paused", False),
            "watch_pid": profile.get("watch_pid"),
            "counts": counts,
            "tracked_batches": tracked,
            "prepared": profile.get("prepared", {}),
            "next_manual_action": self.next_action(profile, counts),
            "profile": str(self.profile_path),
            "log": str(self.log_path),
        }

    def poll(self) -> dict[str, Any]:
        auto_audit = False
        with exclusive_lock(self.lock_path):
            profile = self.load()
            if profile.get("paused"):
                return {"paused": True, "message": "profile is paused; run resume to continue"}
            results = []
            for item in profile.get("tracked_batches", []):
                if item.get("status") in TERMINAL_BATCH_STATES and item.get("terminal_ingested"):
                    continue
                code, output = self.command("batch-status", "--batch-id", item["batch_id"], allow_failure=True)
                result = self.output_json(output)
                status = result.get("status", "unknown")
                item["status"] = status
                item["last_checked_at"] = now_iso()
                item["request_counts"] = result.get("request_counts")
                files = result.get("files") or {}
                ingested = set(item.get("ingested_files", []))
                for label in ("output", "errors"):
                    path = files.get(label)
                    if not path or path in ingested or not Path(path).is_file():
                        continue
                    ingest_code, ingest_output = self.command("ingest-batch", "--input", path, allow_failure=True)
                    ingested.add(path)
                    self.event(profile, "ingest", {"batch_id": item["batch_id"], "file": path, "exit": ingest_code, "output": ingest_output[-1000:]})
                item["ingested_files"] = sorted(ingested)
                if status in TERMINAL_BATCH_STATES:
                    item["terminal_ingested"] = not files or all(path in ingested for path in files.values())
                    if item["kind"] == "article" and item["terminal_ingested"] and not item.get("local_audit_complete"):
                        item["local_audit_pending"] = True
                        auto_audit = True
                results.append({"batch_id": item["batch_id"], "kind": item["kind"], "status": status, "request_counts": result.get("request_counts"), "provider_exit": code})
            self.event(profile, "poll", results)
            self.save(profile)
            response = {"batches": results, "next_manual_action": self.next_action(profile, self.counts(profile))}
        if auto_audit:
            try:
                response["local_audit"] = self.audit(True)
                with exclusive_lock(self.lock_path):
                    profile = self.load()
                    for item in profile.get("tracked_batches", []):
                        if item.get("local_audit_pending"):
                            item["local_audit_pending"] = False
                            item["local_audit_complete"] = True
                    self.event(profile, "automatic_local_audit", {"status": "complete"})
                    self.save(profile)
            except Exception as exc:
                response["local_audit_error"] = str(exc)[:1000]
                with exclusive_lock(self.lock_path):
                    profile = self.load()
                    self.event(profile, "automatic_local_audit", {"status": "failed", "error": str(exc)[:1000]})
                    self.save(profile)
        return response

    def prepare(self, kind: str, limit: int) -> dict[str, Any]:
        with exclusive_lock(self.lock_path):
            profile = self.load()
            active = [
                item for item in profile.get("tracked_batches", [])
                if item.get("kind") == kind and item.get("status") not in TERMINAL_BATCH_STATES
            ]
            if active:
                raise RuntimeError(f"cannot prepare {kind}: an existing {kind} batch is still active ({active[-1]['batch_id']})")
            run_id = profile["run_id"]
            wave = self.base / "waves" / f"{kind}-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
            wave.mkdir(parents=True, exist_ok=True)
            if kind == "article":
                self.command("source-packs-build", "--run-id", run_id, "--limit", str(limit))
                self.command("links-build", "--run-id", run_id, "--limit", str(limit), "--output", str(wave / "links.jsonl"))
            input_path = wave / f"{kind}-input.jsonl"
            self.command("jobs-export", "--run-id", run_id, "--kind", kind, "--limit", str(limit), "--output", str(input_path))
            if not input_path.is_file() or not input_path.read_text(encoding="utf-8").strip():
                raise RuntimeError(f"no eligible {kind} jobs were exported")
            batch_dir = wave / "batches"
            self.command("build-batches", "--run-id", run_id, "--kind", kind, "--input", str(input_path), "--output-dir", str(batch_dir), "--chunk-size", "500")
            profile.setdefault("prepared", {})[kind] = {"wave": str(wave), "input": str(input_path), "batch_dir": str(batch_dir), "prepared_at": now_iso()}
            self.event(profile, "prepare", {"kind": kind, "wave": str(wave)})
            self.save(profile)
            return profile["prepared"][kind]

    def submit(self, kind: str, confirm_paid: bool) -> dict[str, Any]:
        if not confirm_paid:
            raise RuntimeError("paid API action blocked; repeat with --confirm-paid after reviewing the prepared files")
        with exclusive_lock(self.lock_path):
            profile = self.load()
            active = [
                item for item in profile.get("tracked_batches", [])
                if item.get("kind") == kind and item.get("status") not in TERMINAL_BATCH_STATES
            ]
            if active:
                raise RuntimeError(f"duplicate paid submit blocked: {kind} batch is still active ({active[-1]['batch_id']})")
            prepared = profile.get("prepared", {}).get(kind)
            if not prepared:
                raise RuntimeError(f"no prepared {kind} wave; run prepare --kind {kind} first")
            manifest = json.loads((Path(prepared["batch_dir"]) / "manifest.json").read_text(encoding="utf-8"))
            submitted = []
            for file_item in manifest.get("files", []):
                batch_file = Path(file_item["path"])
                rows = [json.loads(line) for line in batch_file.read_text(encoding="utf-8").splitlines() if line.strip()]
                if not rows:
                    continue
                custom_ids = [row["custom_id"] for row in rows]
                with sqlite3.connect(self.db_path) as connection:
                    already = connection.execute(
                        f"SELECT COUNT(*) FROM batch_requests WHERE custom_id IN ({','.join('?' for _ in custom_ids)}) AND batch_id IS NOT NULL",
                        custom_ids,
                    ).fetchone()[0]
                if already:
                    continue
                _, output = self.command("batch-submit", "--run-id", profile["run_id"], "--kind", kind, "--input", str(batch_file))
                result = self.output_json(output)
                tracked = {
                    "batch_id": result["batch_id"], "kind": kind, "input": str(batch_file),
                    "status": result.get("status", "submitted"), "tracked_at": now_iso(), "ingested_files": [],
                }
                profile.setdefault("tracked_batches", []).append(tracked)
                submitted.append(tracked)
            self.event(profile, "paid_submit", {"kind": kind, "batches": submitted})
            self.save(profile)
            return {"submitted": submitted}

    def audit(self, semantic: bool) -> dict[str, Any]:
        with exclusive_lock(self.lock_path):
            profile = self.load()
            run_id = profile["run_id"]
            audit_dir = self.base / "audits" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            audit_dir.mkdir(parents=True, exist_ok=True)
            articles = audit_dir / "articles.jsonl"
            _, export_output = self.command(
                "articles-export", "--run-id", run_id,
                "--status", "awaiting_semantic_review", "--status", "validated",
                "--limit", "10000", "--output", str(articles),
            )
            _, lexical_output = self.command("dedupe", "--input", str(articles), "--output", str(audit_dir / "lexical.jsonl"), "--apply")
            detail: dict[str, Any] = {"export": self.output_json(export_output), "lexical": self.output_json(lexical_output)}
            if semantic:
                detail["semantic"] = {}
                for granularity in ("article", "section"):
                    embedding_input = audit_dir / f"{granularity}-embedding-input.jsonl"
                    embedded = audit_dir / f"{granularity}-embedded.jsonl"
                    semantic_output = audit_dir / f"{granularity}-semantic.jsonl"
                    self.command(
                        "embedding-export", "--run-id", run_id, "--object-type", "chunk",
                        "--granularity", granularity, "--status", "awaiting_semantic_review", "--status", "validated",
                        "--limit", "10000", "--output", str(embedding_input),
                    )
                    self.command("embed", "--provider", "local", "--object-type", "chunk", "--input", str(embedding_input), "--output", str(embedded))
                    _, output = self.command(
                        "dedupe-semantic", "--run-id", run_id, "--input", str(embedded),
                        "--output", str(semantic_output), "--apply",
                    )
                    detail["semantic"][granularity] = self.output_json(output)
            self.event(profile, "audit", detail)
            profile["last_audit"] = {"at": now_iso(), "semantic": semantic, "path": str(audit_dir)}
            self.save(profile)
            return detail

    def prepare_repair(self) -> dict[str, Any]:
        with exclusive_lock(self.lock_path):
            profile = self.load()
            article_inputs = [Path(item["input"]) for item in profile.get("tracked_batches", []) if item.get("kind") == "article" and item.get("input")]
            if not article_inputs:
                raise RuntimeError("no tracked article input files are available for semantic repair")
            wave = self.base / "waves" / f"repair-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
            wave.mkdir(parents=True, exist_ok=True)
            merged = wave / "original-article-requests.jsonl"
            seen: set[str] = set()
            with merged.open("w", encoding="utf-8") as target:
                for path in article_inputs:
                    for line in path.read_text(encoding="utf-8").splitlines():
                        if not line.strip():
                            continue
                        custom_id = json.loads(line)["custom_id"]
                        if custom_id not in seen:
                            target.write(line + "\n")
                            seen.add(custom_id)
            repair_file = wave / "repair-001.jsonl"
            _, output = self.command("semantic-repair", "--run-id", profile["run_id"], "--input", str(merged), "--output", str(repair_file))
            result = self.output_json(output)
            manifest_dir = wave / "batches"
            manifest_dir.mkdir()
            target = manifest_dir / repair_file.name
            target.write_bytes(repair_file.read_bytes())
            atomic_json(manifest_dir / "manifest.json", {"run_id": profile["run_id"], "kind": "repair", "files": [{"path": str(target)}]})
            profile.setdefault("prepared", {})["repair"] = {"wave": str(wave), "input": str(merged), "batch_dir": str(manifest_dir), "prepared_at": now_iso()}
            self.event(profile, "prepare_repair", result)
            self.save(profile)
            return result

    def prepare_retry(self, batch_id: str) -> dict[str, Any]:
        with exclusive_lock(self.lock_path):
            profile = self.load()
            tracked = next((item for item in profile.get("tracked_batches", []) if item["batch_id"] == batch_id), None)
            if not tracked:
                raise RuntimeError("the batch is not tracked by this profile")
            wave = self.base / "waves" / f"transport-retry-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
            manifest_dir = wave / "batches"
            manifest_dir.mkdir(parents=True)
            retry_file = manifest_dir / "repair-001.jsonl"
            _, output = self.command("batch-retry", "--run-id", profile["run_id"], "--input", tracked["input"], "--output", str(retry_file))
            result = self.output_json(output)
            atomic_json(manifest_dir / "manifest.json", {"run_id": profile["run_id"], "kind": "repair", "files": [{"path": str(retry_file)}]})
            profile.setdefault("prepared", {})["repair"] = {"wave": str(wave), "input": tracked["input"], "batch_dir": str(manifest_dir), "prepared_at": now_iso(), "purpose": "transport_retry"}
            self.event(profile, "prepare_transport_retry", {"batch_id": batch_id, **result})
            self.save(profile)
            return result

    def finalize(self, create_pr: bool) -> dict[str, Any]:
        with exclusive_lock(self.lock_path):
            profile = self.load()
            run_id = profile["run_id"]
            self.command("review-enforce", "--run-id", run_id, "--retract")
            self.command("publication-select", "--run-id", run_id, "--target", str(profile["target"]))
            self.command("links-reconcile", "--run-id", run_id)
            self.command("render-run", "--run-id", run_id, "--limit", str(profile["target"]))
            _, acceptance = self.command("acceptance-check", "--run-id", run_id, "--target", str(profile["target"]), "--build-site", allow_failure=True)
            result = self.output_json(acceptance)
            profile["acceptance"] = result
            if create_pr:
                if not result.get("passed"):
                    raise RuntimeError("PR blocked because acceptance-check did not pass")
                _, output = self.command("prepare-pr", "--run-id", run_id)
                profile["pull_request"] = self.output_json(output)
            self.event(profile, "finalize", {"acceptance": result, "create_pr": create_pr})
            self.save(profile)
            return {"acceptance": result, "pull_request": profile.get("pull_request")}


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description="Manually controlled MicroSwitchGuide batch supervisor")
    root.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parents[1])
    root.add_argument("--name", default="pilot")
    commands = root.add_subparsers(dest="command", required=True)
    configure = commands.add_parser("configure")
    configure.add_argument("--run-id", required=True)
    configure.add_argument("--target", type=int, default=50)
    configure.add_argument("--poll-seconds", type=int, default=300)
    configure.add_argument("--force", action="store_true", help="replace an existing profile")
    track = commands.add_parser("track")
    track.add_argument("--batch-id", required=True)
    track.add_argument("--kind", choices=["plan", "article", "review", "repair"], required=True)
    track.add_argument("--input", type=Path, required=True)
    commands.add_parser("status")
    commands.add_parser("run-once")
    watch = commands.add_parser("watch", aliases=["start"])
    watch.add_argument("--interval", type=int)
    commands.add_parser("pause")
    commands.add_parser("resume")
    prepare = commands.add_parser("prepare")
    prepare.add_argument("--kind", choices=["plan", "article", "review"], required=True)
    prepare.add_argument("--limit", type=int, default=500)
    submit = commands.add_parser("submit")
    submit.add_argument("--kind", choices=["plan", "article", "review", "repair"], required=True)
    submit.add_argument("--confirm-paid", action="store_true")
    audit = commands.add_parser("audit")
    audit.add_argument("--semantic", action="store_true")
    commands.add_parser("prepare-repair")
    prepare_retry = commands.add_parser("prepare-retry")
    prepare_retry.add_argument("--batch-id", required=True)
    finalize = commands.add_parser("finalize")
    finalize.add_argument("--create-pr", action="store_true")
    return root


def main(argv: list[str] | None = None) -> int:
    raw_args = list(sys.argv[1:] if argv is None else argv)
    # Keep --name convenient after the subcommand even though it is a global
    # option internally (for example: `content-supervisor status --name pilot`).
    if "--name" in raw_args:
        index = raw_args.index("--name")
        if index + 1 >= len(raw_args):
            raise SystemExit("--name requires a value")
        pair = raw_args[index:index + 2]
        del raw_args[index:index + 2]
        raw_args[0:0] = pair
    args = parser().parse_args(raw_args)
    supervisor = Supervisor(args.project_root, args.name)
    try:
        if args.command == "configure":
            if not 1 <= args.target <= 10_000:
                raise RuntimeError("target must be between 1 and 10,000")
            if args.poll_seconds < 30:
                raise RuntimeError("poll interval must be at least 30 seconds")
            if supervisor.profile_path.exists() and not args.force:
                raise RuntimeError("profile already exists; use --force only when you intentionally want to replace it")
            profile = {
                "version": 1, "name": args.name, "run_id": args.run_id, "target": args.target,
                "poll_seconds": args.poll_seconds, "paused": False, "tracked_batches": [],
                "prepared": {}, "events": [], "created_at": now_iso(), "updated_at": now_iso(),
            }
            with sqlite3.connect(supervisor.db_path) as connection:
                if not connection.execute("SELECT 1 FROM runs WHERE run_id=?", (args.run_id,)).fetchone():
                    raise RuntimeError(f"unknown run id: {args.run_id}")
            supervisor.save(profile)
            result: Any = supervisor.status()
        elif args.command == "track":
            if not args.input.is_file():
                raise RuntimeError(f"batch input does not exist: {args.input}")
            with exclusive_lock(supervisor.lock_path):
                profile = supervisor.load()
                existing = next((item for item in profile["tracked_batches"] if item["batch_id"] == args.batch_id), None)
                if existing:
                    existing.update({"kind": args.kind, "input": str(args.input.resolve())})
                else:
                    profile["tracked_batches"].append({"batch_id": args.batch_id, "kind": args.kind, "input": str(args.input.resolve()), "status": "submitted", "tracked_at": now_iso(), "ingested_files": []})
                supervisor.event(profile, "track", {"batch_id": args.batch_id, "kind": args.kind})
                supervisor.save(profile)
            result = supervisor.status()
        elif args.command == "status":
            result = supervisor.status()
        elif args.command == "run-once":
            result = supervisor.poll()
        elif args.command in {"watch", "start"}:
            profile = supervisor.load()
            interval = args.interval or profile["poll_seconds"]
            if interval < 30:
                raise RuntimeError("poll interval must be at least 30 seconds")
            profile["watch_pid"] = os.getpid()
            profile["paused"] = False
            supervisor.save(profile)
            print(json.dumps({"watching": args.name, "pid": os.getpid(), "interval": interval, "stop": "Ctrl-C or run pause from another terminal"}, ensure_ascii=False), flush=True)
            try:
                while True:
                    result = supervisor.poll()
                    print(json.dumps(result, ensure_ascii=False), flush=True)
                    if result.get("paused"):
                        break
                    time.sleep(interval)
            except KeyboardInterrupt:
                pass
            finally:
                profile = supervisor.load()
                if profile.get("watch_pid") == os.getpid():
                    profile["watch_pid"] = None
                    supervisor.save(profile)
            return 0
        elif args.command in {"pause", "resume"}:
            with exclusive_lock(supervisor.lock_path):
                profile = supervisor.load()
                profile["paused"] = args.command == "pause"
                pid = profile.get("watch_pid")
                supervisor.event(profile, args.command, {"watch_pid": pid})
                supervisor.save(profile)
            if args.command == "pause" and pid and pid != os.getpid():
                try:
                    os.kill(int(pid), signal.SIGINT)
                except (ProcessLookupError, ValueError):
                    pass
            result = supervisor.status()
        elif args.command == "prepare":
            result = supervisor.prepare(args.kind, args.limit)
        elif args.command == "submit":
            result = supervisor.submit(args.kind, args.confirm_paid)
        elif args.command == "audit":
            result = supervisor.audit(args.semantic)
        elif args.command == "prepare-repair":
            result = supervisor.prepare_repair()
        elif args.command == "prepare-retry":
            result = supervisor.prepare_retry(args.batch_id)
        elif args.command == "finalize":
            result = supervisor.finalize(args.create_pr)
        else:
            raise AssertionError(args.command)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
