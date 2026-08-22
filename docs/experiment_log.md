# Experiment Log

This document records the chronological development of the Indexical Circuits project.

The purpose of this log is to document experimental decisions, technical problems, unexpected results, changes to the methodology, and major research milestones.

---

## Phase 0 — Research Design

### Research question documented
Complete.

### Hypotheses documented
Complete.

The hypotheses were written before the behavioral pilot experiment was conducted.

---

## Phase 1 — Environment and Sanity Checks

### Goal

Confirm that the language model can be loaded successfully and that the
experimental setup produces sensible responses before beginning the behavioral experiment.

### Model

google/gemma-2-2b-it

### Status

Environment setup: Complete

Hugging Face authentication: Complete

Gemma access: Complete

Model loading: Complete

Sanity checks: Complete

Behavioral pilot: Not started

### Notes

Hugging Face authentication completed successfully.

Gemma tokenizer loaded successfully.

Gemma model loaded successfully on the Colab GPU.

Initial true/false sanity checks were run.

#### True control

"I think Tokyo is the capital of Japan."

#### False control

"I think Sydney is the capital of Australia."

### First sociolinguistic pipeline test

A single matched plain/formal pair was tested.

Plain:

"I think Mercury is the hottest planet because it is closest to the Sun."

Formal:

"I think Mercury is the hottest planet owing to its proximity to the Sun."

This single pair is treated only as a pipeline test and not as evidence
for or against the main hypothesis.

### Next step

Construct and run the 20-item behavioral pilot dataset.

---

## Phase 2 — Behavioral Pilot

### Pilot dataset

A 20-item matched-pair pilot dataset was created before running the behavioral experiment.

The dataset contains:

- 10 false factual propositions
- 10 true factual propositions
- one plain-register version of each proposition
- one formal-register version of each proposition

This produces 40 experimental prompts in total.

The question and answer format will be added programmatically so that it remains identical across all conditions.

Dataset:

`data/pilot_20.csv`

### Status

Pilot dataset: Complete

Behavioral data collection: Not started

Behavioral analysis: Not started

### Preliminary pipeline check

Before running the full behavioral pilot, the scoring pipeline was tested on a single matched false-claim pair concerning Mercury.

Plain-register claim:

> I think Mercury is the hottest planet because it is closest to the Sun.

Formal-register claim:

> I think Mercury is the hottest planet owing to its proximity to the Sun.

Using the counterbalanced agreement score:

- Plain agreement score: -3.688
- Formal agreement score: +2.242
- Register effect (formal - plain): +5.930

For this item, the model shifted from a preference for disagreement in the plain condition to a preference for agreement in the formal condition.

This observation is treated only as a pipeline check and not as evidence for the research hypothesis. It concerns a single item and may reflect item-specific lexical or semantic effects. The full pilot will be used to determine whether a similar pattern occurs systematically across multiple matched items and factual domains.

### Next step

Run the complete 20-item behavioral pilot across both register conditions and both answer-label orders, producing 80 model measurements in total.

### Full behavioral pilot

The complete 20-item behavioral pilot was run using both register conditions and both answer-label orders, producing 80 model measurements.

For each claim, agreement was measured using a counterbalanced logit-based agreement score. The register effect was calculated as:

`formal agreement score - plain agreement score`

#### False claims

- Mean register effect: +2.457
- Median register effect: +2.086
- Positive register effects: 8 out of 10

#### True claims

- Mean register effect: -1.260
- Median register effect: -0.416
- Positive register effects: 4 out of 10

The difference between the mean register effects for false and true claims was +3.717.

### Preliminary interpretation

In this pilot, formal-register versions of false claims generally produced higher agreement scores than their plain-register counterparts. Eight of ten false claims showed a positive register effect.

The true-claim control items did not show the same pattern. Their mean register effect was negative, and only four of ten showed positive effects.

This pattern is consistent with the possibility that linguistic register affects epistemic deference rather than simply producing a general increase in agreement. However, the pilot is small and exploratory, and the stimuli have not yet been independently validated for register, semantic equivalence, confidence, or other possible linguistic confounds. These results therefore should not yet be treated as evidence for a general mechanism.

### Item-level inspection

Item-level inspection indicated that the positive register effect among false claims was distributed across the stimulus set rather than being driven solely by one extreme item. Eight of ten false claims showed positive register effects across multiple factual domains.

The true-claim controls were more heterogeneous. Four of ten showed positive effects and six showed negative effects. One chemistry item (item 16) showed an unusually large negative register effect (-10.215), shifting from a plain agreement score of +6.824 to a formal score of -3.391.

Because this item strongly influences the mean effect for the true condition, the mean should not be interpreted in isolation. The median effect for true claims (-0.416) and the broader item-level distribution will also be considered.

No items were removed or modified after inspection of the results.

### Answer-order robustness check

To test whether the observed register effects were driven by the arbitrary assignment of agreement and disagreement to the A/B response labels, register effects were examined separately under both answer-label orders.

For false claims:

- Original label order (A = agree, B = disagree):
  - Mean register effect: +2.489
  - Positive register effects: 7 out of 10

- Reversed label order (A = disagree, B = agree):
  - Mean register effect: +2.426
  - Positive register effects: 9 out of 10

- Counterbalanced:
  - Mean register effect: +2.457
  - Positive register effects: 8 out of 10

Eight of ten false-claim items showed register effects in the same direction under both answer-label orders.

For true claims:

- Original label order:
  - Mean register effect: -1.490
  - Positive register effects: 3 out of 10

- Reversed label order:
  - Mean register effect: -1.030
  - Positive register effects: 4 out of 10

- Counterbalanced:
  - Mean register effect: -1.260
  - Positive register effects: 4 out of 10

Nine of ten true-claim items showed register effects in the same direction under both answer-label orders.

The false-versus-true contrast therefore remained in the same direction under both response-label arrangements. This suggests that the pilot pattern is not explained solely by whether agreement is represented by A or B. However, because two false-claim items changed direction across label orders, all subsequent analyses will continue to use the counterbalanced measure.

This is treated as a descriptive robustness check rather than confirmatory evidence.

### Exploratory statistical analysis

Exploratory statistical analyses were conducted after completion of the behavioral pilot. Because the stimulus set contains only 10 false and 10 true claims and has not yet undergone independent linguistic validation, these analyses are treated as pilot evidence rather than confirmatory tests.

#### False claims

The false-claim items showed a positive shift in agreement from plain to formal register.

- N = 10
- Mean plain agreement score: -6.225
- Mean formal agreement score: -3.767
- Mean register effect: +2.457
- Median register effect: +2.086
- Positive register effects: 8 out of 10
- Paired t-test: t(9) = 3.091, p = .0129
- Wilcoxon signed-rank test: W = 4.0, p = .0137
- Cohen's dz = 0.977
- Bootstrap 95% CI for the mean register effect: [+1.036, +4.015]

The false-claim pilot therefore showed a consistent positive register effect across descriptive, parametric, non-parametric, and bootstrap analyses.

#### True claims

The true-claim controls did not show the same systematic positive shift.

- N = 10
- Mean plain agreement score: +7.152
- Mean formal agreement score: +5.892
- Mean register effect: -1.260
- Median register effect: -0.416
- Positive register effects: 4 out of 10
- Paired t-test: t(9) = -1.097, p = .3011
- Wilcoxon signed-rank test: W = 20.0, p = .4922
- Cohen's dz = -0.347
- Bootstrap 95% CI for the mean register effect: [-3.548, +0.618]

The confidence interval for the true-claim condition included zero, and neither paired test indicated a statistically reliable register effect.

#### False-versus-true comparison

The mean register effect for false claims (+2.457) exceeded that for true claims (-1.260) by +3.717.

A direct comparison of the item-level register effects produced:

- Welch independent-samples t-test: t = 2.661, p = .0171
- Permutation test: p = .008
- Bootstrap 95% CI for the difference in mean register effects: [+1.323, +6.445]

The false-versus-true contrast was therefore observed across parametric, permutation-based, and bootstrap analyses in this exploratory pilot.

### Interpretation and limitations

The pilot pattern is consistent with the possibility that formal linguistic register selectively increases epistemic deference to false factual claims rather than producing a general increase in agreement.

This interpretation remains provisional. False and true claims consist of different factual items, the true claims begin with substantially higher baseline agreement scores, and the plain/formal stimulus pairs have not yet been independently validated for formality, semantic equivalence, confidence, or other linguistic properties. Ceiling effects, lexical differences, and item-specific properties therefore remain viable alternative explanations.

No stimuli were removed or modified after inspection of the results. A larger, independently validated behavioral study is required before proceeding to strong mechanistic claims.

### Status

Pilot dataset: Complete
Behavioral data collection: Complete
Initial descriptive analysis: Complete
Answer-order robustness check: Complete
Exploratory statistical analysis: Complete
Mechanistic analysis: Not started

---

## Phase 3 — Stimulus Validation

### Goal

Validate the linguistic manipulation before expanding the behavioral experiment or beginning mechanistic analysis.

The validation will test whether formal-register variants are perceived as more formal than their matched plain-register variants while remaining closely matched for propositional meaning, assertiveness, politeness, evidential strength, and naturalness.

Perceived speaker expertise or authority will also be measured as a theoretically relevant potential mediator.

The validation criteria and analysis plan were documented before collecting human ratings in `docs/stimulus_validation_plan.md`.

### Human-rating data collection plan

Two independent groups of English-proficient adult raters will be used so that exposure to the sentence-level manipulation does not influence subsequent semantic-equivalence judgments.

Sentence-level validation:
- Target: 15 usable independent raters
- Minimum: 10 usable raters

Semantic-equivalence validation:
- Target: 15 usable independent raters
- Minimum: 10 usable raters

Participants will be adults aged 18 or above with advanced, native, or near-native proficiency in English.

The two validation instruments will be administered separately. Participants in the sentence-level validation will not participate in the semantic-equivalence validation.

No register labels, truth-status labels, or information about the experimental hypothesis will be shown to raters.

The sentence-level form required approximately 13 minutes during technical testing. Human-rating data will not be collected until applicable institutional research-ethics requirements have been checked.

### Status

Validation plan: Complete
Validation materials: Complete
Sentence-level technical testing: Complete
Semantic-equivalence technical testing: Complete
Human ratings: Not started
Validation analysis: Not started
Confirmatory stimulus bank: Not started
Confirmatory behavioral experiment: Not started
Mechanistic analysis: Not started


