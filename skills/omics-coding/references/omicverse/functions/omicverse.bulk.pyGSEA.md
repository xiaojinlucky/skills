# omicverse.bulk.pyGSEA #

- Package: omicverse
- Language: Python
- Function: `omicverse.bulk.pyGSEA`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.bulk.pyGSEA.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Gene Set Enrichment Analysis (GSEA) wrapper for ranked gene lists.

## Signature

```text
class omicverse.bulk. pyGSEA ( gene_rnk , pathways_dict , processes = 1 , permutation_num = 1000 , outdir = './enrichr_gsea' , cutoff = 0.5 , organism = 'Human' , backend = 'numpy' , weight = 1.0 , min_size = 15 , max_size = 500 , progress = True )
```

## Parameters

- `gene_rnk`: ( pd.DataFrame ) – Ranked gene table used for enrichment scoring.
- `pathways_dict`: ( dict | str ) – Gene sets — a prepared dict, a .gmt / .txt path, or an Enrichr library name (resolved and auto-downloaded internally).
- `processes`: ( int , optional , default=8 ) – Number of worker processes.
- `permutation_num`: ( int , optional , default=100 ) – Number of permutations for enrichment significance.
- `outdir`: ( str , optional , default='./enrichr_gsea' ) – Output directory for reports and plots.
- `cutoff`: ( float , optional , default=0.5 ) – Significance/score threshold for result filtering.
- `organism`: Detected from function signature; no parameter description detected.
- `backend`: Detected from function signature; no parameter description detected.
- `weight`: Detected from function signature; no parameter description detected.
- `min_size`: Detected from function signature; no parameter description detected.
- `max_size`: Detected from function signature; no parameter description detected.
- `progress`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.bulk.pyGSEA #

class omicverse.bulk. pyGSEA ( gene_rnk , pathways_dict , processes = 1 , permutation_num = 1000 , outdir = './enrichr_gsea' , cutoff = 0.5 , organism = 'Human' , backend = 'numpy' , weight = 1.0 , min_size = 15 , max_size = 500 , progress = True ) [source] #

Gene Set Enrichment Analysis (GSEA) wrapper for ranked gene lists.

Parameters :

-
gene_rnk ( pd.DataFrame ) – Ranked gene table used for enrichment scoring.

-
pathways_dict ( dict | str ) – Gene sets — a prepared dict, a `.gmt `/ `.txt `path, or an Enrichr library name (resolved and auto-downloaded internally).

-
processes ( int , optional , default=8 ) – Number of worker processes.

-
permutation_num ( int , optional , default=100 ) – Number of permutations for enrichment significance.

-
outdir ( str , optional , default='./enrichr_gsea' ) – Output directory for reports and plots.

-
cutoff ( float , optional , default=0.5 ) – Significance/score threshold for result filtering.

Returns :

Initializes GSEA analysis settings.

Return type :

None

Examples

```text
>>> # Initialize GSEA object

```

Parameters :

-
organism ( `str `(default: `'Human' `))

-
backend ( `str `(default: `'numpy' `))

-
weight ( `float `(default: `1.0 `))

-
min_size ( `int `(default: `15 `))

-
max_size ( `int `(default: `500 `))

-
progress ( `bool `(default: `True `))

__init__ ( gene_rnk , pathways_dict , processes = 1 , permutation_num = 1000 , outdir = './enrichr_gsea' , cutoff = 0.5 , organism = 'Human' , backend = 'numpy' , weight = 1.0 , min_size = 15 , max_size = 500 , progress = True ) [source] #

Initialize pyGSEA with ranked genes and pathway libraries.

Parameters :

-
gene_rnk ( pandas.DataFrame ) – Ranked gene table equivalent to GSEA `.rnk `input.

-
pathways_dict ( dict ) – Dictionary of pathway collections/gene sets.

-
processes ( int , optional ) – Number of parallel worker processes.

-
permutation_num ( int , optional ) – Number of permutations for null distribution estimation.

-
outdir ( str , optional ) – Output directory for GSEA artifacts.

-
cutoff ( float , optional ) – Internal GSEA cutoff threshold.

-
organism ( `str `(default: `'Human' `))

-
backend ( `str `(default: `'numpy' `))

-
weight ( `float `(default: `1.0 `))

-
min_size ( `int `(default: `15 `))

-
max_size ( `int `(default: `500 `))

-
progress ( `bool `(default: `True `))

Methods

`__init__ `(gene_rnk, pathways_dict[, ...])

Initialize pyGSEA with ranked genes and pathway libraries.

`enrichment `([format, pval, seed])

Run GSEA and return filtered enrichment results.

`plot_enrichment `([num, node_size, cax_loc, ...])

Plot top GSEA terms as bubble enrichment chart.

`plot_gsea `([term_num, gene_set_title, ...])

Plot running-enrichment curve for one selected GSEA term.
