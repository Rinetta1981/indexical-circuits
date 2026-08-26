# Focused `functions_as` Replication

## Status

This hypothesis was specified after exploratory construction-level analysis of the
60-family held-out role-relational experiment and before construction or model
testing of the new focused stimulus bank.

It is therefore a new confirmatory replication of an exploratory finding.

## Exploratory Motivation

The broad held-out role-relational hypothesis was not supported.

Primary held-out result:

- mean false role-relational minus formal-control effect = +0.0904
- t(59) = 0.3734
- p = .7102
- bootstrap 95% CI = [-0.3928, 0.5546]

Construction-level exploratory analysis revealed substantial heterogeneity.

For the `functions_as` construction:

- n = 10
- false role-minus-formal effect = +1.080
- false positive rate = 8/10
- true role-minus-formal effect = -0.655
- true positive rate = 2/10
- false-minus-true interaction = +1.735

This pattern motivates a new focused replication.

## Primary Hypothesis

For false claims:

`false_functions_as - false_formal_control > 0`

## Interaction Hypothesis

The `functions_as` effect will be larger for false than true claims:

`(false_functions_as - false_formal_control)
-
(true_functions_as - true_formal_control) > 0`

## Design

The replication will use:

- 30 completely new factual families
- 4 conditions per family
- 120 stimuli
- AB/BA counterbalanced scoring
- 240 total model evaluations

Conditions:

1. true_formal_control
2. true_functions_as
3. false_formal_control
4. false_functions_as

None of the factual propositions used in the pilot, confirmatory experiment,
or previous held-out experiment may be reused.

## Model

`google/gemma-2-2b-it`

The same frozen Gemma chat-template interface and counterbalanced agreement-score
procedure will be used.

## Primary Success Criteria

The focused replication will be considered successful if:

1. the mean false `functions_as` effect is positive;
2. its bootstrap 95% CI excludes zero positively;
3. its paired two-sided t-test has p < .05;
4. the false-minus-true interaction is positive;
5. the result is not driven by one extreme item or one semantic domain.

## Mechanistic Gate

Mechanistic localization and causal intervention will begin only if this new
focused replication supports the `functions_as` behavioral effect.
