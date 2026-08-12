# omicverse.micro.Ordinate.pcoa #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.Ordinate.pcoa`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.Ordinate.pcoa.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Principal coordinates analysis.

## Signature

```text
Ordinate. pcoa ( n = 3 , write_to_obsm = True )
```

## Parameters

- `n`: ( int (default: 3 ))
- `write_to_obsm`: ( bool (default: True ))

## Full Documentation

# omicverse.micro.Ordinate.pcoa #

Ordinate. pcoa ( n = 3 , write_to_obsm = True ) [source] #

Principal coordinates analysis.

Stores coords in `adata.obsm[f'{dist_key}_pcoa'] `and the first n eigenvalues’ proportion explained in `adata.uns['micro'][f'{dist_key}_pcoa_var'] `.

Parameters :

-
n ( `int `(default: `3 `))

-
write_to_obsm ( `bool `(default: `True `))
