# Stimulus Validation Analysis Plan

## Purpose

This document specifies the analysis of the human stimulus-validation data before inspection of the substantive ratings.

Two independent groups of raters will evaluate:

1. sentence-level linguistic properties;
2. semantic equivalence of matched plain/formal pairs.

The aim is to identify stimulus pairs suitable for a larger confirmatory behavioral experiment.

## Participant inclusion

Responses will be included when:

- the participant provides consent;
- the participant is aged 18 or above;
- English proficiency is Advanced, Native, or Near-native;
- the required ratings are substantially complete.

The sentence-level and semantic-equivalence validation samples will consist of independent participant groups.

## Sentence-level validation

For each stimulus, mean ratings will be calculated for:

- formality
- assertiveness / confidence
- politeness
- naturalness
- perceived expertise / authority
- evidential strength

The human ratings will then be joined to the researcher-only master file using `stimulus_id`.

For each matched plain/formal pair, formal-minus-plain differences will be calculated.

### Primary manipulation check

A pair will pass the formality manipulation check when:

- mean formality of the formal version is at least 1.0 point higher than the corresponding plain version.

### Control dimensions

A pair will normally be retained when:

- absolute assertiveness/confidence difference <= 0.75;
- absolute politeness difference <= 0.75;
- absolute evidential-strength difference <= 0.75;
- mean naturalness >= 4.5 for both variants.

### Perceived expertise / authority

Perceived expertise/authority will be analysed but will not be treated as a matching requirement.

A positive formal-minus-plain authority difference is theoretically relevant because perceived epistemic authority is a candidate mediator between linguistic register and model deference.

## Semantic-equivalence validation

For each matched pair, calculate:

- mean semantic-equivalence score;
- proportion of `Yes` responses to the same-factual-proposition question;
- proportion of `No`;
- proportion of `Unsure`.

The primary semantic-equivalence criterion is:

- mean semantic-equivalence rating >= 6.0.

The categorical same-proposition response will be used as an additional diagnostic. Pairs receiving fewer than 80% `Yes` responses will be flagged for manual review.

## Pair-level validation decision

Each pair will be classified as:

- PASS
- REVIEW
- FAIL

A PASS pair should normally satisfy:

1. formality difference >= +1.0;
2. semantic equivalence >= 6.0;
3. assertiveness/confidence difference <= 0.75 in absolute value;
4. politeness difference <= 0.75 in absolute value;
5. evidential-strength difference <= 0.75 in absolute value;
6. naturalness >= 4.5 for both variants.


### Review and fail criteria

A pair will be classified as `PASS` when all primary validation criteria are satisfied.

A pair will be classified as `REVIEW` when it does not satisfy all PASS criteria but does not meet any FAIL criterion. REVIEW therefore identifies potentially usable pairs requiring linguistic inspection or revision.

A pair will be classified as `FAIL` when one or more of the following substantial problems occurs:

- formal-minus-plain formality difference <= 0;
- mean semantic-equivalence rating < 5.0;
- fewer than 60% of raters judge the pair to express the same factual proposition;
- mean naturalness < 3.5 for either variant;
- absolute plain-formal difference > 1.5 for assertiveness/confidence;
- absolute plain-formal difference > 1.5 for politeness;
- absolute plain-formal difference > 1.5 for evidential strength.

Values falling between the PASS and FAIL thresholds will be classified as REVIEW.

Thus, for example:

- semantic equivalence >= 6.0 supports PASS;
- semantic equivalence from 5.0 to < 6.0 produces REVIEW;
- semantic equivalence < 5.0 produces FAIL.

Likewise, an absolute control-dimension difference:

- <= 0.75 supports PASS;
- > 0.75 and <= 1.5 produces REVIEW;
- > 1.5 produces FAIL.

These thresholds are pre-specified for stimulus screening and are not inferential statistical significance thresholds.


## Reliability and diagnostics

Rater distributions and disagreement will be inspected before relying on means alone.

Inter-rater reliability will be estimated for the principal rating dimensions where appropriate.

Outliers or unusual ratings will not be removed solely because they weaken the predicted effect.

## Confirmatory stimulus bank

Validation results will be used to create a new stimulus bank rather than modifying the historical pilot.

The confirmatory design will preferentially use matched factual families containing:

- true + plain;
- true + formal;
- false + plain;
- false + formal.

A subset of validated stimulus families will be held out for later mechanistic-generalization testing.
