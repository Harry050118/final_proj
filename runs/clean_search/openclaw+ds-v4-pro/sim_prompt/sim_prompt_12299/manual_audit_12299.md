# Evaluation Tables Based on New Pipeline Report

被评样本：`runs/clean_search/openclaw+ds-v4-pro/sim_prompt/sim_prompt_12299`
目标论文：sample 12299 — MobileIPL（CoaT-tree + Thinking-level DPO for mobile GUI agents）
candidate：21 篇 reference、1183 词，长度是 gold（345 词）的 3.43×；分四个主题段 + 一段 “Our work … differs from” 对比段。
评分细则参考 `HUMAN_EVALUATION_RUBRIC_ZH.md`，Pipeline 分取自 `report.md` / `report.json`。

## 主表

| 指标                    | Pipeline 分 | Pipeline 理由                                                                                                                                                              | 人工分 | 人工打分理由                                                                                                                                                                                                                       |
| --------------------- | ---------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| content_coverage      |       4.20 | Pipeline 列出 6 条 missing_points：closed-source VLM + multi-agent framework、ReFT、Digirl/Distrl、Reachagent、TCPO、TreePO/TreeRL/SPO，均未被 candidate 提及，matched_weight=10.5/25.0 | 5.0 | 同意覆盖偏弱：gold RL 子节明确点名的 mobile-GUI RL 方法（Digirl、Distrl、Reachagent、TCPO、TreePO/TreeRL/SPO、ReFT、IPO/KTO/PPO）全部缺失。但 candidate 补了 SeeClick/UGround/OS-ATLAS/UI-TARS/Falcon-UI 等等价开源 VLM agent，并引到 DPO/Step-DPO/ToT/ReST-MCTS\*/Xie/CPO，方向正确，故较 pipeline 略上调，落在“覆盖大方向但漏关键方法”的 5 档 |
| citation_quality      |       7.79 | Pipeline 认为无 hallucinated reference、validity 高、placement/topic 一致；composite 由子项加权得到（见下表）                                                                                  | 7.2 | 引用真实性确实好，但 3 个 bad pair 与 1 个 mild overclaim 都落在核心 synthesis claim（ReST-MCTS\*、AITZ），且 citation coverage 对 gold 明显不足，故应低于 pipeline（详见 Citation Quality 展开表）                                                                          |
| relevance             |       8.09 | Pipeline 认为内容整体围绕 mobile GUI agent + RL/preference optimization，高度相关                                                                                                      | 7.5 | 基本相关，但 Li et al. 的 CoT 实证段与 DeepSeek-R1 这类纯文本 RL 在 gold 语境里偏 weakly relevant；3.43× 的篇幅也带进若干 background/边缘内容                                                                                                                       |
| thematic_structure    |       8.25 | Pipeline 认为主题分组清楚（S1–S11 按主题成段），仅因 paragraph text not available 用 topic summary 估分                                                                                          | 8.0 | 四个主题段 + 总结段，topic purity/ordering 都不错；唯一弱点是 gold 中同属 RL 一条线的 self-training/preference 与 MCTS 在此被拆成两段，主题颗粒度略偏细                                                                                                                       |
| synthesis_quality     |       8.00 | Pipeline 认为有较好的 gap framing 与对比                                                                                                                                          | 7.5 | 末段“Our work, MobileIPL, differs from …”比较与 gap 清楚；但前四段以逐篇描述为主，段间整合较弱，且对 ReST-MCTS\* 的 “GUI step-reward 成本高” framing 属 over-synthesized                                                                                            |
| writing_quality       |       8.50 | Pipeline 认为语言成熟、术语一致                                                                                                                                                     | 8.0 | 句式清晰、术语统一；个别 PR 化措辞（“significantly improve …”），个别长句信息密度过高                                                                                                                                                                       |
| length_conciseness    |       4.02 | Pipeline 标 relative length ratio=3.43（s=1183 / g=345），明显偏长                                                                                                               | 3.5 | 3.43×原文太长了；信息密度尚可，但 CogAgent/SeeClick/AITW 等描述相对 gold framing 是 padded background，落在 3-4 档                                                                                                                              |
| overall / final_score |       7.04 | Pipeline 综合分 7.04；低 coverage / length 被较高 citation、relevance、structure、writing 拉回                                                                                         | 6.81 | 人工分与 pipeline 接近。candidate 不是引用造假型问题，而是 gold coverage 不足（漏掉 gold 明确点名的 mobile-GUI RL 方法）、长度失控（3.43× gold）、以及个别核心 claim 撑不住（ReST-MCTS\* 被用来支撑 GUI step-reward 成本的中心动机句，与原论文设定矛盾）。写作与结构成熟、引用真实可查，整体属于可用但需要收紧篇幅并补关键文献线的 related work                                                                                 |

---

## Citation Quality 展开表

| Citation quality 子项        | Pipeline 分 | Pipeline 理由                                                                                                  | 人工分 | 人工打分理由                                                                                                                                                | Pipeline 和人工对齐情况  |
| -------------------------- | ---------: | ----------------------------------------------------------------------------------------------------------- | --: | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| citation_validity          |       9.72 | 无 hallucinated reference；14 条 bibliographic accuracy issue 仅为“retrieved metadata omits authors”，作者无法外部核验      | 9.5 | 21 篇 reference 全部 arXiv-可识别、与正文标题一致；report 的 author-omission 属外部 metadata 检索侧问题（rubric: `metadata_retrieval_failure`），不应记在 candidate 头上，故近满分              | 对齐               |
| citation_appropriateness   |       9.00 | Pipeline 标出 3 条 bad pair（SClaim15、SClaim29、SClaim32）和 SClaim33 的 mild overclaim，但综合给 9.00 偏高                  | 7.5 | 大多数引用能支撑 claim，但问题集中在核心句：SClaim29/32 用纯文本的 ReST-MCTS\* 撑 “GUI step-reward 成本高/需独立 PRM”，与该论文设定矛盾（support=no）；SClaim15 把单篇 AITZ 写成 “widely validated”。按 rubric 2.2/2.3 应明显低于 9 | Pipeline 偏高       |
| citation_coverage          |       2.17 | coverage matched_weight=5.0/23.0；gold key reference 大量未命中                                                     | 4.0 | coverage 客观弱：gold 点名的 ReFT、IPO/KTO/PPO、Digirl、Distrl、Reachagent、TCPO、TreePO/TreeRL/SPO 全缺。但 candidate 用 SeeClick/UGround/OS-ATLAS/UI-TARS + DPO/Step-DPO/ToT/CPO 等等价替代覆盖了同方向，pipeline 只按 gold 命中率打分偏低，人工给等价替代部分信用 | Pipeline 偏低       |
| citation_placement         |       8.22 | Pipeline 认为 placement 基本合理                                                                                    | 8.5 | 引用紧贴对应 claim，无 citation dump；段首 group citation [1,2,3,4] 经 group_support=yes 验证，边界清楚                                                                     | 对齐               |
| citation_topic_consistency |       9.49 | Pipeline 认为引用与段落主题高度一致                                                                                        | 8.5 | 大方向一致（GUI agent / RL / preference / tree-search）；但 topic consistency ≠ claim-level support，ReST-MCTS\* 主题相关却撑不住 GUI-cost claim，故略低于 pipeline             | Pipeline 略高       |
| citation_quality 综合分       |       7.79 | 由子项按 validity25/appr35/cov20/place10/topic10 加权得到（已复算=7.79）                                                   | 7.2 | 同权重加权 ≈7.5；但 2 条 ReST-MCTS\* unsupported 引用正好落在论文中心动机（“PRM 成本高 → 用 rule-based reward 替代”），按 rubric“核心 claim 依赖撑不住的引用”应额外下压，故定 7.2                          | Pipeline 略高 |

---

## 简短人工结论

candidate 的主要问题不是 reference 伪造（validity 近满分），而是两点：

1. **gold coverage 不足** —— gold RL 子节明确列举的 mobile-GUI RL/preference 方法（Digirl、Distrl、Reachagent、TCPO、TreePO/TreeRL/SPO、ReFT、IPO/KTO/PPO）全部缺失，candidate 用通用文本 RL（DPO、Step-DPO、DeepSeek-R1、ToT）填空，方向对但重点错位（`incorrect_topic_emphasis` + `missing_key_reference`）。
2. **长度失控 + 个别核心 claim 撑不住** —— 3.43× 的篇幅属 `too_long`；ReST-MCTS\*（纯文本）被用来支撑 “GUI step-reward 成本高、需独立 PRM” 的中心动机句，与原论文设定矛盾。

> 说明：citation_coverage 人工分（4.0）与 pipeline（2.17）相差 >1，原因是 pipeline 只按 gold reference 命中率打分，未给等价替代文献信用；其余指标人工与 pipeline 偏差均 <1。

最终人工分建议：**6.8 / 10**。
