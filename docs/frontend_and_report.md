# 前端展示与最终报告

> 主要负责人：成员 D。目标是把实验设置、结果和典型案例整理成易展示、易答辩的材料。

## 1. 前端展示目标

展示页不需要覆盖所有过程细节，重点让读者快速理解：

- 项目评测什么问题；
- 三类输入条件和三组对比方法是什么；
- Citation-Grounding Workflow 是否降低错误引用；
- 典型成功和失败案例是什么；
- OpenClaw 暴露了哪些可靠性问题。

## 2. 最小可行展示

- 项目简介；
- 实验设置；
- 三组对比结果；
- citation 错误案例；
- 评分雷达图或柱状图；
- 结论与风险。

## 3. 页面结构建议

1. Overview：一句话介绍任务和核心发现。
2. Experiment Setup：展示输入条件、对比组和评分维度。
3. Results Dashboard：展示总分、引用错误率、误导采纳率。
4. Case Study：展示原文输入、候选论文、模型输出和人工标签。
5. Takeaways：总结 OpenClaw 的缺陷和改进方向。

## 4. 最终报告结构

建议报告按以下顺序组织：

1. Problem：为什么 Related Work generation 能代表 citation-grounded scientific writing。
2. Setup：匿名化输入、三类条件、三组对比方法。
3. Method：Citation-Grounding Workflow 的设计。
4. Evaluation：评分表、鲁棒性指标、人工标注方式。
5. Results：总分、错误率、典型案例。
6. Discussion：OpenClaw 的缺陷、workflow 的有效性和局限。
7. Conclusion：最终结论和 future work。

## 5. PPT 建议

PPT 控制在 8-12 页：

1. 项目问题；
2. 为什么选择 Related Work；
3. 实验设置；
4. 三类输入条件；
5. 三组对比方法；
6. 评分指标；
7. 主要结果；
8. 典型错误案例；
9. 改进效果；
10. 结论与限制。

## 6. 必须展示的案例

- 至少一个 Clean Search 下写作质量较好的案例。
- 至少一个 Noisy Search 下误引明显无关论文的案例。
- 至少一个 Misleading Search 下被表面相关论文误导的案例。
- 至少一个 Citation-Grounding Workflow 成功过滤错误 citation 的案例。
