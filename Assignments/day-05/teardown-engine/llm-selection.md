# LLM Selection Decision — AI Product Teardown Engine

> Decision based on evidence from the multi-LLM comparison on Google Maps ETA Prediction. Not preference — evidence.

---

## Decision Framework

| Decision Factor | My Choice | Reason |
|----------------|-----------|--------|
| Which LLM followed my prompt structure most faithfully? | Kimi | Fully preserved the 6-layer structure and added Honesty Check sections that went beyond the prompt's minimum requirements — showing structural discipline, not just compliance. |
| Which LLM was most technically accurate (least hallucination)? | DeepSeek | Claims were cautious, referenced verifiable items (GTFS feeds, GMM-based lane detection from Google Research papers), and avoided over-specific internal system names without hedging. |
| Which LLM's output was most readable and well-organized? | ChatGLM | Delivered the most concise, scannable answers without overwhelming detail — best signal-to-noise ratio for a first read. |
| Which LLM handled the "honesty check" best (admitting when a layer doesn't apply)? | Kimi | Most explicitly addressed peripheral layers (especially Layer 4 LLM/GenAI) and evaluated applicability rigorously — did not pad, did not deflect. |

---

## Selected LLM for Final Tool: **Kimi (Moonshot AI)**

**Why:** Kimi consistently demonstrated the deepest systems-level reasoning, strongest technical specificity, and the only self-auditing behavior in the comparison — its Honesty Check sections didn't just answer the prompt, they evaluated the quality of the answer itself. While DeepSeek was more conservative and less likely to hallucinate, Kimi's architectural depth across all six layers produces more actionable output for an engineering audience.

**Trade-off acknowledged:** DeepSeek would be the safer choice if the primary concern is hallucination risk on unfamiliar products. Kimi produces richer output but requires the grounding and confidence-calibration rules in V2 to prevent over-confident claims from slipping through.
