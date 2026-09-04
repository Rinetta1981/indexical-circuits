# Reproducibility

## Scope

Indexical Circuits preserves the complete research sequence from the
initial exploratory pilot through the final preregistered focused
replication.

The repository distinguishes between:

1. lightweight repository-integrity checks that can run automatically
   in GitHub Actions; and
2. GPU/model experiments preserved in the research notebooks.

The CI workflow does not attempt to redownload or reevaluate
Gemma-2-2B-IT on every repository change.

## Primary model

The behavioral experiments use:

google/gemma-2-2b-it

Access to the model may require authentication through Hugging Face and
acceptance of the model's applicable access conditions.

## Original computational environment

The original experimental notebooks were run in Google Colab with GPU
acceleration.

The environment sanity-check notebook records use of a Tesla T4 GPU.

Core libraries used in the notebook environment include:

- PyTorch
- transformers
- accelerate
- huggingface_hub
- pandas

The environment notebook explicitly installed:

- transformers
- accelerate
- huggingface_hub
- pandas==2.2.3

PyTorch was available in the Colab runtime.

Because hosted notebook environments and model-serving libraries change
over time, the repository preserves the executed notebooks and outputs
as part of the computational record rather than claiming that future
library versions will reproduce floating-point values bit-for-bit.

## Authentication

Model loading requires appropriate Hugging Face access.

The notebooks use Hugging Face authentication before loading
google/gemma-2-2b-it.

Authentication credentials are not stored in this repository.

## Research workflow

The numbered notebooks in `notebooks/` preserve the chronological
experimental workflow.

They should be read in order.

The project intentionally preserves exploratory and confirmatory stages
rather than rewriting the notebook history after the final result.

## Lightweight automated checks

The repository includes a GitHub Actions workflow that runs:

pytest -q

The test environment is intentionally minimal and is specified in:

requirements-test.txt

These checks validate repository-level invariants without requiring a
GPU or model download.

## Data and result provenance

The repository retains:

- exploratory stimulus material;
- confirmatory stimulus banks;
- held-out replication material;
- prior-data overlap audits;
- source-verification logs;
- preregistration documents;
- frozen focused-replication data;
- behavioral outputs;
- analysis results;
- portfolio figures.

The final focused `functions as` stimulus bank was constructed from 30
new factual families and checked against prior experimental material
before model testing.

Its frozen dataset fingerprint is:

64b3fd0cc9d0cba4f650789fc0a6e7b35787352fa17b15a5592cf885db48a14e

## Interpretation boundary

Reproducing an already completed analysis does not turn an exposed result
into a new confirmatory test.

The final primary `functions as` hypothesis did not replicate, and the
pre-specified mechanistic gate remained closed.

Any future test of the secondary truth-dependent interaction should use
new held-out material and should be treated as a separate study.

## Recommended reproduction path

For repository-integrity checks:

1. Clone the repository.
2. Create a Python environment.
3. Install:

   python -m pip install -r requirements-test.txt

4. Run:

   pytest -q

For the original model experiments:

1. Use a GPU-capable Python environment.
2. Obtain access to google/gemma-2-2b-it through Hugging Face.
3. Authenticate without storing credentials in the repository.
4. Follow the numbered notebooks in `notebooks/`.
5. Compare regenerated outputs with the preserved files in `results/`.

The repository's primary purpose is to preserve the experimental design,
evidence sequence, and decision logic transparently.
