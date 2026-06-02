# Related Work Generation — Post-Mortem: sim_prompt+memory-evotest (Paper 12299)

**Date:** 2026-06-01 | **Score:** 6.89/10 | **Task:** Generate Related Work for anonymized paper via DeepXiv search.
**Paper Topic:** MobileIPL — Iterative Preference Learning for VLM-based Mobile GUI Agents using CoaT-tree MCTS + T-DPO.

---

## 1. Writing Process Summary

### 1.1 Paper Analysis
- Read anonymized paper body (abstract, intro, methodology).
- Inferred: mobile GUI agent, CoaT reasoning (description → thought → action → grounding), iterative preference learning (IPL), MCTS-based CoaT-tree, rule-based rewards, T-DPO, instruction evolution, Qwen2-VL-7B backbone, AITZ/AMEX/AndroidControl benchmarks.
- Baselines mentioned: CogAgent, Auto-GUI, SphAgent, OS-Atlas, UGround, UI-TARS, FedMobileAgent, Falcon-UI.

### 1.2 Search Strategy
- Conducted 34 DeepXiv search queries across 5 batches.
- Queries covered: VLM GUI agents, GUI grounding, CoaT reasoning, MCTS+DPO, self-training, step-level preference optimization, datasets.
- Verified 28 papers via `head`/`brief` endpoints for author names, venues, years.
- Selected 24 papers for citation organized into 4 themes.

### 1.3 Final Output
- s_text.txt: 4 themed paragraphs, 707 words, 24 citations.
- s_reference.txt: 24 verified entries.
- No hallucinations detected by evaluator (citation_validity: 10/10).

---

## 2. Problems Identified by Evaluation

### Problem 1: Severely Low Citation Coverage (2.40/10) and Content Coverage (4.38/10)
**Root cause:** Missed 6 gold points that the ground-truth Related Work expected.

**Missed papers/methods:**
1. **Closed-source VLM mobile agents / multi-agent frameworks (arxiv:2303.08774)** — I focused exclusively on open-source VLM agents and never searched for closed-source approaches. The ground truth expects coverage of early work using GPT-4V/closed models.
2. **ReFT (arxiv:2401.08967)** — RL fine-tuning for math reasoning. My MCTS+DPO searches didn't surface this because ReFT is a pure RL approach, not tree-search-based.
3. **Reachagent (arxiv:2502.02955)** — DPO-based training for comparing action quality. This is directly relevant to the paper's T-DPO approach but I never searched for "reachagent" or action-level DPO.
4. **TCPO (arxiv:2509.08500)** — Optimizes thoughts but doesn't enforce thought-action consistency. Directly comparable to the paper's T-DPO approach.
5. **TreePO, TreeRL, SPO** — These methods segment long sequences into short segments, causing computational issues. The paper explicitly contrasts against these. I found SPO-related papers briefly but didn't identify TreePO or TreeRL as distinct methods.
6. **Method self-positioning** — The paper's own advantages (fixed CoaT-tree, T-DPO, rule-based rewards without PRMs) should be discussed as a gap in prior work.

**Lesson:** When a paper's method compares against specific named approaches, search for EACH of those approaches explicitly. The paper mentioned "SPO" and alluded to tree-based preference methods — I should have searched for each comparison point individually rather than relying on broad theme-level searches. Also, closed-source VLM agents represent a distinct line of work that should be covered.

### Problem 2: Low Synthesis Quality (2.50/10)
**Root cause:** The Related Work reads as an enumeration of papers rather than synthesized narrative.

**Specific issue:** Each paragraph lists papers sequentially with "X [n] proposed Y. Z [m] introduced W." structure. Missing are:
- Cross-cutting observations about common limitations.
- Explicit contrasts between approaches.
- How the proposed method addresses gaps left by prior work.
- Thematic synthesis rather than cataloging.

**Lesson:** After gathering papers, explicitly identify common limitations across groups of papers and write about the shared problems, not just individual contributions. The final sentence of each paragraph should connect back to the paper's motivation.

### Problem 3: Overclaims (2 instances)
**Overclaim 1 (mild): InfiGUI-R1 [13] / SClaim15**
- My text: "...then reinforces them via **preference optimization**."
- Reality: InfiGUI-R1 uses RL (sub-goal guidance, error recovery), not explicit preference optimization like DPO.
- **Lesson:** When unsure about the specific training method a paper uses (RL vs DPO vs preference optimization), use more general language ("reinforcement learning") or verify the method name precisely. Don't assume similar-sounding methods are the same.

**Overclaim 2 (moderate): ReST-MCTS* [14] / SClaim18**
- My text: "...though it **requires process-level annotations**."
- Reality: ReST-MCTS* explicitly circumvents manual annotation by inferring process rewards via tree search using only oracle final answers.
- **Lesson:** This is a serious factual error. I should have read the TLDR/abstract more carefully — it states "circumvents the per-step manual annotation." When describing a paper's limitation, verify the limitation is actually stated in the paper, not inferred from analogy with related work.

### Problem 4: Excessive Length (2.05x ground truth)
- My section: 707 words, 24 citations.
- Ground truth: 345 words, presumably fewer citations.
- **Root cause:** I included 10 papers in paragraph 1 (VLM-based GUI Agents) when a more selective approach would cite only the most representative. I was trying to be comprehensive rather than focused.
- **Lesson:** For Related Work, 5-7 papers per paragraph max. Prioritize papers that are (a) directly compared against, (b) methodologically closest, or (c) represent distinct research directions. Pure-survey inclusion of every related agent dilutes the section.

### Problem 5: Missing Methodological Contrasts
- The paper designs its method explicitly to address: (1) lack of step-level annotation → rule-based rewards, (2) overfitting to fixed CoaT patterns → instruction evolution, (3) unstable PRMs → T-DPO with credit backpropagation.
- My Related Work mentions these problems in the intro-copy sentences but doesn't build the Related Work around showing how prior work fails to solve them.
- **Lesson:** The Related Work should be organized around the paper's claimed contributions/improvements, showing how each prior approach is deficient in the ways the proposed method addresses.

---

## 3. What Went Well

1. **Zero hallucinated references (citation_validity: 10/10).** All 24 papers verified via DeepXiv.
2. **Strong citation appropriateness (9.79/10) and topic consistency (10.00/10).** Papers placed in correct thematic sections.
3. **Good thematic structure (9.18/10).** Four-theme organization was appropriate.
4. **High relevance (9.48/10).** All cited papers are actually relevant to the topic.
5. **Clean output format.** No LaTeX forbidden commands, correct citation format.

---

## 4. Actionable Improvements for Future Related Work Generation

1. **Search for ALL named comparison methods explicitly.** If the paper mentions "SPO," "TreePO," "GRPO," etc., create a dedicated search query for each.
2. **Search for closed-source/baseline approaches** — papers using GPT-4V, Claude, or other proprietary models as backbone agents.
3. **Verify claims about paper limitations before writing.** Read the TLDR/abstract of every cited paper for the specific limitation being attributed to it.
4. **Use precise training method terminology.** Don't say "preference optimization" when the paper uses RL; use the exact method name.
5. **Limit paragraph length.** Target 4-6 citations per paragraph, not 8-10.
6. **Structure paragraphs around shared limitations**, not paper-by-paper enumeration. Each paragraph should end by connecting to the proposed method's motivation.
7. **Include explicit method positioning** — the final paragraph or closing sentences should state what gap remains that the proposed method fills.
8. **Target word count:** For a focused Related Work, aim for 300-400 words, not 700+.
