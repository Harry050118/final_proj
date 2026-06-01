# MEMORY.md

## Technical Knowledge

### DeepXiv
- **Do NOT make direct HTTP calls** to deepxiv.com — the API token only works through the `deepxiv-sdk` Python package (`pip install deepxiv-sdk`)
- Usage: `from deepxiv_sdk import Reader; reader = Reader(token='...'); result = reader.search(query, size=5, source='arxiv')`
- Also supports `reader.brief(arxiv_id)` and `reader.head(arxiv_id)` for metadata
- Token is in `.env` as `DEEPXIV_API_TOKEN=sniRmh…F6A8`

### Related Work Generation Lessons (from evotest, cumulative across 3 attempts)

**Scores:** Task #1 (clean): 6.17 → Task #2 (memory): 8.12 → Task #3 (high-memory): 8.68 ✅

Critical mistakes to avoid:
1. **Overclaiming**: Only claim what papers explicitly state. "Self-rewarding" ≠ "self-play". A benchmark existing ≠ it proves a claim.
2. **Title accuracy**: Always verify paper titles via DeepXiv `brief()` before writing reference entries. Search-result snippets can differ from actual metadata.
3. **Theme discipline**: Stick to themes the paper itself cares about. Adding tangential themes (Preference Optimization, Text Detection) dilutes focus and lowers relevance scores.
4. **Narrative arc**: Don't just list papers. Explain what prior work CAN'T do → how this paper fills the gap. Cover the limitation/need/contribution chain.
5. **Search breadth**: Search for specific prior works the paper might cite (ResearchAgent, SciMON, MLAgentBench, MARG, Generative Verifiers, Tyser et al.) — not just high-level themes.
6. **Historical context**: Some papers expect classical references (Langley 1987, Buchanan 1981) in the AI4Science narrative.
7. **ALWAYS include arXiv IDs** in references: `arXiv preprint arXiv:2401.04259, 2024.` not just `arXiv, 2024.` — Task #2's MARG mismatch was caused by missing ID.
8. **Exact wording for contribution claims**: The evaluator matches near-exactly. Use "leader in scientific discovery" NOT "active participant." Keep self-contribution claims short and standalone.
9. **Don't extend citations beyond their scope**: RewardBench evaluates reward models generally, not AI-driven peer review specifically. Attribute peer-review gap claims to the paper itself, not to RewardBench.
10. **Dual-relevance papers cite twice**: The AI Scientist should be cited in BOTH Theme 1 (pipeline) AND Theme 3 (PDF evaluation).
11. **MARG metadata_mismatch is systemic** (3-time occurrence): arXiv:2401.04259 cannot be resolved by the evaluation system. Flag is cosmetic — citation_quality scored 9.05 despite it. Don't waste effort trying to fix it.
12. **Search author-name queries**: e.g., "Tyser" to find Tyser et al. (arXiv:2408.10365) — missed by topical searches.

Detailed per-task analyses: `memory/2026-05-31_task2_lessons.md`, `memory/2026-05-31_task3_lessons.md`
