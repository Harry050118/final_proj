# Trace for 07794 Related Work Generation

## Search Queries Used
1. "agentic retrieval-augmented generation reinforcement learning search agent"
2. "Search-R1 reinforcement learning retrieval agent"
3. "process reward model reinforcement learning reasoning LLM"
4. "over-search under-search retrieval efficiency agentic RAG"
5. "GRPO PPO reinforcement learning large language model training"
6. "multi-hop question answering retrieval HotpotQA Musique"
7. "beta-GRPO R1-Searcher++ retrieval efficiency reinforcement learning"
8. "outcome reward reinforcement learning reasoning sparse reward dense reward"
9. "chain-of-thought reasoning interleaving retrieval multi-step QA"
10. "IRCoT iterative retrieval chain of thought multi-hop"
11. "Natural Questions TriviaQA PopQA open-domain question answering benchmark"
12. "reward shaping knowledge awareness retrieval decision LLM"
13. "self-knowledge LLM know what it knows retrieval decision confidence"
14. "Search-o1 prompting agentic search multi-step reasoning"
15. "Bamboogle 2WikiMultiHopQA multi-hop question answering dataset"
16. "PopQA entity-centric question answering probing factual knowledge"
17. "E5 text embedding retrieval dense passage retriever"
18. "verifiable reward outcome-based reward reasoning LLM RL training"

## Main Candidate Papers Considered
- Search-R1 (2503.09516) — cited [5]
- R1-Searcher (2503.05592) — cited [6]
- R1-Searcher++ (2505.17005) — cited [7]
- Search Wisely / beta-GRPO (2505.17281) — cited [13]
- PRIME / Process Reinforcement through Implicit Rewards (2502.01456) — cited [10]
- VERITAS / Beyond Correctness (2510.13272) — cited [11]
- Search-P1 (2602.22576) — cited [12]
- AutoSearch (2604.17337) — cited [14]
- DeepRAG (2502.01142) — cited [15]
- IRCoT (2212.10509) — cited [3]
- ReAct (not arXiv, ICLR 2023) — cited [4]
- HotpotQA (1809.09600) — cited [17]
- MuSiQue (2108.00573) — cited [18]
- TriviaQA (1705.03551) — cited [19]
- Natural Questions (TACL 2019) — cited [20]
- E5 (2212.03533) — cited [21]
- DPR / Dense Passage Retrieval (2004.04906) — cited [2]
- PPO (arXiv:1707.06347) — cited [8]
- Process reward modeling (Uesato et al. 2022) — cited [9]
- RAG original (Lewis et al. NeurIPS 2020) — cited [1]
- LLM Knowledge Boundary (2307.11019) — cited [16]

## Final Cited Papers (22 references)
[1] Lewis et al. RAG (NeurIPS 2020)
[2] Karpukhin et al. DPR (EMNLP 2020)
[3] Trivedi et al. IRCoT (arXiv 2022)
[4] Yao et al. ReAct (ICLR 2023)
[5] Jin et al. Search-R1 (arXiv 2025)
[6] Zhang et al. R1-Searcher (arXiv 2025)
[7] Zhang et al. R1-Searcher++ (arXiv 2025)
[8] Schulman et al. PPO (arXiv 2017)
[9] Uesato et al. Process- and Outcome-Based Feedback (arXiv 2022)
[10] Yuan et al. PRIME (arXiv 2025)
[11] Chen et al. VERITAS (arXiv 2025)
[12] Li et al. Search-P1 (arXiv 2026)
[13] Zhang et al. Search Wisely / beta-GRPO (arXiv 2025)
[14] Sun et al. AutoSearch (arXiv 2026)
[15] Guo et al. DeepRAG (arXiv 2025)
[16] Dong et al. LLM Knowledge Boundary (arXiv 2023)
[17] Yang et al. HotpotQA (EMNLP 2018)
[18] Trivedi et al. MuSiQue (ACL 2022)
[19] Joshi et al. TriviaQA (ACL 2017)
[20] Kwiatkowski et al. Natural Questions (TACL 2019)
[21] Wang et al. E5 (arXiv 2022)

## Uncertainties and Notes
- The exact authors for some cited works (ReAct, RAG, PPO, process reward modeling) were inferred from well-known publications rather than retrieved directly from DeepXiv. These are standard, widely-cited works in the field.
- PopQA and Bamboogle datasets are mentioned in the paper body but not cited separately, as they are secondary evaluation datasets compared to HotpotQA, MuSiQue, TriviaQA, and Natural Questions.
- The E5-base retriever mentioned in the paper body is cited via the E5 paper (Wang et al. 2022), which includes the base variant.
- GRPO is discussed in the paper but not cited as a separate reference, as it is primarily a methodological detail (RL algorithm) rather than a core contribution of the related work.
- No attempt was made to find the exact arXiv ID for Natural Questions (published in TACL, not arXiv), so it is cited via its original venue.
- The paper mentions Search-o1 as a baseline; this was considered but not included in the final related work because it is primarily a prompting-based method and less central to the RL training methodology focus of the paper.
