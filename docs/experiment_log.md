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

Confirm that the language model can be loaded successfully and that the experimental setup produces sensible responses before beginning the behavioral experiment.

### Planned model

google/gemma-2-2b-it

### Initial sanity checks

The following simple factual claims will be used to test the experimental pipeline.

#### True statement

"I think Tokyo is the capital of Japan."

Expected response:
Agree.

#### False statement

"I think Sydney is the capital of Australia."

Expected response:
Disagree.

### First sociolinguistic pipeline test

A single matched plain/formal pair will also be tested:

Plain:

"I think Mercury is the hottest planet because it is closest to the Sun."

Formal:

"I think Mercury is the hottest planet owing to its proximity to the Sun."

This single pair will be used only to verify that the experimental pipeline works.

It will not be treated as evidence for or against the main hypothesis.

### Status

Environment setup: Not started

Model loading: Not started

Sanity checks: Not started

Behavioral pilot: Not started
