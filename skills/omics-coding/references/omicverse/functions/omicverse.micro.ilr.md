# omicverse.micro.ilr #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.ilr`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.ilr.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

ILR transform — orthonormal coordinate system after closure removal.

## Signature

```text
omicverse.micro. ilr ( adata , layer_out = 'ilr' , copy = False )
```

## Parameters

- `adata`: ( AnnData )
- `layer_out`: ( str (default: 'ilr' ))
- `copy`: ( bool (default: False ))

## Full Documentation

# omicverse.micro.ilr #

omicverse.micro. ilr ( adata , layer_out = 'ilr' , copy = False ) [source] #

ILR transform — orthonormal coordinate system after closure removal.

Stores an (n_samples × (n_features - 1)) matrix in `obsm[layer_out] `(not `layers `because ILR changes dimensionality).

Parameters :

-
adata ( `AnnData `)

-
layer_out ( `str `(default: `'ilr' `))

-
copy ( `bool `(default: `False `))
