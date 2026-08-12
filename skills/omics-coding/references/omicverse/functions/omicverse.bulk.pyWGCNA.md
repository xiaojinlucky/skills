# omicverse.bulk.pyWGCNA #

- Package: omicverse
- Language: Python
- Function: `omicverse.bulk.pyWGCNA`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.bulk.pyWGCNA.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Weighted Gene Co-expression Network Analysis.

## Signature

```text
class omicverse.bulk. pyWGCNA ( name = 'WGCNA' , TPMcutoff = 1 , powers = None , RsquaredCut = 0.85 , MeanCut = 100 , networkType = 'signed hybrid' , TOMType = 'signed' , minModuleSize = 50 , naColor = 'grey' , cut = inf , MEDissThres = 0.2 , species = None , level = 'gene' , anndata = None , geneExp = None , geneExpPath = None , sep = ',' , geneInfo = None , sampleInfo = None , save = False , outputPath = None , figureType = 'pdf' )
```

## Parameters

- `name`: ( str ) – Analysis label, used for output file names.
- `species`: ( str ) – Organism (e.g. "mus musculus" , "homo sapiens" ).
- `geneExp`: ( pandas.DataFrame ) – Expression matrix shaped (samples × genes): sample identifiers are the row index, gene identifiers are the column names — the same orientation AnnData uses. (The upstream PyWGCNA docstring claims the opposite, but its constructor in geneExp.py treats rows as samples and columns as genes, so pass samples × genes.)
- `TPMcutoff`: ( float , default 1 ) – Per-gene TPM threshold; genes whose maximum across samples falls below this are dropped during preprocess .
- `powers`: ( list [ int ] , optional ) – Candidate soft-threshold powers. Defaults to a 1–30 sweep.
- `networkType`: ( {"signed" , "unsigned" , "signed hybrid"} ) – How adjacency is computed from correlation.
- `minModuleSize`: ( int , default 50 ) – Smallest module size kept by the dynamic tree cut.
- `save`: ( bool , default False ) – Whether to persist results to disk.
- `RsquaredCut`: Detected from function signature; no parameter description detected.
- `MeanCut`: Detected from function signature; no parameter description detected.
- `TOMType`: Detected from function signature; no parameter description detected.
- `naColor`: Detected from function signature; no parameter description detected.
- `cut`: Detected from function signature; no parameter description detected.
- `MEDissThres`: Detected from function signature; no parameter description detected.
- `level`: Detected from function signature; no parameter description detected.
- `anndata`: Detected from function signature; no parameter description detected.
- `geneExpPath`: Detected from function signature; no parameter description detected.
- `sep`: Detected from function signature; no parameter description detected.
- `geneInfo`: Detected from function signature; no parameter description detected.
- `sampleInfo`: Detected from function signature; no parameter description detected.
- `outputPath`: Detected from function signature; no parameter description detected.
- `figureType`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.bulk.pyWGCNA #

class omicverse.bulk. pyWGCNA ( name = 'WGCNA' , TPMcutoff = 1 , powers = None , RsquaredCut = 0.85 , MeanCut = 100 , networkType = 'signed hybrid' , TOMType = 'signed' , minModuleSize = 50 , naColor = 'grey' , cut = inf , MEDissThres = 0.2 , species = None , level = 'gene' , anndata = None , geneExp = None , geneExpPath = None , sep = ',' , geneInfo = None , sampleInfo = None , save = False , outputPath = None , figureType = 'pdf' ) [source] #

Weighted Gene Co-expression Network Analysis.

Identifies highly co-expressed gene modules and relates them to clinical traits / sample metadata. Standard WGCNA workflow:

-
Preprocess — remove low-expressed genes (TPM cutoff) and outlier samples (Euclidean distance to mean).

-
Soft-thresholding — pick a power that yields scale-free topology in the gene-gene correlation network.

-
Adjacency + TOM — adjacency = `|cor|^power `; topological overlap matrix (TOM) measures shared neighbourhood.

-
Dynamic tree cut — hierarchical clustering on `1 - TOM `; tree cut yields gene modules (named by colour).

-
Module eigengenes — first principal component of each module’s expression matrix.

-
Module-trait correlation — Pearson correlation of each module eigengene against numeric sample traits, with FDR-corrected p-values.

Parameters :

-
name ( str ) – Analysis label, used for output file names.

-
species ( str ) – Organism (e.g. `"mus musculus" `, `"homo sapiens" `).

-
geneExp ( pandas.DataFrame ) – Expression matrix shaped (samples × genes): sample identifiers are the row index, gene identifiers are the column names — the same orientation AnnData uses. (The upstream PyWGCNA docstring claims the opposite, but its constructor in `geneExp.py `treats rows as samples and columns as genes, so pass samples × genes.)

-
TPMcutoff ( float , default 1 ) – Per-gene TPM threshold; genes whose maximum across samples falls below this are dropped during `preprocess `.

-
powers ( list [ int ] , optional ) – Candidate soft-threshold powers. Defaults to a 1–30 sweep.

-
networkType ( {"signed" , "unsigned" , "signed hybrid"} ) – How adjacency is computed from correlation.

-
minModuleSize ( int , default 50 ) – Smallest module size kept by the dynamic tree cut.

-
save ( bool , default False ) – Whether to persist results to disk.

Notes

Expression CSVs are usually already shaped samples × genes (rows = samples, columns = genes); pass them directly — do not transpose.

Methods (call in this order — each step populates the attributes listed under it). Use the high-level `runWGCNA() `to chain everything end-to-end, or the explicit methods below for finer control:

-
`preprocess() `— drop low-TPM genes, drop outlier samples (updates `self.datExpr `).

-
`calculate_soft_threshold() `— scale-free fit power scan; sets `self.power `(int, not `self.softPower `) and `self.sft `(DataFrame with R²/slope/k per power).

-
`calculating_adjacency_matrix() `— sets `self.adjacency `.

-
`calculating_TOM_similarity_matrix() `— sets `self.TOM `.

-
`calculate_geneTree() `— sets `self.geneTree `(linkage matrix).

-
`calculate_dynamicMods(kwargs_function={...}) `— sets `self.dynamicMods `and `self.datExpr.var['dynamicColors'] `.

-
`calculate_gene_module(kwargs_function={...}) `— merges close modules, sets `self.datExpr.var['moduleColors'] `, `self.datExpr.var['moduleLabels'] `, `self.MEs `, `self.datME `.

-
`findModules() `— convenience that runs the soft-threshold + adjacency + TOM + tree + module merge as one call (preferred). Pass `findModules(max_block_size=5000) `for large gene counts: this switches to the memory-bounded blockwise pipeline (the R WGCNA `blockwiseModules `analogue) — genes are pre-clustered into size-capped blocks and the dense gene×gene adjacency / TOM is built one block at a time, so peak memory is `max_block_size² `instead of `N² `. Without it, `N >> 10000 `genes can OOM.

-
`runWGCNA() `— runs `preprocess() `then `findModules() `.

-
`analyseWGCNA(geneList=None) `— module–trait correlation; sets `self.moduleTraitCor `and `self.moduleTraitPvalue `. Requires sample metadata (set via `updateSampleInfo(...) `or passed via `sampleInfo `at construction).

Attributes (state machine — populated in this order). The class is a thin shim that delegates to the upstream PyWGCNA implementation; these are the actual attribute names on the returned instance, which agents commonly mis-spell:

-
`self.geneExpr `— AnnData (genes × samples) holding the original input expression.

-
`self.datExpr `— AnnData (genes × samples), filtered after `preprocess() `. Per-gene module annotations live on `self.datExpr.var `.

-
`self.power `(int) — chosen soft-threshold power. The attribute is ``power``, NOT ``softPower``. Set after `calculate_soft_threshold() `or `findModules() `; before that it is `0 `.

-
`self.sft `(pandas.DataFrame) — scale-free fit table per candidate power (columns: `Power `, `SFT.R.sq `, `slope `, `mean(k) `, …). Set together with `self.power `.

-
`self.adjacency `(pandas.DataFrame) — gene-gene weighted adjacency. `None `until `calculating_adjacency_matrix() `/ `findModules() `runs.

-
`self.TOM `(numpy.ndarray) — topological overlap matrix. `None `until `calculating_TOM_similarity_matrix() `/ `findModules() `runs.

-
`self.geneTree `— scipy linkage matrix from `1 - TOM `.

-
`self.dynamicMods `— initial dynamic-tree-cut module integer labels per gene.

-
`self.datExpr.var['dynamicColors'] `— initial module colour per gene (string, e.g. `'turquoise' `).

-
`self.datExpr.var['moduleColors'] `— final module colour per gene (after merging close modules). Use this for downstream.

-
`self.datExpr.var['moduleLabels'] `— integer label per gene aligned to `moduleColors `.

-
`self.MEs `(pandas.DataFrame) — module eigengenes, samples × modules. Do not compute this manually — the class already provides it; manual mean-by-mask is not equivalent (eigengene = first PC of the module’s expression, not the mean).

-
`self.datME `— pre-merge eigengene matrix; usually `self.MEs `is what you want.

-
`self.moduleTraitCor `(pandas.DataFrame) — module × trait Pearson correlations. `None `until `analyseWGCNA() `runs.

-
`self.moduleTraitPvalue `(pandas.DataFrame) — parallel p-value table. `None `until `analyseWGCNA() `runs.

Examples

```text
>>> import pandas as pd, omicverse as ov
>>> data = pd.read_csv('expressionList.csv', index_col=0) # samples × genes
>>> wgcna = ov.bulk.pyWGCNA(
... name='5xFAD',
... species='mus musculus',
... geneExp=data, # rows = samples, columns = genes
... TPMcutoff=1,
... networkType='signed hybrid',
... )
>>> wgcna.preprocess()
>>> wgcna.findModules() # or findModules(max_block_size=5000)

```

__init__ ( ) #

Methods

`__init__ `()
