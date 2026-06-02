## Run Metadata
- Date: 2026-05-26
- Search source: DeepXiv only
- Output directory: runs/clean_search/sim_prompt+skill/researcher

## Paper Profile
- Topic: Automating the scientific research lifecycle using LLMs
- Task: Full-cycle automated research and review: literature review → manuscript preparation → peer review → paper refinement
- Method: Iterative preference training framework with CycleResearcher (policy model) and CycleReviewer (reward model), using Iterative SimPO and NLL loss. Built on Mistral and Qwen 2.5 (12B–123B).
- Data type / benchmark: Review-5k (ICLR 2024 papers with reviews, ~5K papers, 16K+ reviews) and Research-14k (accepted ML conference papers 2022–2024, ~14K papers). Evaluation on Reviewer-5k test set, arXiv Sep 2024 preprints, and AI Scientist outputs.
- Evaluation focus: Proxy MSE/MAE for review scoring consistency; average scores, acceptance rates, and human evaluation for paper generation quality.
- Main contribution: A fully automated Research-Review-Refinement cycle using open-source LLMs with iterative SimPO training; two new datasets (Review-5k, Research-14k).
- Boundaries: Experimental results are fabricated (not executed); generalizability across research domains remains a challenge; scope limited to ML paper generation; actual experiments are beyond scope.

## Visible Related Work Headings
| Heading | Extracted coverage signals | Planned theme |
|---|---|---|
| LLMs for Research | Si et al. (idea generation human study), Wang et al. (AutoSurvey), Huang et al. (MLAgentBench), Wang et al. (scientific literature retrieval), AI Scientist, multi-agent collaborative writing, multi-module retrieval | LLMs for Research |
| LLMs for Science Discovery | Historical AI4Science (chemistry, synthetic biology, material discovery, mathematics), passive data analysis vs active discovery | LLMs for Science Discovery |
| Automated Evaluation of Research Papers | Hosseini & Horbach, Robertson, Lu et al., Tyser et al., RewardBench, GenRM | Automated Evaluation of Research Papers |

## Visible Coverage Scaffold
| Visible signal | Signal type | Exact recovery query | DeepXiv recovery status | Planned use |
|---|---|---|---|---|
| Si et al. — LLM idea generation human evaluation | named works | Si + human evaluation idea generation language models | Recovered: arXiv:2409.04109 | Core citation for Theme 1 |
| Wang et al. — automatic survey writing | named works | Wang + LLM automatic survey paper writing | Recovered: arXiv:2406.10252 (AutoSurvey) | Core citation for Theme 1 |
| Huang et al. — MLAgentBench | named works | Huang + MLAgentBench benchmarking LLM ML experimentation | Recovered: arXiv:2310.03302 | Core citation for Theme 1 |
| Wang et al. — scientific literature retrieval | named works | Wang + LLM scientific literature retrieval | Not found with confidence | Gap; recorded as uncertain |
| AI Scientist — automated research pipeline | named works | AI Scientist automated research pipeline | Recovered: arXiv:2408.06292 | Core citation for Theme 1 |
| AI4Science / Langley historical context | field background | Langley + computational scientific discovery | Not found (pre-arXiv work) | Gap; covered via AI4Research survey |
| Hosseini & Horbach — ChatGPT peer review | named works | Hosseini Horbach ChatGPT peer review qualitative | Not found | Gap |
| Robertson — GPT-4 peer review assistance | named works | Robertson GPT-4 assisting peer review | Recovered: arXiv:2307.05492 | Core citation for Theme 3 |
| Lu et al. — GPT-4 full-PDF evaluation | named works | Lu GPT-4 auto review full paper | Not found with confidence | Gap |
| Tyser et al. — LLM full-text paper evaluation | named works | Tyser LLM evaluate full-text scientific papers | Not found with confidence | Gap |
| RewardBench — reward model evaluation | named works | RewardBench evaluating reward models | Recovered: arXiv:2403.13787 | Core citation for Theme 3 |
| GenRM — generative reward model | named works | Generative Reward Model GenRM next-token prediction | Recovered: arXiv:2408.15240 | Core citation for Theme 3 |
| Paper SEA — automated review framework | named works | Paper SEA automated scientific peer review | Recovered: arXiv:2407.12857 | Core citation for Theme 3 |
| Multi-agent collaborative writing | field background | multi-agent collaborative writing LLM research paper | Not found as independent citation; covered via IdeaBench | Context |

## Search Queries
| Query | Purpose | Source |
|---|---|---|
| Si human evaluation idea generation language models research | Exact recovery: Si et al. | DeepXiv |
| Wang LLM automatic survey paper writing | Exact recovery: Wang et al. (AutoSurvey) | DeepXiv |
| Huang MLAgentBench benchmarking LLM ML experimentation coding | Exact recovery: Huang et al. (MLAgentBench) | DeepXiv |
| Wang LLM scientific literature retrieval | Exact recovery: Wang et al. (retrieval) | DeepXiv |
| AI Scientist automated research pipeline fully autonomous paper generation | Exact recovery: AI Scientist | DeepXiv |
| Hosseini Horbach ChatGPT peer review effectiveness qualitative | Exact recovery: Hosseini & Horbach | DeepXiv |
| Robertson GPT-4 assisting peer review benefits participants | Exact recovery: Robertson | DeepXiv |
| Lu Tyser GPT-4 evaluate full-text PDF scientific papers peer review | Exact recovery: Lu et al. and Tyser et al. | DeepXiv |
| RewardBench evaluating reward models human preference benchmark Lambert | Exact recovery: RewardBench | DeepXiv |
| Generative Reward Model GenRM next-token prediction reinforcement learning | Exact recovery: GenRM | DeepXiv |
| Langley computational scientific discovery AI automated hypothesis | Exact recovery: Langley historical context | DeepXiv |
| Paper SEA automated scientific peer review evaluation framework | Exact recovery: Paper SEA | DeepXiv |
| Si et al language model idea generation novelty diversity human study | Exact recovery: Si follow-up | DeepXiv |
| SimPO simple preference optimization direct preference alignment | Method context | DeepXiv |
| AI4Science survey artificial intelligence scientific discovery | Field background for Theme 2 | DeepXiv |
| autonomous research agent LLM open-source fine-tuning | Theme 2 supplementary | DeepXiv |

## Candidate Screening
| Title | Authors | Year | Source | Label | Reason |
|---|---|---|---:|---|---|
| Can LLMs Generate Novel Research Ideas? | Si, Yang, Hashimoto | 2024 | arXiv:2409.04109 | relevant | Directly cited named work; human study of LLM idea generation |
| IdeaBench | Guo et al. | 2024 | arXiv:2411.02429 | weakly relevant | Benchmark for LLM idea generation; supports evaluation context but not the named citation |
| AutoSurvey | Wang et al. | 2024 | arXiv:2406.10252 | relevant | Directly cited named work; LLM automatic survey writing |
| MLAgentBench | Huang, Vora, Liang, Leskovec | 2023 | arXiv:2310.03302 | relevant | Directly cited named work; evaluating LLM agents on ML experimentation |
| The AI Scientist | Lu et al. | 2024 | arXiv:2408.06292 | relevant | Directly cited named work; fully automated scientific discovery |
| AI4Research: A Survey | Chen et al. | 2025 | arXiv:2507.01903 | weakly relevant | Survey on AI for scientific research; context for Theme 2 |
| data-to-paper | Ifargan et al. | 2024 | arXiv:2404.17605 | weakly relevant | Autonomous research from data to manuscripts; adjacent to Theme 2 |
| GPT4 is Slightly Helpful for Peer-Review | Robertson | 2023 | arXiv:2307.05492 | relevant | Directly cited named work; pilot study on GPT-4 peer review |
| RewardBench | Lambert et al. | 2024 | arXiv:2403.13787 | relevant | Directly cited named work; reward model evaluation benchmark |
| Generative Verifiers (GenRM) | Zhang et al. | 2024 | arXiv:2408.15240 | relevant | Directly cited named work; generative reward models |
| Paper SEA | Yu et al. | 2024 | arXiv:2407.12857 | relevant | Directly cited named work; automated peer reviewing framework |
| Towards Scientific Discovery with Generative AI | — | 2024 | arXiv:2412.11427 | irrelevant | Screened; superseded by more targeted AI4Research survey |
| MARG: Multi-Agent Review Generation | D'Arcy et al. | 2024 | arXiv:2401.04259 | screened only | Metadata mismatch risk per benchmark rules; not final-cited |
| AutoFlow | — | 2024 | arXiv:2407.12821 | irrelevant | Workflow automation for LLM agents; wrong task |

## Planned Themes
| Theme | Input signal it maps to | Core/context citations | Notes |
|---|---|---|---|
| LLMs for Research | Visible heading 1 | [1] Si, [3] Wang, [4] Huang, [5] AI Scientist (core); [2] IdeaBench (context) | 5 papers; Wang (retrieval) recorded as gap |
| LLMs for Science Discovery | Visible heading 2 | [6] AI4Research survey, [7] data-to-paper (context) | 2 papers; Langley and historical named works are pre-arXiv gaps |
| Automated Evaluation of Research Papers | Visible heading 3 | [8] Robertson, [9] RewardBench, [10] GenRM, [11] Paper SEA (core) | 4 papers; Hosseini & Horbach, Lu et al., Tyser et al. recorded as gaps |

## Final Cited Papers
| Title | Authors | Year | Source | Citation role |
|---|---|---:|---|---|
| Can LLMs Generate Novel Research Ideas? | Si, Yang, Hashimoto | 2024 | arXiv:2409.04109 | Core: large-scale human study of LLM idea generation |
| IdeaBench | Guo et al. | 2024 | arXiv:2411.02429 | Context: benchmark for LLM idea generation evaluation |
| AutoSurvey | Wang et al. | 2024 | arXiv:2406.10252 | Core: LLM automatic survey writing |
| MLAgentBench | Huang et al. | 2023 | arXiv:2310.03302 | Core: benchmarking LLM agents on ML experimentation |
| The AI Scientist | Lu et al. | 2024 | arXiv:2408.06292 | Core: fully automated end-to-end scientific discovery |
| AI4Research: A Survey | Chen et al. | 2025 | arXiv:2507.01903 | Context: taxonomy of AI for scientific research tasks |
| data-to-paper | Ifargan et al. | 2024 | arXiv:2404.17605 | Context: autonomous research from data to manuscripts |
| GPT4 is Slightly Helpful for Peer-Review | Robertson | 2023 | arXiv:2307.05492 | Core: pilot study on GPT-4 peer review assistance |
| RewardBench | Lambert et al. | 2024 | arXiv:2403.13787 | Core: reward model evaluation benchmark |
| Generative Verifiers (GenRM) | Zhang et al. | 2024 | arXiv:2408.15240 | Core: generative reward models via next-token prediction |
| Paper SEA | Yu et al. | 2024 | arXiv:2407.12857 | Core: structured automated peer reviewing framework |

## Claim-Citation Self-Check
| Citation | Claim | Supported? | Action | Notes |
|---|---|---|---|---|
| [1] | "LLM-generated research ideas judged as more novel than human expert ideas" | Supported | keep | Directly from abstract + TLDR |
| [2] | "benchmark for systematically evaluating LLM research idea generation capabilities" | Supported | keep | Abstract confirms benchmark and evaluation framework |
| [3] | "automates comprehensive survey writing through retrieval-augmented outline generation" | Supported | keep | Abstract confirms systematic survey automation |
| [4] | "evaluate LLM agents on designing, executing, and iterating on ML experiments" | Supported | keep | Abstract confirms 13-task suite for ML experimentation |
| [5] | "fully automated end-to-end scientific discovery pipeline" | Supported | keep | Abstract confirms: idea generation, code, experiments, paper, simulated review |
| [6] | "taxonomy of AI4Research tasks spanning scientific comprehension, discovery, academic writing, and peer review" | Supported | keep | Abstract confirms taxonomy with five mainstream tasks |
| [7] | "guiding LLM agents through complete research process from data to manuscripts" | Supported | keep | Abstract confirms data-to-paper automation platform |
| [8] | "GPT-4-generated reviews can provide moderately helpful feedback" | Supported | keep | Abstract + title confirm pilot study on GPT-4 peer review helpfulness |
| [9] | "systematic benchmark for evaluating reward models across chat, reasoning, and safety domains" | Supported | keep | Abstract confirms prompt-chosen-rejected trios spanning those domains |
| [10] | "train reward models as next-token predictors... outperforming discriminative reward models and LLM-as-a-Judge" | Supported | keep | TLDR confirms outperformance on GSM8K and MATH |
| [11] | "structured automated peer reviewing framework that standardizes heterogeneous reviews, generates feedback, evaluates consistency" | Supported | keep | TLDR confirms SEA-S, SEA-E, SEA-A modules |

Final actions: all keep; no narrowing needed. All claims are directly supported by DeepXiv abstract/TLDR evidence.

## Citation Ledger
| Citation string | Matching paper | In Related Work? | In Final References? | In Self-Check? | Scope |
|---|---|---|---|---|---|
| [1] | Si et al. 2024 | Yes | Yes | Yes | Theme 1 |
| [2] | Guo et al. 2024 (IdeaBench) | Yes | Yes | Yes | Theme 1 |
| [3] | Wang et al. 2024 (AutoSurvey) | Yes | Yes | Yes | Theme 1 |
| [4] | Huang et al. 2023 (MLAgentBench) | Yes | Yes | Yes | Theme 1 |
| [5] | Lu et al. 2024 (AI Scientist) | Yes | Yes | Yes | Theme 1 |
| [6] | Chen et al. 2025 (AI4Research) | Yes | Yes | Yes | Theme 2 |
| [7] | Ifargan et al. 2024 (data-to-paper) | Yes | Yes | Yes | Theme 2 |
| [8] | Robertson 2023 | Yes | Yes | Yes | Theme 3 |
| [9] | Lambert et al. 2024 (RewardBench) | Yes | Yes | Yes | Theme 3 |
| [10] | Zhang et al. 2024 (GenRM) | Yes | Yes | Yes | Theme 3 |
| [11] | Yu et al. 2024 (Paper SEA) | Yes | Yes | Yes | Theme 3 |

## Completion Status
| Gate | Status |
|---|---|
| RWEval Citation Format | Pass: numeric citations [1]–[11] |
| Read the Visible Input | Pass: full input checked |
| Visible Heading Preservation | Pass: 3 headings mirrored as 3 themes |
| Named Citation Exactness | Pass: author-year exactness verified for all recovered named works |
| Reference Validity Guard | Pass: all final-cited papers have consistent metadata; MARG screened only |
| Dynamic Citation Budget | Pass: 11 papers in 8–12 range |
| Final Consistency | Pass: 11 in-text citations map to 11 reference entries; all cited in self-check |

## Uncertain Points
- **Wang et al. (scientific literature retrieval):** The visible Related Work cites "Wang et al." for "a method leveraging LLMs for scientific literature retrieval." DeepXiv searches did not recover a confident match under Wang + scientific literature retrieval. This named citation is recorded as a gap; not substituted.
- **Hosseini & Horbach:** The visible Related Work cites them for "small-scale qualitative experiments to evaluate the effectiveness of ChatGPT in the peer review process." Not found on DeepXiv. Recorded as a gap.
- **Lu et al. (GPT-4 full-PDF evaluation):** The visible Related Work cites "Lu et al." for using "GPT-4 to evaluate full-text PDFs of scientific papers." DeepXiv searches did not return a confident match. Recorded as a gap.
- **Tyser et al.:** The visible Related Work cites "Tyser et al." alongside Lu et al. for evaluating full-text scientific papers with GPT-4. Not found on DeepXiv. Recorded as a gap.
- **Langley (historical computational scientific discovery):** Pre-arXiv work from the 1970s–1980s; not available on DeepXiv. Historical context for Theme 2 is covered through the AI4Research survey [6] using narrow wording.
- **MARG (arXiv:2401.04259):** Appeared in search results for Lu/Tyser queries. Per benchmark rules, screened only — not final-cited due to known metadata mismatch risk in this benchmark.

## Active Budget
- Range: 8–12
- Chosen: 11 papers
- Reason: Three visible themes with overlapping recovery coverage. Majority of named works recovered (8/13). Remaining gaps are narrow historical or pre-arXiv works unsuitable for substitution. Budget reflects the actual recoverable evidence without padding.
