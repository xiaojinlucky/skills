# omicverse.metabol.mixed_model #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.mixed_model`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.mixed_model.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Per-feature statsmodels.MixedLM fit.

## Signature

```text
omicverse.metabol. mixed_model ( adata , * , formula , groups , re_formula = '1' , term = None , layer = None )
```

## Parameters

- `formula`: ( str ) – Patsy-style formula without the y ~ prefix. Categorical effects, interactions ( a * b ), and numerics all work.
- `groups`: ( str ) – Name of the adata.obs column carrying the random-effect grouping labels. Usually patient / subject ID.
- `re_formula`: ( Optional [ str ] (default: '1' )) – Random-effect formula. "1" (default) = random intercept. Use "1 + time" for random slopes.
- `term`: ( Optional [ str ] (default: None )) – If given, return a short-format table with one row per feature for this specific fixed-effect term (matches the metabol.differential() schema: stat / pvalue / padj ). If None , return a long-format table with one row per (feature, term) pair, excluding the intercept and variance components.
- `layer`: ( Optional [ str ] (default: None )) – AnnData layer name (default None → adata.X ).
- `adata`: ( AnnData )

## Full Documentation

# omicverse.metabol.mixed_model #

omicverse.metabol. mixed_model ( adata , * , formula , groups , re_formula = '1' , term = None , layer = None ) [source] #

Per-feature `statsmodels.MixedLM `fit.

Fits `y ~ <formula> `for each metabolite with `groups=<groups> `defining the random-effect grouping variable (e.g. patient ID).

Parameters :

-
formula ( `str `) – Patsy-style formula without the `y ~ `prefix. Categorical effects, interactions ( `a * b `), and numerics all work.

-
groups ( `str `) – Name of the `adata.obs `column carrying the random-effect grouping labels. Usually patient / subject ID.

-
re_formula ( `Optional `[ `str `] (default: `'1' `)) – Random-effect formula. `"1" `(default) = random intercept. Use `"1 + time" `for random slopes.

-
term ( `Optional `[ `str `] (default: `None `)) – If given, return a short-format table with one row per feature for this specific fixed-effect term (matches the `metabol.differential() `schema: `stat / pvalue / padj `). If `None `, return a long-format table with one row per `(feature, term) `pair, excluding the intercept and variance components.

-
layer ( `Optional `[ `str `] (default: `None `)) – AnnData layer name (default `None `→ `adata.X `).

-
adata ( `AnnData `)

Returns :

Long format (default): columns `feature, term, coef, se, stat, pvalue, padj `. Short format ( `term=... `): indexed by feature with `coef, se, stat, pvalue, padj `.

Return type :

pd.DataFrame
