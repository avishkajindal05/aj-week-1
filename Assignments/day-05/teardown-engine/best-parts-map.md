# Best-Parts Map — Google Maps ETA Prediction

> This table records which LLM produced the strongest output for each layer and what specifically to carry forward into the V2 synthesis. Extracted directly from the LLM comparison findings.

---

| Layer | Best LLM | What to Extract |
|-------|----------|-----------------|
| **Layer 1: Data Foundation** | Kimi (slight edge over DeepSeek) | S2 geometry levels (10–14) for spatial bucketing, Bigtable for time-series probe storage, Kafka for real-time ingestion, differential privacy as a first-class architectural constraint — not an afterthought. Extract the framing: "privacy-utility tradeoff is acute on low-traffic segments." |
| **Layer 2: Statistics & Analysis** | Kimi | Cluster-robust standard errors for spatially correlated A/B tests — the insight that neighboring road segments violate standard independence assumptions. Extract the survivorship bias framing (abandoned trips excluded from training data, creating optimistic evaluation bias). |
| **Layer 3: ML Models** | Kimi | Lighthill-Whitham-Richards physics model as an ensemble component alongside GNNs. GNN oversmoothing problem (losing discriminative power beyond 3–4 layers while traffic propagation requires 10+ hops). Multi-horizon training targets (5-min, 15-min, 30-min). GraphSAGE-style sampling to bound inference complexity. |
| **Layer 4: LLM / Generative AI** | Kimi | The explicit statement that no transformer architecture is used for travel time prediction — architecturally inappropriate for a structured regression problem. Grounding constraint: generated explanations must be verified against probe data, not hallucinated. Keep this layer short; honesty is the value here. |
| **Layer 5: Deployment & Infrastructure** | Kimi | Borg (cluster orchestrator), Dapper (distributed tracing), TF Serving (model inference), TF Lite (offline Android fallback). Three-tier graceful degradation: GNN → XGBoost baseline → historical time-of-day lookup. |
| **Layer 6: System Design & Scale** | Kimi | S2 cell levels 12–14 for geographic sharding (~1–10 km² per cell). Eventual consistency for probe data (seconds-to-minutes), strong consistency for topology updates (road closures must propagate immediately). CAP theorem framed in product terms: stale ETA vs. unavailable ETA, with safety implications for missed closures. Data residency compliance as a first-class architectural constraint. |
| **Overall Analysis / Hardest Problem** | Kimi | Privacy-preserving aggregation pipeline as the most defended proprietary asset — the insight that data moat, not algorithmic sophistication, is the actual ceiling. "Fewer than five organizations globally possess the infrastructure to attempt this architecture" (note: this claim needs hedging in V2). |
| **Writing Style / Structure** | Kimi | Honesty Check sections with CRITICAL / SUBSTANTIAL / PERIPHERAL ratings + 1–2 sentence rationale. This meta-commentary structure is the single biggest structural improvement over ChatGLM and DeepSeek. Carry this format explicitly into V2 prompt rules. |

---

## Executive Takeaway

- **Optimizing for technical depth** → Use Kimi as the backbone
- **Optimizing for verifiable grounding and caution** → Blend DeepSeek's hedged phrasing for technology claims
- **Optimizing for brevity and readability** → Borrow ChatGLM's concise paragraph structure

The V2 prompt is designed so that a single LLM run on Kimi produces output combining all three strengths by encoding the grounding and concision requirements as explicit rules.
