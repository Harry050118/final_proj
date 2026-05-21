# 仓库目录创建方案

> 全组共用。目标是统一文件放置位置，避免实验输入、输出、标注和报告材料混在一起。

## 1. 推荐目录结构

```text
final_proj/
├── README.md
├── docs/
│   ├── paper_input_protocol.md
│   ├── experiment_protocol.md
│   ├── annotation_guideline.md
│   ├── frontend_and_report.md
│   └── repo_structure.md
├── papers/
│   ├── raw/
│   ├── anonymized_inputs/
│   └── ground_truth_related_work/
├── prompts/
│   ├── base_prompt.txt
│   ├── generic_writing_prompt.txt
│   └── citation_grounding_workflow.md
├── runs/
│   ├── clean_search/
│   ├── noisy_search/
│   └── misleading_search/
├── annotations/
│   ├── rubric.xlsx
│   ├── citation_labels.csv
│   └── adjudication_notes.md
├── analysis/
│   ├── scoring_summary.ipynb
│   ├── error_analysis.md
│   └── figures/
├── frontend/
│   ├── data/
│   └── src/
└── final_report/
    ├── report.md
    ├── slides.pptx
    └── assets/
```

## 2. 创建顺序

1. 先建 `docs/`，放项目总纲、实验协议、标注规则和报告提纲。
2. 再建 `papers/`，按 raw、匿名化输入、ground truth Related Work 分开保存。
3. 再建 `prompts/`，固定三类实验提示，避免运行时临时改 prompt。
4. 再建 `runs/`，按 Clean、Noisy、Misleading 三类条件保存 OpenClaw 输出和检索日志。
5. 再建 `annotations/`，保存评分表、citation 标签和复核记录。
6. 再建 `analysis/`，保存统计脚本、错误分析和图表。
7. 最后建 `frontend/` 和 `final_report/`，用于展示页、最终报告和答辩材料。

## 3. PowerShell 创建命令

```powershell
New-Item -ItemType Directory -Force -Path "docs"
New-Item -ItemType Directory -Force -Path "papers\raw"
New-Item -ItemType Directory -Force -Path "papers\anonymized_inputs"
New-Item -ItemType Directory -Force -Path "papers\ground_truth_related_work"
New-Item -ItemType Directory -Force -Path "prompts"
New-Item -ItemType Directory -Force -Path "runs\clean_search"
New-Item -ItemType Directory -Force -Path "runs\noisy_search"
New-Item -ItemType Directory -Force -Path "runs\misleading_search"
New-Item -ItemType Directory -Force -Path "annotations"
New-Item -ItemType Directory -Force -Path "analysis\figures"
New-Item -ItemType Directory -Force -Path "frontend\data"
New-Item -ItemType Directory -Force -Path "frontend\src"
New-Item -ItemType Directory -Force -Path "final_report\assets"
```

## 4. 各目录职责

| 目录 | 放什么 | 负责人建议 |
|---|---|---|
| `docs/` | 总纲、实验协议、标注规则、报告提纲 | 全组共同维护 |
| `papers/raw/` | 原始论文 PDF 或文本 | 成员 A |
| `papers/anonymized_inputs/` | 删除敏感线索后的模型输入 | 成员 A |
| `papers/ground_truth_related_work/` | 原论文 Related Work 片段 | 成员 A |
| `prompts/` | base prompt、generic prompt、workflow | 成员 B |
| `runs/` | 每次 OpenClaw 输出、query、候选论文、最终引用 | 成员 B |
| `annotations/` | 打分表、citation 标签、复核记录 | 成员 C |
| `analysis/` | 统计、图表、错误案例分析 | 成员 C |
| `frontend/` | 可视化展示页和展示数据 | 成员 D |
| `final_report/` | 最终报告、PPT、图片素材 | 成员 D |
