# Related Work Evaluation: sim_prompt-evotest

Overall: 7.04/10

## Metric Breakdown
- content_coverage: 4.20/10
- citation_quality: 7.79/10
- relevance: 8.09/10
- thematic_structure: 8.25/10
- synthesis_quality: 8.00/10
- writing_quality: 8.50/10
- length_conciseness: 4.02/10
- citation_validity: 9.72/10
- citation_appropriateness: 9.00/10
- citation_coverage: 2.17/10
- citation_placement: 8.22/10
- citation_topic_consistency: 9.49/10

## Input Cleaning
- s_text: replacements={}, length 8466 -> 8465
- s_references: replacements={}, length 4070 -> 4069
- g_text: replacements={}, length 2370 -> 2369
- g_references: replacements={'\\_': 8}, length 22834 -> 22695

## Missing Points
- Researchers build mobile GUI agents and multi-agent frameworks based on closed-source VLMs. (No candidate claim mentions building agents based on closed-source VLMs.)
- ReFT uses reinforcement learning as a fine-tuning paradigm to improve performance on math problems. (No candidate claim mentions ReFT.)
- Digirl and Distrl use online trajectory collection to improve generalization, but the process is slow. (No candidate claim mentions Digirl or Distrl.)
- Reachagent uses DPO training to compare the quality of multiple actions. (No candidate claim mentions Reachagent.)
- TCPO optimizes thoughts but does not explicitly enforce thought–action consistency. (No candidate claim mentions TCPO.)
- TreePO, TreeRL, and SPO segment long sequences into many short segments, leading to high computational cost and low data efficiency. (No candidate claim mentions TreePO, TreeRL, or SPO.)

## Hallucinated References
- None

## Bibliographic Accuracy Issues
- R1 arxiv:2307.10088 Android in the Wild: A Large-Scale Dataset for Android Device Control [bibliographic_accuracy=9.50]: authors:Retrieved metadata omits authors, so authorship cannot be fully verified against the raw reference. provided='Christopher Rawles, Alice Li, Daniel Rodriguez, Oriana Riva, and Timothy Lillicrap' expected=''
- R2 arxiv:2312.08914 CogAgent: A Visual Language Model for GUI Agents [bibliographic_accuracy=9.50]: authors:Retrieved metadata omits authors, so authorship cannot be fully verified against the raw reference. provided='Wenyi Hong, Weihan Wang, Qingsong Lv, Jiazheng Xu, Wenmeng Yu, Junhui Ji, Yan Wang, Zihan Wang, Yuxiao Dong, Ming Ding, and Jie Tang' expected=''
- R3 arxiv:2312.13771 AppAgent: Multimodal Agents as Smartphone Users [bibliographic_accuracy=9.50]: authors:Retrieved metadata omits authors, so authorship cannot be fully verified against the raw reference. provided='Chi Zhang; Zhao Yang; Jiaxuan Liu; Yucheng Han; Xin Chen; Zebiao Huang; Bin Fu; Gang Yu' expected=''
- R4 arxiv:2309.11436 You Only Look at Screens: Multimodal Chain-of-Action Agents [bibliographic_accuracy=9.20]: authors:Retrieved metadata omits authors, so authorship cannot be fully verified against the raw reference. provided='Zecheng Zhang; Aston Zhang' expected=''
- R7 arxiv:2410.23218 OS-ATLAS: A Foundation Action Model for Generalist GUI Agents [bibliographic_accuracy=9.50]: authors:Retrieved metadata omits authors, so authorship cannot be fully verified against the raw reference. provided='Zhiyong Wu, Zhenyu Wu, Fangzhi Xu, Yian Wang, Qiushi Sun, Chengyou Jia, Kanzhi Cheng, Zihan Ding, Liqian Chen, Benlin Liu, et al.' expected=''
- R9 arxiv:2412.09362 Falcon-UI: Understanding GUI Before Following User Instructions [bibliographic_accuracy=9.50]: authors:Retrieved metadata has no authors, so author consistency cannot be verified against the raw reference. provided='Wei Liu; Jiawei Chen; Yifei Zhang; Xi Chen; Jun Liu; Zhihong Chen; Zhiyi Zhang; Yu Zheng' expected=''
- R10 arxiv:2407.17490 AMEX: Android Multi-annotation Expo Dataset for Mobile GUI Agents [bibliographic_accuracy=9.50]: authors:Retrieved metadata has no authors, so authors cannot be verified against the raw reference. provided='Yuxiang Chai, Siyuan Huang, Yazhe Niu, Han Xiao, Liang Liu, Dingyu Zhang, Peng Gao, Shuai Ren, and Hongsheng Li' expected=''
- R11 arxiv:2406.03679 On the Effects of Data Scale on UI Control Agents [bibliographic_accuracy=9.00]: authors:Retrieved metadata omits authors, so authorship cannot be fully verified against the raw reference. provided='Jiachen Li, Yizhe Zhang, Qin Liu, Nan Hua, Pengyun Wang, Xiaofei Sun, and Tao Ge' expected=''
- R14 arxiv:2305.18290 Direct Preference Optimization: Your Language Model is Secretly a Reward Model [bibliographic_accuracy=9.50]: authors:Retrieved metadata omits authors, so authors cannot be fully verified against the raw reference. provided='Rafael Rafailov; Archit Sharma; Eric Mitchell; Stefano Ermon; Christopher D. Manning; Chelsea Finn' expected=''
- R15 arxiv:2406.18629 Step-DPO: Step-wise Preference Optimization for Long-chain Reasoning of LLMs [bibliographic_accuracy=9.50]: authors:Retrieved metadata omits authors, so authorship cannot be fully verified against the raw reference. provided='Xin Lai; Zhuotao Tian; Yukang Chen; Senqiao Yang; Xianglong Peng; Jiaya Jia' expected=''
- R16 arxiv:2501.12948 DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning [bibliographic_accuracy=9.50]: authors:Retrieved metadata omits authors, so authorship cannot be fully verified against the raw reference. provided='Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al.' expected=''
- R17 arxiv:2505.15810 GUI-G1: Understanding R1-Zero-Like Training for Visual Grounding in GUI Agents [bibliographic_accuracy=9.20]: authors:Retrieved metadata omits authors, so authorship cannot be fully verified against the raw reference. provided='Yuqi Zhou; Shuai Wang; Haoyuan Li; Hanqing Zhao; Xiao Ma; Yizhou Wang' expected=''
- R18 arxiv:2305.10601 Tree of Thoughts: Deliberate Problem Solving with Large Language Models [bibliographic_accuracy=9.50]: authors:Retrieved metadata omits authors, so authorship cannot be fully verified against the raw reference. provided='Shunyu Yao; Dian Yu; Jeffrey Zhao; Izhak Shafran; Thomas L. Griffiths; Yuan Cao; Karthik Narasimhan' expected=''
- R19 arxiv:2405.00451 Monte Carlo Tree Search Boosts Reasoning via Iterative Preference Learning [bibliographic_accuracy=9.50]: authors:Retrieved metadata omits authors, so author consistency cannot be confirmed from metadata. provided='Yuxi Xie; Anirudh Goyal; Wenyue Zheng; Min-Yen Kan; Timothy P. Lillicrap; Kenji Kawaguchi; Michael Shieh' expected=''
- R21 arxiv:2406.09136 Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs [bibliographic_accuracy=9.50]: authors:Retrieved metadata omits authors, so authorship cannot be fully verified against the raw reference. provided='Xinyue Chen; Jiaxin Ge; Tianyu Liu; Zhi Jin; Lingpeng Kong; Jiajun Wu' expected=''

## Bad Citation-Claim Pairs
- SClaim15 -> arxiv:2403.02713 [support=weak]: support_reason=The cited paper validates the CoAT (thinking-decision-grounding) triplet for GUI agents, but the claim asserts it is 'widely validated in subsequent GUI works,' which is not supported by evidence from this single paper.
- SClaim29 -> arxiv:2406.03816 [support=no]: support_reason=The cited paper ReST-MCTS* focuses on text-based reasoning tasks and does not discuss step-level reward annotation cost in the GUI domain or mention real devices/simulators. Retrieved evidence confirms the paper avoids manual per-step annotation via tree search, but this does not address GUI-specific costs.
- SClaim32 -> arxiv:2406.03816 [support=no]: support_reason=The cited ReST-MCTS* paper does not mention MobileIPL. Moreover, ReST-MCTS* explicitly avoids requiring a separate PRM by inferring process rewards via tree search using oracle final answers, contradicting the claim that it requires a separate PRM.

## Overclaim Citation-Claim Pairs
- SClaim33 -> arxiv:2405.00451 [support=partial, overclaim=mild]: support_reason=The cited paper (Xie et al.) focuses on text-based reasoning, supporting the 'unlike' part of the claim. However, the claim about MobileIPL operating in visual GUI domain is not supported by this citation.; overclaim_reason=The claim attributes characteristics to MobileIPL that are not present in the cited paper, though the comparative statement about the cited paper is correct.
- SClaim33 -> arxiv:2406.09136 [support=partial, overclaim=mild]: support_reason=The CPO paper focuses on text-based reasoning, supporting the 'unlike' part. The MobileIPL aspect is unsupported by this citation.; overclaim_reason=The claim attributes characteristics to MobileIPL that are not present in the cited paper.

## Citation Group Support
- SClaim1 [group_support=yes, citation_count=4]: reason=All four citations directly support both components of the claim: the existence of mobile GUI agents that autonomously interact with smartphone interfaces and the role of advances in VLMs in driving research interest. Each reference describes a VLM-based agent or benchmark for mobile GUI tasks, confirming the claim without any missing aspects.; covered=['Mobile GUI agents that autonomously interact with smartphone interfaces', 'Advances in VLMs driving research interest']
- SClaim33 [group_support=partial, citation_count=2]: reason=Both citations support the part of the claim that CPO and the MCTS-based framework of Xie et al. focus on text-based reasoning. However, neither citation provides any evidence for the claim about MobileIPL's operation in the visually grounded mobile GUI domain with multi-turn dialogues conditioned on real UI screenshots, so that aspect is unsupported.; covered=['The claim that CPO and the MCTS-based framework of Xie et al. focus on text-based reasoning.']; missing=['The claim that MobileIPL operates in the visually grounded mobile GUI domain with multi-turn dialogues conditioned on real UI screenshots.']

## Topic Structure Issues
- paragraph_id=S1, issue=Paragraph text not available; scores estimated from topic summary and grouping.
- paragraph_id=S2, issue=Paragraph text not available; scores estimated from topic summary and grouping.
- paragraph_id=S3, issue=Paragraph text not available; scores estimated from topic summary and grouping.
- paragraph_id=S4, issue=Paragraph text not available; scores estimated from topic summary and grouping.
- paragraph_id=S5, issue=Paragraph text not available; scores estimated from topic summary and grouping.
- paragraph_id=S6, issue=Paragraph text not available; scores estimated from topic summary and grouping.
- paragraph_id=S7, issue=Paragraph text not available; scores estimated from topic summary and grouping.
- paragraph_id=S8, issue=Paragraph text not available; scores estimated from topic summary and grouping.
- paragraph_id=S9, issue=Paragraph text not available; scores estimated from topic summary and grouping.
- paragraph_id=S10, issue=Paragraph text not available; scores estimated from topic summary and grouping.
- paragraph_id=S11, issue=Paragraph text not available; scores estimated from topic summary and grouping.

## Length / Conciseness Issues
- Relative length ratio=3.43 (s=1183 words, g=345 words)
