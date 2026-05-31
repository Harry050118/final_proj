## Run Metadata
- Date: 2026-05-30
- Model: claude_code+ds-v4-pro
- Search source: DeepXiv only

## Paper Profile (Inferred from Body Text)
- **Topic**: MLLMs as verifiers of agent behavior in open-ended interactive environments
- **Key Finding**: Agreement bias — MLLMs systematically over-validate flawed agent trajectories
- **Proposed Method**: Self-Grounded Verification (SGV) — zero-shot method modulating (un)conditional generation
- **Environments**: VisualWebArena (web, 910 tasks), OSWorld (desktop, 369 tasks), robomimic (robot manipulation, tool hang)
- **Applications**: Offline trajectory evaluation, self-improvement via Reflexion, online supervision
- **Main Contribution**: Identifying agreement bias as pervasive across 13+ model families; SGV improves failure detection by up to 25pp and accuracy by up to 14pp

## Planned Themes

| Theme | Core Citations | Coverage |
|---|---|---|
| LLM-based Evaluation and Verification | [1]-[6] | LLM-as-a-Judge, MLLM-as-a-Judge, CoT, self-consistency, generative verifiers, process reward models, known biases |
| Autonomous Agents and Self-Improvement | [7]-[9] | ReAct, Reflexion, Diffusion Policy, dependency on verifier quality |
| Benchmarks for Multimodal Agent Evaluation | [10]-[14] | WebArena, VisualWebArena, OSWorld, robomimic, AgentRewardBench |

## Search Queries Used

| Query | Purpose | Results |
|---|---|---|
| LLM as a judge evaluation MT-Bench Chatbot Arena | Recover Zheng et al. [1] | 5 results |
| MLLM as a judge multimodal evaluation assessment | Recover Chen et al. [2] | 5 results |
| chain-of-thought prompting elicits reasoning large language models | Recover Wei et al. [3] | 5 results |
| self-consistency chain of thought reasoning majority voting | Recover Wang et al. [4] | 5 results |
| generative verifier reward modeling next token prediction | Recover Zhang et al. [5] | 5 results |
| ReAct synergizing reasoning and acting language models | Recover Yao et al. [7] | 5 results |
| Reflexion language agents verbal reinforcement learning self-improvement | Recover Shinn et al. [8] | 5 results |
| diffusion policy visuomotor robot manipulation action | Recover Chi et al. [9] | 5 results |
| WebArena realistic web environment autonomous agents benchmark | Recover Zhou et al. [10] | 5 results |
| VisualWebArena multimodal visual web tasks benchmark | Recover Koh et al. [11] | 5 results |
| OSWorld benchmarking multimodal agents open-ended computer tasks | Recover Xie et al. [12] | 5 results |
| robomimic offline human demonstrations robot manipulation benchmark | Recover Mandlekar et al. [13] | 5 results |
| LLM judge bias positional phrasing evaluation template | Background on judge biases | 5 results |
| process reward model PRM step verification reasoning | Recover process reward models | 5 results |
| Let's Verify Step by Step (verified via brief lookup) | Recover Lightman et al. [6] | 1 result (2305.20050) |
| agent reward benchmark evaluation web trajectories | Recover AgentRewardBench [14] | 5 results |
| LLM self-bias self-preference generated text evaluation | Background on self-bias | 5 results |
| Judging the Judges position bias (brief lookup) | Background on position bias | 1 result (2406.07791) |
| Self-Preference Bias in LLM-as-a-Judge (brief lookup) | Background on self-bias | 1 result (2410.21819) |

## Key Papers Verified via DeepXiv

All 14 citations were verified through DeepXiv `brief()` and `head()` calls, confirming title, author lists, venue, and year.

| # | arXiv ID | Title | Authors | Venue | Year |
|---|---|---|---|---|---|
| 1 | 2306.05685 | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | Zheng et al. (13 authors) | NeurIPS | 2023 |
| 2 | 2402.04788 | MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge... | Chen et al. (10 authors) | ICML | 2024 |
| 3 | 2201.11903 | Chain-of-Thought Prompting Elicits Reasoning in LLMs | Wei et al. (9 authors) | NeurIPS | 2022 |
| 4 | 2203.11171 | Self-Consistency Improves Chain of Thought Reasoning... | Wang et al. (8 authors) | ICLR | 2023 |
| 5 | 2408.15240 | Generative Verifiers: Reward Modeling as Next-Token Prediction | Zhang et al. (6 authors) | ICLR | 2025 |
| 6 | 2305.20050 | Let's Verify Step by Step | Lightman et al. (10 authors) | ICLR | 2024 |
| 7 | 2210.03629 | ReAct: Synergizing Reasoning and Acting in Language Models | Yao et al. (7 authors) | arXiv | 2022 |
| 8 | 2303.11366 | Reflexion: Language Agents with Verbal Reinforcement Learning | Shinn et al. (6 authors) | NeurIPS | 2023 |
| 9 | 2303.04137 | Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | Chi et al. (7 authors) | RSS | 2023 |
| 10 | 2307.13854 | WebArena: A Realistic Web Environment for Building... | Zhou et al. (12 authors) | ICLR | 2024 |
| 11 | 2401.13649 | VisualWebArena: Evaluating Multimodal Agents on... | Koh et al. (10 authors) | arXiv | 2024 |
| 12 | 2404.07972 | OSWorld: Benchmarking Multimodal Agents for Open-Ended... | Xie et al. (17 authors) | NeurIPS | 2024 |
| 13 | 2108.03298 | What Matters in Learning from Offline Human Demonstrations... | Mandlekar et al. (10 authors) | CoRL | 2021 |
| 14 | 2504.08942 | AgentRewardBench: Evaluating Automatic Evaluations of... | Lu et al. (10 authors) | arXiv | 2025 |

## Final Consistency Check
- All 14 citations in s_text.txt have matching entries in s_reference.txt: PASS
- All 14 references in s_reference.txt are cited in s_text.txt: PASS
- No LaTeX sectioning or citation commands in s_text.txt: PASS
- No top-level "Related Work" heading: PASS
- Numeric citation labels used consistently: PASS
- Bold inline theme headings only: PASS
- No markdown code fences in either file: PASS
- Claim-citation verification against DeepXiv TLDR/abstract: PASS (all claims match retrieved metadata)

## Papers Considered But Not Cited
- Self-Preference Bias in LLM-as-a-Judge (2410.21819): Relevant to judge bias discussion but covered by [1]'s treatment of biases
- Judging the Judges: Position Bias in LLM-as-a-Judge (2406.07791): Specific position bias study; covered by broader bias discussion in [1]
- SeeClick (2401.10935): GUI agent grounding method; not core to verification theme
- Agentic Reward Modeling / VAGEN (2602.00575): Very recent (2025); overlaps with input paper's contributions
- Various process reward model papers (ThinkPRM, PQM, BiPRM): Too specific to math/code domains

## Uncertain Points
- The paper 2507.11662 titled "Let's Think in Two Steps: Mitigating Agreement Bias in MLLMs with Self-Grounded Verification" appeared in DeepXiv search results with a TLDR about video understanding, suggesting either a metadata mismatch or a different paper. Not cited due to potential overlap with the input paper.
- Author name with diacritics (Stanczak, Martin-Martin) were normalized to ASCII for compatibility.
- Some DeepXiv venue metadata may reflect accepted conference rather than publication year.
