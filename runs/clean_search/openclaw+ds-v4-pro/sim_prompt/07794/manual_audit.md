# 人工评测内容表

## 主表

| 指标                    | Pipeline 分 | Pipeline 理由                                                                                                                                                     | 人工分 | 人工打分理由                                                                                                                                                                                           |
| --------------------- | ---------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| content_coverage      |       3.64 | 报告指出 candidate 漏掉 ReAct、Chain-of-Retrieval、DeepRAG、heuristic/classifier adaptive retrieval、SMART/SMARTCAL/OTC，以及 HiPRAG 的 on-the-fly step necessity evaluation。 | 4.8 | Pipeline 对缺失点判断基本正确。candidate 覆盖了 RAG、IRCoT、Self-RAG、Search-o1、Search-R1 系列和 process reward，但对 gold 中的 agentic tool use、adaptive retrieval、tool overuse mitigation 覆盖不足，因此只能给中低分。                |
| citation_quality      |       9.22 | 报告认为 reference 都可识别，没有 hallucinated references，也没有明显 bad citation-claim pair；只指出 DeepSeek-R1 相关 claim 有 mild overclaim。                                         | 8.1 | 逐条核查后，14 条 reference 基本真实可查，DeepSeek-R1 被用于引出 search-agent RL 属于间接支持；Self-RAG 被归入 frozen prompting-based methods 不够准确；citation coverage 明显不足。 |
| relevance             |       5.33 | Pipeline 可能因为 candidate 没有覆盖多个 gold 核心点，尤其没有明确写出 HiPRAG 的 direct on-the-fly evaluation，所以给出较低分。                                                                 | 6.0 | Candidate 的内容整体仍然围绕 HiPRAG 的问题域，包括 RAG、agentic retrieval、RL search agent、over-search/under-search 和 process reward。问题主要是 gold 覆盖不足，不是大面积偏题。                                                      |
| thematic_structure    |       8.57 | Pipeline 认为三段结构清晰，只指出部分段落与 tool use 的连接可以更深入。                                                                                                                   | 8.3 | 三段结构合理：RAG/Agentic RAG → RL Search Agents → Process Rewards/Search Efficiency。段落顺序自然，但第三段仍略像论文罗列。                                                                                                |
| synthesis_quality     |       8.00 | Pipeline 认为 candidate 有较好的 gap framing，能够指出 outcome reward 和 proxy/process reward 的不足。                                                                          | 7.6 | Candidate 有基本综合能力，能把现有工作引向“缺少 step-level search decision feedback”的 gap。但不同路线之间的比较还不够细，比如 adaptive retrieval、confidence heuristic、learned PRM、direct verification 没有系统展开。                        |
| writing_quality       |       9.00 | Pipeline 认为语言流畅、学术风格较好。                                                                                                                                         | 8.5 | 写作整体清楚、正式、可读性强。但个别表述过度概括，例如把 Self-RAG 放进 frozen prompting-based methods，以及把 RL search-agent 方法统一说成 outcome-only reward。                                                                          |
| length_conciseness    |       8.58 | Pipeline 没有发现明显冗余或篇幅问题。                                                                                                                                         | 8.4 | 篇幅合适，段落不拖沓。但部分空间用于新增 process-RAG 工作，反而没有补足 gold 里的 ReAct、DeepRAG、ToolRL、SMART 等核心背景。                                                                                                             |
| overall / final_score |       7.12 | Pipeline 综合后给 7.12，主要由较高的 citation、structure、writing 分数拉高，同时 coverage 和 relevance 较低。                                                                           | 7.2 | 人工总分与 pipeline 接近。主要调整是：content coverage 仍然偏低；citation quality 经逐条核查后应保持较高，但不应满分；relevance 比 pipeline 稍高。整体是“写得不错、引用基本真实，但 gold 覆盖不足”的样本。                                                        |

---

## Citation Quality 展开表

| Citation quality 子项        | Pipeline 分 | Pipeline 理由                                                                        | 人工分 | 人工打分理由                                                                                                                                                              | Pipeline 和人工对齐情况                                         |
| -------------------------- | ---------: | ---------------------------------------------------------------------------------- | --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| citation_validity          |      10.00 | Pipeline 判断没有 hallucinated references。                                             | 9.2 | 逐条核查后，14 条 reference 基本都能在 arXiv、ACL Anthology、NeurIPS 或 OpenReview 找到对应记录。                                       | 基本对齐。Pipeline 在 reference 真实性判断上基本正确。                    |
| citation_appropriateness   |       9.79 | Pipeline 没有发现 bad citation-claim pairs。                                            | 7.8 | 大多数 citation 可以支撑对应 claim，但仍有几处支持强度偏弱。例如 DeepSeek-R1 支持“RL 激发 reasoning”，但用于说明 autonomous search/RAG RL 的启发属于间接推断；Self-RAG 被归为 frozen prompting-based method 也不够准确。 | Pipeline 略高估。它更关注 broad match，我更关注 claim-level support。 |
| citation_coverage          |       3.67 | Pipeline 认为 candidate 漏掉大量 gold references。                                        | 4.2 | 低分合理。Candidate 没有覆盖 ReAct、Chain-of-Retrieval、DeepRAG、ToolRL、ToRL、ReARTeR、SMART、SMARTCAL、OTC 等 gold 中的重要 reference。                                              | 基本对齐。Citation coverage 是最明显短板。                           |
| citation_placement         |       9.79 | Pipeline 认为 citation 放置位置合理。                                                       | 9.5 | 引用大多贴近 claim，placement 没有严重问题。但部分 citation group 范围较宽，例如 [6]-[9] 一起支撑 RL search-agent 局限，容易掩盖不同方法 reward 设计的差异。                                                     | 基本对齐                                    |
| citation_topic_consistency |       9.86 | Pipeline 认为 citation 与段落主题高度一致。                                                    | 9.3 | 大多数 reference 与 RAG、agentic retrieval、RL search、process reward 主题一致。但 topic consistency 不能完全替代 claim-level appropriateness，所以不能给接近满分。                               | 基本对齐                           |
| citation_quality 综合分       |       9.22 | Pipeline 综合 validity、appropriateness、coverage、placement 和 topic consistency 后给出高分。 | 8.1 | Reference 真实性整体较强，没有确认出伪造文献。但 citation coverage 很低，且存在少量 over-generalization 和 weak support            | Pipeline 总体方向正确，但对 coverage 缺陷和 claim-level 弱支持扣分不够。     |

---

## 核心人工结论

candidate 的主要问题不是“引用造假”，而是“覆盖不完整”和“部分概括过强”。

最终人工分：**7.2 / 10**。
