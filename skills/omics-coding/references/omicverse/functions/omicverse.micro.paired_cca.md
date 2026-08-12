# omicverse.micro.paired_cca #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.paired_cca`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.paired_cca.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run sklearn CCA on the paired tables.

## Signature

```text
omicverse.micro. paired_cca ( adata_microbe , adata_metabolite , n_components = 3 , clr_microbe = True , log1p_metabolite = True , max_iter = 500 )
```

## Parameters

- `adata_microbe`: ( AnnData )
- `adata_metabolite`: ( AnnData )
- `n_components`: ( int (default: 3 ))
- `clr_microbe`: ( bool (default: True ))
- `log1p_metabolite`: ( bool (default: True ))
- `max_iter`: ( int (default: 500 ))

## Full Documentation

# omicverse.micro.paired_cca #

omicverse.micro. paired_cca ( adata_microbe , adata_metabolite , n_components = 3 , clr_microbe = True , log1p_metabolite = True , max_iter = 500 ) [source] #

Run sklearn CCA on the paired tables.

Returns a dict with keys:

-
`cca `— fitted `sklearn.cross_decomposition.CCA `

-
`x_scores `— sample × components (microbe side)

-
`y_scores `— sample × components (metabolite side)

-
`microbe_loadings `— DataFrame (features × components)

-
`metabolite_loadings `— DataFrame (features × components)

-
`canonical_correlations `— list of correlations per component

Parameters :

-
adata_microbe ( `AnnData `)

-
adata_metabolite ( `AnnData `)

-
n_components ( `int `(default: `3 `))

-
clr_microbe ( `bool `(default: `True `))

-
log1p_metabolite ( `bool `(default: `True `))

-
max_iter ( `int `(default: `500 `))
