# omicverse.metabol.msea_gsea #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.msea_gsea`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.msea_gsea.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

GSEA-style ranked enrichment via omicverse’s NumPy pre-ranked GSEA.

## Signature

```text
omicverse.metabol. msea_gsea ( deg , * , stat_col = 'stat' , pathways = None , n_perm = 1000 , min_size = 3 , max_size = 500 , seed = 0 , mass_db = None )
```

## Parameters

- `deg`: ( DataFrame ) – Output DataFrame from differential() . Rows indexed by metabolite name; column stat_col provides the ranking metric.
- `stat_col`: ( str (default: 'stat' )) – Which column of deg to rank on. Default "stat" (signed t-statistic); "log2fc" is another common choice.
- `pathways`: ( Optional [ dict [ str , list [ str ]]] (default: None )) – Dict mapping pathway name to list of KEGG compound IDs.
- `n_perm`: ( int (default: 1000 )) – Permutation count for the empirical null. 1000 is fine for tutorials; bump to ≥10000 for publication.
- `mass_db`: ( Optional [ DataFrame ] (default: None )) – Optional pre-fetched ChEBI DataFrame from fetch_chebi_compounds() — same role as in msea_ora() . Recommended for cold-cache runs to avoid per-name PubChem REST round-trips.
- `min_size`: ( int (default: 3 ))
- `max_size`: ( int (default: 500 ))
- `seed`: ( int (default: 0 ))

## Full Documentation

# omicverse.metabol.msea_gsea #

omicverse.metabol. msea_gsea ( deg , * , stat_col = 'stat' , pathways = None , n_perm = 1000 , min_size = 3 , max_size = 500 , seed = 0 , mass_db = None ) [source] #

GSEA-style ranked enrichment via omicverse’s NumPy pre-ranked GSEA.

Parameters :

-
deg ( `DataFrame `) – Output DataFrame from `differential() `. Rows indexed by metabolite name; column `stat_col `provides the ranking metric.

-
stat_col ( `str `(default: `'stat' `)) – Which column of `deg `to rank on. Default `"stat" `(signed t-statistic); `"log2fc" `is another common choice.

-
pathways ( `Optional `[ `dict `[ `str `, `list `[ `str `]]] (default: `None `)) – Dict mapping pathway name to list of KEGG compound IDs.

-
n_perm ( `int `(default: `1000 `)) – Permutation count for the empirical null. 1000 is fine for tutorials; bump to ≥10000 for publication.

-
mass_db ( `Optional `[ `DataFrame `] (default: `None `)) – Optional pre-fetched ChEBI DataFrame from `fetch_chebi_compounds() `— same role as in `msea_ora() `. Recommended for cold-cache runs to avoid per-name PubChem REST round-trips.

-
min_size ( `int `(default: `3 `))

-
max_size ( `int `(default: `500 `))

-
seed ( `int `(default: `0 `))

Returns :

Columns: `Term `, `NES `, `NOM p-val `, `FDR q-val `, `ES `, `Lead_genes `(metabolites driving the enrichment).

Return type :

pd.DataFrame
