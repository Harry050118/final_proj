# Related Work Writing — Post-Mortem: sim_prompt+memory-evotest

**Date:** 2026-06-01  
**Score:** 6.24/10 (content_coverage: **0.53/10**)

## Overall Assessment

This was a significant failure, primarily driven by **missing an entire gold-standard Related Work theme** (Test-time scaling) and writing in a structure that diverged from the ground truth. Citation quality was excellent (citation_validity: 10.0, citation_appropriateness: 9.86, citation_topic_consistency: 10.0), but content coverage was catastrophically low.

---

## Problem 1: MISSING THE "TEST-TIME SCALING" THEME (Critical)

### What happened
The ground truth Related Work has **three** paragraphs:
1. **MLLMs as Evaluators** — (M)LLMs as judges, critics, reward models, value functions; multimodal focus; scoring/filtering trajectories; real-time feedback
2. **AI Agents** — web/mobile/computer agents; GPT-4V-based evaluators for Reflexion and behavior cloning; tree search, memory/tool generation, RL training
3. **Test-time scaling** — TTS paradigm; chain-of-thought prompting; multimodal and embodied CoT; scaling test-time compute via sampling/search; DeepSeek-R1, self-consistency, verifiers; need for flexible multimodal verification

I wrote **four** paragraphs and completely omitted the "Test-time scaling" theme.

### Why this happened
1. **I did not extract test-time scaling signals from the input paper body.** The paper body clearly discusses: "test-time scaling techniques," "chains-of-thought (CoT)," "majority voting," "techniques to mitigate biases in LLM judges," "test-time scaling is resilient to agreement bias." These are all strong signals that test-time scaling literature MUST be covered in Related Work.

2. **I focused too narrowly on the paper's explicit named references** (Reflexion, VWA, OSWorld, etc.) instead of inferring the full scope of the gold Related Work themes.

3. **I treated test-time scaling as an experimental detail** rather than a Related Work theme. This was a fundamental misjudgment: the abstract explicitly discusses test-time scaling, and the introduction positions the work against this literature.

### Root cause: Failure to comprehensively scan the entire body text for Related Work signals
The input paper mentions in the abstract: "This bias is pervasive across models, is resilient to test-time scaling, and can harm applications..." The paper also discusses Chain-of-Thought, majority voting, and other test-time scaling techniques throughout. I should have recognized these as mandatory Related Work themes.

### Corrective action
- **Before searching, create a comprehensive "Related Work signals" extraction from the FULL body text**, not just from the abstract and methodology sections.
- Look for signals beyond named paper references: concepts like "test-time scaling," "chain-of-thought," "process reward models," "search-based methods" are equally important signals.
- If the paper positions itself against a broad paradigm (e.g., "test-time scaling is resilient to..."), that paradigm MUST appear in Related Work.

---

## Problem 2: THEMATIC STRUCTURE MISMATCH (Serious)

### What happened
My 4-theme structure didn't match the gold 3-theme structure. Specifically:
- I made "Agent Self-Improvement" a standalone theme, but the ground truth subsumes Reflexion under "AI Agents"
- I made "Biases in LLM-based Evaluation" a standalone theme, but the ground truth subsumes biases under "MLLMs as Evaluators"

### Why this happened
I over-segmented the Related Work. Two of my themes (Self-Improvement, Biases) should have been integrated into the main themes rather than being standalone. The ground truth uses larger, more cohesive paragraphs that each cover multiple related concepts.

### Corrective action
- Aim for 3-4 paragraphs that are broadly scoped, not narrowly focused on one paper each.
- Each paragraph should cover multiple related subtopics, not just list papers.
- When a subtopic has only 1-2 papers, it should be folded into a broader theme.

---

## Problem 3: LENGTH INFLATION (Serious)

### What happened
- My Related Work: **623 words**
- Ground truth: **278 words**
- Ratio: **2.24x** (evaluator flagged this as excessive)

### Why this happened
1. I was too verbose in describing individual paper contributions. Each paper got a full sentence with many details.
2. The ground truth is notably dense and concise — it uses citations freely without over-describing what each paper does.
3. I included expanded descriptions of benchmarks (WebArena's 812 tasks, OSWorld's 369 tasks, 12.24% success rate) that are unnecessary in a Related Work section.

### Corrective action
- **Target 250-350 words for Related Work sections**, not 500-600.
- Be dense and concise. Use citations freely without expanding every paper's contributions.
- Mention benchmark details sparingly — a brief description is sufficient.
- After writing, ALWAYS check word count against a 350-word budget.

---

## Problem 4: MISSING KEY CITATIONS (Serious)

### What happened
The ground truth cites many papers I didn't find or include:
- Pan et al. (2024) — "Autonomous Evaluation and Refinement of Digital Agents" — GPT-4V evaluator for Reflexion
- Koh et al. (2024) — "Tree Search for Language Model Agents" — tree search for web agents
- Wang et al. (2024) — "Agent Workflow Memory" — trajectory filtering for memories/tools
- DigiRL (Bai et al. 2024) — RL training with VLM evaluators
- Chain-of-thought papers: Wei et al. (2022), Kojima et al. (2022), Zhang et al. (2023)
- Test-time scaling: Snell et al. (2024), Welleck et al. (2024)
- Verifiers: Lightman et al. (2023), DeepSeek-R1, Kimi k1.5
- Tree of Thoughts (Yao et al. 2023), Self-consistency (Wang et al. 2022)

### Why this happened
1. **I didn't generate search queries targeting the "test-time scaling" theme** because I missed it entirely.
2. **My search queries were too broad** — I needed targeted searches like "autonomous evaluation refinement digital agents" to find Pan et al.
3. **I didn't search for canonical "test-time scaling" or "chain-of-thought" papers** because I didn't recognize them as Related Work topics.

### Corrective action
- After extracting the paper profile and signals, generate targeted search queries for EACH signal type.
- For "chain-of-thought," "test-time scaling," "process rewards," etc., search for the canonical papers in those areas.
- If the paper discusses a method (e.g., Reflexion), search for papers that USE that method in related settings (e.g., "Reflexion web agent tree search").

---

## Problem 5: DUPLICATE SENTENCE STRUCTURE (Minor)

### What happened
The evaluator flagged S3_sent2 ("Shinn et al.") and S4_sent2 ("Shi et al.") as having 0.90 similarity — caused by adjacent paragraphs with identical sentence structures ("Author et al. [N] introduced/proposed..."). This is a writing quality issue.

### Corrective action
- Vary sentence openers across paragraphs. Don't use "Author et al. [N] introduced..." as the default sentence structure.
- Use passive voice, transition phrases, and contextual framing to break repetitive patterns.

---

## What Went Well

1. **Citation validity: 10.0/10** — All 12 citations were verified as valid, with no hallucinated references.
2. **Citation appropriateness: 9.86/10** — Nearly all citations were appropriate.
3. **Citation placement: 10.0/10** — Citations were correctly placed.
4. **Citation topic consistency: 10.0/10** — All cited papers match the topics they were cited for.
5. **No hallucinated references** — Zero invented papers.

---

## Incident Prevention Checklist

Before writing any future Related Work section, I MUST:

1. ✅ Read the ENTIRE visible input (not just abstract/intro) and extract ALL Related Work signals — both named papers AND broad concepts/paradigms.
2. ✅ Check: does the paper discuss "test-time scaling," "chain-of-thought," "search," "self-consistency," "process reward models," "RLHF," "reasoning"? If so, these are mandatory themes.
3. ✅ Map each signal to a theme BEFORE searching.
4. ✅ Generate search queries for ALL themes, not just the obvious ones.
5. ✅ Target 250-350 words for the final section.
6. ✅ Use 3-4 broadly-scoped paragraphs, not narrow ones.
7. ✅ Vary sentence structures to avoid duplicate patterns.
8. ✅ After writing, verify: does every signal from the paper body have a theme that covers it?
