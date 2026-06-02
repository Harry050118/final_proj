## 主表

| 指标 | Pipeline 打分 | Pipeline 理由 | 人工打分 | 人工打分理由 |
| --- | ---: | --- | ---: | --- |
| content_coverage | 4.58 | Pipeline 指出 candidate 漏掉了 prompt-based 方法局限、AI4Science 历史、单领域被动分析、RewardBench、Generative Reward Model 等关键点 | 4.2 |coverage 确实偏低。candidate 写到了 LLM research automation 和 peer review，但 gold 里很重要的 “AI 从辅助工具变成科学发现领导者”、RewardBench、Generative Reward Model 这些没有写出来 |
| citation_quality | 5.00 | 见下表 | 8.55 | 见下表 |
| relevance | 7.50 | Pipeline 认为 candidate 大体围绕自动科研、自动 peer review、alignment 和 scientific writing， 整体还可以 | 7.50 | 整体是相关的，不是完全跑题。但 Preference Optimization 和 AI-generated text detection 两段和 gold related work 的核心关系比较弱，relevance不够好 |
| thematic_structure | 8.17 | Pipeline 认为结构清楚，但 S3 和 S5 有偏题风险 | 8.20 | 结构本身挺清楚，分段也自然。不过作为目标论文的 related work，第三段和第五段不够好，没有很好服务论文主题 |
| synthesis_quality | 7.50 | Pipeline 认为有一定 synthesis 和 gap framing | 7.50 | 同意 pipeline 的判断 |
| writing_quality | 8.50 | Pipeline 认为语言流畅，学术表达较好 | 8.50 | 同意 pipeline 的判断 |
| length_conciseness | 7.96 | Pipeline 认为篇幅基本合适，但有轻微重复和偏题内容 | 7.50 | 篇幅不算太长，但内容分配不太理想。Preference Optimization 和 AI detection 占的篇幅有点大 |
| overall / final_score | 6.34 | 加权得到 | 7.48 | 加权得到 |

---

## Citation Quality 展开表

| Citation quality 子项 | Pipeline 打分 | Pipeline 理由 | 人工打分 | 人工打分理由 |  |
| --- | ---: | --- | ---: | --- | --- |
| citation_validity | 9.19 | 大多数 reference 能匹配，但 MARG 被标为 metadata mismatch | 9.50 | metadata mismatch是 evaluation pipeline 的问题，不是 openclaw 的问题，所以citation的validity是没什么问题的 |
| citation_appropriateness | 9.39 | Pipeline 列出了 bad citation-claim pairs | 8.50 | 这里 pipeline 给的分偏高。Fast-DetectGPT 的方法可以被引用，但“我们采用它作为 ethical safeguard”这种 claim 不是论文引用本身能证明的 |
| citation_coverage | 7.50 | Pipeline 认为仍有关键 gold references 缺失 | 6.00 | 我打的分更低一点。RewardBench、Generative Reward Model、AI4Science 这些主题这些对 gold 很关键，但 candidate 没有写 |
| citation_placement | 8.61 | Pipeline 认为 citation placement 基本合理 | 9.0 | 同意pipeline |
| citation_topic_consistency | 9.70 | Pipeline 认为引用和段落主题高度一致 | 10.0 | 引用一致性没有问题 |
| citation_quality 综合分 | 5.00 | 加权得到 | 8.55 | 加权得到 |

---