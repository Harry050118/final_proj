# Trace: Related Work Generation for Paper 07794

## Paper Analysis

### Inferred Research Topic
The paper introduces HiPRAG (Hierarchical Process Rewards for Efficient Agentic RAG), a training methodology that uses reinforcement learning with fine-grained process rewards to optimize search behavior in agentic Retrieval-Augmented Generation (RAG) systems.

### Inferred Task
Training LLMs to perform efficient agentic RAG for question answering, specifically reducing over-search and under-search behaviors.

### Inferred Method
- Hierarchical process reward function that combines outcome reward, format reward, and a gated process bonus based on the ratio of optimal search/non-search steps
- Structured parsable output format (XML-tagged reasoning steps) enabling rule-based step isolation
- On-the-fly over-search and under-search detection using external LLM judges (GPT-4.1 mini, GPT-5 mini)
- Compatible with PPO and GRPO RL algorithms
- Tested on Qwen2.5 (3B/7B) and Llama-3.2 (3B) models

### Inferred Datasets
Training: NQ + HotpotQA (combined)
Evaluation: NQ, PopQA, TriviaQA, 2WikiMultiHopQA, Bamboogle, HotpotQA, MuSiQue
Retrieval: Wikipedia 2018 dump with E5-base retriever

### Inferred Contribution
First method to provide explicit, step-specific process rewards for each search decision in agentic RAG, dramatically reducing over-search rate (from >27% to 2.3%) and under-search rate while improving accuracy.

## DeepXiv Access Attempts

### Status: FAILED
All attempts to authenticate with the DeepXiv API at `https://deepxiv.com/api/search` returned HTTP 401 with `{"error":"Not authenticated"}`.

### Attempted Authentication Methods
1. Bearer token in Authorization header
2. api-key header
3. x-api-key header
4. deepxiv-api-key header
5. Token in request body
6. Token in query parameter
7. Cookie-based token

### Verified Endpoints
- `GET /api/health` → `{"status":"healthy"}` (public)
- `POST /api/search` → 401 Unauthorized (requires authentication)
- `GET /api/search` → 405 Method Not Allowed

### Token
`DEEPXIV_API_TOKEN=sniRmhNSA2A2UVETupSomuV_eqv9c5flac8LCj0F6A8` (from .env)

## Search Queries (Would Have Used)
If DeepXiv had been accessible, the following queries would have been used:

1. "agentic retrieval augmented generation reinforcement learning"
2. "process reward reinforcement learning large language model retrieval"
3. "Search-R1 retrieval augmented generation reinforcement learning agent"
4. "over-search under-search retrieval augmented generation efficiency"
5. "process reward model step-level supervision LLM reasoning"
6. "GRPO PPO reinforcement learning retrieval augmented generation"
7. "IRCoT interleaving retrieval chain-of-thought reasoning"
8. "tool-augmented LLM search agent question answering"

## Related Work Themes Identified

1. **Retrieval-Augmented Generation and Agentic RAG**: RAG [1], NQ [2], HotpotQA [3], TriviaQA [4], MuSiQue [5]
2. **Reinforcement Learning for LLM Reasoning**: PPO [8], GRPO [9]
3. **RL-Based Search Agents**: Search-R1 [10], R1-Searcher [11], R1-Searcher++ [12], β-GRPO [13]
4. **Process-Level Supervision and Rewards**: Lightman et al. [14], Math-Shepherd [15]
5. **Prompt-Based Multi-Step Reasoning with Retrieval**: IRCoT [6], Search-o1 [7]

## Final Cited Papers
15 references covering the five identified research themes.

## Uncertainty
- DeepXiv API token from .env is not accepted by the service. The token may be expired, for a different service, or the API requires a different authentication flow.
- Citations [10-13] and [7] are 2025 preprints; exact author lists and venues were inferred from prior knowledge and paper body mentions. Venue information may not be definitive.
- Paper [13] (β-GRPO) is cited with "Anonymous" authors as the paper body does not specify authors and reliable metadata could not be retrieved through DeepXiv.
- Citations [7] and [10-12] represent recent (2025) arXiv preprints in a rapidly evolving field; exact metadata should be verified against the published versions.
