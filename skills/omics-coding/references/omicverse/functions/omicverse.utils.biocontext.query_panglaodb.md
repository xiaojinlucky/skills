# omicverse.utils.biocontext.query_panglaodb #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.biocontext.query_panglaodb`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.biocontext.query_panglaodb.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Query PanglaoDB for cell type marker genes.

## Signature

```text
omicverse.utils.biocontext. query_panglaodb ( species = 'Hs' , cell_type = None , gene_symbol = None , organ = None , min_sensitivity = None , min_specificity = None )
```

## Parameters

- `species`: ( str ) – 'Hs' (human), 'Mm' (mouse), or 'Mm Hs' (both).
- `cell_type`: ( str , optional ) – Cell type to query (e.g. 'T cells' ).
- `gene_symbol`: ( str , optional ) – Gene symbol to look up.
- `organ`: ( str , optional ) – Organ filter (e.g. 'Brain' ).
- `min_sensitivity`: ( float , optional ) – Minimum sensitivity threshold.
- `min_specificity`: ( float , optional ) – Minimum specificity threshold.

## Full Documentation

# omicverse.utils.biocontext.query_panglaodb #

omicverse.utils.biocontext. query_panglaodb ( species = 'Hs' , cell_type = None , gene_symbol = None , organ = None , min_sensitivity = None , min_specificity = None ) [source] #

Query PanglaoDB for cell type marker genes.

Parameters :

-
species ( str ) – `'Hs' `(human), `'Mm' `(mouse), or `'Mm Hs' `(both).

-
cell_type ( str , optional ) – Cell type to query (e.g. `'T cells' `).

-
gene_symbol ( str , optional ) – Gene symbol to look up.

-
organ ( str , optional ) – Organ filter (e.g. `'Brain' `).

-
min_sensitivity ( float , optional ) – Minimum sensitivity threshold.

-
min_specificity ( float , optional ) – Minimum specificity threshold.

Returns :

Marker gene table with sensitivity and specificity scores.

Return type :

pd.DataFrame
