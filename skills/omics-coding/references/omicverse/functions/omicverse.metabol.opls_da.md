# omicverse.metabol.opls_da #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.opls_da`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.opls_da.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Orthogonal Projection to Latent Structures — Discriminant Analysis.

## Signature

```text
omicverse.metabol. opls_da ( adata , * , group_col = 'group' , group_a = None , group_b = None , n_ortho = 1 , scale = False , max_iter = 500 , tol = 1e-08 )
```

## Parameters

- `n_ortho`: ( int (default: 1 )) – Number of orthogonal components to extract. 1 is usually enough for a two-group comparison; increase if the data have strong batch or technical structure.
- `adata`: ( AnnData )
- `group_col`: ( str (default: 'group' ))
- `group_a`: ( Optional [ str ] (default: None ))
- `group_b`: ( Optional [ str ] (default: None ))
- `scale`: ( bool (default: False ))
- `max_iter`: ( int (default: 500 ))
- `tol`: ( float (default: 1e-08 ))

## Full Documentation

# omicverse.metabol.opls_da #

omicverse.metabol. opls_da ( adata , * , group_col = 'group' , group_a = None , group_b = None , n_ortho = 1 , scale = False , max_iter = 500 , tol = 1e-08 ) [source] #

Orthogonal Projection to Latent Structures — Discriminant Analysis.

Port of Trygg & Wold 2002 — NIPALS-style iteration that separates one predictive component (captures variance correlated with Y) from `n_ortho `orthogonal components (variance uncorrelated with Y but present in X). The predictive component’s loadings + VIP are the publication-quality output.

Parameters :

-
n_ortho ( `int `(default: `1 `)) – Number of orthogonal components to extract. 1 is usually enough for a two-group comparison; increase if the data have strong batch or technical structure.

-
adata ( `AnnData `)

-
group_col ( `str `(default: `'group' `))

-
group_a ( `Optional `[ `str `] (default: `None `))

-
group_b ( `Optional `[ `str `] (default: `None `))

-
scale ( `bool `(default: `False `))

-
max_iter ( `int `(default: `500 `))

-
tol ( `float `(default: `1e-08 `))
