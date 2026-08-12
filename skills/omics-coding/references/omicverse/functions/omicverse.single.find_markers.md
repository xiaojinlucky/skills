# omicverse.single.find_markers #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.find_markers`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.find_markers.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Find marker genes for each cluster / group in single-cell data.

## Signature

```text
omicverse.single. find_markers ( adata , groupby , method = 'cosg' , n_genes = 50 , key_added = None , use_raw = None , layer = None , groups = 'all' , reference = 'rest' , corr_method = 'benjamini-hochberg' , rankby_abs = False , tie_correct = False , pts = True , ** kwargs )
```

## Parameters

- `adata`: (Annotated data matrix. Data must be log-normalised for) – statistical tests; raw counts are expected for method='cosg' .
- `groupby`: (Key in adata.obs to group cells by (e.g. 'leiden' ).)
- `method`: ( Algorithm. One of: ) – 'cosg' — cosine-similarity-based, fast, recommended for large datasets.
- `n_genes`: (Top marker genes per group to keep. Default: 50 .)
- `key_added`: (Key in adata.uns to write results to.) – Default: 'rank_genes_groups' .
- `use_raw`: (Use adata.raw for expression values. None (default)) – means use raw if it exists (matching scanpy behaviour).
- `layer`: (Layer to use instead of adata.X . Default: None .)
- `groups`: (Groups to compute markers for — 'all' or a list of names.) – Default: 'all' .
- `reference`: (Reference group. 'rest' (default) compares each group) – against the union of all other cells; a group name restricts the comparison to that group only.
- `corr_method`: (Multiple-testing correction. 'benjamini-hochberg' ) – (default) or 'bonferroni' . Ignored for 'cosg' and 'logreg' .
- `rankby_abs`: ( Rank genes by absolute score instead of raw score. ) – Default: False .
- `tie_correct`: (Apply tie correction for 'wilcoxon' . Default: False .)
- `pts`: ( Compute fraction of cells expressing each gene ( stored as ) – adata.uns[key_added]['pts'] ). Default: False .
- `**kwargs`: (Forwarded to the underlying method (e.g. mu for cosg,) – or sklearn parameters for logreg).

## Full Documentation

# omicverse.single.find_markers #

omicverse.single. find_markers ( adata , groupby , method = 'cosg' , n_genes = 50 , key_added = None , use_raw = None , layer = None , groups = 'all' , reference = 'rest' , corr_method = 'benjamini-hochberg' , rankby_abs = False , tie_correct = False , pts = True , ** kwargs ) [source] #

Find marker genes for each cluster / group in single-cell data.

A unified wrapper supporting multiple algorithms. For statistical methods ( `t-test `, `wilcoxon `, `logreg `) the implementation is ported directly from scanpy — no scanpy runtime dependency . Results are stored in `adata.uns[key_added] `using the same structured-array format as `sc.tl.rank_genes_groups `, so all downstream tools (including `omicverse.single.get_markers() `and `omicverse.pl.markers_dotplot() `) work out of the box.

Parameters :

-
adata (Annotated data matrix. Data must be log-normalised for) – statistical tests; raw counts are expected for `method='cosg' `.

-
groupby (Key in `adata.obs `to group cells by (e.g. `'leiden' `).)

-
method ( Algorithm. One of: ) –
-
`'cosg' `— cosine-similarity-based, fast, recommended for large datasets.

-
`'t-test' `— Welch’s t-test.

-
`'t-test_overestim_var' `— t-test with per-group variance overestimation (conservative).

-
`'wilcoxon' `— Wilcoxon rank-sum / Mann-Whitney U test.

-
`'logreg' `— logistic regression (requires scikit-learn).

Default: `'cosg' `.

-
n_genes (Top marker genes per group to keep. Default: `50 `.)

-
key_added (Key in `adata.uns `to write results to.) – Default: `'rank_genes_groups' `.

-
use_raw (Use `adata.raw `for expression values. `None `(default)) – means use raw if it exists (matching scanpy behaviour).

-
layer (Layer to use instead of `adata.X `. Default: `None `.)

-
groups (Groups to compute markers for — `'all' `or a list of names.) – Default: `'all' `.

-
reference (Reference group. `'rest' `(default) compares each group) – against the union of all other cells; a group name restricts the comparison to that group only.

-
corr_method (Multiple-testing correction. `'benjamini-hochberg' `) – (default) or `'bonferroni' `. Ignored for `'cosg' `and `'logreg' `.

-
rankby_abs ( Rank genes by absolute score instead of raw score. ) – Default: `False `.

-
tie_correct (Apply tie correction for `'wilcoxon' `. Default: `False `.)

-
pts ( Compute fraction of cells expressing each gene ( stored as ) – `adata.uns[key_added]['pts'] `). Default: `False `.

-
**kwargs (Forwarded to the underlying method (e.g. `mu `for cosg,) – or sklearn parameters for logreg).

Returns :

-
`None `. Results are written to `adata.uns[key_added] `.

-
Examples – >>> import omicverse as ov >>> ov.single.find_markers(adata, groupby=’leiden’, method=’cosg’) >>> df = ov.single.get_markers(adata, n_genes=5) >>> ov.pl.markers_dotplot(adata, groupby=’leiden’, n_genes=5)
