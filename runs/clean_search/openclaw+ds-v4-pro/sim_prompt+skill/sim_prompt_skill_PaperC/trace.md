## Run Metadata
- Date: 2026-05-27
- Search source: DeepXiv only
- Input paper: papers/12299.txt (MobileIPL)
- Candidate papers: none (clean search)
- Active citation budget: 11 (8-12 range, focused method paper with three themes)

## Paper Profile
- Topic: VLM-based mobile GUI agents, iterative self-training, preference learning
- Task: Autonomous mobile GUI interaction using Chain of Action-Planning Thoughts (CoaT)
- Method: MobileIPL — Iterative Preference Learning framework combining CoaT-tree MCTS sampling, rule-based reward backpropagation, Thinking-level DPO (T-DPO), and three-stage instruction evolution
- Data type / benchmark: Mobile GUI screenshots/trajectories — AITZ (from AITW), AMEX, AndroidControl
- Evaluation focus: Step Accuracy, action type matching, OOD generalization, low-resource efficiency
- Main contribution: A self-training framework that (1) builds CoaT-tree through iterative MCTS sampling, (2) constructs T-DPO pairs via rule-based reward backpropagation without manual step annotation, (3) introduces instruction evolution for diversity
- Boundaries: Mobile GUI domain only; not continual pretraining; Qwen2-VL-7B backbone; not using PRM; not general LLM reasoning; not text-only tasks

## Visible Related Work Headings
No explicit Related Work section present. Related work signals are embedded in the Introduction and Methodology sections.

## Visible Coverage Ledger
| Visible signal | Signal type | Exact recovery query | DeepXiv recovery status | Planned use | Final disposition |
|---|---|---|---|---|---|
| AITZ / CoAT paradigm | named work | "Chain of Action-Planning Thoughts CoaT VLM mobile GUI agents AITZ" | Found: 2403.02713 (Zhang et al. 2024) | Core GUI agent citation | covered |
| Self-training with final answer reward | field background | N/A (general domain context) | — | Context sentence in self-training theme | covered (uncited field background) |
| ReST-MCTS | named work | "ReST-MCTS process reward model self-training reasoning step-level" | Found: 2406.03816 (Zhang et al. 2024) | Core self-training citation | covered |
| PRM requiring manual annotation | field background | N/A (general observation) | — | Context sentence | covered (uncited field background) |
| CogAgent | named work | "CogAgent visual GUI agent foundation model mobile" | Found: 2312.08914 (Hong et al. 2023) | Core GUI agent citation | covered |
| Auto-GUI / Auto-UI | named work | "AUTO-GUI mobile agent autonomous GUI multimodal action" | Found: 2309.11436 (Zhang & Zhang 2023) | Core GUI agent citation | covered |
| OS-Atlas | named work | "OS-Atlas GUI grounding agent foundation model" | Found: 2410.23218 (Wu et al. 2024) | Core GUI agent citation | covered |
| UI-TARS | named work | "UI-TARS GUI agent model pioneering automated" | Found: 2501.12326 (Qin et al. 2025) | Core GUI agent citation | covered |
| UGround | named work | "UGround GUI grounding visual agent model" | Found: 2410.05243 (Gou et al. 2024) | Core GUI grounding citation | covered |
| Falcon-UI | named work | "Falcon-UI GUI agent multimodal understanding mobile" | Found: 2412.09362 | Screened; lower priority | intentionally omitted (lower relevance; budget-limited) |
| SphAgent | named work | "SphAgent mobile GUI agent" | NOT FOUND on DeepXiv | Context mention | unresolved gap |
| FedMobileAgent | named work | "FedMobileAgent mobile GUI agent" | NOT FOUND on DeepXiv | Context mention | unresolved gap |
| SPO-Chain | named work | "SPO-Chain chain-of-thought MCTS preference optimization" | Not found by exact name; related: CPO (2406.09136), SVPO (2406.10858), MCTS-DPO (2405.00451) | Context mention | unresolved gap (no exact match) |
| GRPO | named work | "GRPO Group Relative Policy Optimization reinforcement learning LLM" | Found but not in DeepXiv as canonical paper for GUI | Screened | intentionally omitted (not a Related Work theme; experimental baseline in target paper) |
| AITW | named work | "Android in the Wild AITW mobile GUI dataset benchmark" | Found: 2307.10088 (Rawles et al. 2023) | Context dataset | intentionally omitted (covered indirectly via AITZ paper; budget-limited) |
| AMEX | named work | — | Found: 2407.17490 | Context dataset | intentionally omitted (budget-limited; dataset rather than method) |
| AndroidControl | named work | "AndroidControl mobile GUI benchmark" | Found: 2406.03679 (Li et al. 2024) | Context benchmark citation | covered |
| DPO | named work | "Direct Preference Optimization DPO language model RLHF Rafailov" | Found: 2305.18290 (Rafailov et al. 2023) | Core preference optimization citation | covered |
| Multi-turn thinking / CoaT | field background | (covered by AITZ paper) | — | — | covered |
| VLM-based mobile agents | field background | (covered by multiple GUI agent papers) | — | — | covered |
| Self-training with MCTS | field background | (covered by MCTS-DPO and ReST-MCTS*) | — | — | covered |
| Instruction diversity for SFT | target motivation | (target paper's own contribution) | — | Target-paper motivation | covered (uncited target motivation) |
| Iterative preference learning for GUI | target motivation | (target paper's own contribution) | — | Target-paper motivation | covered (uncited target motivation) |

## Must-Not-Drop Signals
| Signal | Source heading/theme | Required handling | Final status |
|---|---|---|---|
| AITZ/CoAT paradigm | VLM-Based Mobile GUI Agents | Cite as core named work | covered [3] |
| ReST-MCTS* | Self-Training | Cite as core named work | covered [8] |
| MCTS + DPO for step-level reasoning | Self-Training / Preference Optimization | Cite as core named work | covered [9] |
| DPO | Preference Optimization | Cite as foundational method | covered [10] |
| VLM GUI agents (CogAgent, Auto-UI) | VLM-Based Mobile GUI Agents | Cite as field context | covered [1, 2] |
| Foundation GUI models (OS-Atlas, UI-TARS) | VLM-Based Mobile GUI Agents | Cite as recent advances | covered [4, 5] |
| GUI grounding (UGround) | VLM-Based Mobile GUI Agents | Cite as grounding context | covered [6] |
| AndroidControl benchmark | VLM-Based Mobile GUI Agents | Cite as evaluation context | covered [7] |
| CPO chain-level preference | Preference Optimization | Cite as related preference method | covered [11] |

## Search Queries
| Query | Purpose | Source |
|---|---|---|
| "Chain of Action-Planning Thoughts CoaT VLM mobile GUI agents AITZ" | Exact recovery: AITZ/CoAT | Visible named work |
| "ReST-MCTS process reward model self-training reasoning step-level" | Exact recovery: ReST-MCTS | Visible named work |
| "Auto-GUI mobile GUI agent autonomous task completion" | Exact recovery: Auto-UI | Visible named work |
| "CogAgent visual GUI agent foundation model mobile" | Exact recovery: CogAgent | Visible named work |
| "OS-Atlas GUI grounding agent foundation model" | Exact recovery: OS-Atlas | Visible named work |
| "UI-TARS GUI agent model pioneering automated" | Exact recovery: UI-TARS | Visible named work |
| "UGround GUI grounding visual agent model" | Exact recovery: UGround | Visible named work |
| "Falcon-UI GUI agent multimodal understanding mobile" | Exact recovery: Falcon-UI | Visible named work |
| "SphAgent mobile GUI agent" | Exact recovery: SphAgent | Visible named work |
| "FedMobileAgent mobile GUI agent" | Exact recovery: FedMobileAgent | Visible named work |
| "SPO-Chain chain-of-thought MCTS preference optimization" | Exact recovery: SPO-Chain | Visible named work |
| "GRPO Group Relative Policy Optimization reinforcement learning LLM" | Exact recovery: GRPO | Visible named work |
| "Android in the Wild AITW mobile GUI dataset benchmark" | Exact recovery: AITW | Visible named work |
| "AndroidControl mobile GUI benchmark" | Exact recovery: AndroidControl | Visible named work |
| "Direct Preference Optimization DPO language model RLHF Rafailov" | Exact recovery: DPO | Visible named work |
| "MCTS reasoning iterative preference learning LLM" (result 2405.00451) | Broad discovery: MCTS + DPO | Field background |
| "Chain of Preference Optimization improving chain-of-thought" (result 2406.09136) | Broad discovery: chain-level DPO | Field background |
| "Android in the Zoo AITZ benchmark" (result 2407.17490) | Broad discovery: AMEX | Field background |

## Candidate Screening
| Title | Authors | Year | Source | Label | Reason |
|---|---|---|---|---|---|
| Android in the Zoo: Chain-of-Action-Thought for GUI Agents | Zhang et al. | 2024 | DeepXiv 2403.02713 | relevant | Core CoAT paradigm and AITZ benchmark |
| CogAgent: A Visual Language Model for GUI Agents | Hong et al. | 2023 | DeepXiv 2312.08914 | relevant | Foundational VLM GUI agent |
| You Only Look at Screens: Multimodal Chain-of-Action Agents (Auto-UI) | Zhang & Zhang | 2023 | DeepXiv 2309.11436 | relevant | Chain-of-action GUI agent, AITW benchmark |
| OS-ATLAS: A Foundation Action Model for Generalist GUI Agents | Wu et al. | 2024 | DeepXiv 2410.23218 | relevant | Foundation GUI model with cross-platform grounding |
| UI-TARS: Pioneering Automated GUI Interaction with Native Agents | Qin et al. | 2025 | DeepXiv 2501.12326 | relevant | Native end-to-end GUI agent with System-2 reasoning |
| Navigating the Digital World as Humans Do (UGround) | Gou et al. | 2024 | DeepXiv 2410.05243 | relevant | Universal visual grounding for GUI agents |
| ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search | Zhang et al. | 2024 | DeepXiv 2406.03816 | relevant | Process reward MCTS self-training |
| Monte Carlo Tree Search Boosts Reasoning via Iterative Preference Learning | Xie et al. | 2024 | DeepXiv 2405.00451 | relevant | MCTS + DPO for step-level reasoning |
| Direct Preference Optimization: Your Language Model is Secretly a Reward Model | Rafailov et al. | 2023 | DeepXiv 2305.18290 | relevant | Foundational DPO method |
| Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs | Zhang et al. | 2024 | DeepXiv 2406.09136 | relevant | Chain-level preference optimization from search trees |
| On the Effects of Data Scale on UI Control Agents (AndroidControl) | Li et al. | 2024 | DeepXiv 2406.03679 | weakly relevant | Benchmark paper; provides evaluation context |
| Falcon-UI: Understanding GUI Before Following User Instructions | — | 2024 | DeepXiv 2412.09362 | weakly relevant | Screened; lower priority for budget |
| Android in the Wild (AITW) | Rawles et al. | 2023 | DeepXiv 2307.10088 | weakly relevant | Dataset paper; covered indirectly via AITZ |
| AMEX: Android Multi-annotation Expo Dataset | — | 2024 | DeepXiv 2407.17490 | weakly relevant | Dataset paper; budget-limited |
| Step-level Value Preference Optimization for Mathematical Reasoning | — | 2024 | DeepXiv 2406.10858 | weakly relevant | Math domain; screened for relevance to GUI |
| Does Chain-of-Thought Reasoning Help Mobile GUI Agent? | — | 2025 | DeepXiv 2503.16788 | screened | Empirical study; not a primary method/system citation |

## Planned Themes
| Theme | Input signal it maps to | Core/context citations | Notes |
|---|---|---|---|
| VLM-Based Mobile GUI Agents | CoAT, CogAgent, Auto-UI, OS-Atlas, UI-TARS, UGround, AndroidControl | [1-7] core | Covers named systems visible in paper |
| Self-Training with Process-Level Rewards | ReST-MCTS, MCTS-DPO, self-training, PRM | [8, 9] core | Covers MCTS-based self-training methods |
| Preference Optimization for Step-Level Reasoning | DPO, CPO, step-level preference | [10, 11] core | Covers DPO and chain-level preference variants |

## Coverage Allocation
| Heading/theme | Recoverable named/background signals | Covered in final text | Unresolved gaps |
|---|---|---|---|
| VLM-Based Mobile GUI Agents | AITZ, CogAgent, Auto-UI, OS-Atlas, UI-TARS, UGround, AndroidControl, VLM agents field | All covered [1-7] + field background | SphAgent (not on DeepXiv), FedMobileAgent (not on DeepXiv) |
| Self-Training with Process-Level Rewards | ReST-MCTS*, MCTS-DPO, self-training field, PRM context | Both named works [8, 9] + field background | SPO-Chain (no exact match on DeepXiv) |
| Preference Optimization for Step-Level Reasoning | DPO, CPO, step-level preference field | Both named works [10, 11] + target motivation | — |

## Length Control
- Target word budget: 450-650 words (focused method paper, three themes)
- Estimated visible signal density: Moderate (no explicit Related Work section)
- Final word count: 588
- Status: within target

## Final Cited Papers
| # | Title | Authors | Year | Source | Citation role |
|---|---|---|---|---|---|
| [1] | CogAgent: A Visual Language Model for GUI Agents | Hong et al. | 2023 | 2312.08914 | Core: VLM GUI agent foundation |
| [2] | You Only Look at Screens: Multimodal Chain-of-Action Agents | Zhang & Zhang | 2023 | 2309.11436 | Core: Chain-of-action GUI agent |
| [3] | Android in the Zoo: Chain-of-Action-Thought for GUI Agents | Zhang et al. | 2024 | 2403.02713 | Core: CoAT paradigm and AITZ |
| [4] | OS-ATLAS: A Foundation Action Model for Generalist GUI Agents | Wu et al. | 2024 | 2410.23218 | Core: Foundation GUI model |
| [5] | UI-TARS: Pioneering Automated GUI Interaction with Native Agents | Qin et al. | 2025 | 2501.12326 | Core: Native end-to-end GUI agent |
| [6] | Navigating the Digital World as Humans Do (UGround) | Gou et al. | 2024 | 2410.05243 | Core: GUI visual grounding |
| [7] | On the Effects of Data Scale on UI Control Agents | Li et al. | 2024 | 2406.03679 | Context: AndroidControl benchmark |
| [8] | ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search | Zhang et al. | 2024 | 2406.03816 | Core: Process reward MCTS self-training |
| [9] | Monte Carlo Tree Search Boosts Reasoning via Iterative Preference Learning | Xie et al. | 2024 | 2405.00451 | Core: MCTS + DPO step-level reasoning |
| [10] | Direct Preference Optimization: Your Language Model is Secretly a Reward Model | Rafailov et al. | 2023 | 2305.18290 | Core: Foundational DPO |
| [11] | Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs | Zhang et al. | 2024 | 2406.09136 | Core: Chain-level preference optimization |

## Claim-Citation Self-Check
| Citation | Claim | Supported? | Action | Notes |
|---|---|---|---|---|
| [1] | CogAgent introduced an 18B-parameter VLM with high-resolution screen encoding, achieving strong performance on AITW | Supported | keep | Confirmed by DeepXiv metadata/title/abstract |
| [2] | Auto-UI proposed a multimodal chain-of-action approach fusing historical action sequences with future action plans | Supported | keep | Confirmed by DeepXiv metadata/TLDR |
| [3] | CoAT paradigm introduced alongside AITZ dataset, capturing semantic reasoning through screen context, action thinking, target, and outcome | Supported | keep | Confirmed by DeepXiv metadata/TLDR |
| [4] | OS-Atlas provides a unified grounding corpus spanning desktop, mobile, and web platforms | Supported | keep | Confirmed by DeepXiv metadata |
| [5] | UI-TARS integrates perception, System-2 reasoning, and unified action modeling into an end-to-end native agent | Supported | keep | Confirmed by DeepXiv metadata/TLDR |
| [6] | UGround demonstrated that purely visual grounding can match or exceed agents relying on text-based representations | Supported | keep | Confirmed by DeepXiv metadata/TLDR |
| [7] | AndroidControl dataset introduced a diverse benchmark with high-level and low-level task instructions | Supported | keep | Confirmed by DeepXiv metadata/TLDR |
| [8] | ReST-MCTS* integrates process reward guidance with MCTS, inferring per-step rewards through tree-search rollouts | Supported | keep | Confirmed by DeepXiv metadata/TLDR |
| [9] | Xie et al. leveraged MCTS to decompose instance-level rewards into step-level preference signals and applied DPO | Supported | keep | Confirmed by DeepXiv metadata/TLDR |
| [10] | DPO reformulated RLHF as a closed-form binary classification objective | Supported | keep | Confirmed by DeepXiv metadata/TLDR |
| [11] | CPO constructs step-level preference pairs from tree-of-thought search trees | Supported | keep | Confirmed by DeepXiv metadata/TLDR |
| — | "most existing agents are trained on static demonstration data" | Target-paper interpretation | keep | Target-paper motivation, uncited |
| — | "they have primarily been developed in text-based reasoning domains" | Target-paper interpretation | keep | Target-paper motivation, uncited |
| — | "they rely on structured search trees with clear win/lose branching" | Target-paper interpretation | keep | Target-paper motivation, uncited |
| — | "This motivates the target paper's approach..." | Target-paper interpretation | keep | Explicitly target-paper motivation |

## Citation Ledger
| Citation string | Matching paper | In Related Work? | In Final References? | In Self-Check? | Scope |
|---|---|---|---|---|---|
| [1] | CogAgent (Hong et al. 2023) | ✓ | ✓ | ✓ | Core GUI agent |
| [2] | Auto-UI (Zhang & Zhang 2023) | ✓ | ✓ | ✓ | Core GUI agent |
| [3] | AITZ/CoAT (Zhang et al. 2024) | ✓ | ✓ | ✓ | Core GUI agent |
| [4] | OS-Atlas (Wu et al. 2024) | ✓ | ✓ | ✓ | Core GUI agent |
| [5] | UI-TARS (Qin et al. 2025) | ✓ | ✓ | ✓ | Core GUI agent |
| [6] | UGround (Gou et al. 2024) | ✓ | ✓ | ✓ | Core grounding |
| [7] | AndroidControl (Li et al. 2024) | ✓ | ✓ | ✓ | Context benchmark |
| [8] | ReST-MCTS* (Zhang et al. 2024) | ✓ | ✓ | ✓ | Core self-training |
| [9] | MCTS-DPO (Xie et al. 2024) | ✓ | ✓ | ✓ | Core self-training |
| [10] | DPO (Rafailov et al. 2023) | ✓ | ✓ | ✓ | Core preference |
| [11] | CPO (Zhang et al. 2024) | ✓ | ✓ | ✓ | Core preference |

## Completion Status
| Gate | Status |
|---|---|
| RWEval Citation Format | ✓ Numeric citations in s_text.txt, matching numbered references in s_reference.txt |
| Read the Visible Input | ✓ Full paper checked; no explicit Related Work section |
| Visible Heading Preservation | ✓ Three themes derived from Introduction signals |
| Visible Coverage Ledger | ✓ All visible signals have final dispositions |
| Coverage Allocation | ✓ Each theme covers ≥2 named/background signals |
| Must-Not-Drop Signals | ✓ All 9 must-not-drop signals covered |
| Named Citation Exactness | ✓ Author-year signals searched exactly; unresolved gaps recorded |
| Reference Validity Guard | ✓ All metadata verified; no unstable references |
| Length Control | ✓ 588 words within 450-650 target |
| Dynamic Citation Budget | ✓ 11 papers within 8-12 budget |
| Final Consistency | ✓ All citations appear in both text and references; self-check complete |
| No ground truth access | ✓ Did not read g_text.txt, g_reference.txt, or ground_truth_related_work |

## Benchmark-Specific Deny / Handle List
| Paper or pattern | Reason | Handling | Theme preserved by |
|---|---|---|---|
| MARG: Multi-Agent Review Generation (D'Arcy et al., 2401.04259) | Benchmark metadata_mismatch history | Not screened/not cited (not relevant to this paper's domain) | N/A (mobile GUI domain) |

## Uncertain Points
- SphAgent: Not recovered on DeepXiv. Appears as a baseline in the target paper's experiments. Recorded as unresolved gap; not cited. GUI agent theme preserved through CogAgent, Auto-UI, OS-Atlas, UI-TARS, UGround.
- FedMobileAgent: Not recovered on DeepXiv. Recorded as unresolved gap; not cited. Not essential to Related Work themes.
- SPO-Chain: No exact match on DeepXiv. The target paper's mention of SPO-Chain as an MCTS-style baseline may refer to Chain of Preference Optimization (CPO, [11]) or Step-level Value Preference Optimization (2406.10858), but exact identity is uncertain. Recorded as unresolved gap. Self-training theme preserved through ReST-MCTS* [8] and MCTS-DPO [9].
- No explicit Related Work section in the input paper, so theme planning was derived from Introduction signals rather than following visible headings.
