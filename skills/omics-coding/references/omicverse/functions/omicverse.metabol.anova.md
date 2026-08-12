# omicverse.metabol.anova #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.anova`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.anova.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Per-metabolite test across 3+ groups.

## Signature

```text
omicverse.metabol. anova ( adata , * , group_col = 'group' , groups = None , method = 'welch_anova' , layer = None )
```

## Parameters

- `group_col`: ( str (default: 'group' )) – Factor column in adata.obs .
- `groups`: ( Optional [ list ] (default: None )) – Subset of levels to test. None → use every unique level in group_col with at least 2 samples.
- `method`: ( Literal [ 'welch_anova' , 'anova' , 'kruskal' ] (default: 'welch_anova' )) – "welch_anova" (default) — Alexander-Govern test ( scipy.stats.alexandergovern ), Welch’s generalisation for unequal variances. Robust and recommended.
- `layer`: ( Optional [ str ] (default: None )) – AnnData layer (default None → adata.X ).
- `adata`: ( AnnData )

## Full Documentation

# omicverse.metabol.anova #

omicverse.metabol. anova ( adata , * , group_col = 'group' , groups = None , method = 'welch_anova' , layer = None ) [source] #

Per-metabolite test across 3+ groups.

Parameters :

-
group_col ( `str `(default: `'group' `)) – Factor column in `adata.obs `.

-
groups ( `Optional `[ `list `] (default: `None `)) – Subset of levels to test. `None `→ use every unique level in `group_col `with at least 2 samples.

-
method ( `Literal `[ `'welch_anova' `, `'anova' `, `'kruskal' `] (default: `'welch_anova' `)) –
-
`"welch_anova" `(default) — Alexander-Govern test ( `scipy.stats.alexandergovern `), Welch’s generalisation for unequal variances. Robust and recommended.

-
`"anova" `— classic one-way `f_oneway `. Assumes equal variances across groups; most sensitive when that holds.

-
`"kruskal" `— non-parametric `kruskal `. Use when the Gaussian / symmetry assumption fails even after log.

-
layer ( `Optional `[ `str `] (default: `None `)) – AnnData layer (default `None `→ `adata.X `).

-
adata ( `AnnData `)

Returns :

Indexed by metabolite with columns:

-
`stat `— test statistic (F, Kruskal H, or Alexander-Govern A)

-
`pvalue `, `padj `— raw and BH-FDR

-
`mean_<level> `— one column per tested group level

-
`n_groups `— number of levels actually tested

Return type :

pd.DataFrame
