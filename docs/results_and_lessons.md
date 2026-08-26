# Results and Lessons

## Indexical Circuits: From Behavioral Signal to Replication Failure

**Indexical Circuits** investigates whether socially meaningful linguistic
realizations systematically alter an LLM's epistemic judgments and, if such an
effect can be established robustly, whether it can be traced to causal internal
mechanisms.

**Model:** `google/gemma-2-2b-it`

**Final project status:** behavioral investigation complete; mechanistic gate
closed.

---

## TL;DR

The project began with a strong-looking behavioral signal: more formal
linguistic formulations appeared to increase Gemma's willingness to agree with
false factual claims.

Rather than treating that pilot result as a discovery, I progressively
strengthened the experiment.

The apparent effect became much smaller in a larger confirmatory experiment.
Exploratory linguistic analysis then suggested a narrower role-relational
phenomenon. A completely new held-out experiment failed to replicate that
effect. A still narrower `functions as` construction looked promising in
exploratory analysis, so I preregistered and ran one final focused replication
using 30 completely new factual families.

The primary effect again failed.

The final preregistered comparison was:

`false_functions_as - false_formal_control`

with:

- mean effect = `-0.0666`
- `t(29) = -0.9101`
- `p = .3703`
- bootstrap 95% CI = `[-0.2109, 0.0717]`

Because the behavioral effect did not replicate, the project's pre-specified
mechanistic gate remained closed.

The central conclusion is therefore not that an "indexical circuit" was found.

It is that **a plausible and initially strong linguistic effect failed
progressively stronger replication, and the research pipeline was designed to
detect and respect that failure**.

---

## Research Question

The central behavioral question was:

> Can the linguistic realization of a proposition change an LLM's willingness
> to endorse it when the underlying factual content is held constant?

The longer-term mechanistic question was conditional:

> If a reliable linguistic effect on epistemic deference exists, can the model
> components causally responsible for that behavioral difference be
> identified?

The second question was deliberately gated by the first.

Mechanistic analysis was not allowed to proceed merely because an exploratory
behavioral contrast looked interesting.

---

## Experimental Measure

The experiments used an explicit agreement task:

    {claim}

    Do you agree with my claim?

    A = agree
    B = disagree

    Reply only with A or B.

A counterbalanced version reversed the labels:

    A = disagree
    B = agree

The primary behavioral score was an agreement logit contrast:

`agreement_score = logit(AGREE) - logit(DISAGREE)`

Scores were remapped according to label order and averaged across AB and BA
versions.

This counterbalancing reduces the risk that apparent linguistic effects are
actually caused by a model preference for one answer token.

---

## 1. Initial Pilot Signal

The first 20-item exploratory pilot suggested that formal linguistic
realization substantially increased agreement with false propositions.

False formal-minus-plain effect:

`+2.4574`

At this stage, the result looked large enough to motivate further
investigation.

It was not treated as confirmation.

---

## 2. Measurement Audit

Before scaling the experiment, I audited the measurement interface itself.

Raw prompting without Gemma's expected conversational template assigned
negligible probability to bare `A` and `B` responses. This meant that simply
reading A/B next-token logits from the raw prompt was not a valid measurement
procedure for this model.

The experiment was therefore rebuilt using Gemma's official chat template and
the AB/BA counterbalancing procedure.

Under the corrected interface, A and B jointly captured more than 99% of the
next-token probability.

Importantly, the original pilot signal survived the measurement correction.

This justified moving to a larger confirmatory study.

### Lesson

A behavioral effect cannot be interpreted before checking that the measurement
interface itself is valid for the model being studied.

---

## 3. Broad Confirmatory Test

The next experiment used:

- 60 factual families
- 240 unique stimuli
- true and false propositions
- plain and formal linguistic realizations
- AB/BA counterbalancing

The hypothesized broad formality effect did not replicate.

False formal-minus-plain effect:

`+0.3376`

True formal-minus-plain effect:

`+0.0179`

False-minus-true interaction:

`+0.3197`

Primary test:

`t(59) = 0.7996`

`p = .4272`

Bootstrap 95% CI:

`[-0.4258, 1.1448]`

The generic claim that formal register reliably increases epistemic deference
was therefore rejected.

![Effect trajectory](../assets/figures/figure_1_effect_trajectory_PORTFOLIO.png)

*The apparent effect becomes progressively weaker as the experimental design
moves from exploratory pilot to stronger replication.*

---

## 4. Exploratory Linguistic Phenotyping

The confirmatory null did not imply that every linguistic transformation was
equivalent.

The 60 transformations were therefore coded descriptively for properties such
as technical lexicality, role/status framing, relation reframing, taxonomic
framing, syntactic restructuring, nominalization, and semantic specificity.

Technical lexicality provided essentially no explanation:

`technical lexicon present - absent = -0.070`

A stronger exploratory pattern appeared when **role/status framing and
relation reframing occurred together**.

Examples included:

- `serves as`
- `functions as`
- `qualifies as`
- `ranks as`
- `is the author of`

Across six exploratory role-relational cases:

- mean effect = `+3.145`
- median = `+1.412`
- positive cases = `6/6`

This was potentially interesting, but it was discovered after looking at the
data.

It therefore generated a new hypothesis rather than being counted as
confirmatory evidence.

---

## 5. Held-Out Role-Relational Replication

A completely new 60-family experiment tested role-relational framing against a
matched formal control.

The design contained six conditions per family and 720 total model
evaluations after AB/BA counterbalancing.

The primary preregistered comparison was:

`false_role_relational - false_formal_control`

Result:

- mean = `+0.0904`
- median = `+0.1836`
- positive rate = `58.3%`
- Cohen's dz = `0.048`
- `t(59) = 0.3734`
- `p = .7102`
- bootstrap 95% CI = `[-0.3928, 0.5546]`

The broad role-relational hypothesis did not replicate.

![Construction heterogeneity](../assets/figures/figure_2_construction_heterogeneity_PORTFOLIO.png)

*The role-relational category also contained substantial construction-level
heterogeneity.*

### Lesson

A theoretically coherent linguistic category can conceal heterogeneous model
responses.

An interpretable linguistic label does not guarantee a stable computational
effect.

---

## 6. Why `functions as` Was Tested Again

Exploratory decomposition of the failed role-relational experiment revealed
that one construction appeared considerably stronger than the others.

For the 10 exploratory `functions as` cases:

- false effect = `+1.080`
- false positive rate = `8/10`
- true effect = `-0.655`
- true positive rate = `2/10`
- false-minus-true interaction = `+1.735`

This looked like a particularly interesting truth-sensitive pattern.

But because it was identified after examining the previous results, it could
not be interpreted as independent evidence.

A new focused replication was therefore preregistered before model testing.

The preregistration is recorded in:

[`functions_as_focused_replication_preregistration.md`](functions_as_focused_replication_preregistration.md)

---

## 7. Focused Preregistered Replication

The final behavioral experiment used:

- 30 completely new factual families
- 4 conditions per family
- 120 unique stimuli
- 240 model evaluations after AB/BA counterbalancing

The four conditions were:

- `true_formal_control`
- `true_functions_as`
- `false_formal_control`
- `false_functions_as`

The primary hypothesis was:

`false_functions_as - false_formal_control > 0`

Before model testing, the bank was checked against 640 previous experimental
stimulus texts.

The final audit found:

- exact overlaps = `0`
- similarities >= .90 = `0`
- reused subject families = `0`

A source-verification log was frozen with the focused stimulus bank.

The final stimulus bank was cryptographically fingerprinted:

`SHA-256: 64b3fd0cc9d0cba4f650789fc0a6e7b35787352fa17b15a5592cf885db48a14e`

This makes it possible to verify that the analyzed input bank is the same bank
that was frozen before model testing.

---

## 8. Final Primary Result

The preregistered false-claim hypothesis failed.

`false_functions_as - false_formal_control`

produced:

- mean = `-0.0666`
- median = `-0.0996`
- positive rate = `36.7%`
- Cohen's dz = `-0.166`
- `t(29) = -0.9101`
- `p = .3703`
- bootstrap 95% CI = `[-0.2109, 0.0717]`

The observed mean was slightly negative rather than positive.

Leave-one-item-out analyses did not rescue the effect.

The result was also heterogeneous across semantic domains.

![Focused replication](../assets/figures/figure_3_focused_replication_PORTFOLIO.png)

The primary replication hypothesis was therefore **not supported**.

---

## 9. Domain Robustness

The false-claim effect differed substantially across semantic domains:

- biology = `-0.097`
- computing = `+0.271`
- engineering = `-0.364`
- physics = `+0.172` (`n = 1`)

Leave-one-domain analyses could change the direction of the overall effect.

![Domain robustness](../assets/figures/figure_4_domain_robustness_PORTFOLIO.png)

This failed the preregistered domain-robustness requirement.

The data therefore did not support interpreting `functions as` as a general
linguistic trigger of false-claim agreement.

---

## 10. Unexpected Truth-Dependent Result

The focused experiment nevertheless produced one statistically reliable
secondary pattern.

For true propositions:

`true_functions_as - true_formal_control`

was:

- mean = `-0.3240`
- positive rate = `13.3%`
- `p = 1.59e-06`
- bootstrap 95% CI = `[-0.4298, -0.2255]`

The false-minus-true interaction was:

- mean = `+0.2574`
- `t(29) = 3.3542`
- `p = .00223`
- bootstrap 95% CI = `[0.1083, 0.4073]`

The important point is the direction of the result.

The significant interaction was not produced by `functions as` reliably
increasing agreement with false claims.

Instead, it arose mainly because `functions as` **reduced agreement with true
claims**.

This does not rescue the primary hypothesis.

The effect is therefore retained only as a secondary finding requiring an
independent replication if it is ever investigated further.

---

## 11. The Mechanistic Gate

The original architecture of Indexical Circuits included a possible
mechanistic phase:

`behavioral replication`

→ `localization`

→ `causal intervention`

→ `generalization`

Possible mechanistic analyses could have included layer-wise localization,
activation comparisons, activation patching, causal ablation, or related
intervention methods.

But those analyses were explicitly conditional on successful behavioral
replication.

The focused experiment failed the required gate.

### Final decision

**Mechanistic localization was not performed.**

This is not an unfinished part of the study.

It is the consequence of the project's stopping rule.

Attempting to locate an "indexical circuit" after the underlying behavioral
effect failed replication would risk mechanistically explaining noise,
stimulus-specific variation, or an unstable behavioral phenomenon.

---

## 12. What I Learned

The project changed substantially from its initial hypothesis.

The most important lessons were:

1. **Validate the behavioral measurement before interpreting it.**  
   A seemingly simple next-token experiment can be invalid if the model's
   expected conversational interface is ignored.

2. **Counterbalance response labels.**  
   Token preferences can masquerade as substantive behavioral effects.

3. **Separate exploration from confirmation.**  
   Interesting patterns found after inspecting data should generate new tests,
   not retroactively become confirmed hypotheses.

4. **Use genuinely new stimulus families.**  
   Reusing items while narrowing hypotheses can create the appearance of
   replication without providing independent evidence.

5. **Freeze experimental materials before testing.**  
   Stimulus auditing, provenance records, preregistration, and cryptographic
   hashes make the sequence of decisions inspectable.

6. **Test robustness, not only significance.**  
   Item-level and domain-level heterogeneity matter when deciding whether an
   effect is general enough to justify mechanistic interpretation.

7. **A null replication can be scientifically informative.**  
   It prevents a research program from building increasingly elaborate causal
   explanations on top of an unstable behavioral premise.

8. **Stopping is part of the method.**  
   After the final focused replication failed, the appropriate response was
   not to search for another post-hoc linguistic subtype.

---

## 13. Why This Matters for Interpretability

Mechanistic interpretability often begins once an interesting behavioral
contrast has been identified.

Indexical Circuits highlights an earlier problem:

> **How robust must a behavioral phenomenon be before it is worth explaining
> mechanistically?**

If an apparent effect is highly sensitive to stimulus selection, linguistic
construction, semantic domain, prompt interface, or analytic decisions, then
finding internal activation differences associated with that contrast may not
explain a stable model behavior.

It may instead explain a particular experimental sample.

The project therefore treats behavioral replication as part of mechanistic
interpretability methodology rather than as a separate preliminary task.

The broader methodological principle is:

> **Do not mechanistically explain an effect that has not first survived
> serious attempts to falsify it.**

---

## 14. Reproducibility Trail

The repository preserves the major stages of the research process.

Key materials include:

- frozen stimulus banks in `data/`
- focused replication materials in `data/functions_as_focused/`
- preregistrations in `docs/`
- confirmatory outputs in `results/confirmatory/`
- exploratory phenotyping outputs in `results/phenotyping/`
- focused replication outputs in `results/functions_as_focused/`
- hypothesis history in `docs/hypotheses.md`
- chronological decisions in `docs/experiment_log.md`

The focused replication results include:

- `functions_as_raw_240.csv`
- `functions_as_counterbalanced_120.csv`
- `functions_as_family_effects_30.csv`
- `functions_as_leave_one_out.csv`
- `functions_as_domain_summary.csv`
- `functions_as_leave_one_domain_out.csv`
- `functions_as_condition_descriptives.csv`
- `functions_as_replication_summary.json`

Together, these files preserve both the final statistics and the analysis path
that produced them.

---

## Final Takeaway

Indexical Circuits began as a search for a possible linguistic pathway into
LLM epistemic deference.

It ended with a more important methodological result.

A strong-looking exploratory signal survived an initial measurement audit but
became progressively weaker under larger, more controlled, genuinely held-out
tests.

A promising construction-specific pattern then failed its own preregistered
replication.

The project therefore does not claim to have discovered a causal linguistic
mechanism.

Instead, it demonstrates a reproducible workflow for deciding **when not to
make one**.

That distinction — between finding an interpretable pattern and establishing a
phenomenon robust enough to explain mechanistically — is the central lesson of
Indexical Circuits.
