# omicverse.metabol.volcano #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.volcano`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.volcano.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Metabolomics volcano plot — log2FC vs -log10(padj) (or pvalue).

## Signature

```text
omicverse.metabol. volcano ( deg , * , padj_thresh = 0.05 , log2fc_thresh = 1.0 , label_top_n = 10 , use_pvalue = False , clip_log2fc = None , ax = None , figsize = (5.5, 4.5) )
```

## Parameters

- `use_pvalue`: ( bool (default: False )) – Plot against the raw pvalue column instead of the BH-adjusted padj . Useful for small-n untargeted LC-MS where the 5000+ feature FDR burden means no peak survives FDR; raw p-value is the honest axis for the volcano in that regime.
- `clip_log2fc`: ( Optional [ float ] (default: None )) – Clip the x-axis to ±this value. On LC-MS data with below-detection zeros, a handful of features can have log2fc up to ±25 after pseudo-count logging and completely dominate the plot. Set e.g. clip_log2fc=5 to keep the volcano interpretable.
- `deg`: ( DataFrame )
- `padj_thresh`: ( float (default: 0.05 ))
- `log2fc_thresh`: ( float (default: 1.0 ))
- `label_top_n`: ( int (default: 10 ))
- `ax`: ( Optional [ Axes ] (default: None ))
- `figsize`: ( tuple [ float , float ] (default: (5.5, 4.5) ))

## Full Documentation

# omicverse.metabol.volcano #

omicverse.metabol. volcano ( deg , * , padj_thresh = 0.05 , log2fc_thresh = 1.0 , label_top_n = 10 , use_pvalue = False , clip_log2fc = None , ax = None , figsize = (5.5, 4.5) ) [source] #

Metabolomics volcano plot — log2FC vs -log10(padj) (or pvalue).

Parameters :

-
use_pvalue ( `bool `(default: `False `)) – Plot against the raw `pvalue `column instead of the BH-adjusted `padj `. Useful for small-n untargeted LC-MS where the 5000+ feature FDR burden means no peak survives FDR; raw p-value is the honest axis for the volcano in that regime.

-
clip_log2fc ( `Optional `[ `float `] (default: `None `)) – Clip the x-axis to ±this value. On LC-MS data with below-detection zeros, a handful of features can have log2fc up to ±25 after pseudo-count logging and completely dominate the plot. Set e.g. `clip_log2fc=5 `to keep the volcano interpretable.

-
deg ( `DataFrame `)

-
padj_thresh ( `float `(default: `0.05 `))

-
log2fc_thresh ( `float `(default: `1.0 `))

-
label_top_n ( `int `(default: `10 `))

-
ax ( `Optional `[ `Axes `] (default: `None `))

-
figsize ( `tuple `[ `float `, `float `] (default: `(5.5, 4.5) `))
