# omicverse.metabol.corr_network #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.corr_network`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.corr_network.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Pairwise metabolite correlation network within a single condition.

## Signature

```text
omicverse.metabol. corr_network ( adata , * , group_col = None , group = None , features = None , method = 'spearman' , abs_r_threshold = 0.5 , padj_threshold = 0.05 , layer = None )
```

## Parameters

- `group_col`: ( Optional [ str ] (default: None )) – If both given, restrict to samples where adata.obs[group_col] == group . If group_col is given but group is None a ValueError is raised — partial filtering makes no sense. If both are None, all samples are used.
- `group`: ( Optional [ str ] (default: None )) – If both given, restrict to samples where adata.obs[group_col] == group . If group_col is given but group is None a ValueError is raised — partial filtering makes no sense. If both are None, all samples are used.
- `features`: ( Optional [ Sequence [ str ]] (default: None )) – Optional subset of metabolite names (reduces O(p^2)).
- `method`: ( str (default: 'spearman' )) – "spearman" (default, heavy-tailed-friendly) or "pearson" .
- `abs_r_threshold`: ( float (default: 0.5 )) – Keep pairs with |r| >= abs_r_threshold in the output edge list.
- `padj_threshold`: ( float (default: 0.05 )) – Keep pairs with BH-FDR padj < padj_threshold .
- `layer`: ( Optional [ str ] (default: None )) – AnnData layer (default None → adata.X ).
- `adata`: ( AnnData )

## Full Documentation

# omicverse.metabol.corr_network #

omicverse.metabol. corr_network ( adata , * , group_col = None , group = None , features = None , method = 'spearman' , abs_r_threshold = 0.5 , padj_threshold = 0.05 , layer = None ) [source] #

Pairwise metabolite correlation network within a single condition.

Parameters :

-
group_col ( `Optional `[ `str `] (default: `None `)) – If both given, restrict to samples where `adata.obs[group_col] == group `. If `group_col `is given but `group `is None a `ValueError `is raised — partial filtering makes no sense. If both are None, all samples are used.

-
group ( `Optional `[ `str `] (default: `None `)) – If both given, restrict to samples where `adata.obs[group_col] == group `. If `group_col `is given but `group `is None a `ValueError `is raised — partial filtering makes no sense. If both are None, all samples are used.

-
features ( `Optional `[ `Sequence `[ `str `]] (default: `None `)) – Optional subset of metabolite names (reduces O(p^2)).

-
method ( `str `(default: `'spearman' `)) – `"spearman" `(default, heavy-tailed-friendly) or `"pearson" `.

-
abs_r_threshold ( `float `(default: `0.5 `)) – Keep pairs with `|r| >= abs_r_threshold `in the output edge list.

-
padj_threshold ( `float `(default: `0.05 `)) – Keep pairs with BH-FDR `padj < padj_threshold `.

-
layer ( `Optional `[ `str `] (default: `None `)) – AnnData layer (default `None `→ `adata.X `).

-
adata ( `AnnData `)

Returns :

Filtered edge list, columns `feature_a, feature_b, r, pvalue, padj `. Sorted by `|r| `descending. Intended as input to `networkx.Graph `( `nx.from_pandas_edgelist(df, source='feature_a', target='feature_b', edge_attr='r') `).

Return type :

pd.DataFrame
