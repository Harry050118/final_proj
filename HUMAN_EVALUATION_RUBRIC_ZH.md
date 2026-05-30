# Related Work 人工评分指南

本文档用于人工复核 pipeline 生成的 related-work 评分报告。评分范围均为 0-10 分，分数越高表示质量越好。

本指南与 report 顶部的七个指标对齐：

- `content_coverage`
- `citation_quality`
- `relevance`
- `thematic_structure`
- `synthesis_quality`
- `writing_quality`
- `length_conciseness`

## 评分表

每个样本先填写这张表。`Pipeline Score` 来自自动报告，`Human Score` 是人工复核后的分数。

| 指标 | Human Score (0-10) | Pipeline Score | Difference | 主要依据 / 备注 |
| --- | ---: | ---: | ---: | --- |
| `content_coverage` |  |  |  | 是否覆盖 gold related work 的关键点。 |
| `citation_quality` |  |  |  | 引用是否真实、恰当、充分、位置合理，是否有 mis-citation / over-claim。 |
| `relevance` |  |  |  | 候选内容是否与目标论文和 gold 范围相关。 |
| `thematic_structure` |  |  |  | 主题组织、段落纯度、段落连贯性和顺序。 |
| `synthesis_quality` |  |  |  | 是否有综合、比较、趋势归纳和 gap framing。 |
| `writing_quality` |  |  |  | 语言清晰度、学术表达、术语一致性。 |
| `length_conciseness` |  |  |  | 长度是否合适、信息密度是否足够、是否冗余。 |

如果人工分数与 pipeline 分数相差超过 1 分，需要在备注中说明原因。

## 总体评分锚点

| 分数 | 含义 |
| --- | --- |
| 9-10 | 很强。覆盖充分、引用可靠、结构清晰、表达成熟。 |
| 7-8 | 较好。存在少量遗漏、弱引用或表达问题，但整体可用。 |
| 5-6 | 中等。存在明显缺陷，需要较大修改。 |
| 3-4 | 较差。关键内容缺失、引用问题较多或结构混乱。 |
| 0-2 | 基本不可用。严重偏题、引用不可信、内容大面积缺失或误导。 |

## 评审流程

1. 先读 candidate related work，不立即打分。
2. 再读 gold related work，列出核心主题、关键方法、benchmark、重要论文和研究 gap。
3. 检查 candidate 的每个 citation 是否能对应到 reference。
4. 对照 report 中的 diagnostics：`missing_points`、`bad_citation_claim_pairs`、`overclaim_citation_claim_pairs` 等。
5. 给七个指标分别打分。

## 1. `content_coverage`

衡量 candidate 是否覆盖 gold related work 中的重要内容。

| 分数 | 标准 |
| --- | --- |
| 9-10 | 几乎覆盖所有核心主题、关键方法、重要 benchmark 和重要文献。 |
| 7-8 | 覆盖大多数核心内容，但有少量遗漏或展开不足。 |
| 5-6 | 覆盖了大方向，但漏掉若干重要方法、数据集、比较或局限。 |
| 3-4 | 只覆盖很窄的一部分，遗漏中心主题。 |
| 0-2 | 与 gold related work 基本不相关或覆盖极少。 |

重点检查：

- `diagnostics.missing_points`
- `scores.content_coverage`
- `intermediate.alignment`

常见扣分：

- 漏掉核心研究方向。
- 漏掉关键 benchmark / dataset。
- 漏掉 gold 中重要的代表性论文。
- 没有覆盖 gold 中的 limitation / gap。
- 只讲背景，不讲与目标 work 最相关的内容。

建议标注标签：

- `missing_major_topic`
- `missing_key_reference`
- `missing_method_or_dataset`
- `missing_limitation_or_gap`
- `incorrect_topic_emphasis`

## 2. `citation_quality`

衡量引用整体质量。它是最重要的指标之一，包含 citation validity、mis-citation、over-claim、coverage、placement 等维度。

| 分数 | 标准 |
| --- | --- |
| 9-10 | 参考文献真实可识别；引用基本都直接支持对应 claim；无严重 over-claim；关键文献覆盖充分。 |
| 7-8 | 大多数引用可靠；少量引用偏宽泛或支持不够直接；少量关键文献缺失。 |
| 5-6 | 存在多处弱引用、引用位置不清、关键文献缺失或 over-claim。 |
| 3-4 | 大量 claim 缺乏 citation 支持，或 metadata 缺失严重，引用整体不可靠。 |
| 0-2 | 引用大面积错误、伪造、错配，或几乎不能支持正文。 |

建议人工加权：

| 子维度 | 权重 |
| --- | ---: |
| Citation validity | 25% |
| Appropriateness / mis-citation | 35% |
| Citation coverage | 20% |
| Citation placement | 10% |
| Topic consistency | 10% |

### 2.1 Citation Validity

看 reference 本身是否真实、可识别、metadata 是否匹配。

| 分数 | 标准 |
| --- | --- |
| 9-10 | 所有 reference 都能正确识别，metadata 与论文匹配。 |
| 7-8 | 少量 metadata 模糊，但大多数 reference 可确认。 |
| 5-6 | 有一些 unresolved 或弱匹配 reference。 |
| 3-4 | 多个 reference 无法解析或 metadata mismatch。 |
| 0-2 | 大量 reference 伪造、错配或不可识别。 |

检查字段：

- `diagnostics.hallucinated_references`
- `metric_details.citation_quality.validity`
- reference 的 `validity`
- reference 的 `issues`

错误标签：

- `unresolved_reference`
- `metadata_mismatch`
- `hallucinated_reference`
- `wrong_paper_same_title_or_author`
- `missing_reference_entry`

### 2.2 Mis-Citation

mis-citation 指引用的论文不能支持它附近的 claim。

| 分数 | 标准 |
| --- | --- |
| 9-10 | 几乎所有 citation 都直接支持对应 claim。 |
| 7-8 | 少量 citation 只提供间接支持，但大多数合理。 |
| 5-6 | 多个 citation 只弱相关，或只支持 claim 的一部分。 |
| 3-4 | 很多 citation 与 claim 不匹配。 |
| 0-2 | citation placement 和 claim-support 关系大面积错误。 |

检查字段：

- `diagnostics.bad_citation_claim_pairs`
- `metric_details.citation_quality.problematic_citation_claim_pairs`
- `intermediate.citation_judgment.citation_judgments`

支持等级：

- `yes`: citation 直接支持 claim。
- `partial`: citation 支持 claim 的一部分。
- `weak`: citation 主题相关，但不足以支撑 claim。
- `no`: citation 不支持 claim。
- `unknown`: metadata 或 evidence 不足，无法判断。

错误标签：

- `mis_citation_wrong_topic`
- `mis_citation_too_broad`
- `mis_citation_supports_different_claim`
- `mis_citation_only_background`
- `mis_citation_no_evidence`
- `citation_metadata_missing`

### 2.3 Over-Claim

over-claim 指 candidate 的说法比 citation 实际支持的内容更强、更具体或更因果。

| 分数 | 标准 |
| --- | --- |
| 9-10 | claim 表述谨慎，强度与 citation evidence 匹配。 |
| 7-8 | 有轻微夸大，但不影响中心结论。 |
| 5-6 | 多个 claim 夸大结果、泛化范围或因果关系。 |
| 3-4 | 重要 claim 经常超出 citation 支持范围。 |
| 0-2 | 系统性地把弱证据写成强结论。 |

检查字段：

- `diagnostics.overclaim_citation_claim_pairs`
- `overclaim_rationale`
- `diagnostics.citation_group_support`
- `missing_aspects`

错误标签：

- `overclaim_causal`
- `overclaim_generality`
- `overclaim_performance`
- `overclaim_sota`
- `overclaim_scope`
- `overclaim_mechanism`
- `unsupported_comparison`

例子：

- citation 只显示一个 benchmark 上有效，但 candidate 写成“解决了该问题”。
- citation 只是提出方法，但 candidate 写成“证明了某个机制”。
- citation 是 text-only setting，但 candidate 用它支持 multimodal GUI agent 的 claim。

### 2.4 Citation Coverage

看 candidate 是否引用了 gold 中重要的参考文献，或合理的等价替代文献。

| 分数 | 标准 |
| --- | --- |
| 9-10 | 覆盖几乎所有核心 reference。 |
| 7-8 | 覆盖大多数重要 reference，少量遗漏。 |
| 5-6 | 漏掉若干重要 reference，或替代文献较弱。 |
| 3-4 | 漏掉很多核心 reference。 |
| 0-2 | citation set 大多无关或过少。 |

检查字段：

- `metric_details.citation_quality.coverage`
- `missing_key_references`
- `diagnostics.missing_points`

错误标签：

- `missing_key_reference`
- `missing_foundational_work`
- `missing_recent_work`
- `missing_benchmark_reference`
- `citation_set_too_sparse`

### 2.5 Citation Placement

看 citation 是否放在它实际支持的 claim 附近。

| 分数 | 标准 |
| --- | --- |
| 9-10 | citation 紧贴对应 claim，支持关系清楚。 |
| 7-8 | 位置基本合理，少量歧义。 |
| 5-6 | 一些 citation 离 claim 太远，或多个 citation 打包导致支持关系不清。 |
| 3-4 | citation placement 经常模糊。 |
| 0-2 | 大量 citation 堆在段尾，无法判断支持哪句话。 |

错误标签：

- `citation_too_far`
- `citation_group_ambiguous`
- `citation_dump`
- `uncited_specific_claim`

### 2.6 Citation Group Support

如果一个 claim 同时引用多篇论文，需要判断这些 citation 作为一个 group 是否共同支持完整 claim。

| 分数 | 标准 |
| --- | --- |
| 9-10 | citation group 能覆盖 claim 的所有主要部分。 |
| 7-8 | 支持大部分 claim，但有少量缺口。 |
| 5-6 | 只部分支持，重要方面缺失。 |
| 3-4 | 多数 citation 只是邻近主题，不能真正支撑 claim。 |
| 0-2 | citation group 基本不支持 claim。 |

检查字段：

- `diagnostics.citation_group_support`
- `covered_aspects`
- `missing_aspects`
- `group_rationale`

错误标签：

- `group_partial_support`
- `group_missing_major_aspect`
- `group_mixed_unrelated_citations`
- `group_supports_background_only`

## 3. `relevance`

衡量 candidate 的 claim 是否与目标论文和 gold related work 的范围相关。

| 分数 | 标准 |
| --- | --- |
| 9-10 | 几乎所有 claim 都与目标 work 高度相关，并能帮助定位研究背景。 |
| 7-8 | 大多数内容相关，有少量 topic drift 或多余背景。 |
| 5-6 | 有多处内容只弱相关、过泛或偏离目标问题。 |
| 3-4 | 经常偏题，重要 claim 与目标研究语境不匹配。 |
| 0-2 | 大部分内容与目标 work 无关。 |

检查字段：

- `scores.relevance`
- `intermediate.claim_judgment`
- `weakly_relevant_claims`
- `irrelevant_claims`

常见扣分：

- 讲了邻近领域，但没有连接到目标论文。
- 加入泛泛的 LLM / agent 背景，但没有服务于 related work argument。
- 问题设定、模态、任务或 evaluation regime 与 gold 不一致。
- 与 gold 的事实判断冲突。

错误标签：

- `irrelevant_claim`
- `weakly_relevant_claim`
- `topic_drift`
- `wrong_problem_setting`
- `contradicts_gold`

## 4. `thematic_structure`

衡量 section 是否按照清晰主题组织，而不是简单堆论文。

| 分数 | 标准 |
| --- | --- |
| 9-10 | 主题分组清楚，段落内部连贯，段落顺序自然。 |
| 7-8 | 结构基本清楚，少量段落混杂或转折略生硬。 |
| 5-6 | 有一定主题结构，但多个段落主题混杂或逻辑流较弱。 |
| 3-4 | 主要是 list-like organization，主题关系难以跟随。 |
| 0-2 | 几乎没有清晰结构。 |

子维度：

| 子维度 | 检查内容 |
| --- | --- |
| Topic coverage | 是否覆盖 gold 的主要主题。 |
| Topic purity | 每段是否聚焦一个清楚主题。 |
| Topic coherence | 段内句子是否互相支撑。 |
| Topic granularity | 主题颗粒度是否合适，不太粗也不太碎。 |
| Topic ordering | 段落顺序是否符合逻辑。 |

建议权重：

| 子维度 | 权重 |
| --- | ---: |
| Topic coverage | 30% |
| Topic purity | 25% |
| Topic coherence | 20% |
| Topic granularity | 15% |
| Topic ordering | 10% |

错误标签：

- `mixed_paragraph_topics`
- `paper_list_without_theme`
- `poor_transition`
- `topic_too_broad`
- `topic_too_fragmented`
- `illogical_ordering`

## 5. `synthesis_quality`

衡量 candidate 是否真正综合文献，而不是逐篇罗列。

| 分数 | 标准 |
| --- | --- |
| 9-10 | 有强比较、趋势归纳、清晰 gap framing，文献被很好整合。 |
| 7-8 | 有较好的综合和部分比较，少量段落偏描述。 |
| 5-6 | 主要是描述性总结，比较和关系解释较弱。 |
| 3-4 | 基本是 paper-by-paper listing，缺少整合。 |
| 0-2 | 几乎没有 synthesis。 |

检查字段：

- `scores.synthesis_quality`
- `intermediate.synthesis_writing_judgment.synthesis_quality`
- synthesis `issues`

常见扣分：

- 逐篇列论文，不解释它们之间的关系。
- 没有说明 prior work 如何 motivate 当前 work。
- 提到 limitation，但没有形成明确 research gap。
- 没有比较方法、benchmark、assumption 或 evaluation setting。

错误标签：

- `paper_list_without_synthesis`
- `weak_comparison`
- `missing_gap_statement`
- `unsupported_trend`
- `poor_integration`

## 6. `writing_quality`

衡量语言清晰度、流畅性、准确性和学术风格。

| 分数 | 标准 |
| --- | --- |
| 9-10 | 表达成熟、准确、清晰，有良好学术风格。 |
| 7-8 | 基本清楚流畅，少量别扭或重复。 |
| 5-6 | 可读但有些含糊、啰嗦、不均衡或偶尔难懂。 |
| 3-4 | 经常不清楚、重复或措辞不佳。 |
| 0-2 | 语言混乱，基本不可用。 |

检查字段：

- `scores.writing_quality`
- `intermediate.synthesis_writing_judgment.writing_quality`
- writing `issues`

常见扣分：

- 使用 “many works show” 等含糊表述但不给具体内容。
- 句子过长，影响理解。
- 段落之间重复同一套 framing。
- 术语不一致。
- 表达不够学术或过于口语化。

错误标签：

- `vague`
- `verbose`
- `repetitive`
- `unclear_sentence`
- `terminology_inconsistent`
- `poor_academic_style`

## 7. `length_conciseness`

衡量篇幅是否合适、信息密度是否足够、是否冗余。

| 分数 | 标准 |
| --- | --- |
| 9-10 | 长度合适，信息密度高，几乎没有冗余。 |
| 7-8 | 略长或略短，但整体有效。 |
| 5-6 | 明显偏长、偏短、信息密度不均或有 padding。 |
| 3-4 | 严重啰嗦，或严重展开不足。 |
| 0-2 | 极短、极长或高度重复。 |

子维度：

| 子维度 | 检查内容 |
| --- | --- |
| Relative length | candidate 长度相对 gold 是否合理。 |
| Information density | 当前长度是否真正承载了相关信息。 |
| Redundancy | 句子或段落是否重复同一内容。 |

建议权重：

| 子维度 | 权重 |
| --- | ---: |
| Relative length | 50% |
| Information density | 30% |
| Redundancy | 20% |

常见扣分：

- 太短，无法覆盖关键 related work。
- 很长，但仍然漏掉核心内容。
- 多个段落重复同一 framing。
- 大量泛泛背景或 filler。

错误标签：

- `too_short`
- `too_long`
- `low_information_density`
- `redundant`
- `padded_background`

## Pipeline Error Overrides

当自动报告的分数受到解析或检索错误影响，而不是 candidate 本身质量问题时，使用 override。

| 标签 | 使用场景 |
| --- | --- |
| `pipeline_parse_error` | report 没有正确把 citation 映射到 reference，但人工能从输入文件中清楚确认映射。 |
| `reference_key_mismatch` | 正文 citation 和 bibliography label 使用不同 key 体系，例如正文 `\cite{dpo}`，reference 是 `[1]`。 |
| `metadata_retrieval_failure` | reference 在输入中有效，但外部 metadata 检索失败。 |
| `llm_judgment_incomplete` | report 漏掉了 citation-claim pair，或 judgment 为空。 |
| `false_positive_overclaim` | report 标了 over-claim，但人工判断 citation 足够支持。 |
| `false_negative_miscitation` | report 漏掉了明显 unsupported citation。 |

使用 override 时：

1. 保留原 pipeline score。
2. 给出 human-adjusted score。
3. 用一句话解释原因。

例子：

```text
Pipeline citation_quality = 5.0
Human citation_quality = 8.0
Override = pipeline_parse_error
Reason = bibliography 中有有效的 [dpo] label，但 report 是在 string label 支持修复前生成的。
```

## 标注模板

```text
sample_id:
reviewer:
date:

overall_score:
content_coverage:
citation_quality:
relevance:
thematic_structure:
synthesis_quality:
writing_quality:
length_conciseness:

major_errors:
- 

mis_citations:
- claim_id:
  reference_key:
  severity: minor|moderate|severe|critical
  reason:

over_claims:
- claim_id:
  reference_key:
  severity: minor|moderate|severe|critical
  reason:

missing_key_points:
- 

hallucinated_or_invalid_references:
- reference_key:
  reason:

citation_group_issues:
- claim_id:
  reference_keys:
  missing_aspects:
  reason:

pipeline_overrides:
- label:
  pipeline_score:
  human_adjusted_score:
  reason:

final_notes:
```

## Severity 说明

| 严重程度 | 定义 |
| --- | --- |
| minor | 不影响 section 的主要判断。 |
| moderate | 影响局部段落或局部 claim，但不破坏整体。 |
| severe | 影响重要 claim、主题或一组 citation。 |
| critical | 系统性破坏 section 的可信度。 |

## 快速规则

- 如果核心 claim 依赖 fabricated 或 wrong-paper reference，`citation_quality` 通常不应高于 5。
- 如果有 3 个以上 severe citation-support failures，`citation_quality` 通常不应高于 4。
- 如果文字很好但 citation 大量不支持 claim，`overall_score` 通常不应高于 6。
- 如果 coverage 弱但 citation 本身可靠，`citation_quality` 仍可以高于 8。
- 不要因为已知 pipeline parsing bug 惩罚 candidate；应使用 `pipeline_parse_error` 并给 human-adjusted score。
- over-claim 和 mis-citation 要分开标：citation 可以相关，但仍不足以支持 claim 的强度。
