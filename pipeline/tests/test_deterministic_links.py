import unittest

from content_ops import apply_authoritative_internal_links


class DeterministicLinkTests(unittest.TestCase):
    def test_replaces_model_links_and_inserts_before_closing_h2(self):
        article = {
            "primary_keyword": "micro switch 5pa2",
            "body_markdown": "## Main\nText [old](/guides/old/).\n\n## Conclusion\nFinal text.",
            "internal_links": [{"url": "/guides/old/"}],
        }
        links = [
            {
                "target_job_id": "job_a",
                "relation": "related",
                "anchor_text": "operating force",
                "url": "/guides/operating-force/",
            }
        ]
        result = apply_authoritative_internal_links(article, links)
        self.assertNotIn("/guides/old/", result["body_markdown"])
        self.assertEqual(result["body_markdown"].count("/guides/operating-force/"), 1)
        self.assertLess(result["body_markdown"].index("### Related guides"), result["body_markdown"].index("## Conclusion"))
        self.assertEqual(result["internal_links"], links)
        closing = result["body_markdown"].split("## Conclusion", 1)[1].casefold()
        self.assertEqual(closing.count("micro switch 5pa2"), 1)

    def test_closing_keeps_only_one_complete_keyword(self):
        article = {
            "primary_keyword": "micro switch lsm6d",
            "body_markdown": "## Main\nText.\n\n## Micro switch lsm6d conclusion\nMicro switch lsm6d remains unverified. Check micro switch lsm6d records.",
            "internal_links": [],
        }
        result = apply_authoritative_internal_links(article, [])
        closing = result["body_markdown"].split("## Micro switch lsm6d conclusion", 1)[1]
        self.assertEqual(closing.casefold().count("micro switch lsm6d"), 1)
        self.assertIn("this identifier", closing)


if __name__ == "__main__":
    unittest.main()
