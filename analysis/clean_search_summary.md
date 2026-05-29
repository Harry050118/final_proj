# Clean Search 结果汇总

## 实验设置

本分析只覆盖当前已经完成的 Clean Search 实验。`sim_prompt` 解释为 No Intervention / baseline，`sim_prompt+skill` 解释为 skill-guided citation-grounding intervention。

本次没有运行 Noisy Search / Misleading Search，因此不能据此声称系统已经验证了对无关论文或误导论文注入的抗干扰能力。

RWEval report 是本阶段的主要量化证据。下方人工审计区域会保留为空白，用于你后续做代表性 case 的 sanity check，再决定哪些内容进入前端展示。

## 总体结果

| Group | N | Overall | Citation quality | Relevance | Coverage |
|---|---:|---:|---:|---:|---:|
| No Intervention / baseline (`sim_prompt`) | 5 | 6.36 | 6.22 | 7.17 | 3.18 |
| Skill-guided citation-grounding intervention (`sim_prompt+skill`) | 5 | 7.72 | 9.05 | 8.40 | 4.35 |
| Skill - baseline | - | +1.36 | +2.83 | +1.23 | +1.17 |

## 定量分析

在 5 个 Clean Search case 中，skill-guided 设置的平均 overall 从 6.36 提升到 7.72。提升最明显的维度是 citation quality，从 6.22 提升到 9.05。Relevance 也从 7.17 提升到 8.40。Coverage 仍然是相对较弱的维度，虽然它也从 3.18 提升到 4.35。

因此，目前可以支持一个有边界的结论：在 Clean Search 条件下，skill-guided workflow 相比 baseline 改善了引用可靠性和主题相关性。但它不能证明系统在 noisy 或 misleading 检索条件下也同样稳健。

## Case 级别对比

| Case | Baseline overall | Skill overall | Overall delta | Citation quality delta | Relevance delta | Coverage delta |
|---|---:|---:|---:|---:|---:|---:|
| 07794 | 7.92 | 7.78 | -0.14 | -0.35 | +0.28 | +1.07 |
| 11662 | 5.98 | 7.38 | +1.40 | +3.83 | +0.30 | +0.80 |
| 12299 | 5.96 | 7.61 | +1.65 | +3.40 | +2.43 | -0.15 |
| researcher | 4.88 | 8.03 | +3.15 | +6.50 | +2.87 | +2.06 |
| source | 7.07 | 7.82 | +0.75 | +0.77 | +0.26 | +2.09 |

## 诊断计数

| Case | Baseline missing points | Skill missing points | Baseline bad pairs | Skill bad pairs | Baseline overclaims | Skill overclaims |
|---|---:|---:|---:|---:|---:|---:|
| 07794 | 5 | 10 | 0 | 0 | 1 | 0 |
| 11662 | 8 | 7 | 2 | 0 | 0 | 3 |
| 12299 | 8 | 6 | 20 | 0 | 1 | 1 |
| researcher | 14 | 11 | 21 | 0 | 0 | 0 |
| source | 6 | 4 | 1 | 0 | 0 | 1 |

## 自动审计诊断摘要

RWEval 的自动诊断已经提供了较具体的审计证据，包括 missing points、bad citation-claim pairs、overclaim citation-claim pairs、citation group support 和 topic structure issues。Markdown 里每类最多展示 3 条；完整诊断见 JSON 的 `detailed_diagnostics` 字段。

### 07794

| Group | Diagnostic type | Count | 摘要 |
|---|---|---:|---|
| Baseline | missing points | 5 | ReAct demonstrated that LLMs can synergize reasoning and acting, enabling autonomous retrieval decisions. 原因：No candidate claim mentions ReAct or the synergistic reasoning-acting concept from the given citation.<br>Chain-of-Retrieval and DeepRAG structure retrieval into sequential steps for handling complex queries. 原因：No candidate claim mentions Chain-of-Retrieval, DeepRAG, or their specific citations.<br>Early approaches for adaptive retrieval used heuristics or classifiers to detect uncertainty and determine retrieval need. 原因：No candidate claim describes early approaches using heuristics or classifiers for uncertainty detection.<br>... 另有 2 条，完整诊断见 JSON |
| Baseline | bad citation-claim pairs | 0 | 无 |
| Baseline | overclaim citation-claim pairs | 1 | claim SClaim7；reference arxiv:2501.12948；support=partial；原因：The claim states that DeepSeek-R1 inspired RL training for autonomous search and retrieval, which is not explicitly demonstrated or claimed in the paper; the inspiration is indirect and mild. |
| Baseline | citation group support | 0 | 无 |
| Baseline | topic structure issues | 3 | S2：Paragraph is self-contained but could benefit from deeper connection to tool use specifically.<br>S3：No significant issues; focus is clear and citations align well.<br>S4：May be slightly narrow by emphasizing math reasoning heritage; still relevant to efficiency. |
| Skill | missing points | 10 | ReAct shows LLMs can synergize reasoning and acting for autonomous retrieval decisions. 原因：No candidate claim mentions ReAct or its specific synergy of reasoning and acting for autonomous retrieval decisions.<br>Chain-of-Retrieval and DeepRAG structure retrieval as sequential steps for complex queries. 原因：No candidate claim mentions Chain-of-Retrieval or DeepRAG.<br>RAG-RL uses RL and curriculum learning to enhance retrieval-augmented generation. 原因：No candidate claim mentions RAG-RL or its use of curriculum learning.<br>... 另有 7 条，完整诊断见 JSON |
| Skill | bad citation-claim pairs | 0 | 无 |
| Skill | overclaim citation-claim pairs | 0 | 无 |
| Skill | citation group support | 0 | 无 |
| Skill | topic structure issues | 3 | S2：Could more explicitly link to the evolution toward agentic systems mentioned in GTopic1, but still focused on prompting-based RAG.<br>S3：None significant: clearly focused on RL-based search agents and their limitations.<br>S4：Paragraph is brief but coherent; could expand on how process supervision addresses specific inefficiencies. |

### 11662

| Group | Diagnostic type | Count | 摘要 |
|---|---|---:|---|
| Baseline | missing points | 8 | Closest related work uses GPT-4V evaluator with benchmark-specific rubrics for trajectory evaluation in Reflexion and behavior cloning. 原因：No candidate claim mentions GPT-4V evaluator with rubrics for Reflexion and behavior cloning.<br>Similar evaluator used to guide tree search, filter trajectories for memories/tools, and for RL training. 原因：No candidate claim explicitly describes an evaluator used to guide tree search, filter trajectories for memories/tools, and for RL training.<br>Chain-of-thought extended to multimodal and environment-interaction settings. 原因：No candidate claim discusses extending CoT to multimodal or environment-interaction settings.<br>... 另有 5 条，完整诊断见 JSON |
| Baseline | bad citation-claim pairs | 2 | claim SClaim3；reference wang2024deepseek；support=weak；原因：DeepSeek-Coder focuses on code generation but does not explicitly discuss formal verifiers like unit tests or reinforcement learning with verifiable rewards (RLVR). The connection to breakthroughs through RLVR is indirect and not stated in the cited work.<br>claim SClaim17；reference drouin2024browsergym；support=unknown；原因：No retrieved evidence or citation metadata is available to verify the claim. The reference key suggests a paper on BrowserGym, but without any concrete information, the support cannot be determined. |
| Baseline | overclaim citation-claim pairs | 0 | 无 |
| Baseline | citation group support | 2 | claim SClaim2；reference None<br>claim SClaim3；reference None |
| Baseline | topic structure issues | 0 | 无 |
| Skill | missing points | 7 | Following works employ similar evaluator to guide tree search. 原因：No candidate claim mentions the use of a similar evaluator to guide tree search.<br>Following works employ similar evaluator for RL training in simpler environments. 原因：No candidate claim mentions the use of a similar evaluator for RL training in simpler environments.<br>Orthogonal approaches scale test-time compute via sampling and search, using heuristics or verifiers. 原因：No candidate claim discusses scaling test-time compute via sampling and search using heuristics or verifiers.<br>... 另有 4 条，完整诊断见 JSON |
| Skill | bad citation-claim pairs | 0 | 无 |
| Skill | overclaim citation-claim pairs | 3 | claim SClaim3；reference arxiv:2306.05685；support=partial；原因：The claim states that the paper identified verbosity bias, but the available metadata only mentions position, morbidity, and self-enhancement biases. This introduces a minor inaccuracy.<br>claim SClaim21；reference arxiv:2210.03629；support=partial；原因：The claim implies that ReAct explicitly involves MLLM verifiers providing feedback, but the paper does not use MLLM verifiers in that manner; the feedback comes from environment interactions.<br>claim SClaim21；reference arxiv:2303.11366；support=partial；原因：The claim overstates by attributing MLLM verifier feedback to Reflexion, when the paper uses general task feedback (not specifically MLLM-based). |
| Skill | citation group support | 1 | claim SClaim21；reference None |
| Skill | topic structure issues | 0 | 无 |

### 12299

| Group | Diagnostic type | Count | 摘要 |
|---|---|---:|---|
| Baseline | missing points | 8 | Our method organizes trajectory data into multi-turns of dialogues based on the CoaT thinking pattern. 原因：No candidate claim describes organizing trajectory data into multi-turn dialogues based on CoaT thinking pattern; related claims (SClaim16, SClaim41) do not cover this specific detail.<br>ReFT adopts reinforcement learning as a fine-tuning paradigm to improve performance on math problems. 原因：No candidate claim mentions ReFT or reinforcement learning fine-tuning for math problems.<br>Digirl and Distrl use online trajectory collection for mobile GUI agents, but the process is very slow. 原因：No candidate claim mentions Digirl or Distrl.<br>... 另有 5 条，完整诊断见 JSON |
| Baseline | bad citation-claim pairs | 20 | claim SClaim1；reference aitw；support=weak；原因：AITW is a dataset for Android UI control, not a direct study of VLM-driven agents. The claim discusses general emergence driven by VLMs; AITW serves as a benchmark but is tangentially related.<br>claim SClaim1；reference cogagent；support=unknown；原因：No metadata or retrieved evidence for 'cogagent' is available; the claim's support cannot be assessed.<br>claim SClaim1；reference auto-ui；support=unknown；原因：No metadata or retrieved evidence for 'auto-ui'; cannot assess support.<br>... 另有 17 条，完整诊断见 JSON |
| Baseline | overclaim citation-claim pairs | 1 | claim SClaim41；reference restmcts；support=partial；原因：The claim attributes 'CoaT-tree with rule-based rewards and backward credit assignment' to MobileIPL citing ReST-MCTS*, but ReST-MCTS* does not define CoaT-tree nor mention rule-based rewards; it uses process rewards from tree search. This overstates the similarity. |
| Baseline | citation group support | 2 | claim SClaim1；reference None<br>claim SClaim42；reference None |
| Baseline | topic structure issues | 0 | 无 |
| Skill | missing points | 6 | Closed-source VLM-based agents are used for mobile GUI and multi-agent frameworks. 原因：No candidate claim mentions closed-source VLM-based agents or multi-agent frameworks.<br>ReFT applies reinforcement learning fine-tuning to improve performance on math problems. 原因：No mention of ReFT.<br>Digirl and Distrl use online trajectory collection to improve generalization; however, the process is very slow. 原因：No mention of Digirl or Distrl.<br>... 另有 3 条，完整诊断见 JSON |
| Skill | bad citation-claim pairs | 0 | 无 |
| Skill | overclaim citation-claim pairs | 1 | claim SClaim2；reference arxiv:2312.08914；support=yes；原因：The claim adds 'without relying on HTML or accessibility trees,' but the evidence only specifies that the model does not rely on extracted HTML or OCR text. The exclusion of accessibility trees is not explicitly supported, making this a minor overstatement relative to the cited paper. |
| Skill | citation group support | 1 | claim SClaim5；reference None |
| Skill | topic structure issues | 0 | 无 |

### researcher

| Group | Diagnostic type | Count | 摘要 |
|---|---|---:|---|
| Baseline | missing points | 14 | Multi-agent collaborative writing and multi-module retrieval are used to improve research idea generation. 原因：No candidate claim covers multi-agent collaborative writing and multi-module retrieval for research idea generation.<br>Wang et al. proposed using LLMs to automatically write survey papers. 原因：No candidate claim mentions Wang et al. proposing LLMs for automatic survey writing.<br>Huang et al. introduced a benchmark for evaluating LLMs in coding solutions for machine learning. 原因：No candidate claim mentions Huang et al. introducing a benchmark for coding solutions for machine learning.<br>... 另有 11 条，完整诊断见 JSON |
| Baseline | bad citation-claim pairs | 21 | claim SClaim1；reference llm4sr；support=unknown；原因：No retrieved evidence or metadata available to verify the claim about Luo et al. providing the first systematic survey mapping LLM applications across the full research cycle.<br>claim SClaim2；reference ai_scientist；support=unknown；原因：No retrieved evidence or citation metadata available for reference key 'ai_scientist'. Unable to verify any aspect of the claim from the source.<br>claim SClaim3；reference mlr_copilot；support=unknown；原因：No metadata or retrieved evidence available for reference key 'mlr_copilot'. Unable to verify any aspect of the claim.<br>... 另有 18 条，完整诊断见 JSON |
| Baseline | overclaim citation-claim pairs | 0 | 无 |
| Baseline | citation group support | 2 | claim SClaim12；reference None<br>claim SClaim24；reference None |
| Baseline | topic structure issues | 5 | S2：Paragraph covers a broad range of automation tasks (idea generation, experimentation, writing); could be more focused on specific sub-topic.<br>S3：None significant; well-focused on peer review.<br>S4：Topic is methodological; its connection to scientific research context could be emphasized more in the paragraph.<br>... 另有 2 条，完整诊断见 JSON |
| Skill | missing points | 11 | Multi-agent collaborative writing for research idea generation (Baek et al., 2024) 原因：No candidate claim mentions Baek et al. or multi-agent collaborative writing for research idea generation.<br>Multi-module retrieval for research idea generation (Yang et al., 2023) 原因：No candidate claim mentions Yang et al. or multi-module retrieval for research idea generation.<br>LLMs for scientific literature retrieval (Wang et al., 2023b) 原因：No candidate claim mentions Wang et al. or LLMs for scientific literature retrieval.<br>... 另有 8 条，完整诊断见 JSON |
| Skill | bad citation-claim pairs | 0 | 无 |
| Skill | overclaim citation-claim pairs | 0 | 无 |
| Skill | citation group support | 0 | 无 |
| Skill | topic structure issues | 3 | S2：Paragraph likely covers multiple aspects of LLMs in research, but may intermix idea generation with experimentation; citations are relevant but not all from gold list.<br>S3：Paragraph appears too narrowly focused on data-to-paper, missing broader historical AI-assisted discovery context; only two citations.<br>S4：Citations are relevant, but paragraph could benefit from including more gold citations like CycleReviewer. |

### source

| Group | Diagnostic type | Count | 摘要 |
|---|---|---:|---|
| Baseline | missing points | 6 | MLLMs used to score and filter agent trajectories for finetuning and test-time refinements (prompts, reflections, tools). 原因：No candidate claim mentions MLLMs scoring and filtering agent trajectories for finetuning or test-time refinements.<br>Closely related work uses GPT-4V evaluator prompted with benchmark-specific rubrics to evaluate trajectories for Reflexion and behavior cloning. 原因：No candidate claim mentions GPT-4V evaluator prompted with benchmark-specific rubrics for Reflexion and behavior cloning.<br>Similar evaluator guides tree search, filters trajectories for memories/tools to boost performance in (Visual)WebArena, and for RL training. 原因：No claim about evaluator guiding tree search or filtering trajectories for (Visual)WebArena and RL training.<br>... 另有 3 条，完整诊断见 JSON |
| Baseline | bad citation-claim pairs | 1 | claim SClaim5；reference arxiv:2201.11903；support=no；原因：The cited paper 'Chain-of-Thought Prompting Elicits Reasoning in Large Language Models' focuses on chain-of-thought prompting for reasoning tasks and does not address generative verifiers or the verification process. The abstract mentions 'verifier' only in passing to describe a baseline (finetuned GPT-3 with a verifier) that is surpassed, not to discuss enabling chain-of-thought reasoning during verification. The retrieved evidence confirms the paper's emphasis on few-shot prompting for reasoning, with no mention of generative verifiers. Thus, the claim that chain-of-thought reasoning is enabled during verification by generative verifiers is not supported. |
| Baseline | overclaim citation-claim pairs | 0 | 无 |
| Baseline | citation group support | 1 | claim SClaim3；reference None |
| Baseline | topic structure issues | 0 | 无 |
| Skill | missing points | 4 | MLLMs score and filter agent trajectories for fine-tuning. 原因：No candidate claim explicitly states that MLLMs score and filter agent trajectories for fine-tuning.<br>Closely related work uses a GPT-4V-based evaluator prompted with benchmark-specific rubrics to evaluate trajectories for Reflexion and behavior cloning. 原因：None of the candidate claims mention a GPT-4V-based evaluator with benchmark-specific rubrics used for Reflexion and behavior cloning.<br>Following works employ a similar evaluator to guide tree search, filter trajectories for memory/tool generation, and for RL training. 原因：No candidate claim explicitly describes subsequent works using a similar evaluator for tree search, trajectory filtering for memory/tool generation, or RL training.<br>... 另有 1 条，完整诊断见 JSON |
| Skill | bad citation-claim pairs | 0 | 无 |
| Skill | overclaim citation-claim pairs | 1 | claim SClaim2；reference arxiv:2306.05685；support=partial；原因：The claim asserts that studies have identified and mitigated verbosity preference, but the cited paper does not explicitly address verbosity preference, only position and self-enhancement biases. |
| Skill | citation group support | 3 | claim SClaim12；reference None<br>claim SClaim14；reference None<br>claim SClaim19；reference None |
| Skill | topic structure issues | 2 | S2：No significant issues; some overlap with test-time scaling is acceptable.<br>S5：Only one citation cited; could benefit from more references. |


## 人工审计空白表

上面的自动审计诊断已经提供主要审计证据。这里保留人工审计空白，不要求从零重新标注，只用于确认代表性 case 的自动诊断是否合理，以及是否适合进入前端展示。

| Case | Baseline observation | Skill observation | Needs human check | Human audit notes | Frontend highlight? |
|---|---|---|---|---|---|
| 07794 | Baseline：overall 7.92，citation quality 9.22，relevance 8.33，coverage 3.64；missing points 5，overclaim pairs 1。 | Skill：overall 7.78，citation quality 8.87，relevance 8.61，coverage 4.71；missing points 10，overclaim pairs 0。 | pending |  | false |
| 11662 | Baseline：overall 5.98，citation quality 5.0，relevance 8.4，coverage 3.52；missing points 8，overclaim pairs 0。 | Skill：overall 7.38，citation quality 8.83，relevance 8.7，coverage 4.32；missing points 7，overclaim pairs 3。 | pending |  | false |
| 12299 | Baseline：overall 5.96，citation quality 5.05，relevance 7.09，coverage 3.33；missing points 8，overclaim pairs 1。 | Skill：overall 7.61，citation quality 8.45，relevance 9.52，coverage 3.18；missing points 6，overclaim pairs 1。 | pending |  | false |
| researcher | Baseline：overall 4.88，citation quality 3.5，relevance 3.8，coverage 2.06；missing points 14，overclaim pairs 0。 | Skill：overall 8.03，citation quality 10.0，relevance 6.67，coverage 4.12；missing points 11，overclaim pairs 0。 | pending |  | false |
| source | Baseline：overall 7.07，citation quality 8.34，relevance 8.24，coverage 3.33；missing points 6，overclaim pairs 0。 | Skill：overall 7.82，citation quality 9.11，relevance 8.5，coverage 5.42；missing points 4，overclaim pairs 1。 | pending |  | false |

## 前端数据说明

后续前端图表和 case card 建议直接读取 `analysis/clean_search_summary.json`。其中 `human_audit_placeholders` 已经初始化为 pending 状态，方便人工审计后标记代表性展示案例，而不需要改动原始 RWEval reports。
