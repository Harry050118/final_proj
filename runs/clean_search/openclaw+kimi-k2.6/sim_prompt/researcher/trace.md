## Run Metadata
- Date: 2026-05-29
- Search source: DeepXiv only

## Paper Profile
- Topic: Automated scientific research using open-source LLMs as autonomous agents
- Task: End-to-end research automation (literature review, idea generation, manuscript preparation, peer review, paper refinement)
- Method: Iterative preference training framework with CycleResearcher (policy model) and CycleReviewer (reward model), using SimPO for reinforcement learning
- Data type / benchmark: Review-5k (peer review dataset from ICLR 2024), Research-14k (accepted ML papers for SFT)
- Evaluation focus: Simulated peer review scores, MAE reduction vs human reviewers, paper quality assessment
- Main contribution: First open-source iterative framework that closes the research-review-refinement loop via preference optimization
- Boundaries: Does not execute real experiments (fabricated results for training acceleration); focuses on ML research domain

## Visible Related Work Headings
| Heading | Extracted coverage signals | Planned theme |
|---|---|---|
| LLMs for Research | AI Scientist, AutoSurvey, multi-agent research, MLAgentBench, idea generation benchmarks | LLMs for Research and Scientific Discovery |
| AI for Science Discovery | AI4Science, computational scientific discovery, domain-specific agents | AI for Science and Autonomous Discovery |
| Automated Evaluation of Research Papers | GPT-4 peer review, ChatGPT evaluation, Paper SEA, LLM-as-a-Judge, RewardBench, GenRM | Automated Evaluation and LLM-as-a-Judge |

## Visible Coverage Ledger
| Visible signal | Signal type | Exact recovery query | DeepXiv recovery status | Planned use | Final disposition |
|---|---|---|---|---|---|
| AI Scientist (Lu et al.) | named work | "AI Scientist automated scientific discovery" | Found: arXiv:2408.06292 | Core citation for automated research | covered |
| AutoSurvey (Dong et al.) | named work | "automated survey writing LLM" | Found: arXiv:2406.10252 | Literature review automation | covered |
| MLAgentBench (Huang et al.) | named work | "MLAgentBench LLM machine learning experimentation" | Found: arXiv:2310.03302 | Benchmark for research agents | covered |
| ResearchTown | named work | "ResearchTown simulator human research community" | Found: arXiv:2412.17767 | Multi-agent research simulation | intentionally omitted (covered by other multi-agent works) |
| LiRA | named work | "LiRA multi-agent literature review" | Found: arXiv:2510.05138 | Multi-agent survey generation | intentionally omitted (covered by AutoSurvey) |
| GPT-4 peer review (Robertson) | named work | "Robertson GPT-4 peer review assistance" | Found: arXiv:2307.05492 | LLM peer review evaluation | covered |
| ChatGPT evaluation (Hosseini & Horbach) | named work | "Hosseini Horbach ChatGPT peer review" | Found: arXiv:2402.05519 | Research quality evaluation | covered |
| Paper SEA | named work | "Paper SEA automated peer reviewing" | Found: arXiv:2407.12857 | Standardized automated review | covered |
| LLM-as-a-Judge | field background | "LLM-as-a-Judge evaluation survey" | Found: arXiv:2411.15594 | Evaluation paradigm taxonomy | covered |
| RewardBench | named work | "RewardBench reward model evaluation" | Found: arXiv:2410.12784 (JudgeBench) | Reward model evaluation | covered via JudgeBench |
| GenRM | named work | "Generative Reward Model GenRM" | Found: arXiv:2408.15240 | Generative reward modeling | covered |
| SimPO | method | "SimPO Simple Preference Optimization" | Found: arXiv:2405.14734 | Training method (not RW theme) | intentionally omitted (method detail, not prior work) |
| Fast-DetectGPT | named work | "Fast-DetectGPT LLM-generated text detection" | Not found in search | Detection of AI-generated text | unresolved gap |
| AI4Science | field background | "AI4Science scientific discovery" | Found: arXiv:2412.11427, 2505.13259, 2508.14111 | Broad scientific discovery context | covered |
| Iterative preference training / self-improvement | method family | "iterative preference optimization reinforcement learning" | Found multiple | Training paradigm | covered via Shuai et al. |
| IdeaBench | named work | "IdeaBench benchmarking research idea generation" | Found: arXiv:2411.02429 | Idea generation benchmark | covered |
| Multi-agent dialogue for ideation | method | "multi-agent LLM dialogues research ideation" | Found: arXiv:2507.08350 | Ideation methodology | covered |

## Must-Not-Drop Signals
| Signal | Source heading/theme | Required handling | Final status |
|---|---|---|---|
| AI Scientist | LLMs for Research | Cite as key prior automated research system | covered |
| AutoSurvey | LLMs for Research | Cite as literature review automation | covered |
| MLAgentBench | LLMs for Research | Cite as evaluation benchmark | covered |
| GPT-4 peer review (Robertson) | Automated Evaluation | Cite as peer review pilot study | covered |
| ChatGPT evaluation (Hosseini & Horbach) | Automated Evaluation | Cite as quality evaluation study | covered |
| Paper SEA | Automated Evaluation | Cite as standardized review framework | covered |
| LLM-as-a-Judge survey | Automated Evaluation | Cite as evaluation paradigm | covered |
| GenRM | Automated Evaluation | Cite as generative reward modeling | covered |
| AI4Science / Agentic Science | AI for Science | Cite as field background | covered |
| Iterative/multi-agent research | LLMs for Research | Cite as complementary approach | covered |

## Search Queries
| Query | Purpose | Source |
|---|---|---|
| "AI Scientist automated scientific discovery LLM research pipeline" | Recover AI Scientist | Visible named work |
| "LLM multi-agent collaborative writing research idea generation" | Recover multi-agent research | Visible theme |
| "automated survey writing LLM scientific literature retrieval" | Recover AutoSurvey | Visible named work |
| "MLAgentBench LLM machine learning experimentation benchmark" | Recover MLAgentBench | Visible named work |
| "RewardBench reward model evaluation LLM judge" | Recover RewardBench/JudgeBench | Visible named work |
| "Generative Reward Model GenRM next-token prediction" | Recover GenRM | Visible named work |
| "Robertson GPT-4 peer review assistance evaluation" | Recover Robertson et al. | Visible named work |
| "Hosseini Horbach ChatGPT peer review effectiveness" | Recover Hosseini & Horbach | Visible named work |
| "LLM-as-a-Judge evaluation survey" | Recover LLM-as-a-Judge survey | Visible theme |
| "Fast-DetectGPT LLM-generated text detection" | Recover Fast-DetectGPT | Visible named work |
| "SimPO Simple Preference Optimization DPO" | Recover SimPO (method) | Visible method |
| "AI4Science scientific discovery artificial intelligence chemistry biology" | Recover AI4Science background | Visible theme |
| "ResearchTown simulator human research community LLM" | Recover ResearchTown | Visible named work |
| "Si comprehensive human evaluation idea generation language models" | Recover IdeaBench | Visible named work |
| "Paper SEA automated peer reviewing standardization evaluation" | Recover Paper SEA | Visible named work |
| "iterative preference optimization reinforcement learning self-improvement LLM" | Recover iterative training | Visible method family |

## Candidate Screening
| Title | Authors | Year | Source | Label | Reason |
|---|---|---:|---|---|---|
| The AI Scientist | Lu et al. | 2024 | arXiv:2408.06292 | relevant | End-to-end automated ML research; directly supports theme |
| A Vision for Auto Research with LLM Agents | Li et al. | 2025 | arXiv:2504.18765 | relevant | Full lifecycle automation with multi-agent collaboration |
| AutoSurvey | Dong et al. | 2024 | arXiv:2406.10252 | relevant | Automated literature survey generation |
| Exploring Design of Multi-Agent LLM Dialogues for Research Ideation | Gao et al. | 2025 | arXiv:2507.08350 | relevant | Multi-agent dialogue for research ideation |
| MLAgentBench | Huang et al. | 2023 | arXiv:2310.03302 | relevant | Benchmark for ML research agents |
| IdeaBench | Si et al. | 2024 | arXiv:2411.02429 | relevant | Benchmark for research idea generation |
| Enhancing Research Idea Generation through Combinatorial Innovation | Shuai et al. | 2026 | arXiv:2604.20548 | relevant | Iterative multi-agent idea generation |
| ResearchTown | Li et al. | 2024 | arXiv:2412.17767 | weakly relevant | Research community simulation; overlaps with multi-agent theme |
| LiRA | Chen et al. | 2025 | arXiv:2510.05138 | weakly relevant | Multi-agent literature review; overlaps with AutoSurvey |
| Towards Scientific Discovery with Generative AI | Song et al. | 2024 | arXiv:2412.11427 | relevant | Survey of generative AI for scientific discovery |
| From Automation to Autonomy | Zhang et al. | 2025 | arXiv:2505.13259 | relevant | Taxonomy of LLM autonomy in scientific discovery |
| From AI for Science to Agentic Science | Zhang et al. | 2025 | arXiv:2508.14111 | relevant | Unified framework for autonomous scientific discovery |
| GPT4 is Slightly Helpful for Peer-Review Assistance | Robertson et al. | 2023 | arXiv:2307.05492 | relevant | GPT-4 peer review pilot study |
| Can ChatGPT evaluate research quality? | Hosseini & Horbach | 2024 | arXiv:2402.05519 | relevant | ChatGPT research quality evaluation |
| Automated Peer Reviewing in Paper SEA | Liu et al. | 2024 | arXiv:2407.12857 | relevant | Standardized automated peer review |
| A Survey on LLM-as-a-Judge | Zheng et al. | 2024 | arXiv:2411.15594 | relevant | Comprehensive survey of LLM evaluation |
| JudgeBench | Tan et al. | 2024 | arXiv:2410.12784 | relevant | Benchmark for LLM-based judges |
| Generative Verifiers: Reward Modeling as Next-Token Prediction | Zhang et al. | 2024 | arXiv:2408.15240 | relevant | Generative reward modeling |
| SimPO | Meng et al. | 2024 | arXiv:2405.14734 | weakly relevant | Training method; not a prior work theme |
| PRE: A Peer Review Based LLM Evaluator | Liu et al. | 2024 | arXiv:2401.15641 | weakly relevant | Peer-review-based LLM evaluation; overlaps with SEA |

## Planned Themes
| Theme | Input signal it maps to | Core/context citations | Notes |
|---|---|---|---|
| LLMs for Research and Scientific Discovery | Visible heading "LLMs for Research" | [1, 2, 3, 4, 5, 6, 7] | Covers automated research pipelines, multi-agent collaboration, survey generation, benchmarks |
| AI for Science and Autonomous Discovery | Visible heading "AI for Science Discovery" | [8, 9, 10] | Broader field context from tool-based AI to autonomous agents |
| Automated Evaluation of Research Papers and LLM-as-a-Judge | Visible heading "Automated Evaluation of Research Papers" | [11, 12, 13, 14, 15, 16] | Peer review automation, quality evaluation, LLM-as-judge paradigm, generative reward models |

## Coverage Allocation
| Heading/theme | Recoverable named/background signals | Covered in final text | Unresolved gaps |
|---|---|---|---|
| LLMs for Research | AI Scientist, AutoSurvey, MLAgentBench, ResearchTown, LiRA, IdeaBench, multi-agent ideation | AI Scientist, AutoSurvey, MLAgentBench, multi-agent ideation, IdeaBench, iterative idea generation | ResearchTown (intentionally omitted as overlapping), LiRA (intentionally omitted as overlapping with AutoSurvey) |
| AI for Science Discovery | AI4Science surveys, agentic science | Three survey papers covering progression from tools to autonomy | None major |
| Automated Evaluation | Robertson, Hosseini&Horbach, Paper SEA, LLM-as-a-Judge, RewardBench, GenRM, Fast-DetectGPT | Robertson, Hosseini&Horbach, Paper SEA, LLM-as-a-Judge, JudgeBench, GenRM | Fast-DetectGPT (not found), RewardBench (covered via JudgeBench as related benchmark) |

## Length Control
- Target word budget: 400-500 words
- Estimated visible Related Work length: ~450 words
- Final word count: ~480 words
- Status: within budget

## Final Cited Papers
| Title | Authors | Year | Source | Citation role |
|---|---|---:|---|---|
| The AI Scientist | Lu et al. | 2024 | arXiv:2408.06292 | Core automated research system |
| A Vision for Auto Research with LLM Agents | Li et al. | 2025 | arXiv:2504.18765 | Multi-agent full lifecycle automation |
| AutoSurvey | Dong et al. | 2024 | arXiv:2406.10252 | Automated literature review |
| Exploring Design of Multi-Agent LLM Dialogues for Research Ideation | Gao et al. | 2025 | arXiv:2507.08350 | Multi-agent ideation methodology |
| MLAgentBench | Huang et al. | 2023 | arXiv:2310.03302 | Research agent benchmark |
| IdeaBench | Si et al. | 2024 | arXiv:2411.02429 | Idea generation benchmark |
| Enhancing Research Idea Generation through Combinatorial Innovation | Shuai et al. | 2026 | arXiv:2604.20548 | Iterative multi-agent idea generation |
| Towards Scientific Discovery with Generative AI | Song et al. | 2024 | arXiv:2412.11427 | Field background survey |
| From Automation to Autonomy | Zhang et al. | 2025 | arXiv:2505.13259 | Autonomy taxonomy |
| From AI for Science to Agentic Science | Zhang et al. | 2025 | arXiv:2508.14111 | Agentic science framework |
| GPT4 is Slightly Helpful for Peer-Review Assistance | Robertson et al. | 2023 | arXiv:2307.05492 | Peer review pilot study |
| Can ChatGPT evaluate research quality? | Hosseini & Horbach | 2024 | arXiv:2402.05519 | Quality evaluation study |
| Automated Peer Reviewing in Paper SEA | Liu et al. | 2024 | arXiv:2407.12857 | Standardized review framework |
| A Survey on LLM-as-a-Judge | Zheng et al. | 2024 | arXiv:2411.15594 | Evaluation paradigm survey |
| JudgeBench | Tan et al. | 2024 | arXiv:2410.12784 | Judge evaluation benchmark |
| Generative Verifiers: Reward Modeling as Next-Token Prediction | Zhang et al. | 2024 | arXiv:2408.15240 | Generative reward modeling |

## Claim-Citation Self-Check
| Citation | Claim | Supported? | Action | Notes |
|---|---|---|---|---|
| [1] | "fully automated, prompt-driven pipeline for open-ended machine learning discovery" | Yes | Keep | TLDR confirms end-to-end automation |
| [2] | "multi-agent frameworks...coordinate the full research lifecycle" | Yes | Keep | TLDR confirms full lifecycle via multi-agent collaboration |
| [3] | "retrieval-augmented pipelines synthesize comprehensive literature reviews" | Yes | Keep | TLDR confirms RAG-based survey generation |
| [4] | "multi-agent dialogue designs that improve research ideation through iterative critique and revision loops" | Yes | Keep | TLDR confirms ideation-critique-revision loops |
| [5] | "benchmarks...evaluate language agents on machine learning experimentation tasks" | Yes | Keep | TLDR confirms ML experimentation benchmarking |
| [6] | "LLM-driven idea generation through structured profiling and quantitative scoring frameworks" | Yes | Keep | TLDR confirms profiling and Insight Score |
| [7] | "iterative self-improvement mechanisms that continuously refine research outputs through feedback" | Yes | Keep | TLDR confirms iterative multi-agent search |
| [8] | "Early applications treated AI primarily as a passive analytical tool" | Yes (narrowed) | Keep | Survey covers tool-based AI stage |
| [9] | "evolution from task-specific automation toward autonomous scientific agents" | Yes | Keep | Survey taxonomy confirms progression |
| [10] | "core capabilities including planning, tool use, memory, and collaboration" | Yes | Keep | TLDR confirms five core capabilities |
| [11] | "generated reviews can achieve comparable surface-level helpfulness, but exhibit higher variance" | Yes | Keep | TLDR confirms comparable helpfulness with higher variance |
| [12] | "weak individual correlation with expert judgments and limitations in fine-grained assessment" | Yes | Keep | TLDR confirms weak correlation (r=0.281) |
| [13] | "structured frameworks for generating constructive feedback and measuring content consistency" | Yes | Keep | TLDR confirms standardization and mismatch score |
| [14] | "taxonomies of evaluation scope, reasoning mechanism, and reliability challenges" | Yes | Keep | TLDR confirms formal taxonomy |
| [15] | "even advanced models struggle to distinguish factually correct responses from subtly flawed ones" | Yes | Keep | TLDR confirms GPT-4o slightly above random |
| [16] | "Generative reward models trained via next-token prediction...leveraging chain-of-thought reasoning" | Yes | Keep | TLDR confirms next-token prediction and CoT verification |

## Citation Ledger
| Citation string | Matching paper | In Related Work? | In Final References? | In Self-Check? | Scope |
|---|---|---|---|---|---|
| [1] | Lu et al. 2024 | Yes | Yes | Yes | Core |
| [2] | Li et al. 2025 | Yes | Yes | Yes | Core |
| [3] | Dong et al. 2024 | Yes | Yes | Yes | Core |
| [4] | Gao et al. 2025 | Yes | Yes | Yes | Core |
| [5] | Huang et al. 2023 | Yes | Yes | Yes | Core |
| [6] | Si et al. 2024 | Yes | Yes | Yes | Core |
| [7] | Shuai et al. 2026 | Yes | Yes | Yes | Core |
| [8] | Song et al. 2024 | Yes | Yes | Yes | Context |
| [9] | Zhang et al. 2025 | Yes | Yes | Yes | Context |
| [10] | Zhang et al. 2025 | Yes | Yes | Yes | Context |
| [11] | Robertson et al. 2023 | Yes | Yes | Yes | Core |
| [12] | Hosseini & Horbach 2024 | Yes | Yes | Yes | Core |
| [13] | Liu et al. 2024 | Yes | Yes | Yes | Core |
| [14] | Zheng et al. 2024 | Yes | Yes | Yes | Core |
| [15] | Tan et al. 2024 | Yes | Yes | Yes | Core |
| [16] | Zhang et al. 2024 | Yes | Yes | Yes | Core |

## Completion Status
| Gate | Status |
|---|---|
| Visible Coverage Ledger | Pass - all signals have disposition |
| Coverage Allocation | Pass - each heading has minimum coverage |
| Missing-Point Prevention | Pass - all 10 must-not-drop signals covered |
| Named Citation Exactness | Pass - exact recovery attempted for all named works |
| Reference Validity Guard | Pass - all citations have stable metadata |
| Length Control | Pass - within 400-500 word budget |
| Dynamic Citation Budget | Pass - 16 citations (within 12-18 range) |
| Final Consistency | Pass - in-text, references, self-check agree |

## Benchmark-Specific Deny / Handle List
| Paper or pattern | Reason | Handling | Theme preserved by |
|---|---|---|---|
| MARG (D'Arcy et al., arXiv:2401.04259) | Metadata mismatch warning in SKILL.md | Not cited | Paper SEA, Robertson et al. |
| Fast-DetectGPT | Not recovered via DeepXiv search | Not cited | N/A (detection is peripheral to core themes) |
| SimPO | Method detail, not prior work | Not cited | N/A (training method of target paper) |

## Uncertain Points
- RewardBench was searched but JudgeBench was recovered instead. Both are benchmarks for evaluating LLM judges/reward models. JudgeBench was used as the citation since it directly supports the evaluation theme.
- ResearchTown and LiRA were recovered but intentionally omitted to avoid redundancy with other multi-agent and survey-generation citations.
- PRE (Peer Review Evaluator) was recovered but omitted as Paper SEA provides stronger coverage of the automated peer review theme.
