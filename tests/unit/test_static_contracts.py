import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[2]
APP_JS = (ROOT / "app.js").read_text(encoding="utf-8")
INDEX = (ROOT / "index.html").read_text(encoding="utf-8")


class StaticContractUnitTests(unittest.TestCase):
    def test_metadata_and_claim_ids_are_defined(self):
        self.assertIn("APP_METADATA", APP_JS)
        self.assertIn("appVersion:'0.1.0-roadmap'", APP_JS)
        for claim in ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"]:
            self.assertIn(claim, APP_JS)

    def test_condition_feature_flags_match_research_design(self):
        self.assertRegex(APP_JS, r"A:\{manipulation:true,comparison:false,notation:false")
        self.assertRegex(APP_JS, r"B:\{manipulation:true,comparison:true,notation:false")
        self.assertRegex(APP_JS, r"C:\{manipulation:true,comparison:true,notation:true,explanation:true,transfer:true")

    def test_scoring_contract_rewards_relation_and_symbolic_language(self):
        for term in ["invariant", "inverse", "identity", "order", "preserved", "structure"]:
            self.assertIn(term, APP_JS)
        self.assertIn("symbolicHits", APP_JS)
        self.assertRegex(APP_JS, re.escape("[UDLRFB]") + r".*4")

    def test_export_schema_contains_traceability_fields(self):
        for field in ["appName", "appVersion", "commitSha", "condition", "features", "scores", "eventLog"]:
            self.assertIn(field, APP_JS)

    def test_required_ui_targets_exist(self):
        for element_id in [
            "moveControls",
            "comparisonCards",
            "studentText",
            "transferCards",
            "conditionSelect",
            "eventLogPreview",
            "appVersion",
        ]:
            self.assertIn(f'id="{element_id}"', INDEX)


if __name__ == "__main__":
    unittest.main()

