# Hypotheses

## Research Question

Does linguistic register affect a language model's willingness to agree with a user's factual claim?

## H1 — Behavioral Hypothesis

When a user makes a false factual claim, the model will show greater epistemic deference when the claim is expressed in a more formal register than when the same claim is expressed in a plain register.

In simple terms:

**same false claim + different way of speaking → potentially different level of agreement**

## H2 — Mechanistic Hypothesis

If a reliable behavioral difference is found, some internal model representations should differ systematically between the plain-register and formal-register conditions.

Some of these representations may contribute causally to the model's decision to agree or disagree.

## H3 — Generalization Hypothesis

If the mechanism reflects a broader representation of linguistic or epistemic authority rather than particular words, it should also appear in new prompts that were not used to discover the mechanism.

## Important Experimental Principle

The factual meaning of each matched pair should remain as constant as possible.

The main experimental manipulation is linguistic register.

We will therefore try to keep other factors constant, including:

- factual proposition
- speaker confidence
- politeness
- explicit evidence
- question format
- answer format

## Controls

The experiment will include both true and false factual claims.

This will help distinguish a genuine change in epistemic deference from a simple tendency to choose one answer more often.

We will also later reverse the answer labels (for example, switching which letter means "agree") to check that the result is not caused by a preference for a particular answer token.

## Analysis Order

The project will proceed in this order:

1. Establish whether a behavioral effect exists.
2. Test whether the effect survives basic controls.
3. Search for candidate internal representations.
4. Test candidate mechanisms through causal intervention.
5. Evaluate the mechanism on held-out prompts.

## Current Status

No experimental data have been collected yet.

These hypotheses were documented before the behavioral pilot experiment.

## Hypothesis Status After Confirmatory Testing

### H1 — Generic formal-register deference

**Hypothesis**

Formal register increases model agreement with false claims relative to plain register.

**Status**

Not supported by the 60-family confirmatory experiment.

Observed false-claim register effect:

`false_formal - false_plain = +0.3376`

Observed false-versus-true interaction:

`+0.3197`

Primary interaction test:

- t(59) = 0.7996
- p = .4272
- Cohen's dz = 0.103
- bootstrap 95% CI = [-0.4258, 1.1448]

Conclusion:

Generic formality should not be treated as a reliable deference-inducing feature in the current evidence.

---

### H2 — Pilot effect was caused by the response interface

**Hypothesis**

The original 20-item pilot effect resulted primarily from an invalid raw A/B scoring interface.

**Status**

Not supported.

The original pilot was rerun using Gemma's corrected official chat-template interface.

The pilot effect remained:

- false-claim register effect = +2.4574
- true-claim register effect = -1.2598
- false-minus-true difference = +3.7172

Conclusion:

The original pilot effect survives corrected measurement and is therefore better interpreted as stimulus- or realization-dependent rather than purely an interface artifact.

---

### H3 — Technical lexicality drives the effect

**Hypothesis**

Technical or specialized vocabulary is the primary linguistic feature responsible for increased agreement with false claims.

**Status**

Not supported by exploratory phenotyping.

Observed exploratory mean difference:

`technical_lexicon present - absent = -0.070`

Conclusion:

Technical vocabulary alone does not explain the behavioral pattern.

---

### H4 — Role-relational framing candidate

**Hypothesis**

False claims framed through role, function, status, qualification, ranking, authorship, or analogous relational construal may receive higher agreement than equivalent direct predications.

Examples include:

- serves as
- functions as
- qualifies as
- ranks as
- is the author of

**Status**

Exploratory candidate only.

Among cases coded as both:

1. role/status framing = present
2. relation reframing = present

the observed false-claim register effect was:

- n = 6
- mean = +3.145
- median = +1.412
- positive rate = 6/6

Robustness checks:

- remove largest effect: mean = +2.038; 5/5 positive
- remove two largest effects: mean = +0.840; 4/4 positive

The pattern was present both inside and outside capital-city constructions.

Conclusion:

The role-relational pattern is sufficiently coherent to motivate a new held-out replication.

It must not yet be described as confirmed.

---

## Current Confirmatory Target

The next experiment will test whether:

`role-relational framing > formal lexical control`

for false claims.

The new held-out design will explicitly separate:

1. plain direct predication
2. formal lexical control
3. role-relational framing

The primary confirmatory contrast will be:

`false_role_relational - false_formal_control`

Predicted direction:

positive

Mechanistic analysis will begin only if this behavioral effect replicates in a new held-out stimulus bank.

---

## Interpretation Rule

The project currently distinguishes three levels of evidence:

**Not supported**
- generic formality
- technical lexicality
- interface-artifact explanation

**Exploratory**
- role-relational framing

**Not yet tested**
- held-out replication
- mechanistic localization
- causal intervention
- generalization

No claim about an authority, epistemic-status, indexical, or deference circuit should be made until mechanistic and causal evidence is obtained.
