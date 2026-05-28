## Run Metadata
- Date: 2026-05-27
- Search source: DeepXiv only
- Output directory: runs/clean_search/sim_prompt+skill/11662
- Input paper: papers/anonymized_inputs/11662.txt

## Paper Profile
- Topic: MLLM-based verifiers for agent behavior in open-ended tasks
- Task: Evaluating agent trajectories (web navigation, computer use, robotics) and using MLLM-based rewards for self-improvement and online supervision
- Method: Self-Grounded Verification (SGV) — modulates conditional/unconditional generation to leverage MLLMs' own knowledge and reasoning for verification
- Data type / benchmark: VisualWebArena (VWA), OSWorld, robomimic
- Evaluation focus: Agreement bias identification, offline evaluation of verifiers, self-improvement via Reflexion, online supervision
- Main contribution: Identifies agreement bias (MLLMs' tendency to over-validate agent behavior), characterizes its properties, and proposes SGV to mitigate it, improving failure detection by up to 25pp and boosting downstream task completion
- Boundaries: Does not eliminate agreement bias entirely; limited to three environments; does not explore training-time solutions or process-based verification in depth; does not claim MLLMs replace formal verifiers

## Visible Related Work Headings
No explicit Related Work section detected in the visible input. The paper's input includes: Abstract, Introduction, Problem Setup (with sub-sections), Offline Evaluation, Downstream Applications, Conclusion. Thematic signals were extracted from the full paper body.

## Visible Coverage Ledger
| Visible signal | Signal type | Exact recovery query | DeepXiv recovery status | Planned use | Final disposition |
|---|---|---|---|---|---|
| Zheng et al. LLM-as-a-Judge | named works | Zheng LLM-as-a-Judge MT-Bench Chatbot Arena | Found: 2306.05685 | Core: LLM judge biases theme | covered |
| Liu et al. G-Eval | named works | G-Eval LLM evaluator NLG Liu chain-of-thought | Found: 2303.16634 | Core: LLM evaluator theme | covered |
| Shi et al. position bias | named works | position bias LLM judge pairwise comparison | Found: 2406.07791 | Core: bias theme | covered |
| Lambert et al. RewardBench | named works | RewardBench reward model evaluation benchmark | Found: 2403.13787 | Core: reward model evaluation | covered |
| Zhang et al. GenRM | named works | Generative Reward Model GenRM next-token prediction | Found: 2408.15240 | Core: verifier paradigm | covered |
| Lù et al. AgentRewardBench | named works | AgentRewardBench agent reward benchmark evaluation | Found: 2504.08942 | Core: agent trajectory evaluation benchmark | covered |
| Zhou et al. WebArena | named works | WebArena realistic web environment benchmark | Found: 2307.13854 | Core: benchmark theme | covered |
| Koh et al. VisualWebArena | named works | VisualWebArena multimodal web agent benchmark | Found: 2401.13649 | Core: benchmark theme | covered |
| Xie et al. OSWorld | named works | OSWorld desktop computer agent benchmark | Found: 2404.07972 | Core: benchmark theme | covered |
| Mandlekar et al. robomimic | named works | Mandlekar robomimic robot manipulation benchmark | Found: 2108.03298 | Core: benchmark theme | covered |
| Le Sellier De Chezelles et al. BrowserGym | named works | browsergym web agent benchmark environment library | Found: 2412.05467 | Context: benchmark infrastructure | covered |
| Wei et al. CoT | named works | chain-of-thought prompting Wei reasoning | Found: 2201.11903 | Context: agent method | covered |
| Yao et al. ReAct | named works | ReAct agent reasoning acting web navigation | Found: 2210.03629 | Core: agent architecture | covered |
| Shinn et al. Reflexion | named works | Reflexion self-improvement verbal reinforcement | Found: 2303.11366 | Core: self-improvement | covered |
| Chi et al. Diffusion Policy | named works | Diffusion Policy visuomotor robot | Found: 2303.04137 | Core: robot policy | covered |
| UI-TARS / UI-TARS-1.5 | named works | UI-TARS GUI agent computer use | Found: 2501.12326 | Intentionally omitted: agent tool, not core Related Work theme | intentionally omitted |
| WebVoyager | named works | WebVoyager end-to-end web agent multimodal | Found: 2401.13919 | Intentionally omitted: redundant with VWA benchmark coverage | intentionally omitted |
| Windows Agent Arena | named works | Windows Agent Arena multimodal OS agent | Found: 2409.08264 | Intentionally omitted: adjacent but not directly used in target paper | intentionally omitted |
| Yang et al. Set-of-Marks | named works | Set-of-Marks visual prompting Yang | Found: 2310.11441 | Intentionally omitted: prompting technique, not core theme | intentionally omitted |
| Verifiers in Go, Chess, math, code | field background | — | — | Broad context, discussed without specific citation | intentionally omitted (too broad/general) |
| RLHF limitations (pretraining, human rater satisfaction) | field background | RLHF Ouyang Christiano | Found: 2203.02155, 1706.03741 | Broad motivating context; used as uncited background | narrowed (discussed as known context without specific citations) |
| Automated peer review / MARG | named works | — | MARG flagged as metadata_mismatch per benchmark deny list | Screened only; theme preserved via stable alternatives | intentionally omitted (per benchmark deny list) |
| Robertson automated evaluation | named works | Robertson self-training automated evaluation | Not recovered | Narrowed: not critical for coverage | unresolved gap |
| AgentRewardBench (state-of-the-art on) | target motivation | — | — | Target paper's own claim; used as motivation | covered (as target motivation) |
| Agreement bias distinct from self-bias, position bias | target motivation | — | — | Target paper's positioning | covered (as target motivation) |
| SGV method | target motivation | — | — | Target paper's contribution | covered (as target motivation) |

## Must-Not-Drop Signals
| Signal | Source heading/theme | Required handling | Final status |
|---|---|---|---|
| LLM-as-Judge biases (Zheng et al.) | Verifiers/LLM-as-Judge theme | Core citation | covered |
| Position bias in LLM judges (Shi et al.) | Verifiers/LLM-as-Judge theme | Core citation | covered |
| Reward models and benchmarks (RewardBench) | Verifiers/LLM-as-Judge theme | Core citation | covered |
| GenRM / generative verifiers | Verifiers/LLM-as-Judge theme | Core citation | covered |
| AgentRewardBench | Verifiers/LLM-as-Judge theme | Core citation | covered |
| VisualWebArena benchmark | Agent Benchmarks theme | Named citation | covered |
| OSWorld benchmark | Agent Benchmarks theme | Named citation | covered |
| robomimic benchmark | Agent Benchmarks theme | Named citation | covered |
| ReAct agent architecture | Agent Architectures theme | Named citation | covered |
| Reflexion self-improvement | Agent Architectures theme | Named citation | covered |

## Search Queries
| Query | Purpose | Source |
|---|---|---|
| VisualWebArena multimodal web agent benchmark evaluation | Exact recovery: VisualWebArena | Input paper |
| OSWorld desktop computer agent benchmark | Exact recovery: OSWorld | Input paper |
| robomimic robot manipulation benchmark diffusion policy | Exact recovery: robomimic + Diffusion Policy | Input paper |
| ReAct agent reasoning acting web navigation language model | Exact recovery: ReAct | Input paper |
| Reflexion self-improvement language agent reflection verbal reinforcement | Exact recovery: Reflexion | Input paper |
| LLM as a judge evaluation bias language model | Broad discovery: LLM judge theme | Input paper |
| RewardBench reward model evaluation benchmark | Exact recovery: RewardBench | Input paper |
| AgentRewardBench agent reward benchmark evaluation | Exact recovery: AgentRewardBench | Input paper |
| WebArena realistic web environment benchmark language agent | Exact recovery: WebArena | Input paper |
| chain-of-thought prompting Wei reasoning language model | Exact recovery: CoT | Input paper |
| Set-of-Marks visual prompting grounding large multimodal model Yang | Exact recovery: SoM | Input paper |
| UI-TARS GUI agent computer use desktop automation | Exact recovery: UI-TARS | Input paper |
| browsergym web agent benchmark environment library | Exact recovery: BrowserGym | Input paper |
| Generative Reward Model GenRM next-token prediction reward verification | Exact recovery: GenRM | Input paper |
| LLM self-bias position bias evaluation judge model generation | Broad discovery: bias theme | Input paper |
| Zheng judging LLM-as-a-Judge MT-Bench evaluation | Exact recovery: Zheng et al. | Input paper |
| G-Eval LLM as evaluator NLG evaluation Liu chain-of-thought | Exact recovery: G-Eval | Input paper |
| Mandlekar robomimic robot manipulation benchmark imitation learning | Exact recovery: robomimic (Mandlekar) | Input paper |
| Paper SEA automated scientific peer review | Background check | Skill guidance (deny list context) |

## Candidate Screening
| Title | Authors | Year | Source | Label | Reason |
|---|---|---|---|---|---|
| Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | Zheng et al. | 2023 | arXiv:2306.05685 | relevant | Core LLM-as-judge work; identifies biases |
| G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment | Liu et al. | 2023 | arXiv:2303.16634 | relevant | LLM-based evaluation framework; notes LLM-text bias |
| Judging the Judges: Position Bias in LLM-as-a-Judge | Shi et al. | 2024 | arXiv:2406.07791 | relevant | Systematic study of position bias in LLM judges |
| RewardBench: Evaluating Reward Models for Language Modeling | Lambert et al. | 2024 | arXiv:2403.13787 | relevant | Reward model evaluation benchmark |
| Generative Verifiers: Reward Modeling as Next-Token Prediction | Zhang et al. | 2024 | arXiv:2408.15240 | relevant | Generative verifier paradigm |
| AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories | Lù et al. | 2025 | arXiv:2504.08942 | relevant | First benchmark for LLM judges on web agent trajectories |
| WebArena: A Realistic Web Environment for Building Autonomous Agents | Zhou et al. | 2023 | arXiv:2307.13854 | relevant | Foundational web agent benchmark |
| VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks | Koh et al. | 2024 | arXiv:2401.13649 | relevant | Core benchmark used in target paper |
| OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks | Xie et al. | 2024 | arXiv:2404.07972 | relevant | Core benchmark used in target paper |
| What Matters in Learning from Offline Human Demonstrations for Robot Manipulation | Mandlekar et al. | 2021 | arXiv:2108.03298 | relevant | robomimic benchmark used in target paper |
| The BrowserGym Ecosystem for Web Agent Research | Le Sellier De Chezelles et al. | 2024 | arXiv:2412.05467 | weakly relevant | Benchmark infrastructure; supports evaluation context |
| ReAct: Synergizing Reasoning and Acting in Language Models | Yao et al. | 2022 | arXiv:2210.03629 | relevant | Core agent architecture used in target paper |
| Reflexion: Language Agents with Verbal Reinforcement Learning | Shinn et al. | 2023 | arXiv:2303.11366 | relevant | Self-improvement method used in target paper |
| Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | Wei et al. | 2022 | arXiv:2201.11903 | weakly relevant | Baseline prompting technique; historical context |
| Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | Chi et al. | 2023 | arXiv:2303.04137 | relevant | Robot policy method used in target paper |
| UI-TARS: Pioneering Automated GUI Interaction with Native Agents | Qin et al. | 2025 | arXiv:2501.12326 | weakly relevant | Agent model used for OSWorld trajectories; not a core theme |
| Set-of-Mark Prompting Unleashes Extraordinary Visual Grounding in GPT-4V | Yang et al. | 2023 | arXiv:2310.11441 | weakly relevant | Baseline prompting technique; not a core theme |
| WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models | He et al. | 2024 | arXiv:2401.13919 | weakly relevant | Web agent system with GPT-4V evaluation; adjacent |
| Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale | Bonatti et al. | 2024 | arXiv:2409.08264 | weakly relevant | Adjacent OS benchmark not used in target paper |

## Planned Themes
| Theme | Input signal it maps to | Core/context citations | Notes |
|---|---|---|---|
| Verifiers, Reward Models, and LLM-as-Judge | Introduction discussion of verifiers, LLM-as-judge, agreement bias relation to known biases | [1-6] (Zheng, Liu, Shi, Lambert, Zhang, Lù) | Covers known LLM judge biases, reward model evaluation, and generative verifiers |
| Agent Benchmarks and Environments | VisualWebArena, OSWorld, robomimic usage in Problem Setup | [7-11] (Zhou, Koh, Xie, Le Sellier De Chezelles, Mandlekar) | Covers all three benchmark environments and supporting infrastructure |
| Agent Architectures and Self-Improvement | CoT, SoM, ReAct, Reflexion, Diffusion Policy discussions | [12-15] (Wei, Yao, Shinn, Chi) | Covers agent methods and self-improvement pipelines |

## Coverage Allocation
| Heading/theme | Recoverable named/background signals | Covered in final text | Unresolved gaps |
|---|---|---|---|
| Verifiers, Reward Models, and LLM-as-Judge | Zheng, Liu, Shi, Lambert, Zhang, Lù (6 named) | All 6 named works cited | None |
| Agent Benchmarks and Environments | Zhou, Koh, Xie, Mandlekar, Le Sellier De Chezelles (5 named) | All 5 named works cited | None |
| Agent Architectures and Self-Improvement | Wei, Yao, Shinn, Chi (4 named) | All 4 named works cited | None |

## Length Control
- Target word budget: 450-650 words (focused method paper)
- Estimated visible Related Work length: N/A (no visible section)
- Final word count: ~580 words (excluding LaTeX section header)
- Status: within budget

## Final Cited Papers
| # | Title | Authors | Year | Source | Citation role |
|---|---|---|---|---|---|
| 1 | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | Zheng et al. | 2023 | arXiv:2306.05685 | LLM-as-judge paradigm, known biases |
| 2 | G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment | Liu et al. | 2023 | arXiv:2303.16634 | LLM-based evaluation framework, bias toward LLM text |
| 3 | Judging the Judges: Position Bias in LLM-as-a-Judge | Shi et al. | 2024 | arXiv:2406.07791 | Position bias characterization |
| 4 | RewardBench: Evaluating Reward Models for Language Modeling | Lambert et al. | 2024 | arXiv:2403.13787 | Reward model evaluation benchmark |
| 5 | Generative Verifiers: Reward Modeling as Next-Token Prediction | Zhang et al. | 2024 | arXiv:2408.15240 | Generative verifier paradigm |
| 6 | AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories | Lù et al. | 2025 | arXiv:2504.08942 | Agent trajectory evaluation benchmark |
| 7 | WebArena: A Realistic Web Environment for Building Autonomous Agents | Zhou et al. | 2023 | arXiv:2307.13854 | Foundational web agent benchmark |
| 8 | VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks | Koh et al. | 2024 | arXiv:2401.13649 | Core benchmark used in target paper |
| 9 | OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks | Xie et al. | 2024 | arXiv:2404.07972 | Core benchmark used in target paper |
| 10 | The BrowserGym Ecosystem for Web Agent Research | Le Sellier De Chezelles et al. | 2024 | arXiv:2412.05467 | Benchmark infrastructure |
| 11 | What Matters in Learning from Offline Human Demonstrations for Robot Manipulation (robomimic) | Mandlekar et al. | 2021 | arXiv:2108.03298 | Robot manipulation benchmark |
| 12 | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | Wei et al. | 2022 | arXiv:2201.11903 | Baseline prompting technique |
| 13 | ReAct: Synergizing Reasoning and Acting in Language Models | Yao et al. | 2022 | arXiv:2210.03629 | Core agent architecture |
| 14 | Reflexion: Language Agents with Verbal Reinforcement Learning | Shinn et al. | 2023 | arXiv:2303.11366 | Self-improvement method |
| 15 | Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | Chi et al. | 2023 | arXiv:2303.04137 | Robot policy method |

## Claim-Citation Self-Check
| Citation | Claim | Supported? | Action | Notes |
|---|---|---|---|---|
| [1] Zheng | Strong LLMs as judges for chat assistants; identifies position, verbosity, self-enhancement biases | Supported | keep | Directly from paper abstract and TLDR |
| [2] Liu | G-Eval framework for LLM-based NLG evaluation; notes bias toward LLM-generated text | Supported | keep | Directly from paper abstract |
| [3] Shi | Position bias in LLM judges across pairwise/listwise settings; varies with quality gaps | Supported | keep | Directly from paper abstract |
| [4] Lambert | RewardBench for evaluating reward models in RLHF; covers chat, reasoning, safety | Supported | keep | Directly from paper abstract |
| [5] Zhang | GenRM trained via next-token prediction; leverages text generation of pretrained LLMs | Supported | keep | Directly from paper abstract |
| [6] Lù | AgentRewardBench assesses LLM judges for web agent trajectories; rule-based evaluation underreports success rates | Supported | keep | Directly from paper abstract |
| [7] Zhou | WebArena with fully functional websites across e-commerce, social forums, content management | Supported | keep | Directly from paper abstract |
| [8] Koh | VWA extends WebArena with visually grounded tasks requiring image-text processing | Supported | keep | Directly from paper abstract |
| [9] Xie | OSWorld scalable real-computer benchmark across OS/desktop apps | Supported | keep | Directly from paper abstract |
| [10] Le Sellier De Chezelles | BrowserGym unifies web agent benchmarks under standardized gym-like interface | Supported | keep | Directly from paper abstract |
| [11] Mandlekar | robomimic benchmark for offline human demonstrations on multi-stage manipulation | Supported | keep | Directly from paper abstract |
| [12] Wei | CoT prompting with intermediate reasoning steps improves LLM reasoning | Supported | keep | Directly from paper abstract |
| [13] Yao | ReAct interleaves reasoning traces with actions for environment interaction | Supported | keep | Directly from paper abstract |
| [14] Shinn | Reflexion: agents improve via verbal reflection, episodic memory for better decisions | Supported | keep | Directly from paper abstract |
| [15] Chi | Diffusion Policy represents visuomotor policies as conditional denoising diffusion; strong performance on manipulation benchmarks | Supported | keep | Directly from paper abstract |
| "motivates investigation of MLLMs as verifiers for multimodal, open-ended agent tasks" | Target motivation sentence | Target-paper interpretation | keep | Positioned as target-paper motivation, not cited-paper evidence |
| "effectiveness depends critically on verifier quality" | Target motivation sentence | Target-paper interpretation | keep | Positioned as target-paper motivation |
| "The target paper examines this dependency and proposes SGV" | Target motivation sentence | Target-paper interpretation | keep | Positioned as target-paper contribution description |

## Citation Ledger
| Citation string | Matching paper | In Related Work? | In Final References? | In Self-Check / Uncertain Points? | Scope |
|---|---|---|---|---|---|
| [1] Zheng et al. 2023 | Judging LLM-as-a-Judge | Yes | Yes | Yes | Core: LLM judge theme |
| [2] Liu et al. 2023 | G-Eval | Yes | Yes | Yes | Core: LLM evaluator theme |
| [3] Shi et al. 2024 | Position Bias in LLM-as-a-Judge | Yes | Yes | Yes | Core: bias theme |
| [4] Lambert et al. 2024 | RewardBench | Yes | Yes | Yes | Core: reward model eval |
| [5] Zhang et al. 2024 | GenRM | Yes | Yes | Yes | Core: verifier paradigm |
| [6] Lù et al. 2025 | AgentRewardBench | Yes | Yes | Yes | Core: agent trajectory eval |
| [7] Zhou et al. 2023 | WebArena | Yes | Yes | Yes | Core: benchmark theme |
| [8] Koh et al. 2024 | VisualWebArena | Yes | Yes | Yes | Core: benchmark theme |
| [9] Xie et al. 2024 | OSWorld | Yes | Yes | Yes | Core: benchmark theme |
| [10] Le Sellier De Chezelles et al. 2024 | BrowserGym | Yes | Yes | Yes | Context: infrastructure |
| [11] Mandlekar et al. 2021 | robomimic | Yes | Yes | Yes | Core: benchmark theme |
| [12] Wei et al. 2022 | CoT | Yes | Yes | Yes | Context: prompting |
| [13] Yao et al. 2022 | ReAct | Yes | Yes | Yes | Core: agent architecture |
| [14] Shinn et al. 2023 | Reflexion | Yes | Yes | Yes | Core: self-improvement |
| [15] Chi et al. 2023 | Diffusion Policy | Yes | Yes | Yes | Core: robot policy |
| MARG (D'Arcy et al.) | 2401.04259 | No | No | No (screened only) | Screened only per benchmark deny list |
| UI-TARS (Qin et al. 2025) | 2501.12326 | No | No | No (omitted) | Agent model, not core theme |

## Completion Status
| Gate | Status |
|---|---|
| RWEval Citation Format | ✓ Numeric citations in s_text.txt matching s_reference.txt |
| Read the Visible Input | ✓ Full paper checked; no explicit Related Work section detected |
| Visible Heading Preservation | ✓ Three themes constructed from input signals (no explicit headings to mirror) |
| Visible Coverage Ledger | ✓ All visible signals assigned disposition |
| Coverage Allocation | ✓ Each theme covers ≥2 named works and field background/target motivation |
| Missing-Point Prevention | ✓ All 10 must-not-drop signals covered |
| Named Citation Exactness | ✓ All named works searched exactly before substitutes considered |
| Reference Validity Guard | ✓ MARG screened only per deny list; no unstable metadata in final citations |
| Length Control | ✓ ~580 words within 450-650 target |
| Dynamic Citation Budget | ✓ 15 papers within 12-18 budget |
| Final Consistency | ✓ All in-text citations match references; no orphaned citations or references |
| Final Status | complete with usable RWEval output |

## Benchmark-Specific Deny / Handle List
| Paper or pattern | Reason | Handling | Theme preserved by |
|---|---|---|---|
| MARG: Multi-Agent Review Generation for Scientific Papers (D'Arcy et al., 2401.04259) | metadata_mismatch (per benchmark guidance) | Screened only, not final-cited | Automated evaluation theme preserved via stable alternatives (RewardBench, AgentRewardBench, GenRM); MARG is also off-topic for agent trajectory verification |

## Uncertain Points
- robomimic paper (Mandlekar et al. 2021) was found under its full title "What Matters in Learning from Offline Human Demonstrations for Robot Manipulation" (arXiv:2108.03298), not under the "robomimic" shorthand search — metadata verified as consistent.
- The target paper mentions "Go and Chess" verifiers in passing (Introduction) but these are very broad historical references that do not have specific arXiv papers recoverable via DeepXiv for the specific RL/AlphaGo/AlphaZero citations the target paper likely intends. These are intentionally omitted as too broad for a focused Related Work.
- The target paper references "RLHF limitations" and "pretraining limitations" as general background for why knowledge extraction fails. These are broad concepts not requiring specific citations in the Related Work; they serve as motivating context for the target paper's own approach.
- BrowserGym (Le Sellier De Chezelles et al. 2024, arXiv:2412.05467) has limited metadata (384 tokens) but sufficient information to verify title, year, and domain. Included as context citation with narrowed wording.
- No explicit Related Work section exists in the input paper, so themes were constructed from the full paper's signal coverage rather than mirroring visible headings.
