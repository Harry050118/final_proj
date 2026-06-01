# Trace: Related Work Generation for Paper 07794 (HiPRAG)

## Inferred Research Topic
- **Topic:** Agentic Retrieval-Augmented Generation (RAG) with Reinforcement Learning
- **Task:** Training LLM-based agents to make optimal search decisions during multi-step reasoning — specifically deciding when to search vs. rely on parametric knowledge
- **Method (HiPRAG):** Hierarchical process reward framework that (1) decomposes reasoning trajectories into parsable XML-structured steps, (2) detects over-search and under-search on-the-fly using external LLM judges, (3) applies a gated hierarchical reward that prioritizes format/answer correctness before adding a process bonus proportional to the ratio of optimal steps
- **Dataset:** Training on NQ + HotpotQA; evaluation on NQ, PopQA, TriviaQA, 2WikiMultiHopQA, Bamboogle, HotpotQA, MuSiQue; Wikipedia 2018 dump with E5-base retriever
- **Key Contribution:** Fine-grained, step-specific process rewards for search agent training that simultaneously reduce over-search (from >27% to 2.3%) and under-search, while improving QA accuracy

## Search Queries Used
1. `agentic retrieval augmented generation reinforcement learning search agent`
2. `reinforcement learning training retrieval-augmented LLM search behavior`
3. `process reward retrieval augmented generation agent`
4. `over-search under-search retrieval agent efficiency`
5. `multi-step reasoning retrieval reinforcement learning language model`
6. `hierarchical process reward language model reinforcement learning`
7. `knowledge boundary aware retrieval language model agent`
8. `Search-R1 training LLMs reason search engines reinforcement learning`
9. `R1-Searcher reinforcement learning retrieval augmented generation`
10. `GRPO group relative policy optimization language model reasoning`
11. `process reward model language model reasoning step by step verification`
12. `iterative retrieval augmented generation multi-hop reasoning interleaving`
13. `adaptive retrieval augmented generation when to retrieve language model`
14. `beta-GRPO search efficiency retrieval augmented generation`
15. `IRCoT interleaving retrieval chain-of-thought reasoning knowledge`
16. `Search-o1 agentic retrieval augmented generation multi-step reasoning`
17. `R1-Searcher++ reinforcement learning search agent`
18. `self-RAG retrieval augmented generation adaptive retrieval`
19. `FLARE active retrieval augmented generation forward-looking`
20. `Toolformer language model tool use API call retrieval`
21. `ReAct reasoning acting language model wikipedia search`
22. `Self-RAG self-reflective retrieval augmented generation language model`
23. `GRPO group relative policy optimization DeepSeek`
24. `knowledge boundary language model knows what it knows retrieval`
25. `uncertainty aware retrieval augmented generation confidence`
26. `DeepSeekMath GRPO group relative policy optimization reinforcement learning`
27. `DeepSeek-R1 reasoning reinforcement learning language model`
28. `process reward model LLM reasoning Lightman math verifier`
29. `Agentic RAG search agent tool use planning reasoning`

## Main Candidate Papers Considered
- 2210.03629 — ReAct (Yao et al., 2022)
- 2302.04761 — Toolformer (Schick et al., 2023)
- 2212.10509 — IRCoT (Trivedi et al., 2022)
- 2310.11511 — Self-RAG (Asai et al., 2023)
- 2305.06983 — Active RAG / FLARE (Jiang et al., 2023)
- 2501.05366 — Search-o1 (Li et al., 2025)
- 2503.09516 — Search-R1 (Jin et al., 2025)
- 2503.05592 — R1-Searcher (Song et al., 2025)
- 2505.17005 — R1-Searcher++ (Song et al., 2025)
- 2507.02962 — RAG-R1 (Tan et al., 2025)
- 2510.05691 — DecEx-RAG (Leng et al., 2025)
- 2510.04695 — Beyond Outcome Reward (Wang et al., 2025)
- 2310.10080 — Let's Reward Step by Step (Ma et al., 2023)
- 2501.12948 — DeepSeek-R1 (Guo et al., 2025)
- 2402.03300 — DeepSeekMath / GRPO (Shao et al., 2024)
- 2505.17281 — Search Wisely (Wu et al., 2025)
- 2602.03304 — To Search or Not to Search (Zhang et al., 2026)
- 2604.17337 — AutoSearch (Sun et al., 2026)
- 2505.12065 — Demystifying and Enhancing Efficiency (Yang et al., 2025)
- 2404.19705 — When to Retrieve (Labruna et al., 2024)
- 2406.19215 — SeaKR (Yao et al., 2024)
- 2411.06207 — KBM (Zhang et al., 2024)
- 2507.17365 — DynaSearcher (Hao et al., 2025)
- 2603.13853 — APEX-Searcher (Chen et al., 2026)
- 2507.21892 — Graph-R1 (Luo et al., 2025)
- 2501.09292 — Uncertainty Detection for Dynamic RAG (Dhole, 2025)
- 2501.12835 — Adaptive Retrieval Without Self-Knowledge (Moskvoretskii et al., 2025)
- 2505.07596 — Reinforced Internal-External Knowledge (Huang et al., 2025)

## Final Cited Papers (22 papers in 4 themes)
1. Agentic RAG: ReAct, Toolformer, IRCoT, Self-RAG, FLARE, Search-o1
2. RL for Agentic Search: Search-R1, R1-Searcher, R1-Searcher++, RAG-R1, DecEx-RAG, Beyond Outcome Reward
3. Process Rewards: Let's Reward Step by Step, DeepSeek-R1, DeepSeekMath (GRPO)
4. Search Efficiency: When to Retrieve, SeaKR, KBM, Search Wisely, To Search or Not to Search, AutoSearch, Demystifying Efficiency

## Uncertainty Notes
- Years for all papers were inferred from arXiv ID prefixes (YYMM format → 20YY) since DeepXiv head/brief API did not return year fields reliably.
- Author lists for DeepSeek-R1, DeepSeekMath, Search-o1, Self-RAG, FLARE, Toolformer, SeaKR, and KBM were partially supplemented from known publication records, as DeepXiv returned truncated or incomplete author lists.
- The specific venue (conference/journal) is not confirmed for most papers; all are listed as arXiv preprints consistent with findings from DeepXiv searches.
- The paper β-GRPO (mentioned in the anonymized body as a baseline) was not found as a distinct arXiv paper through DeepXiv. It may be a variant or configuration of GRPO rather than a standalone paper.
- Search-P1 (arXiv:2602.22576) appeared in one DeepXiv search as relevant to reward shaping for agentic RAG but metadata retrieval failed. It was not included in final citations.
