---
name: openclaw-related-work-eval
description: Use when evaluating OpenClaw on Related Work generation, citation reliability, DeepXiv-assisted academic search, Clean/Noisy/Misleading conditions, or the final_proj 3x3 experiment protocol.
---

# OpenClaw Related Work Evaluation

Use this skill for the `final_proj` OpenClaw citation reliability experiment. The authoritative local protocols are:

- `docs/paper_input_protocol.md`
- `docs/experiment_protocol.md`
- `docs/annotation_guideline.md`
- `docs/repo_structure.md`

## Core Rules

- Do not modify OpenClaw internals.
- Use the same anonymized input for all conditions for a paper.
- Never search for removed titles, DOI, arXiv IDs, reference lists, figure captions, or complete paper identifiers.
- Use DeepXiv as the preferred academic retrieval tool when available.
- Save the complete run trace: prompt, query, candidate papers, screening table, final citations, Related Work output, and annotation notes.
- For A2/A3, the OpenClaw prompt may include only candidate paper metadata: title, authors, year/venue, abstract, URL/DOI/arXiv ID. Do not reveal hidden labels such as `noisy`, `misleading`, `irrelevant`, or the human rejection reason.

## Prompt Assembly

Build each run as:

```text
Base Prompt + Input Condition Prompt (A1/A2/A3) + Comparison Group Prompt (B1/B2/B3)
```

Use:

- Base: `prompts/base_prompt.txt`
- A1: `prompts/input_A1_clean_search.txt`
- A2: `prompts/input_A2_noisy_search.txt`
- A3: `prompts/input_A3_misleading_search.txt`
- B1: `prompts/comparison_B1_no_intervention.txt`
- B2: `prompts/comparison_B2_generic_writing.txt`
- B3: `prompts/comparison_B3_citation_grounding.txt`

Do not improvise or rewrite prompt modules during a run. If a prompt must change, create a new versioned file and record the version in the run log.

The 3x3 matrix is:

```text
A1+B1, A1+B2, A1+B3
A2+B1, A2+B2, A2+B3
A3+B1, A3+B2, A3+B3
```

## DeepXiv Workflow

1. Infer the paper topic, task, method, dataset type, and contribution from the anonymized body.
2. Generate conservative academic queries.
3. Search DeepXiv for each query and record returned candidates.
4. Screen candidates as `relevant`, `weakly relevant`, or `irrelevant`.
5. Use only `relevant` papers for core Related Work claims.
6. Treat `weakly relevant` papers as peripheral only.
7. Exclude `irrelevant` papers from citations.

## Run Logging

Start from `runs/RUN_TEMPLATE.md`. Store logs under:

- A1 Clean Search: `runs/clean_search/`
- A2 Noisy Search: `runs/noisy_search/`
- A3 Misleading Search: `runs/misleading_search/`

Every run log must include:

- Paper ID and input condition.
- Comparison group.
- Prompt/workflow version.
- Search queries and purposes.
- Candidate papers with source URLs or IDs.
- Final cited papers.
- Generated Related Work.
- Citation reliability annotations.

## Annotation

Use `docs/annotation_guideline.md` for scoring. Track:

- Irrelevant Citation Rate
- Misleading Citation Adoption Rate
- Unsupported Claim Count
- Core Argument Contamination
- Error labels such as `wrong-topic citation`, `weakly-related overuse`, `invented citation`, and `unsupported claim`
