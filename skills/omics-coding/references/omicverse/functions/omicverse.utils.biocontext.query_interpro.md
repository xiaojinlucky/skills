# omicverse.utils.biocontext.query_interpro #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.biocontext.query_interpro`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.biocontext.query_interpro.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Query InterPro for protein domains.

## Signature

```text
omicverse.utils.biocontext. query_interpro ( protein_id , source_db = None , include_structure_info = False )
```

## Parameters

- `protein_id`: ( str ) – UniProt accession (e.g. 'P04637' ).
- `source_db`: ( str , optional ) – Filter by source database (e.g. 'pfam' ).
- `include_structure_info`: ( bool ) – Include 3D structure information.

## Full Documentation

# omicverse.utils.biocontext.query_interpro #

omicverse.utils.biocontext. query_interpro ( protein_id , source_db = None , include_structure_info = False ) [source] #

Query InterPro for protein domains.

Parameters :

-
protein_id ( str ) – UniProt accession (e.g. `'P04637' `).

-
source_db ( str , optional ) – Filter by source database (e.g. `'pfam' `).

-
include_structure_info ( bool ) – Include 3D structure information.

Returns :

Domain and family annotations.

Return type :

dict
