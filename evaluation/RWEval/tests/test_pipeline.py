import unittest
from unittest.mock import patch

from rw_eval.pipeline import _bibliographic_accuracy_issues, _diagnostics, _nonredundant_citation_group_support, evaluate_sample
from rw_eval.llm.judging import _attach_claim_reference_metadata


SAMPLE = {
    "sample_id": "unit",
    "s_text": "DPO avoids explicit reward model training (Rafailov et al., 2023).",
    "s_references": "Rafailov, R. (2023). Direct Preference Optimization. NeurIPS.",
    "g_text": "Direct Preference Optimization removes the need for an explicit reward model (Rafailov et al., 2023).",
    "g_references": "Rafailov, R. (2023). Direct Preference Optimization. NeurIPS.",
}


class PipelineTests(unittest.TestCase):
    def test_pipeline_has_all_metrics(self):
        report = evaluate_sample(SAMPLE, use_semantic_scholar=False)
        expected = {
            "content_coverage",
            "citation_quality",
            "relevance",
            "thematic_structure",
            "synthesis_quality",
            "writing_quality",
            "length_conciseness",
            "citation_validity",
            "citation_appropriateness",
            "citation_coverage",
            "citation_placement",
            "citation_topic_consistency",
        }
        self.assertEqual(set(report["scores"].keys()), expected)
        self.assertIn("cleaning", report)
        self.assertEqual(list(report["scores"].keys())[:2], ["content_coverage", "citation_quality"])

    def test_pipeline_requires_llm(self):
        with self.assertRaises(ValueError):
            evaluate_sample(SAMPLE, use_llm=False, use_semantic_scholar=False)

    def test_invalid_sample(self):
        with self.assertRaises(ValueError):
            evaluate_sample({"s_text": "", "g_text": "x", "s_references": "", "g_references": ""})

    def test_claim_judging_payload_uses_only_claim_citations(self):
        claims = [
            {"id": "SClaim1", "text": "A", "citations": ["ref-a"]},
            {"id": "SClaim2", "text": "B", "citations": []},
        ]
        metadata = {
            "ref-a": {"title": "Paper A"},
            "ref-b": {"title": "Paper B"},
        }
        enriched = _attach_claim_reference_metadata(claims, metadata)
        self.assertEqual(enriched[0]["reference_metadata"], {"ref-a": {"title": "Paper A"}})
        self.assertEqual(enriched[1]["reference_metadata"], {})

    def test_nonredundant_citation_group_support_filters_single_pair_mirrors(self):
        citation_details = {
            "citation_judgments": [
                {"claim_id": "SClaim1", "reference_key": "ref-1", "support": "weak"},
                {"claim_id": "SClaim2", "reference_key": "ref-2", "support": "weak"},
                {"claim_id": "SClaim2", "reference_key": "ref-3", "support": "partial"},
            ],
            "citation_group_judgments": [
                {
                    "claim_id": "SClaim1",
                    "citation_count": 1,
                    "group_support": "weak",
                    "group_rationale": "Single citation mirror.",
                    "covered_aspects": [],
                    "missing_aspects": [],
                    "derived_from_single_pair": True,
                },
                {
                    "claim_id": "SClaim2",
                    "citation_count": 2,
                    "group_support": "partial",
                    "group_rationale": "Together the citations partially support the claim.",
                    "covered_aspects": ["method exists"],
                    "missing_aspects": ["integration detail"],
                    "derived_from_single_pair": False,
                },
            ],
        }

        filtered = _nonredundant_citation_group_support(citation_details)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]["claim_id"], "SClaim2")

    def test_bibliographic_accuracy_issues_include_invalid_or_flagged_references(self):
        refs = [
            {"ref_id": "R1", "title": "Valid Paper", "validity": "valid", "issues": []},
            {
                "ref_id": "R2",
                "title": "Unresolved Paper",
                "normalized_key": "unresolved-2024",
                "validity": "unresolved",
                "match_score": None,
                "issues": ["deepxiv_no_match"],
            },
            {
                "ref_id": "R3",
                "title": "Flagged Paper",
                "normalized_key": "flagged-2024",
                "validity": "valid",
                "match_score": 0.92,
                "issues": ["manual_check"],
            },
        ]

        issues = _bibliographic_accuracy_issues({"validity": {"references": refs}})

        self.assertEqual([item["ref_id"] for item in issues], ["R2", "R3"])
        self.assertEqual(issues[0]["validity"], "unresolved")
        self.assertEqual(issues[1]["issues"], ["manual_check"])

    def test_diagnostics_keep_hallucinated_references_and_bibliographic_issues(self):
        metric_results = {
            "content_coverage": {"details": {"missing_points": []}},
            "citation_quality": {
                "details": {
                    "validity": {
                        "references": [
                            {
                                "ref_id": "R1",
                                "title": "Mismatch Paper",
                                "normalized_key": "mismatch-2024",
                                "validity": "metadata_mismatch",
                                "match_score": 0.31,
                                "issues": ["deepxiv_metadata_mismatch"],
                            },
                            {
                                "ref_id": "R2",
                                "title": "Unresolved Paper",
                                "normalized_key": "unresolved-2024",
                                "validity": "unresolved",
                                "match_score": None,
                                "issues": ["deepxiv_no_match"],
                            },
                        ]
                    },
                    "problematic_citation_claim_pairs": [],
                    "overclaim_citation_claim_pairs": [],
                    "citation_judgments": [],
                    "citation_group_judgments": [],
                }
            },
            "thematic_structure": {"details": {"issues": []}},
            "length_conciseness": {"details": {"sub_scores": {}, "redundancy": {}}},
        }

        diagnostics = _diagnostics(metric_results, {})

        self.assertEqual(len(diagnostics["hallucinated_references"]), 1)
        self.assertEqual(diagnostics["hallucinated_references"][0]["ref_id"], "R1")
        self.assertEqual(len(diagnostics["bibliographic_accuracy_issues"]), 2)
        self.assertEqual(diagnostics["bibliographic_accuracy_issues"][1]["validity"], "unresolved")


if __name__ == "__main__":
    unittest.main()


class StubExtractor:
    def __init__(self, llm, strict=False):
        self.warnings = []

    def extract_gold(self, document):
        return {
            "topics": [{"id": "GTopic1", "label": "Stub Gold", "summary": document.text, "paragraph_ids": ["G1"], "importance": 3, "key_citations": []}],
            "key_points": [{"id": "GPoint1", "type": "method", "text": document.text, "importance": 3, "topic_id": "GTopic1", "citations": []}],
            "key_references": [],
        }

    def extract_candidate(self, document):
        claims = []
        for idx, sentence in enumerate(document.sentences, start=1):
            claims.append(
                {
                    "id": f"SClaim{idx}",
                    "paragraph_id": sentence.paragraph_id,
                    "text": sentence.text,
                    "is_factual": True,
                    "citations": [],
                }
            )
        return {
            "topics": [{"id": "STopic1", "label": "Stub Candidate", "summary": document.text, "paragraph_ids": ["S1"], "key_citations": []}],
            "claims": claims,
        }


class StubJudger:
    def __init__(self, llm, strict=False):
        self.warnings = []

    def judge_alignment(self, gold, candidate):
        return {
            "alignments": [
                {
                    "gold_point_id": "GPoint1",
                    "best_claim_ids": ["SClaim1"],
                    "match_score": 1.0,
                    "status": "complete",
                    "rationale": "Stub alignment.",
                }
            ]
        }

    def judge_claims(self, gold, candidate, reference_metadata):
        judgments = []
        for claim in candidate.get("claims", []):
            judgments.append({"claim_id": claim["id"], "relevance_score": 1.0, "rationale": "Stub relevance."})
        return {"claim_judgments": judgments}

    def judge_thematic(self, gold, candidate):
        return {
            "topic_alignment": [{"g_topic_id": "GTopic1", "s_topic_ids": ["STopic1"], "match_score": 8.0, "rationale": "Stub thematic."}],
            "paragraph_scores": [{"paragraph_id": "S1", "topic_purity": 8.0, "topic_coherence": 8.0, "citation_topic_consistency": 8.0, "issues": []}],
            "topic_granularity": {"score": 8.0, "rationale": "Stub granularity."},
            "topic_ordering": {"score": 8.0, "rationale": "Stub ordering."},
        }

    def judge_synthesis_writing(self, sample_text, gold, candidate):
        return {
            "synthesis_quality": {"score": 8.0, "rationale": "Stub synthesis.", "issues": []},
            "writing_quality": {"score": 8.0, "rationale": "Stub writing.", "issues": []},
        }

    def judge_citation_appropriateness(self, candidate, reference_metadata, reference_lookup=None, evidence_retriever=None):
        return {
            "citation_judgments": [
                {
                    "claim_id": "SClaim1",
                    "reference_key": "rafailov-2023",
                    "support": "yes",
                    "support_rationale": "Stub citation support.",
                    "appropriateness_score": 8.0,
                    "placement_score": 8.0,
                    "topic_consistency_score": 8.0,
                    "overclaim_status": "none",
                    "overclaim_rationale": "",
                    "rationale": "Stub citation support.",
                }
            ],
            "retrieval_events": [],
        }


for _name in ("test_pipeline_has_all_metrics", "test_invalid_sample"):
    _original = getattr(PipelineTests, _name)
    setattr(
        PipelineTests,
        _name,
        patch("rw_eval.pipeline.Extractor", StubExtractor)(patch("rw_eval.pipeline.Judger", StubJudger)(_original)),
    )
