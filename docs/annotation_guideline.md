# 标注与评分指南

> 主要负责人：成员 C。目标是用一致的 rubric 评估生成 Related Work 的质量、引用可靠性和抗干扰能力。

## 1. 综合质量评分，100 分

| 维度 | 分值 | 说明 |
|---|---:|---|
| 主题识别 | 15 | 是否识别论文任务、方法和贡献 |
| 检索质量 | 20 | 候选论文是否真实相关 |
| 引用准确性 | 25 | citation 是否真实、相关、支撑对应 claim |
| 结构与逻辑 | 15 | 是否按合理主题组织，而不是堆砌文献 |
| 覆盖度 | 10 | 是否覆盖主要 prior work 类型 |
| 保守性 | 10 | 是否避免无依据结果、数据集或贡献 |
| 可复查性 | 5 | 是否保留 query、候选论文和引用来源 |

## 2. 鲁棒性指标

- Irrelevant Citation Rate：最终引用中无关论文比例。
- Misleading Citation Adoption Rate：误导候选论文被采纳比例。
- Unsupported Claim Count：无输入或检索证据支撑的 claim 数。
- Core Argument Contamination：核心论述是否被错误论文带偏。

## 3. 错误标签

- `wrong-topic citation`：引用主题不相关论文。
- `weakly-related overuse`：把弱相关论文当核心工作。
- `invented citation`：编造论文或来源。
- `unsupported claim`：claim 缺乏输入或检索证据。
- `over-specific claim`：只看摘要却声称细节贡献。
- `structure-only improvement`：结构变好但引用可靠性没提升。

## 4. 标注单位

标注时至少覆盖四个层级：

- 每个 citation；
- 每个 claim-citation pair；
- 每段 Related Work；
- 每篇论文、每个条件、每个实验组的整体结果。

## 5. 人工复查

- 至少两名成员独立打分。
- 分歧较大时进行讨论并记录原因。
- 标注分歧不能直接平均，需要保留 adjudication notes。
- 最终报告展示平均分、分歧范围和典型错误案例。

## 6. 对比原则

不只看 BLEU、ROUGE 或文本相似度。开放检索可能找到不同但合理的 prior work，因此评分重点放在：

- 检索质量；
- 引用准确性；
- claim-citation alignment；
- 对 noisy / misleading papers 的过滤能力；
- 论证结构是否合理。

## 7. 风险与应对

| 风险 | 应对 |
|---|---|
| 评分太主观 | 使用明确 rubric，至少两人独立打分 |
| Workflow 只是少引用 | 同时评分覆盖度、结构质量和引用准确性 |
| Generic Prompt 对照不公平 | 只加入写作结构指导，不加入检索过滤和 citation self-check |
