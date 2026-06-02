# Trace: Related Work Generation for Paper 12299

## Inferred Paper Profile

- **Topic:** VLM-based Mobile GUI Agents with Iterative Preference Learning
- **Task:** Autonomous mobile GUI interaction — executing user instructions by interacting with smartphone interfaces
- **Method:** MobileIPL — Iterative Preference Learning framework combining (1) three-stage instruction evolution for warm-up SFT, (2) CoaT-tree construction via MCTS-style iterative sampling, (3) rule-based reward with backward credit assignment, and (4) Thinking-level Direct Preference Optimization (T-DPO)
- **Backbone Model:** Qwen2-VL-7B
- **Datasets/Benchmarks:** AITZ (Chain-of-Action-Thought), AMEX (long-horizon), AndroidControl (OOD generalization)
- **Key Baselines:** CogAgent, Auto-UI, SphAgent, OS-ATLAS, UGround, UI-TARS, Falcon-UI, FedMobileAgent
- **Novelty:** Replaces expensive PRM-based process supervision with rule-based rewards on a CoaT-tree; uses multi-turn dialogue decomposition of reasoning steps; applies instruction evolution to prevent SFT overfitting

## Search Queries

1. `mobile GUI agent vision language model autonomous interaction smartphone` — 15 results
2. `chain of thought reasoning GUI grounding visual agent action planning` — 15 results
3. `direct preference optimization DPO reasoning steps language model` — 15 results
4. `Monte Carlo tree search MCTS reasoning language model self-training process reward model` — 15 results
5. `OS-Atlas GUI grounding visual agent pretraining user interface` — 10 results
6. `AITW Android in the Wild mobile GUI dataset benchmark action prediction` — 10 results
7. `CogAgent visual agent GUI understanding foundation model` — 5 results
8. `self-training iterative preference learning reasoning VLM vision language model` — 10 results
9. `DPO Direct Preference Optimization Rafailov language model alignment` — 5 results
10. `Direct Preference Optimization Your Language Model is Secretly a Reward Model Rafailov` — 5 results
11. `Qwen2-VL vision language model multimodal understanding` — 5 results
12. `SPO self-play optimization chain of thought reasoning preference` — 5 results
13. `Auto-GUI GUI agent autonomous action prediction function calling` — 5 results
14. `GRPO group relative policy optimization reinforcement learning LLM reasoning` — 5 results
15. `Falcon-UI GUI agent vision language model Android grounding` — 5 results
16. `AutoGUI autonomous GUI agent MLLM function call action space` — 5 results
17. `AndroidControl benchmark mobile GUI agent high low level control` — 5 results
18. `"SPO" "self-play" chain reasoning optimization preference tree language model` — 5 results
19. `SphAgent Shpagent mobile agent model hierarchical planning GUI task` — 5 results
20. `DeepSeek-R1 GRPO reinforcement learning reasoning chain of thought` — 5 results
21. `Tree of Thoughts deliberate problem solving language model Yao` — 3 results

Additionally, briefs/metadata were retrieved for 17 specific papers to verify relevance and extract details.

## Main Candidate Papers Considered

- 2404.08755 — Training a Vision Language Model as Smartphone Assistant
- 2312.13771 — AppAgent: Multimodal Agents as Smartphone Users
- 2401.16158 — Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent
- 2403.02713 — Android in the Zoo: Chain-of-Action-Thought for GUI Agents (AITZ)
- 2501.12326 — UI-TARS: Pioneering Automated GUI Interaction
- 2407.04346 — MobileFlow: A Multimodal LLM for Mobile GUI Agent
- 2505.00416 — ScaleTrack: Scaling and Back-tracking Automated GUI Agents
- 2507.05791 — GTA1: GUI Test-time Scaling Agent
- 2412.04454 — Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction
- 2503.16788 — Does Chain-of-Thought Reasoning Help Mobile GUI Agent?
- 2505.00684 — Visual Test-time Scaling for GUI Agent Grounding
- 2505.15810 — GUI-G1: Understanding R1-Zero-Like Training for Visual Grounding
- 2406.18629 — Step-DPO: Step-wise Preference Optimization for Long-chain Reasoning
- 2410.12854 — TPO: Aligning LLMs with Multi-branch & Multi-step Preference Trees
- 2407.18248 — Self-Training with Direct Preference Optimization Improves CoT Reasoning
- 2406.03816 — ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search
- 2405.00451 — Monte Carlo Tree Search Boosts Reasoning via Iterative Preference Learning
- 2412.15797 — Ensembling LLMs with Process Reward-Guided Tree Search
- 2501.01478 — Enhancing Reasoning through Process Supervision with MCTS
- 2410.23218 — OS-ATLAS: A Foundation Action Model for Generalist GUI Agents
- 2401.10935 — SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents
- 2406.11317 — GUICourse: From General Vision Language Models to Versatile GUI Agents
- 2410.05243 — Navigating the Digital World as Humans Do (UGround)
- 2312.08914 — CogAgent: A Visual Language Model for GUI Agents
- 2309.11436 — You Only Look at Screens: Multimodal Chain-of-Action Agents (Auto-UI)
- 2307.10088 — Android in the Wild: A Large-Scale Dataset for Android Device Control
- 2407.17490 — AMEX: Android Multi-annotation Expo Dataset for Mobile GUI Agents
- 2406.03679 — On the Effects of Data Scale on UI Control Agents (AndroidControl)
- 2305.18290 — Direct Preference Optimization (Rafailov et al.)
- 2409.12191 — Qwen2-VL: Enhancing Vision-Language Model's Perception
- 2406.09136 — Chain of Preference Optimization (CPO / SPO-Chain)
- 2501.12948 — DeepSeek-R1
- 2412.09362 — Falcon-UI: Understanding GUI Before Following User Instructions
- 2305.10601 — Tree of Thoughts (Yao et al.)
- 2411.18279 — Large Language Model-Brained GUI Agents: A Survey

## Final Cited Papers (21)

1. AITW (Rawles et al., 2023) — Android in the Wild dataset
2. CogAgent (Hong et al., 2023) — GUI visual language model
3. AppAgent (Zhang et al., 2023) — Multimodal agents for smartphones
4. Auto-UI (Zhang & Zhang, 2023) — Chain-of-action agents
5. SeeClick (Cheng et al., 2024) — GUI grounding pre-training
6. UGround (Cheng et al., 2024) — Universal visual grounding
7. OS-ATLAS (Wu et al., 2024) — Foundation action model
8. UI-TARS (Qin et al., 2025) — Native GUI agent
9. Falcon-UI (Liu et al., 2024) — Decoupled GUI understanding
10. AMEX (Chai et al., 2024) — Multi-annotation dataset
11. AndroidControl (Li et al., 2024) — Data scale study
12. AITZ/CoaT (Zhang et al., 2024) — Chain-of-Action-Thought
13. CoT-Mobile (Li et al., 2025) — Empirical study of CoT for GUI
14. DPO (Rafailov et al., 2023) — Direct Preference Optimization
15. Step-DPO (Lai et al., 2024) — Step-wise preference optimization
16. DeepSeek-R1 (Guo et al., 2025) — RL for reasoning
17. GUI-G1 (Zhou et al., 2025) — R1-Zero-like training for GUI
18. Tree of Thoughts (Yao et al., 2023) — MCTS for LLM reasoning
19. MCTS-DPO (Xie et al., 2024) — MCTS + iterative preference learning
20. ReST-MCTS* (Zhang et al., 2024) — Process reward guided tree search
21. CPO (Chen et al., 2024) — Chain of Preference Optimization

## Papers NOT Found via DeepXiv

- **SphAgent / Shpagent**: Could not find a specific paper matching this baseline name. Not cited.
- **AUTO-GUI** (exact match): Could not find a paper with this exact name. Auto-UI (2309.11436) was found and cited instead; may be the same baseline referenced under a different name.
- **FedMobileAgent**: Could not locate via DeepXiv. Not cited.
- **Qwen2-VL**: Found (2409.12191). Referenced as the backbone model in the text but not formally cited as the paper does not discuss VLM architecture choices.

## Uncertainties

1. **Author names for some papers**: Some author lists were extracted from DeepXiv briefs which may not be complete. Verified where possible through metadata lookups.
2. **AUTO-GUI vs Auto-UI**: The paper mentions "AUTO-GUI" as a baseline, but DeepXiv searches only returned Auto-UI (2309.11436) by Zhang & Zhang. These may refer to the same system, though this cannot be confirmed without the original reference list.
3. **SPO-Chain**: The paper mentions comparing against "SPO-Chain." DeepXiv searches suggest this maps to "Chain of Preference Optimization" (CPO, 2406.09136), which uses a similar tree-based preference construction approach.
4. **SphAgent**: Not found on DeepXiv. The paper cites this as a prior SOTA model on AMEX. Its absence from the citation list may be a limitation.
