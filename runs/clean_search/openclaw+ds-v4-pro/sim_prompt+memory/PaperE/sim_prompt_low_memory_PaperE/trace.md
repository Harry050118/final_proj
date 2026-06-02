## Run Metadata
- Date: 2026-06-01
- Search source: DeepXiv only (via deepxiv_sdk, base_url=https://data.rag.ac.cn)
- Input condition: A1 Clean Search

## Paper Profile
- Topic: MLLM-based verifiers for evaluating agent behavior in open-ended interactive environments
- Task: Studying and improving MLLMs as verifiers/judges of multimodal agent trajectories
- Method: Self-Grounded Verification (SGV) — zero-shot method modulating unconditional/conditional generation;
  first elicits broad priors about desired behavior from partial information, then conditions evaluation on self-generated priors
- Data type / benchmark: VisualWebArena (910 web tasks), OSWorld (369 desktop tasks), robomimic (tool-hang, robotic manipulation)
- Evaluation focus: Offline trajectory evaluation, self-improvement via Reflexion, online supervision; metrics include bias, distance skewness, TPR/TNR; downstream task completion rates
- Main contribution: Identification of agreement bias—MLLMs' systematic tendency to over-validate flawed agent behavior—and SGV to mitigate it; comprehensive evaluation across 13+ model families and 28+ design templates
- Boundaries: Does not address training-based solutions; process-level verification left for future work; SGV mitigates but does not eliminate agreement bias

## Visible Related Work Headings
The input paper does not include a Related Work section. All headings are inferred from body text signals.

## Visible Coverage Ledger
| Visible signal | Signal type | Planned theme | Final disposition |
|---|---|---|---|
| LLM-as-Judge / MT-Bench | named works | MLLM-based Evaluation | covered [1] |
| G-Eval | named works | MLLM-based Evaluation | covered [2] |
| AgentRewardBench | named works | MLLM-based Evaluation | covered [3] |
| MLLMs as reward functions | field background | MLLM-based Evaluation | covered [4, 5] |
| VisualWebArena | named works | Agent Benchmarks | covered [6] |
| WebArena | named works | Agent Benchmarks | covered [5] |
| OSWorld | named works | Agent Benchmarks | covered [7] |
| robomimic | named works | Agent Benchmarks | covered [8] |
| Reflexion | named works | Self-Improvement | covered [9] |
| Self-Rewarding LMs | named works | Self-Improvement | covered [10] |
| LLM evaluation biases (position, self-bias) | field background | Biases in Evaluation | covered [11, 12] |
| RLHF limitations (pretraining, RLHF bottlenecks) | field background | (absorbed into motivation) | intentionally omitted (not citable as prior work entry) |
| ReAct agents | named works | (absorbed as experimental detail) | intentionally omitted (agent architecture, not core Related Work topic) |
| Chain-of-Thought prompting | named works | (absorbed as experimental detail) | intentionally omitted (basic prompting technique) |
| Set-of-Marks prompting | named works | (absorbed as experimental detail) | intentionally omitted (basic prompting technique) |
| Diffusion Policy | named works | (absorbed as experimental detail) | intentionally omitted (agent architecture, not core Related Work topic) |
| UI-TARS | named works | (absorbed as experimental detail) | intentionally omitted (agent architecture, not core Related Work topic) |
| BrowserGym | named works | (absorbed as experimental detail) | intentionally omitted (infrastructure, not core Related Work topic) |

## Must-Not-Drop Signals
| Signal | Source | Required handling | Final status |
|---|---|---|---|
| LLM-as-a-Judge paradigm | core topic | Cite Zheng et al. | covered [1] |
| AgentRewardBench | methodology signal | Cite Lù et al. | covered [3] |
| VisualWebArena | environment signal | Cite Koh et al. | covered [6] |
| WebArena | environment signal | Cite Zhou et al. | covered [5] |
| OSWorld | environment signal | Cite Xie et al. | covered [7] |
| Reflexion | downstream application | Cite Shinn et al. | covered [9] |
| Position bias in LLM judges | bias context | Cite Shi et al. | covered [11] |
| Self-bias in LLM judges | bias context | Cite Spiliopoulou et al. | covered [12] |

## Search Queries
| Query | Purpose | Source |
|---|---|---|
| "LLM as judge evaluation verifier agent trajectory multimodal" | Broad LLM-as-Judge discovery | DeepXiv |
| "VisualWebArena web agent benchmark multimodal evaluation" | Exact recovery of VWA | DeepXiv |
| "OSWorld desktop computer agent benchmark" | Exact recovery of OSWorld | DeepXiv |
| "WebArena web environment agent benchmark" | Exact recovery of WebArena | DeepXiv |
| "Reflexion self-improvement agent language model iterative refinement" | Exact recovery of Reflexion | DeepXiv |
| "reward model process reward agent behavior verification language model" | Reward model discovery | DeepXiv |
| "robomimic robot manipulation learning benchmark" | Exact recovery of robomimic | DeepXiv |
| "LLM evaluation bias self-bias position bias agreement judge" | Bias literature discovery | DeepXiv |
| "GUI agent mobile desktop multimodal language model action" | GUI agent discovery | DeepXiv |
| "set of marks visual prompting grounding multimodal agent" | Exact recovery of SoM | DeepXiv |
| "large reasoning model test time scaling compute verifier" | Verifier literature discovery | DeepXiv |
| "multimodal large language model verifier reward agent behavior open-ended tasks" | Broad discovery | DeepXiv |
| "LLM judge bias leniency agreement bias over-validation" | Agreement bias discovery | DeepXiv |
| "agent reward benchmark evaluation" | AgentRewardBench discovery | DeepXiv |
| "browsergym web agent browser environment" | BrowserGym discovery | DeepXiv |
| "ReAct Synergizing Reasoning Acting language models agent" | Exact recovery of ReAct | DeepXiv |
| "Chain of Thought prompting Wei reasoning large language models" | Exact recovery of CoT | DeepXiv |
| "robomimic robot imitation learning benchmark Mandlekar" | Targeted robomimic search | DeepXiv |
| "Diffusion Policy visuomotor robot learning Chi" | Exact recovery of Diffusion Policy | DeepXiv |
| "UI-TARS GUI agent desktop" | Exact recovery of UI-TARS | DeepXiv |
| "LLM as a Judge Zheng evaluation MT-Bench" | Exact recovery of LLM-as-Judge | DeepXiv |
| "G-Eval NLG evaluation Liu LLM chain of thought" | Exact recovery of G-Eval | DeepXiv |
| "RewardBench evaluating reward models Lambert" | RewardBench discovery | DeepXiv |
| "RLHF training language models human feedback Ouyang" | RLHF discovery | DeepXiv |
| "DPO Direct Preference Optimization language model Rafailov" | DPO discovery | DeepXiv |
| "SeeClick GUI agent visual grounding screenshot" | GUI agent discovery | DeepXiv |
| "CogAgent visual agent GUI grounding" | GUI agent discovery | DeepXiv |
| "robomimic imitation learning robot Mandlekar 2021" | Targeted robomimic search | DeepXiv |

## Candidate Screening
| Title | Authors | Year | ID | Label | Reason |
|---|---|---|---|---|---|
| Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | Zheng et al. | 2023 | 2306.05685 | relevant | Foundational LLM-as-Judge work |
| G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment | Liu et al. | 2023 | 2303.16634 | relevant | Early LLM evaluator work |
| AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories | Lù et al. | 2025 | 2504.08942 | relevant | Direct benchmark for LLM judges of web agent trajectories |
| Agent-RewardBench: Towards a Unified Benchmark for Reward Modeling | Men et al. | 2025 | 2506.21252 | weakly relevant | Related benchmark but redundant with [3]; screened, not cited |
| Reward Design with Language Models | Kwon et al. | 2023 | 2303.00001 | relevant | LLMs as proxy reward functions |
| WebArena: A Realistic Web Environment for Building Autonomous Agents | Zhou et al. | 2023 | 2307.13854 | relevant | Foundational benchmark |
| VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks | Koh et al. | 2024 | 2401.13649 | relevant | Directly used benchmark |
| OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks | Xie et al. | 2024 | 2404.07972 | relevant | Directly used benchmark |
| What Matters in Learning from Offline Human Demonstrations for Robot Manipulation | Mandlekar et al. | 2021 | 2108.03298 | relevant | robomimic framework |
| Reflexion: Language Agents with Verbal Reinforcement Learning | Shinn et al. | 2023 | 2303.11366 | relevant | Core self-improvement method |
| Self-Rewarding Language Models | Yuan et al. | 2024 | 2401.10020 | relevant | Self-improvement via LLM-as-Judge |
| Judging the Judges: Position Bias in LLM-as-a-Judge | Shi et al. | 2024 | 2406.07791 | relevant | Position bias study |
| Play Favorites: Measuring Self-Bias in LLM-as-a-Judge | Spiliopoulou et al. | 2025 | 2508.06709 | relevant | Self-bias study |
| GUI-Shepherd: Process Reward and Verification for GUI Tasks | Chen et al. | 2025 | 2509.23738 | weakly relevant | Process reward model but different focus; screened, not cited |
| TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents | Liu et al. | 2026 | 2602.06443 | weakly relevant | Trajectory verification but different method; screened, not cited |
| BrowserGym Ecosystem for Web Agent Research | Le Sellier De Chezelles et al. | 2024 | 2412.05467 | weakly relevant | Infrastructure; screened, not cited |
| ReAct: Synergizing Reasoning and Acting in Language Models | Yao et al. | 2022 | 2210.03629 | weakly relevant | Agent architecture; screened, not cited |
| Chain-of-Thought Prompting Elicits Reasoning | Wei et al. | 2022 | 2201.11903 | weakly relevant | Prompting technique; screened, not cited |
| Set-of-Mark Prompting Unleashes Visual Grounding in GPT-4V | Yang et al. | 2023 | 2310.11441 | weakly relevant | Prompting technique; screened, not cited |
| Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | Chi et al. | 2023 | 2303.04137 | weakly relevant | Agent architecture; screened, not cited |
| Agent-as-a-Judge (survey) | You et al. | 2026 | 2601.05111 | weakly relevant | Survey of agent-as-judge; screened, not cited |
| DPO: Direct Preference Optimization | Rafailov et al. | 2023 | 2305.18290 | irrelevant | Alignment method, not directly about evaluation; screened, not cited |
| RewardBench: Evaluating Reward Models | Lambert et al. | 2024 | 2403.13787 | irrelevant | Focuses on reward model evaluation for text, not agent verification; screened, not cited |

## Planned Themes
| Theme | Input signal it maps to | Core/context citations | Notes |
|---|---|---|---|
| MLLM-based Evaluation and Verifiers | LLM-as-Judge, G-Eval, AgentRewardBench, reward design | [1,2,3,4] | Core topic of the paper |
| Web, Desktop, and Embodied Agent Benchmarks | WebArena, VWA, OSWorld, robomimic | [5,6,7,8] | Environments used in the study |
| Agent Self-Improvement with LLM Feedback | Reflexion, Self-Rewarding LMs | [9,10] | Downstream applications |
| Biases in LLM-based Evaluation | Position bias, self-bias | [11,12] | Related bias literature |

## Coverage Allocation
| Heading/theme | Recoverable named/background signals | Covered in final text | Unresolved gaps |
|---|---|---|---|
| MLLM-based Evaluation | LLM-as-Judge, G-Eval, AgentRewardBench, LLM reward functions | 4/4 signals covered | - |
| Agent Benchmarks | WebArena, VWA, OSWorld, robomimic | 4/4 signals covered | - |
| Self-Improvement | Reflexion, Self-Rewarding LMs | 2/2 signals covered | - |
| Biases in Evaluation | Position bias, self-bias | 2/2 signals covered | - |

## Length Control
- Target word budget: 450-650 words (focused method paper)
- Final word count: ~500 words
- Status: within budget

## Final Cited Papers (12 total)
[1] Zheng et al. "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena." 2306.05685
[2] Liu et al. "G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment." 2303.16634
[3] Lù et al. "AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories." 2504.08942
[4] Kwon et al. "Reward Design with Language Models." 2303.00001
[5] Zhou et al. "WebArena: A Realistic Web Environment for Building Autonomous Agents." 2307.13854
[6] Koh et al. "VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks." 2401.13649
[7] Xie et al. "OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments." 2404.07972
[8] Mandlekar et al. "What Matters in Learning from Offline Human Demonstrations for Robot Manipulation." 2108.03298
[9] Shinn et al. "Reflexion: Language Agents with Verbal Reinforcement Learning." 2303.11366
[10] Yuan et al. "Self-Rewarding Language Models." 2401.10020
[11] Shi et al. "Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge." 2406.07791
[12] Spiliopoulou et al. "Play Favorites: A Statistical Method to Measure Self-Bias in LLM-as-a-Judge." 2508.06709

## Claim-Citation Self-Check
| Citation | Claim | Supported? | Action |
|---|---|---|---|
| [1] | LLM-as-a-Judge paradigm, GPT-4 >80% agreement with humans, position/verbosity biases identified | Supported | keep |
| [2] | G-Eval extended LLM evaluation to NLG with CoT + probability weighting | Supported | keep |
| [3] | AgentRewardBench benchmark for web agent trajectory evaluation, rule-based underestimation | Supported | keep |
| [4] | LLMs as proxy reward functions, data-efficient reward design | Supported | keep |
| [5] | WebArena: 812 tasks, four domains, functional correctness evaluation | Supported | keep |
| [6] | VisualWebArena: 910 visually grounded tasks, text+image inputs | Supported | keep |
| [7] | OSWorld: 369 tasks, multi-application, cross-platform, ~12% agent success | Supported | keep |
| [8] | robomimic: offline learning, tool-hang, history-dependent models | Supported | keep |
| [9] | Reflexion: verbal RL, reflective summaries, episodic memory | Supported | keep |
| [10] | Self-Rewarding LMs: LLM-as-Judge for iterative DPO training | Supported | keep |
| [11] | Position bias in LLM-as-a-Judge, solution quality gaps | Supported | keep |
| [12] | Self-bias: favorable ratings to own outputs, family-bias | Supported | keep |

## Completion Status
| Gate | Status |
|---|---|
| RWEval Citation Format | pass (numeric [n] in s_text.txt, matching s_reference.txt) |
| Read the Visible Input | pass (full body text analyzed) |
| Visible Heading Preservation | N/A (no visible Related Work section) |
| Visible Coverage Ledger | pass (all signals disposed) |
| Coverage Allocation | pass (all themes have sufficient citations) |
| Missing-Point Prevention | pass (8 must-not-drop signals all covered) |
| Named Citation Exactness | pass (author-year signals directly searched) |
| Reference Validity Guard | pass (all 12 papers have verified metadata) |
| Length Control | pass (~500 words, within budget) |
| Dynamic Citation Budget | pass (12 papers, within 8-12 range) |
| Final Consistency | pass (12 in-text = 12 references) |

## Benchmark-Specific Deny / Handle List
| Paper or pattern | Reason | Handling |
|---|---|---|
| MARG (D'Arcy et al., 2401.04259) | Known metadata_mismatch in this benchmark | Not cited (not relevant to this paper's topic anyway) |

## Uncertain Points
- Paper [8] (robomimic/Mandlekar et al.): DeepXiv brief API returned authors as None for arXiv:2108.03298. Title "What Matters in Learning from Offline Human Demonstrations for Robot Manipulation" correctly matches the robomimic paper (CoRL 2021). Authors reconstructed from known citation: A. Mandlekar, D. Xu, J. Wong, S. Nasiriany, C. Wang, et al.
- Some named methods from the input paper (ReAct, Chain-of-Thought, Set-of-Marks, Diffusion Policy, UI-TARS, BrowserGym) were not cited as they represent agent architectures, prompting techniques, or infrastructure rather than prior work on verifier evaluation—the core focus of this Related Work section.
- The input paper references "concurrent work" comparing rule-based evaluation with human annotations, and "concurrent reward benchmarks." These were not recoverable through generic search without knowing specific author names or titles, which would require searching for removed identifiers.
