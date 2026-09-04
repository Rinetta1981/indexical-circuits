# Indexical Circuits

## A replication-first study of sociolinguistic cues and epistemic judgment in language models

**Model:** `google/gemma-2-2b-it`

**Study status: behavioral replication sequence complete; mechanistic gate closed.**

Indexical Circuits asks whether socially meaningful linguistic
constructions systematically alter a language model's epistemic judgments
when factual content is held constant.

The project was designed with a pre-specified evidence gate:

**mechanistic localization would begin only if the behavioral effect first
replicated robustly.**

That condition was not met.

The project therefore stops before making claims about an "authority
circuit", an "indexical circuit", or another causal internal mechanism.

---

## Executive summary

An exploratory pilot suggested that formal linguistic framing strongly
increased Gemma-2-2B-IT's agreement with false claims.

That apparent effect survived an important measurement-interface
correction, motivating stronger tests.

But the effect did not survive increasingly controlled independent
replication.

The research sequence was:

**Pilot**

→ **Measurement audit**

→ **Broad confirmatory null**

→ **Exploratory linguistic phenotyping**

→ **Held-out role-relational null**

→ **Exploratory `functions as` candidate**

→ **Preregistered focused replication**

→ **Primary null / mechanistic gate closed**

The strongest methodological conclusion is:

> Before explaining an apparent model behavior mechanistically, first
> establish that the behavior itself is reproducible.

The project preserves the complete path from apparently strong signal to
falsification rather than selecting only the positive stages.

---

## Key results

| Stage | Primary result |
| --- | --- |
| Initial exploratory pilot | False-claim formal-minus-plain effect: `+2.4574` |
| Measurement audit | A/B probability mass >99% after correcting the interface |
| Broad confirmatory experiment | `t(59) = 0.7996`, `p = .4272` |
| Held-out role-relational replication | `t(59) = 0.3734`, `p = .7102` |
| Focused preregistered `functions as` replication | `t(29) = -0.9101`, `p = .3703` |
| Mechanistic evidence gate | **Closed** |
| Secondary truth-dependent interaction | `t(29) = 3.3542`, `p = .00223`; requires independent replication |

The original hypothesis that linguistic formality reliably increases
agreement with false claims was not supported.

The later role-relational hypothesis also failed held-out replication.

The focused `functions as` hypothesis likewise failed its preregistered
primary test.

A secondary truth-dependent interaction appeared in the final focused
study, but it was driven primarily by **reduced agreement with true
claims**, not by reliably increased agreement with false claims.

That secondary finding is reported as hypothesis-generating rather than
as a rescue of the original theory.

---

## Effect trajectory

The apparent false-claim effect became progressively weaker as the tests
became more independent and more tightly controlled.

![Effect trajectory](assets/figures/figure_1_effect_trajectory_PORTFOLIO.png)

This trajectory is central to the project.

A strong-looking pilot effect was not sufficient evidence for a stable
behavioral phenomenon.

---

## Research question

Can the linguistic form of a proposition alter a language model's
willingness to endorse it even when the underlying factual claim is held
constant?

The project began with a broad hypothesis:

**formal register may increase epistemic deference.**

After that hypothesis failed confirmatory testing, exploratory linguistic
phenotyping asked whether the effect might instead depend on more specific
sociolinguistic structures such as:

- technical lexicality;
- role and status framing;
- relational reframing;
- taxonomic framing;
- syntactic restructuring;
- nominalization;
- semantic specificity.

This produced narrower candidate hypotheses, each of which was then
tested using new held-out material rather than being treated as confirmed
from the exploratory data that generated it.

---

## 1. Exploratory pilot

A 20-item exploratory pilot produced a substantial apparent register
effect on false claims.

False-claim formal-minus-plain effect:

`+2.4574`

The size of the apparent signal justified a more careful measurement
audit before scaling the experiment.

---

## 2. Measurement-interface audit

The initial experiment used raw A/B next-token scoring.

A diagnostic audit showed that this was not an appropriate measurement
interface for Gemma-2-2B-IT: bare A/B tokens received negligible
probability mass without the conversational formatting expected by the
instruction-tuned model.

The experiment was therefore rebuilt using:

- Gemma's official chat template;
- AB/BA response-label counterbalancing.

Under the corrected interface, the A/B alternatives jointly captured
more than 99% of next-token probability.

Importantly, the original pilot signal survived this correction.

The project therefore did not dismiss the pilot as a measurement artifact;
it proceeded to an independent confirmatory experiment.

---

## 3. Broad confirmatory experiment

The confirmatory experiment used:

- 60 factual families;
- 240 unique stimuli;
- true and false claims;
- plain and formal realizations;
- AB/BA counterbalanced scoring.

The broad formal-register hypothesis did not replicate.

Observed effects:

- false formal-minus-plain: `+0.3376`;
- true formal-minus-plain: `+0.0179`;
- false-minus-true interaction: `+0.3197`.

Primary test:

`t(59) = 0.7996, p = .4272`

Bootstrap 95% CI:

`[-0.4258, 1.1448]`

The project therefore does not treat generic formality as a reliable
deference-inducing feature.

---

## 4. Exploratory linguistic phenotyping

The heterogeneous register transformations were coded for more specific
linguistic properties.

Technical lexicality showed essentially no association with the
false-claim effect:

`technical lexicon present - absent = -0.070`

The strongest descriptive pattern instead appeared when role/status
framing and relation reframing occurred together.

Examples included:

- `serves as`;
- `functions as`;
- `qualifies as`;
- `ranks as`;
- `is the author of`.

For six exploratory role-relational cases:

- mean effect: `+3.145`;
- median effect: `+1.412`;
- positive cases: `6/6`.

After removing the two largest effects:

- mean effect: `+0.840`;
- positive cases: `4/4`.

This pattern was explicitly treated as exploratory.

It generated a new hypothesis rather than being presented as evidence
that the hypothesis was already true.

---

## 5. Held-out role-relational replication

A completely new 60-family stimulus bank was constructed.

Each factual family contained six conditions:

1. true plain direct;
2. true formal control;
3. true role-relational;
4. false plain direct;
5. false formal control;
6. false role-relational.

This produced:

- 60 factual families;
- 360 unique stimuli;
- 720 model evaluations after AB/BA counterbalancing.

Before model testing, the frozen bank was audited against previous
experimental material.

The audit found:

- exact previous overlaps: `0`;
- previous similarities >= `.90`: `0`;
- formal-control role contamination: `0`;
- missing role markers: `0`.

The preregistered primary comparison was:

`false_role_relational - false_formal_control`

Observed result:

- mean effect: `+0.0904`;
- median: `+0.1836`;
- positive rate: `58.3%`;
- Cohen's dz: `0.048`;
- `t(59) = 0.3734`;
- `p = .7102`;
- bootstrap 95% CI: `[-0.3928, 0.5546]`.

The broad role-relational hypothesis was not supported.

---

## 6. Construction-level heterogeneity

Exploratory decomposition of the held-out results showed substantial
construction-specific heterogeneity.

![Construction-level heterogeneity](assets/figures/figure_2_construction_heterogeneity_PORTFOLIO.png)

The most promising apparent pattern occurred for the specific
construction:

`functions as`

For the 10 exploratory `functions as` cases:

- false role-minus-formal effect: `+1.080`;
- false positive rate: `8/10`;
- true role-minus-formal effect: `-0.655`;
- true positive rate: `2/10`;
- false-minus-true interaction: `+1.735`.

Because this pattern was discovered after inspecting construction-level
results, it was treated as a new exploratory finding.

A new confirmatory dataset was required.

---

## 7. Focused preregistered `functions as` replication

The final study used a new preregistered focused replication.

Design:

- 30 completely new factual families;
- 4 conditions per family;
- 120 unique stimuli;
- AB/BA counterbalanced scoring;
- 240 total model evaluations.

Conditions:

1. `true_formal_control`;
2. `true_functions_as`;
3. `false_formal_control`;
4. `false_functions_as`.

The primary hypothesis was:

`false_functions_as - false_formal_control > 0`

The truth-dependent contrast was:

`(false_functions_as - false_formal_control) - (true_functions_as - true_formal_control)`

### Stimulus provenance

Before model testing, the focused bank was checked against all previous
experimental material.

The final audit found:

- previous stimulus texts checked: `640`;
- exact overlaps: `0`;
- similarities >= `.90`: `0`;
- reused subject families: `0`.

The 30 families were also source-checked before model testing.

The frozen dataset fingerprint is:

`64b3fd0cc9d0cba4f650789fc0a6e7b35787352fa17b15a5592cf885db48a14e`

### Primary result

The preregistered primary hypothesis was not supported.

False `functions as` minus formal-control effect:

- mean: `-0.0666`;
- median: `-0.0996`;
- positive rate: `36.7%`;
- Cohen's dz: `-0.166`;
- `t(29) = -0.9101`;
- `p = .3703`;
- bootstrap 95% CI: `[-0.2109, 0.0717]`.

Leave-one-item-out analyses also failed the preregistered robustness
criterion.

Domain-level estimates changed direction:

- biology: `-0.097`;
- computing: `+0.271`;
- engineering: `-0.364`;
- physics: `+0.172` (`n = 1`).

The apparent exploratory `functions as` false-claim effect therefore did
not replicate.

![Focused replication](assets/figures/figure_3_focused_replication_PORTFOLIO.png)

---

## Secondary truth-dependent effect

Although the primary hypothesis failed, the focused replication produced
an unexpected truth-dependent pattern.

For true claims, `functions as` reduced agreement relative to the matched
formal control:

- mean effect: `-0.3240`;
- positive rate: `13.3%`;
- `p = 1.59e-06`;
- bootstrap 95% CI: `[-0.4298, -0.2255]`.

This yielded a positive false-minus-true interaction:

- mean interaction: `+0.2574`;
- median interaction: `+0.2451`;
- `t(29) = 3.3542`;
- `p = .00223`;
- bootstrap 95% CI: `[0.1083, 0.4073]`.

This finding does **not** rescue the original epistemic-deference
hypothesis.

The interaction arose primarily because functional-role wording reduced
agreement with true claims, not because it reliably increased agreement
with false claims.

It is therefore retained as a secondary finding requiring independent
replication.

---

## Robustness across semantic domains

The focused primary effect was not stable across semantic domains.

![Domain robustness](assets/figures/figure_4_domain_robustness_PORTFOLIO.png)

Removing different domains changed the sign of the aggregate effect.

This was another reason the preregistered robustness criterion was not
met.

---

## Evidence gate

The project deliberately separates:

**behavioral discovery**

from:

**mechanistic interpretation**

Mechanistic localization was pre-specified to begin only if a robust
behavioral phenomenon survived replication.

The final focused primary hypothesis failed that criterion.

Therefore:

**Mechanistic gate: closed**

**Mechanistic localization: intentionally not pursued**

**Causal mechanism: not established**

No claim is made that the model contains an:

- authority circuit;
- indexical circuit;
- epistemic-deference circuit;
- causal sociolinguistic feature corresponding to the exploratory effects.

This stopping decision is part of the study design rather than an
unfinished stage of the project.

---

## Why the negative result matters

A large exploratory effect can be tempting to explain mechanistically.

But if the effect is unstable, stimulus-specific, or measurement-dependent,
a mechanistic analysis may produce an explanation for a pattern that does
not generalize.

Indexical Circuits therefore treats behavioral replication as a
precondition for causal interpretation.

The project demonstrates several safeguards:

- measurement-interface validation;
- AB/BA label-order counterbalancing;
- separation of exploratory and confirmatory analyses;
- newly constructed held-out stimulus banks;
- prior-data contamination audits;
- factual source verification;
- frozen stimulus sets;
- cryptographic dataset fingerprints;
- preregistered hypotheses;
- pre-specified success criteria;
- bootstrap uncertainty estimation;
- item-level robustness analysis;
- semantic-domain robustness analysis;
- explicit stopping rules;
- retention of null results.

---

## What this project supports

The project supports a methodological conclusion:

**linguistically plausible LLM effects that look strong in pilots or
exploratory subsets may disappear under independent replication.**

It also identifies an unresolved empirical question:

**why did functional-role wording reduce agreement with true claims in
the final focused dataset?**

That truth-dependent effect is a candidate for a future independent study.

It is not treated as confirmed here.

---

## What this project does not claim

This repository does not claim that:

- formal register reliably induces epistemic deference;
- technical vocabulary explains the apparent pilot effect;
- role-relational framing reliably increases false-claim agreement;
- `functions as` reliably increases false-claim agreement;
- the secondary truth-dependent interaction is independently replicated;
- a causal internal mechanism has been localized.

Those claims are not supported by the completed evidence sequence.

---

## Repository guide

### Research documentation

Key documents in `docs/` include:

- `hypotheses.md` — hypothesis development;
- `dataset_design.md` — experimental-data design;
- `behavioral_phenotyping.md` — exploratory linguistic coding;
- `heldout_role_relational_replication_preregistration.md` — held-out replication protocol;
- `functions_as_focused_replication_preregistration.md` — focused final preregistration;
- `register_realization_coding_manual.md` — linguistic annotation definitions;
- `experiment_log.md` — chronological research record;
- `results_and_lessons.md` — consolidated interpretation;
- `project_architecture.md` — project structure and workflow.

### Data

`data/` contains stimulus banks, validation material, linguistic coding,
and frozen held-out materials.

`data/functions_as_focused/` contains the final 30-family focused
replication bank together with its provenance and audit material.

### Results

`results/confirmatory/` contains broad confirmatory outputs.

`results/phenotyping/` contains exploratory linguistic phenotyping
outputs.

`results/functions_as_focused/` contains the final preregistered focused
replication outputs.

### Computational notebooks

The computational workflow is preserved in numbered notebooks:

- `00_environment_and_sanity_check.ipynb`
- `01_behavioral_pilot.ipynb`
- `02_stimulus_validation_materials.ipynb`
- `03_stimulus_validation_analysis.ipynb`
- `04_confirmatory_stimulus_bank.ipynb`
- `05_confirmatory_validation_materials.ipynb`
- `06_confirmatory_behavior.ipynb`

The notebooks are retained in research order rather than being rewritten
after the final result.

---

## Study history

| Stage | Status |
| --- | --- |
| Exploratory pilot | Apparent positive effect |
| Measurement audit | Interface corrected; pilot signal survived |
| Broad generic-formality replication | Not supported |
| Technical-lexicality explanation | Not supported |
| Exploratory role-relational candidate | Identified |
| Held-out role-relational replication | Not supported |
| Exploratory `functions as` candidate | Identified |
| Focused preregistered replication | Primary hypothesis not supported |
| Secondary truth-dependent interaction | Observed; requires independent replication |
| Mechanistic localization | Intentionally not pursued |

---

## Future work

A clean follow-up should not reinterpret the failed primary hypotheses as
successful.

The most defensible next study would independently test the unexpected
truth-dependent effect using:

- new factual families;
- a preregistered directional hypothesis;
- multiple functional-role constructions;
- multiple model families;
- matched controls;
- the same measurement-interface safeguards.

Only if such a behavioral effect replicates robustly should mechanistic
localization become the primary next step.

---

## Research areas

- mechanistic interpretability;
- behavioral evaluation;
- sociolinguistics;
- linguistic indexicality;
- register and relational construal;
- epistemic judgment;
- large language models;
- AI safety;
- reproducibility.

---

## Researcher

**Irene Theodoropoulou**

Linguist working at the intersection of sociolinguistics, language
variation, discourse, and artificial intelligence.

---

## Bottom line

The project began with an apparently large sociolinguistic effect on model
epistemic judgment.

The effect became weaker and ultimately failed as the experimental
evidence became more independent and more tightly controlled.

Rather than localizing a mechanism anyway, the study obeyed its
pre-specified evidence gate and stopped.

For mechanistic interpretability, knowing when **not** to explain a
behavior is part of the research.
