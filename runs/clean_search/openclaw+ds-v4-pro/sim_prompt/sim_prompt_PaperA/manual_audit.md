# Evaluation Tables Based on New Pipeline Report

## 主表

| 指标                    | Pipeline 分 | Pipeline 理由                                                                                                                                                                                     | 人工分 | 人工打分理由                                                                                                                                                                                                    |
| --------------------- | ---------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| content_coverage      |       3.64 | Pipeline 指出 candidate 漏掉多个 gold 核心点：ReAct、Chain-of-Retrieval、DeepRAG、heuristic/classifier adaptive retrieval、SMART/SMARTCAL/OTC，以及 HiPRAG 的 direct on-the-fly search-step necessity evaluation | 3.8 | 同意 pipeline 的主要判断candidate 覆盖了 RAG、IRCoT、Self-RAG、Search-o1、Search-R1、R1-Searcher 系列和 process reward，但 gold 中 agentic tool use、adaptive retrieval、tool overuse mitigation 这些主线缺失明显          |
| citation_quality      |       9.11 | Pipeline 认为没有 hallucinated references，也没有 bad citation-claim pairs；但发现若干 bibliographic accuracy issues，并指出 DeepSeek-R1 对 search/RAG RL 的支持只是 partial，存在 mild overclaim                         | 8.0 | 引用整体真实可查，未发现明显伪造文献。但 citation quality 不能接近满分，因为存在 bibliographic metadata 不一致、DeepSeek-R1 支持 search-agent RL 只是间接支持、部分 citation group 概括偏宽，以及 gold citation coverage 仍有缺口 |
| relevance             |       8.33 | Pipeline 新版认为 candidate 与目标任务整体高度相关，主要围绕 RAG、agentic search、RL search agent 和 process reward                                                                                                 | 7.6 | candidate 的确基本相关，但没有明确写出 HiPRAG 的核心差异                                                |
| thematic_structure    |       8.57 | Pipeline 认为结构清楚；仅指出 S2 可以更深入连接 tool use，S4 对 math reasoning process reward 的强调略窄但仍相关                                                                                                           | 8.2 | 三段结构自然：RAG/Agentic RAG → RL Search Agents → Process Rewards/Search Efficiency。但第三段仍偏 paper-by-paper summary                                                                                   |
| synthesis_quality     |       8.00 | Pipeline 认为 candidate 有较好的 gap framing，能够指出 outcome-level reward 和 proxy/process reward 的局限                                                                                                  | 7.5 | 有综合和 gap，但还不够像真正人工写的 related work。不同方法路线之间的比较不够系统，例如 adaptive retrieval、confidence heuristic等没有清晰分层                                                           |
| writing_quality       |       8.00 | Pipeline 认为语言流畅、学术表达成熟                                                                                                                                                                         | 7.69 | 写作质量较好，段落衔接自然。但个别表述不够谨慎，例如把 Self-RAG 放进 frozen prompting-based methods                                                                     |
| length_conciseness    |       7.58 | Pipeline 未发现 length/conciseness 问题                                                                                                                                                             | 8.4 | 篇幅合适，没有明显冗余。但内容分配不够理想：部分篇幅给了新增 process-RAG 工作，而 gold 中关键背景没有补足                                                                                                                                           |
| overall / final_score |       7.08 | Pipeline 综合分为 7.08；低 coverage 被较高 citation、structure、writing 和 relevance 拉回                                                                                                                    | 7.0 | 人工总分与 pipeline 接近。candidate 不是引用造假型问题，而是 gold coverage 不足、部分 claim 概括偏强、HiPRAG 差异点没有明确写出。整体属于可用但需要补关键文献线的 related work                                                                               |

---

## Citation Quality 展开表

| Citation quality 子项        | Pipeline 分 | Pipeline 理由                                                                                           | 人工分 | 人工打分理由                                                                                                                                                     | Pipeline 和人工对齐情况        |
| -------------------------- | ---------: | ----------------------------------------------------------------------------------------------------- | --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| citation_validity          |       9.25 | Pipeline 未发现 hallucinated references，但因部分 bibliographic metadata 无法完全核验或存在年份差异，所以低于满分                | 9.0 | 同意 14 条 reference 整体真实可识别；R2、R3、R10 的年份差异主要是 arXiv 年份与会议发表年份不同                                                                                   | 对齐                   |
| citation_appropriateness   |       8.79 | Pipeline 未发现 bad citation-claim pairs，但指出 DeepSeek-R1 对 search/RAG RL 的支持是 partial，属于 mild overclaim | 8.2 | 大多数引用能支撑附近 claim，但支持强度并不都很直接。DeepSeek-R1 只能支持 RL reasoning 背景，不能直接支持 autonomous search/RAG RL；Self-RAG 被归入 frozen prompting-based methods 也不够准确           | Pipeline 略高           |
| citation_coverage          |       6.67 | Pipeline 仍指出多个 gold key points 缺失                                                | 5.0 | 我认为 coverage 仍应更低。candidate 漏掉 ReAct、Chain-of-Retrieval、DeepRAG、ToolRL、ToRL、ReARTeR、OTC 等核心 gold references。虽然它覆盖了不少相关替代文献，但对 gold 的忠实覆盖不足 | Pipeline 偏高        |
| citation_placement         |       9.39 | Pipeline 认为 citation placement 基本合理。                                                                  | 8.6 | 引用位置整体合理，没有明显 citation dump。但部分 group citation 边界较宽异。                                                | pipeline 略高              |
| citation_topic_consistency |       9.26 | Pipeline 认为引用与段落主题高度一致。                                                                               | 8.5 | 大方向一致，基本都属于 RAG、agentic search、RL、process reward。但 topic consistency 不等于 claim-level support                          | pipeline 略高       |
| citation_quality 综合分       |       9.11 | Pipeline 认为引用质量总体很高，但受 bibliographic accuracy issues 和 mild overclaim 影响略低于满分。                        | 8.0 | 引用真实性较好，但不能忽略 citation coverage 缺口、间接支持、group citation 过宽和少量过度概括。人工分应低于 pipeline                                                          | pipeline 偏高 |

---

## 简短人工结论

candidate 的主要问题不是 reference 伪造，而是 **gold coverage 不足**。


最终人工分建议：**7.1 / 10**。
