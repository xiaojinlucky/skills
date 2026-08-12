# omicverse.single.get_markers #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.get_markers`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.get_markers.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Extract top marker genes from rank_genes_groups results.

## Signature

```text
omicverse.single. get_markers ( adata , n_genes = 10 , key = 'rank_genes_groups' , groups = None , return_type = 'dataframe' , min_logfoldchange = None , min_score = None , min_pval_adj = None )
```

## Parameters

- `adata`: ( Annotated data matrix. )
- `n_genes`: ( Maximum number of top marker genes to return per group. ) – Default: 10 .
- `key`: (Key in adata.uns holding the results.) – Default: 'rank_genes_groups' .
- `groups`: ( One or more group names to extract. Accepts: ) – None — all groups (default).
- `return_type`: ( Output format: ) – 'dataframe' — pandas.DataFrame with columns [group, rank, names, scores, logfoldchanges, pvals, pvals_adj] (columns present depend on which stats were computed).
- `min_logfoldchange`: ( Keep only genes with ) – |logfoldchange| ≥ min_logfoldchange . Default: None .
- `min_score`: (Keep only genes with score ≥ min_score . Default: None .)
- `min_pval_adj`: (Keep only genes with pvals_adj ≤ min_pval_adj .) – Default: None .

## Full Documentation

# omicverse.single.get_markers #

omicverse.single. get_markers ( adata , n_genes = 10 , key = 'rank_genes_groups' , groups = None , return_type = 'dataframe' , min_logfoldchange = None , min_score = None , min_pval_adj = None ) [source] #

Extract top marker genes from `rank_genes_groups `results.

Works with results produced by `find_markers() `, `omicverse.single.cosg() `, or `sc.tl.rank_genes_groups `.

Parameters :

-
adata ( Annotated data matrix. )

-
n_genes ( Maximum number of top marker genes to return per group. ) – Default: `10 `.

-
key (Key in `adata.uns `holding the results.) – Default: `'rank_genes_groups' `.

-
groups ( One or more group names to extract. Accepts: ) –
-
`None `— all groups (default).

-
`'0' `— single group as a string.

-
`['0', '1', '3'] `— explicit list of groups.

-
return_type ( Output format: ) –
-
`'dataframe' `— `pandas.DataFrame `with columns `[group, rank, names, scores, logfoldchanges, pvals, pvals_adj] `(columns present depend on which stats were computed).

-
`'dict' `— `{group: [gene1, gene2, ...]} `mapping.

Default: `'dataframe' `.

-
min_logfoldchange ( Keep only genes with ) – `|logfoldchange| ≥ min_logfoldchange `. Default: `None `.

-
min_score (Keep only genes with `score ≥ min_score `. Default: `None `.)

-
min_pval_adj (Keep only genes with `pvals_adj ≤ min_pval_adj `.) – Default: `None `.

Returns :

-
`pandas.DataFrame `or `dict `depending on `return_type `.

-
Examples – >>> import omicverse as ov >>> ov.single.find_markers(adata, groupby=’leiden’) >>> # All clusters >>> df = ov.single.get_markers(adata, n_genes=10) >>> # Single cluster >>> df0 = ov.single.get_markers(adata, n_genes=5, groups=’0’) >>> # As dict for annotation workflows >>> d = ov.single.get_markers(adata, n_genes=5, return_type=’dict’)
