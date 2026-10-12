from __future__ import annotations

import argparse
import csv
import io
import json
import os
import re
import shlex
import subprocess
import sys
import threading
import time
import webbrowser
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlparse

from supervisor import ACTIVE_BATCH_STATES, Supervisor, atomic_json, now_iso


MAX_BODY_BYTES = 25 * 1024 * 1024
AUTO_INTERVAL_SECONDS = 300


class ControlCenter:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.pipeline = self.root / "bin" / "content-pipeline"
        self.supervisor_bin = self.root / "bin" / "content-supervisor"
        self.ui_dir = self.root / "pipeline" / "ui"
        self.base = self.root / "pipeline" / "state" / "control-center"
        self.state_path = self.base / "state.json"
        self.imports = self.base / "imports"
        self._lock = threading.RLock()
        self._task_thread: threading.Thread | None = None
        self._auto_thread: threading.Thread | None = None
        self.base.mkdir(parents=True, exist_ok=True)
        self.imports.mkdir(parents=True, exist_ok=True)
        pilot_profile = self.root / "pipeline" / "state" / "supervisor" / "pilot" / "profile.json"
        if not self.state_path.exists():
            self._save({
                "version": 1, "current_profile": "pilot" if pilot_profile.is_file() else None, "busy": False,
                "task": None, "auto_enabled": False, "events": [],
                "created_at": now_iso(), "updated_at": now_iso(),
            })
        elif pilot_profile.is_file():
            state = self._load()
            if not state.get("current_profile"):
                state["current_profile"] = "pilot"
                self._save(state)

    def _load(self) -> dict[str, Any]:
        with self._lock:
            return json.loads(self.state_path.read_text(encoding="utf-8"))

    def _save(self, state: dict[str, Any]) -> None:
        with self._lock:
            state["updated_at"] = now_iso()
            atomic_json(self.state_path, state)

    def event(self, level: str, message: str, detail: Any = None) -> None:
        state = self._load()
        state.setdefault("events", []).append({"at": now_iso(), "level": level, "message": message, "detail": detail})
        state["events"] = state["events"][-200:]
        self._save(state)

    def command(self, *args: str, supervisor: bool = False) -> str:
        executable = self.supervisor_bin if supervisor else self.pipeline
        completed = subprocess.run(
            [str(executable), *args], cwd=self.root, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        if completed.returncode:
            raise RuntimeError(completed.stdout.strip()[-5000:] or f"command failed: {' '.join(args)}")
        return completed.stdout.strip()

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
        raise RuntimeError(f"command did not return JSON: {output[-1000:]}")

    def current_supervisor(self) -> Supervisor | None:
        name = self._load().get("current_profile")
        return Supervisor(self.root, name) if name else None

    def state(self) -> dict[str, Any]:
        state = self._load()
        status: dict[str, Any] | None = None
        if state.get("current_profile"):
            try:
                status = Supervisor(self.root, state["current_profile"]).status()
            except Exception as exc:
                status = {"ok": False, "error": str(exc)}
        expansion_summary = None
        expansion_path = self.root / "pipeline" / "state" / "outputs" / "keyword-catalog-v1" / "micro-switch-keywords-10000-summary.json"
        if expansion_path.is_file():
            try:
                expansion_summary = json.loads(expansion_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                expansion_summary = {"error": "expansion summary is unreadable"}
        return {
            "control": state,
            "pipeline": status,
            "expansion": expansion_summary,
            "policy": {
                "local_only": True,
                "auto_start_on_login": False,
                "paid_confirmation_required": True,
                "auto_interval_seconds": AUTO_INTERVAL_SECONDS,
                "max_articles": 10_000,
            },
        }

    @staticmethod
    def validate_csv(text: str) -> tuple[list[dict[str, str]], list[str]]:
        if not text.strip():
            raise ValueError("CSV 文件为空")
        reader = csv.DictReader(io.StringIO(text.lstrip("\ufeff")))
        headers = [str(value).strip() for value in (reader.fieldnames or [])]
        if "keyword" not in headers:
            raise ValueError("CSV 必须包含 keyword 列")
        rows = []
        seen = set()
        for number, row in enumerate(reader, 2):
            keyword = str(row.get("keyword") or "").strip()
            if not keyword:
                continue
            key = keyword.casefold()
            if key in seen:
                continue
            seen.add(key)
            rows.append({header: str(row.get(header) or "").strip() for header in headers})
            if len(rows) > 100_000:
                raise ValueError("单次 CSV 最多允许 100,000 行")
        if not rows:
            raise ValueError("CSV 中没有有效 keyword")
        return rows, headers

    def import_csv(self, filename: str, text: str, requested_target: int | None = None) -> dict[str, Any]:
        rows, headers = self.validate_csv(text)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        safe_stem = re.sub(r"[^a-zA-Z0-9_-]+", "-", Path(filename or "keywords.csv").stem).strip("-")[:40] or "keywords"
        csv_path = self.imports / f"{stamp}-{safe_stem}.csv"
        with csv_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)
        os.chmod(csv_path, 0o600)

        run_id = self.command("create-run").splitlines()[-1].strip()
        imported = self.output_json(self.command("import-keywords", str(csv_path)))
        filtered = self.output_json(self.command("keywords-filter"))

        work = self.base / "runs" / run_id
        work.mkdir(parents=True, exist_ok=True)
        topic_input = work / "topics.jsonl"
        topic_embedded = work / "topics-embedded.jsonl"
        exported = self.output_json(self.command(
            "embedding-export", "--object-type", "topic", "--only-unclustered",
            "--limit", "100000", "--output", str(topic_input),
        ))
        clustered: dict[str, Any] = {"items": 0, "clusters": 0, "engine": "none-needed"}
        if exported.get("exported", 0):
            self.command("qdrant-init", "--provider", "local")
            self.command("embed", "--provider", "local", "--object-type", "topic", "--input", str(topic_input), "--output", str(topic_embedded))
            clustered = self.output_json(self.command("cluster", "--input", str(topic_embedded), "--incremental"))

        desired = min(max(int(requested_target or len(rows)), 1), 10_000)
        jobs = self.output_json(self.command("jobs-create", "--run-id", run_id, "--limit", str(desired), "--keyword-file", str(csv_path)))
        created = int(jobs.get("created", 0))
        if created < 1:
            raise RuntimeError("CSV 中的关键词没有创建出新文章任务；它们可能已在历史任务中存在")
        target = min(desired, created)
        profile = f"csv-{stamp.lower()}"
        self.command("--name", profile, "configure", "--run-id", run_id, "--target", str(target), "--poll-seconds", str(AUTO_INTERVAL_SECONDS), supervisor=True)
        prepared = Supervisor(self.root, profile).prepare("plan", min(target, 500))

        state = self._load()
        state.update({
            "current_profile": profile, "last_import": str(csv_path), "last_import_rows": len(rows),
            "auto_enabled": False, "task": None,
        })
        self._save(state)
        result = {
            "run_id": run_id, "profile": profile, "csv_rows": len(rows), "target": target,
            "imported": imported, "filtered": filtered, "clustered": clustered,
            "jobs": jobs, "prepared_plan": prepared,
        }
        self.event("success", "CSV 已导入，关键词已聚类，规划批次已准备", result)
        return result

    def _run_task(self, label: str, callback: Callable[[], Any]) -> bool:
        state = self._load()
        state.update({"busy": True, "task": {"label": label, "started_at": now_iso()}})
        self._save(state)
        self.event("info", f"开始：{label}")
        try:
            result = callback()
            self.event("success", f"完成：{label}", result)
            succeeded = True
        except Exception as exc:
            self.event("error", f"失败：{label}", {"error": str(exc)})
            succeeded = False
        finally:
            state = self._load()
            state.update({"busy": False, "task": None})
            self._save(state)
        return succeeded

    def enqueue(self, label: str, callback: Callable[[], Any]) -> None:
        with self._lock:
            if self._load().get("busy") or (self._task_thread and self._task_thread.is_alive()):
                raise RuntimeError("已有任务正在执行，请等待或暂停自动流程")
            self._task_thread = threading.Thread(target=self._run_task, args=(label, callback), daemon=True)
            self._task_thread.start()

    def action(self, action: str, payload: dict[str, Any]) -> dict[str, Any]:
        supervisor = self.current_supervisor()
        if action == "expand_audit":
            output_dir = self.root / "pipeline" / "state" / "outputs" / "keyword-catalog-v1"
            self.enqueue(
                "生成并审计一万条微动开关关键词",
                lambda: self.output_json(self.command(
                    "keywords-catalog-audit", "--target", "10000", "--output-dir", str(output_dir),
                )),
            )
            return {"accepted": True, "target": 10000, "paid_calls": 0}
        if action == "import":
            self.enqueue("导入 CSV 并准备规划", lambda: self.import_csv(payload.get("filename", "keywords.csv"), payload.get("text", ""), payload.get("target")))
            return {"accepted": True}
        if action == "auto_start":
            if payload.get("confirmation") != "确认自动付费":
                raise ValueError("请输入：确认自动付费")
            if not supervisor:
                raise RuntimeError("请先导入 CSV")
            state = self._load()
            state["auto_enabled"] = True
            self._save(state)
            self._start_auto_thread()
            self.event("warning", "自动流程已授权；规划、正文、审核和最多一次修复会产生 API 费用")
            return {"auto_enabled": True}
        if action == "auto_stop":
            state = self._load()
            state["auto_enabled"] = False
            self._save(state)
            self.event("info", "自动流程已暂停")
            return {"auto_enabled": False}
        if not supervisor:
            raise RuntimeError("请先导入 CSV")
        if self._load().get("auto_enabled") and action not in {"poll", "pause"}:
            raise RuntimeError("自动流程正在运行；请先暂停再进行手动阶段操作")
        if action == "poll":
            self.enqueue("查询并回收批次", supervisor.poll)
        elif action == "prepare":
            kind = payload.get("kind")
            if kind not in {"plan", "article", "review"}:
                raise ValueError("未知阶段")
            self.enqueue(f"准备 {kind}", lambda: supervisor.prepare(kind, int(payload.get("limit", 500))))
        elif action == "submit":
            kind = payload.get("kind")
            if kind not in {"plan", "article", "review", "repair"}:
                raise ValueError("未知阶段")
            if payload.get("confirmation") != "确认付费":
                raise ValueError("请输入：确认付费")
            self.enqueue(f"付费提交 {kind}", lambda: supervisor.submit(kind, True))
        elif action == "audit":
            self.enqueue("文本与语义去重", lambda: supervisor.audit(bool(payload.get("semantic", True))))
        elif action == "prepare_repair":
            self.enqueue("准备一次修改", supervisor.prepare_repair)
        elif action == "finalize":
            create_pr = bool(payload.get("create_pr"))
            if create_pr and payload.get("confirmation") != "创建PR":
                raise ValueError("创建 PR 请输入：创建PR")
            self.enqueue("验收与整理" + ("并创建 PR" if create_pr else ""), lambda: supervisor.finalize(create_pr))
        elif action == "pause":
            state = self._load()
            state["auto_enabled"] = False
            self._save(state)
            profile = supervisor.load()
            profile["paused"] = True
            supervisor.event(profile, "pause", {"source": "control-center"})
            supervisor.save(profile)
            return {"paused": True}
        elif action == "resume":
            profile = supervisor.load()
            profile["paused"] = False
            supervisor.event(profile, "resume", {"source": "control-center"})
            supervisor.save(profile)
            return {"paused": False}
        else:
            raise ValueError(f"不支持的操作：{action}")
        return {"accepted": True}

    def _auto_step(self) -> dict[str, Any]:
        supervisor = self.current_supervisor()
        if not supervisor:
            raise RuntimeError("no current profile")
        profile = supervisor.load()
        if profile.get("paused"):
            return {"waiting": "paused"}
        supervisor.poll()
        status = supervisor.status()
        if any(item.get("status") in ACTIVE_BATCH_STATES or item.get("status") in {"submitted", "unknown"} for item in status["tracked_batches"]):
            return {"waiting": "provider_batch", "batches": status["tracked_batches"]}
        counts = status["counts"]
        target = int(status["target"])
        accepted = sum(counts.get(key, 0) for key in ("validated", "reserve_validated", "rendered", "published"))
        if accepted >= target:
            result = supervisor.finalize(False)
            state = self._load()
            state["auto_enabled"] = False
            self._save(state)
            return {"complete": True, "result": result}
        if counts.get("semantic_review_failed", 0):
            supervisor.prepare_repair()
            return supervisor.submit("repair", True)
        if counts.get("awaiting_semantic_review", 0):
            supervisor.audit(True)
            supervisor.prepare("review", 500)
            return supervisor.submit("review", True)
        if counts.get("planned", 0):
            supervisor.prepare("article", 500)
            return supervisor.submit("article", True)
        if counts.get("queued_for_plan", 0):
            supervisor.prepare("plan", 500)
            return supervisor.submit("plan", True)
        raise RuntimeError(f"自动流程无法继续，当前状态：{counts}")

    def _auto_loop(self) -> None:
        while self._load().get("auto_enabled"):
            state = self._load()
            if not state.get("busy"):
                if not self._run_task("自动推进", self._auto_step):
                    state = self._load()
                    state["auto_enabled"] = False
                    self._save(state)
                    self.event("warning", "自动流程因错误停止；修复后可重新授权启动")
                    return
            for _ in range(AUTO_INTERVAL_SECONDS):
                if not self._load().get("auto_enabled"):
                    return
                time.sleep(1)

    def _start_auto_thread(self) -> None:
        with self._lock:
            if self._auto_thread and self._auto_thread.is_alive():
                return
            self._auto_thread = threading.Thread(target=self._auto_loop, daemon=True)
            self._auto_thread.start()

    def execute_palette(self, value: str) -> dict[str, Any]:
        parts = shlex.split(value)
        if not parts:
            raise ValueError("请输入命令")
        command = " ".join(parts).casefold()
        if command == "status":
            return self.state()
        if command == "expand audit":
            return self.action("expand_audit", {})
        if command in {"poll", "run-once"}:
            return self.action("poll", {})
        if command in {"pause", "resume"}:
            return self.action(command, {})
        if len(parts) == 2 and parts[0].casefold() == "prepare" and parts[1].casefold() in {"plan", "article", "review"}:
            return self.action("prepare", {"kind": parts[1].casefold()})
        if command in {"audit", "audit semantic"}:
            return self.action("audit", {"semantic": command.endswith("semantic")})
        if command == "prepare repair":
            return self.action("prepare_repair", {})
        if command == "finalize":
            return self.action("finalize", {"create_pr": False})
        if command == "auto stop":
            return self.action("auto_stop", {})
        raise ValueError("命令不在白名单中。可用：status、expand audit、poll、pause、resume、prepare plan/article/review、audit semantic、prepare repair、finalize、auto stop")


class Handler(BaseHTTPRequestHandler):
    server_version = "MSGControl/1.0"

    @property
    def app(self) -> ControlCenter:
        return self.server.app  # type: ignore[attr-defined]

    def log_message(self, fmt: str, *args: Any) -> None:
        return

    def _json(self, status: int, value: Any) -> None:
        data = json.dumps(value, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _same_origin(self) -> bool:
        origin = self.headers.get("Origin")
        if not origin:
            return True
        parsed = urlparse(origin)
        return parsed.hostname in {"127.0.0.1", "localhost"}

    def _body(self) -> dict[str, Any]:
        length = int(self.headers.get("Content-Length", "0"))
        if length > MAX_BODY_BYTES:
            raise ValueError("请求体过大")
        value = json.loads(self.rfile.read(length) or b"{}")
        if not isinstance(value, dict):
            raise ValueError("请求必须是 JSON 对象")
        return value

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path == "/api/state":
            self._json(HTTPStatus.OK, self.app.state())
            return
        target = "index.html" if path == "/" else path.lstrip("/")
        if target not in {"index.html", "app.css", "app.js"}:
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        file_path = self.app.ui_dir / target
        content_type = {".html": "text/html", ".css": "text/css", ".js": "text/javascript"}[file_path.suffix]
        data = file_path.read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type + "; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self) -> None:
        if not self._same_origin():
            self._json(HTTPStatus.FORBIDDEN, {"ok": False, "error": "origin rejected"})
            return
        try:
            payload = self._body()
            path = urlparse(self.path).path
            if path == "/api/action":
                result = self.app.action(str(payload.get("action", "")), payload)
            elif path == "/api/command":
                result = self.app.execute_palette(str(payload.get("command", "")))
            else:
                self._json(HTTPStatus.NOT_FOUND, {"ok": False, "error": "not found"})
                return
            self._json(HTTPStatus.ACCEPTED, {"ok": True, "result": result})
        except Exception as exc:
            self._json(HTTPStatus.BAD_REQUEST, {"ok": False, "error": str(exc)})


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description="Local MicroSwitchGuide visual control center")
    root.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parents[1])
    commands = root.add_subparsers(dest="command", required=True)
    serve = commands.add_parser("serve")
    serve.add_argument("--host", default="127.0.0.1", choices=["127.0.0.1", "localhost"])
    serve.add_argument("--port", type=int, default=8765)
    serve.add_argument("--open", action="store_true")
    imported = commands.add_parser("import")
    imported.add_argument("csv", type=Path)
    imported.add_argument("--target", type=int)
    palette = commands.add_parser("command")
    palette.add_argument("value")
    commands.add_parser("status")
    return root


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    app = ControlCenter(args.project_root)
    try:
        if args.command == "serve":
            server = ThreadingHTTPServer((args.host, args.port), Handler)
            server.app = app  # type: ignore[attr-defined]
            url = f"http://{args.host}:{args.port}"
            print(json.dumps({"url": url, "local_only": True, "auto_start_on_login": False}, ensure_ascii=False), flush=True)
            if app._load().get("auto_enabled"):
                app._start_auto_thread()
            if args.open:
                threading.Timer(0.4, lambda: webbrowser.open(url)).start()
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                pass
            finally:
                server.server_close()
            return 0
        if args.command == "import":
            result = app.import_csv(args.csv.name, args.csv.read_text(encoding="utf-8-sig"), args.target)
        elif args.command == "command":
            result = app.execute_palette(args.value)
        else:
            result = app.state()
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
