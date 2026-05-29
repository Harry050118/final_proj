import argparse
import json
from datetime import date
from pathlib import Path
from statistics import mean


GROUPS = {
    "sim_prompt": "No Intervention / baseline",
    "sim_prompt+skill": "Skill-guided citation-grounding intervention",
}

METRICS = {
    "overall": ("overall", "Overall"),
    "citation_quality": ("scores.citation_quality", "Citation quality"),
    "relevance": ("scores.relevance", "Relevance"),
    "content_coverage": ("scores.content_coverage", "Coverage"),
}

DIAGNOSTIC_KEYS = (
    "missing_points",
    "hallucinated_references",
    "bad_citation_claim_pairs",
    "overclaim_citation_claim_pairs",
    "citation_group_support",
    "topic_structure_issues",
)

DETAILED_DIAGNOSTIC_KEYS = (
    "missing_points",
    "bad_citation_claim_pairs",
    "overclaim_citation_claim_pairs",
    "citation_group_support",
    "topic_structure_issues",
)


def _nested_get(data, dotted_key):
    current = data
    for part in dotted_key.split("."):
        current = current[part]
    return float(current)


def _round(value):
    return round(float(value), 2)


def _load_report(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    diagnostics = data.get("diagnostics", {})
    return {
        "sample_id": data.get("sample_id", ""),
        "metrics": {
            metric_key: _round(_nested_get(data, source_key))
            for metric_key, (source_key, _label) in METRICS.items()
        },
        "diagnostics": {
            key: len(diagnostics.get(key, []) or [])
            for key in DIAGNOSTIC_KEYS
        },
        "detailed_diagnostics": {
            key: diagnostics.get(key, []) or []
            for key in DETAILED_DIAGNOSTIC_KEYS
        },
    }


def _discover_reports(repo_root):
    runs_root = repo_root / "runs" / "clean_search"
    reports = {}
    for group in GROUPS:
        group_root = runs_root / group
        group_reports = {}
        for report_path in sorted(group_root.glob("*/report.json")):
            group_reports[report_path.parent.name] = _load_report(report_path)
        reports[group] = group_reports
    return reports


def _metric_delta(skill_metrics, baseline_metrics):
    return {
        key: _round(skill_metrics[key] - baseline_metrics[key])
        for key in METRICS
    }


def _diagnostic_delta(skill_diagnostics, baseline_diagnostics):
    return {
        key: skill_diagnostics[key] - baseline_diagnostics[key]
        for key in DIAGNOSTIC_KEYS
    }


def _observation(case_id, group_label, report):
    m = report["metrics"]
    d = report["diagnostics"]
    return (
        f"{group_label}：overall {m['overall']}，citation quality {m['citation_quality']}，"
        f"relevance {m['relevance']}，coverage {m['content_coverage']}；"
        f"missing points {d['missing_points']}，overclaim pairs {d['overclaim_citation_claim_pairs']}。"
    )


def _build_cases(reports):
    baseline_cases = set(reports["sim_prompt"])
    skill_cases = set(reports["sim_prompt+skill"])
    case_ids = sorted(baseline_cases & skill_cases)
    cases = []
    for case_id in case_ids:
        baseline = reports["sim_prompt"][case_id]
        skill = reports["sim_prompt+skill"][case_id]
        cases.append(
            {
                "case_id": case_id,
                "baseline": baseline,
                "skill": skill,
                "metric_delta_skill_minus_baseline": _metric_delta(
                    skill["metrics"], baseline["metrics"]
                ),
                "diagnostic_delta_skill_minus_baseline": _diagnostic_delta(
                    skill["diagnostics"], baseline["diagnostics"]
                ),
            }
        )
    return cases


def _aggregate_group(reports):
    return {
        "n": len(reports),
        "metrics": {
            metric_key: {
                "mean": _round(mean(report["metrics"][metric_key] for report in reports.values()))
            }
            for metric_key in METRICS
        },
        "diagnostics": {
            key: {
                "mean": _round(mean(report["diagnostics"][key] for report in reports.values()))
            }
            for key in DIAGNOSTIC_KEYS
        },
    }


def _build_aggregates(reports):
    aggregates = {
        group: _aggregate_group(group_reports)
        for group, group_reports in reports.items()
    }
    aggregates["skill_minus_baseline"] = {
        "metrics": {
            key: {
                "mean_delta": _round(
                    aggregates["sim_prompt+skill"]["metrics"][key]["mean"]
                    - aggregates["sim_prompt"]["metrics"][key]["mean"]
                )
            }
            for key in METRICS
        },
        "diagnostics": {
            key: {
                "mean_delta": _round(
                    aggregates["sim_prompt+skill"]["diagnostics"][key]["mean"]
                    - aggregates["sim_prompt"]["diagnostics"][key]["mean"]
                )
            }
            for key in DIAGNOSTIC_KEYS
        },
    }
    return aggregates


def _human_audit_placeholders(case_ids):
    return [
        {
            "case_id": case_id,
            "audit_status": "pending",
            "human_notes": "",
            "confirmed_issue": "",
            "frontend_highlight": False,
        }
        for case_id in case_ids
    ]


def _build_detailed_diagnostics(cases):
    return {
        case_item["case_id"]: {
            "baseline": case_item["baseline"]["detailed_diagnostics"],
            "skill": case_item["skill"]["detailed_diagnostics"],
        }
        for case_item in cases
    }


def _build_payload(repo_root):
    reports = _discover_reports(repo_root)
    cases = _build_cases(reports)
    return {
        "metadata": {
            "generated_on": date.today().isoformat(),
            "condition": "Clean Search",
            "source_root": "runs/clean_search",
            "groups": GROUPS,
            "limitations": [
                "Noisy Search / Misleading Search were not run, so robustness against irrelevant or misleading injected papers is not evaluated.",
                "RWEval reports are treated as the primary quantitative evidence; human audit placeholders are reserved for representative sanity checks.",
                "This artifact does not include PPT or frontend implementation.",
            ],
        },
        "aggregates": _build_aggregates(reports),
        "cases": cases,
        "detailed_diagnostics": _build_detailed_diagnostics(cases),
        "human_audit_placeholders": _human_audit_placeholders(
            [case_item["case_id"] for case_item in cases]
        ),
    }


def _format_metric_delta(delta):
    sign = "+" if delta >= 0 else ""
    return f"{sign}{delta:.2f}"


def _escape_markdown_cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def _diagnostic_summary_text(item):
    if not isinstance(item, dict):
        return _escape_markdown_cell(item)
    if "text" in item and "rationale" in item:
        return _escape_markdown_cell(f"{item['text']} 原因：{item['rationale']}")
    if "claim" in item and "rationale" in item:
        return _escape_markdown_cell(f"{item['claim']} 原因：{item['rationale']}")
    if "claim_id" in item:
        parts = [
            f"claim {item.get('claim_id')}",
            f"reference {item.get('reference_key')}",
        ]
        if item.get("support"):
            parts.append(f"support={item.get('support')}")
        rationale = item.get("overclaim_rationale") or item.get("rationale") or item.get("support_rationale")
        if rationale:
            parts.append(f"原因：{rationale}")
        return _escape_markdown_cell("；".join(parts))
    if "issue" in item:
        return _escape_markdown_cell(f"{item.get('paragraph_id', '')}：{item['issue']}")
    if "rationale" in item:
        return _escape_markdown_cell(item["rationale"])
    return _escape_markdown_cell(json.dumps(item, ensure_ascii=False))


def _render_diagnostic_items(items, limit=3):
    if not items:
        return "无"
    rendered = [_diagnostic_summary_text(item) for item in items[:limit]]
    if len(items) > limit:
        rendered.append(f"... 另有 {len(items) - limit} 条，完整诊断见 JSON")
    return "<br>".join(rendered)


def _render_auto_audit_section(cases):
    lines = [
        "",
        "## 自动审计诊断摘要",
        "",
        "RWEval 的自动诊断已经提供了较具体的审计证据，包括 missing points、bad citation-claim pairs、overclaim citation-claim pairs、citation group support 和 topic structure issues。Markdown 里每类最多展示 3 条；完整诊断见 JSON 的 `detailed_diagnostics` 字段。",
        "",
    ]
    diagnostic_specs = [
        ("missing_points", "missing points"),
        ("bad_citation_claim_pairs", "bad citation-claim pairs"),
        ("overclaim_citation_claim_pairs", "overclaim citation-claim pairs"),
        ("citation_group_support", "citation group support"),
        ("topic_structure_issues", "topic structure issues"),
    ]
    for case_item in cases:
        lines.extend(
            [
                f"### {case_item['case_id']}",
                "",
                "| Group | Diagnostic type | Count | 摘要 |",
                "|---|---|---:|---|",
            ]
        )
        for group_key, label in (("baseline", "Baseline"), ("skill", "Skill")):
            detailed = case_item[group_key]["detailed_diagnostics"]
            for diagnostic_key, diagnostic_label in diagnostic_specs:
                items = detailed.get(diagnostic_key, [])
                lines.append(
                    f"| {label} | {diagnostic_label} | {len(items)} | {_render_diagnostic_items(items)} |"
                )
        lines.append("")
    return lines


def _render_markdown(payload):
    aggregates = payload["aggregates"]
    cases = payload["cases"]
    lines = [
        "# Clean Search 结果汇总",
        "",
        "## 实验设置",
        "",
        "本分析只覆盖当前已经完成的 Clean Search 实验。`sim_prompt` 解释为 No Intervention / baseline，`sim_prompt+skill` 解释为 skill-guided citation-grounding intervention。",
        "",
        "本次没有运行 Noisy Search / Misleading Search，因此不能据此声称系统已经验证了对无关论文或误导论文注入的抗干扰能力。",
        "",
        "RWEval report 是本阶段的主要量化证据。下方人工审计区域会保留为空白，用于你后续做代表性 case 的 sanity check，再决定哪些内容进入前端展示。",
        "",
        "## 总体结果",
        "",
        "| Group | N | Overall | Citation quality | Relevance | Coverage |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for group, label in GROUPS.items():
        metrics = aggregates[group]["metrics"]
        lines.append(
            f"| {label} (`{group}`) | {aggregates[group]['n']} | "
            f"{metrics['overall']['mean']:.2f} | "
            f"{metrics['citation_quality']['mean']:.2f} | "
            f"{metrics['relevance']['mean']:.2f} | "
            f"{metrics['content_coverage']['mean']:.2f} |"
        )
    delta = aggregates["skill_minus_baseline"]["metrics"]
    lines.extend(
        [
            f"| Skill - baseline | - | {_format_metric_delta(delta['overall']['mean_delta'])} | {_format_metric_delta(delta['citation_quality']['mean_delta'])} | {_format_metric_delta(delta['relevance']['mean_delta'])} | {_format_metric_delta(delta['content_coverage']['mean_delta'])} |",
            "",
            "## 定量分析",
            "",
            f"在 5 个 Clean Search case 中，skill-guided 设置的平均 overall 从 {aggregates['sim_prompt']['metrics']['overall']['mean']:.2f} 提升到 {aggregates['sim_prompt+skill']['metrics']['overall']['mean']:.2f}。提升最明显的维度是 citation quality，从 {aggregates['sim_prompt']['metrics']['citation_quality']['mean']:.2f} 提升到 {aggregates['sim_prompt+skill']['metrics']['citation_quality']['mean']:.2f}。Relevance 也从 {aggregates['sim_prompt']['metrics']['relevance']['mean']:.2f} 提升到 {aggregates['sim_prompt+skill']['metrics']['relevance']['mean']:.2f}。Coverage 仍然是相对较弱的维度，虽然它也从 {aggregates['sim_prompt']['metrics']['content_coverage']['mean']:.2f} 提升到 {aggregates['sim_prompt+skill']['metrics']['content_coverage']['mean']:.2f}。",
            "",
            "因此，目前可以支持一个有边界的结论：在 Clean Search 条件下，skill-guided workflow 相比 baseline 改善了引用可靠性和主题相关性。但它不能证明系统在 noisy 或 misleading 检索条件下也同样稳健。",
            "",
            "## Case 级别对比",
            "",
            "| Case | Baseline overall | Skill overall | Overall delta | Citation quality delta | Relevance delta | Coverage delta |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for case_item in cases:
        baseline = case_item["baseline"]["metrics"]
        skill = case_item["skill"]["metrics"]
        deltas = case_item["metric_delta_skill_minus_baseline"]
        lines.append(
            f"| {case_item['case_id']} | {baseline['overall']:.2f} | {skill['overall']:.2f} | "
            f"{_format_metric_delta(deltas['overall'])} | "
            f"{_format_metric_delta(deltas['citation_quality'])} | "
            f"{_format_metric_delta(deltas['relevance'])} | "
            f"{_format_metric_delta(deltas['content_coverage'])} |"
        )
    lines.extend(
        [
            "",
            "## 诊断计数",
            "",
            "| Case | Baseline missing points | Skill missing points | Baseline bad pairs | Skill bad pairs | Baseline overclaims | Skill overclaims |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for case_item in cases:
        baseline = case_item["baseline"]["diagnostics"]
        skill = case_item["skill"]["diagnostics"]
        lines.append(
            f"| {case_item['case_id']} | {baseline['missing_points']} | {skill['missing_points']} | "
            f"{baseline['bad_citation_claim_pairs']} | {skill['bad_citation_claim_pairs']} | "
            f"{baseline['overclaim_citation_claim_pairs']} | {skill['overclaim_citation_claim_pairs']} |"
        )
    lines.extend(_render_auto_audit_section(cases))
    lines.extend(
        [
            "",
            "## 人工审计空白表",
            "",
            "上面的自动审计诊断已经提供主要审计证据。这里保留人工审计空白，不要求从零重新标注，只用于确认代表性 case 的自动诊断是否合理，以及是否适合进入前端展示。",
            "",
            "| Case | Baseline observation | Skill observation | Needs human check | Human audit notes | Frontend highlight? |",
            "|---|---|---|---|---|---|",
        ]
    )
    for case_item in cases:
        baseline_obs = _observation(case_item["case_id"], "Baseline", case_item["baseline"])
        skill_obs = _observation(case_item["case_id"], "Skill", case_item["skill"])
        lines.append(
            f"| {case_item['case_id']} | {baseline_obs} | {skill_obs} | pending |  | false |"
        )
    lines.extend(
        [
            "",
            "## 前端数据说明",
            "",
            "后续前端图表和 case card 建议直接读取 `analysis/clean_search_summary.json`。其中 `human_audit_placeholders` 已经初始化为 pending 状态，方便人工审计后标记代表性展示案例，而不需要改动原始 RWEval reports。",
            "",
        ]
    )
    return "\n".join(lines)


def build_outputs(repo_root, json_output, markdown_output):
    payload = _build_payload(repo_root)
    json_output.parent.mkdir(parents=True, exist_ok=True)
    markdown_output.parent.mkdir(parents=True, exist_ok=True)
    json_output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    markdown_output.write_text(_render_markdown(payload), encoding="utf-8")
    return payload


def main():
    parser = argparse.ArgumentParser(description="Build Clean Search summary artifacts.")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json-output", type=Path, default=Path(__file__).with_name("clean_search_summary.json"))
    parser.add_argument("--markdown-output", type=Path, default=Path(__file__).with_name("clean_search_summary.md"))
    args = parser.parse_args()
    payload = build_outputs(args.repo_root, args.json_output, args.markdown_output)
    print(
        "Wrote Clean Search summary: "
        f"{len(payload['cases'])} paired cases, "
        f"{payload['aggregates']['sim_prompt']['n']} baseline reports, "
        f"{payload['aggregates']['sim_prompt+skill']['n']} skill reports."
    )


if __name__ == "__main__":
    main()
