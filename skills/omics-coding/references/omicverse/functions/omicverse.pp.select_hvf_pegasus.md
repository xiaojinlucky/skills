# omicverse.pp.select_hvf_pegasus #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.select_hvf_pegasus`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.select_hvf_pegasus.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Select highly variable features with the Pegasus strategy.

## Signature

```text
omicverse.pp. select_hvf_pegasus ( data , batch , n_top = 2000 , span = 0.02 )
```

## Parameters

- `data`: ( anndata.AnnData ) – AnnData object with robust-gene annotations in data.var['robust'] .
- `batch`: ( str ) – Batch column in data.obs used for cross-batch statistics. Set to None to ignore batch effects.
- `n_top`: ( int , default=2000 ) – Number of top-ranked highly variable features to retain.
- `span`: ( float , default=0.02 ) – Loess smoothing span for fitting the mean-variance trend.

## Full Documentation

# omicverse.pp.select_hvf_pegasus #

omicverse.pp. select_hvf_pegasus ( data , batch , n_top = 2000 , span = 0.02 ) [source] #

Select highly variable features with the Pegasus strategy.

Parameters :

-
data ( anndata.AnnData ) – AnnData object with robust-gene annotations in `data.var['robust'] `.

-
batch ( str ) – Batch column in `data.obs `used for cross-batch statistics. Set to `None `to ignore batch effects.

-
n_top ( int , default=2000 ) – Number of top-ranked highly variable features to retain.

-
span ( float , default=0.02 ) – Loess smoothing span for fitting the mean-variance trend.

Returns :

Writes `hvf_loess `, `hvf_rank `and `highly_variable_features `to `data.var `.

Return type :

None
