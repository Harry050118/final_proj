# Trace: Related Work Generation for Paper 07794 (HiPRAG)

## Paper Inference

**Topic:** Hierarchical process rewards for efficient agentic Retrieval-Augmented Generation (RAG).
**Task:** Training LLM search agents to avoid over-search and under-search behaviors via reinforcement learning.
**Method:** HiPRAG — decomposes reasoning trajectories into parsable steps, detects over-search and under-search on-the-fly using external LLM judges, and applies a hierarchical reward function that gates a process bonus (proportional to optimal step ratio) behind format and answer correctness.
**Contribution:** A fine-grained, knowledge-grounded process reward for RL-based agentic RAG training that explicitly evaluates each search/non-search decision, plus an efficient detection mechanism for suboptimal search behaviors.

## DeepXiv Status

**Result: Inaccessible.** The domain `deepxiv.org` does not resolve (confirmed via nslookup against both local DNS and Google DNS 8.8.8.8). All URL patterns attempted returned connection failures:
- `https://api.deepxiv.org/v1/search`
- `https://deepxiv.org/api/search`
- `https://www.deepxiv.org/api/search`
- `https://api.deepxiv.com/v1/search`
- `https://deepxiv.ai/api/v1/search`
- `https://deepxiv.app/api/v1/search`
- `https://api.deepxiv.xyz/v1/search`

Token from `.env`: `DEEPXIV_API_TOKEN=sniRmhNSA2A2UVETupSomuV_eqv9c5flac8LCj0F6A8`

## Alternative Verification Methods

Since DeepXiv was inaccessible, papers were verified through direct web_fetch on:
- arXiv abstract pages (by known/plausible arxiv IDs)
- GitHub repository pages (HiPRAG, Search-R1, Search-o1 repos)
- GitHub code search for R1-Searcher

General web search was not available (SearXNG not configured).

## Verified Papers (with confirmation source)

| # | Paper | Verification |
|---|-------|-------------|
| [1] | RAG (Lewis et al., 2020) | arxiv:2005.11401 — confirmed via web_fetch |
| [2] | ReAct (Yao et al., 2022) | arxiv:2210.03629 — confirmed via web_fetch |
| [3] | IRCoT (Trivedi et al., 2022) | arxiv:2212.10509 — confirmed via web_fetch |
| [4] | Toolformer (Schick et al., 2023) | arxiv:2302.04761 — confirmed via web_fetch |
| [5] | Self-RAG (Asai et al., 2023) | arxiv:2310.11511 — confirmed via web_fetch |
| [6] | Search-o1 (Li et al., 2025) | arxiv:2501.05366 — confirmed via web_fetch; GitHub repo at RUC-NLPIR/Search-o1 |
| [7] | Search-R1 (Jin et al., 2025) | arxiv:2503.09516 — confirmed via web_fetch; GitHub repo at PeterGriffinJin/Search-R1 |
| [10] | AutoSearch (Sun et al., 2026) | arxiv:2604.17337 — confirmed via web_fetch; identified from previous run memory as the paper matching β-GRPO |
| [11] | DeepSeek-R1 (DeepSeek-AI, 2025) | arxiv:2501.12948 — confirmed via web_fetch |
| [12] | DeepSeekMath/GRPO (Shao et al., 2024) | arxiv:2402.03300 — confirmed via web_fetch |

## Papers with Limited Verification

| # | Paper | Issue |
|---|-------|-------|
| [8] | R1-Searcher | Title confirmed via GitHub search ("Incentivizing the Search Capability in LLMs via Reinforcement Learning"). Authors and arxiv ID could not be independently verified. Included because explicitly named and described as a baseline in the paper body text. |
| [9] | R1-Searcher++ | Title confirmed via GitHub search ("Incentivizing the Dynamic Knowledge Acquisition of LLMs via Reinforcement Learning"). Authors and arxiv ID could not be independently verified. Same rationale as [8]. |

## Note on β-GRPO / AutoSearch

The paper body text refers to a baseline as "β-GRPO". Previous session memory indicates DeepXiv resolved this to "AutoSearch: Adaptive Search Depth for Efficient Agentic RAG via Reinforcement Learning" (arxiv:2604.17337, Sun et al., 2026). This paper's abstract confirms its relevance (adaptive search depth, self-answering mechanism, penalizing over-search). The reference entry uses the verified title "AutoSearch" rather than the paper body's notation "β-GRPO".

## Search Queries Attempted

- DeepXiv API: `agentic+RAG+reinforcement+learning`, `test` (all failed — domain not found)
- GitHub: HiPRAG repo → confirmed paper metadata; Search-R1 repo → confirmed framework; GitHub search for "R1-Searcher" → confirmed titles
- arXiv direct access: Successfully verified 10 papers via known/plausible arxiv IDs

## Papers Not Included

- **DPR (Karpukhin et al., 2020, arxiv:2004.04906)**: Verified but not directly relevant to agentic search behavior — cited in paper body for retrieval setup, not for method contribution.
- **Search-R1 Empirical Study (Jin et al., 2025, arxiv:2505.15117)**: Verified but represents a companion analysis of the same framework, not a distinct method.
- **Chain-of-Thought (Wei et al., 2022, arxiv:2201.11903)**: Verified but represents general reasoning prompting, not specific to search/retrieval behavior.

## Topic Structure Rationale

Three themes were chosen to progressively build context from foundational RAG work to the specific gap HiPRAG addresses:
1. **Agentic RAG** — establishes the evolution from static retrieval to autonomous search agents
2. **RL for Search Agent Training** — positions HiPRAG against the most directly comparable baselines
3. **Process Rewards and Search Efficiency** — identifies the specific gap (lack of fine-grained, step-level feedback) that HiPRAG fills

Following lessons from previous run: avoided standalone RL background paragraph, avoided citing dataset papers for method claims, and distinguished prompting-based from RL-trained approaches.

## Uncertainty

- R1-Searcher [8] and R1-Searcher++ [9] author/venue metadata could not be independently verified. Titles are from GitHub search results.
- β-GRPO/AutoSearch mapping is from previous session memory, not direct confirmation.
- Some author lists for papers with many co-authors used "et al." after the first few names.
