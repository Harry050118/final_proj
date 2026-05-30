## Run Metadata
- Date: 2026-05-27
- Search source: DeepXiv only

## Paper Profile
- Topic: Multimodal verification of agent behavior in open-ended interactive environments
- Task: Using MLLMs as verifiers for agent trajectories across web navigation, computer use, and robotics
- Method: Comprehensive empirical study diagnosing agreement bias + Self-Grounded Verification (SGV), a zero-shot method modulating conditional/unconditional generation
- Data type / benchmark: VisualWebArena (web, 910 tasks), OSWorld (desktop, 369 tasks), robomimic (robot manipulation, tool hang)
- Evaluation focus: Agreement bias diagnosis (TNR, bias, dSkew), downstream applications (self-improvement via Reflexion, online supervision)
- Main contribution: Identifying agreement bias as a systematic limitation of MLLM verifiers; SGV improves failure detection by up to 25pp
- Boundaries: SGV mitigates but does not eliminate agreement bias; remaining failures stem from base model visual perception–language integration limits

## Visible Related Work Headings
No explicit `\section{Related Work}` found in the input. Related work signals are embedded in the Introduction and Problem Setup sections.

| Heading (inferred from Introduction/Setup) | Extracted coverage signals | Planned theme |
|---|---|---|
| LLM-based Evaluation & Verifiers | LLM-as-a-Judge, MLLM-as-a-Judge, generative verifiers, CoT reasoning, majority voting, biases in LLM judges, pretraining/RLHF limitations | LLM-based Evaluation and Verification |
| Autonomous Agents & Self-Improvement | ReAct, Reflexion, Diffusion Policy, self-improvement pipelines, online supervision, data filtering for fine-tuning | Autonomous Agents and Self-Improvement |
| Benchmarks for Agent Evaluation | WebArena, VisualWebArena, OSWorld, robomimic, AgentRewardBench, browsergym, Set-of-Marks | Benchmarks for Multimodal Agent Evaluation |

## Visible Coverage Ledger
| Visible signal | Signal type | Exact recovery query | DeepXiv recovery status | Planned use | Final disposition |
|---|---|---|---|---|---|
| Zheng LLM-as-a-Judge | named work | Zheng judging LLM-as-a-Judge MT-Bench Chatbot Arena evaluation | Recovered (2306.05685) | Core citation Theme 1 | covered |
| Chen MLLM-as-a-Judge | named work | MLLM-as-a-Judge multimodal benchmark | Recovered (2402.04788) | Core citation Theme 1 | covered |
| Zhang Generative Verifiers (GenRM) | named work | generative verifier reward modeling next-token prediction | Recovered (2408.15240) | Core citation Theme 1 | covered |
| Wei Chain-of-Thought | named work | chain-of-thought prompting Wei reasoning | Recovered (2201.11903) | Context citation Theme 1 | covered |
| Wang Self-Consistency/Majority Voting | named work | self-consistency chain-of-thought Wang reasoning | Recovered (2203.11171) | Context citation Theme 1 | covered |
| Yao ReAct | named work | ReAct agent reasoning action language model | Recovered (2210.03629) | Core citation Theme 2 | covered |
| Shinn Reflexion | named work | Reflexion language agent verbal reinforcement | Recovered (2303.11366) | Core citation Theme 2 | covered |
| Chi Diffusion Policy | named work | Diffusion Policy visuomotor action diffusion | Recovered (2303.04137) | Core citation Theme 2 | covered |
| Zhou WebArena | named work | WebArena realistic web environment Zhou | Recovered (2307.13854) | Core citation Theme 3 | covered |
| Koh VisualWebArena | named work | VisualWebArena multimodal visual web tasks | Recovered (2401.13649) | Core citation Theme 3 | covered |
| Xie OSWorld | named work | OSWorld multimodal computer desktop agent | Recovered (2404.07972) | Core citation Theme 3 | covered |
| Mandlekar robomimic | named work | Mandlekar offline human demonstrations robot manipulation | Recovered (2108.03298) | Core citation Theme 3 | covered |
| Set-of-Marks (SoM) prompting | named work | set-of-marks Yang visual prompting web agent | Embedded in VisualWebArena paper | Covered via VWA citation [10] | covered |
| AgentRewardBench | named work | AgentRewardBench reward model evaluation agent trajectories | Recovered (2504.08942) | Context mention only, not separate citation | narrowed (mentioned as concurrent work context, not separate entry) |
| browsergym | named work | browsergym web agent browser benchmark | Recovered (2412.05467) | Not used in Related Work (weak relevance to method focus) | intentionally omitted (benchmark framework, not a core contribution to verification/evaluation theme) |
| UI-TARS-1.5 | named work | UI-TARS GUI agent desktop automation | Recovered (2501.12326) | Not used in Related Work (agent used in experiments, not a method contribution) | intentionally omitted (agent used in experiments, not a related work method) |
| WebVoyager | named work | WebVoyager end-to-end web agent multimodal | Recovered (2401.13919) | Not used (similar agent space, but not core to verification theme) | intentionally omitted (duplicative with WebArena/VWA line of benchmarks) |
| Pretraining/RLHF limitations | field background | pretraining limitations knowledge extraction RLHF | Partially recovered; broad background | Covered as field background in Theme 1 target motivation | narrowed (broad field background, mentioned as uncited motivation) |
| LLM judge biases (positional, phrasing, self-bias) | field background | LLM judge bias positional phrasing evaluation template | Multiple results; integrated into Theme 1 | Covered via [1] and [2] discussion of biases | covered |
| Verifiers in formal domains (Go, Chess, math, code) | field background | N/A (broad historical context) | N/A | Mentioned as opening context in Theme 1 | covered (broad historical context, uncited) |

## Must-Not-Drop Signals
| Signal | Source heading/theme | Required handling | Final status |
|---|---|---|---|
| LLM-as-a-Judge (Zheng) | Theme 1 | Must cite [1] | covered |
| MLLM-as-a-Judge (Chen) | Theme 1 | Must cite [2] | covered |
| Generative Verifiers (Zhang) | Theme 1 | Must cite [3] | covered |
| Chain-of-Thought (Wei) | Theme 1 | Must cite [4] | covered |
| ReAct (Yao) | Theme 2 | Must cite [6] | covered |
| Reflexion (Shinn) | Theme 2 | Must cite [7] | covered |
| Diffusion Policy (Chi) | Theme 2 | Must cite [8] | covered |
| WebArena (Zhou) | Theme 3 | Must cite [9] | covered |
| VisualWebArena (Koh) | Theme 3 | Must cite [10] | covered |
| OSWorld (Xie) | Theme 3 | Must cite [11] | covered |
| robomimic (Mandlekar) | Theme 3 | Must cite [12] | covered |

## Search Queries
| Query | Purpose | Source |
|---|---|---|
| LLM as a judge evaluation of agent trajectories multimodal verifiers | Theme 1: LLM-as-Judge, MLLM verifiers | Input Introduction |
| VisualWebArena multimodal web agent benchmark evaluation | Theme 3: VWA benchmark | Input Introduction |
| Reflexion self-improvement agents verifier feedback self-reflection | Theme 2: Reflexion | Input Introduction |
| reward models RLHF verifier training agent behavior evaluation bias | Theme 1: Verifiers, RLHF | Input Introduction |
| OSWorld multimodal computer desktop agent benchmark evaluation | Theme 3: OSWorld | Input Introduction |
| robomimic robot manipulation benchmark imitation learning diffusion policy | Theme 3: robomimic + Diffusion Policy | Input Introduction |
| LLM judge bias positional phrasing self-bias evaluation template | Theme 1: LLM judge biases | Input Introduction |
| ReAct agent reasoning action language model interactive environment | Theme 2: ReAct | Input Introduction |
| chain-of-thought prompting Wei reasoning large language models | Theme 1: CoT | Input Introduction |
| set-of-marks visual prompting grounding multimodal Yang | Theme 1: SoM | Input Introduction |
| AgentRewardBench reward model evaluation benchmark agent trajectories | Theme 3: AgentRewardBench | Input Section 2.3 |
| UI-TARS GUI agent desktop automation visual language model | Context: UI-TARS agent | Input Section 2.3 |
| generative reward model GenRM next-token prediction reward modeling | Theme 1: Generative verifiers | Input Introduction |
| browsergym web agent browser environment benchmark | Context: browsergym | Input Section 2.3 |
| Zheng judging LLM-as-a-judge MT-Bench Chatbot Arena evaluation | Theme 1: LLM-as-a-Judge exact recovery | Input Introduction |
| language model agents web navigation computer use multimodal autonomous | Theme 2: Web agents | Input Introduction |
| Yang set-of-marks visual prompting web agent screenshot grounding | Theme 1/3: SoM exact recovery | Input Introduction |
| self-consistency chain-of-thought Wang reasoning path diversity | Theme 1: Majority voting | Input Introduction |
| Shinn Reflexion language agent verbal reinforcement learning | Theme 2: Reflexion exact recovery | Input Introduction |
| WebArena realistic web environment benchmark autonomous agents Zhou | Theme 3: WebArena exact recovery | Input Introduction |
| Mandlekar "What Matters in Learning from Offline Human Demonstrations" robot manipulation | Theme 3: robomimic exact recovery | Input Introduction |

## Candidate Screening
| Title | Authors | Year | Source | Label | Reason |
|---|---|---|---|---|---|
| Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | Zheng et al. | 2023 | 2306.05685 | relevant | Directly establishes LLM-as-a-Judge paradigm; visible in input |
| MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge | Chen et al. | 2024 | 2402.04788 | relevant | Extends judge paradigm to multimodal; directly relevant to MLLM verifier topic |
| Generative Verifiers: Reward Modeling as Next-Token Prediction | Zhang et al. | 2024 | 2408.15240 | relevant | Verifier design via next-token prediction; supports verification theme |
| Chain-of-Thought Prompting Elicits Reasoning in LLMs | Wei et al. | 2022 | 2201.11903 | relevant | Foundational reasoning method used in verifier designs |
| Self-Consistency Improves Chain of Thought Reasoning | Wang et al. | 2022 | 2203.11171 | relevant | Majority voting / test-time scaling method; visible in input |
| ReAct: Synergizing Reasoning and Acting in Language Models | Yao et al. | 2022 | 2210.03629 | relevant | Agent architecture used in input experiments; visible in input |
| Reflexion: Language Agents with Verbal Reinforcement Learning | Shinn et al. | 2023 | 2303.11366 | relevant | Self-improvement method; visible named work in input |
| Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | Chi et al. | 2023 | 2303.04137 | relevant | Robot policy method; visible in input |
| WebArena: A Realistic Web Environment for Building Autonomous Agents | Zhou et al. | 2023 | 2307.13854 | relevant | Foundational web agent benchmark; predecessor to VWA |
| VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks | Koh et al. | 2024 | 2401.13649 | relevant | Core benchmark used in input; introduces SoM |
| OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks | Xie et al. | 2024 | 2404.07972 | relevant | Core benchmark used in input |
| What Matters in Learning from Offline Human Demonstrations (robomimic) | Mandlekar et al. | 2021 | 2108.03298 | relevant | Core benchmark used in input |
| AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories | Anonymous? | 2025 | 2504.08942 | weakly relevant | Concurrent work; used as evaluation context but not core Related Work citation |
| The BrowserGym Ecosystem for Web Agent Research | (various) | 2024 | 2412.05467 | weakly relevant | Benchmark framework; not core to verification theme |
| UI-TARS: Pioneering Automated GUI Interaction | (various) | 2025 | 2501.12326 | weakly relevant | Agent model; used in experiments, not Related Work |
| WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models | (various) | 2024 | 2401.13919 | weakly relevant | Web agent paper; duplicative with WebArena/VWA line |
| Agent-as-a-Judge | (various) | 2025 | 2601.05111 | irrelevant | Different focus (agent-as-judge rather than LLM-as-judge for agent trajectories) |
| Humans or LLMs as the Judge? A Study on Judgement Biases | (various) | 2024 | 2402.10669 | weakly relevant | Bias study but focuses on human vs LLM comparison, not agent trajectory verification |
| CompassVerifier | (various) | 2025 | 2508.03686 | irrelevant | Focuses on answer matching for static benchmarks, not agent trajectory verification |

## Planned Themes
| Theme | Input signal it maps to | Core/context citations | Notes |
|---|---|---|---|
| LLM-based Evaluation and Verification | LLM-as-a-Judge, MLLM-as-a-Judge, generative verifiers, CoT, majority voting, judge biases | [1,2,3] core; [4,5] context | Covers evaluation paradigm, biases, verifier methods |
| Autonomous Agents and Self-Improvement | ReAct, Reflexion, Diffusion Policy, self-improvement pipelines | [6,7,8] core | Covers agent architectures, self-improvement, dependency on verifier quality |
| Benchmarks for Multimodal Agent Evaluation | WebArena, VisualWebArena, OSWorld, robomimic | [9,10,11,12] core | Covers evolution of benchmarks from text to multimodal to computer/robot |

## Coverage Allocation
| Heading/theme | Recoverable named/background signals | Covered in final text | Unresolved gaps |
|---|---|---|---|
| LLM-based Evaluation and Verification | Zheng, Chen, Zhang, Wei, Wang, LLM judge biases, pretraining/RLHF limitations | Zheng [1], Chen [2], Zhang [3], Wei [4], Wang [5], judge biases | Pretraining/RLHF limitations narrowed to broad uncited field background |
| Autonomous Agents and Self-Improvement | Yao (ReAct), Shinn (Reflexion), Chi (Diffusion Policy), Reflexion/online supervision | Yao [6], Shinn [7], Chi [8], self-improvement dependency on verifiers | None |
| Benchmarks for Multimodal Agent Evaluation | Zhou (WebArena), Koh (VWA), Xie (OSWorld), Mandlekar (robomimic), SoM, oracle limitations | Zhou [9], Koh [10], Xie [11], Mandlekar [12], SoM, oracle limitations | AgentRewardBench narrowed to context mention; browsergym intentionally omitted |

## Length Control
- Target word budget: 8-12 citations (focused method paper; no broad visible ledger requiring 12-18)
- Estimated visible Related Work length: N/A (no explicit Related Work section; signals embedded in ~1.5 pages of Introduction)
- Final word count: ~475 words (within 450-650 target)
- Status: within target

## Final Cited Papers
| Title | Authors | Year | Source | Citation role |
|---|---|---|---|---|
| Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | Zheng et al. | 2023 | 2306.05685 | Core: LLM-as-Judge paradigm |
| MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge | Chen et al. | 2024 | 2402.04788 | Core: Multimodal judge paradigm |
| Generative Verifiers: Reward Modeling as Next-Token Prediction | Zhang et al. | 2024 | 2408.15240 | Core: Verifier design method |
| Chain-of-Thought Prompting Elicits Reasoning in LLMs | Wei et al. | 2022 | 2201.11903 | Context: Reasoning method |
| Self-Consistency Improves Chain of Thought Reasoning | Wang et al. | 2022 | 2203.11171 | Context: Test-time scaling |
| ReAct: Synergizing Reasoning and Acting in Language Models | Yao et al. | 2022 | 2210.03629 | Core: Agent architecture |
| Reflexion: Language Agents with Verbal Reinforcement Learning | Shinn et al. | 2023 | 2303.11366 | Core: Self-improvement |
| Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | Chi et al. | 2023 | 2303.04137 | Core: Robot policy |
| WebArena: A Realistic Web Environment for Building Autonomous Agents | Zhou et al. | 2023 | 2307.13854 | Core: Web benchmark |
| VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks | Koh et al. | 2024 | 2401.13649 | Core: Multimodal web benchmark |
| OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks | Xie et al. | 2024 | 2404.07972 | Core: Desktop benchmark |
| What Matters in Learning from Offline Human Demonstrations (robomimic) | Mandlekar et al. | 2021 | 2108.03298 | Core: Robot benchmark |

## Claim-Citation Self-Check
| Citation | Claim | Supported? | Action | Notes |
|---|---|---|---|---|
| [1] | LLM-as-a-Judge established using strong LLMs for evaluation in open-ended settings | Supported | keep | Directly from Zheng et al. abstract/TLDR |
| [1] | LLM judges exhibit positional bias, phrasing sensitivity, self-preference | Supported | keep | Directly from Zheng et al. TLDR |
| [2] | MLLM-as-a-Judge extends evaluation to multimodal settings | Supported | keep | Directly from Chen et al. abstract |
| [2] | MLLM judges show biases and inconsistencies | Supported | keep | Directly from Chen et al. abstract |
| [3] | Generative verifiers reframe reward modeling as next-token prediction | Supported | keep | Directly from Zhang et al. abstract |
| [4] | CoT prompting enables intermediate reasoning steps | Supported | keep | Directly from Wei et al. abstract |
| [5] | Self-consistency aggregates diverse reasoning paths to improve reliability | Supported | keep | Directly from Wang et al. abstract |
| [6] | ReAct interleaves reasoning traces with actions for grounded decision-making | Supported | keep | Directly from Yao et al. abstract |
| [7] | Reflexion generates reflective summaries from feedback for self-improvement | Supported | keep | Directly from Shinn et al. abstract |
| [7] | Self-improvement pipelines critically depend on verifier quality | Target-paper interpretation | keep | Logical consequence, not a claim about [7] itself |
| [8] | Diffusion Policy learns visuomotor policies from demonstration data | Supported | keep | Directly from Chi et al. abstract |
| [9] | WebArena provides realistic web environment for agent benchmarking | Supported | keep | Directly from Zhou et al. abstract |
| [10] | VisualWebArena extends to multimodal settings with visually grounded tasks and SoM | Supported | keep | Directly from Koh et al. abstract |
| [11] | OSWorld provides real computer desktop environment with multi-app workflows | Supported | keep | Directly from Xie et al. abstract |
| [12] | robomimic provides long-horizon manipulation tasks and demonstration datasets | Supported | keep | Directly from Mandlekar et al. abstract |
| Target paper | Oracle scripts can be lenient or brittle, motivating MLLM-based alternatives | Target-paper interpretation | keep | Target paper motivation, uncited |
| Target paper | Agreement bias as critical limitation of MLLM verifiers | Target-paper interpretation | keep | Target paper motivation, uncited |

## Citation Ledger
| Citation string | Matching paper | In Related Work? | In Final References? | In Self-Check / Uncertain Points? | Scope |
|---|---|---|---|---|---|
| [1] | Zheng et al. 2023 (2306.05685) | ✓ | ✓ | ✓ | LLM-as-a-Judge paradigm, biases |
| [2] | Chen et al. 2024 (2402.04788) | ✓ | ✓ | ✓ | MLLM-as-a-Judge, multimodal evaluation |
| [3] | Zhang et al. 2024 (2408.15240) | ✓ | ✓ | ✓ | Generative verifiers |
| [4] | Wei et al. 2022 (2201.11903) | ✓ | ✓ | ✓ | CoT reasoning |
| [5] | Wang et al. 2022 (2203.11171) | ✓ | ✓ | ✓ | Self-consistency / majority voting |
| [6] | Yao et al. 2022 (2210.03629) | ✓ | ✓ | ✓ | ReAct agent |
| [7] | Shinn et al. 2023 (2303.11366) | ✓ | ✓ | ✓ | Reflexion self-improvement |
| [8] | Chi et al. 2023 (2303.04137) | ✓ | ✓ | ✓ | Diffusion Policy |
| [9] | Zhou et al. 2023 (2307.13854) | ✓ | ✓ | ✓ | WebArena benchmark |
| [10] | Koh et al. 2024 (2401.13649) | ✓ | ✓ | ✓ | VisualWebArena benchmark |
| [11] | Xie et al. 2024 (2404.07972) | ✓ | ✓ | ✓ | OSWorld benchmark |
| [12] | Mandlekar et al. 2021 (2108.03298) | ✓ | ✓ | ✓ | robomimic benchmark |

## Completion Status
| Gate | Status |
|---|---|
| RWEval Citation Format | ✓ Numeric citations in s_text.txt, numbered s_reference.txt |
| Read the Visible Input | ✓ Full Introduction + Problem Setup checked |
| Visible Heading Preservation | ✓ Three themes mapped from embedded signals |
| Visible Coverage Ledger | ✓ All signals have final dispositions |
| Coverage Allocation | ✓ Each theme covers ≥2 named works or field background |
| Must-Not-Drop Prevention | ✓ All 11 must-not-drop signals verified against s_text.txt |
| Named Citation Exactness | ✓ Author-year signals searched before substitutes |
| Reference Validity Guard | ✓ No metadata-unstable papers final-cited; MARG excluded |
| Length Control | ✓ ~475 words, within 450-650 budget |
| Dynamic Citation Budget | ✓ 12 citations, at upper end of 8-12 budget |
| Final Consistency | ✓ All in-text citations in references, all references cited |
| No ground-truth read | ✓ Did not read g_text.txt, g_reference.txt, or ground_truth_related_work |

## Benchmark-Specific Deny / Handle List
| Paper or pattern | Reason | Handling | Theme preserved by |
|---|---|---|---|
| MARG: Multi-Agent Review Generation (D'Arcy et al., 2401.04259) | Known metadata_mismatch in benchmark | screened only, not final-cited | N/A (not relevant to this paper's themes) |

## Uncertain Points
- The input paper contains LaTeX citation commands (`\cite{...}`) for pretraining and RLHF limitations that are hidden (not visible in the plain text). These could not be recovered since the citation keys were not visible. Covered as broad field background with narrowed wording.
- robomimic paper (Mandlekar et al., 2108.03298) is the paper that introduced the robomimic benchmark but uses the title "What Matters in Learning from Offline Human Demonstrations for Robot Manipulation" — the connection is confirmed through the abstract (mentions robomimic-web URL) and section content.
- Set-of-Marks prompting was introduced within the VisualWebArena paper (Koh et al., 2024) as a key technical contribution; no separate SoM paper exists on DeepXiv.
