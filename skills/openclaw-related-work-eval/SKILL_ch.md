---
name: openclaw-related-work-eval
description: 当需要根据论文正文、摘要、研究想法、匿名化输入或候选文献列表撰写 Related Work 时使用，尤其适用于强调引用可靠性、仅使用 DeepXiv 检索、生成 RWEval 可读输出或进行 claim-citation grounding 的任务。
---

# Related Work Grounding

## 目的

撰写可靠、可用于 RWEval 的 Related Work：覆盖输入中可见的 prior-work 信号，通过 DeepXiv 验证最终引用，并且只把 citation 绑定到它能直接支持的 claim 上。

除非用户明确要求聚焦 Related Work，否则本 skill 不用于整篇论文写作、实验、Introduction、Discussion 或通用润色。

## 输出

当用户提供输出目录时，写出：

- `s_text.txt`：只包含生成的 Related Work 正文。
- `s_reference.txt`：最终引用列表，每条引用对应一篇论文，包含 title、authors、year，以及可用的 DeepXiv/arXiv/URL 元数据。
- `trace.md`（RWEval run 推荐写出）：queries、screening、coverage decisions、final citations、self-checks 和 unresolved gaps。

RWEval 文件使用数字引用：`s_text.txt` 中使用 `[1]` 或 `[2, 3]`，并在 `s_reference.txt` 中使用匹配编号。不要写 `g_text.txt` 或 `g_reference.txt`，生成过程中不要读取 ground-truth Related Work 文件。

## Evidence Safety Rules

- DeepXiv 是唯一允许的学术检索来源。不要 fallback 到 web search、arXiv search、Google Scholar、Semantic Scholar、DBLP、ACL Anthology、PubMed、ACM、IEEE、publisher search 或纯记忆 citation。
- 如果 DeepXiv 不可用或证据不足，停止并报告检索问题，不要替换为其它来源。
- 不要搜索被移除或隐藏的标识符，例如 hidden title、DOI、arXiv ID、reference list、figure captions、table captions 或完整论文标识。
- 不要编造论文、作者、venue、数据集、数值结果、比较结论或实验 claim。
- 不要把目标论文自己的实验结果、消融、运行时间、百分比提升或 superiority claim 当作 prior-work evidence。
- weakly relevant 或 substitute papers 只能支持窄背景/context claims，不能支持 core claims、named-work recovery 或 comparative claims。
- comparative 或 superiority claims 必须有 DeepXiv 对同一对象、同一任务和同一比较的直接证据；否则窄化、改成 target-paper motivation 或删除。
- 避免使用 `often`、`consistently`、`substantially`、`real-world applicability`、`open challenge`、`human-level`、`outperform` 等强词，除非有直接证据。
- survey 支撑的 claim 通常应写成 survey `organize`、`identify`、`review` 或 `discuss` 某领域，而不是写成该领域已经证明、失败或完成转变。
- benchmark paper 默认只支持 benchmark scope 和 evaluation target；它本身不证明某个模型、系统或训练/评估方案优于另一个。
- 最终引用必须有合理且内部一致的 title、authors、year、identifier 和 citation role。未来年份、异常 arXiv 年月、title-author-year 冲突或不稳定 metadata 必须保持 `screened only`。

## 工作流程

### 1. 读取可见输入

检查完整可见输入，不要只看 abstract 或 introduction。

提取：

- Topic、application area、task、method/system/intervention。
- Dataset、benchmark、data type 和 evaluation focus。
- Main contribution，但不包含 measured results 或 superiority。
- Boundaries：目标论文不主张或不评估什么。

明确检查是否存在可见的 `Related Work`、`RELATED WORK`、`Background` 或等价 section。若存在，提取 headings 和 named citations。除非已经检查完整输入，否则不要声称 Related Work section 缺失。

### 2. 构建 Coverage Scaffold

检索前创建 `Visible Coverage Scaffold`。它指导检索和结构，不是 citation evidence。

将可见信号归类为：

- `named works`：author-year citations、named systems、benchmarks、datasets 或 methods。
- `field background`：historical context、application areas、taxonomies、broad trends 或 field-level challenges。
- `method context`：methods、models、algorithms、system designs、evaluation setups、datasets 或 benchmarks。
- `target motivation`：目标论文陈述的 gap、positioning、need、challenge 或 contribution hook。

如果可见 Related Work 有 2-4 个 headings，默认保留为 planned themes，除非 DeepXiv 无法为某个 heading 验证任何可用证据。

### 3. 检索与筛选

先 exact recovery，再 broad discovery：

- 对 author-year 信号，用作者姓氏加可见 task phrase 或可能 title words 查询。
- 对 named works，还要用 visible contribution phrase、task phrase，以及 system、benchmark、dataset 或 method phrase 查询；不要只依赖作者名。
- 对 systems、benchmarks、datasets、evaluation settings 和 application domains，用 exact name 加 task、modality 或 benchmark context 查询。
- 对 historical 或 field-background 信号，用 field phrase 加 `survey`、`review`、`taxonomy` 或可见 application domain 查询。

query 必须从可见输入动态生成。不要引入输入中没有出现、也没有通过 DeepXiv 发现的固定论文、作者、系统、benchmark 或主题。

筛选每个 candidate：

| Label | 允许用途 |
|---|---|
| `relevant` | 直接支持可见 theme、task、method、benchmark、comparison 或 gap。 |
| `weakly relevant` | 只支持 historical、taxonomy、adjacent-task、benchmark、survey 或 context claims，且必须窄措辞。 |
| `irrelevant` | 不要引用。 |
| `screened only` | 看似有用但 metadata 不稳定、不适合最终正文，或作为最终引用不安全。 |

如果作者无法恢复但概念在输入中可见，可以检索概念级 substitute。最终只能写概念级 claim，不能写成原作者或原论文已被 recovered。

### 4. 规划覆盖

写作前创建 `Final Text Coverage Plan`。对 scaffold 中每个 visible signal，选择且只选择一种处理：

| Handling | 使用条件 | 正文规则 |
|---|---|---|
| `final claim` | DeepXiv 直接证据支持该信号。 | 写入 `s_text.txt` 并绑定具体 citation。 |
| `narrow context` | 只有 survey、taxonomy、benchmark、adjacent-task 或 concept-substitute 证据。 | 只能用窄措辞写入正文。 |
| `target motivation` | 支撑来自目标论文 positioning，而不是 prior-work evidence。 | 无引用写作，或与 citation 明确分离。 |
| `trace-only gap` | 没有稳定 DeepXiv evidence。 | 记录在 `trace.md`，不要强行写入正文。 |

不要让稳定有证据支持的信号只留在 trace。证据允许时保留可见枚举，尤其是 application domains、tool uses、task stages、datasets、benchmarks 或 method families 的列表。

### 5. 撰写 Related Work

按 theme 写，而不是按 search result 顺序写。

- 使用 2-4 个 planned themes；有可见 headings 时默认镜像。
- 每个正文段至少有一个 citation。纯 target-motivation 句并入相邻有引用段，不要留下独立无引用段。
- citation 绑定具体 claim。multi-citation 句只用于 broad context。
- context substitute 必须写成 broad context，不能写成覆盖了缺失 named work。
- 目标论文指出的 need 或 challenge 应写成 target-paper motivation，除非 citation 直接陈述同一 need 或 challenge。
- active citation budget：
  - RWEval 默认 `12-18` 篇最终引用。
  - 可见输入有三个或更多 themes 且有足够 metadata-stable、directly relevant candidates 时，目标至少 `15` 篇。
  - 只有 DeepXiv recovery 稀疏、输入很窄，或候选大多 weakly relevant / metadata-unstable 时，才使用 `8-12`。
  - 不要为了凑够 15 篇加入 weakly relevant、metadata-unstable 或 claim-unsupported papers。

### 6. 最终检查

最终输出前：

- 每个 in-text citation 都出现在 `s_reference.txt`，每个 reference entry 都在 `s_text.txt` 中被引用。
- 每个 citation-claim pair 都是 supported、已窄化、已改成 target motivation，或已删除。
- 没有 weakly relevant paper 支持 core claim。
- 没有 context substitute 被呈现为 named work 的 exact recovery。
- 最终引用中没有 metadata-plausibility concern。
- 没有 comparative claim 留下，除非它由 DeepXiv evidence 直接支持。
- 没有 `Target-paper interpretation` self-check row 的 final action 是 `keep`；最终前必须改写为无引用 motivation、窄化为直接支持的 claim，或删除。

最终 self-check labels 只能是：

- `Supported`
- `Partially supported`
- `Unsupported`
- `Target-paper interpretation`

最终 actions 只能是 `keep` 或 `resolved`；在最终输出前先实际应用 `narrow`、`remove` 或 `move to motivation`。

## Evaluation-Aware Gates

RWEval-oriented runs 检查：

- `RWEval Citation Format`：数字引用能直接映射到编号 references。
- `Read the Visible Input`：完整输入已检查 Related Work/Background section。
- `Visible Heading Preservation`：可见 2-4 个 headings 被镜像为 themes。
- `Named Citation Exactness`：author-year 信号先 exact search，再考虑 substitute。
- `Final Text Coverage`：每个 visible signal 被分配为 `final claim`、`narrow context`、`target motivation` 或 `trace-only gap`；稳定支持的信号不能只留在 trace。
- `Weak Evidence Contained`：弱证据或 substitute evidence 只用于窄 context。
- `Reference Validity Guard`：metadata 不稳定论文不进入最终引用。
- `Metadata Plausibility`：最终 references 的 year、identifier 和 title-author-year consistency 合理。
- `Dynamic Citation Budget`：默认 `12-18`，证据支持时目标至少 `15`，只有证据稀疏或不稳定时才使用 `8-12`。
- `Final Consistency`：in-text citations、references、self-check 和 trace ledger 一致。

如果任何 gate 失败，在 `trace.md` 中将 final status 标为 `incomplete with usable RWEval output`。

## Trace 模板

```markdown
## Run Metadata
- Date:
- Search source: DeepXiv only

## Paper Profile
| Field | Value |
|---|---|

## Visible Coverage Scaffold
| Visible signal | Signal type | Query intent | Recovery status | Planned handling |
|---|---|---|---|---|

## Candidate Screening
| Title | Authors | Year | Source | Label | Reason |
|---|---|---:|---|---|---|

## Final Text Coverage Plan
| Visible signal | Evidence status | Final text handling | Claim wording constraint |
|---|---|---|---|

## Final Cited Papers
| Title | Authors | Year | Source | Citation role |
|---|---|---:|---|---|

## Claim-Citation Self-Check
| Citation | Claim | Supported? | Claim strength | Action | Notes |
|---|---|---|---|---|---|

## Completion Status
| Gate | Status |
|---|---|

## Uncertain Points
-
```

## 候选文献列表

如果用户提供候选论文，把它们当作 candidates，而不是 endorsements。像检索结果一样筛选。

只使用候选列表中的 bibliographic/content metadata：title、authors、year 或 venue、abstract、URL/DOI/arXiv/source page。不要把 hidden labels、private rejection reasons 或 evaluator-only annotations 暴露给生成流程。
