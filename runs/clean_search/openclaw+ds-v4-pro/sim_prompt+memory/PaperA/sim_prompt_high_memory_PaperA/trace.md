# Trace: Related Work Generation for Paper 07794 (HiPRAG)

## 1. Paper Topic Inference

From the anonymized body text, I inferred the following:

- **Research Topic:** Hierarchical process rewards for efficient agentic Retrieval-Augmented Generation (RAG) via reinforcement learning.
- **Task:** Training LLMs to autonomously decide when to search and what to retrieve during multi-step reasoning, while minimizing over-search and under-search.
- **Method:** HiPRAG — a hierarchical process reward framework that (1) decomposes agent reasoning trajectories into structured, parsable steps, (2) detects over-search and under-search on-the-fly using external LLM verification, and (3) applies a gated hierarchical reward (format + outcome + process bonus) via PPO or GRPO.
- **Dataset type:** Knowledge-intensive question answering (single-hop and multi-hop), including NQ, HotpotQA, PopQA, TriviaQA, 2WikiMultiHopQA, Bamboogle, MuSiQue.
- **Contribution:** Fine-grained, step-specific process rewards for agentic RAG search behavior; on-the-fly over-search/under-search detection; hierarchical reward gating that prioritizes correctness before incentivizing efficiency.

## 2. DeepXiv Search Attempts

DeepXiv API endpoint: `https://deepxiv.com/api/search` (POST, JSON)

**Authentication attempts (all returned `{"error":"Not authenticated"}`):**
- `Authorization: Bearer <token>`
- `X-API-Key: <token>`
- `api-key: <token>`
- `x-api-key: <token>`
- `apikey: <token>`
- `Authorization: Key <token>`
- `Authorization: ApiKey <token>`
- Token in cookie: `next-auth.session-token`, `__Secure-next-auth.session-token`, `session`, `token`
- Token in request body: `{"token":"..."}`, `{"apiKey":"..."}`
- Token as query parameter: `?token=...`

**Other endpoints attempted:**
- `https://deepxiv.com/api/v1/search` → 404
- `https://deepxiv.com/api/chat` → 404
- `https://deepxiv.com/api/auth/session` → 404
- `https://deepxiv.com/api/auth/login` → 404
- `https://deepxiv.com/api/auth/callback/credentials` → 404
- GET `https://deepxiv.com/api/search?q=...` → empty response

**HTTP variant:**
- `http://deepxiv.com/api/search` → empty response

**Status:** DeepXiv search API is inaccessible. The endpoint responds with "Not authenticated" for all authentication methods attempted with the token from `.env`. Discovery search could not be performed.

## 3. Papers Considered

### Papers from anonymized body text (explicitly named):
- Search-R1 (RL-based agentic RAG baseline)
- R1-Searcher (RL-based search agent)
- R1-Searcher++ (efficiency-focused RL baseline)
- β-GRPO (efficiency-focused RL baseline, resolves to AutoSearch)
- IRCoT (prompting-based agentic RAG)
- Search-o1 (prompting-based agentic RAG)
- PPO (RL algorithm)
- GRPO (RL algorithm, from DeepSeekMath)

### Papers from previous run evaluations (verified by DeepXiv evaluator):
- R1-Searcher: arxiv:2503.05592, authors confirmed (Song et al.)
- R1-Searcher++: arxiv:2505.17005, authors confirmed (Song et al.)
- AutoSearch (β-GRPO): arxiv:2604.17337, authors unconfirmed

### Papers NOT included (cannot verify without search):
- ReAct (Yao et al., 2022) — expected by gold standard but not mentioned in body text
- Self-RAG (Asai et al., 2023) — same
- Toolformer (Schick et al., 2023) — same
- Chain-of-Retrieval / DeepRAG — discovered missing in previous Run 2 evaluation
- RAG-RL, ToolRL, ToRL — discovered missing in previous Run 2 evaluation
- ReARTeR, SMART, SMARTCAL — discovered missing in previous Run 2 evaluation
- Let's Verify Step by Step — had wrong arxiv ID in Run 1, not verified
- Verifiable stepwise rewards — discovered missing in previous Run 2 evaluation

## 4. Final Cited Papers (8 references)

| # | Paper | Verification Status |
|---|-------|-------------------|
| [1] | IRCoT (Trivedi et al., ACL 2023) | Metadata from memory; widely known paper |
| [2] | Search-o1 (Li et al., arXiv:2501.05366, 2025) | arXiv ID from memory; title confirmed from body text |
| [3] | Search-R1 (Feng et al., 2025) | Metadata from memory; named in body text |
| [4] | AutoSearch / β-GRPO (arXiv:2604.17337, 2025) | arXiv ID verified by DeepXiv evaluator in previous Run 2 |
| [5] | R1-Searcher (Song et al., arXiv:2503.05592, 2025) | arXiv ID + authors verified by DeepXiv evaluator in Run 2 |
| [6] | R1-Searcher++ (Song et al., arXiv:2505.17005, 2025) | arXiv ID + authors verified by DeepXiv evaluator in Run 2 |
| [7] | PPO (Schulman et al., arXiv:1707.06347, 2017) | Well-known canonical reference |
| [8] | GRPO / DeepSeekMath (Shao et al., arXiv:2402.03300, 2024) | Well-known canonical reference |

## 5. Uncertainty and Limitations

### Critical limitation: No search performed
DeepXiv API search could not be authenticated despite exhaustive attempts with all standard auth methods. This means:
1. **No discovery search was performed.** Papers not mentioned in the body text could not be found.
2. **Reference metadata for [1], [2], [3] is unverified.** Authors, titles, and arxiv IDs for IRCoT, Search-o1, and Search-R1 come from training knowledge / memory, not from DeepXiv search verification. These could contain errors.
3. **Expected but missing papers** (from previous evaluation gold standard): ReAct, Self-RAG, Toolformer, Chain-of-Retrieval, DeepRAG, RAG-RL, ToolRL, ToRL, ReARTeR, SMART/SMARTCAL, verifiable stepwise rewards. These could not be included because they are not named in the anonymized body text and DeepXiv discovery was unavailable.

### Metadata confidence levels:
- **High confidence:** [4] AutoSearch, [5] R1-Searcher, [6] R1-Searcher++ (verified by DeepXiv evaluator in Run 2)
- **High confidence:** [7] PPO, [8] GRPO/DeepSeekMath (well-known, canonical papers)
- **Medium confidence:** [1] IRCoT, [2] Search-o1 (well-known papers, metadata from training knowledge)
- **Lower confidence:** [3] Search-R1 (recent 2025 paper, less consensus on exact metadata)

### Thematic structure:
Organized by functional concern rather than methodology type, following the lesson from Run 2:
- S1: Agentic RAG (enabling agentic retrieval)
- S2: Efficient search behavior (addressing search inefficiency)
- S3: Process-level supervision and RL training (reward design)

### Writing decisions based on lessons:
- No standalone general RL paragraph (Run 1 error)
- No dataset papers cited for method claims (Run 1 error)
- Promising vs. RL methods clearly distinguished (Run 1 error)
- Each distinct work has its own reference (Run 1 error)
- No absolute language about training regimes (Run 2 lesson)
- Identified inefficiency as an explicit research dimension (Run 2 lesson)
- No fabricated reference entries (Run 1 error: β-GRPO was verified as AutoSearch)
