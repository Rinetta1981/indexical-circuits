# Indexical Circuits

## Mechanistic Sociolinguistics of LLM Epistemic Deference

**Indexical Circuits** investigates whether socially meaningful linguistic constructions systematically alter an LLM's epistemic judgments — and, if a robust behavioral effect can be established, which internal model mechanisms causally produce it.

The project combines sociolinguistic analysis with controlled behavioral experimentation and mechanistic interpretability.

**Model:** `google/gemma-2-2b-it`

**Current stage:** exploratory linguistic phenotyping completed; held-out behavioral replication is next.

---

## Research Question

Can the linguistic form of a proposition change an LLM's willingness to endorse it even when the underlying factual claim is held constant?

The project originally tested whether **formal register** generally increases epistemic deference.

A stronger confirmatory experiment did not support that broad hypothesis.

Instead, exploratory linguistic phenotyping identified a narrower candidate phenomenon: **role-relational framing**.

---

## What We Found

### 1. Initial pilot

A 20-item exploratory pilot produced a substantial register effect for false claims.

False-claim formal-minus-plain effect:

`+2.4574`

This motivated a stronger confirmatory design.

### 2. Measurement audit

A diagnostic showed that raw A/B next-token scoring was inappropriate for Gemma because bare A/B tokens received negligible probability mass.

The experiment was rebuilt using Gemma's official chat template and AB/BA label counterbalancing.

Under the corrected interface, A/B jointly captured more than 99% of next-token probability.

The original pilot effect survived this correction.

### 3. Stronger confirmatory experiment

A new experiment used:

- 60 factual families
- 240 stimuli
- true and false claims
- plain and formal realizations
- AB/BA counterbalanced scoring

The broad formal-register hypothesis did **not** replicate.

False-claim register effect:

`+0.3376`

True-claim register effect:

`+0.0179`

False-minus-true interaction:

`+0.3197`

Primary interaction:

`t(59) = 0.7996, p = .4272`

The project therefore does not treat generic formality as a reliable deference-inducing feature.

### 4. Exploratory linguistic phenotyping

The heterogeneous register transformations were subsequently coded for linguistic properties including technical lexicality, role/status framing, relation reframing, taxonomic framing, syntactic restructuring, nominalization, and semantic specificity.

Technical vocabulary showed essentially no association with the false-claim effect:

`technical lexicon present - absent = -0.070`

The strongest descriptive pattern instead occurred when **role/status framing and relation reframing occurred together**.

Examples include constructions such as:

- `serves as`
- `functions as`
- `qualifies as`
- `ranks as`
- `is the author of`

For the six exploratory role-relational cases:

`mean effect = +3.145`

`median = +1.412`

`positive cases = 6/6`

After removing the two largest effects:

`mean = +0.840`

`positive cases = 4/4`

The pattern was also present outside the repeated capital-city construction cluster.

---

## Current Hypothesis

The evidence currently supports investigating a narrower hypothesis:

> **Role-relational framing may increase model agreement with false propositions relative to matched direct or merely formal formulations.**

This is an **exploratory candidate**, not a confirmed result.

The next experiment will therefore distinguish three linguistic realizations:

`plain direct predication`

→ `formal lexical control`

→ `role-relational framing`

using a completely new held-out stimulus bank.

---

## Evidence Gate

The project deliberately separates behavioral discovery from mechanistic interpretation.

The current research sequence is:

`Pilot`
→ `Measurement Audit`
→ `Bridge Replication`
→ `Controlled Confirmatory Null`
→ `Linguistic Phenotyping`
→ **`Held-Out Replication`**
→ `Mechanistic Localization`
→ `Causal Intervention`
→ `Generalization`

Mechanistic analysis will begin only if the role-relational effect replicates under the pre-specified held-out design.

No claim about an "authority circuit", "indexical circuit", or internal mechanism is currently made.

---

## Why This Matters

Most work on LLM behavior treats linguistic variation primarily as changes in wording or style.

This project asks a different question: whether socially meaningful linguistic constructions can systematically change model epistemic behavior, and whether those effects can eventually be traced to causal internal mechanisms.

The broader goal is to connect sociolinguistic concepts such as register, stance, relational construal, and indexical meaning with experimentally testable questions in mechanistic interpretability.

---

## Repository Structure

`notebooks/` — behavioral experiments and analyses

`data/` — stimuli, validation materials, and linguistic coding

`results/confirmatory/` — confirmatory behavioral outputs

`results/phenotyping/` — exploratory linguistic phenotyping outputs

`docs/` — hypotheses, experiment log, coding manual, validation plans, and project architecture

---

## Scientific Status

The project is ongoing.

Current evidence supports:

**Broad generic-formality effect:** not supported

**Technical-lexicality explanation:** not supported

**Role-relational framing:** exploratory candidate

**Held-out replication:** not yet tested

**Mechanistic localization:** not yet tested

**Causal mechanism:** not yet established


## Research Areas

- Mechanistic interpretability
- Sociolinguistics
- Linguistic indexicality
- Register and relational construal
- Large language models
- AI safety
- Epistemic deference


## Researcher

**Irene Theodoropoulou**

Linguist working at the intersection of sociolinguistics, language variation, discourse, and artificial intelligence.
























