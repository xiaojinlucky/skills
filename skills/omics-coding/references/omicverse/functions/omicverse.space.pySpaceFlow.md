# omicverse.space.pySpaceFlow #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.pySpaceFlow`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.pySpaceFlow.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

SpaceFlow spatial flow analysis class.

## Signature

```text
class omicverse.space. pySpaceFlow ( adata )
```

## Parameters

- `adata`: ( AnnData ) – Spatial AnnData containing expression and coordinates in adata.obsm['spatial'] .

## Full Documentation

# omicverse.space.pySpaceFlow #

class omicverse.space. pySpaceFlow ( adata ) [source] #

SpaceFlow spatial flow analysis class.

SpaceFlow is a deep learning method for analyzing spatial transcriptomics data by learning spatially-aware cell representations. It combines graph neural networks with spatial regularization to capture both transcriptional and spatial relationships between cells.

The method: 1. Constructs a spatial neighborhood graph 2. Learns embeddings using deep graph infomax 3. Applies spatial regularization to preserve spatial structure 4. Generates pseudo-spatial maps for trajectory analysis

Parameters :

-
adata ( AnnData ) – Spatial AnnData containing expression and coordinates in `adata.obsm['spatial'] `.

-
Attributes –

adata: AnnData

Input annotated data matrix containing: - Gene expression data in adata.X - Spatial coordinates in adata.obsm[‘spatial’]

sf: SpaceFlow

Internal SpaceFlow object for computations

embedding: array

Learned spatial-aware embeddings after training

-
Examples –

```text
>>> import scanpy as sc
>>> import omicverse as ov
>>> # Load spatial data
>>> adata = sc.read_visium(...)
>>> # Initialize SpaceFlow
>>> spaceflow = ov.space.pySpaceFlow(adata)
>>> # Train model
>>> embedding = spaceflow.train(
... spatial_regularization_strength=0.1,
... z_dim=50,
... epochs=1000
... )
>>> # Calculate pseudo-spatial map
>>> psm = spaceflow.cal_pSM(n_neighbors=20)

```

__init__ ( adata ) [source] #

Initialize SpaceFlow spatial analysis object.

Parameters :

-
adata ( AnnData ) – Spatial AnnData used for SpaceFlow embedding.

-
Notes –
-
Automatically checks for SpaceFlow package installation

-
Constructs initial spatial neighborhood graph

-
Uses 10 nearest neighbors for graph construction

-
Stores SpaceFlow object in self.sf

Methods

`__init__ `(adata)

Initialize SpaceFlow spatial analysis object.

`cal_pSM `([n_neighbors, resolution, ...])

Calculate pseudo-spatial map using diffusion pseudotime.

`train `([spatial_regularization_strength, ...])

Train SpaceFlow model for spatial embedding.
