# omicverse.single.lazy #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.lazy`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.lazy.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run a one-click single-cell analysis pipeline with resumable steps.

## Signature

```text
omicverse.single. lazy ( adata , species = 'human' , reforce_steps = [] , sample_key = None , qc_kwargs = None , preprocess_kwargs = None , pca_kwargs = None , harmony_kwargs = None , scvi_kwargs = None )
```

## Parameters

- `adata`: ( AnnData ) – Input AnnData to be processed.
- `species`: ( str ) – Species name used by downstream annotation helpers.
- `reforce_steps`: ( list ) – Step names forced to rerun even if status flags exist. Common values: ['qc', 'pca', 'preprocess', 'scaled', 'Harmony', 'scVI', 'eval_bench', 'eval_clusters'] .
- `sample_key`: ( str or None ) – Column in adata.obs used as batch key for correction/integration.
- `qc_kwargs`: ( dict or None ) – Keyword arguments passed to ov.pp.qc .
- `preprocess_kwargs`: ( dict or None ) – Keyword arguments passed to ov.pp.preprocess .
- `pca_kwargs`: ( dict or None ) – Keyword arguments passed to PCA routine.
- `harmony_kwargs`: ( dict or None ) – Keyword arguments for Harmony integration block.
- `scvi_kwargs`: ( dict or None ) – Keyword arguments for scVI integration block.

## Full Documentation

# omicverse.single.lazy #

omicverse.single. lazy ( adata , species = 'human' , reforce_steps = [] , sample_key = None , qc_kwargs = None , preprocess_kwargs = None , pca_kwargs = None , harmony_kwargs = None , scvi_kwargs = None ) [source] #

Run a one-click single-cell analysis pipeline with resumable steps.

Parameters :

-
adata ( AnnData ) – Input AnnData to be processed.

-
species ( str ) – Species name used by downstream annotation helpers.

-
reforce_steps ( list ) – Step names forced to rerun even if status flags exist. Common values: `['qc', 'pca', 'preprocess', 'scaled', 'Harmony', 'scVI', 'eval_bench', 'eval_clusters'] `.

-
sample_key ( str or None ) – Column in `adata.obs `used as batch key for correction/integration.

-
qc_kwargs ( dict or None ) – Keyword arguments passed to `ov.pp.qc `.

-
preprocess_kwargs ( dict or None ) – Keyword arguments passed to `ov.pp.preprocess `.

-
pca_kwargs ( dict or None ) – Keyword arguments passed to PCA routine.

-
harmony_kwargs ( dict or None ) – Keyword arguments for Harmony integration block.

-
scvi_kwargs ( dict or None ) – Keyword arguments for scVI integration block.

Returns :

Updated AnnData with QC, preprocessing, embeddings, and clustering results.

Return type :

AnnData
