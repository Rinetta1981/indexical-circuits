# Hypotheses and Evidence Status

This document records the evolution of the hypotheses tested in
**Indexical Circuits** and distinguishes exploratory observations from
confirmatory evidence.

The project investigates whether socially meaningful linguistic realization
can systematically alter epistemic agreement in `google/gemma-2-2b-it`.

A central methodological rule governs the project:

> Mechanistic interpretation is permitted only after a behavioral effect
> survives independent held-out replication.

---

## H1 — Generic Formality Increases Agreement with False Claims

### Hypothesis

Formal linguistic realization will increase model agreement with false factual
claims relative to semantically matched plain formulations.

Formally:

`false_formal - false_plain > 0`

### Origin

This hypothesis was motivated by the initial 20-item pilot, which showed a
substantial apparent formal-minus-plain effect for false propositions.

Pilot effect:

`+2.4574`

### Stronger confirmatory test

A new 60-family confirmatory experiment was constructed using:

- true and false propositions
- plain and formal realizations
- 240 stimuli
- AB/BA counterbalanced scoring
- Gemma's official chat template

Observed effects:

- false formal-minus-plain = `+0.3376`
- true formal-minus-plain = `+0.0179`
- false-minus-true interaction = `+0.3197`

Primary test:

`t(59) = 0.7996`

`p = .4272`

Bootstrap 95% CI:

`[-0.4258, 1.1448]`

### Status

**NOT SUPPORTED**

Generic formality is not treated as a reliable source of epistemic deference.

---

## H2 — Technical Lexicality Explains the Apparent Register Effect

### Hypothesis

Formal transformations containing technical or specialized lexical material
will produce larger false-claim agreement effects than transformations without
technical lexicality.

### Origin

This was evaluated during exploratory linguistic phenotyping of the
confirmatory stimulus set.

### Result

Technical lexicality showed essentially no positive relationship with the
false-claim effect:

`technical lexicon present - absent = -0.070`

### Status

**NOT SUPPORTED**

Technical vocabulary does not provide a useful explanation of the original
pilot effect.

---

## H3 — Role-Relational Framing Increases Agreement with False Claims

### Hypothesis

Role-relational formulations will increase model agreement with false
propositions relative to matched formal-control formulations.

Formally:

`false_role_relational - false_formal_control > 0`

### Origin

Exploratory linguistic phenotyping identified a subset in which role/status
framing and relation reframing occurred together.

Examples included:

- `serves as`
- `functions as`
- `qualifies as`
- `ranks as`
- `is the author of`

For six exploratory role-relational cases:

- mean effect = `+3.145`
- median = `+1.412`
- positive cases = `6/6`

After removing the two largest effects:

- mean = `+0.840`
- positive cases = `4/4`

Because this candidate emerged after inspection of the confirmatory data, it
was treated as exploratory and subjected to a completely new held-out test.

### Held-out test

The new experiment contained:

- 60 completely new factual families
- 6 conditions per family
- 360 unique stimuli
- 720 total model evaluations after AB/BA counterbalancing

Primary comparison:

`false_role_relational - false_formal_control`

Observed result:

- mean = `+0.0904`
- median = `+0.1836`
- positive rate = `58.3%`
- Cohen's dz = `0.048`
- `t(59) = 0.3734`
- `p = .7102`
- bootstrap 95% CI = `[-0.3928, 0.5546]`

### Status

**NOT SUPPORTED**

The broad role-relational framing effect did not replicate.

---

## H4 — `functions as` Selectively Increases Agreement with False Claims

### Hypothesis

Within otherwise matched formulations, use of the construction
`functions as` will increase agreement with false propositions relative to a
formal control using direct predication.

Primary contrast:

`false_functions_as - false_formal_control > 0`

### Interaction hypothesis

The effect of `functions as` will be larger for false than true propositions:

`(false_functions_as - false_formal_control)
-
(true_functions_as - true_formal_control) > 0`

### Origin

This hypothesis emerged from exploratory construction-level decomposition of
the failed role-relational held-out experiment.

Within the 10 exploratory `functions as` cases:

- false effect = `+1.080`
- false positive rate = `8/10`
- true effect = `-0.655`
- true positive rate = `2/10`
- false-minus-true interaction = `+1.735`

Because these results were identified after inspecting the held-out data, they
were treated as exploratory.

A new focused replication was preregistered before model testing.

---

## H4 Confirmatory Design

The focused replication contained:

- 30 completely new factual families
- 4 conditions per family
- 120 unique stimuli
- AB/BA counterbalancing
- 240 model evaluations

Conditions:

1. `true_formal_control`
2. `true_functions_as`
3. `false_formal_control`
4. `false_functions_as`

The bank was audited against 640 prior experimental stimulus texts.

Final contamination audit:

- exact overlaps = `0`
- similarities >= .90 = `0`
- reused subjects = `0`

The factual families were source-checked before model testing.

Frozen input SHA-256:

`64b3fd0cc9d0cba4f650789fc0a6e7b35787352fa17b15a5592cf885db48a14e`

---

## H4 Primary Result

Observed false `functions as` minus formal-control effect:

- mean = `-0.0666`
- median = `-0.0996`
- positive rate = `36.7%`
- Cohen's dz = `-0.166`
- `t(29) = -0.9101`
- `p = .3703`
- bootstrap 95% CI = `[-0.2109, 0.0717]`

The effect was not positive and was not statistically distinguishable from
zero.

Leave-one-item-out robustness also failed:

- minimum remaining mean = `-0.0957`
- maximum remaining mean = `-0.0262`
- all remaining means positive = `False`

Domain-level false effects were:

- biology = `-0.097`
- computing = `+0.271`
- engineering = `-0.364`
- physics = `+0.172` (`n = 1`)

The effect was therefore not robust across semantic domains.

### Status

**NOT SUPPORTED**

The apparent exploratory `functions as` effect on false-claim agreement did
not replicate.

---

## Secondary Finding — Truth-Dependent `functions as` Effect

The focused experiment produced an unexpected secondary result.

For true propositions:

`true_functions_as - true_formal_control`

was:

- mean = `-0.3240`
- positive rate = `13.3%`
- `p = 1.59e-06`
- bootstrap 95% CI = `[-0.4298, -0.2255]`

The false-minus-true interaction was:

- mean = `+0.2574`
- median = `+0.2451`
- `t(29) = 3.3542`
- `p = .00223`
- bootstrap 95% CI = `[0.1083, 0.4073]`

The interaction therefore reflects a reliable difference between the true and
false conditions.

However, it does **not** support H4.

The interaction arose primarily because `functions as` reduced agreement with
true propositions, not because it increased agreement with false
propositions.

### Status

**SECONDARY / REQUIRES INDEPENDENT REPLICATION**

No causal or mechanistic interpretation is currently made.

---

## Mechanistic Hypothesis

The original research architecture allowed for a later mechanistic hypothesis:

> If a robust linguistic effect on epistemic deference replicates, identifiable
> internal model components should causally mediate that behavioral difference.

Possible tests would have included:

- layer-wise localization
- activation differences
- activation patching
- causal ablation
- mediation-style intervention
- generalization across unseen stimuli

These analyses were conditional on successful behavioral replication.

### Status

**NOT TESTED**

The behavioral gate was not satisfied.

Mechanistic localization was therefore intentionally not initiated.

This is a stopping-rule decision, not missing analysis.

---

## Final Evidence Summary

| Hypothesis | Evidence status |
|---|---|
| Generic formality increases false-claim agreement | **Not supported** |
| Technical lexicality explains the apparent effect | **Not supported** |
| Role-relational framing increases false-claim agreement | **Not supported in held-out replication** |
| `functions as` increases false-claim agreement | **Not supported in focused preregistered replication** |
| `functions as` has a truth-dependent effect | **Secondary finding; requires independent replication** |
| A causal internal "indexical circuit" mediates the effect | **Not tested because behavioral gate failed** |

---

## Stopping Rule

No additional post-hoc behavioral narrowing will be conducted within the main
project sequence.

The completed trajectory is:

`Pilot signal`

→ `Measurement-interface validation`

→ `Broad confirmatory null`

→ `Exploratory linguistic phenotyping`

→ `Role-relational candidate`

→ `Held-out role-relational null`

→ `Exploratory functions-as candidate`

→ `Preregistered focused replication`

→ **`Primary null`**

→ **`Mechanistic gate closed`**

The project therefore preserves the distinction between:

**interesting exploratory patterns**

and

**effects that survive independent confirmation**.

This distinction is central to the scientific contribution of Indexical
Circuits.
