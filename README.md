# Indexical Circuits

**Mechanistically tracing how linguistic register may influence epistemic deference in language models.**

## Research Question

Can the way a person speaks make a language model trust them more, even when what they say is wrong?

## Core Idea

Language communicates more than factual information. Features of linguistic style and register can also signal social meanings such as expertise, authority, status, confidence, and identity.

This project investigates whether a language model internally represents such sociolinguistic signals and whether those representations influence how the model evaluates a user's claims.

The proposed pathway is:

**Linguistic register → internal representation of the speaker → perceived epistemic authority → model deference**

## Experimental Plan

The project will proceed in four stages:

1. **Behavioral experiment**  
   Test whether changing linguistic register changes the model's willingness to agree with a user's factual claim.

2. **Mechanistic analysis**  
   Identify internal model features that differ between plain-register and formal-register prompts.

3. **Causal intervention**  
   Manipulate candidate internal features to test whether they causally affect model deference.

4. **Generalization**  
   Test whether the discovered mechanism also appears in new, previously unseen prompts.

## Current Status

🟡 **Phase 0 — Project setup and experimental design**

No empirical results are reported yet.

## Model

Initial experiments will use an open-weight instruction-tuned language model suitable for mechanistic interpretability experiments.

## Research Areas

- Mechanistic interpretability
- Sociolinguistics
- Linguistic indexicality
- Large language models
- AI safety
- Epistemic deference

## Repository Structure

The repository will gradually contain:

- experimental datasets
- Colab notebooks
- behavioral results
- mechanistic interpretability analyses
- causal intervention experiments
- figures and visualizations
- methodological documentation

## Researcher

**Irene Theodoropoulou**

Linguist working at the intersection of sociolinguistics, language variation, discourse, and artificial intelligence.
