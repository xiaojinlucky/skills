# omicverse.micro.DA #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.DA`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.DA.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Per-feature differential abundance across sample groups.

## Signature

```text
class omicverse.micro. DA ( adata )
```

## Parameters

- `adata`: ( AnnData ) – Samples × features AnnData with int counts in X .

## Full Documentation

# omicverse.micro.DA #

class omicverse.micro. DA ( adata ) [source] #

Per-feature differential abundance across sample groups.

Parameters :

adata ( `AnnData `) – Samples × features AnnData with int counts in `X `.

__init__ ( adata ) [source] #

Parameters :

adata ( `AnnData `)

Methods

`__init__ `(adata)

`ancombc `(group_key[, rank, min_prevalence, ...])

ANCOM-BC via `skbio.stats.composition.ancombc `(skbio ≥ 0.7.1).

`deseq2 `(group_key[, group_a, group_b, rank, ...])

Differential abundance via pyDESeq2 (negative-binomial GLM).

`wilcoxon `(group_key[, group_a, group_b, ...])

Two-group Mann-Whitney U test per feature.
