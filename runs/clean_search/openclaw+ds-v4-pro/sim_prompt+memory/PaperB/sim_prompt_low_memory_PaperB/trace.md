# Related Work Writing — Trace: sim_prompt_low_memory_researcher

**Date:** 2026-06-01
**Search source:** DeepXiv only

## Paper Profile (Inferred from Body Text)

- **Topic:** MLLMs as verifiers of agent behavior in open-ended environments
- **Task:** Evaluating agent trajectories (web navigation, computer use, robotics) using MLLMs
- **Method:** Self-Grounded Verification (SGV) — zero-shot method that modulates (un)conditional generation by first eliciting broad priors about desired behavior, then conditioning evaluation on self-generated priors
- **Data type / benchmarks:** VisualWebArena (web), OSWorld (desktop/computer), robomimic (robotics); 1,300+ trajectories from diverse agents
- **Key finding:** Agreement bias — MLLMs systematically over-validate flawed agent behavior, with failure-detection rates as low as 50%, resilient to test-time scaling
- **Applications:** Offline trajectory evaluation, self-improvement via Reflexion, online supervision
- **Contributions:** (1) Identification and characterization of agreement bias across 13+ model families and 28+ templates; (2) SGV method improving failure detection by 25pp and accuracy by 14pp; (3) New state-of-the-art on VisualWebArena; (4) Updated VWA benchmark release

## Related Work Signals Extracted

### Theme 1: MLLMs as Evaluators
- "LLM judges" — evaluation of model outputs
- "biases in LLM judges" — positional, self-enhancement, verbosity biases
- "MLLM-based evaluations" — using MLLMs as verifiers
- "scoring templates" — Likert scales, binary vs. ternary labels
- Process vs. outcome supervision — "process reward models"
- RLHF limitations — "fundamental limitations in pretraining and RLHF"

### Theme 2: AI Agents and Verifier-Guided Improvement
- VisualWebArena — multimodal web agent benchmark
- OSWorld — real computer environment benchmark
- robomimic — robot manipulation benchmark
- Reflexion — self-improvement via verbal reflection
- Tree search for LM agents
- Agent Workflow Memory
- Self-improvement / online supervision / behavior cloning

### Theme 3: Test-Time Scaling and Reasoning
- "chain-of-thought (CoT)" — reasoning elicitation
- "majority voting" — self-consistency
- "test-time scaling techniques" — inference-time computation
- DeepSeek-R1 — large reasoning models
- Set-of-Marks (SoM) prompting — visual grounding

## Search Queries

| Query | Purpose | Source |
|---|---|---|
| "LLM judge evaluator agent behavior multimodal" | Theme 1 discovery | MLLM evaluators |
| "LLM evaluation bias agreement position self-bias judge" | Theme 1 discovery | Bias literature |
| "MLLM reward model verifier open-ended task trajectory" | Theme 1 discovery | Verifiers |
| "VisualWebArena multimodal web agent benchmark" | Exact recovery | Theme 2 |
| "OSWorld computer desktop agent benchmark multimodal" | Exact recovery | Theme 2 |
| "autonomous evaluation refinement digital agents Reflexion" | Exact recovery | Theme 2 |
| "WebArena realistic web environment building autonomous agents Zhou" | Exact recovery | Theme 2 |
| "tree search language model web agent autonomous" | Exact recovery | Theme 2 |
| "AgentWorkflowMemory trajectory filtering finetuning web agent" | Exact recovery | Theme 2 |
| "chain of thought prompting reasoning large language model Wei" | Exact recovery | Theme 3 |
| "self consistency improves chain of thought reasoning Wang majority voting" | Exact recovery | Theme 3 |
| "DeepSeek R1 Guo incentivizing reasoning LLM arxiv 2501.12948" | Exact recovery | Theme 3 |
| "set of marks prompting visual grounding large multimodal model Yang" | Exact recovery | Theme 3 |
| "LLM as a judge MT bench Zheng chatbot arena evaluation" | Exact recovery | Theme 1 |
| "process reward model verifier step by step Lightman math reasoning" | Exact recovery | Theme 1 |
| "DeepSeek R1 reasoning model reinforcement learning" | Exact recovery | Theme 3 |
| "robomimic robot manipulation benchmark tool hang Mandlekar imitation learning" | Theme 2 | Not found via DeepXiv |
| "diffusion policy robot manipulation imitation learning Chi visuomotor" | Exact recovery | Verified (2303.04137) |
| "SeeClick GUI agent grounding visual mobile device" | Theme 2 discovery | Verified (2401.10935) |
| "training language models follow instructions human feedback RLHF InstructGPT Ouyang" | Theme 1 background | Verified (2203.02155) |
| "ReAct synergizing reasoning acting language model Yao" | Theme 2 background | Verified (2210.03629) |

## Candidate Screening

| Title | Authors | Year | Source | Label | Reason |
|---|---|---|---|---|---|
| Judging LLM-as-a-Judge | Zheng et al. | 2023 | arXiv:2306.05685 | relevant | Core LLM-as-judge reference; cited [1] |
| Judging the Judges: Position Bias | Shi et al. | 2024 | arXiv:2406.07791 | relevant | Bias in LLM evaluation; cited [2] |
| Autonomous Evaluation and Refinement of Digital Agents | Pan et al. | 2024 | arXiv:2404.06474 | relevant | VLM evaluators for agent trajectories; cited [3] |
| Let's Verify Step by Step | Lightman et al. | 2023 | arXiv:2305.20050 | relevant | Process supervision context; cited [4] |
| WebArena | Zhou et al. | 2023 | arXiv:2307.13854 | relevant | Foundational web agent benchmark; cited [5] |
| VisualWebArena | Koh et al. | 2024 | arXiv:2401.13649 | relevant | Multimodal web agent benchmark; cited [6] |
| OSWorld | Xie et al. | 2024 | arXiv:2404.07972 | relevant | Desktop agent benchmark; cited [7] |
| Reflexion | Shinn et al. | 2023 | arXiv:2303.11366 | relevant | Self-improvement via reflection; cited [8] |
| Tree Search for Language Model Agents | Koh et al. | 2024 | arXiv:2407.01476 | relevant | Test-time search for web agents; cited [9] |
| Agent Workflow Memory | Wang et al. | 2024 | arXiv:2409.07429 | relevant | Trajectory-based workflow extraction; cited [10] |
| Chain-of-Thought Prompting | Wei et al. | 2022 | arXiv:2201.11903 | relevant | Foundational CoT; cited [11] |
| Self-Consistency | Wang et al. | 2022 | arXiv:2203.11171 | relevant | Majority voting for reasoning; cited [12] |
| DeepSeek-R1 | Guo et al. | 2025 | arXiv:2501.12948 | relevant | Large reasoning models; cited [13] |
| Set-of-Mark Prompting | Yang et al. | 2023 | arXiv:2310.11441 | relevant | Multimodal visual grounding; cited [14] |
| Diffusion Policy | Chi et al. | 2023 | arXiv:2303.04137 | relevant (not cited) | Robotics policy; background context for Theme 2 but budget constraint |
| InstructGPT (RLHF) | Ouyang et al. | 2022 | arXiv:2203.02155 | relevant (not cited) | RLHF background; folded into Theme 1 without dedicated citation |
| ReAct | Yao et al. | 2022 | arXiv:2210.03629 | relevant (not cited) | Agent paradigm; subsumed by Reflexion in Theme 2 |
| SeeClick | Cheng et al. | 2024 | arXiv:2401.10935 | relevant (not cited) | GUI grounding; budget constraint |
| robomimic | Mandlekar et al. | 2021 | — | not found | Did not appear in DeepXiv searches |

## Final Cited Papers

| # | Title | Authors | Year | Source | Citation role |
|---|---|---|---|---|---|
| [1] | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | Zheng et al. | 2023 | arXiv:2306.05685 | LLM-as-judge paradigm |
| [2] | Judging the Judges: A Systematic Study of Position Bias | Shi et al. | 2024 | arXiv:2406.07791 | Bias in LLM evaluation |
| [3] | Autonomous Evaluation and Refinement of Digital Agents | Pan et al. | 2024 | arXiv:2404.06474 | VLM evaluators for agents |
| [4] | Let's Verify Step by Step | Lightman et al. | 2023 | arXiv:2305.20050 | Process supervision |
| [5] | WebArena | Zhou et al. | 2023 | arXiv:2307.13854 | Web agent benchmark |
| [6] | VisualWebArena | Koh et al. | 2024 | arXiv:2401.13649 | Multimodal web benchmark |
| [7] | OSWorld | Xie et al. | 2024 | arXiv:2404.07972 | Desktop agent benchmark |
| [8] | Reflexion | Shinn et al. | 2023 | arXiv:2303.11366 | Self-improvement |
| [9] | Tree Search for Language Model Agents | Koh et al. | 2024 | arXiv:2407.01476 | Test-time search |
| [10] | Agent Workflow Memory | Wang et al. | 2024 | arXiv:2409.07429 | Trajectory-based memory |
| [11] | Chain-of-Thought Prompting | Wei et al. | 2022 | arXiv:2201.11903 | Reasoning via CoT |
| [12] | Self-Consistency | Wang et al. | 2022 | arXiv:2203.11171 | Majority voting |
| [13] | DeepSeek-R1 | Guo et al. | 2025 | arXiv:2501.12948 | Large reasoning models |
| [14] | Set-of-Mark Prompting | Yang et al. | 2023 | arXiv:2310.11441 | Multimodal prompting |

## Coverage Allocation

| Theme | Coverage | Citations |
|---|---|---|
| MLLMs as Evaluators | LLM judges, biases, VLM trajectory evaluation, process supervision | [1], [2], [3], [4] |
| AI Agents and Verifier-Guided Improvement | Web/desktop benchmarks, Reflexion, tree search, trajectory memory | [5], [6], [7], [8], [9], [10] |
| Test-Time Scaling and Reasoning | CoT, self-consistency, reasoning models, multimodal prompting | [11], [12], [13], [14] |

## Length Control

- Target: 250-350 words
- Final: 348 words
- Status: Within target

## Uncertainties

- robomimic (Mandlekar et al.) was not retrievable via DeepXiv searches. This is a known paper published at CoRL 2021 and may not be indexed by the DeepXiv arXiv source. Not cited.
- The paper's body mentions "web search tools" for grounding and "Platt scaling" for calibration — these are treated as implementation details rather than Related Work themes and were not searched for.
- The paper body discusses "pretraining data rewriting" and symbolic methods as future work directions. These were not included in Related Work as they are forward-looking.
- InstructGPT (RLHF) was located via DeepXiv but not cited — the RLHF context was folded into Theme 1 implicitly through the discussion of biases and alignment rather than given a dedicated citation slot, to stay within the word budget.
