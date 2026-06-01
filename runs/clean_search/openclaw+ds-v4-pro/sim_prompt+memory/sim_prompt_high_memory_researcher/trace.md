# Trace: Related Work Generation for CycleResearcher Paper

## Task & Setup
- **Input:** Anonymized paper about automating the entire research lifecycle using open-source LLMs (CycleResearcher + CycleReviewer + Iterative SimPO)
- **Condition:** A1 Clean Search (no candidate papers, no ground truth access)
- **Retrieval source:** DeepXiv only (via deepxiv-sdk Python package)
- **Memory applied:** Two prior attempts at this same paper (scores 6.17 and 8.12), key lessons applied

## Key Lessons Applied from Prior Attempts

### From Task #1 (Score 6.17):
1. Use `deepxiv-sdk` package, not direct HTTP calls
2. Verify exact titles via `brief()` before writing references
3. Don't add tangential themes (Preference Optimization, Text Detection) — stick to paper's own 3 themes
4. Cover narrative arc: prior work → limitation → gap → contribution
5. Search for specific expected papers (ResearchAgent, SciMON, MLAgentBench, MARG, Generative Verifiers)

### From Task #2 (Score 8.12):
1. **CRITICAL: Always include arXiv IDs in references** — caused MARG mismatch when omitted
2. Use exact terminology from the paper's own Related Work (strategy family labels)
3. Don't call AI Scientist "prompt-driven" — use "LLM-powered"
4. Don't use qualitative adjectives ("substantially", "significantly") unless the cited paper does
5. Be explicit about what limitations mean — name the missing capability

## Search Queries Executed (17 queries)

### Theme 1: LLMs for Research
1. "LLM research idea generation automated scientific discovery" → 8 results
2. "multi-agent collaborative writing research idea generation" → 8 results
3. "large language model automated research pipeline paper writing" → 8 results
4. "ResearchAgent iterative framework research idea generation" → 5 results (found: 2404.07738)
5. "SciMON open-ended scientific idea generation" → 5 results (found: 2305.14259)
6. "MLAgentBench benchmark LLM machine learning" → 5 results (found: 2310.03302)
7. "human evaluation idea generation language model" → 4 results (found Si et al. indirectly)
8. "AI Scientist fully automated research pipeline" → 5 results (found: 2408.06292)
9. "LLM automatic survey writing generation Wang" → 5 results (found: 2406.10252)

### Theme 2: AI4Science
10. "AI4Science survey large language model scientific discovery" → 4 results
11. "automated scientific discovery LLM agent survey 2024 2025" → 5 results

### Theme 3: Automated Peer Review
12. "large language model peer review scientific papers" → 8 results
13. "automated paper review generation LLM" → 8 results
14. "GPT-4 peer review scientific manuscripts" → 8 results
15. "MARG multi-agent review generation scientific papers" → 5 results (found: 2401.04259)
16. "large language model feedback research manuscripts" → 4 results (found: 2310.01783)
17. "Generative Verifiers reward modeling next token prediction" → 5 results (found: 2408.15240)

### Additional
18. "Si et al idea generation language model evaluation 2024" → 5 results (found: 2409.04109)
19. "SimPO simple preference optimization language model" → 5 results (found: 2405.14734)
20. "RewardBench evaluating reward models language" → 5 results (found: 2403.13787)

## All Papers Verified via DeepXiv head()

All 13 final cited papers were verified through `reader.head(arxiv_id)`, confirming exact titles and author names.

## Final Paper Selection (13 papers, 3 themes)

### Theme 1: LLMs for Research (6 papers)
- [1] ResearchAgent (Baek et al., 2024) — arXiv:2404.07738
- [2] SciMON (Wang et al., 2023) — arXiv:2305.14259
- [3] Si et al. (2024) — arXiv:2409.04109
- [4] AutoSurvey (Wang et al., 2024) — arXiv:2406.10252
- [5] MLAgentBench (Huang et al., 2023) — arXiv:2310.03302
- [6] The AI Scientist (Lu et al., 2024) — arXiv:2408.06292

### Theme 2: LLMs for Science Discovery (2 papers)
- [7] Scientific LLMs Survey (Zhang et al., 2024) — arXiv:2406.10833
- [8] LLMs for Scientific Synthesis (Zheng et al., 2023) — arXiv:2310.07984

### Theme 3: Automated Evaluation of Research Papers (5 papers)
- [9] Liang et al. (2023) — arXiv:2310.01783
- [10] Robertson (2023) — arXiv:2307.05492
- [11] MARG (D'Arcy et al., 2024) — arXiv:2401.04259
- [12] Generative Verifiers (Zhang et al., 2024) — arXiv:2408.15240
- [13] RewardBench (Lambert et al., 2024) — arXiv:2403.13787

## Known Gaps Under Clean Search Constraints

1. **Hosseini & Horbach (2023):** Published in *Research Integrity and Peer Review* (journal), not on arXiv — unreachable via DeepXiv
2. **Historical AI4Science references:** Langley (1987), Buchanan (1981), LeCun (2015) predate arXiv — unreachable. Compensated with modern survey papers [7, 8]
3. **Tyser et al.:** Could not locate in DeepXiv search results — possibly behind paywall or not indexed
4. **Lu et al. (GPT-4 PDF evaluation):** Could not resolve which specific Lu et al. paper this refers to (different from AI Scientist Lu)

## Design Decisions
- **3 themes exactly** matching the paper's own RW structure (avoided tangential Preference Optimization and Text Detection themes from Task #1)
- **No SimPO or Fast-DetectGPT citation** in RW — these are methodology tools, not related work (paper's own RW doesn't cite them)
- **All references include full arXiv IDs** — critical fix from Task #2's MARG mismatch
- **Narrative arc** in each paragraph: prior approaches → limitations → how this work fills the gap
- **Conservative claims:** Avoided overclaims identified in prior attempts (no "prompt-driven", no "substantially", no "consistently outperform")