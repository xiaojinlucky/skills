# omicverse.metabol.pathway_dot #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.pathway_dot`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.pathway_dot.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Dot plot of pathway enrichment — the de-facto standard figure.

## Signature

```text
omicverse.metabol. pathway_dot ( enrichment , * , term_col = None , size_col = 'overlap' , x_col = 'odds_ratio' , color_col = 'pvalue' , top_n = 15 , ax = None , figsize = (6.5, 5.5) )
```

## Parameters

- `size_col`: ( str (default: 'overlap' )) – Column mapped to dot size. Default "overlap" (ORA output); use "matched_size" for GSEA output.
- `x_col`: ( str (default: 'odds_ratio' )) – Column mapped to x position. Default "odds_ratio" (ORA); use "nes" for GSEA.
- `color_col`: ( str (default: 'pvalue' )) – Column mapped to color (via -log10 ). Default "pvalue" .
- `enrichment`: ( DataFrame )
- `term_col`: ( Optional [ str ] (default: None ))
- `top_n`: ( int (default: 15 ))
- `ax`: ( Optional [ Axes ] (default: None ))
- `figsize`: ( tuple [ float , float ] (default: (6.5, 5.5) ))

## Full Documentation

# omicverse.metabol.pathway_dot #

omicverse.metabol. pathway_dot ( enrichment , * , term_col = None , size_col = 'overlap' , x_col = 'odds_ratio' , color_col = 'pvalue' , top_n = 15 , ax = None , figsize = (6.5, 5.5) ) [source] #

Dot plot of pathway enrichment — the de-facto standard figure.

Matches the layout of scanpy ’s / clusterProfiler ’s dot plot: each row is a pathway, dot size encodes overlap count, x position encodes fold-enrichment (odds ratio or NES), color encodes -log10(p-value).

Parameters :

-
size_col ( `str `(default: `'overlap' `)) – Column mapped to dot size. Default `"overlap" `(ORA output); use `"matched_size" `for GSEA output.

-
x_col ( `str `(default: `'odds_ratio' `)) – Column mapped to x position. Default `"odds_ratio" `(ORA); use `"nes" `for GSEA.

-
color_col ( `str `(default: `'pvalue' `)) – Column mapped to color (via `-log10 `). Default `"pvalue" `.

-
enrichment ( `DataFrame `)

-
term_col ( `Optional `[ `str `] (default: `None `))

-
top_n ( `int `(default: `15 `))

-
ax ( `Optional `[ `Axes `] (default: `None `))

-
figsize ( `tuple `[ `float `, `float `] (default: `(6.5, 5.5) `))
