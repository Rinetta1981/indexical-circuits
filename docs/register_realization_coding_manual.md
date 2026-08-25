# Register-Realization Coding Manual

## Purpose

This coding scheme is used for the exploratory behavioral phenotyping stage of Indexical Circuits.

The aim is to identify which linguistic transformations distinguish plain from formal stimulus versions.

Coding must be completed without access to the model's register-effect scores.

The coding describes linguistic form only. It does not judge whether a transformation should increase or decrease model agreement.

---

## General coding rule

For the following binary categories, use:

- `1` = clearly present
- `0` = clearly absent
- `U` = genuinely unclear

A pair may receive more than one code because register transformations can involve several linguistic processes simultaneously.

Do not infer a feature merely because a sentence sounds more formal overall. Code only features that can be identified from the actual plain → formal transformation.

---

## 1. Technical lexicon

Column:

`technical_lexicon`

### Code 1 when:

The formal version introduces terminology that is recognizably more specialized, disciplinary, scientific, technical, or field-specific than the plain version.

### Examples

Plain:
`Mars has three moons.`

Formal:
`Mars possesses three natural satellites.`

Code:

`1`

because `natural satellites` is a more technical astronomical term than `moons`.

Plain:
`A square has three equal sides.`

Formal:
`A square possesses three congruent sides.`

Code:

`1`

because `congruent` is more specialized mathematical terminology.

### Code 0 when:

The change is stylistically elevated but not meaningfully more technical.

Example:

`was written by` → `was authored by`

This is lexical elevation, not necessarily technical terminology.

---

## 2. Role or status framing

Column:

`role_or_status_framing`

### Code 1 when:

The formal version frames an entity, institution, concept, or relationship explicitly in terms of role, status, official function, qualification, designation, or recognized standing.

Typical cues may include expressions such as:

- `serves as`
- `functions as`
- `qualifies as`
- `is designated as`
- `constitutes`
- `holds the status of`

### Example

Plain:

`Sydney is the capital of Australia.`

Formal:

`Sydney serves as Australia's national capital.`

Code:

`1`

because the formal version construes the relationship as an institutional role.

### Important

Do not automatically code every use of `constitutes` or `qualifies as` as status framing. The construction must actually present something in terms of role, status, recognized function, or membership.

---

## 3. Taxonomic or categorical framing

Column:

`taxonomic_or_categorical_framing`

### Code 1 when:

The formal version more explicitly represents the proposition as classification, category membership, type membership, or formal categorization.

Typical cues include:

- `qualifies as`
- `belongs to`
- `is classified as`
- `constitutes a`
- `falls within`
- `is designated as`

### Example

Plain:

`HTML is a programming language.`

Formal:

`HTML qualifies as a programming language.`

Code:

`1`

because the formal version foregrounds category membership.

Another example:

`Granite is a sedimentary rock.`

→

`Granite belongs to the sedimentary rock class.`

Code:

`1`

---

## 4. Relation reframing

Column:

`relation_reframing`

### Code 1 when:

The formal version expresses the same factual relation through a substantially different predicate or relational structure.

### Examples

`Earth's revolution causes day and night.`

→

`Day and night result from Earth's revolution.`

Code:

`1`

because the causal relation has been reframed.

`CPU stands for X.`

→

`CPU is an abbreviation for X.`

Code:

`1`

because the abbreviation relation is expressed differently.

### Code 0 when:

The transformation consists mainly of a lexical substitution without restructuring the underlying relation.

Example:

`contains` → `comprises`

may remain primarily lexical unless the proposition is otherwise structurally reframed.

---

## 5. Syntactic restructuring

Column:

`syntactic_restructuring`

### Code 1 when:

The formal version substantially changes grammatical structure while preserving the intended proposition.

Possible cases include:

- active → passive;
- subject/object reorganization;
- clause inversion;
- substantial change in grammatical construction;
- verbal clause → copular structure;
- cause → result construction.

### Example

Plain:

`Earth's revolution causes day and night.`

Formal:

`Day and night result from Earth's revolution.`

Code:

`1`

### Code 0 when:

Sentence structure remains essentially the same and only individual words change.

---

## 6. Nominalization

Column:

`nominalization`

### Code 1 when:

The formal sentence expresses an action, process, property, or relation using a noun or noun phrase where the plain sentence uses a verb, adjective, or simpler predicate.

### Example

Plain:

`Gravity accelerates objects upward.`

Formal:

`Gravity produces upward acceleration.`

Code:

`1`

because `accelerates` becomes the noun `acceleration`.

Another example:

`Light travels faster than sound.`

→

`The propagation speed of light exceeds that of sound.`

Code:

`1`

because motion is reconceptualized through the noun phrase `propagation speed`.

---

## 7. Semantic specificity change

Column:

`semantic_specificity_change`

Use one of:

- `more`
- `same`
- `less`
- `U`

### Code `more` when:

The formal version adds semantic precision or narrows the expression.

Example:

`moons`

→

`natural satellites`

may be coded `more` because the latter provides more explicit scientific categorization.

### Code `same` when:

The wording changes but informational specificity remains effectively equivalent.

### Code `less` when:

The formal version becomes less specific or removes a meaningful distinction.

### Important

Do not judge whether the proposition is true. Code only the difference in semantic specificity between the two formulations.

---

## 8. Other register feature

Column:

`other_register_feature`

Use this field only when an important transformation is not adequately captured by the predefined categories.

Possible descriptions include:

- lexical elevation
- Latinate vocabulary
- impersonal phrasing
- passive construction
- institutional vocabulary
- expanded noun phrase
- reduced personal agency

Do not create a new category after seeing the behavioral effect associated with the item.

Recurring new features may be consolidated only after the full blinded coding stage is complete.

---

## 9. Coding notes

Column:

`coding_notes`

Use this field for short explanations of difficult coding decisions.

Example:

`"natural satellites" coded as both technical lexicon and increased specificity.`

Notes should describe linguistic evidence only.

---

# Blinding rule

During coding:

- do not open the behavioral-effect ranking tables;
- do not consult `false_register_effect`;
- do not sort stimuli according to behavioral results;
- do not classify sentences as "positive-effect", "negative-effect", or "neutral";
- do not alter definitions because of a remembered model response.

Coding is based solely on the plain and formal sentence pair.

---

# Analysis rule

Behavioral scores will be merged with these codes only after the 60 stimulus pairs have been coded.

Any associations discovered between register-realization categories and model deference are exploratory.

They must be tested on newly constructed held-out stimuli before they are treated as evidence for a general behavioral phenomenon or used as the basis for mechanistic interpretation.
