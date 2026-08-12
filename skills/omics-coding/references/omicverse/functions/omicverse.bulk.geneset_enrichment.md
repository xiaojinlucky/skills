# omicverse.bulk.geneset_enrichment #

- Package: omicverse
- Language: Python
- Function: `omicverse.bulk.geneset_enrichment`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.bulk.geneset_enrichment.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Perform pathway enrichment analysis using Enrichr-compatible gene-set libraries.

## Signature

```text
omicverse.bulk. geneset_enrichment ( gene_list , pathways_dict , pvalue_threshold = 0.05 , pvalue_type = 'auto' , organism = 'Human' , description = 'None' , background = None , outdir = './enrichr' , cutoff = 0.5 )
```

## Parameters

- `gene_list`: ( list ) – Input gene symbols (typically DEGs) for enrichment testing.
- `pathways_dict`: ( dict | str ) – Gene sets — a prepared dict ( ov.utils.geneset_prepare ), a .gmt / .txt path, or an Enrichr library name (resolved and auto-downloaded internally).
- `pvalue_threshold`: ( float , optional ) – Significance threshold used to filter enrichment terms.
- `pvalue_type`: ( str , optional ) – P-value mode: auto / adjust /raw P-value filtering.
- `organism`: ( str , optional ) – Organism label passed to Enrichr backend (for example Human / Mouse ).
- `description`: ( str , optional ) – Job description tag stored in output metadata.
- `background`: ( list | None , optional ) – Optional background gene universe. If None , species defaults are used.
- `outdir`: ( str , optional ) – Directory for enrichment output files.
- `cutoff`: ( float , optional ) – Enrichr internal cutoff threshold.

## Full Documentation

# omicverse.bulk.geneset_enrichment #

omicverse.bulk. geneset_enrichment ( gene_list , pathways_dict , pvalue_threshold = 0.05 , pvalue_type = 'auto' , organism = 'Human' , description = 'None' , background = None , outdir = './enrichr' , cutoff = 0.5 ) [source] #

Perform pathway enrichment analysis using Enrichr-compatible gene-set libraries.

Parameters :

-
gene_list ( list ) – Input gene symbols (typically DEGs) for enrichment testing.

-
pathways_dict ( dict | str ) – Gene sets — a prepared dict ( `ov.utils.geneset_prepare `), a `.gmt `/ `.txt `path, or an Enrichr library name (resolved and auto-downloaded internally).

-
pvalue_threshold ( float , optional ) – Significance threshold used to filter enrichment terms.

-
pvalue_type ( str , optional ) – P-value mode: `auto `/ `adjust `/raw `P-value `filtering.

-
organism ( str , optional ) – Organism label passed to Enrichr backend (for example `Human `/ `Mouse `).

-
description ( str , optional ) – Job description tag stored in output metadata.

-
background ( list | None , optional ) – Optional background gene universe. If `None `, species defaults are used.

-
outdir ( str , optional ) – Directory for enrichment output files.

-
cutoff ( float , optional ) – Enrichr internal cutoff threshold.

Returns :

Enrichment result table with statistics and derived plotting columns.

Return type :

pandas.DataFrame
