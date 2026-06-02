# Trace: Related Work Generation for Paper 11662

## Inferred Research Topic
The paper studies **Multimodal Large Language Models (MLLMs) as verifiers of agent behavior** in open-ended domains (web navigation, computer use, robotics). It identifies a systematic limitation called **agreement bias**---MLLMs' tendency to over-validate flawed agent trajectories---and proposes **Self-Grounded Verification (SGV)**, a method that modulates (un)conditional generation to better leverage MLLM knowledge and alignment.

## Inferred Contributions
1. Identification and characterization of agreement bias across 13+ model families and 28+ design templates
2. Demonstration of adverse impacts on offline evaluation, self-improvement (Reflexion), and online supervision
3. Self-Grounded Verification (SGV), a zero-shot method that improves failure detection by up to 25pp
4. Updated VisualWebArena benchmark release
5. New SOTA on VisualWebArena

## Environments Studied
- VisualWebArena (web)
- OSWorld (desktop/computer use)
- robomimic (robotics, tool-hang task)

## Search Queries Used

| # | Query | Results |
|---|-------|---------|
| 1 | "MLLM verifier agent trajectory evaluation reward multimodal" | AgentRewardBench (2506.21252), Agentic Reward Modeling (2602.00575), DeltaRubric (2605.09269), MagicGUI-RMS (2601.13060), AgentV-RL (2604.16004), Rationale Matters (2603.16600) |
| 2 | "LLM as judge evaluation bias over-validation agent behavior" | LLM-as-Judge Survey (2507.21504), Validating LLM-as-a-Judge (2503.05965), Pride and Prejudice (2402.11436), Agent-as-a-Judge (2601.05111) |
| 3 | "VisualWebArena web agent benchmark multimodal evaluation" | VisualWebArena (2401.13649), WebVoyager (2401.13919), VideoWebArena (2410.19100), Windows Agent Arena (2409.08264) |
| 4 | "OSWorld computer desktop agent benchmark multimodal evaluation" | OSWorld (2404.07972), OSUniverse (2505.03570), CRAB (2407.01511), Windows Agent Arena (2409.08264) |
| 5 | "Reflexion self-improvement agent reflection LLM self-correction iterative" | Reflexion (2303.11366), Self-Rewarding LMs (2401.10020), Agent-R (2501.11425), Self-Contrast (2401.02009) |
| 6 | "process reward model outcome reward model verifier agent reasoning" | GUI-Shepherd (2509.23738), CompassVerifier (2508.03686), AgentPRM (2502.10325), Verifiable Process Rewards (2605.10325) |
| 7 | "WebArena realistic web environment agent benchmark language model" | WebArena (2307.13854), Tree Search for LM Agents (2407.01476), LLMs Can Self-Improve at Web Agent Tasks (2405.20309) |
| 8 | "LLM position bias leniency bias evaluation judge reliability calibration" | Large LMs not Fair Evaluators (2305.17926), Judging the Judges: Position Bias (2406.07791), Humans or LLMs as Judge (2402.10669), Skewed Score (2507.03772) |
| 9 | "MLLM agent reward model online supervision steering verifier self-play" | GUI-Shepherd (dup), Search Self-play (2510.18821) |
| 10 | "robomimic robot manipulation benchmark imitation learning diffusion policy" | Diffusion Policy (2303.04137), Diffusion Models for Robotic Manipulation: Survey (2504.08438) |
| 11 | "set-of-marks visual grounding prompting GUI agent screenshot" | Set-of-Mark (2310.11441), SeeClick (2401.10935), UI-AGILE (2507.22025) |
| 12 | "test-time scaling chain-of-thought majority voting reasoning model verifier" | GenPRM (2504.00891), Critique to Verify (2509.23152), Revisiting Test-Time Scaling (2502.12215) |
| 13 | "UI-TARS GUI agent specialist desktop computer use autonomous" | UI-TARS (2501.12326), Agent S2 (2504.00906), Claude 3.5 Computer Use (2411.10323) |
| 14 | "reinforcement learning verifiable rewards RLVR agent training LLM" | Auditable-choice reframing (2511.02463), Agent-RLVR (2506.11425) |
| 15 | "LLM self-enhancement bias self-preference self-bias evaluation text generation" | Pride and Prejudice (dup), Self-Preference Bias (2410.21819), LLM Evaluators Recognize and Favor Their Own Generations (2404.13076) |
| 16 | "browsergym web agent benchmark environment browser automation" | BrowserGym (2412.05467), WorkArena (2403.07718) |
| 17 | "LLM monitoring oversight scalable oversight agents evaluation" | Reliable Weak-to-Strong Monitoring (2508.19461), Scalable Oversight Protocols (2504.03731) |
| 18 | "agent trajectory filtering finetuning behavior cloning successful trajectories self-improvement" | STeCa (2502.14276) |
| 19 | "RLHF limitations reward hacking knowledge extraction pretraining language model" | RLHF Deciphered (2404.08555), Pretraining LMs with Human Preferences (2302.08582) |
| 20 | "chain-of-thought prompting Wei Zhou reasoning large language model" | Chain-of-Thought (2201.11903), Self-Consistency (2203.11171) |

## Final Cited Papers (36 total)

### Theme 1: Verifiers and Reward Models (6 papers)
- [1]-[4] AlphaGo, AlphaZero, DeepSeek-Coder, DeepSeek-R1 (foundational verifier-driven work)
- [5] Agent-RewardBench (2506.21252)
- [6] Agentic Reward Modeling (2602.00575)
- [7] GUI-Shepherd (2509.23738)
- [8] DeltaRubric (2605.09269)
- [9] MagicGUI-RMS (2601.13060)

### Theme 2: Agent Benchmarks (6 papers)
- [10] WebArena (2307.13854)
- [11] VisualWebArena (2401.13649)
- [12] OSWorld (2404.07972)
- [13] robomimic (Mandlekar et al., CoRL 2021)
- [14] BrowserGym (2412.05467)
- [15] Windows Agent Arena (2409.08264)

### Theme 3: LLM-as-Judge and Biases (4 papers)
- [16] Large LMs not Fair Evaluators (2305.17926)
- [17] Pride and Prejudice (2402.11436)
- [18] Self-Preference Bias (2410.21819)
- [19] Humans or LLMs as Judge (2402.10669)

### Theme 4: Self-Improvement (5 papers)
- [20] Reflexion (2303.11366)
- [21] Self-Rewarding LMs (2401.10020)
- [22] LLMs Can Self-Improve at Web Agent Tasks (2405.20309)
- [23] Agent-R (2501.11425)
- [24] STeCa (2502.14276)

### Theme 5: Reasoning and Test-Time Scaling (5 papers)
- [25] Chain-of-Thought (2201.11903)
- [26] Self-Consistency (2203.11171)
- [27] AgentPRM (2502.10325)
- [28] GenPRM (2504.00891)
- [29] Verifiable Process Rewards (2601.17223)

### Theme 6: Visual Grounding and GUI Agents (4 papers)
- [30] Set-of-Mark (2310.11441)
- [31] SeeClick (2401.10935)
- [32] UI-TARS (2501.12326)
- [33] WebVoyager (2401.13919)

### Theme 7: Alignment and Robotics (3 papers)
- [34] RLHF Deciphered (2404.08555)
- [35] Pretraining LMs with Human Preferences (2302.08582)
- [36] Diffusion Policy (2303.04137)

## Uncertainty Notes
- The robomimic paper [13] was not found in DeepXiv search results but is a well-known CoRL 2021 paper by Mandlekar et al. Other papers that cite robomimic were found (e.g., Diffusion Policy), confirming its existence.
- The paper references "concurrent work comparing rule-based evaluation with human annotations" in VWA. This concurrent work could not be identified from the anonymized body text alone and is not cited here.
- Foundational game-playing verifier papers (AlphaGo, AlphaZero) and large reasoning model papers (DeepSeek-Coder, DeepSeek-R1) are cited based on their well-established status in the verifier literature, as the paper's abstract explicitly references "seminal work in Go and Chess" and "large reasoning models (LRMs), leveraging formal verifiers in code and math."
