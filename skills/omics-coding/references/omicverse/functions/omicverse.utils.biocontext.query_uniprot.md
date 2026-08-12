# omicverse.utils.biocontext.query_uniprot #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.biocontext.query_uniprot`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.biocontext.query_uniprot.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Query UniProt protein information.

## Signature

```text
omicverse.utils.biocontext. query_uniprot ( protein_id = None , protein_name = None , gene_symbol = None , species = '9606' , include_references = False )
```

## Parameters

- `protein_id`: ( str , optional ) – UniProt accession (e.g. 'P04637' ).
- `protein_name`: ( str , optional ) – Protein name to search.
- `gene_symbol`: ( str , optional ) – Gene symbol (e.g. 'TP53' ).
- `species`: ( str ) – NCBI taxonomy ID. Default '9606' (human).
- `include_references`: ( bool ) – Include literature references.

## Full Documentation

# omicverse.utils.biocontext.query_uniprot #

omicverse.utils.biocontext. query_uniprot ( protein_id = None , protein_name = None , gene_symbol = None , species = '9606' , include_references = False ) [source] #

Query UniProt protein information.

Provide at least one of `protein_id `, `protein_name `, or `gene_symbol `.

Parameters :

-
protein_id ( str , optional ) – UniProt accession (e.g. `'P04637' `).

-
protein_name ( str , optional ) – Protein name to search.

-
gene_symbol ( str , optional ) – Gene symbol (e.g. `'TP53' `).

-
species ( str ) – NCBI taxonomy ID. Default `'9606' `(human).

-
include_references ( bool ) – Include literature references.

Returns :

UniProt protein record.

Return type :

dict
