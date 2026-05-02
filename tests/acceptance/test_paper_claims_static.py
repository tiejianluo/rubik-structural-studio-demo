import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[2]
APP_JS = (ROOT / "app.js").read_text(encoding="utf-8")
INDEX = (ROOT / "index.html").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")
ALL_TEXT = "\n".join([APP_JS, INDEX, README])


class PaperClaimStaticAcceptanceTests(unittest.TestCase):
    def test_c1_to_c7_claims_are_visible_in_the_experience(self):
        expected_terms = {
            "C1": ["Cube Lab", "reversible", "order-sensitive"],
            "C2": ["Compare", "preserved", "inverse"],
            "C3": ["Notation", "U⁴ = e", "R · R′ = e"],
            "C4": ["Transfer", "Cryptography", "Robotics", "Symmetry-aware AI"],
            "C5": ["Teacher controls", "Teacher orchestration"],
            "C6": ["Research mode", "Condition A", "Condition C"],
            "C7": ["relationalEncoding", "symbolicCompression", "transfer"],
        }
        for claim, terms in expected_terms.items():
            with self.subTest(claim=claim):
                for term in terms:
                    self.assertIn(term, ALL_TEXT)

    def test_c8_release_traceability_is_visible_and_exported(self):
        for term in ["appVersion", "commitSha", "Version", "Exports include app version"]:
            self.assertIn(term, ALL_TEXT)

    def test_reviewer_acceptance_journey_has_required_modules(self):
        for tab in [
            'data-tab="cube"',
            'data-tab="compare"',
            'data-tab="notation"',
            'data-tab="transfer"',
            'data-tab="teacher"',
            'data-tab="research"',
        ]:
            self.assertIn(tab, INDEX)


if __name__ == "__main__":
    unittest.main()

