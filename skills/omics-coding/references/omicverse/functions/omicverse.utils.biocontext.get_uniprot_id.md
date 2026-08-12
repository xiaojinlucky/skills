# omicverse.utils.biocontext.get_uniprot_id #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.biocontext.get_uniprot_id`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.biocontext.get_uniprot_id.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Get UniProt accession ID from protein symbol.

## Signature

```text
omicverse.utils.biocontext. get_uniprot_id ( protein_symbol , species = '9606' )
```

## Parameters

- `protein_symbol`: ( str ) – Gene or protein symbol (e.g. 'TP53' ).
- `species`: ( str ) – NCBI taxonomy ID. Default '9606' (human).

## Full Documentation

# omicverse.utils.biocontext.get_uniprot_id #

omicverse.utils.biocontext. get_uniprot_id ( protein_symbol , species = '9606' ) [source] #

Get UniProt accession ID from protein symbol.

Parameters :

-
protein_symbol ( str ) – Gene or protein symbol (e.g. `'TP53' `).

-
species ( str ) – NCBI taxonomy ID. Default `'9606' `(human).

Returns :

UniProt accession ID.

Return type :

str
