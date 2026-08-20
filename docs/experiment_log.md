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

### Status

Pilot dataset: Complete
Behavioral data collection: Complete
Initial descriptive analysis: Complete
Mechanistic analysis: Not started


