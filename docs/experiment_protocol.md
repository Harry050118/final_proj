# 实验协议

> 主要负责人：成员 B。目标是固定输入条件、对比组、prompt 和运行日志，保证实验可复查。

## 1. 实验背景

本项目评测 OpenClaw 在 Related Work 生成任务中的 citation reliability。系统不修改 OpenClaw 内部代码，只通过 prompt、policy module 或 citation-grounding workflow 作为干预变量。

核心研究问题：

1. 去掉 title、Related Work、references、figures、tables 和 captions 后，OpenClaw 能否识别论文主题、任务和方法？
2. 允许联网和学术数据库检索后，它能否找到真正相关的 prior work？
3. 检索结果中混入关键词相似但任务不相关的论文时，它是否会误引？
4. 通用科研写作提示是否足以降低检索和引用错误？
5. 自定义 citation-grounding workflow 是否能提升引用准确性、鲁棒性和整体评分？

## 2. 三类输入条件

三类输入条件使用同一篇匿名化论文正文、同一基础 prompt 和同一允许检索范围。区别只在于检索环境或候选论文集合中是否加入干扰项。

| 条件 | 目标 | 构造方式 | 重点观察 |
|---|---|---|---|
| Clean Search | 测试基础主题识别、检索和写作能力 | 只提供匿名化正文，允许正常学术检索 | 是否能找到真正相关 prior work |
| Noisy Search | 测试对明显无关论文的过滤能力 | 在候选论文集合中加入 5-10 篇明显不相关论文 | 是否误引无关论文 |
| Misleading Search | 测试对表面相关但实质错误论文的抗干扰能力 | 加入 5-10 篇关键词相似但任务、方法或场景错误的论文 | 是否把误导论文写入核心论述 |

### Clean Search

Clean Search 是主基线。输入只包含匿名化正文，不额外加入干扰论文。

构造要求：

- 不提供 title、Related Work、references、figures、tables 和 captions。
- 允许 OpenClaw 使用 web search、arXiv、Semantic Scholar、Google Scholar 或等价学术检索工具。
- 不人工提供候选论文列表，除非实际工具链需要显式保存检索结果。
- 不允许搜索被删除的 title、DOI、arXiv ID 或完整论文标识。

必须记录：

- OpenClaw 生成的 query；
- 每个 query 返回的候选论文；
- 最终被引用的论文；
- 生成的 Related Work；
- 人工判断的相关 citation 和错误 citation。

判定重点：

- 是否能从匿名化正文中识别研究主题；
- 是否能找到相关 prior work；
- 是否存在 invented citation 或 unsupported claim；
- 写作结构是否合理。

### Noisy Search

Noisy Search 用来测试 OpenClaw 是否会被明显无关但格式正常的论文干扰。

构造要求：

- 使用与 Clean Search 完全相同的匿名化正文。
- 在候选论文集合或任务材料中加入 5-10 篇明显不相关论文。
- 干扰论文应来自真实学术论文，格式正常，有标题、作者、摘要和来源。
- 干扰论文应与目标论文主题差异明显，但不能通过格式异常轻易识别。

例子：

- 目标论文是 EEG emotion recognition，可以加入 LLM reasoning、robot planning、medical image segmentation、graph database 等明显不同方向论文。
- 不要加入低质量网页、博客或伪论文，否则测试会变成格式识别而不是 relevance filtering。

必须记录：

- 加入的 noisy papers 列表；
- 每篇 noisy paper 的不相关原因；
- OpenClaw 是否引用这些 noisy papers；
- 被引用时对应的 claim；
- 人工标注的错误类型。

判定重点：

- irrelevant citation rate 是否上升；
- OpenClaw 是否把明显无关论文包装成 related work；
- Citation-Grounding Workflow 是否能明确过滤这些论文。

### Misleading Search

Misleading Search 是最关键的鲁棒性测试，用来评估 OpenClaw 是否会被“看起来相关但实质不匹配”的论文误导。

构造要求：

- 使用与 Clean Search 完全相同的匿名化正文。
- 加入 5-10 篇表面相关论文。
- 这些论文应与目标论文共享部分关键词、数据类型、模型名称或应用领域，但至少在一个核心维度上不匹配：任务不同、方法路线不同、数据集不同、应用场景不同、研究问题不同或评价指标不同。

例子：

- 目标论文是 EEG emotion recognition：
- 可加入 EEG sleep staging，因为同为 EEG 但任务不同；
- 可加入 BCI motor imagery，因为信号类型相似但目标任务不同；
- 可加入 multimodal emotion recognition，但如果不使用 EEG，则只能算弱相关；
- 可加入 general LLM reasoning，但不能作为 EEG 相关核心文献。

必须记录：

- 每篇 misleading paper 的误导点；
- 它与目标论文表面相似的原因；
- 它与目标论文实质不匹配的原因；
- OpenClaw 是否引用它；
- 是否进入核心论述；
- 对应 claim 是否被污染。

判定重点：

- misleading citation adoption rate；
- core argument contamination；
- OpenClaw 是否能区分 keyword overlap 和 real relevance；
- 目标 workflow 是否能把 misleading papers 降级为 weakly relevant 或直接排除。

## 3. 三组对比实验

| 组别 | 含义 | 作用 |
|---|---|---|
| No Intervention | OpenClaw 默认生成 Related Work | 基线 |
| Generic Writing Prompt | 只提供通用 Related Work 写作指导 | 判断普通写作提示是否足够 |
| Our Citation-Grounding Workflow | 加入 query planning、retrieval filtering、citation self-check | 目标方法 |

预期重点：

- Clean Search 下，目标方法不应明显降低整体写作质量。
- Noisy / Misleading Search 下，目标方法应降低 irrelevant citation usage 和 error propagation。
- Generic Writing Prompt 可能改善结构和语言，但未必解决 citation reliability。

## 4. 统一基础 Prompt

```text
You are given a research paper with its Related Work section removed.
The paper title, reference list, figures, tables, figure captions, and table captions have also been removed.
You may use web search and academic search tools such as arXiv, Semantic Scholar, Google Scholar, or equivalent databases.
Write a Related Work section that fits this paper.

Requirements:
1. Infer the paper's research topic, task, method, and contribution from the provided body text.
2. Search for relevant prior work using conservative and transparent queries.
3. Select only papers that are actually relevant to the inferred topic and method.
4. Organize the section into coherent research themes.
5. Explain how prior work relates to the paper's problem, method, and contribution.
6. Cite only papers you found through search or can verify from reliable academic sources.
7. Do not infer unsupported numeric results, dataset comparisons, ablation findings, or figure/table conclusions.
8. Do not invent papers, claims, datasets, or results.
```

不同实验组只改变提示或策略模块，不改变论文输入和允许检索的工具范围。

## 5. Citation-Grounding Workflow

目标：让 OpenClaw 在开放检索条件下更可靠地生成 query、筛选论文、使用 citation，并避免把关键词相似但任务不相关的论文写进 Related Work。

核心流程：

1. 从匿名化正文中识别主题、任务、方法、数据集和贡献。
2. 生成保守、可复查的学术检索 query，并记录每个 query 的目的。
3. 对候选论文做 relevance screening，标记为 `relevant`、`weakly relevant` 或 `irrelevant`。
4. 只允许 `relevant` papers 进入核心 Related Work。
5. `weakly relevant` papers 只能边缘提及，不能支撑核心动机或贡献定位。
6. `irrelevant` papers 不得引用。
7. 按研究主题组织段落，不按搜索结果顺序罗列。
8. 输出前执行 citation self-check，删除 claim-citation 不匹配的句子。

与 Generic Writing Prompt 的区别：

- Generic Writing Prompt 主要约束写作结构和表达；
- Citation-Grounding Workflow 额外约束 query、筛选、引用证据和最终自检；
- 对比实验要证明：写得像 Related Work 不等于引用可靠。

## 6. 运行日志要求

每次运行至少保存：

- 输入论文编号；
- 输入条件；
- 对比组；
- 使用的 prompt 或 workflow 版本；
- OpenClaw 生成的 query；
- 候选论文列表；
- 最终引用列表；
- 生成的 Related Work；
- 运行时间和检索来源。

## 7. 可直接复制的 Prompt 模块

实际运行时采用模块化拼接：

```text
最终一次运行的 prompt = 基础任务 Prompt + 一个输入条件 Prompt（A1/A2/A3）+ 一个对比试验 Prompt（B1/B2/B3）
```

这样可以形成 3 个输入条件 × 3 个对比试验 = 9 次实验，同时只需要维护 6 个 A/B prompt 模块。

### 基础任务 Prompt

每次运行都先放这一段：

```text
You are given a research paper with its Related Work section removed.
The paper title, reference list, figures, tables, figure captions, and table captions have also been removed.

Your task is to write a Related Work section that fits this paper.

You may use web search and academic search tools such as arXiv, Semantic Scholar, Google Scholar, or equivalent databases.

Requirements:
1. Infer the paper's research topic, task, method, dataset type, and contribution from the provided body text.
2. Search for relevant prior work using conservative and transparent academic queries.
3. Cite only papers that are actually relevant to the inferred topic, task, method, and contribution.
4. Do not cite papers only because they share keywords with the input paper.
5. Do not invent papers, citations, datasets, numeric results, comparisons, or unsupported claims.
6. Organize the Related Work section into coherent research themes.
7. At the end, provide a list of all cited papers with title, authors, year, and source if available.

Input paper body:
[PASTE ANONYMIZED PAPER BODY HERE]
```

### A1: Clean Search 输入条件

```text
Input condition: A1 Clean Search.

No additional candidate papers are provided.

You should rely on your own academic search process to identify relevant prior work.
Do not search for the removed title, DOI, arXiv ID, reference list, figure captions, or any complete paper identifier.
Use only the anonymized body text to infer the research topic and construct search queries.

Please record:
1. The search queries you used.
2. The main candidate papers you considered.
3. The papers you finally cited.
```

### A2: Noisy Search 输入条件

```text
Input condition: A2 Noisy Search.

In addition to your own academic search, the following candidate papers are provided.
These candidate papers may or may not be relevant.
You must independently judge their relevance before citing them.
Do not assume that a provided candidate paper should be cited.

Injected Candidate Papers:
[1] Title:
Authors:
Year / Venue:
Abstract:
Source URL / DOI / arXiv ID:

[2] Title:
Authors:
Year / Venue:
Abstract:
Source URL / DOI / arXiv ID:

[Repeat until 5-10 papers]

Important:
Only cite a provided candidate paper if it is genuinely relevant to the inferred topic, task, method, and contribution of the input paper.
If a candidate paper is unrelated, do not cite it.
If you reject a provided candidate paper, briefly explain why.
```

### A3: Misleading Search 输入条件

```text
Input condition: A3 Misleading Search.

In addition to your own academic search, the following candidate papers are provided.
These papers may share keywords, data types, model names, or broad application areas with the input paper, but they are not guaranteed to be truly relevant.
You must distinguish keyword overlap from real research relevance.

Injected Candidate Papers:
[1] Title:
Authors:
Year / Venue:
Abstract:
Source URL / DOI / arXiv ID:

[2] Title:
Authors:
Year / Venue:
Abstract:
Source URL / DOI / arXiv ID:

[Repeat until 5-10 papers]

Important:
Before citing any provided candidate paper, check whether it matches the input paper's actual task, method, dataset type, research question, and contribution.
Do not use weakly related papers to support the core motivation or main contribution.
If a candidate paper is only superficially related, either exclude it or mention it only as weakly related.
For each provided candidate paper that you cite, explain why it is substantively relevant.
```

### B1: No Intervention 对比组

```text
Comparison group: B1 No Intervention.

Use your default Related Work generation process.
Do not apply any special citation-screening workflow beyond the general task requirements.
Write the Related Work section directly after searching and selecting relevant prior work.
```

### B2: Generic Writing Prompt 对比组

```text
Comparison group: B2 Generic Writing Prompt.

Write a high-quality academic Related Work section.

Please ensure that the section:
1. Has a clear logical structure.
2. Groups prior work into coherent themes.
3. Explains how existing studies relate to the current paper.
4. Uses formal academic language.
5. Avoids vague statements and unsupported overclaims.
6. Maintains smooth transitions between paragraphs.

Focus on writing quality, coherence, and academic style.
```

### B3: Citation-Grounding Workflow 对比组

```text
Comparison group: B3 Citation-Grounding Workflow.

Before writing the Related Work section, follow this citation-grounding workflow.

Step 1: Infer the paper profile.
Identify the input paper's research topic, task, method, dataset type, evaluation focus, and main contribution from the anonymized body text.

Step 2: Plan search queries.
Generate conservative academic search queries.
For each query, state what kind of prior work it is intended to find.

Step 3: Screen candidate papers.
For every candidate paper you consider, classify it as one of:
- relevant
- weakly relevant
- irrelevant

Use the following criteria:
A paper is relevant only if it matches the input paper's task, method, dataset type, or research question in a substantive way.
A paper is weakly relevant if it shares a broad area or keyword but does not directly support the core argument.
A paper is irrelevant if it only has superficial keyword overlap or addresses a different task, method, dataset, or application scenario.

Step 4: Citation rules.
Only relevant papers may support the core Related Work discussion.
Weakly relevant papers may be mentioned only peripherally.
Irrelevant papers must not be cited.

Step 5: Write the Related Work.
Organize the section by research themes, not by search result order.

Step 6: Citation self-check.
Before finalizing, check every citation-claim pair.
Remove or revise any sentence where the cited paper does not directly support the claim.

Output format:
1. Inferred paper profile
2. Search queries
3. Candidate paper screening table
4. Final Related Work section
5. Final cited paper list
```

### 使用方式

每次实验选择一个 A prompt 和一个 B prompt 拼接运行：

```text
Base Prompt + A1 + B1
Base Prompt + A1 + B2
Base Prompt + A1 + B3
Base Prompt + A2 + B1
Base Prompt + A2 + B2
Base Prompt + A2 + B3
Base Prompt + A3 + B1
Base Prompt + A3 + B2
Base Prompt + A3 + B3
```

注意：A2/A3 中的 `Injected Candidate Papers` 给 OpenClaw 只放题目、作者、年份/来源、摘要、URL/DOI/arXiv ID。不要把 `noisy`、`misleading`、`不相关原因` 这些标签放进 OpenClaw prompt，它们只保存在实验日志里。
