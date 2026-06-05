## Run Metadata
- Date: 2026-06-05
- Search source: DeepXiv only
- Input condition: A1 Clean Search
- Output directory: runs/clean_search/test

## Paper Profile
- Topic: Output diversity and mode collapse (Artificial Hivemind) in large language models for open-ended queries; pluralistic preference alignment
- Task: Evaluating intra-model and inter-model output diversity; evaluating calibration of LMs, reward models, and LM judges against human preferences on alternative open-ended responses
- Method: Dataset construction (mining open-ended queries from WildChat), taxonomy development, pairwise embedding similarity analysis, dense human annotation collection (25 annotators per example), correlation analysis between model scores and human ratings
- Data type / benchmark: INFINITY-CHAT — 26K real-world open-ended queries with 6 top-level and 17 subcategories; 33,250 human annotations (absolute ratings + pairwise preferences); 70+ LMs evaluated
- Evaluation focus: Intra-model repetition (pairwise embedding similarity), inter-model homogeneity (cross-model similarity), model-human rating correlation on similar-quality and high-disagreement subsets
- Main contribution: INFINITY-CHAT dataset; first comprehensive taxonomy of open-ended LM queries; discovery of the Artificial Hivemind effect (intra-model + inter-model homogeneity); dense human annotations for studying idiosyncratic preferences; analysis of LM/reward model/judge miscalibration
- Boundaries: Does not claim causal analysis of inter-model homogeneity; does not propose training interventions to fix mode collapse; does not claim superiority of any specific model

## Visible Related Work Headings
No visible Related Work section in the input paper. Themes were inferred from body text signals.

## Visible Coverage Ledger
| Visible signal | Signal type | Exact recovery query | DeepXiv recovery status | Planned use | Final disposition |
|---|---|---|---|---|---|
| WildChat | named works | "WildChat dataset real-world user queries" | Recovered (2405.01470) | Theme 2 core citation | covered |
| HelpSteer3 | named works | "HelpSteer alignment dataset human preference" | Recovered (2311.09528) | Context mention | narrowed — mentioned indirectly via preference dataset gap discussion |
| RewardBench | named works | "RewardBench reward model evaluation benchmark" | Recovered (2403.13787) | Theme 3 core citation | covered |
| min-p decoding | named works | "min-p decoding diversity language model" | Recovered (2407.01082) | Theme 1 core citation | covered |
| Mode collapse / intra-model repetition | field background | "mode collapse output diversity language model" | Recovered (multiple) | Theme 1 field background | covered |
| Inter-model homogeneity | field background | "inter-model homogeneity large language models" | Partially recovered (Representational Similarity paper) | Theme 1 target motivation gap | narrowed — limited prior work found on inter-model homogeneity |
| Human preference alignment / pluralistic | field background | "human preference alignment pluralistic diverse responses" | Recovered (multiple) | Theme 3 field background | covered |
| LM judges | field background | "LLM-as-judge evaluation alignment" | Recovered (multiple) | Theme 3 context | covered |
| Dense human annotation (idiosyncratic preferences) | target motivation | "distributional preference learning annotator disagreement" | Recovered (2410.14632) | Theme 3 target motivation gap | covered |
| Prior diversity benchmarks (persona, storytelling) | field background | "creativity diversity benchmark open-ended generation" | Recovered (2504.05228) | Theme 1 field background | covered |
| RLHF impact on creativity | field background | "RLHF alignment creativity diversity language model" | Recovered (2406.05587) | Theme 1 field background | covered |
| Prompt format diversity collapse | field background | "diversity collapse instruction format LLM" | Recovered (2505.18949) | Theme 1 field background | covered |
| Linguistic diversity benchmarking | field background | "benchmarking linguistic diversity LLM" | Recovered (2412.10271) | Theme 1 field background | covered |
| LMSYS-Chat-1M | named works | Not explicitly recovered — found via diversity search | Recovered (2309.11998) | Theme 2 core citation | covered |
| Common Crawl | field background | Not searched (source dataset, not a paper) | N/A | Intentionally omitted | intentionally omitted — infrastructure, not prior work |
| HelpSteer (sparse labels, 3 annotators) | named works | "HelpSteer alignment dataset" | Recovered (2311.09528) | Not directly cited | narrowed — mentioned as context for sparse annotation gap |

## Must-Not-Drop Signals
| Signal | Source heading/theme | Required handling | Final status |
|---|---|---|---|
| WildChat dataset | Dataset construction | Cite as source for INFINITY-CHAT query mining | covered [7] |
| Mode collapse / intra-model repetition studies | Artificial Hivemind section | Cover prior diversity evaluation work | covered [1,2,3,4,5] |
| min-p decoding | Artificial Hivemind section | Cite as diversity-oriented decoding | covered [6] |
| RewardBench | Evaluation section | Cite as reward model benchmark | covered [14] |
| Human preference alignment / pluralistic | Evaluation section | Cover annotator disagreement and pluralistic alignment | covered [9,10,11,12,13] |
| LM judges | Evaluation section | Cover LLM-as-judge paradigms | covered [14] |
| Dense human annotation gap | Motivation throughout | Position as gap in existing work | covered (target motivation sentences) |
| Inter-model homogeneity gap | Artificial Hivemind section | Note as underexplored in prior work | covered (target motivation sentence) |
| HelpSteer sparse annotation gap | Evaluation section | Note as limitation of existing alignment datasets | narrowed (not directly cited, gap discussed in target motivation) |
| Real-world conversation datasets | INFINITY-CHAT section | Cover existing real-world chat datasets | covered [7,8] |

## Search Queries
| Query | Purpose | Source |
|---|---|---|
| "mode collapse output diversity language model generation open-ended" | Theme 1: find diversity/mode collapse papers | Inferred from paper body |
| "intra-model repetition inter-model homogeneity large language models similarity" | Theme 1: find inter-model homogeneity papers | Inferred from Artificial Hivemind section |
| "human preference alignment pluralistic diverse responses open-ended queries language models" | Theme 3: find pluralistic alignment papers | Inferred from Evaluation section |
| "WildChat dataset real-world user queries chatbot conversations" | Theme 2: find WildChat paper | Named dataset in body |
| "RewardBench reward model evaluation benchmark" | Theme 3: find RewardBench paper | Named benchmark in body |
| "min-p decoding diversity language model generation sampling strategy" | Theme 1: find min-p paper | Named method in body |
| "LLM-as-judge evaluation alignment language model judge benchmark" | Theme 3: find LM judge papers | Inferred from evaluation focus |
| "HelpSteer alignment dataset human preference annotation language model" | Theme 3: find HelpSteer paper | Named dataset in body |
| "creativity diversity benchmark language model evaluation open-ended generation storytelling" | Theme 1: find diversity benchmarks | Inferred from diversity focus |
| "distributional preference learning pluralistic alignment annotator disagreement reward model" | Theme 3: find annotator disagreement papers | Inferred from evaluation focus |
| "text generation diversity decoding strategy nucleus sampling top-p temperature repetition" | Theme 1: find classic decoding diversity papers | Inferred from decoding discussion |
| "synthetic text detection model collapse homogenization AI generated content diversity" | Broader context: homogenization | Inferred from AI safety concern |

## Candidate Screening
| Title | Authors | Year | Source | Label | Reason |
|---|---|---|---|---|---|
| NoveltyBench: Evaluating Language Models for Humanlike Diversity | Zhang et al. | 2025 | 2504.05228 | relevant | Directly about mode collapse, diversity benchmark with real-world queries |
| The Curious Case of Neural Text Degeneration | Holtzman et al. | 2019 | 1904.09751 | relevant | Foundational work on neural text degeneration and nucleus sampling |
| Creativity Has Left the Chat | Mohammadi | 2024 | 2406.05587 | relevant | RLHF impact on creativity, mode collapse, attractor states |
| Benchmarking Linguistic Diversity of LLMs | Guo et al. | 2024 | 2412.10271 | relevant | Framework for lexical/syntactic/semantic diversity evaluation |
| The Price of Format: Diversity Collapse in LLMs | Yun et al. | 2025 | 2505.18949 | relevant | Diversity collapse from structured templates |
| Min-p Sampling for Creative and Coherent LLM Outputs | Nguyen et al. | 2024 | 2407.01082 | relevant | Decoding strategy for improving diversity |
| WildChat: 1M ChatGPT Interaction Logs in the Wild | Zhao et al. | 2024 | 2405.01470 | relevant | Source dataset for INFINITY-CHAT |
| LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset | Zheng et al. | 2023 | 2309.11998 | relevant | Major real-world LLM conversation dataset |
| Diverging Preferences: When do Annotators Disagree | Zhang et al. | 2024 | 2410.14632 | relevant | Taxonomy of annotator disagreement, distributional rewards |
| Dealing with Disagreements: Looking Beyond Majority Vote | Davani et al. | 2021 | 2110.05719 | relevant | Multi-annotator modeling, annotator disagreement |
| Fine-tuning LMs to find agreement | Bakker et al. | 2022 | 2211.15006 | relevant | Heterogeneous preferences, consensus finding |
| PERSONA: Reproducible Testbed for Pluralistic Alignment | Castricato et al. | 2024 | 2407.17387 | relevant | Pluralistic alignment testbed |
| Personalized and Pluralistic Preference Alignment Survey | Xie et al. | 2025 | 2504.07070 | weakly relevant | Survey context for pluralistic alignment |
| RewardBench: Evaluating Reward Models | Lambert et al. | 2024 | 2403.13787 | relevant | Reward model evaluation benchmark |
| Not All Layers Need Tuning | ? | 2025 | 2602.06665 | weakly relevant | Post-training diversity recovery, but less directly about evaluation |
| Group-Aware RL for Output Diversity | ? | 2025 | 2511.12596 | weakly relevant | Diversity optimization via RL, but more about training intervention |
| HelpSteer: Multi-attribute Helpfulness Dataset | Wang et al. | 2023 | 2311.09528 | weakly relevant | Multi-attribute annotation, but less about open-ended diversity |
| Structure-Aware Diversity Pursuit | ? | 2026 | 2601.06116 | weakly relevant | Homogenization as AI safety, but theoretical position paper |
| On Diversified Preferences of LLM Alignment | ? | 2023 | 2312.07401 | irrelevant | Broad alignment, insufficiently specific |
| Aligning Crowd Feedback via Distributional Preference RM | ? | 2024 | 2402.09764 | weakly relevant | Distributional rewards, but covered by more specific papers |

## Planned Themes
| Theme | Input signal it maps to | Core/context citations | Notes |
|---|---|---|---|
| Output Diversity and Mode Collapse in Language Models | Artificial Hivemind section (intra-model repetition, min-p decoding, diversity benchmarks) | [1,2,3,4,5,6] | Covers neural text degeneration, RLHF diversity collapse, linguistic diversity benchmarking, format-induced collapse, NoveltyBench, min-p decoding |
| Real-World Conversation Datasets and Open-Ended Query Resources | INFINITY-CHAT section (WildChat mining, taxonomy) | [7,8] | Covers WildChat and LMSYS-Chat-1M; notes gap in open-ended query taxonomies |
| Pluralistic Alignment, Reward Modeling, and Human Preference Diversity | Evaluation section (annotator disagreement, reward models, LM judges, pluralistic alignment) | [9,10,11,12,13,14] | Covers annotator disagreement modeling, consensus finding, pluralistic alignment testbeds, divergence taxonomy, alignment survey, RewardBench |

## Coverage Allocation
| Heading/theme | Recoverable named/background signals | Covered in final text | Unresolved gaps |
|---|---|---|---|
| Theme 1: Diversity & Mode Collapse | 6 key papers + field background | All 6 papers cited | None |
| Theme 2: Real-World Datasets | 2 key papers (WildChat, LMSYS-Chat-1M) | Both cited | None |
| Theme 3: Pluralistic Alignment & Evaluation | 6 key papers + field background | All 6 papers cited | None |

## Length Control
- Target word budget: 12-18 citations (broader paper covering multiple themes)
- Active budget: 14 final cited papers
- Final word count: ~640 words
- Status: Within budget

## Final Cited Papers
| # | Title | Authors | Year | Source | Citation role |
|---|---|---|---|---|---|
| [1] | The Curious Case of Neural Text Degeneration | Holtzman et al. | 2019 | arXiv:1904.09751 | Foundational neural text degeneration, nucleus sampling |
| [2] | Creativity Has Left the Chat | Mohammadi | 2024 | arXiv:2406.05587 | RLHF diversity collapse, attractor states |
| [3] | Benchmarking Linguistic Diversity of LLMs | Guo et al. | 2024 | arXiv:2412.10271 | Lexical/syntactic/semantic diversity framework |
| [4] | The Price of Format: Diversity Collapse in LLMs | Yun et al. | 2025 | arXiv:2505.18949 | Format-induced diversity collapse |
| [5] | NoveltyBench | Zhang et al. | 2025 | arXiv:2504.05228 | Mode collapse benchmark with real-world queries |
| [6] | Min-p Sampling | Nguyen et al. | 2024 | arXiv:2407.01082 | Diversity-oriented decoding strategy |
| [7] | WildChat | Zhao et al. | 2024 | arXiv:2405.01470 | Source dataset, real-world conversations |
| [8] | LMSYS-Chat-1M | Zheng et al. | 2023 | arXiv:2309.11998 | Real-world LLM conversation dataset |
| [9] | Dealing with Disagreements | Davani et al. | 2021 | arXiv:2110.05719 | Multi-annotator modeling, annotator disagreement |
| [10] | Fine-tuning LMs to find agreement | Bakker et al. | 2022 | arXiv:2211.15006 | Heterogeneous preferences, consensus |
| [11] | PERSONA | Castricato et al. | 2024 | arXiv:2407.17387 | Pluralistic alignment testbed |
| [12] | Diverging Preferences | Zhang et al. | 2024 | arXiv:2410.14632 | Disagreement taxonomy, distributional rewards |
| [13] | Pluralistic Preference Alignment Survey | Xie et al. | 2025 | arXiv:2504.07070 | Survey of pluralistic alignment methods |
| [14] | RewardBench | Lambert et al. | 2024 | arXiv:2403.13787 | Reward model evaluation benchmark |

## Claim-Citation Self-Check
| Citation | Claim | Supported? | Action | Notes |
|---|---|---|---|---|
| [1] | Maximization-based decoding leads to repetitive text; nucleus sampling proposed | Supported | keep | Directly from Holtzman et al. abstract and body |
| [2] | RLHF-aligned models exhibit lower entropy, clustered embeddings, attractor states | Supported | keep | Directly from Mohammadi abstract |
| [3] | Framework for lexical/syntactic/semantic diversity; LLMs underrepresent creative structures | Supported | keep | Directly from Guo et al. abstract |
| [4] | Structured templates induce diversity collapse; role markers act as behavioral anchors | Supported | keep | Directly from Yun et al. abstract |
| [5] | NoveltyBench evaluates multiple distinct outputs; larger models less diverse | Supported | keep | Directly from Zhang et al. abstract |
| [6] | Min-p sampling adjusts threshold based on top token probability, improves coherence and diversity | Supported | keep | Directly from Nguyen et al. abstract |
| [7] | WildChat: 1M user-ChatGPT conversations, 2.5M turns, greater linguistic diversity | Supported | keep | Directly from Zhao et al. abstract |
| [8] | LMSYS-Chat-1M: 1M conversations with 25 LLMs | Supported | keep | Directly from Zheng et al. abstract |
| [9] | Multi-annotator approach preserves individual differences; better uncertainty estimates | Supported | keep | Directly from Davani et al. abstract |
| [10] | 70B LLM fine-tuned for consensus statements maximizing group approval | Supported | keep | Directly from Bakker et al. abstract |
| [11] | PERSONA: synthetic personas from census data for pluralistic alignment evaluation | Supported | keep | Directly from Castricato et al. abstract |
| [12] | >30% disagreements from preference diversity; Bradley-Terry fails to distinguish consensus vs contested | Supported | keep | Directly from Zhang et al. abstract |
| [13] | Survey categorizing training-time, inference-time, user-modeling methods; lack of benchmarks | Supported | keep | Directly from Xie et al. abstract |
| [14] | RewardBench evaluates 80+ reward models across chat, reasoning, safety | Supported | keep | Directly from Lambert et al. abstract |
| Target motivation (Theme 1) | Prior work focused on intra-model, not inter-model; no comprehensive taxonomy | Target-paper interpretation | keep | Phrased as gap/motivation |
| Target motivation (Theme 2) | Existing datasets lack systematic taxonomy or open/closed distinction | Target-paper interpretation | keep | Phrased as gap/motivation |
| Target motivation (Theme 3) | Existing pluralistic alignment uses synthetic personas or crowd aggregates, not dense per-example annotations | Target-paper interpretation | keep | Phrased as gap/motivation |

## Citation Ledger
| Citation string | Matching paper | In Related Work? | In Final References? | In Self-Check? | Scope |
|---|---|---|---|---|---|
| [1] Holtzman | The Curious Case of Neural Text Degeneration | Yes | Yes | Yes | relevant |
| [2] Mohammadi | Creativity Has Left the Chat | Yes | Yes | Yes | relevant |
| [3] Guo | Benchmarking Linguistic Diversity | Yes | Yes | Yes | relevant |
| [4] Yun | The Price of Format | Yes | Yes | Yes | relevant |
| [5] Zhang (NoveltyBench) | NoveltyBench | Yes | Yes | Yes | relevant |
| [6] Nguyen | Min-p Sampling | Yes | Yes | Yes | relevant |
| [7] Zhao | WildChat | Yes | Yes | Yes | relevant |
| [8] Zheng | LMSYS-Chat-1M | Yes | Yes | Yes | relevant |
| [9] Davani | Dealing with Disagreements | Yes | Yes | Yes | relevant |
| [10] Bakker | Fine-tuning LMs to find agreement | Yes | Yes | Yes | relevant |
| [11] Castricato | PERSONA | Yes | Yes | Yes | relevant |
| [12] Zhang (Diverging) | Diverging Preferences | Yes | Yes | Yes | relevant |
| [13] Xie | Pluralistic Alignment Survey | Yes | Yes | Yes | relevant |
| [14] Lambert | RewardBench | Yes | Yes | Yes | relevant |

## Completion Status
| Gate | Status |
|---|---|
| RWEval Citation Format | Pass: numeric citations in s_text.txt, numbered references in s_reference.txt |
| Read the Visible Input | Pass: full paper body read, no Related Work section found |
| Visible Heading Preservation | N/A: No visible Related Work headings; themes inferred from body |
| Visible Coverage Ledger | Pass: all visible signals have final disposition |
| Coverage Allocation | Pass: each theme covers multiple named works and field background |
| Missing-Point Prevention | Pass: 10 must-not-drop signals checked against final text |
| Named Citation Exactness | Pass: all citations verified through DeepXiv metadata |
| Reference Validity Guard | Pass: all metadata stable, no MARG or known mismatch papers |
| Length Control | Pass: 14 citations within 12-18 budget, ~640 words |
| Dynamic Citation Budget | Pass: 14 citations in 12-18 range |
| Final Consistency | Pass: all in-text citations match references, self-check complete |

## Benchmark-Specific Deny / Handle List
| Paper or pattern | Reason | Handling | Theme preserved by |
|---|---|---|---|
| MARG: Multi-Agent Review Generation (2401.04259) | Known metadata_mismatch in benchmark | Screened only, not final-cited | N/A — not relevant to this paper's themes |

## Uncertain Points
- Inter-model homogeneity is mentioned as an underexplored area in prior work; the search for "inter-model homogeneity large language models" returned mostly unrelated papers. This gap in prior work is consistent with the target paper's motivation.
- The target paper is anonymized; its actual title, authors, and arXiv ID are unknown. All searches were constructed from body text signals only.
