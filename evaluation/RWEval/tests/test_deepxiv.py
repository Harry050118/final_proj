import unittest

from rw_eval.external.deepxiv import DeepXivClient
from rw_eval.schemas import ReferenceEntry


class FakeReader:
    def __init__(self):
        self.search_calls = []
        self.brief_calls = []
        self.head_calls = []

    def search(self, query, size=10, source="arxiv", **kwargs):
        self.search_calls.append({"query": query, "size": size, "source": source, **kwargs})
        return {
            "result": [
                {
                    "arxiv_id": "2406.07496",
                    "title": "TextGrad: Automatic Differentiation via Text",
                    "authors": ["Author One", "Author Two"],
                    "abstract": "TextGrad optimizes prompts with textual feedback.",
                    "publish_at": "2024-06-11",
                    "citations": 42,
                    "src_url": "https://arxiv.org/pdf/2406.07496",
                }
            ]
        }

    def brief(self, arxiv_id):
        self.brief_calls.append(arxiv_id)
        return {
            "arxiv_id": arxiv_id,
            "title": "TextGrad: Automatic Differentiation via Text",
            "tldr": "Textual gradients provide feedback for prompt optimization.",
            "publish_at": "2024-06-11",
            "src_url": "https://arxiv.org/pdf/2406.07496",
        }

    def head(self, arxiv_id):
        self.head_calls.append(arxiv_id)
        return {
            "arxiv_id": arxiv_id,
            "title": "TextGrad: Automatic Differentiation via Text",
            "abstract": "TextGrad uses natural language feedback as gradients.",
            "authors": ["Author One", "Author Two"],
            "categories": ["cs.CL"],
        }


class DeepXivClientTests(unittest.TestCase):
    def test_normalize_reference_uses_deepxiv_search_metadata(self):
        reader = FakeReader()
        client = DeepXivClient(reader=reader, search_size=3)
        ref = ReferenceEntry(
            ref_id="R1",
            raw_text="Yuksekgonul et al. (2024). TextGrad: Automatic Differentiation via Text. NeurIPS.",
            title="TextGrad: Automatic Differentiation via Text",
            year=2024,
        )

        normalized = client.normalize_reference(ref)

        self.assertEqual(reader.search_calls[0]["source"], "arxiv")
        self.assertEqual(reader.search_calls[0]["size"], 3)
        self.assertEqual(normalized.validity, "valid")
        self.assertEqual(normalized.arxiv_id, "2406.07496")
        self.assertEqual(normalized.s2_paper_id, "2406.07496")
        self.assertEqual(normalized.s2_metadata["title"], "TextGrad: Automatic Differentiation via Text")
        self.assertEqual(normalized.normalized_key, "arxiv:2406.07496")

    def test_retrieve_claim_evidence_prefers_arxiv_id_and_returns_snippets(self):
        reader = FakeReader()
        client = DeepXivClient(reader=reader)
        ref = ReferenceEntry(
            ref_id="R1",
            raw_text="TextGrad. arXiv 2406.07496.",
            title="TextGrad: Automatic Differentiation via Text",
            arxiv_id="2406.07496",
            normalized_key="textgrad-2024",
        )

        evidence = client.retrieve_claim_evidence(ref, "TextGrad optimizes prompts with textual feedback.")

        self.assertEqual(reader.brief_calls, ["2406.07496"])
        self.assertEqual(reader.head_calls, ["2406.07496"])
        self.assertEqual(evidence["paper_metadata"]["paper_id"], "2406.07496")
        self.assertGreaterEqual(len(evidence["snippets"]), 2)
        self.assertEqual(evidence["snippets"][0]["source"], "deepxiv_tldr")


if __name__ == "__main__":
    unittest.main()
