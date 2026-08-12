# omicverse.datasets.pancreas_cellrank #

- Package: omicverse
- Language: Python
- Function: `omicverse.datasets.pancreas_cellrank`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.datasets.pancreas_cellrank.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

The pancreas cellrank dataset used in theislab/scvelo_notebooks .

## Signature

```text
omicverse.datasets. pancreas_cellrank ( url = 'https://github.com/theislab/scvelo_notebooks/raw/master/data/Pancreas/endocrinogenesis_day15.h5ad' , filename = 'pancreas_cellrank.h5ad' )
```

## Parameters

- `url`: ( str (default: 'https://github.com/theislab/scvelo_notebooks/raw/master/data/Pancreas/endocrinogenesis_day15.h5ad' ))
- `filename`: ( str (default: 'pancreas_cellrank.h5ad' ))

## Full Documentation

# omicverse.datasets.pancreas_cellrank #

omicverse.datasets. pancreas_cellrank ( url = 'https://github.com/theislab/scvelo_notebooks/raw/master/data/Pancreas/endocrinogenesis_day15.h5ad' , filename = 'pancreas_cellrank.h5ad' ) [source] #

The pancreas cellrank dataset used in theislab/scvelo_notebooks .

This data consists of 13,913 genes across 2,930 cells.

Note: The previous figshare URL (files/25060877) returned a 2KB HTML error page instead of the dataset, causing an infinite redownload loop. Switched the default to the scvelo_notebooks GitHub raw URL, which is the upstream source that scvelo / cellrank also use.

Parameters :

-
url ( `str `(default: `'https://github.com/theislab/scvelo_notebooks/raw/master/data/Pancreas/endocrinogenesis_day15.h5ad' `))

-
filename ( `str `(default: `'pancreas_cellrank.h5ad' `))
