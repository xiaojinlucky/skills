# omicverse.metabol.dgca #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.dgca`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.dgca.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Differential correlation between two groups.

## Signature

```text
omicverse.metabol. dgca ( adata , * , group_col , group_a = None , group_b = None , features = None , method = 'pearson' , abs_r_threshold = 0.3 , layer = None )
```

## Parameters

- `group_col`: ( str ) – Column in adata.obs with the two-class labels.
- `group_a`: ( Optional [ str ] (default: None )) – Labels to contrast. None → first two unique values. The z-diff direction is z_a - z_b (so positive z_diff means correlation is stronger in group A).
- `group_b`: ( Optional [ str ] (default: None )) – Labels to contrast. None → first two unique values. The z-diff direction is z_a - z_b (so positive z_diff means correlation is stronger in group A).
- `features`: ( Optional [ Sequence [ str ]] (default: None )) – Optional list of metabolite names to restrict the pair enumeration to. None → all. For p features the output has p*(p-1)/2 rows.
- `method`: ( str (default: 'pearson' )) – "pearson" (default) or "spearman" . Spearman is rank-based and more appropriate for non-Gaussian metabolite distributions; Pearson is faster and matches the DGCA default.
- `abs_r_threshold`: ( float (default: 0.3 )) – Threshold for calling a correlation “significant in group X” when assigning the dc_class label. Default 0.3 matches MetaboAnalyst’s network module.
- `layer`: ( Optional [ str ] (default: None )) – AnnData layer (default None → adata.X ).
- `adata`: ( AnnData )

## Full Documentation

# omicverse.metabol.dgca #

omicverse.metabol. dgca ( adata , * , group_col , group_a = None , group_b = None , features = None , method = 'pearson' , abs_r_threshold = 0.3 , layer = None ) [source] #

Differential correlation between two groups.

Parameters :

-
group_col ( `str `) – Column in `adata.obs `with the two-class labels.

-
group_a ( `Optional `[ `str `] (default: `None `)) – Labels to contrast. `None `→ first two unique values. The z-diff direction is `z_a - z_b `(so positive `z_diff `means correlation is stronger in group A).

-
group_b ( `Optional `[ `str `] (default: `None `)) – Labels to contrast. `None `→ first two unique values. The z-diff direction is `z_a - z_b `(so positive `z_diff `means correlation is stronger in group A).

-
features ( `Optional `[ `Sequence `[ `str `]] (default: `None `)) – Optional list of metabolite names to restrict the pair enumeration to. `None `→ all. For `p `features the output has `p*(p-1)/2 `rows.

-
method ( `str `(default: `'pearson' `)) – `"pearson" `(default) or `"spearman" `. Spearman is rank-based and more appropriate for non-Gaussian metabolite distributions; Pearson is faster and matches the DGCA default.

-
abs_r_threshold ( `float `(default: `0.3 `)) – Threshold for calling a correlation “significant in group X” when assigning the `dc_class `label. Default 0.3 matches MetaboAnalyst’s network module.

-
layer ( `Optional `[ `str `] (default: `None `)) – AnnData layer (default `None `→ `adata.X `).

-
adata ( `AnnData `)

Returns :

Long format, one row per feature pair, columns:

-
`feature_a `, `feature_b `— metabolite names

-
`r_a `, `r_b `— correlation in each group

-
`z_diff `— Fisher-z-transformed difference test statistic

-
`pvalue `, `padj `— two-sided p and BH-FDR

-
`dc_class `— `"+/+" `, `"+/0" `, `"+/-" `, `"0/+" `, `"0/-" `, `"-/+" `, `"-/-" `, or `"0/0" `. The first symbol is group A, the second group B. `+ `/ `- `means `|r| ≥ abs_r_threshold `with that sign; `0 `means below threshold.

The result is sorted by `padj `ascending.

Return type :

pd.DataFrame
