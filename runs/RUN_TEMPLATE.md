# OpenClaw Related Work 运行记录模板

## 元数据

- Paper ID：
- 匿名化输入：`papers/anonymized_inputs/<paper_id>.txt`
- Ground truth Related Work：
- 实验目录：`runs/clean_search/<experiment>/<paper_id>`
- 实验类型：`diff_prompt`（无 skill）/ `sim_prompt+skill`（有 skill）
- Prompt/workflow 版本：
- 运行时间：
- 检索来源：DeepXiv only

## Prompt 组装

- Base prompt：`prompts/base_prompt.txt`
- 实验命令：`runs/command.txt`
- 输出目录：`runs/clean_search/<experiment>/<paper_id>`

## 检索 Query

| Query | 目的 | 来源 | 时间 |
|---|---|---|---|
|  |  | DeepXiv |  |

## 候选论文

| ID | 标题 | 作者 | 年份/Venue | Source URL/DOI/arXiv ID | 筛选标签 | 原因 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## 最终引用论文

| 标题 | 作者 | 年份 | 来源 | 相关性判断 |
|---|---|---|---|---|
|  |  |  |  |  |

## 生成的 Related Work

在这里粘贴 OpenClaw 输出。

## 引用可靠性标注

| Citation | Claim | 标签 | 备注 |
|---|---|---|---|
|  |  |  |  |

## RWEval 文件检查

实验目录应包含：

```text
runs/clean_search/<experiment>/<paper_id>/
  s_text.txt
  s_reference.txt
  g_text.txt
  g_reference.txt
```

可选文件：

```text
runs/clean_search/<experiment>/<paper_id>/trace.md
```

## Reviewer 备注

- 总分：
- 无关引用比例：
- 误导引用采纳比例：
- 不支持 claim 数量：
- 核心论证污染：
