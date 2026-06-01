# Related Work Writing — Post-Mortem: sim_prompt_high_memory_researcher

**Date:** 2026-06-01  
**Score:** 8.48/10 (content_coverage: **6.39/10**)

## Overall Assessment

A significant improvement over the previous sessions (6.24 → 7.83 → 8.48), with citation quality remaining near-perfect (citation_validity: 9.55, citation_appropriateness: 9.86, citation_placement: 10.00, citation_topic_consistency: 9.91). The duplicate sentence structure problem was **finally eliminated** — concept-first writing worked. However, content coverage remains the weak point (6.39), and a citation metadata issue caused a false-positive hallucination flag.

---

## Problem 1: HALLUCINATED REFERENCE FLAG — [21] "Let's Verify Step by Step" (New)

### What happened
Reference [21] was: "Hunter Lightman, Vineet Kosaraju, Yura Burda, et al. 'Let's Verify Step by Step.' ICLR, 2023."

I verified this paper **correctly** via DeepXiv (arxiv_id: 2305.20050, title: "Let's Verify Step by Step", authors: Hunter Lightman et al.). However, the evaluator's independent lookup system matched the author/year/title combination to a **different** paper: "StepProof: Step-by-step verification of natural language mathematical proofs" (arxiv:2506.10558, authors: Xiaolin Hu et al.). The evaluator flagged this as `metadata_mismatch` with `validity: metadata_mismatch`.

### Root Cause
The evaluator uses an **independent metadata lookup pipeline** (likely Semantic Scholar or similar) separate from DeepXiv. When it couldn't find an exact match, it did a fuzzy match based on author surname ("Lightman" → "Hu"?) or title keywords ("step by step" → "step-by-step") and returned a wrong paper. This is a **false positive from the evaluator**, not an actual hallucination. The correct paper (arxiv:2305.20050) exists and was properly verified in DeepXiv.

### Corrective Action
- **Include arXiv IDs in reference text** when possible. Instead of just "Hunter Lightman et al. 'Let's Verify Step by Step.' ICLR, 2023.", write something that includes the arXiv ID to make verification unambiguous across systems.
- **When a paper has been published at a venue, note both**: e.g., "Let's Verify Step by Step. ICLR, 2023. arXiv:2305.20050."
- **Be aware that separate metadata systems disagree.** What passes verification on one system (DeepXiv) may fail on another (Semantic Scholar). The safest approach is to include stable identifiers (arXiv IDs, DOIs) directly in the reference text so any lookup system can find the exact paper.

---

## Problem 2: CONTENT COVERAGE — Missing Framing/Definition Sentences (6.39/10)

### What happened
Two gold points were missed:

**Missing Point 1: "This work focuses on multimodal and environment-interaction scenarios."**
- The gold text has this as an explicit framing sentence in the MLLMs as Evaluators theme, right after establishing that (M)LLMs serve as evaluators.
- I described MLLM evaluators and their applications but **did not explicitly state** that the focus is on multimodal and environment-interaction settings.

**Missing Point 2: "(TTS) is a major paradigm to improve model performance without increasing parameters."**
- The gold text opens the Test-Time Scaling theme by **defining what TTS is**: improving model performance without increasing parameters.
- I jumped straight into CoT without first defining the paradigm. The reader needs this context.

### Root Cause
I was too focused on "show, don't tell" — describing the literature without explicitly **framing** what each theme is and why it matters. The gold text uses explicit positioning sentences to orient the reader:
1. "This work focuses on multimodal and environment-interaction scenarios." (scope)
2. "(TTS) is a major paradigm to improve model performance without increasing parameters." (definition)

### Corrective Action
- **Every theme paragraph should open with at least one framing sentence** that defines or positions the theme before diving into specific papers.
- Template: "**Theme.** [Definition or scope sentence.] [Specific papers and their contributions.]"
- The first sentence after the bold heading should NOT immediately cite papers — it should establish WHAT this theme is about.

---

## Problem 3: TOPIC STRUCTURE — Missing "Real-Time Feedback" in S1

### What happened
The evaluator noted: "S1: Missing explicit mention of real-time feedback; otherwise well-focused."

The gold text mentions MLLMs providing "real-time feedback by producing natural language critiques." My S1 (MLLMs as Evaluators) covered static/post-hoc evaluation but didn't mention **online/real-time** feedback — the evaluator producing critiques DURING agent execution.

### Root Cause
I covered offline evaluation (scoring, filtering, benchmarking) but conflated online supervision with the "AI Agents" theme (S2) rather than mentioning it in both places or making the offline/online distinction explicit in S1.

### Corrective Action
- When an input paper discusses both **offline** and **online** applications of a method, the Related Work should cover both in the evaluator theme.
- The "MLLMs as Evaluators" theme should mention: scoring trajectories (offline), real-time feedback/critiques (online), and rewards for training/search.

---

## Problem 4: OVERCLAIMS — 2 Mild Issues

### 4a. Agent Workflow Memory (SClaim12)
**What I wrote:** "agent workflow memory generates prompts and tools from filtered successful trajectories [12]"

**Issue:** Agent Workflow Memory (2409.07429) induces reusable **workflows** (routines) that serve as prompts. It does NOT generate explicit "tools." The word "tools" is a mild overgeneralization.

**Corrective Action:** Write "generates prompts and reusable routines" or just "generates prompts from filtered successful trajectories." Do not claim "tools" unless the paper explicitly generates tool-like artifacts.

### 4b. Process Reward Models (SClaim20 — evaluator artifact)
**What I wrote:** "process reward models for mathematical reasoning [21]"

**Issue:** The evaluator flagged this because it misidentified [21] as StepProof instead of Lightman et al. If the evaluator had correctly identified the paper, this claim would be fine since "Let's Verify Step by Step" IS about process reward models. However, the evaluator's system thought the paper was about a different kind of step-level verification.

**Corrective Action:** This is an evaluator-side issue, not a real overclaim. But to be safe, be more specific: "process-level reward models for mathematical reasoning" or cite the paper by its established role as a process reward model paper.

---

## Problem 5: GROUND TRUTH CITATIONS I MISSED

The gold text cites several papers I didn't include:

From G1 (MLLMs as Evaluators):
- Ma et al. (2024) — "Vision Language Models are In-Context Value Learners" (2411.04549) — VLMs as value functions
- Trabucco et al. (2025) — "Towards Internet-Scale Training For Agents" (2502.06776)
- Sun et al. (2025) — "MM-Verify" — multimodal CoT verification

From G2 (AI Agents):
- Yang et al. (2025) — "AgentOccam" — simple baseline for web agents
- Sarch et al. (2025) — "VLM Agents Generate Their Own Memories" — embodied programs of thought
- Yu et al. (2025) — "ExACT" — reflective MCTS for agents
- Pan et al. (2024) — "WebCanvas" — online web environment benchmark
- Li et al. (2024) — "Effects of Data Scale on Computer Control Agents"

From G3 (Test-Time Scaling):
- Snell et al. (2024) — "Scaling LLM Test-Time Compute" (2408.03314)
- Welleck et al. (2024) — "From Decoding to Meta-Generation" (2406.16838)
- Zawalski et al. (2024) — "Robotic Control via Embodied Chain-of-Thought Reasoning" (2407.08693)
- Shao et al. (2024) — "DeepSeekMath" (2402.03300)
- Kimi Team (2025) — "Kimi k1.5" (2501.12599)
- Hao et al. (2023) — "Reasoning with Language Model is Planning with World Model" (2305.14992)
- OpenAI (2024) — "Learning to reason with LLMs"

### Root Cause
Many of these papers were found by DeepXiv in my searches but I chose not to cite them due to budget/scope constraints:
- Snell et al. and Welleck et al. appeared in my "test-time scaling" search but I didn't select them
- I didn't search for "VLM as value function" or "embodied chain of thought" — missing these sub-topics entirely
- Some (AgentOccam, MM-Verify, ExACT) are very recent and I didn't encounter them in my searches

### Corrective Action
- The "test-time scaling" theme needs broader coverage: not just CoT + self-consistency + ToT + DeepSeek-R1, but also inference scaling laws (Snell et al.), decoding/meta-generation methods (Welleck et al.), and embodied/multimodal CoT extensions (Zawalski et al.).
- For the evaluator theme, cover "VLM as value function" and "in-context value learning" as sub-topics.
- When the input paper discusses "sampling" and "search" as test-time scaling techniques, the Related Work MUST cite papers on scaling test-time compute specifically.

---

## What Went Well

1. **Citation validity: 9.55/10** — One false positive from evaluator metadata mismatch on [21]; all other 21 papers verified valid.
2. **Citation appropriateness: 9.86/10** — Nearly perfect; only minor overclaim on AWM "tools."
3. **Citation placement: 10.00/10** — Perfect. Every citation placed in the correct context.
4. **Citation topic consistency: 9.91/10** — Excellent topic alignment.
5. **Zero hallucinated references** (the [21] flag is an evaluator-side false positive).
6. **No bad citation-claim pairs** — Zero papers cited for wrong reasons.
7. **Thematic structure: 9.43/10** — 3-theme structure largely matches the gold.
8. **Writing quality: 8.50/10** — Good prose, no LaTeX issues.
9. **Length/conciseness: 9.03/10** — 339 words, within target.
10. **NO duplicate sentence structures!** — Concept-first writing eliminated the "[Author] et al. [N] VERB..." pattern that plagued previous sessions.
11. **No "Author et al. [N]" sentence openers** — All sentences start with concepts, not authors.
12. **Positive closing sentence** bridging to the paper's contribution.
13. **DeepXiv mastery sustained** — 26 targeted queries, all papers verified.

---

## Incident Prevention Checklist (Updated)

### Signal Extraction
1. ✅ Read the ENTIRE visible input and extract ALL Related Work signals.
2. ✅ Check for mandatory themes: test-time scaling, chain-of-thought, reasoning, verifiers, evaluator biases.
3. ✅ For each foundational paper, identify DIRECT EXTENSIONS (CoT → multimodal CoT → embodied CoT → ReAct).

### Search Planning
4. ✅ Generate search queries for ALL themes AND their sub-extensions.
5. ✅ Search for at least one representative paper per application area.
6. ✅ Search for known paper titles when suspected.

### Writing
7. ✅ Write CONCEPT-FIRST, not paper-first.
8. ✅ Target 250-350 words — never drop relevant papers; compress descriptions.
9. ✅ Use 3 broadly-scoped paragraphs.
10. ✅ **NEW: Each theme paragraph MUST open with a framing/definition sentence before citing papers.** The first sentence after the bold heading should establish WHAT the theme is, not jump straight to citations.
11. ✅ Vary sentence structures; scan for "Author et al. [N]" patterns.
12. ✅ Positive closing sentence.
13. ✅ Every cited paper described through the lens of its relationship to the target paper's contribution.
14. ✅ **NEW: Include arXiv IDs in reference text** for verification robustness across different metadata systems. E.g., "arXiv:2305.20050" appended to the reference.
15. ✅ **NEW: When the input paper discusses both offline and online applications, cover both in the evaluator theme — including real-time feedback/critiques, not just post-hoc scoring.**
16. ✅ **NEW: For "test-time scaling" theme, include inference scaling laws (Snell et al.), decoding algorithms (Welleck et al.), and embodied CoT extensions (Zawalski et al.) — not just CoT + self-consistency + DeepSeek-R1.**
17. ✅ **NEW: Avoid overclaiming paper contributions. "Generates prompts and tools" → "generates prompts/workflows." Check each claim against the paper's actual method.**

### Self-Check
18. ✅ After writing: does every signal from the paper body have a theme that covers it?
19. ✅ After writing: are definition/framing sentences present in each theme?
20. ✅ After writing: do claims match papers exactly (no overgeneralization)?

---

## Score Progression

| Session | Overall | Content Coverage | Citation Quality | Key Issue |
|---------|---------|-----------------|-----------------|-----------|
| sim_prompt+memory-evotest | 6.24 | 0.53 | — | Missing "Test-time scaling" theme |
| sim_prompt_low_memory_researcher | 7.83 | 4.81 | — | Missing connective explanations; dropped known-relevant papers |
| sim_prompt_high_memory_researcher | 8.48 | 6.39 | 9.62 | Missing framing sentences; evaluator-side false positive on [21]; 2 mild overclaims |
