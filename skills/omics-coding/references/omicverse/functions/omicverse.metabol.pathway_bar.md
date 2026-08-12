# omicverse.metabol.pathway_bar #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.pathway_bar`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.pathway_bar.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Horizontal bar chart of pathway enrichment p-values.

## Signature

```text
omicverse.metabol. pathway_bar ( enrichment , * , term_col = None , score_col = 'pvalue' , top_n = 15 , ax = None , figsize = (6.0, 5.0) )
```

## Parameters

- `enrichment`: ( DataFrame ) – DataFrame returned by msea_ora() , msea_gsea() , or lion_enrichment() .
- `term_col`: ( Optional [ str ] (default: None )) – Column holding the pathway / term name. Auto-picks from pathway / term / Term / the index if None.
- `score_col`: ( str (default: 'pvalue' )) – Column to plot. "pvalue" (default) → -log10(pvalue) bars; "padj" for FDR-adjusted; "nes" for GSEA normalized enrichment score (plotted as-is, signed).
- `top_n`: ( int (default: 15 )) – Show the top- top_n terms by the score.
- `ax`: ( Optional [ Axes ] (default: None ))
- `figsize`: ( tuple [ float , float ] (default: (6.0, 5.0) ))

## Full Documentation

# omicverse.metabol.pathway_bar #

omicverse.metabol. pathway_bar ( enrichment , * , term_col = None , score_col = 'pvalue' , top_n = 15 , ax = None , figsize = (6.0, 5.0) ) [source] #

Horizontal bar chart of pathway enrichment p-values.

Works for both `msea_ora `output ( `pathway `/ `pvalue `) and `lion_enrichment `output ( `term `/ `pvalue `); auto-detects the term column if `term_col `isn’t given.

Parameters :

-
enrichment ( `DataFrame `) – DataFrame returned by `msea_ora() `, `msea_gsea() `, or `lion_enrichment() `.

-
term_col ( `Optional `[ `str `] (default: `None `)) – Column holding the pathway / term name. Auto-picks from `pathway `/ `term `/ `Term `/ the index if None.

-
score_col ( `str `(default: `'pvalue' `)) – Column to plot. `"pvalue" `(default) → `-log10(pvalue) `bars; `"padj" `for FDR-adjusted; `"nes" `for GSEA normalized enrichment score (plotted as-is, signed).

-
top_n ( `int `(default: `15 `)) – Show the top- `top_n `terms by the score.

-
ax ( `Optional `[ `Axes `] (default: `None `))

-
figsize ( `tuple `[ `float `, `float `] (default: `(6.0, 5.0) `))
