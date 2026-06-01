# Trace: Related Work Generation for Paper 12299

## Inferred Research Topic
**Mobile GUI Agent with Iterative Preference Learning (MobileIPL)**

- **Task:** Autonomous mobile GUI interaction — generating actions (CLICK, INPUT, PRESS, etc.) on Android interfaces given a natural language instruction, a screenshot, and action history.
- **Method:** 
  1. *Instruction Evolution* — three-stage data augmentation using GPT-4o to generate diverse Q&A from real UI screenshots, preventing overfitting during warm-up SFT.
  2. *CoaT-Tree Construction* — Monte Carlo Tree Search (MCTS) to iteratively sample reasoning steps (description → thought → action-decision → grounding), building a tree of reasoning paths.
  3. *Rule-based Reward + Backpropagation* — leaf nodes scored by action correctness (type, format, coordinate/spatial similarity for CLICK, F1 for INPUT), then backpropagated to intermediate nodes.
  4. *Thinking-level DPO (T-DPO)* — contrastive preference pairs from the CoaT-tree used for Direct Preference Optimization at the step level.
  5. *Iterative Rounds* — updated agent used as new base for continued sampling and T-DPO.
- **Backbone:** Qwen2-VL-7B
- **Datasets:** AITZ (filtered from AITW), AMEX (long-horizon), AndroidControl (OOD)
- **Baselines:** CogAgent, Auto-GUI, SphAgent, OS-Atlas, UGround, UI-TARS, FedMobileAgent, Falcon-UI

## DeepXiv Search Queries

| # | Query | Theme |
|---|-------|-------|
| 1 | VLM mobile GUI agent autonomous smartphone task automation | General GUI agents |
| 2 | GUI grounding visual language model mobile screen coordinate prediction | GUI grounding |
| 3 | GUI agent survey mobile device automation vision language model | Survey/overview |
| 4 | chain of thought action planning GUI agent reasoning steps | CoaT reasoning |
| 5 | multi-step reasoning GUI agent thought action planning decision grounding | GUI reasoning |
| 6 | Monte Carlo tree search reasoning process preference optimization DPO LLM | MCTS+DPO |
| 7 | ReST-MCTS process reward model tree search reasoning LLM training | PRM methods |
| 8 | tree search direct preference optimization reasoning steps self training | Tree+DPO |
| 9 | self play optimization chain of thought step level preference learning | SPO methods |
| 10 | iterative preference learning self training DPO language model reasoning | Iterative DPO |
| 11 | GRPO group relative policy optimization reasoning LLM self training | GRPO |
| 12 | self training GUI agent reinforcement learning from feedback | RL for GUI |
| 13 | GUI instruction generation data augmentation screenshot Q&A mobile UI | Data augmentation |
| 14 | mobile UI understanding screenshot question answering visual grounding VLM | UI understanding |
| 15 | AITW Android In The Wild dataset mobile GUI action | AITW dataset |
| 16 | CogAgent visual agent GUI understanding foundation model | CogAgent |
| 17 | OS-Atlas GUI grounding agent foundation model | OS-Atlas |
| 18 | UI-TARS GUI agent vision language model | UI-TARS |
| 19 | SeeClick GUI grounding visual agent | SeeClick |
| 20 | Qwen2-VL vision language model GUI | Qwen2-VL |
| 21 | AUTO-GUI autonomous GUI agent vision language model | Auto-GUI |
| 22 | AMEX mobile agent benchmark complex task long horizon | AMEX |
| 23 | AndroidControl benchmark mobile GUI agent out of distribution | AndroidControl |
| 24 | Chain of Action Thought AITZ CoAT GUI agent reasoning AITW | CoAT |
| 25 | Auto-GUI autonomous GUI agent chain of action multimodal | Auto-GUI direct |
| 26 | DigiRL reinforcement learning device control agent Android | DigiRL |
| 27 | process reward model MCTS step-level supervision reasoning LLM | PRM+MCTS |
| 28 | Step-DPO stepwise preference optimization chain reasoning LLM | Step-DPO |
| 29 | Iterative Reasoning Preference Optimization RPO chain thought | Iterative RPO |
| 30 | Chain Preference Optimization tree-of-thought reasoning preference | CPO |
| 31 | instruction synthesis GUI data generation training data diversity mobile agent | Data synthesis |
| 32 | Falcon-UI GUI understanding pretraining | Falcon-UI |
| 33 | AndroidControl low-level control Android device high precision actions | AndroidControl |
| 34 | DeepSeekMath GRPO group relative policy optimization reasoning | GRPO paper |

## Final Cited Papers (24)

| # | arXiv ID | Short Title | Venue/Year | Relevance |
|---|----------|-------------|------------|-----------|
| 1 | 2312.08914 | CogAgent | CVPR 2023 | Foundational VLM for GUI agents |
| 2 | 2401.10935 | SeeClick | ACL 2024 | GUI grounding pre-training for visual agents |
| 3 | 2312.13771 | AppAgent | CHI 2024 | Multimodal LLM smartphone agent |
| 4 | 2401.16158 | Mobile-Agent | arXiv 2024 | Vision-centric mobile agent |
| 5 | 2309.11436 | Auto-UI | ACL 2023 | Chain-of-action agent (Auto-GUI baseline) |
| 6 | 2412.04454 | Aguvis | ICML 2024 | Unified vision-based GUI agent |
| 7 | 2410.23218 | OS-Atlas | arXiv 2024 | Foundation GUI action model (key baseline) |
| 8 | 2501.12326 | UI-TARS | arXiv 2025 | Native GUI agent (key baseline) |
| 9 | 2406.11896 | DigiRL | NeurIPS 2024 | RL for device-control agents |
| 10 | 2412.09362 | Falcon-UI | arXiv 2024 | Decoupled GUI training (key baseline) |
| 11 | 2403.02713 | CoAT/AITZ | EMNLP 2024 | CoaT paradigm (core dataset used) |
| 12 | 2402.11941 | CoCo-Agent | ACL 2024 | Cognitive MLLM for smartphone GUI |
| 13 | 2504.14239 | InfiGUI-R1 | arXiv 2025 | Deliberative reasoning for GUI agents |
| 14 | 2406.03816 | ReST-MCTS* | NeurIPS 2024 | PRM-guided tree search self-training |
| 15 | 2405.00451 | MCTS+IPL | arXiv 2024 | MCTS iterative preference learning |
| 16 | 2406.18629 | Step-DPO | arXiv 2024 | Step-wise preference optimization |
| 17 | 2404.19733 | Iterative RPO | NeurIPS 2024 | Iterative reasoning preference optimization |
| 18 | 2406.09136 | CPO | NeurIPS 2024 | Tree-of-thought preference optimization |
| 19 | 2406.10858 | SVPO | EMNLP 2024 | Step-level value preference (MCTS-based) |
| 20 | 2407.18248 | Self-Training DPO | ACL 2024 | Self-training with DPO for CoT |
| 21 | 2402.03300 | DeepSeekMath/GRPO | arXiv 2024 | GRPO (comparison method) |
| 22 | 2307.10088 | AITW | NeurIPS 2023 | Foundational Android dataset |
| 23 | 2407.17490 | AMEX | ACL 2024 | Long-horizon mobile GUI dataset |
| 24 | 2406.03679 | AndroidControl | NeurIPS 2024 | OOD GUI benchmark |

## Notes
- All papers were verified through DeepXiv (`brief` and `head` endpoints) for title, authors, venue, and year.
- The paper's own model "MobileIPL" (arXiv:2505.12299) was discovered during search but not cited (it IS the input paper).
- FedMobileAgent and SphAgent were mentioned as baselines in the paper but could not be located as distinct published papers via DeepXiv; they may be unpublished or use different names.
- No ground-truth Related Work file was consulted.
- All citations match between s_text.txt numeric labels and s_reference.txt entries.
