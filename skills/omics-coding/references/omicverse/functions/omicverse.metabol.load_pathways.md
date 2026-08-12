# omicverse.metabol.load_pathways #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.load_pathways`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.load_pathways.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Return {pathway_name: [kegg_id, ...]} — the pathway database used by msea_ora() / msea_gsea() / mummichog_basic() .

## Signature

```text
omicverse.metabol. load_pathways ( path = None , * , organism = None )
```

## Parameters

- `path`: ( Optional [ Path ] (default: None )) – Override with your own pathway CSV (columns: pathway_name , kegg_compounds — the latter a ; -joined list of KEGG IDs). Useful for domain-specific pathway collections (e.g. SMPDB, Reactome-metabolite, or a curated clinical panel). Skips the network entirely.
- `organism`: ( Optional [ str ] (default: None )) – KEGG organism code for species-specific pathways ( "hsa" human, "mmu" mouse, …). Default None → species-agnostic map##### reference metabolic pathways, which is what enrichment papers usually use.

## Full Documentation

# omicverse.metabol.load_pathways #

omicverse.metabol. load_pathways ( path = None , * , organism = None ) [source] #

Return `{pathway_name: [kegg_id, ...]} `— the pathway database used by `msea_ora() `/ `msea_gsea() `/ `mummichog_basic() `.

The default is the full KEGG pathway database fetched from the public KEGG REST endpoint (cached under `~/.cache/omicverse/metabol/ `; ~550 pathways). First call needs network; subsequent calls are free.

Parameters :

-
path ( `Optional `[ `Path `] (default: `None `)) – Override with your own pathway CSV (columns: `pathway_name `, `kegg_compounds `— the latter a `; `-joined list of KEGG IDs). Useful for domain-specific pathway collections (e.g. SMPDB, Reactome-metabolite, or a curated clinical panel). Skips the network entirely.

-
organism ( `Optional `[ `str `] (default: `None `)) – KEGG organism code for species-specific pathways ( `"hsa" `human, `"mmu" `mouse, …). Default `None `→ species-agnostic `map##### `reference metabolic pathways, which is what enrichment papers usually use.
