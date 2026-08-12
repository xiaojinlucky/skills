# omicverse.metabol.s_plot #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.s_plot`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.s_plot.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

OPLS-DA S-plot: p(cov) vs p(corr), i.e. covariance vs correlation between each feature and the predictive component.

## Signature

```text
omicverse.metabol. s_plot ( result , adata , * , label_top_n = 15 , ax = None , figsize = (5.5, 4.5) )
```

## Parameters

- `result`: ( PLSDAResult )
- `label_top_n`: ( int (default: 15 ))
- `ax`: ( Optional [ Axes ] (default: None ))
- `figsize`: ( tuple [ float , float ] (default: (5.5, 4.5) ))
- `adata`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.metabol.s_plot #

omicverse.metabol. s_plot ( result , adata , * , label_top_n = 15 , ax = None , figsize = (5.5, 4.5) ) [source] #

OPLS-DA S-plot: p(cov) vs p(corr), i.e. covariance vs correlation between each feature and the predictive component.

This is the classic visualization for interpreting OPLS-DA loadings (Wiklund et al 2008). Features in the two “arms” of the S (high-covariance, high-correlation) are the strongest drivers of the case/control separation.

Parameters :

-
result ( `PLSDAResult `)

-
label_top_n ( `int `(default: `15 `))

-
ax ( `Optional `[ `Axes `] (default: `None `))

-
figsize ( `tuple `[ `float `, `float `] (default: `(5.5, 4.5) `))
