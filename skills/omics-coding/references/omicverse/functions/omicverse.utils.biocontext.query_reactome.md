# omicverse.utils.biocontext.query_reactome #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.biocontext.query_reactome`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.biocontext.query_reactome.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Query Reactome pathway database.

## Signature

```text
omicverse.utils.biocontext. query_reactome ( identifier , species = 'Homo sapiens' , include_disease = True )
```

## Parameters

- `identifier`: ( str ) – Gene symbol, UniProt ID, or Reactome stable ID.
- `species`: ( str ) – Species name. Default 'Homo sapiens' .
- `include_disease`: ( bool ) – Include disease-related pathways.

## Full Documentation

# omicverse.utils.biocontext.query_reactome #

omicverse.utils.biocontext. query_reactome ( identifier , species = 'Homo sapiens' , include_disease = True ) [source] #

Query Reactome pathway database.

Parameters :

-
identifier ( str ) – Gene symbol, UniProt ID, or Reactome stable ID.

-
species ( str ) – Species name. Default `'Homo sapiens' `.

-
include_disease ( bool ) – Include disease-related pathways.

Returns :

Reactome pathway analysis results.

Return type :

dict
