from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


METRICS = [
    "content_coverage",
    "citation_quality",
    "relevance",
    "thematic_structure",
    "synthesis_quality",
    "writing_quality",
    "length_conciseness",
    "citation_validity",
    "citation_appropriateness",
    "citation_coverage",
    "citation_placement",
    "citation_topic_consistency",
]

KEY_METRICS = [
    "overall",
    "content_coverage",
    "citation_quality",
    "relevance",
    "synthesis_quality",
    "citation_coverage",
]

TASK_ORDER = ["PaperA", "PaperB", "PaperC", "PaperD", "PaperE"]
TASK_LABELS = {
    "07794": "PaperA",
    "11662": "PaperB",
    "12299": "PaperC",
    "researcher": "PaperD",
    "source": "PaperE",
    "PaperA": "PaperA",
    "PaperB": "PaperB",
    "PaperC": "PaperC",
    "PaperD": "PaperD",
    "PaperE": "PaperE",
}
LEGACY_TASK_TO_LABEL = {
    "07794": "PaperA",
    "11662": "PaperB",
    "12299": "PaperC",
    "researcher": "PaperD",
    "source": "PaperE",
}
MEMORY_ORDER = ["no", "low", "high"]

MAIN_METHOD_ORDER = [
    "Claude Code + DS-v4-Pro",
    "OpenClaw + Kimi-K2.6",
    "OpenClaw + DS-v4-Pro",
    "OpenClaw + DS-v4-Pro + Skill",
    "OpenClaw + DS-v4-Pro + Low Memory",
    "OpenClaw + DS-v4-Pro + High Memory",
]

FIG_LABELS = {
    "Claude Code + DS-v4-Pro": "CC+DS",
    "OpenClaw + Kimi-K2.6": "OC+Kimi",
    "OpenClaw + DS-v4-Pro": "OC+DS",
    "OpenClaw + DS-v4-Pro + Skill": "OC+DS+Skill",
    "OpenClaw + DS-v4-Pro + Low Memory": "OC+DS+LowMem",
    "OpenClaw + DS-v4-Pro + High Memory": "OC+DS+HighMem",
}

DISPLAY_MEAN_OVERRIDES: dict[str, float] = {}

PALETTE = {
    "Claude Code + DS-v4-Pro": "#4C78A8",
    "OpenClaw + Kimi-K2.6": "#F58518",
    "OpenClaw + DS-v4-Pro": "#54A24B",
    "OpenClaw + DS-v4-Pro + Skill": "#B279A2",
    "OpenClaw + DS-v4-Pro + Low Memory": "#72B7B2",
    "OpenClaw + DS-v4-Pro + High Memory": "#E45756",
}


def parse_row_identity(rel_dir: Path) -> tuple[str, str, str, str, str, str]:
    parts = rel_dir.parts
    system = parts[0]
    condition = parts[1]
    leaf = parts[-1]
    memory_level = ""
    task = leaf

    if system.startswith("claude_code"):
        method_raw = "Claude Code + DS-v4-Pro"
        task = leaf
    elif system.startswith("kimi"):
        method_raw = "OpenClaw + Kimi-K2.6"
        task = leaf
    elif condition == "sim_prompt":
        method_raw = "OpenClaw + DS-v4-Pro (legacy sim_prompt)"
        task = leaf.removeprefix("sim_prompt_")
    elif condition == "sim_prompt+skill":
        method_raw = "OpenClaw + DS-v4-Pro + Skill"
        task = leaf.removeprefix("sim_prompt_skill_")
    elif condition == "sim_prompt+memory":
        method_raw = "OpenClaw + DS-v4-Pro + Memory"
        if len(parts) < 4:
            raise ValueError(f"Unexpected memory result path: {rel_dir}")
        task = parts[2]
        if "high_memory" in leaf:
            memory_level = "high"
        elif "low_memory" in leaf:
            memory_level = "low"
        elif "no_memory" in leaf:
            memory_level = "no"
        else:
            raise ValueError(f"Cannot parse memory level from: {rel_dir}")
    else:
        method_raw = f"{system} / {condition}"

    task = TASK_LABELS.get(task, task)
    return system, condition, leaf, task, memory_level, method_raw


def load_rows(root: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for report_json in sorted(root.rglob("report.json")):
        rel_dir = report_json.parent.relative_to(root)
        if len(rel_dir.parts) < 3:
            continue
        data = json.loads(report_json.read_text(encoding="utf-8"))
        system, condition, leaf, task, memory_level, method_raw = parse_row_identity(rel_dir)
        row: dict[str, object] = {
            "system": system,
            "condition": condition,
            "method_raw": method_raw,
            "task": task,
            "paper_label": TASK_LABELS.get(task, task),
            "memory_level": memory_level,
            "leaf": leaf,
            "sample_id": data.get("sample_id", ""),
            "overall": float(data["overall"]),
            "path": str(rel_dir),
        }
        for metric in METRICS:
            row[metric] = float(data["scores"][metric])
        rows.append(row)
    return rows


def build_main_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    main_rows: list[dict[str, object]] = []
    for row in rows:
        raw = str(row["method_raw"])
        level = str(row["memory_level"])
        if raw in {
            "Claude Code + DS-v4-Pro",
            "OpenClaw + Kimi-K2.6",
            "OpenClaw + DS-v4-Pro + Skill",
        }:
            out = dict(row)
            out["method"] = raw
            out["comparison_source"] = "direct"
            main_rows.append(out)
        elif raw == "OpenClaw + DS-v4-Pro + Memory" and level in {"no", "low", "high"}:
            out = dict(row)
            if level == "no":
                out["method"] = "OpenClaw + DS-v4-Pro"
            elif level == "low":
                out["method"] = "OpenClaw + DS-v4-Pro + Low Memory"
            else:
                out["method"] = "OpenClaw + DS-v4-Pro + High Memory"
            out["comparison_source"] = f"{level}_memory"
            main_rows.append(out)
    return main_rows


def check_reports(root: Path) -> tuple[int, int, list[str]]:
    md_dirs = {p.parent for p in root.rglob("report.md")}
    json_dirs = {p.parent for p in root.rglob("report.json")}
    missing_json = sorted(str(p.relative_to(root)) for p in md_dirs - json_dirs)
    return len(md_dirs), len(json_dirs), missing_json


def mean(values: list[float]) -> float:
    return statistics.fmean(values) if values else math.nan


def population_sd(values: list[float]) -> float:
    if len(values) <= 1:
        return 0.0
    avg = mean(values)
    return math.sqrt(sum((v - avg) ** 2 for v in values) / len(values))


def fmt_score(value: float | None) -> str:
    return "--" if value is None or math.isnan(value) else f"{value:.2f}"


def display_mean(method: str, values: list[float]) -> float:
    return DISPLAY_MEAN_OVERRIDES.get(method, mean(values))


def present_values(values: list[float | None]) -> list[float]:
    return [float(v) for v in values if v is not None and not math.isnan(float(v))]


def tex_escape(value: object) -> str:
    text = str(value)
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def write_csvs(
    raw_rows: list[dict[str, object]],
    main_rows: list[dict[str, object]],
    out_dir: Path,
) -> list[dict[str, object]]:
    raw_fields = [
        "system",
        "condition",
        "method_raw",
        "task",
        "paper_label",
        "memory_level",
        "leaf",
        "sample_id",
        "overall",
        *METRICS,
        "path",
    ]
    with (out_dir / "clean_search_scores_full.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=raw_fields)
        writer.writeheader()
        writer.writerows(raw_rows)

    summary_rows: list[dict[str, object]] = []
    for method in MAIN_METHOD_ORDER:
        group = [r for r in main_rows if r["method"] == method]
        item: dict[str, object] = {
            "method": method,
            "figure_label": FIG_LABELS[method],
            "n": len(group),
        }
        for metric in ["overall", *METRICS]:
            values = [float(r[metric]) for r in group]
            metric_mean = display_mean(method, values) if metric == "overall" else mean(values)
            item[f"{metric}_mean"] = round(metric_mean, 4)
            item[f"{metric}_sd"] = round(population_sd(values), 4)
        summary_rows.append(item)

    fields = ["method", "figure_label", "n"]
    for metric in ["overall", *METRICS]:
        fields.extend([f"{metric}_mean", f"{metric}_sd"])
    with (out_dir / "clean_search_group_summary.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(summary_rows)
    return summary_rows


def pivot_overall(main_rows: list[dict[str, object]]) -> dict[tuple[str, str], float]:
    return {
        (str(r["method"]), str(r["task"])): float(r["overall"])
        for r in main_rows
    }


def standalone_tex_document(title: str, body_lines: list[str], landscape: bool = False) -> list[str]:
    geometry = "margin=0.7in"
    if landscape:
        geometry += ",landscape"
    return [
        r"\documentclass[10pt]{article}",
        rf"\usepackage[{geometry}]{{geometry}}",
        r"\usepackage{booktabs}",
        r"\usepackage{array}",
        r"\usepackage{caption}",
        r"\usepackage[T1]{fontenc}",
        r"\usepackage{lmodern}",
        r"\usepackage{microtype}",
        r"\begin{document}",
        rf"\section*{{{title}}}",
        *body_lines,
        r"\end{document}",
        "",
    ]


def write_overall_task_tex(main_rows: list[dict[str, object]], out_dir: Path) -> None:
    pivot = pivot_overall(main_rows)
    best_by_task = {
        task: max(pivot[(method, task)] for method in MAIN_METHOD_ORDER if (method, task) in pivot)
        for task in TASK_ORDER
    }
    table = [
        r"\begin{table}[t]",
        r"\centering",
        r"\caption{Overall scores on each clean\_search evaluation sample. Best scores in each task column are bolded.}",
        r"\label{tab:clean-search-overall-by-task}",
        r"\small",
        r"\begin{tabular}{lrrrrrrr}",
        r"\toprule",
        "Method & PaperA & PaperB & PaperC & PaperD & PaperE & Mean & Std \\\\",
        r"\midrule",
    ]
    for method in MAIN_METHOD_ORDER:
        vals = []
        cells = []
        for task in TASK_ORDER:
            value = pivot.get((method, task))
            if value is None:
                cells.append("--")
                continue
            vals.append(value)
            cell = fmt_score(value)
            if abs(value - best_by_task[task]) < 1e-9:
                cell = rf"\textbf{{{cell}}}"
            cells.append(cell)
        table.append(
            f"{tex_escape(method)} & "
            + " & ".join(cells)
            + f" & {display_mean(method, vals):.2f} & {population_sd(vals):.2f} \\\\"
        )
    table.extend([r"\bottomrule", r"\end{tabular}", r"\end{table}", ""])
    lines = standalone_tex_document("clean\\_search Overall Scores by Task", table)
    (out_dir / "clean_search_overall_by_task.tex").write_text("\n".join(lines), encoding="utf-8")


def write_metrics_tex(raw_rows: list[dict[str, object]], main_rows: list[dict[str, object]], out_dir: Path) -> None:
    compact_metrics = [
        "overall",
        "content_coverage",
        "citation_quality",
        "relevance",
        "synthesis_quality",
        "citation_coverage",
    ]
    headers = ["Method", "Task", "Memory", "Overall", "Content", "Citation Q.", "Relevance", "Synthesis", "Citation Cov."]
    table = [
        r"\begin{table*}[t]",
        r"\centering",
        r"\caption{Detailed clean\_search scores. Main-comparison rows use no-memory results for OpenClaw + DS-v4-Pro.}",
        r"\label{tab:clean-search-full-metrics}",
        r"\scriptsize",
        r"\begin{tabular}{lllrrrrrr}",
        r"\toprule",
        " & ".join(headers) + r" \\",
        r"\midrule",
    ]
    main_keys = {(str(r["path"]), str(r["method"])) for r in main_rows}
    rows = []
    for row in raw_rows:
        matching = [m for path, m in main_keys if path == str(row["path"])]
        display = matching[0] if matching else str(row["method_raw"])
        item = dict(row)
        item["display_method"] = display
        rows.append(item)
    rows.sort(
        key=lambda r: (
            MAIN_METHOD_ORDER.index(str(r["display_method"])) if r["display_method"] in MAIN_METHOD_ORDER else 99,
            TASK_ORDER.index(str(r["task"])) if r["task"] in TASK_ORDER else 99,
            MEMORY_ORDER.index(str(r["memory_level"])) if r["memory_level"] in MEMORY_ORDER else 99,
            str(r["path"]),
        )
    )
    for row in rows:
        cells = [
            tex_escape(row["display_method"]),
            tex_escape(row["paper_label"]),
            tex_escape(row["memory_level"] or "--"),
            *[fmt_score(float(row[m])) for m in compact_metrics],
        ]
        table.append(" & ".join(cells) + r" \\")
    table.extend([r"\bottomrule", r"\end{tabular}", r"\end{table*}", ""])
    lines = standalone_tex_document("Detailed clean\\_search Scores", table, landscape=True)
    (out_dir / "clean_search_metrics_full.tex").write_text("\n".join(lines), encoding="utf-8")


def setup_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 8,
            "axes.titlesize": 9,
            "axes.labelsize": 8,
            "xtick.labelsize": 7,
            "ytick.labelsize": 7,
            "legend.fontsize": 7,
            "figure.dpi": 120,
            "savefig.dpi": 300,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.alpha": 0.25,
            "grid.linewidth": 0.6,
            "axes.axisbelow": True,
        }
    )


def save_figure(fig: plt.Figure, out_dir: Path, stem: str) -> None:
    fig.savefig(out_dir / f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(out_dir / f"{stem}.png", bbox_inches="tight", dpi=300)
    plt.close(fig)


def plot_overall_by_task(main_rows: list[dict[str, object]], out_dir: Path) -> None:
    pivot = pivot_overall(main_rows)
    x = np.arange(len(TASK_ORDER))
    width = 0.12
    fig, ax = plt.subplots(figsize=(8.2, 3.5))
    offsets = (np.arange(len(MAIN_METHOD_ORDER)) - (len(MAIN_METHOD_ORDER) - 1) / 2) * width
    for i, method in enumerate(MAIN_METHOD_ORDER):
        values = [pivot.get((method, task), np.nan) for task in TASK_ORDER]
        ax.bar(
            x + offsets[i],
            values,
            width=width,
            label=FIG_LABELS[method],
            color=PALETTE[method],
            edgecolor="black",
            linewidth=0.35,
        )
    ax.set_ylabel("Overall score")
    ax.set_ylim(0, 10)
    ax.set_xticks(x)
    ax.set_xticklabels([TASK_LABELS[t] for t in TASK_ORDER])
    ax.set_title("Per-sample Overall Scores")
    ax.legend(ncol=3, frameon=False, loc="upper center", bbox_to_anchor=(0.5, 1.27))
    save_figure(fig, out_dir, "clean_search_overall_by_task")


def plot_group_summary(summary_rows: list[dict[str, object]], out_dir: Path) -> None:
    labels = [str(r["figure_label"]) for r in summary_rows]
    methods = [str(r["method"]) for r in summary_rows]
    means = [float(r["overall_mean"]) for r in summary_rows]
    sds = [float(r["overall_sd"]) for r in summary_rows]
    x = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(7.6, 3.4))
    ax.bar(
        x,
        means,
        yerr=sds,
        capsize=3,
        color=[PALETTE[m] for m in methods],
        edgecolor="black",
        linewidth=0.35,
    )
    ax.set_ylabel("Overall score")
    ax.set_ylim(0, 10)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=20, ha="right")
    ax.set_title("Method-level Overall Mean ± Std")
    save_figure(fig, out_dir, "clean_search_group_summary")


def plot_metric_heatmap(summary_rows: list[dict[str, object]], out_dir: Path) -> None:
    labels = [str(r["figure_label"]) for r in summary_rows]
    data = np.array([[float(r[f"{m}_mean"]) for m in KEY_METRICS] for r in summary_rows])
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    im = ax.imshow(data, vmin=0, vmax=10, cmap="YlGnBu", aspect="auto")
    ax.set_xticks(np.arange(len(KEY_METRICS)))
    ax.set_xticklabels([m.replace("_", "\n") for m in KEY_METRICS])
    ax.set_yticks(np.arange(len(labels)))
    ax.set_yticklabels(labels)
    ax.grid(False)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            color = "white" if data[i, j] >= 7.8 else "black"
            ax.text(j, i, f"{data[i, j]:.2f}", ha="center", va="center", color=color, fontsize=7)
    cbar = fig.colorbar(im, ax=ax, fraction=0.035, pad=0.02)
    cbar.set_label("Mean score")
    ax.set_title("Mean Scores Across Key Metrics")
    save_figure(fig, out_dir, "clean_search_metric_heatmap")


def plot_memory_ablation(raw_rows: list[dict[str, object]], out_dir: Path) -> None:
    memory_rows = [r for r in raw_rows if r["method_raw"] == "OpenClaw + DS-v4-Pro + Memory"]
    pivot = {
        (str(r["memory_level"]), str(r["task"])): float(r["overall"])
        for r in memory_rows
    }
    x = np.arange(len(TASK_ORDER))
    width = 0.22
    fig, ax = plt.subplots(figsize=(6.6, 3.4))
    colors = {"no": "#54A24B", "low": "#72B7B2", "high": "#E45756"}
    labels = {"no": "NoMem", "low": "LowMem", "high": "HighMem"}
    offsets = (np.arange(len(MEMORY_ORDER)) - 1) * width
    for i, level in enumerate(MEMORY_ORDER):
        values = [pivot.get((level, task), np.nan) for task in TASK_ORDER]
        ax.bar(
            x + offsets[i],
            values,
            width=width,
            label=labels[level],
            color=colors[level],
            edgecolor="black",
            linewidth=0.35,
        )
    ax.set_ylabel("Overall score")
    ax.set_ylim(0, 10)
    ax.set_xticks(x)
    ax.set_xticklabels([TASK_LABELS[t] for t in TASK_ORDER])
    ax.set_title("Memory Ablation Across Samples")
    ax.legend(ncol=3, frameon=False, loc="upper center", bbox_to_anchor=(0.5, 1.2))
    save_figure(fig, out_dir, "clean_search_memory_ablation")


def wrap_method_for_table(method: str) -> str:
    return {
        "Claude Code + DS-v4-Pro": "Claude Code\n+ DS-v4-Pro",
        "OpenClaw + Kimi-K2.6": "OpenClaw\n+ Kimi-K2.6",
        "OpenClaw + DS-v4-Pro": "OpenClaw\n+ DS-v4-Pro",
        "OpenClaw + DS-v4-Pro + Skill": "OpenClaw\n+ DS-v4-Pro+Skill",
        "OpenClaw + DS-v4-Pro + Low Memory": "OpenClaw\n+ DS-v4-Pro\n+ Low Memory",
        "OpenClaw + DS-v4-Pro + High Memory": "OpenClaw\n+ DS-v4-Pro\n+ High Memory",
        "OpenClaw + DS-v4-Pro + Memory": "OpenClaw\n+ DS-v4-Pro\n+ Memory",
        "OpenClaw + DS-v4-Pro (legacy sim_prompt)": "OpenClaw legacy\nsim_prompt",
    }.get(method, method)


def save_table_figure(
    data: list[list[str]],
    columns: list[str],
    out_dir: Path,
    stem: str,
    title: str,
    figsize: tuple[float, float],
    font_size: int,
    col_widths: list[float] | None = None,
    y_scale: float = 1.25,
) -> None:
    fig, ax = plt.subplots(figsize=figsize)
    ax.axis("off")
    ax.set_title(title, fontsize=10, pad=8)
    table = ax.table(cellText=data, colLabels=columns, loc="center", cellLoc="center", colWidths=col_widths)
    table.auto_set_font_size(False)
    table.set_fontsize(font_size)
    table.scale(1.0, y_scale)
    for (row, _col), cell in table.get_celld().items():
        cell.set_linewidth(0.35)
        if row == 0:
            cell.set_facecolor("#EAEAEA")
            cell.set_text_props(weight="bold")
        else:
            cell.set_facecolor("#FFFFFF")
    save_figure(fig, out_dir, stem)


def plot_overall_table(main_rows: list[dict[str, object]], out_dir: Path) -> None:
    pivot = pivot_overall(main_rows)
    data = []
    for method in MAIN_METHOD_ORDER:
        values = [pivot.get((method, task)) for task in TASK_ORDER]
        vals = present_values(values)
        data.append(
            [
                wrap_method_for_table(method),
                *[fmt_score(pivot.get((method, task))) for task in TASK_ORDER],
                f"{display_mean(method, vals):.2f}",
                f"{population_sd(vals):.2f}",
            ]
        )
    save_table_figure(
        data,
        ["Method", *[TASK_LABELS[t] for t in TASK_ORDER], "Mean", "Std"],
        out_dir,
        "clean_search_overall_by_task_table",
        "Overall Scores by Task",
        (9.4, 4.6),
        font_size=6,
        col_widths=[0.24, 0.1, 0.1, 0.1, 0.12, 0.1, 0.1, 0.1],
        y_scale=1.7,
    )


def plot_metrics_table(raw_rows: list[dict[str, object]], main_rows: list[dict[str, object]], out_dir: Path) -> None:
    compact_metrics = [
        "overall",
        "content_coverage",
        "citation_quality",
        "relevance",
        "synthesis_quality",
        "citation_coverage",
    ]
    main_by_path = {str(r["path"]): str(r["method"]) for r in main_rows}
    rows = []
    for row in raw_rows:
        item = dict(row)
        item["display_method"] = main_by_path.get(str(row["path"]), str(row["method_raw"]))
        rows.append(item)
    rows.sort(
        key=lambda r: (
            MAIN_METHOD_ORDER.index(str(r["display_method"])) if r["display_method"] in MAIN_METHOD_ORDER else 99,
            TASK_ORDER.index(str(r["task"])) if r["task"] in TASK_ORDER else 99,
            MEMORY_ORDER.index(str(r["memory_level"])) if r["memory_level"] in MEMORY_ORDER else 99,
            str(r["path"]),
        )
    )
    data = [
        [
            wrap_method_for_table(str(r["display_method"])),
            str(r["paper_label"]),
            str(r["memory_level"] or "--"),
            *[fmt_score(float(r[m])) for m in compact_metrics],
        ]
        for r in rows
    ]
    save_table_figure(
        data,
        ["Method", "Task", "Memory", "Overall", "Content", "Citation Q.", "Relevance", "Synthesis", "Citation Cov."],
        out_dir,
        "clean_search_metrics_full_table",
        "Detailed clean_search Scores",
        (13.0, 13.0),
        font_size=4.5,
        col_widths=[0.25, 0.08, 0.07, 0.075, 0.075, 0.085, 0.075, 0.075, 0.085],
        y_scale=1.25,
    )


def markdown_main_table(main_rows: list[dict[str, object]]) -> str:
    pivot = pivot_overall(main_rows)
    lines = [
        "| 方法 | PaperA | PaperB | PaperC | PaperD | PaperE | Mean | Std |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for method in MAIN_METHOD_ORDER:
        values = [pivot.get((method, task)) for task in TASK_ORDER]
        vals = present_values(values)
        cells = [fmt_score(pivot.get((method, task))) for task in TASK_ORDER]
        lines.append(
            f"| {method} | "
            + " | ".join(cells)
            + f" | {display_mean(method, vals):.2f} | {population_sd(vals):.2f} |"
        )
    return "\n".join(lines)


def markdown_group_summary(summary_rows: list[dict[str, object]]) -> str:
    lines = [
        "| 方法/条件 | 图中缩写 | n | Overall mean | Overall std | Content coverage mean | Citation quality mean | Citation coverage mean |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for r in summary_rows:
        lines.append(
            f"| {r['method']} | {r['figure_label']} | {r['n']} | "
            f"{float(r['overall_mean']):.2f} | {float(r['overall_sd']):.2f} | "
            f"{float(r['content_coverage_mean']):.2f} | {float(r['citation_quality_mean']):.2f} | "
            f"{float(r['citation_coverage_mean']):.2f} |"
        )
    return "\n".join(lines)


def markdown_memory_table(raw_rows: list[dict[str, object]]) -> str:
    memory_rows = [r for r in raw_rows if r["method_raw"] == "OpenClaw + DS-v4-Pro + Memory"]
    pivot = {(str(r["memory_level"]), str(r["task"])): float(r["overall"]) for r in memory_rows}
    lines = [
        "| Memory | PaperA | PaperB | PaperC | PaperD | PaperE | Mean | Std |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for level in MEMORY_ORDER:
        values = [pivot.get((level, task)) for task in TASK_ORDER]
        vals = present_values(values)
        lines.append(
            f"| {level} | "
            + " | ".join(fmt_score(pivot.get((level, task))) for task in TASK_ORDER)
            + f" | {mean(vals):.2f} | {population_sd(vals):.2f} |"
        )
    return "\n".join(lines)


def write_summary_md(
    raw_rows: list[dict[str, object]],
    main_rows: list[dict[str, object]],
    summary_rows: list[dict[str, object]],
    out_dir: Path,
    md_count: int,
    json_count: int,
) -> None:
    best = max(summary_rows, key=lambda r: float(r["overall_mean"]))
    stable = min(summary_rows, key=lambda r: float(r["overall_sd"]))
    text = f"""# clean_search 评测分数汇总与图表说明

## 数据来源

本次重新读取 `D:\\college\\llm\\final_proj\\runs\\clean_search` 下所有最后一级评测文件夹，共检查到 `{md_count}` 个 `report.md` 和 `{json_count}` 个 `report.json`，二者一一对应。分数提取以 `report.json` 为准。

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

`OpenClaw + DS-v4-Pro` 与 `OpenClaw + DS-v4-Pro + No Memory` 是同一配置。最终主比较中只使用 no-memory 的五篇结果，并将其显示为 `OpenClaw + DS-v4-Pro`。旧的 `openclaw+ds-v4-pro\\sim_prompt` 五行仍保留在 `clean_search_scores_full.csv` 中用于追溯，但不进入主图、主表、heatmap 或 group summary。

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

{markdown_main_table(main_rows)}

## 方法总体汇总

{markdown_group_summary(summary_rows)}

## Memory 消融

{markdown_memory_table(raw_rows)}

## 主要观察

- 主比较中，`{best['method']}` 的 Overall mean 最高，为 `{float(best['overall_mean']):.2f}`。
- `{stable['method']}` 的 Overall std 最小，为 `{float(stable['overall_sd']):.2f}`，说明跨五篇论文波动最小。
- Memory 消融现在覆盖五篇论文，因此可以进入主比较；但 no/low/high memory 应分开展示，不能合并成一个 `Memory` 条件。
- 逐 task 表格仍然比单一均值更重要，因为不同配置在不同论文样本上的优势并不完全一致。

## 使用建议

论文主文建议放 `clean_search_overall_by_task.tex` 或 `clean_search_overall_by_task_table.pdf`，再配合 `clean_search_overall_by_task.pdf`。附录建议放 `clean_search_metrics_full.tex`、`clean_search_metric_heatmap.pdf` 和 `clean_search_memory_ablation.pdf`。如果本机没有 LaTeX，直接使用 `*_table.pdf/png` 即可。
"""
    (out_dir / "clean_search_summary_report.md").write_text(text, encoding="utf-8")


def validate_outputs(
    root: Path,
    out_dir: Path,
    raw_rows: list[dict[str, object]],
    main_rows: list[dict[str, object]],
    summary_rows: list[dict[str, object]],
    md_count: int,
    json_count: int,
) -> None:
    if md_count != json_count:
        raise RuntimeError(f"report.md and report.json counts differ: {md_count} and {json_count}.")
    if len(raw_rows) != json_count:
        raise RuntimeError(f"Expected raw rows to match report.json count {json_count}, got {len(raw_rows)}.")
    if len(summary_rows) != 6:
        raise RuntimeError(f"Expected 6 main summary groups, got {len(summary_rows)}.")

    for row in raw_rows:
        for metric in ["overall", *METRICS]:
            value = float(row[metric])
            if not 0 <= value <= 10:
                raise RuntimeError(f"Score out of range for {row['path']} {metric}: {value}")

    for task in TASK_ORDER:
        levels = {
            str(r["memory_level"])
            for r in raw_rows
            if r["method_raw"] == "OpenClaw + DS-v4-Pro + Memory" and r["task"] == task
        }
        if not levels.issubset({"no", "low", "high"}):
            raise RuntimeError(f"Unexpected memory levels for task {task}: {levels}.")
        if not levels:
            raise RuntimeError(f"No memory rows found for task {task}.")

    no_memory_paths = {
        str(r["path"])
        for r in raw_rows
        if r["method_raw"] == "OpenClaw + DS-v4-Pro + Memory" and r["memory_level"] == "no"
    }
    openclaw_main_paths = {
        str(r["path"])
        for r in main_rows
        if r["method"] == "OpenClaw + DS-v4-Pro"
    }
    if openclaw_main_paths != no_memory_paths:
        raise RuntimeError("OpenClaw + DS-v4-Pro main rows are not exactly the no-memory rows.")

    required = [
        "clean_search_scores_full.csv",
        "clean_search_group_summary.csv",
        "clean_search_overall_by_task.tex",
        "clean_search_metrics_full.tex",
        "clean_search_overall_by_task_table.pdf",
        "clean_search_overall_by_task_table.png",
        "clean_search_metrics_full_table.pdf",
        "clean_search_metrics_full_table.png",
        "clean_search_overall_by_task.pdf",
        "clean_search_overall_by_task.png",
        "clean_search_group_summary.pdf",
        "clean_search_group_summary.png",
        "clean_search_metric_heatmap.pdf",
        "clean_search_metric_heatmap.png",
        "clean_search_memory_ablation.pdf",
        "clean_search_memory_ablation.png",
        "clean_search_summary_report.md",
    ]
    missing = [name for name in required if not (out_dir / name).exists()]
    if missing:
        raise RuntimeError(f"Missing required outputs: {missing}")

    tex = (out_dir / "clean_search_overall_by_task.tex").read_text(encoding="utf-8")
    if r"\textbf{" not in tex:
        raise RuntimeError("Best-score bold markers were not written to the main LaTeX table.")
    md = (out_dir / "clean_search_summary_report.md").read_text(encoding="utf-8")
    for label in ["CC+DS", "OC+Kimi", "OC+DS", "OC+DS+Skill", "OC+DS+LowMem", "OC+DS+HighMem"]:
        if label not in md:
            raise RuntimeError(f"Missing label mapping in Markdown: {label}")
    for old_label in ["Claude |", "OC+Skill", "OC+LowMem", "OC+HighMem"]:
        if old_label in md:
            raise RuntimeError(f"Unexpected old or ambiguous label in Markdown: {old_label}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("runs/clean_search"))
    parser.add_argument("--out", type=Path, default=Path("runs/clean_search/summary"))
    args = parser.parse_args()

    root = args.root.resolve()
    out_dir = args.out.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    raw_rows = load_rows(root)
    main_rows = build_main_rows(raw_rows)
    md_count, json_count, missing_json = check_reports(root)
    if missing_json:
        raise RuntimeError(f"report.md directories without report.json: {missing_json}")

    summary_rows = write_csvs(raw_rows, main_rows, out_dir)
    write_overall_task_tex(main_rows, out_dir)
    write_metrics_tex(raw_rows, main_rows, out_dir)
    setup_style()
    plot_overall_by_task(main_rows, out_dir)
    plot_group_summary(summary_rows, out_dir)
    plot_metric_heatmap(summary_rows, out_dir)
    plot_memory_ablation(raw_rows, out_dir)
    plot_overall_table(main_rows, out_dir)
    plot_metrics_table(raw_rows, main_rows, out_dir)
    write_summary_md(raw_rows, main_rows, summary_rows, out_dir, md_count, json_count)
    validate_outputs(root, out_dir, raw_rows, main_rows, summary_rows, md_count, json_count)

    print(f"Extracted raw rows: {len(raw_rows)}")
    print(f"Main comparison rows: {len(main_rows)}")
    print(f"Main summary groups: {len(summary_rows)}")
    print(f"report.md count: {md_count}")
    print(f"report.json count: {json_count}")
    print(f"Output directory: {out_dir}")


if __name__ == "__main__":
    main()
