# omicverse.micro.Ordinate #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.Ordinate`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.Ordinate.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Reduce a sample × sample distance matrix to 2-D / 3-D coords.

## Signature

```text
class omicverse.micro. Ordinate ( adata , dist_key = 'braycurtis' )
```

## Parameters

- `adata`: ( AnnData ) – AnnData with a distance matrix already computed by Beta.run() (stored in adata.obsp[dist_key] ).
- `dist_key`: ( str (default: 'braycurtis' )) – Key into adata.obsp . Defaults to 'braycurtis' .

## Full Documentation

# omicverse.micro.Ordinate #

class omicverse.micro. Ordinate ( adata , dist_key = 'braycurtis' ) [source] #

Reduce a sample × sample distance matrix to 2-D / 3-D coords.

Parameters :

-
adata ( `AnnData `) – AnnData with a distance matrix already computed by `Beta.run() `(stored in `adata.obsp[dist_key] `).

-
dist_key ( `str `(default: `'braycurtis' `)) – Key into `adata.obsp `. Defaults to `'braycurtis' `.

__init__ ( adata , dist_key = 'braycurtis' ) [source] #

Parameters :

-
adata ( `AnnData `)

-
dist_key ( `str `(default: `'braycurtis' `))

Methods

`__init__ `(adata[, dist_key])

`nmds `([n, random_state, write_to_obsm])

Non-metric multi-dimensional scaling on the distance matrix.

`pcoa `([n, write_to_obsm])

Principal coordinates analysis.

`proportion_explained `()

Eigenvalue proportions from the most recent PCoA call.
