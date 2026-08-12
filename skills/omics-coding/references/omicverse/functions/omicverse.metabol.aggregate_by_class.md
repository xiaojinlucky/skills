# omicverse.metabol.aggregate_by_class #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.aggregate_by_class`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.aggregate_by_class.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Collapse the matrix to class-level totals.

## Signature

```text
omicverse.metabol. aggregate_by_class ( adata , * , agg = 'sum' )
```

## Parameters

- `adata`: ( AnnData )
- `agg`: ( str (default: 'sum' ))

## Full Documentation

# omicverse.metabol.aggregate_by_class #

omicverse.metabol. aggregate_by_class ( adata , * , agg = 'sum' ) [source] #

Collapse the matrix to class-level totals.

`adata.var['lipid_class'] `must already exist (run `annotate_lipids `first). Returns a new AnnData with `n_vars = n_lipid_classes `and per-sample class totals in `.X `. Handy for quick-look class-level QC and for some regression models.

Parameters :

-
adata ( `AnnData `)

-
agg ( `str `(default: `'sum' `))
