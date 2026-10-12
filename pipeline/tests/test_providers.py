from __future__ import annotations

import sys
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))

from providers import DataForSEOClient, GitHubClient, OpenRouterClient, QdrantClient, request_json


class ProviderContractTests(unittest.TestCase):
    @patch("providers.time.sleep")
    @patch("providers.urllib.request.urlopen")
    def test_get_retries_transient_network_errors(self, urlopen, sleep):
        response = unittest.mock.MagicMock()
        response.__enter__.return_value.read.return_value = b'{"ok": true}'
        urlopen.side_effect = [urllib.error.URLError("temporary"), response]
        self.assertEqual(request_json("test", "GET", "https://example.test"), {"ok": True})
        self.assertEqual(urlopen.call_count, 2)
        sleep.assert_called_once()

    @patch("providers.request_json")
    def test_dataforseo_keyword_tasks_are_split_by_seed(self, request):
        request.return_value = {"tasks": []}
        DataForSEOClient("login", "password").keyword_ideas(["micro switch", "snap action"], 2840, "en", 100)
        body = request.call_args.kwargs["body"]
        self.assertEqual(len(body), 2)
        self.assertEqual(body[0]["keywords"], ["micro switch"])
        self.assertEqual(body[0]["limit"], 100)

    @patch("providers.request_json")
    def test_openrouter_preserves_embedding_input_order(self, request):
        request.return_value = {"data": [{"index": 1, "embedding": [0, 1]}, {"index": 0, "embedding": [1, 0]}]}
        vectors = OpenRouterClient("key", "model").embed(["a", "b"])
        self.assertEqual(vectors, [[1, 0], [0, 1]])

    @patch("providers.request_json")
    def test_keyword_suggestions_require_exact_seed_phrase(self, request):
        request.return_value = {"tasks": []}
        DataForSEOClient("login", "password").keyword_suggestions("micro switch", 2840, "en", 25)
        body = request.call_args.kwargs["body"][0]
        self.assertTrue(body["exact_match"])
        self.assertTrue(body["include_seed_keyword"])
        self.assertEqual(body["keyword"], "micro switch")

    @patch("providers.request_json")
    def test_async_google_ads_discovery_posts_one_task(self, request):
        request.return_value = {"tasks": []}
        DataForSEOClient("login", "password").post_keywords_for_keywords_task(["micro switch", "snap action switch"], 2840, "en")
        self.assertTrue(request.call_args.args[2].endswith("/task_post"))
        self.assertEqual(request.call_args.kwargs["body"][0]["keywords"], ["micro switch", "snap action switch"])

    @patch("providers.request_json")
    def test_qdrant_collection_contract(self, request):
        request.return_value = {"result": True}
        QdrantClient("https://qdrant.example", "key").create_collection("msg_topics_v1", 768, "Cosine")
        self.assertEqual(request.call_args.kwargs["body"], {"vectors": {"size": 768, "distance": "Cosine"}})

    @patch("providers.request_json")
    def test_qdrant_batch_query_uses_read_retry_contract(self, request):
        request.return_value = {"result": [{"points": [{"score": 0.9}]}]}
        result = QdrantClient("https://qdrant.example", "key").query_batch("msg_topics_v1", [[1.0, 0.0]], 5, 0.87)
        self.assertEqual(result, [[{"score": 0.9}]])
        self.assertTrue(request.call_args.args[2].endswith("/points/query/batch"))
        self.assertEqual(request.call_args.kwargs["max_attempts"], 3)
        self.assertEqual(request.call_args.kwargs["body"]["searches"][0]["score_threshold"], 0.87)

    @patch("providers.request_json")
    def test_qdrant_upsert_retries_transient_writes(self, request):
        request.return_value = {"result": {"status": "completed"}}
        points = [{"id": "point-1", "vector": [1.0, 0.0], "payload": {"local_id": "kw-1"}}]
        QdrantClient("https://qdrant.example", "key").upsert("msg_topics_v1", points)
        self.assertEqual(request.call_args.kwargs["max_attempts"], 4)
        self.assertEqual(request.call_args.kwargs["body"], {"points": points})

    @patch("providers.request_json")
    def test_github_pr_never_requests_merge(self, request):
        request.return_value = {"html_url": "https://example/pr/1"}
        GitHubClient("token", "owner", "repo").create_pull_request("title", "content/run", "main", "body")
        self.assertTrue(request.call_args.args[2].endswith("/pulls"))
        self.assertEqual(request.call_args.kwargs["body"]["base"], "main")


if __name__ == "__main__":
    unittest.main()
