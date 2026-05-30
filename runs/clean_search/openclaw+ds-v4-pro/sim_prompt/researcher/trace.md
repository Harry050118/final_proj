# Trace: Related Work Generation via DeepXiv Clean Search (Sim Prompt)

## Date
2026-05-25

## Inferred Research Topic
The paper proposes a framework for automating the full scientific research lifecycle using open-source post-trained LLMs as autonomous agents. Key components:
- **CycleResearcher**: A policy model that performs literature review, idea generation, experimental design, and paper writing
- **CycleReviewer**: A reward model that simulates peer review, evaluating papers and providing feedback
- **Iterative SimPO**: A self-improving training framework combining preference optimization with iterative refinement
- **Datasets**: Review-5k (ICLR 2024 reviews) and Research-14k (ML conference papers 2022-2024)
- **Ethical safeguards**: Fast-DetectGPT for AI-generated text detection

## Search Queries Executed

### Round 1: Broad discovery
1. "automated scientific research lifecycle large language models autonomous agent paper generation peer review"
   - Found: LLM4SR survey, AI Scientist paper, CycleResearcher (own paper - NOT cited), AI-Researcher
2. "LLM peer review automated evaluation research papers scoring consistency"
   - Found: SEA, MARG, ReviewerGPT, ReviewRL, LLM-as-Judge surveys
3. "iterative preference optimization SimPO reinforcement learning language model alignment self-improvement"
   - Found: Self-Rewarding LMs, SimPO, DPO

### Round 2: Targeted searches
4. "AI scientist automated research paper generation language model end-to-end pipeline"
   - Found: The AI Scientist (2408.06292), MLR-Copilot
5. "LLM as judge reward model academic paper evaluation quality assessment trained"
   - Found: Think-J, LLM-as-a-Judge surveys
6. "large language model research idea generation ideation novelty scientific hypothesis creative"
   - Found: Si et al. human study, Hypothesis Generation with LLMs

### Round 3: Method-specific searches
7. "self-rewarding self-improving language model iterative training reinforcement learning preference optimization DPO"
   - Found: Self-Rewarding LMs, DPO, Online Iterative RLHF
8. "large language model automated literature review writing survey generation manuscript"
   - Found: AutoSurvey
9. "Fast-DetectGPT AI generated text detection academic paper watermark machine generated"
   - Found: Fast-DetectGPT, DetectGPT

### Round 4: Refinement searches
10. "LLM automated peer review GPT-4 evaluate scientific paper review generation benchmark RewardBench"
    - Found: MARG, ReviewRL, AI-Driven Review Systems
11. "SimPO simple preference optimization length normalized direct preference optimization reference free"
    - Found: SimPO (2405.14734)
12. "Si human evaluation LLM idea generation research novelty feasibility comprehensive study"
    - Found: Si et al. (2409.04109)
13. "Huang benchmark MLAgentBench evaluating LLM machine learning research coding solutions"
    - Found: MLAgentBench (2310.03302)
14. "LoRA-GA gradient approximation low-rank adaptation fine-tuning large language model"
    - Found: LoRA-GA (2407.05000) — not cited (implementation detail)

## Main Candidate Papers Considered
- The AI Scientist (2408.06292) — 757 citations — CITED
- MLR-Copilot (2408.14033) — 52 citations — CITED
- Si et al. idea generation study (2409.04109) — 347 citations — CITED
- LLM4SR Survey (2501.04306) — 80 citations — CITED
- ReviewerGPT (2306.00622) — 133 citations — CITED
- MARG (2401.04259) — 87 citations — CITED
- SEA (2407.12857) — 26 citations — CITED
- AI-Driven Review Systems (2408.10365) — 47 citations — CITED
- ReviewRL (2508.10308) — 8 citations — CITED
- LLM-as-a-Judge surveys (2411.16594, 2411.15594) — CITED
- DPO (2305.18290) — 8577 citations — CITED
- SimPO (2405.14734) — 971 citations — CITED
- Self-Rewarding LMs (2401.10020) — 587 citations — CITED
- Online Iterative RLHF (2405.07863) — 247 citations — CITED
- AutoSurvey (2406.10252) — 108 citations — CITED
- Fast-DetectGPT (2310.05130) — 316 citations — CITED
- DetectGPT (2301.11305) — 1002 citations — CITED
- RewardBench (2403.13787) — considered but not cited (evaluated reward model quality; less directly relevant)
- MLAgentBench (2310.03302) — considered but not cited (benchmark for ML experimentation, not paper generation)
- CycleResearcher (2411.00816) — IDENTIFIED AS THE INPUT PAPER — NOT CITED

## Final Cited Papers (18 total)
Organized into 5 themes:
1. LLMs for Automated Scientific Research (4 papers)
2. LLMs for Automated Peer Review (7 papers)
3. Preference Optimization for LLM Alignment (4 papers)
4. LLM-Assisted Scientific Writing (1 paper)
5. AI-Generated Text Detection (2 papers)

## Uncertainty Notes
- All cited papers were verified via DeepXiv metadata to confirm title, authors, year, and relevance
- No papers were invented; all 18 cited papers are real arXiv publications
- The input paper's own arXiv ID (2411.00816) was identified during search and explicitly excluded from citations
- Paper 2408.14033 (MLR-Copilot) mention of Du as author is Xinya Du; verified via DeepXiv
- SEA paper: Jianxiang Yu et al. — truncated to first author due to 13 total authors
- ReviewRL: Sihang Zeng et al. — truncated to first author
- The "Huang et al." reference in the original paper's Related Work refers to MLAgentBench (2310.03302) by Qian Huang et al., not cited here as it relates to ML experimentation benchmarks rather than full research automation
