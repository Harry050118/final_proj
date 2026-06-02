# Related Work Generation — Trace

**Date:** 2026-06-01  
**Session:** sim_prompt_high_memory_researcher  
**Condition:** A1 Clean Search (no candidate papers provided)

## Paper Profile (Inferred from Body Text)

- **Topic:** MLLM-based verifiers for agent behavior in open-ended interactive environments
- **Core Finding:** "Agreement bias" — MLLMs systematically over-validate flawed agent behavior, with TNR as low as 50%
- **Proposed Method:** Self-Grounded Verification (SGV) — two-step sampling process: (1) generate priors about desired behavior from partial information, (2) evaluate trajectories conditioned on self-generated priors
- **Environments:** VisualWebArena (web), OSWorld (desktop), robomimic (robotics)
- **Applications Evaluated:** Offline trajectory evaluation, self-improvement via Reflexion, online supervision
- **Key Signals Extracted:**
  - MLLM/LLM-as-judge, evaluator biases (self-bias, positional bias, phrasing bias)
  - Test-time scaling (CoT, majority voting, reasoning models)
  - Agent benchmarks (WebArena, VisualWebArena, OSWorld)
  - Self-improvement (Reflexion), tree search, RL training with evaluators
  - Multimodal chain-of-thought, Set-of-Marks prompting
  - Process reward models, DeepSeek-R1

## Thematic Structure

1. **MLLMs and LLMs as Evaluators** — LLM-as-a-Judge paradigm, evaluation biases, MLLM evaluators for agent trajectories, verifier design
2. **AI Agents and Self-Improvement** — Benchmarks, Reflexion, evaluator-guided tree search, workflow memory, RL training
3. **Test-Time Scaling and Reasoning** — CoT, multimodal CoT, ReAct, self-consistency, Tree of Thoughts, process rewards, reasoning models, SoM

## DeepXiv Search Queries

All searches via `https://data.rag.ac.cn/arxiv/?type=retrieve&query=...&top_k=N`:

| # | Query | Key Papers Found |
|---|-------|-----------------|
| 1 | LLM as a judge evaluator multimodal | Agent-as-a-Judge, LLMBar, JETTS |
| 2 | MLLM verifier agent trajectory web navigation computer use | Art of Building Verifiers (Rosset et al.), Let's Think in Two Steps |
| 3 | WebArena VisualWebArena web agent benchmark | WebArena (Zhou et al.), VisualWebArena (Koh et al.) |
| 4 | Reflexion self-improvement agent language model | Reflexion (Shinn et al.), Towards Autonomous Agents |
| 5 | chain of thought prompting reasoning Wei 2022 | CoT (Wei et al.) |
| 6 | test-time scaling compute inference large language model | Inference Scaling Laws, Large Language Monkeys |
| 7 | OSWorld computer use benchmark agent | OSWorld (Xie et al.) |
| 8 | ReAct reasoning acting language model agent environment | ReAct (Yao et al.) |
| 9 | self consistency chain of thought majority voting | Self-Consistency (Wang et al.) |
| 10 | autonomous evaluation refinement digital agents GPT-4V | Autonomous Evaluation (Pan et al.) |
| 11 | tree search language model agent web autonomous | Tree Search for LM Agents (Koh et al.) |
| 12 | agent workflow memory trajectory filtering tool | Agent Workflow Memory (Wang et al.) |
| 13 | Set of Marks prompting visual grounding large language model | Set-of-Mark Prompting (Yang et al.) |
| 14 | diffusion policy robot manipulation visuomotor | Diffusion Policy (Chi et al.) |
| 15 | DigiRL reinforcement learning VLM evaluator device control | DigiRL (Bai et al.) |
| 16 | process reward model verifier math reasoning step by step | Let's Verify Step by Step (Lightman et al.) |
| 17 | DeepSeek R1 reasoning model reinforcement learning | DeepSeek-R1 |
| 18 | LLM judge bias position bias verbosity bias evaluation Zheng | Mitigating Bias of LLM Evaluation, Humans or LLMs as the Judge |
| 19 | multimodal chain of thought reasoning vision language | Multimodal CoT (Zhang et al.) |
| 20 | MT-Bench LLM judge evaluator chatbot arena Zheng | MT-Bench / Chatbot Arena (Zheng et al.) |
| 21 | robomimic benchmark imitation learning robot manipulation Mandlekar | robomimic (Mandlekar et al.) — verified via direct ID lookup |
| 22 | self-consistency improves chain of thought reasoning language models | Self-Consistency (Wang et al.) |
| 23 | tree of thoughts deliberate problem solving large language models | Tree of Thoughts (Yao et al.) |
| 24 | zero-shot chain of thought reasoning large language models Kojima | Zero-shot CoT (Kojima et al.) |
| 25 | LLM self bias preference own generations evaluator | LLM Evaluators Recognize and Favor Their Own Generations (Panickssery et al.) |
| 26 | AgentRewardBench benchmark reward model agent trajectory | AgentRewardBench (Lu et al.) |

## Final Cited Papers (22 papers)

All 22 papers verified via DeepXiv `type=head` API endpoint — titles, authors, venues, and years confirmed.

### Theme 1: MLLMs and LLMs as Evaluators (papers [1]–[5])
- [1] Zheng et al. 2023 — MT-Bench/Chatbot Arena (NeurIPS)
- [2] Panickssery et al. 2024 — LLM self-preference bias (NeurIPS)
- [3] Pan et al. 2024 — Autonomous Evaluation and Refinement of Digital Agents (arXiv)
- [4] Lu et al. 2025 — AgentRewardBench (arXiv)
- [5] Rosset et al. 2026 — Art of Building Verifiers for Computer Use Agents (arXiv)

### Theme 2: AI Agents and Self-Improvement (papers [6]–[13])
- [6] Zhou et al. 2023 — WebArena (ICLR)
- [7] Koh et al. 2024 — VisualWebArena (arXiv)
- [8] Xie et al. 2024 — OSWorld (NeurIPS)
- [9] Mandlekar et al. 2021 — robomimic (CoRL)
- [10] Shinn et al. 2023 — Reflexion (NeurIPS)
- [11] Koh et al. 2024 — Tree Search for LM Agents (TMLR)
- [12] Wang et al. 2024 — Agent Workflow Memory (ICML)
- [13] Bai et al. 2024 — DigiRL (NeurIPS)

### Theme 3: Test-Time Scaling and Reasoning (papers [14]–[22])
- [14] Wei et al. 2022 — Chain-of-Thought (NeurIPS)
- [15] Kojima et al. 2022 — Zero-Shot CoT (NeurIPS)
- [16] Zhang et al. 2023 — Multimodal CoT (TMLR)
- [17] Yao et al. 2022 — ReAct (ICLR)
- [18] Wang et al. 2022 — Self-Consistency (ICLR)
- [19] Yao et al. 2023 — Tree of Thoughts (NeurIPS)
- [20] Yang et al. 2023 — Set-of-Mark Prompting (arXiv)
- [21] Lightman et al. 2023 — Let's Verify Step by Step (ICLR)
- [22] DeepSeek-AI 2025 — DeepSeek-R1 (arXiv)

## Lessons Applied from Previous Postmortems

1. ✅ **Read entire body text for signals** — Extracted test-time scaling, CoT, Reflexion, biases, benchmarks
2. ✅ **Three broad themes** — Not over-segmented; folded biases into "Evaluators" theme
3. ✅ **Target 250-350 words** — Final output: 339 words
4. ✅ **Concept-first writing** — No "Author et al. [N]" sentence openers; papers cited as evidence
5. ✅ **Searched for extensions** — CoT → multimodal CoT → ReAct; evaluators → Reflexion → tree search → DigiRL
6. ✅ **Never dropped a relevant paper for budget** — All 22 relevant papers included
7. ✅ **Positive closing sentence** — "MLLMs offer a compelling foundation—motivating systematic investigation..."
8. ✅ **Varied sentence structures** — Used passive voice, transition phrases, conceptual framing
9. ✅ **Every cited paper verified** — All 22 papers confirmed via DeepXiv API

## Uncertainties / Notes

- The Robomimic paper (2108.03298) has a long title; cited as "What Matters in Learning from Offline Human Demonstrations for Robot Manipulation" per the paper's actual title
- DeepSeek-R1 author list is extremely long (>150 authors); cited as "DeepSeek-AI" per convention
- Rosset et al. (2604.06240) and Lu et al. (2504.08942) are very recent preprints; their publication venues may change
