from __future__ import annotations

import base64
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from core import canonical_json


class ProviderError(RuntimeError):
    def __init__(self, provider: str, status: int | None, message: str):
        super().__init__(f"{provider}: {status or 'network'}: {message}")
        self.provider = provider
        self.status = status


def request_json(
    provider: str,
    method: str,
    url: str,
    *,
    headers: dict[str, str] | None = None,
    body: Any | None = None,
    timeout: int = 15,
    max_attempts: int | None = None,
) -> Any:
    data = None if body is None else canonical_json(body).encode("utf-8")
    request_headers = {"Accept": "application/json", **(headers or {})}
    if data is not None:
        request_headers.setdefault("Content-Type", "application/json")
    attempts = max_attempts if max_attempts is not None else (3 if method.upper() == "GET" else 1)
    if attempts < 1:
        raise ValueError("max_attempts must be at least 1")
    for attempt in range(attempts):
        req = urllib.request.Request(url, data=data, method=method, headers=request_headers)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                payload = response.read()
                return json.loads(payload) if payload else {}
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")[:1000]
            retryable = exc.code == 429 or 500 <= exc.code < 600
            if not retryable or attempt + 1 == attempts:
                raise ProviderError(provider, exc.code, detail) from exc
        except urllib.error.URLError as exc:
            if attempt + 1 == attempts:
                raise ProviderError(provider, None, str(exc.reason)) from exc
        time.sleep(0.5 * (2 ** attempt))
    raise AssertionError("unreachable")


@dataclass
class DataForSEOClient:
    login: str
    password: str

    @property
    def headers(self) -> dict[str, str]:
        token = base64.b64encode(f"{self.login}:{self.password}".encode()).decode()
        return {"Authorization": f"Basic {token}"}

    def ping(self) -> dict[str, Any]:
        return request_json("dataforseo", "GET", "https://api.dataforseo.com/v3/appendix/user_data", headers=self.headers)

    def keyword_ideas(self, seeds: list[str], location_code: int, language_code: str, limit: int = 1000) -> dict[str, Any]:
        payload = [{"keywords": [seed], "location_code": location_code, "language_code": language_code, "limit": limit, "tag": f"seed-{index}"} for index, seed in enumerate(seeds)]
        return request_json(
            "dataforseo", "POST", "https://api.dataforseo.com/v3/dataforseo_labs/google/keyword_ideas/live",
            headers=self.headers, body=payload, timeout=180,
        )

    def keyword_suggestions(self, seed: str, location_code: int, language_code: str, limit: int = 1000) -> dict[str, Any]:
        return request_json(
            "dataforseo", "POST", "https://api.dataforseo.com/v3/dataforseo_labs/google/keyword_suggestions/live",
            headers=self.headers,
            body=[{
                "keyword": seed, "location_code": location_code, "language_code": language_code,
                "limit": limit, "exact_match": True, "include_seed_keyword": True,
                "ignore_synonyms": False, "filters": [["keyword_info.search_volume", ">", 0]],
            }],
            timeout=180,
        )

    def post_keywords_for_keywords_task(self, seeds: list[str], location_code: int, language_code: str) -> dict[str, Any]:
        if not 1 <= len(seeds) <= 20:
            raise ValueError("Google Ads Keywords For Keywords accepts 1-20 seed keywords per task")
        return request_json(
            "dataforseo", "POST", "https://api.dataforseo.com/v3/keywords_data/google_ads/keywords_for_keywords/task_post",
            headers=self.headers,
            body=[{
                "keywords": seeds, "location_code": location_code, "language_code": language_code,
                "include_adult_keywords": False, "sort_by": "search_volume", "tag": "microswitchguide",
            }],
            timeout=30,
        )

    def get_keywords_for_keywords_task(self, task_id: str) -> dict[str, Any]:
        return request_json(
            "dataforseo", "GET",
            f"https://api.dataforseo.com/v3/keywords_data/google_ads/keywords_for_keywords/task_get/{urllib.parse.quote(task_id)}",
            headers=self.headers, timeout=30,
        )

    def search_intent(self, keywords: list[str]) -> dict[str, Any]:
        if len(keywords) > 1000:
            raise ValueError("DataForSEO search intent accepts at most 1,000 keywords per task")
        return request_json(
            "dataforseo", "POST", "https://api.dataforseo.com/v3/dataforseo_labs/google/search_intent/live",
            headers=self.headers, body=[{"keywords": keywords}], timeout=180,
        )

    def organic_serp(self, keyword: str, location_code: int, language_code: str, device: str = "desktop", depth: int = 10) -> dict[str, Any]:
        return request_json(
            "dataforseo", "POST", "https://api.dataforseo.com/v3/serp/google/organic/live/advanced",
            headers=self.headers, body=[{"keyword": keyword, "location_code": location_code, "language_code": language_code, "device": device, "depth": depth}], timeout=180,
        )

    def post_organic_serp_tasks(self, keywords: list[tuple[str, str]], location_code: int, language_code: str, device: str = "desktop") -> dict[str, Any]:
        if len(keywords) > 100:
            raise ValueError("DataForSEO Standard SERP accepts at most 100 tasks per POST")
        payload = [{"keyword": keyword, "location_code": location_code, "language_code": language_code, "device": device, "depth": 10, "priority": 1, "tag": local_id} for local_id, keyword in keywords]
        return request_json(
            "dataforseo", "POST", "https://api.dataforseo.com/v3/serp/google/organic/task_post",
            headers=self.headers, body=payload, timeout=180,
        )

    def get_organic_serp_task(self, task_id: str) -> dict[str, Any]:
        return request_json(
            "dataforseo", "GET", f"https://api.dataforseo.com/v3/serp/google/organic/task_get/advanced/{urllib.parse.quote(task_id)}",
            headers=self.headers, timeout=30,
        )


@dataclass
class OpenRouterClient:
    api_key: str
    model: str

    def embed(self, texts: list[str], input_type: str = "document") -> list[list[float]]:
        result = request_json(
            "openrouter", "POST", "https://openrouter.ai/api/v1/embeddings",
            headers={"Authorization": f"Bearer {self.api_key}"},
            body={"model": self.model, "input": texts, "input_type": input_type}, timeout=180,
        )
        data = sorted(result.get("data", []), key=lambda item: item.get("index", 0))
        return [item["embedding"] for item in data]


@dataclass
class LocalEmbeddingClient:
    model: str
    device: str | None = None

    def __post_init__(self) -> None:
        try:
            from sentence_transformers import SentenceTransformer
        except ImportError as exc:
            raise ProviderError("local-embeddings", None, "sentence-transformers is missing; run ./bin/bootstrap-embeddings") from exc
        kwargs = {"device": self.device} if self.device else {}
        self._encoder = SentenceTransformer(self.model, **kwargs)

    def embed(self, texts: list[str], input_type: str = "document") -> list[list[float]]:
        del input_type
        vectors = self._encoder.encode(texts, batch_size=min(64, max(1, len(texts))), normalize_embeddings=True, show_progress_bar=False)
        return [vector.tolist() for vector in vectors]


@dataclass
class QdrantClient:
    url: str
    api_key: str

    @property
    def headers(self) -> dict[str, str]:
        return {"api-key": self.api_key}

    def ping(self) -> dict[str, Any]:
        return request_json("qdrant", "GET", self.url.rstrip("/") + "/collections", headers=self.headers)

    def create_collection(self, name: str, dimensions: int, distance: str) -> dict[str, Any]:
        return request_json(
            "qdrant", "PUT", f"{self.url.rstrip('/')}/collections/{urllib.parse.quote(name)}",
            headers=self.headers, body={"vectors": {"size": dimensions, "distance": distance}},
        )

    def upsert(self, collection: str, points: list[dict[str, Any]]) -> dict[str, Any]:
        return request_json(
            "qdrant", "PUT", f"{self.url.rstrip('/')}/collections/{urllib.parse.quote(collection)}/points?wait=true",
            headers=self.headers, body={"points": points}, timeout=180, max_attempts=4,
        )

    def query(self, collection: str, vector: list[float], limit: int = 20, score_threshold: float | None = None) -> list[dict[str, Any]]:
        body: dict[str, Any] = {"query": vector, "limit": limit, "with_payload": True}
        if score_threshold is not None:
            body["score_threshold"] = score_threshold
        result = request_json(
            "qdrant", "POST", f"{self.url.rstrip('/')}/collections/{urllib.parse.quote(collection)}/points/query",
            headers=self.headers, body=body,
        )
        return result.get("result", {}).get("points", result.get("result", []))

    def query_batch(self, collection: str, vectors: list[list[float]], limit: int = 20, score_threshold: float | None = None) -> list[list[dict[str, Any]]]:
        searches = []
        for vector in vectors:
            search: dict[str, Any] = {"query": vector, "limit": limit, "with_payload": True}
            if score_threshold is not None:
                search["score_threshold"] = score_threshold
            searches.append(search)
        result = request_json(
            "qdrant", "POST", f"{self.url.rstrip('/')}/collections/{urllib.parse.quote(collection)}/points/query/batch",
            headers=self.headers, body={"searches": searches}, timeout=60, max_attempts=3,
        )
        batches = result.get("result", [])
        return [batch.get("points", batch if isinstance(batch, list) else []) for batch in batches]


@dataclass
class OpenAIClient:
    api_key: str

    @property
    def headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.api_key}"}

    def list_models(self) -> dict[str, Any]:
        return request_json("openai", "GET", "https://api.openai.com/v1/models", headers=self.headers)

    def create_response(self, body: dict[str, Any]) -> dict[str, Any]:
        return request_json("openai", "POST", "https://api.openai.com/v1/responses", headers=self.headers, body=body, timeout=180)

    def upload_batch_file(self, path: Path) -> dict[str, Any]:
        boundary = "----msg-content-pipeline-boundary"
        payload = path.read_bytes()
        body = (
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"purpose\"\r\n\r\nbatch\r\n"
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{path.name}\"\r\n"
            "Content-Type: application/jsonl\r\n\r\n"
        ).encode() + payload + f"\r\n--{boundary}--\r\n".encode()
        req = urllib.request.Request(
            "https://api.openai.com/v1/files", data=body, method="POST",
            headers={**self.headers, "Content-Type": f"multipart/form-data; boundary={boundary}"},
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as response:
                return json.loads(response.read())
        except urllib.error.HTTPError as exc:
            raise ProviderError("openai", exc.code, exc.read().decode(errors="replace")[:1000]) from exc

    def create_batch(self, input_file_id: str, metadata: dict[str, str]) -> dict[str, Any]:
        return request_json(
            "openai", "POST", "https://api.openai.com/v1/batches", headers=self.headers,
            body={"input_file_id": input_file_id, "endpoint": "/v1/responses", "completion_window": "24h", "metadata": metadata},
        )

    def get_batch(self, batch_id: str) -> dict[str, Any]:
        return request_json("openai", "GET", f"https://api.openai.com/v1/batches/{batch_id}", headers=self.headers)

    def download_file(self, file_id: str) -> bytes:
        req = urllib.request.Request(f"https://api.openai.com/v1/files/{file_id}/content", headers=self.headers)
        try:
            with urllib.request.urlopen(req, timeout=180) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            raise ProviderError("openai", exc.code, exc.read().decode(errors="replace")[:1000]) from exc


@dataclass
class GitHubClient:
    token: str
    owner: str
    repo: str

    @property
    def base(self) -> str:
        return f"https://api.github.com/repos/{self.owner}/{self.repo}"

    @property
    def headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def repository(self) -> dict[str, Any]:
        return request_json("github", "GET", self.base, headers=self.headers)

    def create_pull_request(self, title: str, head: str, base: str, body: str) -> dict[str, Any]:
        return request_json("github", "POST", self.base + "/pulls", headers=self.headers, body={"title": title, "head": head, "base": base, "body": body})
