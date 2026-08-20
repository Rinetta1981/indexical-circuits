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


