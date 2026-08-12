# omicverse.utils.biocontext.query_string #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.biocontext.query_string`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.biocontext.query_string.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Query STRING for protein-protein interactions.

## Signature

```text
omicverse.utils.biocontext. query_string ( protein_symbol , species = 9606 , min_score = None )
```

## Parameters

- `protein_symbol`: ( str ) – Protein symbol.
- `species`: ( int ) – NCBI taxonomy ID. Default 9606 (human).
- `min_score`: ( float , optional ) – Minimum interaction score (0-1).

## Full Documentation

# omicverse.utils.biocontext.query_string #

omicverse.utils.biocontext. query_string ( protein_symbol , species = 9606 , min_score = None ) [source] #

Query STRING for protein-protein interactions.

Parameters :

-
protein_symbol ( str ) – Protein symbol.

-
species ( int ) – NCBI taxonomy ID. Default 9606 (human).

-
min_score ( float , optional ) – Minimum interaction score (0-1).

Returns :

STRING interaction data.

Return type :

dict
