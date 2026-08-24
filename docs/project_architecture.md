# Indexical Circuits — Project Architecture

## Project aim

**Indexical Circuits** investigates whether linguistic register can influence how a language model represents a speaker's epistemic authority and whether this representation causally affects the model's willingness to defer to that speaker.

The project connects sociolinguistic theories of register and indexicality with mechanistic interpretability.

The central proposed pathway is:

**Linguistic form → social/indexical inference → epistemic authority → model deference**

The project does not assume that this mechanism exists. Each stage tests a different part of this proposed causal chain.

---

## Core research question

**Can formal linguistic register cause a language model to infer greater epistemic authority from a speaker, and can that internal representation increase agreement with the speaker's claims, including false claims?**

A secondary question is whether linguistic cues to authority and explicit authority information converge on shared internal representations.

---

## Research architecture

### Phase 1 — Exploratory behavioral discovery

A 20-pair behavioral pilot tested whether matched plain and formal formulations changed agreement behavior in `google/gemma-2-2b-it`.

Agreement was measured using token logits rather than only the model's final categorical response.

The exploratory results suggested that formal register may increase agreement particularly for false claims.

This phase is treated as **hypothesis-generating rather than confirmatory**.

### Phase 2 — Confound identification and validation design

The exploratory findings motivated explicit consideration of possible alternative explanations, including:

- assertiveness / confidence;
- politeness;
- naturalness;
- perceived expertise / authority;
- evidential strength;
- semantic equivalence.

A human-rating validation framework was developed to measure these properties independently.

### Phase 3 — Confirmatory stimulus construction

A stronger matched factual-family design was created.

The design independently manipulates:

**Truth:** true / false  
**Register:** plain / formal

Each of 60 factual families therefore contains four versions:

- True + Plain
- True + Formal
- False + Plain
- False + Formal

This produces 240 candidate sentences.

All 60 families were fact-checked and structurally audited before confirmatory model testing.

### Phase 4 — Human-validation infrastructure

A blinded human-validation experiment has been fully designed and instrumented.

It includes:

- 16 counterbalanced validation forms;
- 45 sentences per participant;
- six independent linguistic rating dimensions;
- eligibility screening;
- balanced allocation procedures;
- a pre-specified recruitment and stopping protocol.

The planned confirmatory human sample is 80 usable participants, yielding approximately 15 ratings per candidate sentence.

**Current status:** recruitment has not yet been conducted.

The stimulus bank must therefore be described as **fact-verified and construction-audited**, not as human-validated.

Human recruitment can be completed later for publication-quality validation.

### Phase 5 — Confirmatory model behavior

The 60-family 2 × 2 stimulus bank will next be tested on Gemma 2 2B.

The primary behavioral analysis asks whether there is a:

**Register × Truth interaction**

with particular interest in whether formal register increases agreement with false claims.

This stage establishes whether there is a sufficiently robust behavioral phenomenon to justify mechanistic investigation.

### Phase 6 — Mechanistic localization

If the behavioral effect replicates, the next question is:

**Where and how is register-related social information represented inside the model?**

Candidate internal features, activations, components, or circuits will be traced across the plain/formal contrast.

The aim is to distinguish representations associated with:

- linguistic formality itself;
- inferred expertise or authority;
- downstream agreement/deference behavior.

### Phase 7 — Causal intervention

Candidate mechanisms will then be tested causally.

Interventions may suppress, amplify, patch, or otherwise manipulate candidate internal representations.

The key test is whether changing the proposed authority-related representation changes the model's agreement behavior.

A correlation between an activation and formal language is not sufficient to establish a mechanism.

### Phase 8 — Generalization

Any candidate mechanism will be tested on:

- held-out factual families;
- new plain/formal sentence pairs;
- different realizations of formal register;
- potentially explicit speaker-authority manipulations.

This stage tests whether the discovered mechanism generalizes beyond particular lexical items or stimulus templates.

---

## Evidential logic

The project follows the sequence:

**Observe → Control → Replicate → Localize → Intervene → Generalize**

Each stage supports a progressively stronger claim.

Behavioral evidence establishes an effect.

Controlled stimuli reduce alternative explanations.

Mechanistic localization identifies candidate representations.

Causal intervention tests whether those representations contribute to the behavior.

Held-out testing evaluates whether the mechanism generalizes.

---

## Contribution

### To mechanistic interpretability

The project investigates whether models contain internal mechanisms that translate socially meaningful linguistic variation into downstream epistemic decisions.

Rather than studying only factual content, syntax, or semantic concepts, it asks whether **social meaning itself becomes mechanistically consequential inside a language model**.

### To sociolinguistics

The project operationalizes register and indexicality as experimentally manipulable and potentially mechanistically traceable phenomena.

It therefore moves from describing how linguistic forms index social meanings for human communities toward asking how such indexical relationships may be represented and used by artificial language systems.

### To AI safety

If stylistic cues associated with authority can alter model deference independently of factual accuracy, this could reveal a socially mediated route through which models become more susceptible to confidently or institutionally framed misinformation.

Understanding the mechanism could support more robust models whose epistemic judgments depend less on socially indexed authority cues and more on evidence and factual reliability.

---

## Portfolio claim

The project should ultimately demonstrate a complete research progression:

**sociolinguistic hypothesis → controlled behavioral effect → internal representation → causal mechanism → generalization**

The distinctive contribution of **Indexical Circuits** is to treat linguistic style not merely as an input feature, but as a possible source of socially meaningful internal computation with causal consequences for language-model behavior.
