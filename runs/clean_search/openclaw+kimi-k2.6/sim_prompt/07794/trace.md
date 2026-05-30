# Trace for 07794 Related Work Generation

## Inferred Paper Profile
- **Topic:** Agentic Retrieval-Augmented Generation (RAG) trained with Reinforcement Learning
- **Task:** Multi-step question answering (single-hop and multi-hop) with autonomous search decisions
- **Method:** HiPRAG — a hierarchical process reward framework that decomposes reasoning trajectories into parsable steps, detects over-search/under-search on-the-fly via an external LLM judge, and applies a gated process bonus on top of outcome and format rewards
- **Dataset type:** QA benchmarks (NQ, HotpotQA, PopQA, TriviaQA, 2WikiMultiHopQA, Bamboogle, MuSiQue)
- **Contribution:** Fine-grained process-level supervision for search agents; dramatically reduces over-search (27% -> 2.3%) and under-search while improving accuracy; generalizes across model families (Qwen2.5, Llama-3.2), sizes (3B, 7B), RL algorithms (PPO, GRPO), and model types (base, instruct)

## Search Queries Executed
1. `agentic retrieval-augmented generation reinforcement learning search agent` — 15 results
2. `Search-R1 reinforcement learning retrieval-augmented generation` — 10 results
3. `process reward reinforcement learning large language model reasoning` — 10 results
4. `R1-Searcher reinforcement learning retrieval efficiency` — 10 results
5. `beta-GRPO retrieval-augmented generation search efficiency` — 10 results
6. `over-search under-search retrieval-augmented generation agent` — 10 results
7. `GRPO group relative policy optimization large language model` — 10 results
8. `IRCoT interleaving retrieval chain-of-thought multi-hop reasoning` — 10 results
9. `Search-o1 agentic retrieval-augmented generation` — 10 results

## Candidate Papers Evaluated
| arXiv ID | Title | Relevance | Decision |
|----------|-------|-----------|----------|
| 2407.01219 | Searching for Best Practices in RAG | General RAG survey; useful for foundational context | Cited [1] |
| 2212.10509 | Interleaving Retrieval with Chain-of-Thought Reasoning | Prompt-based agentic RAG baseline mentioned in paper | Cited [2] |
| 2501.05366 | Search-o1: Agentic Search-Enhanced Large Reasoning Models | Prompt-based agentic RAG baseline mentioned in paper | Cited [3] |
| 2503.09516 | Search-R1: Training LLMs to Reason and Leverage Search Engines with RL | Primary baseline; outcome-based RL agentic RAG | Cited [4] |
| 2503.05592 | R1-Searcher: Incentivizing the Search Capability in LLMs via RL | Strong RL baseline for search agents | Cited [5] |
| 2505.17005 | R1-Searcher++: Incentivizing the Dynamic Knowledge Acquisition of LLMs via RL | Efficiency-focused baseline explicitly compared | Cited [6] |
| 2505.14146 | s3: You Don't Need That Much Data to Train a Search Agent via RL | RL search agent with minimal data | Cited [7] |
| 2501.15228 | Improving RAG through Multi-Agent RL | Multi-agent RL for RAG | Cited [8] |
| 2505.17281 | Search Wisely: Mitigating Sub-optimal Agentic Searches By Reducing Uncertainty | Directly addresses over-search/under-search; beta-GRPO baseline | Cited [9] |
| 2604.17337 | AutoSearch: Adaptive Search Depth for Efficient Agentic RAG via RL | Efficiency-focused RL agentic RAG | Cited [10] |
| 2507.02962 | RAG-R1: Incentivizing Search and Reasoning via Multi-query Parallelism | Efficiency-focused agentic RAG | Cited [11] |
| 2510.15719 | Cost-Aware Retrieval-Augmentation Reasoning Models with Adaptive Retrieval Depth | Cost-aware retrieval depth | Cited [12] |
| 2502.01456 | Process Reinforcement through Implicit Rewards (PRIME) | Process reward modeling for reasoning | Cited [13] |
| 2601.10201 | PRL: Process Reward Learning Improves LLMs' Reasoning Ability | Process reward decomposition for reasoning | Cited [14] |
| 2602.22576 | Search-P1: Path-Centric Reward Shaping for Stable and Efficient Agentic RAG Training | Path-level process reward for agentic RAG | Cited [15] |
| 2510.05691 | DecEx-RAG: Boosting Agentic RAG with Decision and Execution Optimization via Process Supervision | Process supervision for agentic RAG | Cited [16] |
| 2510.13272 | Beyond Correctness: Rewarding Faithful Reasoning in RAG | Faithfulness process rewards for agentic RAG | Cited [17] |

## Excluded Candidates
- 2510.16724 (Comprehensive Survey on RL-based Agentic Search): Too broad/survey; not cited to keep focus on specific technical contributions
- 2510.01925 (Reward Models Survey): General survey on reward models; less specific than the process reward papers selected
- 2510.27569 (MARAG-R1): Multi-tool retrieval; less directly relevant to the search efficiency focus
- 2601.17755 (ProGraph-R1): GraphRAG; different retrieval paradigm
- 2509.26383 (Efficient KG-RAG via RL): Knowledge graph RAG; different domain
- 2509.14750 (Enhancing RAG via Adversarial Collaboration): Adversarial focus; not directly relevant
- 2501.08105 (Query Suggestion for RAG via Dynamic ICL): Query suggestion; not directly relevant
- 2603.03293 (SE-Search): Self-evolving search agent with memory; interesting but less directly related
- 2501.11888 (Agentic-R): Learning to retrieve for agentic search; focuses on retriever design rather than search behavior
- 2603.13853 (APEX-Searcher): Agentic planning and execution; broader scope

## Uncertainty Notes
- The paper mentions "beta-GRPO" as a baseline. The search result 2505.17281 (Search Wisely) introduces beta-GRPO and directly addresses over-search/under-search. This is the most likely match.
- The paper mentions "Search-o1" as a baseline. The search result 2501.05366 (Search-o1) is the clear match.
- The paper mentions "IRCoT" as a baseline. The search result 2212.10509 (Interleaving Retrieval with Chain-of-Thought Reasoning) is the clear match.
- Author names for references were not available in the anonymized input; they were obtained from DeepXiv briefs.
- Some papers (e.g., AutoSearch, Search-P1, PRL) have 2026 dates, indicating they are very recent preprints. They are included because they are directly relevant to the themes of process reward and efficiency in agentic RAG.
