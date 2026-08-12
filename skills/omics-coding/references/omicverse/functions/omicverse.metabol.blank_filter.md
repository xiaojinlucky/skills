# omicverse.metabol.blank_filter #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.blank_filter`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.blank_filter.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Drop features whose sample-mean intensity isn’t at least ratio × the blank-mean intensity.

## Signature

```text
omicverse.metabol. blank_filter ( adata , * , blank_mask , ratio = 3.0 )
```

## Parameters

- `blank_mask`: ( str | ndarray ) – Column name (bool) or bool array marking blank / extraction-control samples in adata.obs .
- `ratio`: ( float (default: 3.0 )) – Features with mean(sample)/mean(blank) < ratio are dropped. 3× is the community default; 5× for more stringent filtering.
- `adata`: ( AnnData )

## Full Documentation

# omicverse.metabol.blank_filter #

omicverse.metabol. blank_filter ( adata , * , blank_mask , ratio = 3.0 ) [source] #

Drop features whose sample-mean intensity isn’t at least `ratio `× the blank-mean intensity.

Parameters :

-
blank_mask ( `str `| `ndarray `) – Column name (bool) or bool array marking blank / extraction-control samples in `adata.obs `.

-
ratio ( `float `(default: `3.0 `)) – Features with `mean(sample)/mean(blank) < ratio `are dropped. 3× is the community default; 5× for more stringent filtering.

-
adata ( `AnnData `)
