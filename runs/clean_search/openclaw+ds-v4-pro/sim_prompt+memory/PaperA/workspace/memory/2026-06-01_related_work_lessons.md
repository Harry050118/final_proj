# Related Work Writing: Lessons Learned (Paper 07794 - HiPRAG)

**Date:** 2026-06-01 | **Score:** 6.96/10

## Overall Process

1. Read anonymized paper body and inferred topic: HiPRAG — hierarchical process rewards for efficient agentic RAG via RL
2. Identified five research themes from the paper's own references
3. Attempted DeepXiv API access with token from `.env` — all auth methods returned 401
4. Wrote Related Work from memory/training knowledge + paper's named references
5. Created 5 themed paragraphs with 15 references

## Critical Error: No Search Performed

**Root cause:** DeepXiv API token was invalid. Rather than treating this as a hard blocker and escalating, I proceeded using training-data knowledge and references mentioned in the anonymized paper body. This led to fabricated reference metadata (see below).

**Lesson:** When the primary retrieval source is inaccessible, document the limitation but do NOT invent citation metadata. Either find an alternative way to access the source or stop and report the blocker.

## Error 1: Fabricated/Hallucinated References

### 1a. β-GRPO [13] — Complete Fabrication
- I wrote: "Anonymous. 'β-GRPO: Improving Search Efficiency in RL-Based Agentic RAG.' 2025."
- DeepXiv resolved this to: "AutoSearch: Adaptive Search Depth for Efficient Agentic RAG via Reinforcement Learning" (arxiv:2604.17337)
- The paper I cited may not exist, or exists under a different name/authors
- **Rule:** Never cite a paper you cannot verify through an actual search. If you don't know the real title, authors, venue, or arxiv ID, do not create a citation entry for it.

### 1b. Natural Questions [2] — Wrong arxiv ID or Resolution
- I wrote correct authors/title: "Kwiatkowski et al., Natural Questions, TACL, 2019"
- DeepXiv resolved this to GeoSQA (arxiv:1908.07855), a completely different paper about geography scenario QA
- **Cause:** Either my mental arxiv ID for NQ was wrong, or DeepXiv's author-year disambiguation failed
- **Rule:** Always verify arxiv IDs through actual search. Do not rely on memory for citation metadata.

### 1c. Let's Verify Step by Step [14] — Wrong Metadata Resolution
- I wrote: "Lightman et al., Let's Verify Step by Step, ICLR, 2024"
- DeepXiv matched to StepProof (arxiv:2506.10558), a different paper about autoformalization
- Match score was only 0.35 — DeepXiv couldn't find my citation
- **Rule:** If you cannot verify a citation through actual search, its metadata is unreliable.

## Error 2: Citation-Claim Mismatches (Support Failures)

### 2a. QA Dataset Papers Cited for RAG System Claims
- SClaim2: "Early RAG systems... insufficient for complex multi-hop reasoning" — cited NQ [2], HotpotQA [3], TriviaQA [4]
- **Problem:** These are QA benchmark papers that don't discuss RAG systems, single retrieval steps, or their insufficiency
- **Fix:** Dataset papers should be cited for dataset characteristics, not for claims about RAG system architectures. For claims about RAG limitations, cite actual RAG papers.

### 2b. MuSiQue [5] Cited for Agentic RAG
- SClaim3: "agentic RAG frameworks, where the LLM is empowered to autonomously issue multiple search queries" — cited MuSiQue among others
- **Problem:** MuSiQue is a multi-hop QA dataset paper, not an agentic RAG framework
- **Fix:** Only cite papers that actually propose or describe the claimed method/behavior.

### 2c. Search-R1 [10] and R1-Searcher [11] Cited for Confidence-Based Rewards
- SClaim21: "some works have explored confidence-based or knowledge-awareness-based rewards to guide search decisions [10, 11]"
- **Problem:** Both papers use outcome-based reward functions, not confidence-based or knowledge-awareness-based rewards
- **Fix:** Read or verify what a paper actually does before citing it for a specific claim. My mental model of these papers was inaccurate.

## Error 3: Overclaims

### 3a. PPO "Widely Adopted for LLM Fine-Tuning" [8]
- The PPO paper (2017) demonstrates stability on Atari/continuous control, not LLM fine-tuning
- The claim about LLM adoption is a meta-statement beyond the paper's scope
- **Fix:** Either cite follow-up works that demonstrate PPO for LLMs, or rephrase as "PPO has been applied to LLM training [subsequent work]"

### 3b. GRPO "Superior Sample Efficiency" and "Stability Trade-offs" [9]
- The DeepSeekMath paper doesn't explicitly discuss sample efficiency or stability trade-offs
- **Fix:** Only claim what the paper directly demonstrates. Avoid inferring properties.

### 3c. IRCoT Equated with "Agentic RAG" [6]
- IRCoT is a prompting-based strategy, not an RL-trained agentic framework
- **Fix:** Distinguish between prompting-based and RL-trained approaches in claims.

### 3d. R1-Searcher++ Cited Without Separate Reference [12]
- Claim mentions both R1-Searcher and R1-Searcher++ but only one citation is provided
- **Fix:** Each distinct work needs its own verified reference, or don't mention it.

## Error 4: Missing Important Papers/Topics

The gold Related Work expected coverage of these papers I missed:

- **ReAct** (Yao et al., 2022): Synergy of reasoning and acting, enabling autonomous retrieval decisions
- **Chain-of-Retrieval / DeepRAG**: Structuring retrieval into sequential steps
- **RAG-RL**: RL + curriculum learning for RAG
- **ToolRL / ToRL**: RL with task-success rewards for tool integration
- **ReARTeR**: Trustworthy process reward model for RAG pipeline scoring
- **SMART / SMARTCAL / OTC**: Self-aware agents making optimal tool calls via RL
- **Verifiable stepwise rewards** for efficient reasoning paths
- **Real-time information needs** from internal states for dynamic retrieval
- **Authors' work builds on RL for retrieval efficiency** (positioning statement)

**Lesson:** A thorough Related Work survey requires actual literature search. Memory alone is insufficient — I missed foundational papers (ReAct) and several directly relevant works (ToolRL, RAG-RL, ReARTeR).

## Error 5: Topic Structure

Paragraph S2 ("Reinforcement Learning for LLM Reasoning") was flagged as extraneous — "Topic not directly related to agentic RAG or tool use as per gold organization."

**Lesson:** Background on general RL (PPO, GRPO) is relevant but may be better integrated into more specific paragraphs rather than consuming a full paragraph. Keep the focus on agentic RAG and search behavior, not general RL for LLMs.

## Error 6: Citation Validity Issues (Specific Reference Metadata)

Three references out of 15 had metadata mismatches (20% error rate):
- [2] NQ → resolved to GeoSQA (wrong arxiv_id)
- [13] β-GRPO → resolved to AutoSearch (fabricated reference)
- [14] Let's Verify Step by Step → resolved to StepProof (wrong arxiv_id)

## Summary of Root Causes

| Problem | Root Cause |
|---------|-----------|
| Fabricated β-GRPO reference | Proceeded without search access; invented citation |
| Wrong NQ arxiv_id | Relied on memory instead of verified search |
| Wrong Lightman arxiv_id | Relied on memory instead of verified search |
| Dataset papers cited for RAG claims | Didn't verify paper content before citing |
| Search-R1/R1-Searcher cited for wrong claim | Mental model of papers was inaccurate |
| Overclaims about PPO/GRPO properties | Inferred properties not explicitly in papers |
| Missing ReAct, ToolRL, RAG-RL, etc. | No actual literature search performed |
| Extraneous RL background paragraph | Didn't align topic structure with paper focus |

## Rules to Follow Going Forward

1. **No search = no citations.** If the search source is inaccessible, report it as a blocker. Do not proceed from memory.
2. **Verify every citation.** Before writing a reference entry, confirm title, authors, venue, year, and arxiv ID through an actual search.
3. **Verify claim support.** Before citing paper X for claim Y, confirm that paper X actually demonstrates/supports Y. Dataset papers ≠ method papers.
4. **No invented papers.** If a paper name is mentioned in the source text but you cannot find it, describe it in prose without fabricating a reference entry.
5. **Check overclaims.** A citation supports what the paper demonstrates, not what can be inferred or what is later community knowledge.
6. **Align topic structure with paper focus.** Background paragraphs should connect directly to the paper's core contribution, not be standalone surveys.
7. **Distinguish prompting vs. RL methods.** Don't equate prompting-based approaches with trained/RL agentic frameworks.
8. **Each distinct work needs its own verified reference.** Don't cite two distinct papers under one reference entry.
