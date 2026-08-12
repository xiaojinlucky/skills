# omicverse.metabol.msea_ora #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.msea_ora`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.msea_ora.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Over-representation analysis via Fisher’s exact test.

## Signature

```text
omicverse.metabol. msea_ora ( hits , background , * , pathways = None , min_size = 3 , mass_db = None )
```

## Parameters

- `hits`: ( Iterable [ str ] ) – Metabolite names (e.g. from pyMetabo.significant_metabolites() ).
- `background`: ( Iterable [ str ] ) – All tested metabolite names (the universe). Usually adata.var_names after filtering.
- `pathways`: ( Optional [ dict [ str , list [ str ]]] (default: None )) – Optional override of {pathway_name: [kegg_id, ...]} . Default is the local KEGG subset shipped with omicverse.
- `min_size`: ( int (default: 3 )) – Skip pathways with fewer than this many overlapping background compounds.
- `mass_db`: ( Optional [ DataFrame ] (default: None )) – Optional pre-fetched ChEBI DataFrame from fetch_chebi_compounds() . When supplied, map_ids uses it as an in-memory lookup for the ~54 k ChEBI names and only falls back to PubChem for names not resolved there. On a cold session this turns the map_ids cost from O(n_features) HTTP round-trips into a single dict probe per feature — often a 30–100x speedup on the first call.

## Full Documentation

# omicverse.metabol.msea_ora #

omicverse.metabol. msea_ora ( hits , background , * , pathways = None , min_size = 3 , mass_db = None ) [source] #

Over-representation analysis via Fisher’s exact test.

Parameters :

-
hits ( `Iterable `[ `str `] ) – Metabolite names (e.g. from `pyMetabo.significant_metabolites() `).

-
background ( `Iterable `[ `str `] ) – All tested metabolite names (the universe). Usually `adata.var_names `after filtering.

-
pathways ( `Optional `[ `dict `[ `str `, `list `[ `str `]]] (default: `None `)) – Optional override of `{pathway_name: [kegg_id, ...]} `. Default is the local KEGG subset shipped with omicverse.

-
min_size ( `int `(default: `3 `)) – Skip pathways with fewer than this many overlapping background compounds.

-
mass_db ( `Optional `[ `DataFrame `] (default: `None `)) – Optional pre-fetched ChEBI DataFrame from `fetch_chebi_compounds() `. When supplied, `map_ids `uses it as an in-memory lookup for the ~54 k ChEBI names and only falls back to PubChem for names not resolved there. On a cold session this turns the `map_ids `cost from `O(n_features) `HTTP round-trips into a single dict probe per feature — often a 30–100x speedup on the first call.

Returns :

Columns: `pathway `, `overlap `, `set_size `, `universe_size `, `odds_ratio `, `pvalue `, `padj `(BH).

Return type :

pd.DataFrame
