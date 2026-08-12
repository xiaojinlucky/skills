# omicverse.single.cosg #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.cosg`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.cosg.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Identify cluster-specific marker genes with COSG.

## Signature

```text
omicverse.single. cosg ( adata , groupby = 'CellTypes' , groups = 'all' , mu = 1 , remove_lowly_expressed = False , expressed_pct = 0.1 , n_genes_user = 50 , key_added = None , calculate_logfoldchanges = True , use_raw = True , layer = None , reference = 'rest' , copy = False )
```

## Parameters

- `adata`: ( anndata.AnnData ) – Annotated data matrix for marker detection.
- `groupby`: ( str , default='CellTypes' ) – Obs column containing cluster/group labels.
- `groups`: ( {'all'} or Iterable [ str ] , default='all' ) – Group subset to analyze.
- `mu`: ( float , default=1 ) – Specificity penalty against expression in non-target groups.
- `remove_lowly_expressed`: ( bool , default=False ) – Whether to remove genes with low detection rates in target groups.
- `expressed_pct`: ( float , default=0.1 ) – Minimum fraction of expressing cells when low-expression filtering is enabled.
- `n_genes_user`: ( int , default=50 ) – Number of top marker genes retained per group.
- `key_added`: ( str or None , default=None ) – Key in adata.uns used to store COSG results.
- `calculate_logfoldchanges`: ( bool , default=True ) – Whether to compute log-fold changes.
- `use_raw`: ( bool , default=True ) – Whether to use adata.raw expression values when available.
- `layer`: ( str or None , default=None ) – Layer key used as expression matrix.
- `reference`: ( str , default='rest' ) – Reference strategy for differential comparison.
- `copy`: ( bool , default=False ) – If True , run on a copy and return it.

## Full Documentation

# omicverse.single.cosg #

omicverse.single. cosg ( adata , groupby = 'CellTypes' , groups = 'all' , mu = 1 , remove_lowly_expressed = False , expressed_pct = 0.1 , n_genes_user = 50 , key_added = None , calculate_logfoldchanges = True , use_raw = True , layer = None , reference = 'rest' , copy = False ) [source] #

Identify cluster-specific marker genes with COSG.

Parameters :

-
adata ( anndata.AnnData ) – Annotated data matrix for marker detection.

-
groupby ( str , default='CellTypes' ) – Obs column containing cluster/group labels.

-
groups ( {'all'} or Iterable [ str ] , default='all' ) – Group subset to analyze.

-
mu ( float , default=1 ) – Specificity penalty against expression in non-target groups.

-
remove_lowly_expressed ( bool , default=False ) – Whether to remove genes with low detection rates in target groups.

-
expressed_pct ( float , default=0.1 ) – Minimum fraction of expressing cells when low-expression filtering is enabled.

-
n_genes_user ( int , default=50 ) – Number of top marker genes retained per group.

-
key_added ( str or None , default=None ) – Key in `adata.uns `used to store COSG results.

-
calculate_logfoldchanges ( bool , default=True ) – Whether to compute log-fold changes.

-
use_raw ( bool , default=True ) – Whether to use `adata.raw `expression values when available.

-
layer ( str or None , default=None ) – Layer key used as expression matrix.

-
reference ( str , default='rest' ) – Reference strategy for differential comparison.

-
copy ( bool , default=False ) – If `True `, run on a copy and return it.

Returns :

Returns modified copy when `copy=True `; otherwise updates input object in place.

Return type :

anndata.AnnData or None
