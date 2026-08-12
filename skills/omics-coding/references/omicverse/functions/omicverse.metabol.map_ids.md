# omicverse.metabol.map_ids #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.map_ids`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.map_ids.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Resolve metabolite names to external database IDs.

## Signature

```text
omicverse.metabol. map_ids ( names , * , targets = ('hmdb', 'kegg', 'chebi') , mass_db = None )
```

## Parameters

- `names`: ( Iterable [ str ] ) – Iterable of metabolite names (e.g. adata.var_names ).
- `targets`: ( tuple [ str , ... ] (default: ('hmdb', 'kegg', 'chebi') )) – Which external IDs to resolve — any subset of ("hmdb", "kegg", "chebi", "pubchem", "lipidmaps") .
- `mass_db`: ( Optional [ DataFrame ] (default: None )) – Optional pre-fetched ChEBI DataFrame from fetch_chebi_compounds() . When supplied, we look the name up in mass_db["name"] first (instant) and fall back to PubChem only for unresolved names. Recommended for workflows that call map_ids many times in a loop: fetch the DB once and pass it every call to avoid per-name HTTP round-trips.

## Full Documentation

# omicverse.metabol.map_ids #

omicverse.metabol. map_ids ( names , * , targets = ('hmdb', 'kegg', 'chebi') , mass_db = None ) [source] #

Resolve metabolite names to external database IDs.

Parameters :

-
names ( `Iterable `[ `str `] ) – Iterable of metabolite names (e.g. `adata.var_names `).

-
targets ( `tuple `[ `str `, `... `] (default: `('hmdb', 'kegg', 'chebi') `)) – Which external IDs to resolve — any subset of `("hmdb", "kegg", "chebi", "pubchem", "lipidmaps") `.

-
mass_db ( `Optional `[ `DataFrame `] (default: `None `)) – Optional pre-fetched ChEBI DataFrame from `fetch_chebi_compounds() `. When supplied, we look the name up in `mass_db["name"] ` first (instant) and fall back to PubChem only for unresolved names. Recommended for workflows that call `map_ids `many times in a loop: fetch the DB once and pass it every call to avoid per-name HTTP round-trips.

Returns :

One row per input name, indexed by the original (un-normalized) string, with one column per requested target. Empty string for unresolved targets.

Return type :

pd.DataFrame
