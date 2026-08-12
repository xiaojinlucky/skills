# omicverse.micro.filter_by_prevalence #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.filter_by_prevalence`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.filter_by_prevalence.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Filter rare features by prevalence.

## Signature

```text
omicverse.micro. filter_by_prevalence ( adata , min_prevalence = 0.1 , min_count = 1 , copy = False )
```

## Parameters

- `min_prevalence`: ( float (default: 0.1 )) – Minimum fraction of samples in which a feature must have >= min_count reads. 0.1 = 10 % of samples.
- `min_count`: ( int (default: 1 )) – Per-sample count threshold used to define “present”.
- `adata`: ( AnnData )
- `copy`: ( bool (default: False ))

## Full Documentation

# omicverse.micro.filter_by_prevalence #

omicverse.micro. filter_by_prevalence ( adata , min_prevalence = 0.1 , min_count = 1 , copy = False ) [source] #

Filter rare features by prevalence.

Parameters :

-
min_prevalence ( `float `(default: `0.1 `)) – Minimum fraction of samples in which a feature must have `>= min_count `reads. 0.1 = 10 % of samples.

-
min_count ( `int `(default: `1 `)) – Per-sample count threshold used to define “present”.

-
adata ( `AnnData `)

-
copy ( `bool `(default: `False `))
