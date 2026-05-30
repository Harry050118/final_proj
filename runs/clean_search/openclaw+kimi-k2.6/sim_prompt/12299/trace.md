# Trace for 12299 Related Work Generation

## Inferred Paper Profile
- **Topic:** VLM-based mobile GUI agents with structured reasoning
- **Task:** Mobile GUI automation via Chain-of-Action-Thought (CoaT) reasoning
- **Method:** Iterative Preference Learning (IPL) — constructs CoaT-tree via iterative sampling, scores leaf nodes with rule-based reward, backpropagates feedback to form thinking-level DPO (T-DPO) pairs; plus three-stage instruction evolution for warm-up SFT diversity
- **Dataset type:** Mobile GUI trajectory datasets (AITZ, AMEX, AndroidControl)
- **Contribution:** Self-training framework for CoaT reasoning without process reward model annotations; instruction evolution to mitigate overfitting; state-of-the-art results on three mobile GUI benchmarks and strong OOD generalization

## Search Queries Used
1. `vision language model mobile GUI agent action planning`
2. `chain of thought reasoning GUI agent mobile`
3. `self-training preference optimization reasoning VLM`
4. `Monte Carlo Tree Search reasoning language model`
5. `Direct Preference Optimization DPO reasoning chain of thought`
6. `instruction evolution data augmentation VLM`
7. `GUI agent dataset AITW AndroidControl mobile benchmark`
8. `process reward model reasoning step annotation`
9. `reinforcement learning GUI agent GRPO self-play`
10. `OS-ATLAS UI-TARS continual pretraining GUI agent`
11. `CogAgent AutoGUI Shpagent GUI agent mobile`
12. `Qwen2-VL vision language model backbone`
13. `SPO-Chain MCTS reasoning self-training`
14. `Falcon-UI GUI grounding agent`

## Main Candidate Papers Considered
- CogAgent [1] — early VLM for GUI agents
- SeeClick [2] — GUI grounding pre-training
- OS-ATLAS [3] — continual pre-training foundation model
- UI-TARS [4] — native GUI agent with System-2 reasoning
- AITZ [5] — CoaT paradigm origin
- AITW [6] — large-scale Android dataset
- AMEX [7] — multi-annotation mobile GUI dataset
- Self-Training with DPO [8] — DPO for CoT reasoning
- Iterative Reasoning Preference Optimization [9] — iterative DPO for reasoning
- CPO [10] — tree-structured preference optimization for CoT
- TPO [11] — multi-branch preference trees
- PRM step-by-step [12] — process reward model
- CFPRM [13] — coarse-to-fine PRM
- ReST-MCTS* [14] — MCTS self-training without step annotations
- Mulberry [15] — collective MCTS for multimodal reasoning
- ARPO [16] — GRPO with experience replay for GUI agents
- MobileGUI-RL [17] — online RL for mobile GUI
- CRAFT-GUI [18] — curriculum RL for GUI tasks
- AndroidControl data scale [19] — data scaling and OOD generalization

## Final Cited Papers (19 references)
All 19 papers were selected because they directly address:
- VLM backbones and GUI grounding for mobile agents (1–4)
- CoaT reasoning and mobile GUI datasets (5–7)
- Self-training and preference optimization for reasoning (8–11)
- Process reward / tree-search alternatives to step annotation (12–15)
- RL-based GUI agent training (16–18)
- Data diversity and scaling in UI control (19)

## Uncertainty Notes
- Exact author lists for some 2024–2025 arXiv papers were abbreviated or inferred from brief metadata; full author lists should be verified if exact citation is required.
- The input paper mentions SphAgent and FedMobileAgent as baselines but these were not located via DeepXiv search; they were excluded to avoid unsupported citations.
- The input paper mentions GRPO and SPO-Chain as comparison methods; while ARPO and MobileGUI-RL cite GRPO, the exact SPO-Chain paper was not confidently identified via search and was therefore not cited.
- The input paper’s instruction evolution strategy is conceptually similar to general instruction-evolution literature (e.g., Evol-Instruct), but no single prior work exactly matches the three-stage GUI-specific evolution described; the related work therefore discusses the general principle without attributing it to a specific prior paper.