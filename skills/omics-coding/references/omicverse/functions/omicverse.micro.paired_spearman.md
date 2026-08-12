# omicverse.micro.paired_spearman #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.paired_spearman`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.paired_spearman.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Rank correlation between every (microbe, metabolite) pair.

## Signature

```text
omicverse.micro. paired_spearman ( adata_microbe , adata_metabolite , clr_microbe = True , log1p_metabolite = True , min_prevalence = 0.0 )
```

## Parameters

- `adata_microbe`: ( AnnData ) – Must share obs_names (same samples, same order).
- `adata_metabolite`: ( AnnData ) – Must share obs_names (same samples, same order).
- `clr_microbe`: ( bool (default: True )) – CLR-transform the microbes first (recommended — compositional data).
- `log1p_metabolite`: ( bool (default: True )) – log(1 + x) -transform the metabolites first.
- `min_prevalence`: ( float (default: 0.0 )) – Drop microbes present in < this fraction of samples before testing (Spearman is undefined on constant rows).

## Full Documentation

# omicverse.micro.paired_spearman #

omicverse.micro. paired_spearman ( adata_microbe , adata_metabolite , clr_microbe = True , log1p_metabolite = True , min_prevalence = 0.0 ) [source] #

Rank correlation between every (microbe, metabolite) pair.

Parameters :

-
adata_microbe ( `AnnData `) – Must share `obs_names `(same samples, same order).

-
adata_metabolite ( `AnnData `) – Must share `obs_names `(same samples, same order).

-
clr_microbe ( `bool `(default: `True `)) – CLR-transform the microbes first (recommended — compositional data).

-
log1p_metabolite ( `bool `(default: `True `)) – `log(1 + x) `-transform the metabolites first.

-
min_prevalence ( `float `(default: `0.0 `)) – Drop microbes present in < this fraction of samples before testing (Spearman is undefined on constant rows).

Returns :

-
DataFrame with columns `microbe / metabolite / rho / p_value / fdr_bh `

-
sorted by `p_value `ascending.
