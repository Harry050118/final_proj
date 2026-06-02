# DeepXiv Search Trace — MobileIPL Related Work (Paper 12299)

## Inferred Paper Profile

- **Topic:** VLM-based Mobile GUI Agents with Iterative Preference Learning
- **Task:** Autonomous mobile GUI interaction and action reasoning
- **Method:** MobileIPL — Iterative Preference Learning framework with CoaT-tree (MCTS-based iterative sampling), rule-based rewards without PRMs, Thinking-level DPO (T-DPO) with backward credit assignment, and three-stage instruction evolution to prevent SFT overfitting
- **Backbone:** Qwen2-VL-7B
- **Datasets:** AITZ (CoaT trajectories), AMEX (long-horizon), AndroidControl (OOD generalization)
- **Baselines:** CogAgent, Auto-GUI, SphAgent, OS-Atlas, UGround, UI-TARS, FedMobileAgent, Falcon-UI

## Previous Postmortem Lessons Applied

From `memory/2026-06-01_related_work_postmortem.md` (run 2, score 6.89) and `memory/2026-06-01_related_work_postmortem_run3.md` (run 3, score 6.73):

1. **Two-theme structure:** Mobile GUI Agent + RL/Preference Optimization (not 4 narrow themes)
2. **No overclaims:** TCPO "introduces APC" not "enforces"; ReachAgent uses "reward-based preference learning" not "DPO"; CoaT "structures reasoning" not "decomposes"
3. **No packed claims:** Each claim has its own citation verification
4. **Synthesize not enumerate:** Organized around common limitations, not paper-by-paper catalog
5. **Target ~350-450 words:** Kept compact with 15 citations
6. **Explicit method positioning:** Final sentence states what gaps MobileIPL fills
7. **Searched specifically for named missed papers:** Digirl→MobileRL, DistRL, ReachAgent, TCPO, Xie et al., ReFT

## Search Queries (DeepXiv via `deepxiv_sdk.Reader.search`)

### Batch 1: Mobile GUI Agents
- "VLM vision language model mobile GUI agent autonomous smartphone" (10 results)
- "mobile GUI grounding agent vision language model screen" (10 results)
- "CogAgent visual grounding GUI agent" (5 results)
- "OS-Atlas GUI agent foundation model" (5 results)
- "UI-TARS GUI agent visual grounding" (5 results)
- "SeeClick GUI grounding mobile agent" (5 results)
- "Auto-GUI mobile agent autonomous navigation" (5 results)
- "GPT-4V mobile GUI agent smartphone task" (5 results)
- "chain of action thought reasoning mobile GUI" (5 results)
- "AITW Android in the wild dataset mobile GUI agent" (5 results)

### Batch 2: RL / Preference Optimization
- "DPO direct preference optimization alignment" (5 results)
- "IPO KTO preference optimization alignment" (5 results)
- "ReFT reinforcement learning fine-tuning reasoning math" (5 results)
- "ReST-MCTS tree search process reward reasoning" (5 results)
- "MCTS iterative preference learning reasoning" (5 results)
- "Step-DPO preference optimization step-level reasoning" (5 results)
- "GRPO group relative policy optimization reasoning" (5 results)
- "SPO self-play optimization chain reasoning" (5 results)
- "TreeRL tree reinforcement learning reasoning chain" (5 results)
- "TreePO tree preference optimization" (5 results)

### Batch 3: Specific Missed Papers
- "Digirl reinforcement learning GUI mobile agent" (5 results) → found MobileRL, MobileGUI-RL, SWIRL, CRAFT-GUI
- "Distrl mobile agent reinforcement learning" (5 results) → found DistRL
- "ReachAgent mobile agent page reaching operation" (5 results) → found ReachAgent
- "TCPO thought-centric preference optimization" (5 results) → found TCPO
- "Xie et al MCTS preference labeling iterative preference learning" (5 results) → found Xie et al. (2405.00451)

### Direct Lookups
- `brief("2305.18290")` → DPO (Rafailov et al.)
- Searched "Direct Preference Optimization Rafailov 2023" → confirmed via brief

## Main Candidate Papers (verified via brief/head)

Total unique papers from all searches: 112. Verified 39 papers via `brief` and `head` endpoints.

## Final Cited Papers (15)

| # | Paper | ID | Theme |
|---|-------|-----|-------|
| 1 | MM-Navigator (GPT-4V) | 2311.07562 | GUI Agents |
| 2 | CogAgent | 2312.08914 | GUI Agents |
| 3 | SeeClick | 2401.10935 | GUI Agents |
| 4 | OS-Atlas | 2410.23218 | GUI Agents |
| 5 | UI-TARS | 2501.12326 | GUI Agents |
| 6 | CoaT / AITZ | 2403.02713 | GUI Agents |
| 7 | DPO (Rafailov et al.) | 2305.18290 | RL/Preference |
| 8 | ReFT | 2401.08967 | RL/Preference |
| 9 | ReST-MCTS* | 2406.03816 | RL/Preference |
| 10 | Xie et al. (MCTS+IPL) | 2405.00451 | RL/Preference |
| 11 | Step-DPO | 2406.18629 | RL/Preference |
| 12 | TPO | 2410.12854 | RL/Preference |
| 13 | TreeRL | 2506.11902 | RL/Preference |
| 14 | ReachAgent | 2502.02955 | RL/Preference |
| 15 | TCPO | 2509.08500 | RL/Preference |

## Uncertainty Notes

- ReFT (2401.08967) is verified as a math reasoning paper using PPO-based RL; its applicability to GUI domains is inferred by the input paper's own discussion
- The CoaT paper (2403.02713) authors differ slightly between what was found in head vs. the paper's own reference — used the head endpoint data
- UI-TARS has 43+ authors; used "et al." after first 12 names
- Did not find specific "Digirl" paper in search results; the closest matches were MobileGUI-RL, MobileRL, and SWIRL which represent the same online RL approach for GUI agents
- All 15 papers verified via DeepXiv `brief` or `head` endpoints — zero hallucinated references
