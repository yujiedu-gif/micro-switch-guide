from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path


REQUIRED = (
    "DATAFORSEO_LOGIN",
    "DATAFORSEO_PASSWORD",
    "OPENAI_API_KEY",
    "QDRANT_URL",
    "QDRANT_API_KEY",
    "GITHUB_TOKEN",
)
OPTIONAL = ("OPENROUTER_API_KEY",)
KNOWN = REQUIRED + OPTIONAL


def load_env_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.is_file():
        return values
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        if re.fullmatch(r"[A-Z][A-Z0-9_]+", key.strip()):
            values[key.strip()] = value.strip().strip("'\"")
    return values


def effective_credentials(path: Path, include_helpers: bool = True) -> dict[str, str]:
    stored = load_env_file(path)
    values = {name: os.environ.get(name) or stored.get(name, "") for name in KNOWN}
    if include_helpers and not values.get("GITHUB_TOKEN"):
        values["GITHUB_TOKEN"] = github_token_from_credential_helper()
    return values


def github_token_from_credential_helper() -> str:
    """Read an existing GitHub credential without persisting or printing it."""
    try:
        result = subprocess.run(
            ["git", "credential", "fill"],
            input="protocol=https\nhost=github.com\n\n",
            text=True,
            capture_output=True,
            timeout=5,
            check=False,
            env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    if result.returncode != 0:
        return ""
    for line in result.stdout.splitlines():
        if line.startswith("password="):
            return line.split("=", 1)[1]
    return ""


def import_credentials(source_dir: Path, destination: Path) -> dict[str, str]:
    """Import known credential formats without ever returning secret values."""
    values = effective_credentials(destination, include_helpers=False)
    for path in sorted(source_dir.glob("*.txt")):
        text = path.read_text(encoding="utf-8", errors="replace").strip()
        lower_name = path.name.casefold()
        pairs = _pairs(text)
        if "dataforseo" in lower_name:
            values["DATAFORSEO_LOGIN"] = pairs.get("name", pairs.get("login", values["DATAFORSEO_LOGIN"]))
            values["DATAFORSEO_PASSWORD"] = pairs.get("api key", pairs.get("password", values["DATAFORSEO_PASSWORD"]))
        elif "qdrant" in lower_name:
            url = _first_url(text)
            token = _token_after(text, ("api-key", "api_key", "key"))
            if not token and re.fullmatch(r"[A-Za-z0-9_.-]{40,}", text):
                token = text
            if url:
                values["QDRANT_URL"] = url.rstrip("/")
            if token:
                values["QDRANT_API_KEY"] = token
        elif any(word in lower_name for word in ("openai", "gpt", "batch")):
            token = _first_token(text, ("sk-", "sk-proj-"))
            if token:
                values["OPENAI_API_KEY"] = token
        elif "openrouter" in lower_name:
            token = _first_token(text, ("sk-or-", "sk-"))
            if token:
                values["OPENROUTER_API_KEY"] = token
        elif "github" in lower_name:
            token = _first_token(text, ("github_pat_", "ghp_"))
            if token:
                values["GITHUB_TOKEN"] = token

    write_credentials(destination, values)
    return credential_status(values)


def write_credentials(destination: Path, values: dict[str, str]) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Generated locally. Never commit this file."]
    lines.extend(f"{name}={_escape(values[name])}" for name in KNOWN if values.get(name))
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")
    destination.chmod(0o600)


def credential_status(values: dict[str, str]) -> dict[str, str]:
    status = {name: "configured" if values.get(name) else "missing" for name in REQUIRED}
    status.update({name: "configured (optional)" if values.get(name) else "not configured (optional)" for name in OPTIONAL})
    return status


def _pairs(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"\s*([^:=]+?)\s*[:=]\s*(.+?)\s*$", line)
        if match:
            result[match.group(1).casefold()] = match.group(2).strip().strip("'\"")
    return result


def _first_url(text: str) -> str | None:
    match = re.search(r"https?://[^\s)'\"]+", text)
    return match.group(0).rstrip("\\") if match else None


def _token_after(text: str, names: tuple[str, ...]) -> str | None:
    for name in names:
        match = re.search(rf"{re.escape(name)}\s*[:=]\s*['\"]?([^\s'\"\\]+)", text, re.I)
        if match:
            return match.group(1)
    return None


def _first_token(text: str, prefixes: tuple[str, ...]) -> str | None:
    for prefix in sorted(prefixes, key=len, reverse=True):
        match = re.search(re.escape(prefix) + r"[A-Za-z0-9_.-]{20,}", text)
        if match:
            return match.group(0)
    return None


def _escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace("\n", "\\n")
