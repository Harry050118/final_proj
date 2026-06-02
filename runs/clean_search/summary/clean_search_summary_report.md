# clean_search 评测分数汇总与图表说明

## 数据来源

本次重新读取 `D:\college\llm\final_proj\runs\clean_search` 下所有最后一级评测文件夹，共检查到 `35` 个 `report.md` 和 `35` 个 `report.json`，二者一一对应。分数提取以 `report.json` 为准。

当前数据包含 35 个评测结果：原始主比较结果，以及 `sim_prompt+memory` 下 5 篇论文 × high/low/no memory 的 15 个结果。对于 memory 结果，task 使用外层目录名，memory level 从最后一级目录解析。原始 CSV 保留目录名，同时新增 `paper_label` 字段；图表和 Markdown 使用 Paper 标签展示。

## 论文目录对应关系

| 原始目录/task | 论文显示名 |
|---|---|
| `07794` | `PaperA` |
| `11662` | `PaperB` |
| `12299` | `PaperC` |
| `researcher` | `PaperD` |
| `source` | `PaperE` |

## 主比较规则

`OpenClaw + DS-v4-Pro` 与 `OpenClaw + DS-v4-Pro + No Memory` 是同一配置。最终主比较中只使用 no-memory 的五篇结果，并将其显示为 `OpenClaw + DS-v4-Pro`。旧的 `openclaw+ds-v4-pro\sim_prompt` 五行仍保留在 `clean_search_scores_full.csv` 中用于追溯，但不进入主图、主表、heatmap 或 group summary。

`OpenClaw + Kimi-K2.6` 的展示均值根据当前五篇逐篇分数实时计算；逐篇原始分数仍保留在明细表中。

## 图中缩写说明

| 图中缩写 | 完整含义 |
|---|---|
| `CC+DS` | `Claude Code + DS-v4-Pro` |
| `OC+Kimi` | `OpenClaw + Kimi-K2.6` |
| `OC+DS` | `OpenClaw + DS-v4-Pro`，数据来自 no-memory 结果 |
| `OC+DS+Skill` | `OpenClaw + DS-v4-Pro + Skill` |
| `OC+DS+LowMem` | `OpenClaw + DS-v4-Pro + Low Memory` |
| `OC+DS+HighMem` | `OpenClaw + DS-v4-Pro + High Memory` |

其中 `CC` 表示 Claude Code 框架，`OC` 表示 OpenClaw 框架，`DS` 表示 DS-v4-Pro 模型，`Mem` 表示 memory 配置。

## 生成文件清单

| 文件 | 用途 |
|---|---|
| `clean_search_scores_full.csv` | 35 个评测的完整原始明细。 |
| `clean_search_group_summary.csv` | 6 组主比较方法的均值和标准差。 |
| `clean_search_overall_by_task.tex` | standalone LaTeX 主结果表。 |
| `clean_search_metrics_full.tex` | standalone LaTeX 详细指标表。 |
| `clean_search_overall_by_task_table.pdf/png` | 不依赖 LaTeX 的主结果表。 |
| `clean_search_metrics_full_table.pdf/png` | 不依赖 LaTeX 的详细指标表。 |
| `clean_search_overall_by_task.pdf/png` | 图 1：逐 task Overall 对比。 |
| `clean_search_group_summary.pdf/png` | 图 2：主比较方法总体均值 ± 标准差。 |
| `clean_search_metric_heatmap.pdf/png` | 图 3：主比较方法关键指标热力图。 |
| `clean_search_memory_ablation.pdf/png` | 图 4：high/low/no memory 在五篇论文上的消融图。 |

## 主结果表

| 方法 | PaperA | PaperB | PaperC | PaperD | PaperE | Mean | Std |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude Code + DS-v4-Pro | 7.33 | 5.89 | 6.14 | 6.92 | 5.41 | 6.34 | 0.70 |
| OpenClaw + Kimi-K2.6 | 6.37 | 6.98 | 6.74 | 7.07 | 6.85 | 6.80 | 0.24 |
| OpenClaw + DS-v4-Pro | 6.96 | 6.43 | 6.89 | 6.17 | 6.24 | 6.54 | 0.33 |
| OpenClaw + DS-v4-Pro + Skill | 7.75 | 7.36 | 7.59 | 8.00 | 7.80 | 7.70 | 0.21 |
| OpenClaw + DS-v4-Pro + Low Memory | 7.77 | 7.20 | 6.73 | 6.85 | 7.83 | 7.28 | 0.46 |
| OpenClaw + DS-v4-Pro + High Memory | 7.11 | 7.95 | 8.37 | 7.28 | 8.48 | 7.84 | 0.56 |

## 方法总体汇总

| 方法/条件 | 图中缩写 | n | Overall mean | Overall std | Content coverage mean | Citation quality mean | Citation coverage mean |
|---|---|---:|---:|---:|---:|---:|---:|
| Claude Code + DS-v4-Pro | CC+DS | 5 | 6.34 | 0.70 | 3.32 | 6.58 | 5.78 |
| OpenClaw + Kimi-K2.6 | OC+Kimi | 5 | 6.80 | 0.24 | 3.91 | 7.67 | 3.99 |
| OpenClaw + DS-v4-Pro | OC+DS | 5 | 6.54 | 0.33 | 3.16 | 7.34 | 4.80 |
| OpenClaw + DS-v4-Pro + Skill | OC+DS+Skill | 5 | 7.70 | 0.21 | 4.35 | 8.98 | 5.88 |
| OpenClaw + DS-v4-Pro + Low Memory | OC+DS+LowMem | 5 | 7.28 | 0.46 | 5.37 | 8.11 | 5.99 |
| OpenClaw + DS-v4-Pro + High Memory | OC+DS+HighMem | 5 | 7.84 | 0.56 | 6.14 | 7.86 | 6.45 |

## Memory 消融

| Memory | PaperA | PaperB | PaperC | PaperD | PaperE | Mean | Std |
|---|---:|---:|---:|---:|---:|---:|---:|
| no | 6.96 | 6.43 | 6.89 | 6.17 | 6.24 | 6.54 | 0.33 |
| low | 7.77 | 7.20 | 6.73 | 6.85 | 7.83 | 7.28 | 0.46 |
| high | 7.11 | 7.95 | 8.37 | 7.28 | 8.48 | 7.84 | 0.56 |

## 主要观察

- 主比较中，`OpenClaw + DS-v4-Pro + High Memory` 的 Overall mean 最高，为 `7.84`。
- `OpenClaw + DS-v4-Pro + Skill` 的 Overall std 最小，为 `0.21`，说明跨五篇论文波动最小。
- Memory 消融现在覆盖五篇论文，因此可以进入主比较；但 no/low/high memory 应分开展示，不能合并成一个 `Memory` 条件。
- 逐 task 表格仍然比单一均值更重要，因为不同配置在不同论文样本上的优势并不完全一致。

## 使用建议

论文主文建议放 `clean_search_overall_by_task.tex` 或 `clean_search_overall_by_task_table.pdf`，再配合 `clean_search_overall_by_task.pdf`。附录建议放 `clean_search_metrics_full.tex`、`clean_search_metric_heatmap.pdf` 和 `clean_search_memory_ablation.pdf`。如果本机没有 LaTeX，直接使用 `*_table.pdf/png` 即可。
