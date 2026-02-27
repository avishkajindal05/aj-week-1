# LLM Comparison — Product Teardown: Google Maps ETA Prediction

## Models Used

| # | LLM Name | Mode | Response Time (approx) |
|---|----------|------|------------------------|
| 1 | Kimi (Moonshot AI) | Standard | ~12s |
| 2 | ChatGLM (Zhipu AI) | Standard | ~8s |
| 3 | DeepSeek | Standard | ~11s |

---

## Layer-by-Layer Comparison

### Layer 1: Data Foundation

| Criteria | Kimi | ChatGLM | DeepSeek | Best? |
|----------|------|---------|----------|-------|
| Specificity (1–5) | 4 | 3 | 4 | Kimi / DeepSeek |
| Named real tech? | Y | Y | Y | Tie |
| Identified a real engineering challenge? | Y | Y | Y | Tie |
| Notes | Kimi cited S2 geometry levels, Kafka, Bigtable, differential privacy pipeline in detail. DeepSeek named Pub/Sub, BigQuery, GTFS feeds — all verifiable. ChatGLM named fewer systems and was less specific on the privacy constraint. | | | |

### Layer 2: Statistics & Analysis

| Criteria | Kimi | ChatGLM | DeepSeek | Best? |
|----------|------|---------|----------|-------|
| Specificity (1–5) | 4 | 3 | 4 | Kimi / DeepSeek |
| Named real tech? | Y | Y | Y | Kimi |
| Identified a real engineering challenge? | Y | Y | Y | Kimi |
| Notes | Kimi raised spatial autocorrelation and cluster-robust standard errors — a rare, precise insight showing statistical maturity. DeepSeek mentioned GMMs for HOV lane detection — highly specific and grounded in a published Google paper. ChatGLM accurate but more generic. | | | |

### Layer 3: Machine Learning Models

| Criteria | Kimi | ChatGLM | DeepSeek | Best? |
|----------|------|---------|----------|-------|
| Specificity (1–5) | 5 | 4 | 4 | Kimi |
| Named real tech? | Y | Y | Y | Kimi |
| Named model family? | Y (GNN, LWR physics model, XGBoost) | Y (GNN, LSTM, TCN) | Y (GNN, Transformers) | Kimi |
| Identified a real engineering challenge? | Y | Y | Y | Kimi |
| Notes | Kimi cited the Lighthill-Whitham-Richards physics model, multi-horizon training targets, and GNN oversmoothing — graduate-level accuracy. DeepSeek used the "butterfly effect" framing for long-range traffic correlation — effective and conceptually sharp. ChatGLM solid but least distinctive. | | | |

### Layer 4: LLM / Generative AI

| Criteria | Kimi | ChatGLM | DeepSeek | Best? |
|----------|------|---------|----------|-------|
| Specificity (1–5) | 3 | 2 | 2 | Kimi |
| Honest if not applicable? | Y | Y | Y | Tie |
| Notes | All three correctly identified LLMs as peripheral to core ETA. Kimi went further — discussed grounding constraints and multilingual explanation generation. ChatGLM and DeepSeek were brief but honest. None padded this layer, which is correct behavior. | | | |

### Layer 5: Deployment & Infrastructure

| Criteria | Kimi | ChatGLM | DeepSeek | Best? |
|----------|------|---------|----------|-------|
| Specificity (1–5) | 5 | 4 | 4 | Kimi |
| Named real tech? | Y | Y | Y | Kimi |
| Notes | Kimi uniquely named Borg, Borgmon, Dapper, TF Serving — Google-internal tooling documented in public research. ChatGLM and DeepSeek named Kubernetes and gRPC accurately. DeepSeek noted the CPU vs. GPU tradeoff for GNN inference — subtle and correct. | | | |

### Layer 6: System Design & Scale

| Criteria | Kimi | ChatGLM | DeepSeek | Best? |
|----------|------|---------|----------|-------|
| Specificity (1–5) | 5 | 4 | 4 | Kimi |
| Named real tech? | Y | Y | Y | Kimi |
| Notes | Kimi explicitly discussed S2 sharding levels (12–14), CAP theorem in product terms, and data-residency compliance — most complete answer. ChatGLM and DeepSeek both covered geo-sharding and eventual consistency. DeepSeek added graceful degradation to historical lookup tables. | | | |

---

## Overall Verdict

| Dimension | Winner | Why? |
|-----------|--------|------|
| Most technically specific overall | Kimi | Named Google-internal systems (Borg, Borgmon, F1, Dapper) and ML-theory nuances (LWR model, GNN oversmoothing) absent from other responses. |
| Best at naming real technologies | Kimi | Broadest range of named, verifiable technologies across all six layers. |
| Least hallucination / made-up info | DeepSeek | Claims consistently grounded and cautious; GTFS and GMM examples verifiable in Google Research papers. |
| Best at "hardest problem" insight | Kimi | Identified privacy-preserving aggregation pipeline as the most defended proprietary asset — subtle and defensible. |
| Best structured output | Kimi | Honesty Check sections added evaluative meta-commentary absent in other responses. |
| Fastest useful response | ChatGLM | Shortest responses with adequate coverage across all six layers. |

---

## Key Observation

> One thing I noticed about how different LLMs handle the same prompt: Kimi was the only model that produced self-auditing behavior — its Honesty Check sections didn't just rate layers, they explained *why* a layer was critical or peripheral in terms of the product's competitive position. ChatGLM and DeepSeek answered the prompt; Kimi audited its own answers. This is a qualitatively different behavior, and it's what makes Kimi useful as an analysis tool rather than just a Q&A system. DeepSeek's restraint was also notable — it was the only model that consistently hedged claims rather than projecting false confidence, which matters more in production than raw depth.
