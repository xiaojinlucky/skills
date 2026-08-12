# omicverse.space.Tangram #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.Tangram`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.Tangram.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Tangram spatial deconvolution class for cell type mapping.

## Signature

```text
class omicverse.space. Tangram ( adata_sc , adata_sp , clusters = '' , marker_size = 100 , gene_to_lowercase = False )
```

## Parameters

- `adata_sc`: ( AnnData ) – Single-cell reference AnnData with cell-type labels.
- `adata_sp`: ( AnnData ) – Spatial AnnData to receive projected cell-type information.
- `clusters`: ( str , default='' ) – Cell-type column name in adata_sc.obs .
- `marker_size`: ( int , default=100 ) – Number of marker genes selected per cell type for mapping.
- `gene_to_lowercase`: ( bool , default=False ) – Whether to lowercase gene names before matching genes across datasets.

## Full Documentation

# omicverse.space.Tangram #

class omicverse.space. Tangram ( adata_sc , adata_sp , clusters = '' , marker_size = 100 , gene_to_lowercase = False ) [source] #

Tangram spatial deconvolution class for cell type mapping.

Tangram is a method for integrating single-cell RNA sequencing (scRNA-seq) data with spatial transcriptomics data. It enables: 1. Mapping cell types from scRNA-seq to spatial locations 2. Deconvolving cell type proportions in spatial spots 3. Imputing gene expression in spatial data 4. Analyzing spatial organization of cell types

The method works by: 1. Identifying marker genes for each cell type 2. Training a mapping model using these markers 3. Projecting cell type annotations to spatial coordinates 4. Optionally imputing full gene expression profiles

Parameters :

-
adata_sc ( AnnData ) – Single-cell reference AnnData with cell-type labels.

-
adata_sp ( AnnData ) – Spatial AnnData to receive projected cell-type information.

-
clusters ( str , default='' ) – Cell-type column name in `adata_sc.obs `.

-
marker_size ( int , default=100 ) – Number of marker genes selected per cell type for mapping.

-
gene_to_lowercase ( bool , default=False ) – Whether to lowercase gene names before matching genes across datasets.

-
Attributes –

adata_sc: AnnData

Single-cell RNA-seq data with: - Gene expression matrix in X - Cell type annotations in obs[clusters]

adata_sp: AnnData

Spatial transcriptomics data with: - Gene expression matrix in X - Spatial coordinates in obsm[‘spatial’]

clusters: str

Column name in adata_sc.obs containing cell type labels

markers: list

Selected marker genes used for mapping

ad_map: AnnData

Mapping results after training

-
Examples –

```text
>>> import scanpy as sc
>>> import omicverse as ov
>>> # Load data
>>> adata_sc = sc.read_h5ad("sc_data.h5ad")
>>> adata_sp = sc.read_visium("spatial_data")
>>> # Initialize Tangram
>>> tangram = ov.space.Tangram(
... adata_sc=adata_sc,
... adata_sp=adata_sp,
... clusters='cell_type'
... )
>>> # Train model
>>> tangram.train(mode='clusters', num_epochs=500)
>>> # Project cell types
>>> adata_spatial = tangram.cell2location()

```

__init__ ( adata_sc , adata_sp , clusters = '' , marker_size = 100 , gene_to_lowercase = False ) [source] #

Initialize Tangram spatial deconvolution object.

This method sets up the Tangram analysis by: 1. Checking package installation 2. Processing input data 3. Identifying marker genes 4. Preparing data for mapping

Parameters :

-
adata_sc ( AnnData ) – Single-cell reference AnnData used as source profiles.

-
adata_sp ( AnnData ) – Spatial AnnData used as target tissue map.

-
clusters ( str , default='' ) – Cell-type annotation column in `adata_sc.obs `.

-
marker_size ( int , default=100 ) – Number of top-ranked marker genes selected per cell type.

-
gene_to_lowercase ( bool , default=False ) – Whether to lowercase gene names before intersection.

-
Notes –
-
Automatically filters genes present in at least one cell

-
Identifies marker genes using scanpy’s rank_genes_groups

-
Prepares data structures for Tangram mapping

-
Adds reference annotation to both AnnData objects

Methods

`__init__ `(adata_sc, adata_sp[, clusters, ...])

Initialize Tangram spatial deconvolution object.

`cell2location `([annotation_list])

Project cell type annotations to spatial coordinates.

`check_tangram `()

Check if Tangram package is installed.

`impute `([ad_map, ad_sc])

Impute gene expression in spatial data using trained model.

`train `([mode, num_epochs, device])

Train the Tangram spatial mapping model.
