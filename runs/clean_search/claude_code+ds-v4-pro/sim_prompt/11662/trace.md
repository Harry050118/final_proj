# Related Work Generation Trace

## Inferred Research Topic
- **Task:** Evaluating Multimodal Large Language Models (MLLMs) as verifiers of agent behavior in open-ended environments (web navigation, computer use, robotics).
- **Core Problem:** MLLMs exhibit "agreement bias" — a strong tendency to over-validate agent behavior, judging flawed trajectories as successful.
- **Proposed Method:** Self-Grounded Verification (SGV) — a zero-shot method that first elicits broad priors about desired behavior conditioned on partial information, then evaluates trajectories conditioned on those self-generated priors.
- **Datasets/Environments:** VisualWebArena, OSWorld, robomimic (tool-hang)
- **Contributions:** Systematic characterization of agreement bias across 13+ model families and 28+ design templates; SGV method improving failure detection by ~25pp; new SOTA on VisualWebArena; updated VWA release.

## DeepXiv Search Queries

1. `LLM as evaluator agent trajectory verification multimodal`
2. `LLM judge bias evaluation benchmark Zheng`
3. `LLM as judge evaluator benchmark bias`
4. `multimodal LLM verifier agent web navigation robotics`
5. `VisualWebArena web agent benchmark evaluation`
6. `OSWorld computer desktop agent benchmark`
7. `Reflexion self-improvement agent reflection LLM`
8. `LLM evaluation bias agreement over-validation failure detection`
9. `reward model verifier math code reasoning LLM`
10. `agent trajectory success detection failure identification multimodal`
11. `test-time scaling chain-of-thought majority voting LLM reasoning verifier`
12. `robomimic robot learning manipulation benchmark diffusion policy`
13. `WebArena agent benchmark Zhou`
14. `G-Eval NLG evaluation chain-of-thought Liu`
15. `Set-of-Marks visual prompting grounding Yang`
16. `ReAct reasoning acting language agent Yao`
17. `process reward model outcome verifier math code Uesato Lightman`
18. `self-rewarding language model alignment Yuan`
19. `LLM self-training self-improvement fine-tuning generated data`
20. `LLM-as-a-judge MT-Bench Zheng evaluation`
21. `LLM self-preference bias evaluation`
22. `AgentRewardBench benchmark agent reward evaluation`
23. `LLM position bias verbosity bias evaluation judge Zheng`
24. `training language models rewards RLHF Ouyang`
25. `web agent vision language model grounding HTML DOM`
26. `agent self-correction self-refine reflection Madaan`
27. `GUI agent grounding multimodal screen`
28. `web agent online supervision reward steering`
29. `digital agent self-improvement successful trajectory finetuning`
30. `What Matters in Learning from Offline Human Demonstrations for Robot Manipulation Mandlekar`
31. `LLM verifier agent behavior open-ended task evaluation reward`
32. `visual language model agent verification robot success detection`
33. `outcome-based process-based verification LLM agent task`

## Main Candidate Papers (Full Metadata Retrieved via head/brief)

| arxiv_id | Title | First Author | Venue | Year |
|----------|-------|-------------|-------|------|
| 2306.05685 | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | Lianmin Zheng | NeurIPS | 2023 |
| 2303.16634 | G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment | Yang Liu | EMNLP | 2023 |
| 2303.07280 | Vision-Language Models as Success Detectors | Yuqing Du | CoLLAs | 2023 |
| 2404.06474 | Autonomous Evaluation and Refinement of Digital Agents | Jiayi Pan | arXiv | 2024 |
| 2401.13649 | VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks | Jing Yu Koh | arXiv | 2024 |
| 2307.13854 | WebArena: A Realistic Web Environment for Building Autonomous Agents | Shuyan Zhou | ICLR | 2023 |
| 2303.11366 | Reflexion: Language Agents with Verbal Reinforcement Learning | Noah Shinn | NeurIPS | 2023 |
| 2210.03629 | ReAct: Synergizing Reasoning and Acting in Language Models | Shunyu Yao | arXiv | 2022 |
| 2310.11441 | Set-of-Mark Prompting Unleashes Extraordinary Visual Grounding in GPT-4V | Jianwei Yang | arXiv | 2023 |
| 2201.11903 | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | Jason Wei | NeurIPS | 2022 |
| 2305.20050 | Let's Verify Step by Step | Hunter Lightman | ICLR | 2023 |
| 2401.10020 | Self-Rewarding Language Models | Weizhe Yuan | ICML | 2024 |
| 2404.07972 | OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments | Tianbao Xie | NeurIPS | 2024 |
| 2303.04137 | Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | Cheng Chi | RSS | 2023 |
| 2504.08942 | AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories | Xing Han Lu | arXiv | 2025 |
| 2509.23738 | GUI-Shepherd: Reliable Process Reward and Verification for Long-Sequence GUI Tasks | Cong Chen | arXiv | 2025 |
| 2602.00575 | Agentic Reward Modeling: Verifying GUI Agent via Online Proactive Interaction (VAGEN) | Chaoqun Cui | arXiv | 2026 |
| 2203.02155 | Training language models to follow instructions with human feedback | Long Ouyang | NeurIPS | 2022 |
| 2312.10003 | ReST meets ReAct: Self-Improvement for Multi-Step Reasoning LLM Agent | Renat Aksitov | arXiv | 2023 |
| 2401.01614 | GPT-4V(ision) is a Generalist Web Agent, if Grounded (SEEACT) | Boyuan Zheng | ICML | 2024 |
| 2401.10935 | SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents | Kanzhi Cheng | ACL | 2024 |
| 2506.21252 | Agent-RewardBench: Towards a Unified Benchmark for Reward Modeling | Tianyi Men | ACL | 2025 |
| 2406.07791 | Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge | Lin Shi | IJCNLP-AACL | 2024 |
| 2410.21819 | Self-Preference Bias in LLM-as-a-Judge | Koki Wataoka | arXiv | 2024 |
| 2404.13076 | LLM Evaluators Recognize and Favor Their Own Generations | Arjun Panickssery | NeurIPS | 2024 |
| 2407.13692 | Prover-Verifier Games improve legibility of LLM outputs | Jan Hendrik Kirchner | arXiv | 2024 |
| 2410.00371 | AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation | Jiafei Duan | ICLR | 2024 |
| 2501.12326 | UI-TARS: Pioneering Automated GUI Interaction with Native Agents | Yujia Qin | arXiv | 2025 |
| 2411.02337 | WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning | Zehan Qi | arXiv | 2024 |
| 2108.03298 | What Matters in Learning from Offline Human Demonstrations for Robot Manipulation (robomimic) | Ajay Mandlekar | CoRL | 2021 |

## Final Cited Papers (29 papers in 5 themes)

### Theme 1: LLM-based Evaluation ([1]–[5])
[1] Zheng et al. 2023 — LLM-as-a-Judge (NeurIPS)
[2] Liu et al. 2023 — G-Eval (EMNLP)
[3] Shi et al. 2024 — Position bias in LLM-as-a-Judge (IJCNLP-AACL)
[4] Panickssery et al. 2024 — Self-recognition and self-preference (NeurIPS)
[5] Wataoka et al. 2024 — Self-preference bias (arXiv)

### Theme 2: Verifiers and Reward Models ([6]–[9])
[6] Lightman et al. 2023 — Let's Verify Step by Step (ICLR)
[7] Ouyang et al. 2022 — InstructGPT/RLHF (NeurIPS)
[8] Yuan et al. 2024 — Self-Rewarding Language Models (ICML)
[9] Kirchner et al. 2024 — Prover-Verifier Games (arXiv)

### Theme 3: Multimodal Agents and Benchmarks ([10]–[19])
[10] Zhou et al. 2023 — WebArena (ICLR)
[11] Koh et al. 2024 — VisualWebArena (arXiv)
[12] Xie et al. 2024 — OSWorld (NeurIPS)
[13] Mandlekar et al. 2021 — robomimic (CoRL)
[14] Yao et al. 2022 — ReAct (arXiv)
[15] Yang et al. 2023 — Set-of-Mark Prompting (arXiv)
[16] Cheng et al. 2024 — SeeClick (ACL)
[17] Zheng et al. 2024 — GPT-4V Web Agent / SEEACT (ICML)
[18] Qin et al. 2025 — UI-TARS (arXiv)
[19] Chi et al. 2023 — Diffusion Policy (RSS)

### Theme 4: MLLM-based Verification of Agent Behavior ([20]–[26])
[20] Du et al. 2023 — SuccessVQA (CoLLAs)
[21] Pan et al. 2024 — Autonomous Evaluation and Refinement (arXiv)
[22] Lu et al. 2025 — AgentRewardBench (arXiv)
[23] Men et al. 2025 — Agent-RewardBench (ACL)
[24] Chen et al. 2025 — GUI-Shepherd (arXiv)
[25] Cui et al. 2026 — VAGEN (arXiv)
[26] Duan et al. 2024 — AHA (ICLR)

### Theme 5: Self-Improvement and Online Learning ([27]–[29])
[27] Shinn et al. 2023 — Reflexion (NeurIPS)
[28] Aksitov et al. 2023 — ReST meets ReAct (arXiv)
[29] Qi et al. 2024 — WebRL (arXiv)

## Uncertainties and Notes

1. **AgentRewardBench first author name:** The DeepXiv head endpoint returned "Xing Han L��" with encoding artifacts. The name is romanized as "X. H. Lu" in the reference list; the exact diacritic could not be resolved.

2. **Paper self-identification:** DeepXiv search returned arXiv ID 2507.11662 ("Let's Think in Two Steps: Mitigating Agreement Bias in MLLMs with Self-Grounded Verification") which corresponds to the input paper. This paper was excluded from citations. Note: the DeepXiv TLDR for this paper is incorrect (describes video understanding rather than MLLM verification).

3. **Robomimic paper:** The robomimic paper (Mandlekar et al., CoRL 2021, 2108.03298) was found via DeepXiv search rather than direct ID lookup, confirming it is indexed.

4. **Verification depth:** All 29 cited papers were verified via the `head` endpoint which returns title, authors, venue, year, and abstract. No paper was cited solely from search result snippets.

5. **No invented claims:** All statements about cited papers are grounded in verified metadata (title, abstract, venue). No numeric comparisons, dataset statistics, or unsupported performance claims about cited papers are made.

6. **Theme boundaries:** Some papers span multiple themes (e.g., Reflexion could also fit under MLLM-based verification when using MLLMs as the verifier), but each paper is placed in the most thematically representative category.
