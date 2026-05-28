---
name: openclaw-related-work-eval
description: Use when writing Related Work from a paper body, abstract, research idea, anonymized input, or candidate literature list, especially when citation reliability, DeepXiv-only retrieval, RWEval-ready output, or claim-citation grounding matters.
---

# Related Work Grounding

## Purpose

Use this skill to write a reliable, RWEval-ready Related Work section. The priority order is:

1. Cover the prior-work signals visible in the input.
2. Verify every final citation through DeepXiv.
3. Attach citations only to claims they directly support.
4. Keep the output clean enough for `s_text.txt` and `s_reference.txt`.

This skill is not for full-paper writing, experiments, Introduction, Discussion, or generic polishing unless the user explicitly asks to focus on Related Work.

## Inputs And Outputs

When the user provides an output directory, write:

- `s_text.txt`: only the generated Related Work section.
- `s_reference.txt`: final cited paper list, one entry per cited paper, with title, authors, year, and DeepXiv/arXiv/URL metadata when available.
- `trace.md` (optional): audit trail for queries, screening, themes, citations, self-checks, and unresolved gaps.

RWEval citation format gate:

- For RWEval files, use numeric citations in `s_text.txt`, such as `[1]` or `[2, 3]`.
- Number `s_reference.txt` with the same labels, such as `[1] ...`.
- Do not use BibTeX-style keys such as `\cite{reddy2024}` in `s_text.txt` unless `s_reference.txt` is a complete BibTeX bibliography with exactly matching keys.
- Prefer numeric citations for all project evaluation runs.

Do not write `g_text.txt` or `g_reference.txt`. Do not read `papers/ground_truth_related_work/`, `g_text.txt`, `g_reference.txt`, or any ground-truth Related Work file during generation. Ground truth is only for the evaluator after the run.

If no output directory is provided for an evaluation run, ask for one. For a quick draft, return the Related Work and a brief trace in the conversation.

## Hard Rules

- Use DeepXiv as the only academic retrieval source.
- Do not use web search, arXiv search, Google Scholar, Semantic Scholar, DBLP, ACL Anthology, PubMed, ACM, IEEE, publisher search, or memory-only citations as substitutes.
- If DeepXiv is unavailable or evidence is insufficient, stop and report the retrieval problem instead of falling back.
- Do not search for removed identifiers such as hidden title, DOI, arXiv ID, reference list, figure captions, table captions, or complete paper identifiers.
- Do not invent papers, authors, venues, datasets, numeric results, comparisons, or experimental claims.
- Do not cite a paper because it only shares keywords with the target work.
- Do not use target-paper experimental results, ablations, hardware/runtime details, percentage improvements, or superiority claims in the paper profile, screening, citation roles, Related Work, or self-check.
- Every in-text citation must appear in `s_reference.txt`; every `s_reference.txt` entry must be cited in `s_text.txt`.

## Workflow

### 1. Read The Visible Input

First inspect the full visible input, not only the abstract or introduction.

Extract a paper profile:

- Topic and application area.
- Task or research problem.
- Method, model, system, or intervention.
- Dataset, data type, benchmark, or empirical setting.
- Evaluation focus.
- Main contribution, stated without measured results or superiority.
- Boundaries: what the paper does not claim or evaluate.

Then explicitly check for a visible `Related Work`, `RELATED WORK`, `Background`, or equivalent LaTeX section. If present, extract its paragraph headings and named citations. Do not claim the Related Work section is absent unless the complete visible input has been checked.

### 2. Build A Coverage Scaffold

Create a `Visible Coverage Scaffold` before searching. It is a search-and-structure guide, not citation evidence.

Capture:

- Named authors, systems, benchmarks, datasets, and methods.
- Method families, task functions, and application areas.
- Historical or field-background signals.
- Publishing, peer-review, evaluation, reward-model, and LLM-as-judge signals.
- Stated gaps or motivations that connect prior work to the target contribution.

For each planned heading, keep a lightweight scaffold with only these signal types:

- `named works`: visible author-year citations, named systems, benchmarks, datasets, or methods.
- `field background`: visible historical context, application areas, taxonomies, broad trends, or field-level challenges.
- `target motivation`: the target paper's stated gap, positioning, or contribution hook.

Use this scaffold to guide writing, but do not turn it into a hard coverage checklist. If a named work cannot be recovered through DeepXiv, record the gap and avoid forcing a weak substitute into the final citations.

If a visible Related Work section has 2-4 headings, those headings define the default planned themes. For example, do not merge separate visible headings such as `LLMs for Research`, `LLMs for Science Discovery`, and `Automated Evaluation of Research Papers` into one theme.

### 3. Search With DeepXiv

Run exact recovery before broad discovery:

- For visible author-year signals, query the author surname plus visible task phrase or likely title words.
- For visible systems or benchmarks, query the exact name plus the task phrase.
- For visible method families, query the method phrase plus the target domain.

Examples of exact recovery intent:

- Baek + `ResearchAgent` or iterative research idea generation.
- Yang + automated open-domain scientific hypothesis discovery or retrieval for idea generation.
- Wang + automated survey writing or scientific literature retrieval.
- Huang + MLAgentBench or ML experimentation benchmark.
- Langley + computational scientific discovery.
- RewardBench + reward model evaluation.
- Generative Reward Model / GenRM + next-token prediction reward modeling.

Do not mark a named citation as covered using a different-author substitute. A substitute may be cited only as adjacent context after the named work is recorded as `Gap` or `Not found`.

For agent, test-time learning, self-improvement, or evolutionary-system papers, attempt canonical family searches only when those families are actually relevant to the visible input. Otherwise mark seed coverage as not applicable.

### 4. Screen Candidates

Classify each candidate before citing it:

| Label | Meaning | Allowed use |
|---|---|---|
| `relevant` | Directly supports a visible theme, task, method, benchmark, comparison, or gap. | Core Related Work claims. |
| `weakly relevant` | Supports historical, taxonomy, adjacent-task, benchmark, or context only. | Peripheral/context sentences with narrow wording. |
| `irrelevant` | Superficial keyword overlap, wrong task, wrong method, wrong source, or cannot support a planned sentence. | Do not cite. |

Apply a reference validity guard before final citation:

- Keep only records with internally consistent title, authors, year, and identifier.
- Do not final-cite records with missing authors, conflicting metadata, uncertain title matches, or likely RWEval metadata mismatch.
- Do not final-cite papers that have already triggered `metadata_mismatch` in this project. In the current benchmark, `MARG: Multi-Agent Review Generation for Scientific Papers` / D'Arcy et al. / `arXiv:2401.04259` must be `screened only` or an `Uncertain Point`, not a final citation.
- Prefer omitting an unstable paper over risking a hallucinated or metadata-mismatch reference.

Apply a claim-type guard before writing from a candidate:

| Candidate type | Safe claim scope |
|---|---|
| `benchmark` | Benchmark scope, evaluation target, task/domain, and dataset shape when directly supported. |
| `survey` | Taxonomy, field trend, broad context, and stated open challenges. |
| `method` | Method mechanism, training/inference setup, claimed task setting, and directly stated empirical scope. |
| `system` | System capability, workflow, components, and reported setting. |

Comparative or superiority claims require direct DeepXiv evidence. If the evidence only supports context, rewrite the sentence as target-paper motivation or remove the comparison.

For benchmark comparisons, apply an extra guard:

- Benchmark papers do not by themselves support claims that one model family, training regime, or evaluator type outperforms another.
- Claims like `task-specific models outperform general-purpose models`, `A beats B`, or `trained reward models outperform LLM judges` require direct DeepXiv TLDR/abstract evidence for that exact comparison and task setting.
- If the evidence only establishes a benchmark or evaluation framework, write that it motivates task-specific evaluation or reward modeling rather than reporting a comparative result.

### 5. Plan Themes

Use 2-4 planned themes.

If a visible Related Work section has 2-4 headings, mirror them unless DeepXiv cannot verify any usable citation for a heading. If a heading has weak evidence, keep it with narrow verified context rather than deleting it.

Benchmark/environment papers should not become standalone themes unless the target paper is itself a benchmark/environment paper or the visible Related Work makes evaluation the central topic. Otherwise, mention them briefly inside the relevant theme.

Use the active citation budget:

- `8-12` final cited papers for focused method-paper Related Work with no broad visible scaffold.
- `12-18` final cited papers when the visible input clearly covers three or more broad themes.

Use the smaller `8-12` budget by default when the candidate pool is mostly weakly relevant, broad background, or unstable. Use `12-18` only when the visible input itself clearly has multiple themes and enough directly relevant, metadata-stable candidates to support them.

Write the active budget and the reason in `trace.md`. Do not invent other budget ranges.

### 6. Write Related Work

Write by theme, not by search result order.

Use compact synthesis:

- One paragraph per planned theme when possible.
- Every Related Work body paragraph should include at least one citation. If a paragraph only contains target-paper motivation or contribution, merge it into the previous relevant paragraph instead of leaving it as a standalone uncited paragraph.
- Multi-citation sentences for broad context.
- Specific citations attached to specific claims.
- Narrow wording for context citations.
- For each broad planned theme, cover at least two of the lightweight scaffold signal types when evidence permits: named works, field background, and target motivation.
- For Science Discovery context, prefer visible-background claims such as Langley, LeCun, AI4Science, and the shift from passive data analysis to active discovery. If DeepXiv cannot recover stable metadata for older or non-arXiv works, record the citation gap in `trace.md` instead of padding with unstable substitute surveys.
- For Automated Evaluation context, prefer stable citations such as Robertson, Liu/Shah, RewardBench, GenRM, and Paper SEA. Do not final-cite MARG in this benchmark because it has triggered `metadata_mismatch`.
- For missing named lines such as Hosseini & Horbach or Lu/Tyser full-PDF evaluation, use narrow wording only when needed for coverage and record the unresolved DeepXiv gap. Do not invent a citation.
- No unsupported claims such as `first`, `state-of-the-art`, `outperforms`, or universal `prior work fails to...` unless directly verified.

Each theme may end with at most one target motivation sentence. This sentence can describe the target paper's gap, contribution, or positioning without a prior-work citation, but it must be phrased as target-paper motivation rather than cited prior-work evidence.

If a limitation is the target paper's own positioning rather than the cited paper's claim, phrase it as motivation: `This motivates the target paper's move toward...` rather than stating the limitation as an objective fact.

### 7. Self-Check And Finalize

Before finalizing, check:

- Every citation-claim pair is supported, partially supported with narrowed wording, or removed.
- Every in-text citation exactly matches one final reference entry.
- Every final reference entry appears in the Related Work.
- Every self-check citation appears in the final reference list, unless marked `screened only`.
- No weakly relevant paper supports a core claim.
- No target-paper result is used as prior-work evidence.
- No unstable DeepXiv metadata remains in final citations.
- Every comparative claim is directly supported by the cited paper's DeepXiv evidence, or has been rewritten as target-paper motivation.
- Every target-paper motivation sentence is uncited or clearly separated from the prior-work citation it follows.
- No Related Work body paragraph is left without an in-text citation unless it has been merged into a cited paragraph.
- If a final self-check would label a citation-claim pair as `weak` or `Partially supported`, first narrow the claim. If narrowing still requires an inference chain beyond the retrieved evidence, rewrite the sentence as target-paper motivation or remove it.

Final self-check labels must be:

- `Supported`
- `Partially supported`
- `Unsupported`
- `Target-paper interpretation`

Final actions must be only `keep` or `resolved`; apply `narrow`, `remove`, or `move to motivation` before final output.

## Evaluation-Aware Gates

Use these gates for RWEval-oriented runs:

- `RWEval Citation Format`: `s_text.txt` uses numeric citations that map directly to numbered `s_reference.txt` entries.
- `Read the Visible Input`: full input checked for a Related Work section before scaffold construction.
- `Visible Heading Preservation`: visible 2-4 Related Work headings are mirrored as planned themes.
- `Named Citation Exactness`: author-year signals are searched exactly before substitutes are considered.
- `Reference Validity Guard`: metadata-unstable papers are not final-cited.
- `Dynamic Citation Budget`: active budget is exactly `8-12` or `12-18`.
- `Final Consistency`: in-text citations, final references, self-check, and trace ledger agree.

If any gate fails, mark final status as `incomplete with usable RWEval output` in `trace.md`. Do not claim success while unresolved gaps, screened-only metadata mismatch papers, or named-citation gaps remain.

## Trace Template

Use this structure for `trace.md` when an audit trail is requested:

```markdown
## Run Metadata
- Date:
- Search source: DeepXiv only

## Paper Profile
- Topic:
- Task:
- Method:
- Data type / benchmark:
- Evaluation focus:
- Main contribution:
- Boundaries:

## Visible Related Work Headings
| Heading | Extracted coverage signals | Planned theme |
|---|---|---|

## Visible Coverage Scaffold
| Visible signal | Signal type | Exact recovery query | DeepXiv recovery status | Planned use |
|---|---|---|---|---|

## Search Queries
| Query | Purpose | Source |
|---|---|---|

## Candidate Screening
| Title | Authors | Year | Source | Label | Reason |
|---|---|---:|---|---|---|

## Planned Themes
| Theme | Input signal it maps to | Core/context citations | Notes |
|---|---|---|---|

## Final Cited Papers
| Title | Authors | Year | Source | Citation role |
|---|---|---:|---|---|

## Claim-Citation Self-Check
| Citation | Claim | Supported? | Action | Notes |
|---|---|---|---|---|

## Citation Ledger
| Citation string | Matching paper | In Related Work? | In Final References? | In Self-Check / Uncertain Points? | Scope |
|---|---|---|---|---|---|

## Completion Status
| Gate | Status |
|---|---|

## Uncertain Points
-
```

## Candidate Lists

If the user provides candidate papers, treat them as candidates, not endorsements. Screen them like search results.

The evaluated prompt may include only bibliographic/content metadata:

- Title.
- Authors.
- Year or venue.
- Abstract.
- URL, DOI, arXiv ID, or source page.

Do not expose hidden labels such as `noisy`, `misleading`, `irrelevant`, or private rejection reasons to the evaluated model.

## Optional Evaluation Mode

Use this mode only when evaluating whether the workflow improves citation reliability.

- A2/A3 noisy or misleading candidate sets are stress tests for rejecting irrelevant or superficially related papers.
- B1 and B2 are baselines, not this skill's default behavior.
- The citation-grounding workflow is the default behavior of this skill.

Track:

- Irrelevant Citation Rate.
- Misleading Citation Adoption Rate.
- Unsupported Claim Count.
- Core Argument Contamination.
- Error labels: `wrong-topic citation`, `weakly-related overuse`, `invented citation`, `metadata_mismatch`, `unsupported claim`, `over-specific claim`.
