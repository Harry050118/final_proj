# Trace: Related Work Generation for "Artificial Hivemind" Paper

## Inferred Research Topic
The paper studies mode collapse in large language models (LMs), specifically:
- **Intra-model repetition**: a single LM generates highly similar outputs to the same open-ended prompt
- **Inter-model homogeneity**: different LMs independently produce strikingly similar outputs
- **Dense human preference annotation**: 25 annotators per example to capture distributional preferences
- **Model calibration**: LMs, reward models, and LM judges are miscalibrated on responses with divergent human preferences

## Key Contributions (inferred from body text)
1. INFINITY-CHAT dataset: 26K real-world open-ended queries mined from WildChat, organized into a taxonomy of 6 top-level and 17 fine-grained categories
2. First large-scale study of the "Artificial Hivemind" effect across 70+ LMs
3. 32,250 human annotations (25 per example) for both absolute ratings and pairwise preferences
4. Finding that models show weaker alignment with human ratings on (a) similar-quality alternative responses and (b) responses with high annotator disagreement

## Search Queries Used

1. "mode collapse diversity evaluation large language models open-ended generation homogenization"
2. "diversity evaluation benchmark open-ended prompts persona generation creative writing language models"
3. "inter-model similarity cross-model repetition language model outputs synthetic text homogenization"
4. "reward model human preference alignment open-ended queries pluralistic diverse preferences LLM judge"
5. "min-p decoding diversity language model generation sampling strategy top-p temperature mode collapse"
6. "WildChat dataset real world user queries chatbot conversations open ended natural prompts"
7. "HelpSteer dataset human preference alignment rating fine-grained LM reward modeling"
8. "annotator disagreement human evaluation open-ended generation subjective NLP preference idiosyncratic"
9. "model collapse synthetic data recursive training LLM self-consuming loop diversity loss"
10. "LLM-as-judge evaluation open-ended response quality reward benchmark GPT judge Prometheus"
11. "RewardBench reward model benchmark evaluation quality human preference alignment ranking"
12. "nucleus sampling top-p Holtzman curious case neural text degeneration language model decoding"
13. "training language models follow instructions human feedback RLHF InstructGPT Ouyang"
14. "Direct Preference Optimization DPO Rafailov language model alignment human preferences"
15. "AlpacaEval LLM evaluation benchmark instruction following automated evaluation length-controlled"
16. "judging LLM-as-judge MT-Bench Zheng strong evaluation GPT-4 judge chatbot arena"

## Main Candidate Papers Retrieved (with metadata verification)

All 24 cited papers had their metadata verified via DeepXiv `get_paper_metadata`:
- [1] Holtzman et al. (1904.09751) - Nucleus sampling, text degeneration ✓
- [2] Su et al. (2202.06417) - SimCTG, contrastive search ✓
- [3] Zhang et al. (2504.05228) - NoveltyBench ✓
- [4] Le Bronnec et al. (2402.10693) - Precision/Recall for LLMs ✓
- [5] Guo et al. (2412.10271) - Linguistic diversity benchmarking ✓
- [6] Zhao et al. (2405.01470) - WildChat ✓
- [7] Wu et al. (2503.05244) - WritingBench ✓
- [8] Zhang et al. (2004.10450) - Quality-diversity tradeoff ✓
- [9] Minh et al. (2407.01082) - Min-p sampling ✓
- [10] Padmakumar & He (2309.05196) - LLM writing diversity ✓
- [11] Briesch et al. (2311.16822) - Self-consuming training loop ✓
- [12] Guo et al. (2311.09807) - Synthetic text diversity decline ✓
- [13] Rios-Sialer (2601.06116) - Diversity as AI safety ✓
- [14] Ouyang et al. (2203.02155) - InstructGPT/RLHF ✓
- [15] Rafailov et al. (2305.18290) - DPO ✓
- [16] Lambert et al. (2403.13787) - RewardBench ✓
- [17] Wang et al. (2406.08673) - HelpSteer2 ✓
- [18] Wang et al. (2505.11475) - HelpSteer3 ✓
- [19] Kim et al. (2310.08491) - Prometheus ✓
- [20] Zheng et al. (2306.05685) - LLM-as-a-judge, MT-Bench ✓
- [21] Bakker et al. (2211.15006) - Diverse human preferences ✓
- [22] Padmakumar et al. (2412.03822) - Beyond the Binary ✓
- [23] Zhang et al. (2410.14632) - Diverging Preferences ✓
- [24] Xie et al. (2504.07070) - Pluralistic alignment survey ✓

## Organization into Themed Paragraphs

1. **Mode Collapse and Output Diversity in Language Models** — [1-5]
2. **Open-Ended Generation Benchmarks and Datasets** — [6-7]
3. **Decoding Strategies for Output Diversity** — [8-9]
4. **Cross-Model Homogenization and AI Safety Risks** — [10-13]
5. **Human Preference Alignment and Reward Modeling** — [14-20]
6. **Pluralistic Preferences and Annotator Disagreement** — [21-24]

## Uncertainty Notes

- The paper mentions "persona generation" and "keyword-driven storytelling" as examples of stylized diversity tasks in prior work, but does not cite specific papers. These are described as limitations of existing approaches rather than specific prior works to cite.
- The paper references "HelpSteer3" as containing sparse labels (3 annotators per item), which was confirmed from the metadata.
- The paper mentions "6 top-ranked reward models (per RewardBench)", confirming RewardBench [16] as a directly relevant resource.
- Min-p decoding [9] is explicitly discussed and evaluated in the paper body — directly relevant.
- The paper mines queries from WildChat [6], making this a directly relevant upstream resource.
- No papers were invented; all 24 citations were verified via DeepXiv metadata retrieval.
- All papers were selected based on relevance to the inferred research topics, tasks, methods, and contributions, not merely shared keywords.
