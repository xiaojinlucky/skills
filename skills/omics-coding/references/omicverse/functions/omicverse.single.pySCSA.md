# omicverse.single.pySCSA #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.pySCSA`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.pySCSA.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Automated cell-type annotation using SCSA marker-enrichment scoring.

## Signature

```text
class omicverse.single. pySCSA ( adata , foldchange = 1.5 , pvalue = 0.05 , output = 'temp/rna_anno.txt' , model_path = '' , outfmt = 'txt' , Gensymbol = True , species = 'Human' , weight = 100 , tissue = 'All' , target = 'cellmarker' , celltype = 'normal' , norefdb = False , cellrange = None , noprint = True , list_tissue = False , tissuename = None , speciename = None )
```

## Parameters

- `adata`: ( anndata.AnnData ) – Query AnnData for cell-type annotation.
- `foldchange`: ( float , optional , default=1.5 ) – Fold-change cutoff for marker filtering.
- `pvalue`: ( float , optional , default=0.05 ) – P-value cutoff for marker filtering.
- `output`: ( str , optional , default='temp/rna_anno.txt' ) – Output path for SCSA annotation report.
- `model_path`: ( str , optional , default='' ) – Path to local SCSA database/model.
- `outfmt`: ( str , optional , default='txt' ) – Output format for intermediate annotation report.
- `Gensymbol`: ( bool , optional , default=True ) – Whether gene symbols are used as identifiers.
- `species`: ( str , optional , default='Human' ) – Species used for marker database matching.
- `weight`: ( int , optional , default=100 ) – Marker-weight scaling factor used by SCSA scoring.
- `tissue`: ( str , optional , default='All' ) – Tissue filter for marker database query.
- `target`: ( str , optional , default='cellmarker' ) – Marker database target (for example 'cellmarker' or 'panglaodb' ).
- `celltype`: ( str , optional , default='normal' ) – Annotation context/type mode used by SCSA.
- `norefdb`: ( bool , optional , default=False ) – If True , skip reference database matching.
- `cellrange`: ( str , optional , default=None ) – Optional range/filter for cell selection.
- `noprint`: ( bool , optional , default=True ) – If True , suppress verbose console output.
- `list_tissue`: ( bool , optional , default=False ) – If True , list available tissues and exit.
- `tissuename`: ( str , optional , default=None ) – Compatibility alias for tissue .
- `speciename`: ( str , optional , default=None ) – Compatibility alias for species .

## Full Documentation

# omicverse.single.pySCSA #

class omicverse.single. pySCSA ( adata , foldchange = 1.5 , pvalue = 0.05 , output = 'temp/rna_anno.txt' , model_path = '' , outfmt = 'txt' , Gensymbol = True , species = 'Human' , weight = 100 , tissue = 'All' , target = 'cellmarker' , celltype = 'normal' , norefdb = False , cellrange = None , noprint = True , list_tissue = False , tissuename = None , speciename = None ) [source] #

Automated cell-type annotation using SCSA marker-enrichment scoring.

Parameters :

-
adata ( anndata.AnnData ) – Query AnnData for cell-type annotation.

-
foldchange ( float , optional , default=1.5 ) – Fold-change cutoff for marker filtering.

-
pvalue ( float , optional , default=0.05 ) – P-value cutoff for marker filtering.

-
output ( str , optional , default='temp/rna_anno.txt' ) – Output path for SCSA annotation report.

-
model_path ( str , optional , default='' ) – Path to local SCSA database/model.

-
outfmt ( str , optional , default='txt' ) – Output format for intermediate annotation report.

-
Gensymbol ( bool , optional , default=True ) – Whether gene symbols are used as identifiers.

-
species ( str , optional , default='Human' ) – Species used for marker database matching.

-
weight ( int , optional , default=100 ) – Marker-weight scaling factor used by SCSA scoring.

-
tissue ( str , optional , default='All' ) – Tissue filter for marker database query.

-
target ( str , optional , default='cellmarker' ) – Marker database target (for example `'cellmarker' `or `'panglaodb' `).

-
celltype ( str , optional , default='normal' ) – Annotation context/type mode used by SCSA.

-
norefdb ( bool , optional , default=False ) – If `True `, skip reference database matching.

-
cellrange ( str , optional , default=None ) – Optional range/filter for cell selection.

-
noprint ( bool , optional , default=True ) – If `True `, suppress verbose console output.

-
list_tissue ( bool , optional , default=False ) – If `True `, list available tissues and exit.

-
tissuename ( str , optional , default=None ) – Compatibility alias for `tissue `.

-
speciename ( str , optional , default=None ) – Compatibility alias for `species `.

Returns :

Initializes SCSA annotation settings and database options.

Return type :

None

Examples

```text
>>> # CRITICAL: Use clustertype='leiden', NOT cluster='leiden'!

```

__init__ ( adata , foldchange = 1.5 , pvalue = 0.05 , output = 'temp/rna_anno.txt' , model_path = '' , outfmt = 'txt' , Gensymbol = True , species = 'Human' , weight = 100 , tissue = 'All' , target = 'cellmarker' , celltype = 'normal' , norefdb = False , cellrange = None , noprint = True , list_tissue = False , tissuename = None , speciename = None ) [source] #

Initialize SCSA annotation workflow configuration.

Parameters :

-
adata ( anndata.AnnData ) – Query AnnData object.

-
foldchange ( float ) – Fold-change threshold used for marker filtering.

-
pvalue ( float ) – P-value threshold used for marker filtering.

-
output ( str ) – Output path of annotation report.

-
model_path ( str ) – Local SCSA database path. If empty, downloads default database.

-
outfmt ( str ) – Output format for SCSA report.

-
Gensymbol ( bool ) – Whether input gene identifiers are gene symbols.

-
species ( str ) – Species used for marker-database lookup.

-
weight ( int ) – SCSA weighting parameter.

-
tissue ( str ) – Tissue filter used for database matching.

-
target ( str ) – Marker database target (for example `cellmarker `).

-
celltype ( str ) – Cell-type mode used by SCSA.

-
norefdb ( bool ) – Whether to disable reference database.

-
cellrange ( str or None ) – Optional lineage restriction (for example T-cell subtypes only).

-
noprint ( bool ) – Whether to suppress verbose output.

-
list_tissue ( bool ) – Whether to list available tissues.

-
tissuename ( str or None ) – Compatibility alias for `tissue `.

-
speciename ( str or None ) – Compatibility alias for `species `.

Methods

`__init__ `(adata[, foldchange, pvalue, ...])

Initialize SCSA annotation workflow configuration.

`cell_anno `([clustertype, cluster, rank_rep])

Annotate cell type for each cluster.

`cell_anno_print `()

Print the annotation result.

`cell_auto_anno `(adata[, clustertype, key])

Add cell type annotation to anndata.obs['scsa_celltype'].

`get_celltype_marker `(adata[, clustertype, ...])

Get marker genes for each clusters.

`get_model_tissue `([species])

List all available tissues in the database.
