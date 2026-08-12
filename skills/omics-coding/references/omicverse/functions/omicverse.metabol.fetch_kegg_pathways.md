# omicverse.metabol.fetch_kegg_pathways #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.fetch_kegg_pathways`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.fetch_kegg_pathways.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Fetch the full KEGG compound→pathway map via KEGG REST.

## Signature

```text
omicverse.metabol. fetch_kegg_pathways ( organism = None , * , cache = True , refresh = False )
```

## Parameters

- `organism`: ( Optional [ str ] (default: None )) – KEGG organism code ( "hsa" human, "mmu" mouse, …). When None , the reference pathway namespace ( map##### , species- agnostic metabolic pathways) is used. For metabolomics enrichment this is almost always what you want.
- `cache`: ( bool (default: True )) – Read/write a TSV cache at ~/.cache/omicverse/metabol/kegg_<org>.tsv .
- `refresh`: ( bool (default: False )) – Ignore the cache and re-fetch.

## Full Documentation

# omicverse.metabol.fetch_kegg_pathways #

omicverse.metabol. fetch_kegg_pathways ( organism = None , * , cache = True , refresh = False ) [source] #

Fetch the full KEGG compound→pathway map via KEGG REST.

Parameters :

-
organism ( `Optional `[ `str `] (default: `None `)) – KEGG organism code ( `"hsa" `human, `"mmu" `mouse, …). When `None `, the reference pathway namespace ( `map##### `, species- agnostic metabolic pathways) is used. For metabolomics enrichment this is almost always what you want.

-
cache ( `bool `(default: `True `)) – Read/write a TSV cache at `~/.cache/omicverse/metabol/kegg_<org>.tsv `.

-
refresh ( `bool `(default: `False `)) – Ignore the cache and re-fetch.

Returns :

`{pathway_name: [kegg_compound_id, ...]} `— the same shape `load_pathways() `returns for the shipped subset, so `msea_ora() `/ `msea_gsea() `accept it directly.

Return type :

dict [ str , list [ str ]]
