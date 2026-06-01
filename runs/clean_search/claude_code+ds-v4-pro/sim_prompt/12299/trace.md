# Related Work Generation Trace — Paper 12299

## Inferred Research Topic

**Mobile GUI Agent with Iterative Preference Learning (MobileIPL):** A VLM-based mobile GUI agent that uses Chain of Action-Planning Thoughts (CoaT), iterative sampling in a CoaT-tree with rule-based rewards, and Thinking-level DPO (T-DPO) for reasoning optimization. Includes a three-stage instruction evolution strategy using GPT-4o on real mobile UI screenshots. Evaluated on AITZ, AMEX, and AndroidControl benchmarks using Qwen2-VL-7B as backbone.

**Key method components:**
1. CoaT multi-turn thinking (Description → Action-Thought → Action-Decision → Grounding)
2. Instruction Evolution (3-level Q&A generation on UI screenshots)
3. Iterative Preference Learning (CoaT-tree sampling + rule-based reward + T-DPO)
4. Self-training framework without expensive process-level annotations

## Search Queries Used (DeepXiv)

1. `mobile GUI agent vision language model` — broad search for VLM GUI agents
2. `chain of thought action plan GUI agent mobile reasoning` — CoaT/CoT papers for GUI
3. `direct preference optimization DPO reasoning LLM self-training process reward` — DPO for reasoning
4. `monte carlo tree search MCTS LLM reasoning self-training iterative sampling` — MCTS reasoning methods
5. `Android in the Wild AITW GUI agent benchmark mobile dataset` — datasets/benchmarks
6. `OS-ATLAS GUI grounding agent pretraining` — specific baseline model
7. `UI-TARS GUI agent continual pretraining` — specific baseline model
8. `CogAgent visual GUI agent mobile` — specific baseline model
9. `AUTO-GUI autonomous GUI agent` — specific baseline model
10. `GUI agent instruction data augmentation evolution` — instruction evolution
11. `Qwen2-VL vision language model mobile agent` — backbone model
12. `GRPO group relative policy optimization GUI agent` — RL comparison method
13. `WizardLM Evol-Instruct instruction evolution data augmentation LLM` — instruction evolution origin
14. `direct preference optimization DPO Rafailov language model` — original DPO paper
15. `process reward model PRM LLM reasoning step-level` — PRM-related work
16. `AndroidControl dataset GUI agent OOD benchmark` — AndroidControl dataset
17. Target searches for specific arXiv IDs to retrieve author/venue details

## Main Candidate Papers Found

| arXiv ID | Title | Relevance |
|----------|-------|-----------|
| 2312.08914 | CogAgent: A Visual Language Model for GUI Agents | VLM GUI agent baseline |
| 2401.16158 | Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent | Mobile GUI agent baseline |
| 2309.11436 | You Only Look at Screens: Multimodal Chain-of-Action Agents | AUTO-GUI, chain-of-action |
| 2410.23218 | OS-ATLAS: A Foundation Action Model for Generalist GUI Agents | Continual pretraining baseline |
| 2501.12326 | UI-TARS: Pioneering Automated GUI Interaction with Native Agents | Continual pretraining baseline |
| 2412.09362 | Falcon-UI: Understanding GUI Before Following User Instructions | GUI pretraining baseline |
| 2410.05243 | UGround: Universal Visual Grounding for GUI Agents | GUI grounding baseline |
| 2403.02713 | Android in the Zoo: Chain-of-Action-Thought for GUI Agents | CoAT/AITZ — core CoaT paradigm |
| 2503.16788 | Does Chain-of-Thought Reasoning Help Mobile GUI Agent? | Empirical CoT study |
| 2305.18290 | DPO: Your Language Model is Secretly a Reward Model | Foundational DPO |
| 2405.00451 | MCTS Boosts Reasoning via Iterative Preference Learning | MCTS + DPO for reasoning |
| 2406.03816 | ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search | PRM + MCTS self-training |
| 2407.18248 | Self-Training with DPO Improves CoT Reasoning | DPO self-training for CoT |
| 2501.12948 | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL | GRPO-based reasoning |
| 2502.14356 | Full-Step-DPO: Self-Supervised Preference Optimization with Step-wise Rewards | Step-level DPO |
| 2304.12244 | WizardLM: Empowering LLMs to Follow Complex Instructions | Evol-Instruct origin |
| 2307.10088 | Android in the Wild: A Large-Scale Dataset for Android Device Control | AITW dataset |
| 2407.17490 | AMEX: Android Multi-annotation Expo Dataset for Mobile GUI Agents | AMEX dataset |
| 2406.03679 | On the Effects of Data Scale on UI Control Agents | AndroidControl dataset |
| 2409.12191 | Qwen2-VL: Enhancing VLM's Perception at Any Resolution | Backbone model |

## Final Cited Papers (20 papers)

Organized into 4 themes:
1. **VLM-based Mobile GUI Agents** [1–7]: CogAgent, Mobile-Agent, AUTO-GUI, OS-ATLAS, UI-TARS, Falcon-UI, UGround
2. **Chain-of-Thought Reasoning for GUI Agents** [8–9]: AITZ/CoAT, Empirical CoT study
3. **Self-Training via Preference Optimization for Reasoning** [10–15]: DPO, MCTS+Pref, ReST-MCTS*, Self-Training DPO, DeepSeek-R1, Full-Step-DPO
4. **Instruction and Data Augmentation Strategies** [16–20]: WizardLM, AITW, AMEX, AndroidControl, Qwen2-VL

## Uncertainty Notes

- **SphAgent/Shpagent:** Listed as a baseline in the paper ("Shpagent" and "SphAgent-7B") but could not be located via DeepXiv search. May be published under a different title or venue. Not cited.
- **FedMobileAgent:** Listed as a baseline but could not be located. Not cited.
- **SPO-Chain:** Mentioned in the rollout efficiency comparison but not independently verified. Not cited.
- **GRPO original paper (DeepSeekMath, arXiv:2402.03300):** Verified to exist; cited DeepSeek-R1 (arXiv:2501.12948) instead as it popularized GRPO for reasoning and is more directly relevant.
- Author names were extracted from DeepXiv search results. For [15] Full-Step-DPO, author extraction was incomplete — the reference uses the verified title and arXiv ID.

## Search Transparency

- All searches conducted via DeepXiv SDK (`deepxiv_sdk.Reader.search()`)
- Source: `arxiv` for all queries
- Search size: 5–10 results per query
- Paper details verified via `reader.brief()` and search result metadata
- No external search engines, arXiv direct search, Semantic Scholar, Google Scholar, or memory-only discovery used
