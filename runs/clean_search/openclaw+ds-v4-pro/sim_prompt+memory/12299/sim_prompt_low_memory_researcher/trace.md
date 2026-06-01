# Related Work Generation Trace — Paper 12299 (MobileIPL)

## Inferred Paper Topic
- **Topic:** VLM-based Mobile GUI Agents with Chain-of-Action-Thought (CoaT) reasoning
- **Method:** Iterative Preference Learning (IPL) framework: MCTS-based CoaT-tree construction, rule-based rewards with backward credit assignment, Thinking-level DPO (T-DPO), three-stage instruction evolution
- **Datasets:** AITZ, AMEX, AndroidControl
- **Backbone:** Qwen2-VL-7B
- **Contributions:** (1) CoaT-tree + rule-based rewards + T-DPO for reasoning optimization without PRMs, (2) instruction evolution to prevent SFT overfitting, (3) SOTA on three benchmarks, surpassing continual pretraining models

## Lessons Applied from Previous Run (Postmortem: 6.89/10)
1. **Search for ALL named comparison methods explicitly:** Ran dedicated queries for SPO, TreeRL, ReFT, ReachAgent, TCPO, GRPO, ReST-MCTS
2. **Cover closed-source approaches:** Included GPT-4V in Wonderland [7] as early closed-source VLM agent
3. **Verify limitations before claiming:** Checked TLDRs of all cited papers — no overclaims about paper limitations
4. **Use precise terminology:** Used "GRPO," "DPO," "RL" precisely, not "preference optimization" generically
5. **Synthesize, don't enumerate:** Each paragraph organized around shared methods/limitations, closing with gap
6. **Target word count:** 464 words (vs 707 in previous run; ground truth ~345)
7. **Method positioning:** Final paragraph explicitly states gaps and how proposed method addresses them

## Search Queries (35 queries across 6 batches)
### Batch 1: Core VLM GUI Agents
- "CogAgent visual language model mobile GUI agent"
- "OS-Atlas GUI grounding visual agent"
- "UI-TARS mobile GUI agent vision language model"
- "autonomous GUI agent VLM mobile device"
- "Falcon-UI GUI agent vision language model"
- "UGround GUI grounding visual agent"
- "FedMobileAgent mobile GUI federated"

### Batch 2: CoaT / CoT for GUI
- "chain of action planning thoughts CoaT GUI agent"
- "AITZ AITW mobile GUI agent dataset trajectories"
- "multi-turn thinking reasoning GUI agent VLM"
- "chain of thought reasoning GUI agent screenshot visual"

### Batch 3: Self-training / RL for GUI agents
- "GRPO reinforcement learning GUI agent mobile"
- "ReST-MCTS tree search reasoning process reward model"
- "self-training reinforcement learning mobile GUI agent DPO"
- "SphAgent mobile GUI agent vision"
- "AndroidControl mobile GUI agent benchmark OOD"

### Batch 4: Step/Process-level preference optimization
- "MCTS DPO step-level preference optimization reasoning"
- "TreePO tree preference optimization segment reasoning"
- "TreeRL tree reinforcement learning reasoning preference"
- "SPO segment preference optimization chain reasoning"
- "step-level direct preference optimization reasoning process"

### Batch 5: Named comparison methods from postmortem
- "ReachAgent DPO action quality comparison GUI agent"
- "TCPO thought consistency preference optimization"
- "ReFT reinforcement learning fine-tuning reasoning"
- "InfiGUI-R1 reinforcement learning mobile GUI agent"
- "Search-R1 reinforcement learning reasoning search agent"

### Batch 6: Closed-source VLM / Data augmentation / Additional
- "GPT-4V mobile GUI agent smartphone app control"
- "instruction evolution data augmentation GUI visual question answering"
- "process reward model reasoning step annotation expensive"
- "GUI data augmentation grounding question answering screenshots"
- "Monte Carlo tree search reasoning step-level credit assignment"
- "rule-based reward tree search reasoning without process reward model"
- "Qwen2-VL mobile GUI agent"
- "DPO direct preference optimization GUI action agent"
- "AMEX mobile GUI agent benchmark"
- "GUI continual pre-training grounding agent visual"

Additional targeted searches:
- "GPT-4V multimodal mobile phone GUI control agent app"
- "closed-source large multimodal model mobile GUI agent"
- "Mobile-Agent autonomous multimodal mobile device visual perception"
- "Tree Preference Optimization tree search segment reasoning LLM"

## Verification
- 128 unique papers identified from all searches
- 29 papers verified via DeepXiv `brief` endpoint
- 16 papers further verified via `head` endpoint for author/venue metadata
- All 16 cited papers verified with confirmed titles, authors, venues

## Final Cited Papers (16 papers, 4 themes)

### Theme 1: VLM-based Mobile GUI Agents (5 papers)
[1] CogAgent (2312.08914) — Hong et al., CVPR 2023
[2] SeeClick (2401.10935) — Cheng et al., ACL 2024
[3] OS-ATLAS (2410.23218) — Wu et al., arXiv 2024
[4] UI-TARS (2501.12326) — Qin et al., arXiv 2025
[5] Falcon-UI (2412.09362) — Shen et al., arXiv 2024

### Theme 2: Chain-of-Thought Reasoning for GUI (3 papers)
[6] AITZ / CoaT (2403.02713) — Zhang et al., EMNLP 2024
[7] GPT-4V in Wonderland (2311.07562) — Yan et al., arXiv 2023
[8] Does CoT Help Mobile GUI Agent (2503.16788) — Zhang et al., arXiv 2025

### Theme 3: Tree Search & Preference Optimization (4 papers)
[9] ReST-MCTS* (2406.03816) — Zhang et al., NeurIPS 2024
[10] Step-DPO (2406.18629) — Lai et al., arXiv 2024
[11] SPO (2505.23564) — Guo et al., arXiv 2025
[12] TreeRL (2506.11902) — Hou et al., ACL 2025

### Theme 4: Preference Optimization for GUI Agents (4 papers)
[13] UI-R1 (2503.21620) — Lu et al., AAAI 2025
[14] Mobile-R1 (2506.20332) — Gu et al., arXiv 2025
[15] ReachAgent (2502.02955) — Wu et al., NAACL 2025
[16] TCPO (2509.08500) — Jiao et al., EMNLP 2025

## Uncertainty Notes
- Paper [8] (Does CoT Help Mobile GUI Agent) venue listed as arXiv.org — may appear in a conference venue later
- Several papers (OS-ATLAS, UI-TARS, Falcon-UI, SPO, etc.) currently listed as arXiv — their final publication venues may differ
- The paper's own references to AITZ, AMEX, AndroidControl, AITW datasets were not verified via DeepXiv as they are dataset papers
- "GPT-4V in Wonderland" [7] is the MM-Navigator paper — confirmed correct via DeepXiv
