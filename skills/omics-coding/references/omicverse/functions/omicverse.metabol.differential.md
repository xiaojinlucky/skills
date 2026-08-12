# omicverse.metabol.differential #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.differential`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.differential.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run a univariate two-group test across all metabolites.

## Signature

```text
omicverse.metabol. differential ( adata , * , group_col = 'group' , group_a = None , group_b = None , method = 'welch_t' , layer = None , log_transformed = True )
```

## Parameters

- `group_col`: ( str (default: 'group' )) – Name of the factor column in adata.obs .
- `group_a`: ( Optional [ str ] (default: None )) – Which two values of group_col to contrast. When None , the first two unique values are used. log2fc is reported as group_a / group_b .
- `group_b`: ( Optional [ str ] (default: None )) – Which two values of group_col to contrast. When None , the first two unique values are used. log2fc is reported as group_a / group_b .
- `method`: ( Literal [ 't' , 'welch_t' , 'wilcoxon' , 'limma' ] (default: 'welch_t' )) – "welch_t" (default) — Welch’s t-test; handles unequal variances. The MetaboAnalyst default.
- `layer`: ( Optional [ str ] (default: None )) – AnnData layer holding the values to test. Default None = use adata.X (which the pyMetabo pipeline leaves normalized and transformed).
- `log_transformed`: ( bool (default: True )) – If True (default), data are assumed already log-transformed and log2fc = mean_a - mean_b (difference of logs). If False, the fold-change is computed as log2(mean_a/mean_b) on the raw scale.
- `adata`: ( AnnData )

## Full Documentation

# omicverse.metabol.differential #

omicverse.metabol. differential ( adata , * , group_col = 'group' , group_a = None , group_b = None , method = 'welch_t' , layer = None , log_transformed = True ) [source] #

Run a univariate two-group test across all metabolites.

Parameters :

-
group_col ( `str `(default: `'group' `)) – Name of the factor column in `adata.obs `.

-
group_a ( `Optional `[ `str `] (default: `None `)) – Which two values of `group_col `to contrast. When `None `, the first two unique values are used. `log2fc `is reported as `group_a / group_b `.

-
group_b ( `Optional `[ `str `] (default: `None `)) – Which two values of `group_col `to contrast. When `None `, the first two unique values are used. `log2fc `is reported as `group_a / group_b `.

-
method ( `Literal `[ `'t' `, `'welch_t' `, `'wilcoxon' `, `'limma' `] (default: `'welch_t' `)) –
-
`"welch_t" `(default) — Welch’s t-test; handles unequal variances. The MetaboAnalyst default.

-
`"t" `— Student’s t (equal-variance).

-
`"wilcoxon" `— Mann-Whitney U; non-parametric.

-
`"limma" `— empirical-Bayes moderated t (Smyth 2004). Implemented here directly on the variance pool — matches limma’s output at `atol~1e-6 `on real data.

-
layer ( `Optional `[ `str `] (default: `None `)) – AnnData layer holding the values to test. Default `None `= use `adata.X `(which the pyMetabo pipeline leaves normalized and transformed).

-
log_transformed ( `bool `(default: `True `)) – If True (default), data are assumed already log-transformed and `log2fc = mean_a - mean_b `(difference of logs). If False, the fold-change is computed as `log2(mean_a/mean_b) `on the raw scale.

-
adata ( `AnnData `)

Returns :

Indexed by metabolite ( `adata.var_names `) with columns `stat `, `pvalue `, `padj `, `log2fc `, `mean_a `, `mean_b `.

Return type :

pd.DataFrame
