## Run Metadata
- Date: 2026-05-28
- Search source: DeepXiv only

## Paper Profile
- Topic: Agentic Retrieval-Augmented Generation (RAG) with Reinforcement Learning
- Task: Optimizing search behavior in agentic RAG systems — reducing over-search and under-search
- Method: HiPRAG — Hierarchical Process Rewards with structured output format, on-the-fly over-search/under-search detection via external LLM, and a hierarchical reward function gating process bonus behind format and answer correctness
- Data type / benchmark: QA benchmarks — NQ, HotpotQA, PopQA, TriviaQA, 2WikiMultiHopQA, Bamboogle, MuSiQue
- Evaluation focus: Accuracy (Cover Exact Match) and search efficiency (Over-search Rate, Under-search Rate)
- Main contribution: A fine-grained, knowledge-grounded process reward framework that provides step-specific feedback on each search decision, decomposing trajectories into parsable steps and evaluating the necessity of each search action on-the-fly
- Boundaries: Not about general RAG architecture design, retrieval index optimization, math/code reasoning process rewards, or non-agentic single-step RAG

## Visible Related Work Headings
- No explicit Related Work section headings in the visible text. All related work discussion is embedded in the Introduction. Themes inferred from introduction content.

## Visible Coverage Ledger
| Visible signal | Signal type | Exact recovery query | DeepXiv recovery status | Planned use | Final disposition |
|---|---|---|---|---|---|
| RAG foundations (Lewis et al.) | field background | "Lewis retrieval augmented generation knowledge intensive NLP tasks 2020" | Found (2005.11401) | Theme 1 | covered |
| Prompt-based multi-step RAG (IRCoT) | named works | "IRCoT interleaving retrieval chain-of-thought reasoning multi-step QA" | Found (2212.10509) | Theme 1 | covered |
| Self-RAG (adaptive retrieval) | named works | "Self-RAG self-reflective retrieval augmented generation knowledge boundary" | Found (2310.11511) | Theme 1 | covered |
| Search-o1 (agentic search) | named works | "Search-o1 agentic retrieval augmented generation multi-step reasoning" | Found (2501.05366) | Theme 1 | covered |
| DeepSeek-R1 (RL reasoning) | field background | "DeepSeek-R1 reinforcement learning reasoning LLM GRPO verifiable reward" | Found (2501.12948) | Theme 2 | covered |
| Search-R1 (RL-based agentic RAG) | named works | "Search-R1 reinforcement learning search agent retrieval augmented generation" | Found (2503.09516) | Theme 2 | covered |
| R1-Searcher | named works | "Search-R1 reinforcement learning search agent retrieval augmented generation" | Found (2503.05592) | Theme 2 | covered |
| R1-Searcher++ | named works | "Search-R1 reinforcement learning search agent retrieval augmented generation" | Found (2505.17005) | Theme 2 | covered |
| ReSearch | named works | "ReSearch learning to reason with search for LLMs via reinforcement learning" | Found (2503.19470) | Theme 2 | covered |
| β-GRPO / Search Wisely | named works | "beta-GRPO search agent efficiency retrieval reinforcement learning" | Found (2505.17281) | Theme 3 | covered |
| Process supervision (Lightman) | field background | "Lightman process supervision math reasoning step by step verifier PRM" | Found (2305.20050) | Theme 3 | covered |
| DecEx-RAG (process supervision for RAG) | named works | "agentic retrieval augmented generation reinforcement learning search efficiency process reward" | Found (2510.05691) | Theme 3 | covered |
| ReasonRAG (process rewards) | named works | "agentic retrieval augmented generation reinforcement learning search efficiency process reward" | Found (2505.14069) | Theme 3 | covered |
| ProRAG (process-supervised RL for RAG) | named works | "process reward model reinforcement learning LLM reasoning step-level feedback" | Found (2601.21912) | Theme 3 | covered |
| s3 (data-efficient search agent RL) | named works | "Search-R1 reinforcement learning search agent retrieval augmented generation LLM" | Found (2505.14146) | Not cited | intentionally omitted (data-efficiency focus, less central to search behavior optimization) |
| AutoSearch (adaptive search depth) | named works | "agentic retrieval augmented generation reinforcement learning search efficiency process reward" | Found (2604.17337) | Not cited | intentionally omitted (overlaps with β-GRPO conceptually; budget constraint) |
| Coarse outcome-based rewards | target motivation | n/a | N/A | Theme 2-3 gap statement | covered (uncited target motivation bridging sentence) |
| Length/retrieval-times-based penalties | field background | n/a | Covered indirectly via β-GRPO | Theme 3 | narrowed (described as confidence-threshold-based rather than length-based) |
| Over-search and under-search definition | target motivation | n/a | N/A | Theme 3 | covered (Wu et al. [11] formally defines these) |

## Must-Not-Drop Signals
| Signal | Source heading/theme | Required handling | Final status |
|---|---|---|---|
| Search-R1 | Introduction / RL agentic RAG | Must cite | covered [6] |
| R1-Searcher / R1-Searcher++ | Introduction / baselines | Must cite | covered [7], [8] |
| β-GRPO | Introduction / search efficiency | Must cite | covered [11] |
| IRCoT | Introduction / prompt-based agentic RAG | Must cite | covered [2] |
| Search-o1 | Introduction / prompt-based agentic RAG | Must cite | covered [4] |
| Process supervision (Lightman) | Introduction / process reward context | Must cite | covered [10] |
| Over-search and under-search problem definition | Introduction / problem statement | Must cover | covered [11] |
| Outcome-based reward limitations | Introduction / gap | Must cover | covered (target motivation) |
| Fine-grained process reward gap | Introduction / contribution | Must cover | covered (target motivation) |

## Search Queries
| Query | Purpose | Source |
|---|---|---|
| "agentic retrieval augmented generation reinforcement learning search efficiency process reward" | Broad discovery | Theme 1-3 |
| "Search-R1 reinforcement learning search agent retrieval augmented generation LLM" | Exact recovery | Baselines |
| "process reward model reinforcement learning LLM reasoning step-level feedback" | Field background discovery | Theme 3 |
| "IRCoT interleaving retrieval chain-of-thought reasoning multi-step QA" | Exact recovery | Baselines |
| "Search-o1 agentic retrieval augmented generation multi-step reasoning search" | Exact recovery | Baselines |
| "GRPO group relative policy optimization LLM reinforcement learning" | Background | RL algorithm context |
| "beta-GRPO search agent efficiency retrieval reinforcement learning" | Exact recovery | Baselines |
| "retrieval augmented generation RAG survey large language model knowledge grounding" | Background | Theme 1 |
| "PPO proximal policy optimization reinforcement learning human feedback LLM fine-tuning" | Background | RL context |
| "Lewis retrieval augmented generation knowledge intensive NLP tasks 2020" | Exact recovery | Theme 1 |
| "Self-RAG self-reflective retrieval augmented generation knowledge boundary reflection" | Exact recovery | Theme 1 |
| "DeepSeek-R1 reinforcement learning reasoning LLM GRPO verifiable reward" | Exact recovery | Theme 2 |
| "adaptive retrieval when to retrieve LLM knowledge boundary selective retrieval" | Background | Theme 1 |
| "ReST meets ReAct self-taught reasoner search agent LLM tool use iterative reasoning" | Background | Agentic RAG context |
| "ReAct reasoning acting language model interleaving thought action observation tool" | Background | Agentic RAG context |
| "FLARE active retrieval augmented generation forward-looking iterative retrieval LLM" | Background | Adaptive retrieval |
| "Lightman process supervision math reasoning step by step verifier PRM process reward model" | Exact recovery | Theme 3 |
| "ReSearch learning to reason with search for LLMs via reinforcement learning" | Discovery | Theme 2 |

## Candidate Screening
| Title | Authors | Year | Source | Label | Reason |
|---|---|---|---|---|---|
| AutoSearch | Sun et al. | 2026 | arXiv:2604.17337 | weakly relevant | Adaptive search depth via RL; overlaps with β-GRPO; budget constraint; not cited |
| HiPRAG | (target paper) | 2025 | arXiv:2510.07794 | N/A | Target paper — not citation material |
| Graph-R1 | - | 2025 | arXiv:2507.21892 | irrelevant | GraphRAG, not agentic search behavior optimization |
| APEX-Searcher | - | 2026 | arXiv:2603.13853 | weakly relevant | Agentic planning and execution; recent; budget constraint |
| DecEx-RAG | Leng et al. | 2025 | arXiv:2510.05691 | relevant | Process supervision for agentic RAG; cited [12] |
| Search Wisely (β-GRPO) | Wu et al. | 2025 | arXiv:2505.17281 | relevant | Directly relevant — over-search/under-search, β-GRPO; cited [11] |
| Process vs Outcome Reward (ReasonRAG) | Zhang et al. | 2025 | arXiv:2505.14069 | relevant | Process-supervised RL for RAG; cited [13] |
| s3 | - | 2025 | arXiv:2505.14146 | weakly relevant | Data-efficient search agent RL; less central to search behavior optimization; not cited |
| DynaSearcher | - | 2025 | arXiv:2507.17365 | irrelevant | KG-augmented search, not process reward focus |
| TeaRAG | - | 2025 | arXiv:2511.05385 | weakly relevant | Token-efficient RAG; not centered on search behavior; not cited |
| ProRAG | Wang et al. | 2026 | arXiv:2601.21912 | relevant | Process-supervised RL for RAG with PRM; cited [14] |
| Search-R1 | Jin et al. | 2025 | arXiv:2503.09516 | relevant | Core RL-based agentic RAG baseline; cited [6] |
| RAG-R1 | - | 2025 | arXiv:2507.02962 | weakly relevant | Multi-query parallelism; less focused on process rewards; not cited |
| R1-Searcher | Song et al. | 2025 | arXiv:2503.05592 | relevant | Two-stage RL for search; cited [7] |
| R1-Searcher++ | Song et al. | 2025 | arXiv:2505.17005 | relevant | Dynamic knowledge acquisition; cited [8] |
| SE-Search | - | 2026 | arXiv:2603.03293 | weakly relevant | Self-evolving search; budget constraint; not cited |
| ReSearch | Chen et al. | 2025 | arXiv:2503.19470 | relevant | RL-trained search with GRPO; cited [9] |
| IRCoT | Trivedi et al. | 2022 | arXiv:2212.10509 | relevant | Prompt-based multi-step RAG; cited [2] |
| Search-o1 | Li et al. | 2025 | arXiv:2501.05366 | relevant | Agentic search-enhanced reasoning; cited [4] |
| Self-RAG | Asai et al. | 2023 | arXiv:2310.11511 | relevant | Adaptive retrieval via reflection tokens; cited [3] |
| RAG (Lewis) | Lewis et al. | 2020 | arXiv:2005.11401 | relevant | Foundational RAG; cited [1] |
| Let's Verify Step by Step | Lightman et al. | 2023 | arXiv:2305.20050 | relevant | Process supervision in math reasoning; cited [10] |
| DeepSeek-R1 | Guo et al. | 2025 | arXiv:2501.12948 | relevant | RL for reasoning capability; cited [5] |

## Planned Themes
| Theme | Input signal it maps to | Core/context citations | Notes |
|---|---|---|---|
| Retrieval-Augmented Generation and Agentic RAG | RAG foundations, prompt-based multi-step RAG, adaptive retrieval | [1] Lewis, [2] IRCoT, [3] Self-RAG, [4] Search-o1 | Covers one-step RAG → multi-step agentic RAG evolution |
| Reinforcement Learning for Search Agents | RL-based agentic RAG, DeepSeek-R1 context | [5] DeepSeek-R1, [6] Search-R1, [7] R1-Searcher, [8] R1-Searcher++, [9] ReSearch | Covers outcome-based RL training for search agents |
| Process Rewards and Search Efficiency Optimization | Process supervision, search efficiency, β-GRPO, DecEx-RAG, ReasonRAG, ProRAG | [10] Lightman, [11] β-GRPO, [12] DecEx-RAG, [13] ReasonRAG, [14] ProRAG | Covers process-level rewards for improving search behavior |

## Coverage Allocation
| Heading/theme | Recoverable named/background signals | Covered in final text | Unresolved gaps |
|---|---|---|---|
| Theme 1: RAG and Agentic RAG | 4 (Lewis, IRCoT, Self-RAG, Search-o1) | 4/4 | None |
| Theme 2: RL for Search Agents | 5 (DeepSeek-R1, Search-R1, R1-Searcher, R1-Searcher++, ReSearch) | 5/5 | None |
| Theme 3: Process Rewards and Efficiency | 5 (Lightman, β-GRPO, DecEx-RAG, ReasonRAG, ProRAG) | 5/5 | None |

## Length Control
- Target word budget: 450-650 (focused method paper, 12-18 budget with three themes)
- Estimated visible Related Work length: N/A (no explicit Related Work section)
- Final word count: ~520 words
- Status: Within target range

## Final Cited Papers
| # | Title | Authors | Year | Source | Citation role |
|---|---|---|---|---|---|
| [1] | RAG for Knowledge-Intensive NLP Tasks | Lewis et al. | 2020 | arXiv:2005.11401 | Foundational RAG |
| [2] | IRCoT | Trivedi et al. | 2022 | arXiv:2212.10509 | Prompt-based multi-step RAG |
| [3] | Self-RAG | Asai et al. | 2023 | arXiv:2310.11511 | Adaptive retrieval |
| [4] | Search-o1 | Li et al. | 2025 | arXiv:2501.05366 | Agentic search in reasoning models |
| [5] | DeepSeek-R1 | Guo et al. | 2025 | arXiv:2501.12948 | RL for reasoning context |
| [6] | Search-R1 | Jin et al. | 2025 | arXiv:2503.09516 | Core RL-based agentic RAG |
| [7] | R1-Searcher | Song et al. | 2025 | arXiv:2503.05592 | Two-stage RL for search |
| [8] | R1-Searcher++ | Song et al. | 2025 | arXiv:2505.17005 | Dynamic knowledge switching |
| [9] | ReSearch | Chen et al. | 2025 | arXiv:2503.19470 | RL search with GRPO |
| [10] | Let's Verify Step by Step | Lightman et al. | 2023 | arXiv:2305.20050 | Process supervision context |
| [11] | Search Wisely (β-GRPO) | Wu et al. | 2025 | arXiv:2505.17281 | Over/under-search definition, confidence-based RL |
| [12] | DecEx-RAG | Leng et al. | 2025 | arXiv:2510.05691 | Process-supervised MDP for RAG |
| [13] | ReasonRAG | Zhang et al. | 2025 | arXiv:2505.14069 | MCTS-based process rewards |
| [14] | ProRAG | Wang et al. | 2026 | arXiv:2601.21912 | Process-supervised RL with PRM |

## Claim-Citation Self-Check
| Citation | Claim | Supported? | Action | Notes |
|---|---|---|---|---|
| [1] | RAG addresses static parametric knowledge limitations | Supported | keep | Verified via abstract |
| [2] | IRCoT interleaves retrieval with CoT reasoning | Supported | keep | Verified via abstract |
| [3] | Self-RAG uses reflection tokens for on-demand retrieval | Supported | keep | Verified via abstract |
| [4] | Search-o1 triggers retrieval when uncertainty detected | Supported | keep | Verified via abstract |
| [5] | DeepSeek-R1 demonstrates RL-elicited reasoning | Supported | keep | Verified via abstract |
| [6] | Search-R1 trains LLMs to interleave reasoning with search via outcome reward | Supported | keep | Verified via abstract |
| [7] | R1-Searcher uses two-stage RL for retrieval invocation | Supported | keep | Verified via abstract |
| [8] | R1-Searcher++ incorporates memory and internal knowledge reward | Supported | keep | Verified via abstract |
| [9] | ReSearch treats search as component of reasoning chain via GRPO | Supported | keep | Verified via abstract |
| [10] | Process supervision outperforms outcome supervision in math | Supported | keep | Verified via abstract |
| [11] | β-GRPO formally defines over-search/under-search, uses confidence thresholds | Supported | keep | Verified via abstract |
| [12] | DecEx-RAG models RAG as MDP with process-level supervision | Supported | keep | Verified via abstract |
| [13] | ReasonRAG uses MCTS for process-level preference data | Supported | keep | Verified via abstract |
| [14] | ProRAG uses MCTS-based PRM with dual-granularity advantage | Supported | keep | Verified via abstract |
| Target-paper motivation | Outcome-based rewards lack fine-grained search decision feedback | Target-paper interpretation | keep | Phrased as target motivation |
| Target-paper motivation | Learned reward models/confidence heuristics may imperfectly capture search necessity | Target-paper interpretation | keep | Phrased as target motivation |

## Citation Ledger
| Citation string | Matching paper | In Related Work? | In Final References? | In Self-Check? | Scope |
|---|---|---|---|---|---|
| [1] | Lewis et al. 2020 | Yes | Yes | Yes | Theme 1 |
| [2] | Trivedi et al. 2022 | Yes | Yes | Yes | Theme 1 |
| [3] | Asai et al. 2023 | Yes | Yes | Yes | Theme 1 |
| [4] | Li et al. 2025 | Yes | Yes | Yes | Theme 1 |
| [5] | Guo et al. 2025 | Yes | Yes | Yes | Theme 2 |
| [6] | Jin et al. 2025 | Yes | Yes | Yes | Theme 2 |
| [7] | Song et al. 2025 | Yes | Yes | Yes | Theme 2 |
| [8] | Song et al. 2025 | Yes | Yes | Yes | Theme 2 |
| [9] | Chen et al. 2025 | Yes | Yes | Yes | Theme 2 |
| [10] | Lightman et al. 2023 | Yes | Yes | Yes | Theme 3 |
| [11] | Wu et al. 2025 | Yes | Yes | Yes | Theme 3 |
| [12] | Leng et al. 2025 | Yes | Yes | Yes | Theme 3 |
| [13] | Zhang et al. 2025 | Yes | Yes | Yes | Theme 3 |
| [14] | Wang et al. 2026 | Yes | Yes | Yes | Theme 3 |

## Completion Status
| Gate | Status |
|---|---|
| RWEval Citation Format | ✓ Numeric citations, matching numbered references |
| Read the Visible Input | ✓ Full anonymized body text inspected |
| Visible Heading Preservation | N/A — no explicit Related Work headings |
| Visible Coverage Ledger | ✓ All signals have final disposition |
| Coverage Allocation | ✓ Each theme covers ≥2 signals |
| Missing-Point Prevention | ✓ All 9 must-not-drop signals covered |
| Named Citation Exactness | ✓ All visible named works verified via DeepXiv |
| Reference Validity Guard | ✓ All 14 final citations have stable metadata |
| Length Control | ✓ ~520 words within 450-650 target |
| Dynamic Citation Budget | ✓ 14 citations within 12-18 budget |
| Final Consistency | ✓ All citations present in both text and references |

## Benchmark-Specific Deny / Handle List
| Paper or pattern | Reason | Handling | Theme preserved by |
|---|---|---|---|
| MARG (D'Arcy et al., arXiv:2401.04259) | Known metadata_mismatch in benchmark | Not cited, not mentioned | N/A — not visible in input |

## Uncertain Points
- The target paper mentions "length or retrieval times-based penalties" in prior work without naming specific papers. β-GRPO [11] is cited as the closest match (confidence-based rather than length-based), but the specific length-penalty work is not independently identified through DeepXiv.
- The target paper mentions "model confidence and knowledge awareness" incorporated into rewards. β-GRPO [11] covers this via confidence thresholds. Other confidence-aware methods (e.g., SUGAR, Self-Routing RAG) were found but considered less central to the RL-based search agent training context.
