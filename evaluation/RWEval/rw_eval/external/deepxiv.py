"""DeepXiv-backed reference normalization and evidence retrieval."""

from __future__ import annotations

import json
import os
import re
from dataclasses import replace
from typing import Any, Dict, List, Optional

from rw_eval.external.cache import JsonCache
from rw_eval.parsing.references import make_reference_key
from rw_eval.schemas import ReferenceEntry
from rw_eval.utils import text_similarity


class DeepXivClient:
    def __init__(
        self,
        reader: Any | None = None,
        token: str | None = None,
        source: str = "arxiv",
        search_size: int = 5,
        cache: Optional[JsonCache] = None,
    ):
        self.reader = reader if reader is not None else _build_reader(token)
        self.source = source
        self.search_size = search_size
        self.cache = cache

    def normalize_references(self, references: List[ReferenceEntry]) -> List[ReferenceEntry]:
        return [self.normalize_reference(ref) for ref in references]

    def normalize_reference(self, ref: ReferenceEntry) -> ReferenceEntry:
        lookup_key = json.dumps(
            {
                "arxiv_id": ref.arxiv_id,
                "title": ref.title,
                "year": ref.year,
                "raw": ref.raw_text,
                "source": self.source,
            },
            sort_keys=True,
        )
        cached = self.cache.get("deepxiv_normalize", lookup_key) if self.cache else None
        if cached is not None:
            return _reference_from_cached(ref, cached)

        out = replace(ref)
        arxiv_id = ref.arxiv_id or _extract_arxiv_id(ref.raw_text) or _extract_arxiv_id(ref.title or "")
        metadata: Dict[str, Any] = {}
        errors: List[str] = []

        if arxiv_id:
            try:
                metadata = self.reader.brief(arxiv_id) or {}
            except Exception as exc:
                errors.append(str(exc))

        if not metadata:
            query = ref.title or ref.raw_text
            try:
                candidates = _search_results(self.reader.search(query, size=self.search_size, source=self.source))
                metadata = _select_best_candidate(ref, candidates) or {}
            except Exception as exc:
                errors.append(str(exc))

        if metadata:
            out.arxiv_id = _paper_id(metadata) or arxiv_id
            out.s2_paper_id = out.arxiv_id
            out.s2_metadata = _metadata_payload(metadata, out.arxiv_id)
            out.title = out.s2_metadata.get("title") or out.title
            out.authors = _authors(out.s2_metadata.get("authors")) or out.authors
            out.year = _year(out.s2_metadata) or out.year
            out.match_score = _metadata_match_score(ref, out.s2_metadata)
            out.validity = "valid" if out.match_score >= 0.65 else "metadata_mismatch"
            if out.validity == "metadata_mismatch":
                out.issues = list(out.issues) + ["deepxiv_metadata_mismatch"]
            out.normalized_key = make_reference_key(out)
        else:
            out.validity = "unresolved"
            out.issues = list(out.issues) + (errors or ["deepxiv_no_match"])

        if self.cache:
            self.cache.set("deepxiv_normalize", lookup_key, _cached_reference_payload(out))
        return out

    def retrieve_claim_evidence(self, ref: ReferenceEntry, claim_text: str, max_snippets: int = 4) -> Dict[str, Any]:
        arxiv_id = ref.arxiv_id or ref.s2_paper_id or _extract_arxiv_id(ref.raw_text) or _extract_arxiv_id(ref.title or "")
        cache_key = json.dumps(
            {
                "arxiv_id": arxiv_id,
                "title": ref.title,
                "claim_text": claim_text,
                "max_snippets": max_snippets,
            },
            sort_keys=True,
        )
        cached = self.cache.get("deepxiv_claim_evidence", cache_key) if self.cache else None
        if cached is not None:
            return cached

        errors: List[str] = []
        paper: Dict[str, Any] = {}
        snippets: List[Dict[str, str]] = []
        query = ref.title or ref.raw_text

        if arxiv_id:
            query = arxiv_id
            try:
                brief = self.reader.brief(arxiv_id) or {}
                paper.update(brief)
                snippets.extend(_paper_snippets(brief))
            except Exception as exc:
                errors.append(str(exc))
            try:
                head = self.reader.head(arxiv_id) or {}
                paper.update({k: v for k, v in head.items() if v})
                snippets.extend(_paper_snippets(head))
            except Exception as exc:
                errors.append(str(exc))
        else:
            try:
                candidates = _search_results(self.reader.search(query, size=1, source=self.source))
                if candidates:
                    paper = candidates[0]
                    snippets.extend(_paper_snippets(paper))
            except Exception as exc:
                errors.append(str(exc))

        result = {
            "query": query,
            "snippets": _dedupe_snippets(snippets)[:max_snippets],
            "paper_metadata": {
                "paper_id": _paper_id(paper) or arxiv_id,
                "title": paper.get("title") or ref.title,
                "venue": paper.get("venue") or self.source,
                "year": _year(paper) or ref.year,
                "url": paper.get("url") or paper.get("src_url"),
            },
            "errors": errors,
        }
        if self.cache:
            self.cache.set("deepxiv_claim_evidence", cache_key, result)
        return result


def _build_reader(token: str | None = None) -> Any:
    from deepxiv_sdk import Reader

    return Reader(token=token or os.environ.get("DEEPXIV_TOKEN") or os.environ.get("DEEPXIV_API_TOKEN"))


def _search_results(payload: Any) -> List[Dict[str, Any]]:
    if isinstance(payload, dict):
        result = payload.get("result", [])
        return result if isinstance(result, list) else []
    return []


def _select_best_candidate(ref: ReferenceEntry, candidates: List[Dict[str, Any]]) -> Dict[str, Any] | None:
    if not candidates:
        return None
    title = ref.title or ref.raw_text
    if not title:
        return candidates[0]
    return max(candidates, key=lambda item: text_similarity(title, str(item.get("title") or "")))


def _metadata_payload(metadata: Dict[str, Any], paper_id: str | None) -> Dict[str, Any]:
    return {
        "paperId": paper_id or _paper_id(metadata),
        "title": metadata.get("title"),
        "authors": _authors(metadata.get("authors")),
        "year": _year(metadata),
        "venue": metadata.get("venue") or "DeepXiv",
        "abstract": metadata.get("abstract") or metadata.get("summary"),
        "url": metadata.get("url") or metadata.get("src_url"),
        "externalIds": {"ArXiv": paper_id or _paper_id(metadata)} if (paper_id or _paper_id(metadata)) else {},
        "tldr": {"text": metadata.get("tldr")} if metadata.get("tldr") else None,
        "citationCount": metadata.get("citations"),
        "source": "deepxiv",
    }


def _paper_id(metadata: Dict[str, Any]) -> str | None:
    for key in ("arxiv_id", "paper_id", "id"):
        value = metadata.get(key)
        if value:
            return str(value)
    return _extract_arxiv_id(str(metadata.get("src_url") or metadata.get("url") or ""))


def _paper_snippets(paper: Dict[str, Any]) -> List[Dict[str, str]]:
    snippets = []
    if paper.get("tldr"):
        snippets.append({"source": "deepxiv_tldr", "citation": _paper_id(paper) or "", "text": str(paper["tldr"])})
    if paper.get("abstract"):
        snippets.append({"source": "deepxiv_abstract", "citation": _paper_id(paper) or "", "text": str(paper["abstract"])})
    if paper.get("summary"):
        snippets.append({"source": "deepxiv_summary", "citation": _paper_id(paper) or "", "text": str(paper["summary"])})
    return snippets


def _dedupe_snippets(snippets: List[Dict[str, str]]) -> List[Dict[str, str]]:
    seen = set()
    deduped = []
    for snippet in snippets:
        text = (snippet.get("text") or "").strip()
        if not text or text in seen:
            continue
        seen.add(text)
        deduped.append(snippet)
    return deduped


def _authors(value: Any) -> List[str]:
    if isinstance(value, list):
        authors = []
        for item in value:
            if isinstance(item, dict):
                name = item.get("name")
            else:
                name = str(item)
            if name:
                authors.append(str(name))
        return authors
    if isinstance(value, str) and value.strip():
        return [part.strip() for part in value.split(",") if part.strip()]
    return []


def _year(metadata: Dict[str, Any]) -> int | None:
    value = metadata.get("year") or metadata.get("publish_at") or metadata.get("publicationDate")
    if value is None:
        return None
    match = re.search(r"(19|20)\d{2}", str(value))
    return int(match.group(0)) if match else None


def _metadata_match_score(ref: ReferenceEntry, metadata: Dict[str, Any]) -> float:
    score = 0.0
    if ref.title and metadata.get("title"):
        score = max(score, text_similarity(ref.title, str(metadata.get("title"))))
    if ref.arxiv_id and ref.arxiv_id == _paper_id(metadata):
        score = max(score, 1.0)
    return score or 0.5


def _extract_arxiv_id(text: str) -> str | None:
    match = re.search(r"(?:arxiv[:\s/abs]*|^)(\d{4}\.\d{4,5})(?:v\d+)?", text or "", re.IGNORECASE)
    return match.group(1) if match else None


def _cached_reference_payload(ref: ReferenceEntry) -> Dict[str, Any]:
    return {
        "arxiv_id": ref.arxiv_id,
        "s2_paper_id": ref.s2_paper_id,
        "s2_metadata": ref.s2_metadata,
        "match_score": ref.match_score,
        "validity": ref.validity,
        "issues": ref.issues,
        "normalized_key": ref.normalized_key,
        "title": ref.title,
        "authors": ref.authors,
        "year": ref.year,
    }


def _reference_from_cached(ref: ReferenceEntry, cached: Dict[str, Any]) -> ReferenceEntry:
    out = replace(ref)
    out.arxiv_id = cached.get("arxiv_id")
    out.s2_paper_id = cached.get("s2_paper_id")
    out.s2_metadata = cached.get("s2_metadata") or {}
    out.match_score = float(cached.get("match_score") or 0.0)
    out.validity = cached.get("validity") or "unknown"
    out.issues = list(cached.get("issues") or [])
    out.normalized_key = cached.get("normalized_key") or make_reference_key(out)
    out.title = cached.get("title") or out.title
    out.authors = list(cached.get("authors") or out.authors)
    out.year = cached.get("year") or out.year
    return out
