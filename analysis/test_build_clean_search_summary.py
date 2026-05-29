import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_clean_search_summary as summary


class CleanSearchSummaryTest(unittest.TestCase):
    def test_build_summary_from_current_runs(self):
        repo_root = Path(__file__).resolve().parents[1]

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp)
            payload = summary.build_outputs(
                repo_root=repo_root,
                json_output=output_dir / "summary.json",
                markdown_output=output_dir / "summary.md",
            )

            data = json.loads((output_dir / "summary.json").read_text(encoding="utf-8"))
            markdown = (output_dir / "summary.md").read_text(encoding="utf-8")

        self.assertEqual(payload["metadata"]["condition"], "Clean Search")
        self.assertEqual(data["metadata"]["groups"]["sim_prompt"], "No Intervention / baseline")
        self.assertEqual(data["aggregates"]["sim_prompt"]["n"], 5)
        self.assertEqual(data["aggregates"]["sim_prompt+skill"]["n"], 5)
        self.assertAlmostEqual(data["aggregates"]["sim_prompt"]["metrics"]["overall"]["mean"], 6.36, places=2)
        self.assertAlmostEqual(data["aggregates"]["sim_prompt+skill"]["metrics"]["overall"]["mean"], 7.72, places=2)
        self.assertEqual(len(data["cases"]), 5)
        self.assertEqual(len(data["human_audit_placeholders"]), 5)
        self.assertIn("detailed_diagnostics", data)
        self.assertIn("07794", data["detailed_diagnostics"])
        self.assertIn("baseline", data["detailed_diagnostics"]["07794"])
        self.assertIn("skill", data["detailed_diagnostics"]["07794"])
        self.assertGreater(len(data["detailed_diagnostics"]["07794"]["baseline"]["missing_points"]), 0)
        self.assertGreater(len(data["detailed_diagnostics"]["07794"]["baseline"]["overclaim_citation_claim_pairs"]), 0)
        self.assertIn("本次没有运行 Noisy Search / Misleading Search", markdown)
        self.assertIn("## 自动审计诊断摘要", markdown)
        self.assertIn("完整诊断见 JSON", markdown)
        self.assertIn("citation group support", markdown)
        self.assertIn("| Case | Baseline observation | Skill observation | Needs human check | Human audit notes | Frontend highlight? |", markdown)
        self.assertIn("## 人工审计空白表", markdown)


if __name__ == "__main__":
    unittest.main()
