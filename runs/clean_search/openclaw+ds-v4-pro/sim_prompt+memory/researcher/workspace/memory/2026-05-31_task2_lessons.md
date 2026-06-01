# 2026-05-31 — Related Work Generation Task #2: Detailed Problem Analysis

## Overall Score: 8.12/10
Improvement from previous run (6.17/10). Strong areas: thematic structure (9.32), writing quality (9.00), citation validity (9.17).

Weak areas: content_coverage (5.85), relevance (6.61), citation_placement (7.93).

---

## PROBLEM 1 (CRITICAL): Reference [9] MARG Became Hallucinated

**What happened:**
Reference [9] was correctly verified through DeepXiv `brief('2401.04259')` returning title "MARG: Multi-Agent Review Generation for Scientific Papers" by Mike D'Arcy et al. However, the evaluation system resolved this reference to `arxiv:astro-ph/0212269` "Recent Results from the VERITAS Collaboration" — a completely unrelated TeV gamma-ray astronomy paper. Flagged as `metadata_mismatch` with `match_score: 0.38`.

**Root cause:**
The reference format was too vague — only `"arXiv, 2024."` without including the arXiv ID (`arXiv:2401.04259`). The evaluation system performs fuzzy title-based matching against its own DeepXiv index, and when MARG's title didn't match any entry exactly (possibly due to indexing gaps), the system fell back to a nearest-match that was completely wrong.

The ground truth references use full identifiers like `arXiv preprint arXiv:2401.04259` or specific venue names. Without the arXiv ID, the evaluation system has no anchor for exact matching.

**Lesson:**
- **ALWAYS include the arXiv ID in references** — write `arXiv:2401.04259, 2024.` not just `arXiv, 2024.`
- **Use the format from the ground truth as the gold standard:** `"Authors. Title. arXiv preprint arXiv:xxxx.xxxxx, year."` 
- **Do not assume titles will survive fuzzy matching** — even a correctly-verified paper can fail evaluation if the reference format is too vague.
- **Bonus: This also validates that the `brief()` output title matches what I wrote in the reference.** My brief() returned the correct title, but without the arXiv ID, the system couldn't anchor it.

---

## PROBLEM 2: Missing 7 Ground Truth Content Points

### 2a. GPoint1 — Multi-agent collaborative writing and multi-module retrieval
**What ground truth says:** Prior work uses "multi-agent collaborative writing" and "multi-module retrieval" to improve research idea generation.  
**What I missed:** I described ResearchAgent [1] with its "multi-agent peer review" and SciMON [2] with "open-ended idea generation," but I never explicitly named "multi-agent collaborative writing" and "multi-module retrieval" as high-level strategies. I described the mechanisms without labeling them at the right abstraction level.  
**Lesson:** Use the exact terminology that the paper's own Related Work uses for categorizing prior approaches. Don't just describe what individual papers do — name the strategy families they belong to.

### 2b. GPoint2 — Si et al. (2024) human evaluation of LLM research ideas
**What ground truth says:** "Si et al. (2024) conducted a comprehensive human evaluation of the task of idea generation by language models."  
**What happened:** I searched for "Si et al human evaluation idea generation LLM" but only found IdeaBench (2411.02429) and Rapid AIdeation. I never located the specific Si et al. paper. The gold reference is `arxiv:2409.04109`.  
**Lesson:** Some papers are hard to find via semantic search alone. Try author name queries more aggressively. Also: the "IdeaBench" result was close but not the same paper — don't settle for nearby results when a specific named paper is expected.

### 2c. GPoint9 — Modern AI4Science with neural networks and multi-agent perspectives
**What I missed:** I said AI is used "primarily as a passive tool for data analysis" which covers the limitation but I never stated the positive: "modern AI4Science efforts leverage neural networks and multi-agent perspectives."  
**Lesson:** For each theme, cover both the positive trajectory (what prior work DOES) AND the limitation (what it DOESN'T do). I covered the limitation well but wasn't specific enough about the positive contribution of modern AI4Science works.

### 2d. GPoint13 — AI tools for summarizing, detecting inaccuracies, fairness disparities
**What I missed:** In the Automated Evaluation paragraph (S3), I jumped directly to LLM-based review approaches without mentioning the broader context of AI tools in scientific publishing: summarizing paper content, detecting statistical inaccuracies, and identifying fairness disparities.  
**Lesson:** Before diving into the specific sub-problem (LLM peer review), establish the broader ecosystem of AI in scientific publishing. This provides context and shows the paper's place in a larger research landscape.

### 2e. GPoint15 — Small-scale qualitative experiments with ChatGPT/GPT-4
**What I missed:** The ground truth specifically mentions "Hosseini & Horbach (2023) conducted small-scale qualitative experiments" and "Robertson (2023) invited 10 participants to assess GPT-4 in peer review." I couldn't find these through DeepXiv (the Hosseini paper is in a journal: Research Integrity and Peer Review, 8(1):4, 2023). I therefore didn't cite them.  
**Lesson:** When papers exist outside arXiv (journal publications), they won't be found through DeepXiv. But the task rules say "Use DeepXiv as the only academic retrieval source" — so I correctly didn't fabricate them. The missing point reflects a fundamental limitation of the clean search condition. However, I COULD have mentioned small-scale qualitative studies in general terms even without specific citations, connecting them to the GPT4-is-slightly-helpful paper [2307.05492] which I DID find.

### 2f. GPoint16 — GPT-4 evaluating full-text PDFs
**What I missed:** The ground truth mentions that GPT-4 was used to evaluate full-text PDFs of scientific papers. Liang et al. [8] DOES do this (they "created an automated pipeline using GPT-4 to provide comments on full PDFs") — but I described their work as "whether LLMs can provide useful feedback on research manuscripts" without mentioning the full-text PDF evaluation aspect.  
**Lesson:** Read abstracts carefully. Liang et al. explicitly mention PDF processing — I should have included this concrete detail to match the ground truth's specificity.

### 2g. GPoint18 — Challenge of human-level judgment in AI-driven peer reviews
**What I missed:** The ground truth states: "This gap highlights the challenge of achieving human-level judgment and reasoning in AI-driven peer reviews." I mentioned the gap between purpose-trained reward models and general-purpose LLM judges, but I framed it as "purpose-trained reward models can exhibit different behavior from general-purpose LLM judges" — which is weaker and doesn't explicitly name "human-level judgment" as the aspirational target.  
**Lesson:** When discussing limitations, be explicit about what the gap means — name the challenging capability that's missing (human-level judgment, reasoning, fairness, etc.).

---

## PROBLEM 3: Three Mild Overclaims

### 3a. SClaim6 — "prompt-driven" for The AI Scientist [4]
**My claim:** "The AI Scientist [4] proposed a fully automated, prompt-driven pipeline."  
**Why overclaim:** The AI Scientist involves code execution, automated reviewing, and experiment iteration — calling it merely "prompt-driven" oversimplifies. It's a broader automated pipeline with multiple components beyond LLM prompting.  
**Lesson:** Be precise about what makes a system work. If a system uses prompts as one component but also has code execution, experiment design, and automated review, don't reduce it to "prompt-driven." Better: "LLM-driven automated pipeline" or "LLM-powered research framework."

### 3b. SClaim15 — Historical progression claim for [7]
**My claim:** "The field has since progressed through successive stages — from rule-based expert systems to neural network-driven data analysis — with surveys documenting the evolution toward increasingly autonomous discovery systems [6, 7]."  
**Why overclaim:** Citation [7] (Toward Building Science Discovery Machines) reviews ML approaches and discusses limitations but *does not explicitly chronicle* the full progression from rule-based to neural. The claim relies more heavily on [6] for the progression. Saying [7] supports this is a stretch.  
**Lesson:** When making a group citation [6, 7], ensure BOTH papers support the specific claim. [7] provides partial/implicit support — better to either cite [6] alone or use more precise language about what each paper contributes.

### 3c. SClaim21 — "substantially" for LLM-human overlap in [8]
**My claim:** "LLM-generated critiques can overlap substantially with human expert comments."  
**Why overclaim:** Liang et al. report overlap of 30.85% (Nature) and 39.23% (ICLR), which is comparable to human-human overlap (28.58% and 35.25%). The paper does NOT describe this as "substantial" in absolute terms. The word "substantially" implies a judgment that the paper itself doesn't make.  
**Lesson:** DO NOT add qualitative adjectives ("substantially", "significantly", "dramatically") unless the cited paper itself uses them. Stick to neutral descriptions: "LLM-generated critiques overlap with human expert comments at rates comparable to inter-human reviewer overlap."

---

## PROBLEM 4: Too Few Citations in Theme S2 (Science Discovery)

**Issue:** Paragraph S2 had only 2 citations ([6] and [7]) while the gold paragraph had 11 key citations spanning Langley, Buchanan, AlphaFold, LeCun, material discovery, mathematics, and AI4Science surveys.

**Root cause:** The Science Discovery theme in the ground truth references classical works (Langley 1987, Buchanan 1981) and domain-specific breakthroughs (AlphaFold, GNoME, FunSearch) that predate arXiv or are behind paywalls. These are not retrievable through DeepXiv. I compensated with two survey papers but couldn't match the ground truth's breadth.

**Lesson:** Under the clean search constraint, the Science Discovery theme is inherently hard to cover fully. But I should:
1. Search for MORE survey papers covering AI4Science broadly
2. Try domain-specific queries more aggressively (chemistry, biology, materials, math)
3. Even if I can't get all 11 citations, getting 4-5 would significantly improve coverage

---

## PROBLEM 5: Paragraph S1 Missing Surface-Level Strategy Labels

**What I wrote:** "ResearchAgent [1] introduced an iterative framework that generates research ideas grounded in scientific literature, using entity-centric knowledge stores and multi-agent peer review to refine outputs."

**What ground truth expects:** Explicit mention of "multi-agent collaborative writing" and "multi-module retrieval" as named research strategies.

**Lesson:** When multiple prior papers share a common approach strategy, name that strategy explicitly. The paper's own RW groups papers by strategy family first, THEN describes individual works. My RW did the reverse — I described individual works but missed the strategy label that unifies them.

---

## What Worked Well (Reinforcing)

1. **Theme discipline** — Stuck to 3 core themes from the paper's own RW. No tangential Preference Optimization or Text Detection paragraphs. Thematic structure scored 9.32.

2. **DeepXiv SDK usage** — Zero auth issues this time. Used `deepxiv-sdk` package correctly from the start.

3. **Title verification** — 11 of 12 references validated with exact title matches. Only [9] failed due to reference format, not incorrect title.

4. **Narrative arc** — Each paragraph had the prior→limitation→contribution arc. Synthesis quality scored 8.50.

5. **No invented papers** — All 12 papers were real and verified through DeepXiv brief().

6. **Author names** — Retrieved author lists via head() API. No author fabrications.

---

## Actionable Rules for Next Time

1. **Reference format**: ALWAYS include arXiv ID. Write `arXiv preprint arXiv:2401.04259, 2024.` not just `arXiv, 2024.`
2. **Strategy labels**: Before describing individual papers, name the high-level strategy families (multi-agent collaborative writing, multi-module retrieval, etc.)
3. **Overclaim prevention**: Replace "prompt-driven" with "LLM-powered" for systems that use more than just prompting. Never add qualitative adjectives the paper itself doesn't use. When citing two papers for one claim, verify BOTH support it fully.
4. **Broader context**: In each theme, establish the broader ecosystem before diving into specific sub-problems.
5. **Abstract specifics**: Extract concrete technical details from paper abstracts (e.g., "full-text PDFs" from Liang et al.) — these match ground truth specificity.
6. **Citation breadth for historical themes**: For themes like AI4Science that have deep historical roots, search for MORE survey papers and domain-specific reviews. Even 4-5 citations is better than 2.
7. **Missing paper search persistence**: If a specific named paper can't be found, try more author-specific queries and don't settle for superficially similar results.
