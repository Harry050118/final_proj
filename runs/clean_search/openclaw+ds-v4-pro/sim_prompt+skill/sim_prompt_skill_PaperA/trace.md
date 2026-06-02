## Run Metadata
- Date: 2026-05-28
- Search source: DeepXiv only
- Input: papers/07794.txt (HiPRAG - Hierarchical Process Rewards for Efficient Agentic RAG)
- Output dir: runs/clean_search/sim_prompt+skill/07794

## Paper Profile
- Topic: Agentic Retrieval-Augmented Generation (RAG) systems with reinforcement learning training
- Task: Training LLMs to make optimal search decisions (when to search vs. use parametric knowledge) in agentic RAG
- Method: HiPRAG — hierarchical, knowledge-aware process reward framework that decomposes reasoning trajectories into parsable steps, detects over-search and under-search on-the-fly via external LLM verification, and provides a gated process bonus proportional to optimal step ratio
- Data type / benchmark: Seven QA benchmarks — NQ, PopQA, TriviaQA, 2WikiMultiHopQA, Bamboogle, HotpotQA, MuSiQue
- Evaluation focus: Accuracy (Cover Exact Match), search efficiency (Over-search Rate OSR, Under-search Rate USR)
- Main contribution: Hierarchical process reward for RL training of agentic RAG that provides fine-grained, step-specific feedback on retrieval decisions, gated behind format and answer correctness
- Boundaries: Focuses on training methodology for agentic RAG; does not propose new retrieval methods, architectures, or search engines; uses rule-based parsing + external LLM for detection rather than learned reward models

## Visible Related Work Headings
| Heading | Extracted coverage signals | Planned theme |
|---|---|---|
| (No explicit Related Work section in paper) | N/A — prior work discussion embedded in Introduction and baseline taxonomy | Themes constructed from Introduction's prior-work narrative |

## Visible Coverage Ledger
| Visible signal | Signal type | Exact recovery query | DeepXiv recovery status | Planned use | Final disposition |
|---|---|---|---|---|---|
| Search-R1 | named works | "Search-R1 agentic RAG reinforcement learning search agent reasoning" | Found: 2503.09516 | Core citation in RL-based agentic RAG theme | covered |
| R1-Searcher | named works | "R1-Searcher reinforcement learning retrieval-augmented generation search efficiency" | Found: 2503.05592 | Core citation in RL-based agentic RAG theme | covered |
| R1-Searcher++ | named works | "R1-Searcher++ reinforcement learning search agent efficiency retrieval" | Found: 2505.17005 | Core citation in RL-based agentic RAG theme | covered |
| β-GRPO | named works | "beta-GRPO retrieval-augmented generation search behavior" → found as "Search Wisely": 2505.17281 | Found: 2505.17281 | Core citation for over/under-search quantification and confidence-based reward | covered |
| IRCoT | named works | "IRCoT interleaving retrieval chain-of-thought reasoning multi-step QA" | Found: 2212.10509 | Prompt-based agentic RAG context | covered |
| Search-o1 | named works | "Search-o1 agentic search large reasoning model knowledge insufficiency retrieval" | Found: 2501.05366 | Prompt-based agentic RAG context | covered |
| PPO | named works (RL algorithm) | Not separately cited (widely known algorithm) | N/A | Mentioned as common RL algorithm, no separate citation needed | intentionally omitted (common knowledge) |
| GRPO | named works (RL algorithm) | "DeepSeek-R1 GRPO Shao" → referenced via DeepSeek-R1: 2501.12948 | Found: 2501.12948 | Context via DeepSeek-R1 | covered (via [9]) |
| Qwen2.5, Llama-3.2 | named works (models) | Not separately cited | N/A | Model families, not prior work | intentionally omitted (infrastructure) |
| E5-base, Wikipedia 2018 | named works (infrastructure) | Not separately cited | N/A | Infrastructure, not prior work | intentionally omitted (infrastructure) |
| NQ, HotpotQA, PopQA, TriviaQA, 2WikiMultiHopQA, Bamboogle, MuSiQue | named works (datasets) | Not separately cited | N/A | Evaluation benchmarks, not theoretical prior work | intentionally omitted (evaluation benchmarks) |
| Agentic RAG evolution | field background | Multiple queries for RAG, IRCoT, Search-o1 | Found | Theme 1: From static RAG to agentic search | covered |
| RL for LLM training | field background | DeepSeek-R1, RLHF survey | Found | Theme 2/3 context | covered |
| Process reward models | field background | "Let's Verify Step by Step" | Found: 2305.20050 | Theme 3 | covered |
| Over-search/under-search problem | field background | β-GRPO / Search Wisely query | Found | Theme 2/3 context | covered |
| Length/retrieval penalties | field background | General observation in prior work | Not separately cited | Noted in text as general approach | intentionally omitted (general observation, not a specific paper) |
| Model confidence and knowledge awareness | field background | Covered through β-GRPO | Found | Theme 2 | covered |
| Lack of fine-grained step-specific feedback | target motivation | N/A (target paper's own positioning) | N/A | Motivation sentence, uncited | covered (as motivation) |
| Suboptimal search behaviors (over-search, under-search) | target motivation | β-GRPO provides quantification | Found | Motivation + supported claim via [7] | covered |
| Standard RAG (Lewis et al.) | field background | "retrieval-augmented generation RAG Lewis" | Found: 2005.11401 | Foundational context | covered |
| RL-based Agentic Search survey | field background | "reinforcement learning retrieval-augmented generation survey LLM search agent" | Found: 2510.16724 | Broad context/taxonomy | covered |

## Must-Not-Drop Signals
| Signal | Source heading/theme | Required handling | Final status |
|---|---|---|---|
| Search-R1 | RL-based agentic RAG baselines | Must cite with exact metadata | covered: [4] |
| R1-Searcher | RL-based agentic RAG baselines | Must cite with exact metadata | covered: [5] |
| R1-Searcher++ | RL-based agentic RAG baselines (efficiency-focused) | Must cite with exact metadata | covered: [6] |
| β-GRPO | RL-based agentic RAG baselines (efficiency-focused) | Must cite with exact metadata | covered: [7] |
| IRCoT | Prompt-based agentic RAG | Must cite with exact metadata | covered: [2] |
| Search-o1 | Prompt-based agentic RAG | Must cite with exact metadata | covered: [3] |
| Process supervision (Lightman) | Process reward context | Must cite | covered: [8] |
| DeepSeek-R1 / GRPO | RL training paradigm | Must cite | covered: [9] |
| Over-search/under-search problem | Central challenge | Must describe with evidence | covered via [7] |
| Fine-grained step-level feedback gap | Target motivation | Must articulate as uncited motivation | covered as motivation |

## Search Queries
| Query | Purpose | Source |
|---|---|---|
| "Search-R1 agentic RAG reinforcement learning search agent reasoning" | Exact recovery of Search-R1 | Named baseline |
| "R1-Searcher reinforcement learning retrieval-augmented generation search efficiency" | Exact recovery of R1-Searcher | Named baseline |
| "R1-Searcher++ reinforcement learning search agent efficiency retrieval" | Exact recovery of R1-Searcher++ | Named baseline |
| "β-GRPO search efficiency agentic RAG reinforcement learning" | Exact recovery of β-GRPO | Named baseline |
| "IRCoT interleaving retrieval chain-of-thought reasoning multi-step QA" | Exact recovery of IRCoT | Named baseline |
| "Search-o1 agentic search large reasoning model knowledge insufficiency retrieval" | Exact recovery of Search-o1 | Named baseline |
| "GRPO group relative policy optimization LLM training reinforcement learning" | GRPO algorithm context | Field background |
| "beta-GRPO retrieval-augmented generation search behavior reinforcement learning" | β-GRPO full title recovery | Named baseline |
| "Search Wisely sub-optimal agentic searches uncertainty retrieval RAG" | Confirm β-GRPO = Search Wisely | Named baseline |
| "process reward model LLM training reinforcement learning step-level supervision" | Process reward context | Field background |
| "agentic RAG over-search under-search efficiency retrieval behavior optimization" | Over/under-search context | Field background |
| "DeepSeek-R1 GRPO Shao Zhihong reinforcement learning reasoning" | GRPO/RL context | Field background |
| "retrieval-augmented generation RAG Lewis language model knowledge intensive NLP" | Foundational RAG | Field background |
| "PPO proximal policy optimization LLM fine-tuning RLHF" | PPO algorithm context | Field background |
| "GRPO DeepSeek-R1 Shao group relative policy optimization reasoning" | DeepSeek-R1 paper | Field background |
| "process reward model step-level verification LLM reasoning PRM ORM" | Process reward specifics | Field background |
| "reinforcement learning retrieval-augmented generation survey LLM search agent training" | Survey paper | Field background |
| "beta GRPO suboptimal search mitigation agentic retrieval uncertainty reduction" | Confirming β-GRPO | Named baseline |

## Candidate Screening
| Title | Authors | Year | Source | Label | Reason |
|---|---|---|---:|---|---|
| Search-R1: Training LLMs to Reason and Leverage Search Engines with RL | Jin et al. | 2025 | 2503.09516 | relevant | Core RL-based agentic RAG framework; direct baseline |
| R1-Searcher: Incentivizing the Search Capability in LLMs via RL | Song et al. | 2025 | 2503.05592 | relevant | RL-based search agent training; direct baseline |
| R1-Searcher++: Incentivizing the Dynamic Knowledge Acquisition of LLMs via RL | Song et al. | 2025 | 2505.17005 | relevant | Efficiency-focused RL-based agent; direct baseline |
| Search Wisely (β-GRPO) | Wu et al. | 2025 | 2505.17281 | relevant | Over/under-search quantification, confidence-based reward; direct baseline |
| Search-o1: Agentic Search-Enhanced Large Reasoning Models | Li et al. | 2025 | 2501.05366 | relevant | Prompt-based agentic RAG; direct baseline |
| IRCoT: Interleaving Retrieval with CoT Reasoning | Trivedi et al. | 2022 | 2212.10509 | relevant | Foundational prompt-based multi-step retrieval; direct baseline |
| RAG for Knowledge-Intensive NLP Tasks | Lewis et al. | 2020 | 2005.11401 | relevant | Foundational RAG paradigm |
| Let's Verify Step by Step | Lightman et al. | 2023 | 2305.20050 | relevant | Process supervision vs outcome supervision; context for process reward |
| DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL | DeepSeek-AI | 2025 | 2501.12948 | relevant | GRPO + RL for LLM reasoning; field context |
| Survey on RL-based Agentic Search | Lin et al. | 2025 | 2510.16724 | weakly relevant | Survey provides taxonomy and broad context |
| s3: You Don't Need That Much Data to Train a Search Agent via RL | Jiang et al. | 2025 | 2505.14146 | weakly relevant | Adjacent RL-based search agent work; not included in final budget |
| AutoSearch: Adaptive Search Depth for Efficient Agentic RAG | N/A | 2025 | 2604.17337 | irrelevant | 0 citations, not a named baseline in target paper |
| HiPRAG (target paper) | N/A | 2025 | 2510.07794 | screened only | Target paper; not for citation |
| COSEARCH: Joint Training of Reasoning and Document Ranking | N/A | 2025 | 2604.17555 | irrelevant | 0 citations, not directly relevant to search behavior optimization |
| RAG-Gym | N/A | 2025 | 2502.13957 | irrelevant | Different focus (optimization framework for agentic RAG), not a named baseline |
| RLHF survey | Kaufmann et al. | 2023 | 2312.14925 | weakly relevant | RL context; not included (DeepSeek-R1 covers RL paradigm) |

## Planned Themes
| Theme | Input signal it maps to | Core/context citations | Notes |
|---|---|---|---|
| From Static RAG to Agentic Search | Introduction: agentic RAG evolution, prompt-based methods | [1] Lewis, [2] IRCoT, [3] Search-o1 | Covers evolution from single-turn RAG → interleaved retrieval → agentic search workflow |
| Reinforcement Learning for Search Agents | Introduction: RL-based training, baselines (Search-R1, R1-Searcher, R1-Searcher++, β-GRPO) | [4] Search-R1, [5] R1-Searcher, [6] R1-Searcher++, [7] β-GRPO, [10] survey | Covers RL-based methods that train search decision-making |
| Process Supervision and Fine-Grained Rewards | Introduction: process-level reward limitations, need for fine-grained feedback | [8] Lightman, [9] DeepSeek-R1 | Covers process supervision paradigm and the gap HiPRAG fills |

## Coverage Allocation
| Heading/theme | Recoverable named/background signals | Covered in final text | Unresolved gaps |
|---|---|---|---|
| From Static RAG to Agentic Search | 3 named (Lewis, IRCoT, Search-o1) + field background (RAG evolution) | All 3 named + background covered | None |
| RL for Search Agents | 5 named (Search-R1, R1-Searcher, R1-Searcher++, β-GRPO, survey) + field background (RL training, over/under-search) | All 5 named + background covered | None |
| Process Supervision | 2 named (Lightman, DeepSeek-R1) + target motivation (gap) | All 2 named + motivation covered | None |

## Length Control
- Target word budget: 450-650 (focused method paper with no visible Related Work section)
- Estimated visible Related Work length: N/A (no explicit section)
- Final word count: ~510 words
- Status: within range

## Final Cited Papers
| Title | Authors | Year | Source | Citation role |
|---|---|---:|---|---|
| Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | Lewis et al. | 2020 | 2005.11401 | Foundational RAG paradigm [1] |
| IRCoT: Interleaving Retrieval with CoT Reasoning | Trivedi et al. | 2022 | 2212.10509 | Prompt-based multi-step retrieval [2] |
| Search-o1: Agentic Search-Enhanced Large Reasoning Models | Li et al. | 2025 | 2501.05366 | Prompt-based agentic search workflow [3] |
| Search-R1: Training LLMs to Reason and Leverage Search Engines with RL | Jin et al. | 2025 | 2503.09516 | Core RL-based agentic RAG [4] |
| R1-Searcher: Incentivizing the Search Capability in LLMs via RL | Song et al. | 2025 | 2503.05592 | RL-based search agent [5] |
| R1-Searcher++: Incentivizing Dynamic Knowledge Acquisition via RL | Song et al. | 2025 | 2505.17005 | Efficiency-focused RL agent [6] |
| Search Wisely: Mitigating Sub-optimal Agentic Searches (β-GRPO) | Wu et al. | 2025 | 2505.17281 | Over/under-search quantification + confidence reward [7] |
| Let's Verify Step by Step | Lightman et al. | 2023 | 2305.20050 | Process vs outcome supervision [8] |
| DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL | DeepSeek-AI | 2025 | 2501.12948 | GRPO + RL for LLM reasoning [9] |
| Survey on RL-based Agentic Search | Lin et al. | 2025 | 2510.16724 | Field taxonomy [10] |

## Claim-Citation Self-Check
| Citation | Claim | Supported? | Action | Notes |
|---|---|---|---|---|
| [1] | RAG introduced as framework for grounding LLM outputs in external knowledge, combining parametric and non-parametric memory | Supported | keep | Directly from abstract |
| [2] | IRCoT interleaves retrieval with CoT reasoning, using retrieved results to guide subsequent reasoning | Supported | keep | Directly from abstract |
| [3] | Search-o1 integrates agentic search workflow, enabling dynamic retrieval at uncertainty points, with document refinement | Supported | keep | Directly from abstract |
| [4] | Search-R1 uses RL to train LLMs for multi-turn search during reasoning, outcome-based rewards, retrieved-token masking | Supported | keep | Directly from abstract |
| [5] | R1-Searcher proposes two-stage outcome-based RL, no process rewards or cold start | Supported | keep | Directly from abstract |
| [6] | R1-Searcher++ introduces dynamic knowledge acquisition, balances internal/external knowledge | Supported | keep | Directly from abstract |
| [7] | β-GRPO quantifies over/under-search, incorporates confidence thresholds into RL reward | Supported | keep | Directly from abstract |
| [8] | Process reward models provide step-level feedback, outperform outcome supervision for math reasoning | Supported | keep | Directly from abstract |
| [9] | DeepSeek-R1 uses GRPO to elicit reasoning behaviors via large-scale RL | Supported | keep | Directly from abstract |
| [10] | Survey provides taxonomy of RL-based agentic search methods | Supported | keep | From metadata/title |
| Motivation (uncited) | Prompting methods don't train search decision mechanism | Target-paper interpretation | keep | Target-paper positioning |
| Motivation (uncited) | RL methods rely on outcome rewards or coarse proxies, no step-level feedback | Target-paper interpretation | keep | Synthesized from prior work limitations discussed in target paper intro |
| Motivation (uncited) | Adapting process supervision to agentic retrieval faces parsing and proxy bias challenges | Target-paper interpretation | keep | Target-paper gap articulation |
| Motivation (uncited) | Need for fine-grained, knowledge-grounded feedback on each search decision | Target-paper interpretation | keep | Target-paper motivation |

## Citation Ledger
| Citation string | Matching paper | In Related Work? | In Final References? | In Self-Check / Uncertain Points? | Scope |
|---|---|---|---|---|---|
| [1] | Lewis et al. 2020 | Yes | Yes | Yes | Broad context |
| [2] | Trivedi et al. 2022 | Yes | Yes | Yes | Core |
| [3] | Li et al. 2025 | Yes | Yes | Yes | Core |
| [4] | Jin et al. 2025 | Yes | Yes | Yes | Core |
| [5] | Song et al. 2025a | Yes | Yes | Yes | Core |
| [6] | Song et al. 2025b | Yes | Yes | Yes | Core |
| [7] | Wu et al. 2025 | Yes | Yes | Yes | Core |
| [8] | Lightman et al. 2023 | Yes | Yes | Yes | Context |
| [9] | DeepSeek-AI 2025 | Yes | Yes | Yes | Context |
| [10] | Lin et al. 2025 | Yes | Yes | Yes | Context/survey |

## Completion Status
| Gate | Status |
|---|---|
| RWEval Citation Format | ✅ Numeric [1]-[10], matching s_reference.txt |
| Read the Visible Input | ✅ Full paper read; no visible Related Work section |
| Visible Heading Preservation | ✅ N/A — no visible Related Work section; themes from Introduction |
| Visible Coverage Ledger | ✅ All signals have final disposition |
| Coverage Allocation | ✅ All themes cover ≥2 named/background signals |
| Missing-Point Prevention | ✅ All 10 must-not-drop signals covered |
| Named Citation Exactness | ✅ All named works recovered via exact-queried DeepXiv search |
| Reference Validity Guard | ✅ All papers have verified metadata (title, authors, year, arXiv ID) |
| Length Control | ✅ ~510 words within 450-650 budget |
| Dynamic Citation Budget | ✅ 10 citations (active budget 8-12 for focused method paper) |
| Final Consistency | ✅ All in-text citations in references, all references cited, self-check consistent |

## Benchmark-Specific Deny / Handle List
| Paper or pattern | Reason | Handling | Theme preserved by |
|---|---|---|---|
| MARG: Multi-Agent Review Generation / D'Arcy et al. / 2401.04259 | Known metadata_mismatch in benchmark | Screened only; not final-cited | N/A (MARG not in visible input signals) |

## Uncertain Points
- β-GRPO was recovered under the title "Search Wisely: Mitigating Sub-optimal Agentic Searches By Reducing Uncertainty" (2505.17281). The paper mentions β-GRPO by its algorithm name in the target paper, while DeepXiv uses the full title. This is confirmed as the same work.
- The target paper discusses "length or retrieval times-based penalties" as a class of prior approaches. No single canonical paper was identified for this technique; treated as a general observation rather than a named citation.
- No visible Related Work section exists in the target paper. Themes were constructed from the Introduction's prior-work narrative and the baseline taxonomy in Section 4.2.
- The target paper's Introduction mentions "model confidence and knowledge awareness incorporated into the reward" without naming specific papers beyond those in baselines. This is covered via β-GRPO [7].
