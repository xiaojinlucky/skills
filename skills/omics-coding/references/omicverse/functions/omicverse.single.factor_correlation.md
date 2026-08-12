# omicverse.single.factor_correlation #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.factor_correlation`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.factor_correlation.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Score MOFA-factor enrichment across annotated groups.

## Signature

```text
omicverse.single. factor_correlation ( adata , cluster , factor_list , p_threshold = 500 )
```

## Parameters

- `adata`: ( anndata.AnnData ) – AnnData containing factor* columns in obs .
- `cluster`: ( str ) – Group label column in adata.obs .
- `factor_list`: ( list ) – Factor indices to evaluate.
- `p_threshold`: ( int ) – Upper cap applied to -log(p) values to avoid extreme outliers.

## Full Documentation

# omicverse.single.factor_correlation #

omicverse.single. factor_correlation ( adata , cluster , factor_list , p_threshold = 500 ) [source] #

Score MOFA-factor enrichment across annotated groups.

For each factor and each group in `cluster `, a two-sample t-test compares factor values in-group vs out-group, and stores `-log(p) `.

Parameters :

-
adata ( anndata.AnnData ) – AnnData containing `factor* `columns in `obs `.

-
cluster ( str ) – Group label column in `adata.obs `.

-
factor_list ( list ) – Factor indices to evaluate.

-
p_threshold ( int ) – Upper cap applied to `-log(p) `values to avoid extreme outliers.

Returns :

DataFrame indexed by group labels with factor association scores.

Return type :

pd.DataFrame
