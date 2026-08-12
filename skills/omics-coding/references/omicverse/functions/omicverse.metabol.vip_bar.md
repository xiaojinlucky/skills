# omicverse.metabol.vip_bar #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.vip_bar`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.vip_bar.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Horizontal bar chart of top- top_n VIP metabolites.

## Signature

```text
omicverse.metabol. vip_bar ( result , var_names , * , top_n = 15 , ax = None , figsize = (5.0, 5.0) )
```

## Parameters

- `result`: ( PLSDAResult ) – Output of omicverse.metabol.plsda() or opls_da() .
- `var_names`: – Iterable of metabolite names — typically adata.var_names — used to label the bars.
- `top_n`: ( int , default 15 ) – Number of top-VIP metabolites to plot.
- `ax`: ( Optional [ Axes ] (default: None )) – Standard matplotlib hooks.
- `figsize`: ( tuple [ float , float ] (default: (5.0, 5.0) )) – Standard matplotlib hooks.

## Full Documentation

# omicverse.metabol.vip_bar #

omicverse.metabol. vip_bar ( result , var_names , * , top_n = 15 , ax = None , figsize = (5.0, 5.0) ) [source] #

Horizontal bar chart of top- `top_n `VIP metabolites.

Bars sorted by VIP score (descending). Colour encodes the sign of the PLS-DA regression coefficient — red for upregulated in the positive class, blue for downregulated — so the figure simultaneously shows importance and direction. The dashed grey line at VIP=1 is Wold’s classical importance cutoff (features above 1 are retained).

Parameters :

-
result ( PLSDAResult ) – Output of `omicverse.metabol.plsda() `or `opls_da() `.

-
var_names – Iterable of metabolite names — typically `adata.var_names `— used to label the bars.

-
top_n ( int , default 15 ) – Number of top-VIP metabolites to plot.

-
ax ( `Optional `[ `Axes `] (default: `None `)) – Standard matplotlib hooks.

-
figsize ( `tuple `[ `float `, `float `] (default: `(5.0, 5.0) `)) – Standard matplotlib hooks.

Return type :

(fig, ax) tuple.
