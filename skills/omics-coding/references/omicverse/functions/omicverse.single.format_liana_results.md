# omicverse.single.format_liana_results #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.format_liana_results`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.format_liana_results.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Format LIANA results into the communication AnnData expected by ov.pl.ccc_* .

## Signature

```text
omicverse.single. format_liana_results ( adata = None , * , liana_res = None , uns_key = 'liana_res' , score_key = 'specificity_rank' , pvalue_key = 'specificity_rank' , inverse_score = True , inverse_pvalue = False , classification = None , classification_reference = 'cellchat' , classification_fallback = 'family' )
```

## Parameters

- `adata`: (default: None ) – AnnData containing adata.uns[uns_key] .
- `liana_res`: ( Optional [ DataFrame ] (default: None )) – LIANA result table. If omitted, it is read from adata.uns[uns_key] .
- `uns_key`: ( str (default: 'liana_res' )) – Key in adata.uns that stores the LIANA result DataFrame.
- `score_key`: ( str (default: 'specificity_rank' )) – Column used to populate layers['means'] . For current aggregated LIANA results, 'specificity_rank' is the safest default because 'magnitude_rank' can be empty on some datasets.
- `pvalue_key`: ( str (default: 'specificity_rank' )) – Column used to populate layers['pvalues'] . For aggregated LIANA results, 'specificity_rank' is recommended.
- `inverse_score`: ( bool (default: True )) – Whether smaller values in score_key should be transformed to larger communication strengths. This should stay True for rank-based scores.
- `inverse_pvalue`: ( bool (default: False )) – Whether smaller values in pvalue_key should be inverted before being written to layers['pvalues'] . Keep False for rank / p-value-like columns where smaller values indicate stronger support.
- `classification`: ( Union [ Mapping [ str , str ], str , None ] (default: None )) – Optional column name or ligand-receptor mapping used to populate var['classification'] .
- `classification_reference`: ( str | DataFrame | None (default: 'cellchat' )) – Optional built-in reference ( 'cellchat' , 'cellchat_human' , 'cellchat_mouse' ) or a custom DataFrame used to backfill pathway annotations for interactions not covered by classification .
- `classification_fallback`: ( str | None (default: 'family' )) – Fallback strategy for interactions still not covered after reference matching. Use 'family' for coarse signaling-family hints, a custom string for a fixed fallback label, or None to keep 'Unclassified' .

## Full Documentation

# omicverse.single.format_liana_results #

omicverse.single. format_liana_results ( adata = None , * , liana_res = None , uns_key = 'liana_res' , score_key = 'specificity_rank' , pvalue_key = 'specificity_rank' , inverse_score = True , inverse_pvalue = False , classification = None , classification_reference = 'cellchat' , classification_fallback = 'family' ) [source] #

Format LIANA results into the communication AnnData expected by `ov.pl.ccc_* `.

Parameters :

-
adata (default: `None `) – AnnData containing `adata.uns[uns_key] `.

-
liana_res ( `Optional `[ `DataFrame `] (default: `None `)) – LIANA result table. If omitted, it is read from `adata.uns[uns_key] `.

-
uns_key ( `str `(default: `'liana_res' `)) – Key in `adata.uns `that stores the LIANA result DataFrame.

-
score_key ( `str `(default: `'specificity_rank' `)) – Column used to populate `layers['means'] `. For current aggregated LIANA results, `'specificity_rank' `is the safest default because `'magnitude_rank' `can be empty on some datasets.

-
pvalue_key ( `str `(default: `'specificity_rank' `)) – Column used to populate `layers['pvalues'] `. For aggregated LIANA results, `'specificity_rank' `is recommended.

-
inverse_score ( `bool `(default: `True `)) – Whether smaller values in `score_key `should be transformed to larger communication strengths. This should stay `True `for rank-based scores.

-
inverse_pvalue ( `bool `(default: `False `)) – Whether smaller values in `pvalue_key `should be inverted before being written to `layers['pvalues'] `. Keep `False `for rank / p-value-like columns where smaller values indicate stronger support.

-
classification ( `Union `[ `Mapping `[ `str `, `str `], `str `, `None `] (default: `None `)) – Optional column name or ligand-receptor mapping used to populate `var['classification'] `.

-
classification_reference ( `str `| `DataFrame `| `None `(default: `'cellchat' `)) – Optional built-in reference ( `'cellchat' `, `'cellchat_human' `, `'cellchat_mouse' `) or a custom DataFrame used to backfill pathway annotations for interactions not covered by `classification `.

-
classification_fallback ( `str `| `None `(default: `'family' `)) – Fallback strategy for interactions still not covered after reference matching. Use `'family' `for coarse signaling-family hints, a custom string for a fixed fallback label, or `None `to keep `'Unclassified' `.

Returns :

Communication AnnData with `obs `cell-type pairs and `var `LR pairs.

Return type :

anndata.AnnData
