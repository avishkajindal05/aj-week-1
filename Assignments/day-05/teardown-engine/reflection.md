# Reflection — AI Product Teardown Engine
### Google Maps ETA Prediction | Kimi (Moonshot AI)

---

## Question 1: Which of the 6 layers surprised you the most in terms of complexity for the product you chose? Why?

Layer 1 (Data Foundation) was the most surprising — and not because of the volume of data, which I expected. What I didn't expect was that the privacy-preserving aggregation pipeline is effectively the ceiling on ETA accuracy, not the machine learning models. The specific constraint is this: stricter differential privacy reduces spatial granularity, which directly degrades prediction quality on low-traffic road segments where you cannot aggregate enough individual traces to meet k-anonymity thresholds without losing location resolution. No GNN architecture, no matter how sophisticated, can recover accuracy that was lost before the data reached the model. I had assumed Layer 3 would be the hard part — the graph neural networks, the multi-horizon targets, the oversmoothing problem. Instead, the teardown process revealed that Layer 3 is doing precision engineering within a ceiling that Layer 1 set. The data moat is not just about volume; it is about the specific trade-off between privacy compliance and spatial granularity that a company with Android-scale device penetration has to navigate in a way that Apple Maps or HERE simply cannot replicate, regardless of their ML talent.

---

## Question 2: What was the single biggest difference you noticed between the LLMs you tested?

The most specific difference was not depth or accuracy — it was that Kimi was the only model that produced self-auditing behavior. ChatGLM and DeepSeek answered the prompt. Kimi evaluated whether its own answers were worth trusting. The Honesty Check sections in Kimi's output didn't just rate layers as Critical or Peripheral — they explained the *competitive reason* for that rating. For Layer 4, Kimi didn't just say "LLMs are not used here." It said: applying transformer architectures to a structured spatiotemporal regression problem would be architecturally inappropriate — and then explained why. That is a qualitatively different output from a model that says "this layer is minimal." DeepSeek's restraint was the second-most notable behavior: it hedged claims rather than projecting false confidence, consistently flagging when it was inferring vs. citing a source. ChatGLM never did either — it answered fluently but without epistemic markers. In production, where a wrong confident answer is more dangerous than a hedged correct one, the difference between Kimi's self-auditing and ChatGLM's confident fluency is not a style preference — it is an reliability gap.
