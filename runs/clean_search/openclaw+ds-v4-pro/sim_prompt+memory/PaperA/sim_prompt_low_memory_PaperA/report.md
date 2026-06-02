# Related Work Evaluation: sim_prompt+memory-evotest

Overall: 6.96/10

## Metric Breakdown
- content_coverage: 4.61/10
- citation_quality: 6.10/10
- relevance: 10.00/10
- thematic_structure: 7.94/10
- synthesis_quality: 7.50/10
- writing_quality: 9.00/10
- length_conciseness: 8.24/10
- citation_validity: 8.00/10
- citation_appropriateness: 5.17/10
- citation_coverage: 5.88/10
- citation_placement: 5.39/10
- citation_topic_consistency: 5.72/10

## Input Cleaning
- s_text: replacements={}, length 4762 -> 4761
- s_references: replacements={}, length 3404 -> 3403
- g_text: replacements={'\\&': 2}, length 2945 -> 2942
- g_references: replacements={}, length 21940 -> 20825

## Missing Points
- ReAct demonstrated that LLMs can synergize reasoning and acting, enabling autonomous retrieval decisions. (No candidate claim mentions ReAct or cites the specified paper, and no text covers the specific synergy of reasoning and acting.)
- Chain-of-Retrieval and DeepRAG structure retrieval into sequential steps to handle complex queries. (No claim mentions Chain-of-Retrieval or DeepRAG or their sequential step structuring.)
- RAG-RL uses RL and curriculum learning to enhance retrieval-augmented generation. (No claim references RAG-RL or its use of RL and curriculum learning.)
- ToolRL and ToRL show that RL with task-success rewards significantly scales tool-integration in LLMs. (ToolRL and ToRL are not mentioned in any candidate claim.)
- Authors' work builds on RL for retrieval efficiency, not just final answer correctness. (No claim explicitly states that the authors' work builds on RL for retrieval efficiency; only general limitations are discussed.)
- More sophisticated methods assess LLMs' real-time information needs from internal states for dynamic retrieval. (No claim discusses assessing LLMs' real-time information needs from internal states for dynamic retrieval.)
- ReARTeR introduces a framework with a trustworthy process reward model to score and refine each step in a RAG pipeline. (ReARTeR is not referenced in any claim.)
- SMART, SMARTCAL, and OTC train agents to be self-aware and make optimal tool calls, often using RL. (None of SMART, SMARTCAL, or OTC are mentioned.)
- Verifiable stepwise rewards promote more efficient general reasoning paths. (No claim discusses verifiable stepwise rewards promoting efficient reasoning paths.)

## Hallucinated References
- GeoSQA: A Benchmark for Scenario-based Question Answering in the Geography Domain at High School Level [metadata_mismatch]
- AutoSearch: Adaptive Search Depth for Efficient Agentic RAG via Reinforcement Learning [metadata_mismatch]
- StepProof: Step-by-step verification of natural language mathematical proofs [metadata_mismatch]

## Bad Citation-Claim Pairs
- SClaim2 -> arxiv:1908.07855 [support=no]: support_reason=The paper introduces a geography QA dataset and does not discuss RAG systems, single retrieval steps, or multi-hop reasoning. The retrieved evidence further confirms that it focuses on scenario-based QA and cross-modal challenges, not RAG.
- SClaim2 -> arxiv:1809.09600 [support=weak]: support_reason=HotpotQA introduces a multi-hop QA dataset challenging for existing systems, which indirectly suggests that simple retrieval may be insufficient for complex multi-hop reasoning. However, the paper does not discuss RAG systems or retrieval strategies, so the support is weak.
- SClaim2 -> arxiv:1705.03551 [support=no]: support_reason=The TriviaQA paper introduces a reading comprehension dataset with complex, multi-hop questions, but it does not discuss retrieval-augmented generation (RAG) systems or the insufficiency of single-step retrieval. The claim about RAG is not supported by this reference.
- SClaim3 -> arxiv:2108.00573 [support=no]: support_reason=The MuSiQue paper presents a multi-hop QA dataset; it does not describe an agentic RAG framework nor address autonomous search queries or iterative reasoning by LLMs.
- SClaim14 -> arxiv:2604.17337 [support=no]: support_reason=The paper presents the AutoSearch framework for adaptive search depth in agentic RAG, not the β-GRPO method. Neither GRPO nor length/retrieval-count penalties are mentioned; the paper's RL objectives are distinct.
- SClaim19 -> arxiv:2506.10558 [support=no]: support_reason=StepProof focuses on step-by-step verification in autoformalization for mathematical proofs, not on process reward models that evaluate reasoning steps in LLM training or inference-time search.
- SClaim21 -> arxiv:2503.09516 [support=no]: support_reason=The Search-R1 paper uses a simple outcome-based reward function, not confidence-based or knowledge-awareness-based rewards. It does not provide evidence for the claim that some works have explored such reward types for retrieval-augmented tasks.
- SClaim21 -> arxiv:2503.05592 [support=no]: support_reason=R1-Searcher uses a two-stage outcome-based RL reward (retrieve-only reward to teach retrieval invocation and answer-based reward for final answer accuracy). It does not employ confidence-based or knowledge-awareness-based rewards, so it does not support the claim.

## Overclaim Citation-Claim Pairs
- SClaim3 -> arxiv:2212.10509 [support=partial, overclaim=mild]: support_reason=IRCoT interleaves retrieval with CoT reasoning, issuing multiple queries and incorporating retrieved information iteratively, which aligns with the claim's description of agentic behavior, though it is a prompting-based method rather than a trained agentic framework.; overclaim_reason=The claim refers to 'Agentic RAG frameworks' which typically imply autonomous, RL-trained agents; IRCoT is a prompting strategy, so the citation slightly overstates by equating it with agentic RAG.
- SClaim7 -> arxiv:1707.06347 [support=partial, overclaim=mild]: support_reason=The PPO paper introduces the algorithm and demonstrates its stability in continuous control and Atari tasks, but does not provide evidence of widespread adoption in complex LLM fine-tuning; the claim about adoption is a meta-statement beyond the paper's scope.; overclaim_reason=The claim states PPO 'has been widely adopted for its training stability in complex LLM fine-tuning scenarios', but the cited paper only shows the algorithm's stability in classic RL domains, not its adoption in LLM fine-tuning.
- SClaim8 -> arxiv:2402.03300 [support=partial, overclaim=mild]: support_reason=The DeepSeekMath paper introduces GRPO and shows its improved math performance, but does not explicitly discuss sample efficiency or stability trade-offs, though these can be inferred.; overclaim_reason=The claim asserts GRPO offers 'superior sample efficiency' and 'trade-offs in stability', but the paper does not provide direct evidence for these specific properties, relying on implicit performance comparisons.
- SClaim13 -> arxiv:2503.05592 [support=partial, overclaim=moderate]: support_reason=The cited paper introduces R1-Searcher and demonstrates its enhanced search capabilities, but the claim also references R1-Searcher++ which is not covered by this citation; the support is only for one part of the claim.; overclaim_reason=The claim states that both R1-Searcher and R1-Searcher++ enhance search capabilities, but only R1-Searcher is cited; the inclusion of R1-Searcher++ without a supporting citation constitutes a moderate overclaim.

## Citation Group Support
- SClaim2 [group_support=no, citation_count=3]: reason=All three citations discuss multi-hop QA datasets (GeoSQA, HotpotQA, TriviaQA) and their challenges, but none of them discuss early RAG systems, single retrieval steps, or evaluate the insufficiency of such systems for complex multi-hop reasoning. Therefore, the claim about RAG systems is not supported.; missing=["Early RAG systems' single retrieval step", 'Insufficiency for complex multi-hop reasoning']
- SClaim3 [group_support=yes, citation_count=3]: reason=The Search-o1 citation (arxiv:2501.05366) describes an agentic RAG framework that autonomously issues multiple search queries, incorporates retrieved information, and performs iterative reasoning, directly supporting the claim. The IRCoT citation (arxiv:2212.10509) provides partial support with similar behavior in a prompting strategy. Together, they confirm the claim.; covered=['autonomously issue multiple search queries', 'incorporate retrieved information', 'perform iterative reasoning']
- SClaim19 [group_support=yes, citation_count=2]: reason=One citation (arxiv:2312.08935) directly supports the claim by demonstrating that Math-Shepherd, a process reward model evaluating individual reasoning steps, improves both training (via PPO) and inference-time verification. The other citation (arxiv:2506.10558) is about step-by-step autoformalization and does not support the claim, but it does not contradict or undermine the supportive evidence.; covered=['Process reward models that evaluate individual reasoning steps', 'improve training', 'improve inference-time search', 'mathematical reasoning']
- SClaim21 [group_support=no, citation_count=2]: reason=Both cited papers use outcome-based reward functions, not confidence-based or knowledge-awareness-based rewards. None of the citations provide evidence for exploring such reward types.; missing=['confidence-based rewards', 'knowledge-awareness-based rewards', 'guiding search decisions']

## Topic Structure Issues
- paragraph_id=S2, issue=Topic not directly related to agentic RAG or tool use as per gold organization; may be extraneous background.

## Length / Conciseness Issues
- None
