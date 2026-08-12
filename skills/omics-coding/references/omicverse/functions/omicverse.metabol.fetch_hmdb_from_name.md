# omicverse.metabol.fetch_hmdb_from_name #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.fetch_hmdb_from_name`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.fetch_hmdb_from_name.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Resolve a metabolite name → HMDB / KEGG / ChEBI / PubChem CID.

## Signature

```text
omicverse.metabol. fetch_hmdb_from_name ( name , * , cache = True , refresh = False )
```

## Parameters

- `name`: ( str ) – Common name ( "Glucose" , "L-isoleucine" , …). Case- insensitive; PubChem’s synonym index covers most aliases.
- `cache`: ( bool (default: True )) – Cache under ~/.cache/omicverse/metabol/pubchem_xref_cache.json so repeat calls are free.
- `refresh`: ( bool (default: False )) – Force a network round-trip even if the name is cached.

## Full Documentation

# omicverse.metabol.fetch_hmdb_from_name #

omicverse.metabol. fetch_hmdb_from_name ( name , * , cache = True , refresh = False ) [source] #

Resolve a metabolite name → HMDB / KEGG / ChEBI / PubChem CID.

Uses the PubChem REST API in two hops:

-
`compound/name/<name>/cids/JSON `→ PubChem CID

-
`compound/cid/<cid>/xrefs/RegistryID/JSON `→ a long list of external registry IDs; we filter by regex to pick out the HMDB, KEGG-compound, and ChEBI identifiers.

PubChem is publicly-accessible, tolerant of synonyms, and gives HMDB/KEGG/ChEBI in a single call. No API key needed.

Parameters :

-
name ( `str `) – Common name ( `"Glucose" `, `"L-isoleucine" `, …). Case- insensitive; PubChem’s synonym index covers most aliases.

-
cache ( `bool `(default: `True `)) – Cache under `~/.cache/omicverse/metabol/pubchem_xref_cache.json `so repeat calls are free.

-
refresh ( `bool `(default: `False `)) – Force a network round-trip even if the name is cached.

Returns :

Keys: `hmdb `, `kegg `, `chebi `, `pubchem `. Missing ID → `"" `.

Return type :

dict [ str , str ]
