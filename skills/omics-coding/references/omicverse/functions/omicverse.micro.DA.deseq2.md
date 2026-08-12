# omicverse.micro.DA.deseq2 #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.DA.deseq2`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.DA.deseq2.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Differential abundance via pyDESeq2 (negative-binomial GLM).

## Signature

```text
DA. deseq2 ( group_key , group_a = None , group_b = None , rank = None , min_prevalence = 0.1 , alpha = 0.05 )
```

## Parameters

- `group_key`: ( str ) – Column in adata.obs with the binary phenotype.
- `group_a`: ( str , optional ) – Class labels; if omitted, the two alphabetically smallest values in adata.obs[group_key] are used. Convention: log2fc > 0 ⇒ feature higher in group_a .
- `group_b`: ( str , optional ) – Class labels; if omitted, the two alphabetically smallest values in adata.obs[group_key] are used. Convention: log2fc > 0 ⇒ feature higher in group_a .
- `rank`: ( str , optional ) – Collapse counts to this taxonomic rank ( 'genus' , 'family' , …) before testing; None uses ASVs.
- `min_prevalence`: ( float , default 0.1 ) – Drop features present in fewer than this fraction of samples before testing.
- `alpha`: ( float , default 0.05 ) – FDR threshold passed to pyDESeq2’s summary .

## Full Documentation

# omicverse.micro.DA.deseq2 #

DA. deseq2 ( group_key , group_a = None , group_b = None , rank = None , min_prevalence = 0.1 , alpha = 0.05 ) [source] #

Differential abundance via pyDESeq2 (negative-binomial GLM).

Models raw integer counts directly with a NB GLM — no prior CLR / log transform. Mature method from RNA-seq adapted to microbiome composition; tends to be more conservative than Wilcoxon and has explicit shrinkage of small-count log-fold-changes. ANCOM-BC is closer to the compositional ground-truth but pyDESeq2 is faster and more widely cited.

Parameters :

-
group_key ( str ) – Column in `adata.obs `with the binary phenotype.

-
group_a ( str , optional ) – Class labels; if omitted, the two alphabetically smallest values in `adata.obs[group_key] `are used. Convention: `log2fc > 0 `⇒ feature higher in `group_a `.

-
group_b ( str , optional ) – Class labels; if omitted, the two alphabetically smallest values in `adata.obs[group_key] `are used. Convention: `log2fc > 0 `⇒ feature higher in `group_a `.

-
rank ( str , optional ) – Collapse counts to this taxonomic rank ( `'genus' `, `'family' `, …) before testing; `None `uses ASVs.

-
min_prevalence ( float , default 0.1 ) – Drop features present in fewer than this fraction of samples before testing.

-
alpha ( float , default 0.05 ) – FDR threshold passed to pyDESeq2’s summary .

Returns :

-
pd.DataFrame indexed by feature with columns `baseMean `,

-
`log2fc `, `lfcSE `, `stat `, `pvalue `, `padj `.
