# omicverse.metabol.annotate_lipids #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.annotate_lipids`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.annotate_lipids.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Parse each var_name as a lipid and add lipid_class / total_carbons / total_db columns to adata.var .

## Signature

```text
omicverse.metabol. annotate_lipids ( adata , * , feature_names = None )
```

## Parameters

- `adata`: ( AnnData )
- `feature_names`: ( Optional [ Iterable [ str ]] (default: None ))

## Full Documentation

# omicverse.metabol.annotate_lipids #

omicverse.metabol. annotate_lipids ( adata , * , feature_names = None ) [source] #

Parse each `var_name `as a lipid and add `lipid_class `/ `total_carbons `/ `total_db `columns to `adata.var `.

Returns a copy of `adata `— existing columns are preserved. Unparseable names get `lipid_class = NaN `.

Parameters :

-
adata ( `AnnData `)

-
feature_names ( `Optional `[ `Iterable `[ `str `]] (default: `None `))
