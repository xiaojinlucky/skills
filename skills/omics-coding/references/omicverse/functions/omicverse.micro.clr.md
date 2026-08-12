# omicverse.micro.clr #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.clr`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.clr.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

CLR transform: log(x_i) - mean(log(x)) per sample (post pseudo-count).

## Signature

```text
omicverse.micro. clr ( adata , layer_out = 'clr' , copy = False )
```

## Parameters

- `adata`: ( AnnData )
- `layer_out`: ( str (default: 'clr' ))
- `copy`: ( bool (default: False ))

## Full Documentation

# omicverse.micro.clr #

omicverse.micro. clr ( adata , layer_out = 'clr' , copy = False ) [source] #

CLR transform: `log(x_i) - mean(log(x)) `per sample (post pseudo-count).

Result is written to `adata.layers[layer_out] `. Negative values are expected; this is a vector-space transform that removes closure.

Parameters :

-
adata ( `AnnData `)

-
layer_out ( `str `(default: `'clr' `))

-
copy ( `bool `(default: `False `))
