# 论文与输入构造协议

> 主要负责人：成员 A。目标是为每篇论文制作可复查、可重复使用的匿名化输入和 ground truth Related Work。

## 1. 论文选择

优先选择 3-5 篇 pilot 论文，满足以下条件：

- 研究方向明确，Related Work 结构清楚。
- 论文较新、非高引用，降低模型凭预训练记忆复现原文的风险。
- 正文中有足够信息让模型推断任务、方法和贡献。
- 不依赖图表才能理解核心任务，否则删除图表后信息会不足。

暂不选择：

- 过于经典或高引用的论文。
- 标题、数据集或方法名称极易唯一定位的论文。
- Related Work 很短或结构混乱、难以作为评测参照的论文。

## 2. 匿名化输入

每篇论文构造一个匿名化输入，用于所有实验条件。

保留：

- Abstract；
- Introduction；
- Method；
- Experiments 正文描述；
- Conclusion。

删除：

- Title；
- 原 Related Work；
- References / Bibliography；
- Figures、Tables；
- Figure captions、Table captions；
- 明显复述 Related Work 的附录段落。

控制要求：

- 不在输入中保留 DOI、arXiv ID 或完整论文标识。
- 不直接搜索被删除的 title、DOI、arXiv ID 或完整论文标识。
- 保留实验正文描述，但不保留图表和 caption。
- 如果删除图表后导致任务不可理解，需要记录该论文不适合进入主实验。

## 3. Ground Truth Related Work

为每篇论文单独保存原 Related Work，作为人工评测参照。

用途：

- 辅助判断生成内容是否覆盖合理 prior work 类型。
- 辅助识别 OpenClaw 是否生成与原 Related Work 逐句高度相似的内容。
- 不作为自动文本相似度的唯一标准，也不要求生成内容复刻原 references。

## 4. 必须记录

每篇论文至少记录：

- 原始论文文件名或来源；
- 匿名化输入文件；
- 删除内容清单；
- ground truth Related Work；
- 是否存在唯一标识残留；
- 是否存在删除图表后信息不足的问题。

## 5. 风险与应对

| 风险 | 应对 |
|---|---|
| 模型可能记得原论文 Related Work | 优先选择较新、非高引用论文，并检查输出是否与原 Related Work 高度相似 |
| 删除图表后信息不足 | 保留实验正文描述；如果仍不足，则替换论文 |
| 匿名化不彻底 | 检查 title、DOI、arXiv ID、完整论文标识和显式引用线索 |
