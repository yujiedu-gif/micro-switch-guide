import json
import unittest

from operations import _review_article, _review_custom_id, _review_plan


class ReviewIdentityTests(unittest.TestCase):
    def test_advisory_nearby_questions_do_not_change_review_identity(self):
        base = {
            "article": {"body_markdown": "A factual sentence."},
            "plan": {"owned_question": "What is it?"},
            "source_pack": {"claims": []},
            "nearby_owned_questions": ["Question A"],
        }
        changed = json.loads(json.dumps(base))
        changed["nearby_owned_questions"] = ["Question B", "Question C"]
        self.assertEqual(
            _review_custom_id("run", "job", "{}", base),
            _review_custom_id("run", "job", "{}", changed),
        )

    def test_internal_link_routing_is_not_review_relevant(self):
        first = {
            "body_markdown": "Read [operating force](/guides/operating-force/) next.",
            "internal_links": [{"url": "/guides/operating-force/", "anchor_text": "operating force"}],
            "title": "A title",
        }
        second = {
            "body_markdown": "Read [release force](/guides/release-force/) next.",
            "internal_links": [{"url": "/guides/release-force/", "anchor_text": "release force"}],
            "title": "A title",
        }
        self.assertEqual(_review_article(first), _review_article(second))

    def test_factual_prose_change_remains_review_relevant(self):
        first = {"body_markdown": "The switch is open.", "internal_links": []}
        second = {"body_markdown": "The switch is closed.", "internal_links": []}
        self.assertNotEqual(_review_article(first), _review_article(second))

    def test_plan_link_targets_are_not_review_relevant(self):
        first = {"owned_question": "What is release force?", "internal_link_targets": ["a"]}
        second = {"owned_question": "What is release force?", "internal_link_targets": ["b"]}
        self.assertEqual(_review_plan(first), _review_plan(second))


if __name__ == "__main__":
    unittest.main()
