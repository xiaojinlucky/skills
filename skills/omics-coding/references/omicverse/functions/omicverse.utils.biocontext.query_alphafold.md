# omicverse.utils.biocontext.query_alphafold #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.biocontext.query_alphafold`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.biocontext.query_alphafold.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Query AlphaFold DB for predicted protein structure.

## Signature

```text
omicverse.utils.biocontext. query_alphafold ( protein_symbol , species = '9606' )
```

## Parameters

- `protein_symbol`: ( str ) – Gene or protein symbol.
- `species`: ( str ) – NCBI taxonomy ID. Default '9606' (human).

## Full Documentation

# omicverse.utils.biocontext.query_alphafold #

omicverse.utils.biocontext. query_alphafold ( protein_symbol , species = '9606' ) [source] #

Query AlphaFold DB for predicted protein structure.

Parameters :

-
protein_symbol ( str ) – Gene or protein symbol.

-
species ( str ) – NCBI taxonomy ID. Default `'9606' `(human).

Returns :

AlphaFold prediction data including confidence scores.

Return type :

dict
