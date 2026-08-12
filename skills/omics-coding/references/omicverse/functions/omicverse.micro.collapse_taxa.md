# omicverse.micro.collapse_taxa #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.collapse_taxa`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.collapse_taxa.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Collapse ASVs to a taxonomic rank.

## Signature

```text
omicverse.micro. collapse_taxa ( adata , rank = 'genus' , unassigned_label = 'Unassigned' )
```

## Parameters

- `adata`: ( AnnData )
- `rank`: ( str (default: 'genus' ))
- `unassigned_label`: ( str (default: 'Unassigned' ))

## Full Documentation

# omicverse.micro.collapse_taxa #

omicverse.micro. collapse_taxa ( adata , rank = 'genus' , unassigned_label = 'Unassigned' ) [source] #

Collapse ASVs to a taxonomic rank.

Returns a NEW AnnData where `var_names `are taxonomic labels at the chosen rank and counts are summed across ASVs sharing that label.

Parameters :

-
adata ( `AnnData `)

-
rank ( `str `(default: `'genus' `))

-
unassigned_label ( `str `(default: `'Unassigned' `))
