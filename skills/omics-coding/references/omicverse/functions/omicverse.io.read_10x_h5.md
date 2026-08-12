# omicverse.io.read_10x_h5 #

- Package: omicverse
- Language: Python
- Function: `omicverse.io.read_10x_h5`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.io.read_10x_h5.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Read a 10x Genomics HDF5 matrix file.

## Signature

```text
omicverse.io. read_10x_h5 ( filename , * , genome = None , gex_only = True , backup_url = None )
```

## Parameters

- `filename`: ( str or pathlib.Path ) – Path to the 10x .h5 matrix file.
- `genome`: ( str or None , default=None ) – Genome identifier to keep for legacy multi-genome files. Ignored for single-genome inputs.
- `gex_only`: ( bool , default=True ) – If True , keep only features with feature_types == 'Gene Expression' .
- `backup_url`: ( str or None , default=None ) – Reserved parameter for API compatibility. Remote fallback is not implemented.

## Full Documentation

# omicverse.io.read_10x_h5 #

omicverse.io. read_10x_h5 ( filename , * , genome = None , gex_only = True , backup_url = None ) [source] #

Read a 10x Genomics HDF5 matrix file.

Parameters :

-
filename ( str or pathlib.Path ) – Path to the 10x `.h5 `matrix file.

-
genome ( str or None , default=None ) – Genome identifier to keep for legacy multi-genome files. Ignored for single-genome inputs.

-
gex_only ( bool , default=True ) – If `True `, keep only features with `feature_types == 'Gene Expression' `.

-
backup_url ( str or None , default=None ) – Reserved parameter for API compatibility. Remote fallback is not implemented.

Returns :

AnnData object with barcodes in `obs_names `and features in `var_names `.

Return type :

anndata.AnnData
