# Related Work Evaluation: sim_prompt-evotest

Overall: 6.74/10

## Metric Breakdown
- content_coverage: 2.17/10
- citation_quality: 7.74/10
- relevance: 8.70/10
- thematic_structure: 8.66/10
- synthesis_quality: 7.50/10
- writing_quality: 8.50/10
- length_conciseness: 6.20/10
- citation_validity: 10.00/10
- citation_appropriateness: 9.05/10
- citation_coverage: 1.00/10
- citation_placement: 9.16/10
- citation_topic_consistency: 9.53/10

## Input Cleaning
- g_text: replacements={}, length 2370 -> 2369
- g_references: replacements={'\\_': 8}, length 22834 -> 22695

## Missing Points
- Proposed method organizes trajectory data into multi-turn dialogues based on CoaT thinking pattern to prevent agent becoming a limited action model. (No candidate claim describes the proposed method of organizing trajectory data into multi-turn dialogues based on CoaT.)
- ReFT uses reinforcement learning as a fine-tuning paradigm to improve performance on math problems. (No candidate claim mentions ReFT.)
- Xie et al. label preferences via MCTS based on feedback from self-evaluation. (No candidate claim mentions Xie et al. or labeling preferences via MCTS.)
- Digirl and Distrl use online trajectory collection to improve generalization of mobile GUI agents, but the process is very slow. (No candidate claim mentions Digirl or Distrl.)
- Reachagent uses DPO training to compare the quality of multiple actions. (No candidate claim mentions Reachagent.)
- TCPO optimizes thoughts but does not explicitly enforce thought–action consistency. (No candidate claim mentions TCPO.)
- TreePO, TreeRL, and SPO segment long sequences into many short segments, leading to high computational cost and low data efficiency. (No candidate claim mentions TreePO, TreeRL, or SPO.)
- Proposed method models thoughts with a fixed CoaT-tree and uses T-DPO to optimize the thinking process, while step values are computed directly from rule-based rewards without unstable PRMs. (No candidate claim describes the proposed method with fixed CoaT-tree and T-DPO.)
- The design yields more efficient sampling and training, especially in GUI-agent settings. (No candidate claims describe the design's efficiency in GUI-agent settings.)

## Hallucinated References
- None

## Bibliographic Accuracy Issues
- None

## Bad Citation-Claim Pairs
- SClaim16 -> arxiv:2310.10080 [support=weak]: support_reason=The paper proposes an automated method (AST-based dataset creation) to generate step-level rewards for code generation, and does not explicitly state that PRM training typically requires expensive manual annotation of intermediate reasoning steps. The claim is not directly supported; the paper focuses on using PRM in decoding rather than training with manual annotations.

## Overclaim Citation-Claim Pairs
- None

## Citation Group Support
- SClaim2 [group_support=yes, citation_count=2]: reason=Both citations fully support their respective parts of the claim: CogAgent introduces specialized visual encoders for high-resolution screenshots, and SeeClick demonstrates that GUI grounding pre-training improves agent performance across mobile, desktop, and web platforms.; covered=["CogAgent's specialized visual encoders for high-resolution screenshot understanding", "SeeClick's GUI grounding pre-training improves downstream agent performance across mobile, desktop, and web platforms"]
- SClaim3 [group_support=yes, citation_count=2]: reason=Both citations confirm that OS-Atlas and UI-TARS employed large-scale continual pre-training on millions of GUI elements, achieved strong in-domain performance, and serve as open-source alternatives to commercial VLMs. The evidence collectively supports all key aspects of the claim.; covered=['OS-ATLAS scaled direction via large-scale continual pre-training', 'UI-TARS scaled direction via large-scale continual pre-training', 'millions of GUI elements', 'strong in-domain performance', 'open-source alternatives to commercial VLMs']
- SClaim8 [group_support=yes, citation_count=2]: reason=Both citations provide direct support: AITW offers 715k episodes with 30k unique instructions (large-scale, diverse), and AMEX provides 104K screenshots with stepwise instructions and action chains, enabling supervised fine-tuning. Together, they collectively confirm the claim that these datasets provide large-scale human demonstrations with diverse instructions and action spaces that enable supervised fine-tuning of agents (including CoaT-capable agents, as the datasets are designed for general mobile GUI agent training).; covered=['Large-scale human demonstrations', 'Diverse instructions and action spaces', 'Enables supervised fine-tuning']
- SClaim13 [group_support=yes, citation_count=2]: reason=Both citations explicitly support that CPO and TPO explore tree-structured preference learning with multi-step or multi-branch preference trees, fully covering the claim.; covered=['CPO uses tree-of-thought search trees for multi-step preference data', 'TPO learns from multi-branch, multi-step preference trees', 'Both methods capture finer-grained reasoning quality through tree-structured preference learning']
- SClaim16 [group_support=yes, citation_count=2]: reason=The first citation (arxiv:2310.10080) provides evidence that PRMs use step-level feedback (e.g., 'step-level feedback from a process-supervised reward model'), supporting the first part of the claim. The second citation (arxiv:2501.13622) implies that existing PRM training typically requires expensive manual annotation by introducing a method to reduce annotation cost, thereby supporting the second part. Together, the citations cover both key aspects of the claim.; covered=['PRMs assign per-step feedback', 'their training typically requires expensive manual annotation of intermediate reasoning steps']
- SClaim21 [group_support=yes, citation_count=2]: reason=Both citations directly support their respective components: ARPO with experience-replay-augmented GRPO for sparse-reward GUI environments (arxiv:2505.16282) and MobileGUI-RL with online RL and curriculum task synthesis in real mobile settings (arxiv:2507.05720). Together, they fully support the entire claim without any missing aspects.; covered=['ARPO introduced experience-replay-augmented GRPO for end-to-end policy optimization in sparse-reward GUI environments', 'MobileGUI-RL explored online RL with curriculum task synthesis in real mobile settings']

## Topic Structure Issues
- paragraph_id=S1, issue=None identified.
- paragraph_id=S2, issue=Could be more explicitly linked to VLM-based agents; reads as a separate reasoning topic.
- paragraph_id=S3, issue=Lacks application to the GUI domain; focus on text reasoning may feel disconnected.
- paragraph_id=S4, issue=Does not connect to mobile agent context; appears as a standalone method description.
- paragraph_id=S5, issue=As noted, may lack step-level reasoning optimization; could benefit from bridging self-training and process rewards.
- paragraph_id=S6, issue=Only one citation; topic seems ancillary to main themes and feels slightly out of place.

## Length / Conciseness Issues
- Relative length ratio=1.96 (s=675 words, g=345 words)
