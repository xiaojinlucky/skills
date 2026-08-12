# omicverse.space.STT #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.STT`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.STT.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Spatial Transition Tensor (STT) analysis class.

## Signature

```text
class omicverse.space. STT ( adata , spatial_loc = 'xy_loc' , region = 'Region' )
```

## Parameters

- `adata`: ( AnnData ) – Spatial AnnData containing spliced/unspliced layers and coordinates.
- `spatial_loc`: ( str , default='xy_loc' ) – Coordinate key in adata.obsm .
- `region`: ( str , default='Region' ) – Region annotation column in adata.obs .

## Full Documentation

# omicverse.space.STT #

class omicverse.space. STT ( adata , spatial_loc = 'xy_loc' , region = 'Region' ) [source] #

Spatial Transition Tensor (STT) analysis class.

STT models spatial dynamics and transitions by learning spatial-temporal patterns in spatial transcriptomics data using transition tensors. This class provides methods for analyzing cell state transitions, developmental trajectories, and spatial dynamics in tissue organization.

Parameters :

-
adata ( AnnData ) – Spatial AnnData containing spliced/unspliced layers and coordinates.

-
spatial_loc ( str , default='xy_loc' ) – Coordinate key in `adata.obsm `.

-
region ( str , default='Region' ) – Region annotation column in `adata.obs `.

-
Attributes –

adata: AnnData

Input annotated data matrix.

adata_aggr: AnnData or None

Aggregated data after training.

spatial_loc: str

Key for spatial coordinates.

region: str

Key for region annotations.

-
Examples –

```text
>>> import scanpy as sc
>>> import omicverse as ov
>>> # Load data with spliced/unspliced counts
>>> adata = sc.read_h5ad('spatial_velocity.h5ad')
>>> # Initialize STT object
>>> stt = ov.space.STT(
... adata,
... spatial_loc='spatial',
... region='tissue_region'
... )
>>> # Estimate cell stages
>>> stt.stage_estimate()
>>> # Train the model
>>> stt.train(n_states=10)

```

__init__ ( adata , spatial_loc = 'xy_loc' , region = 'Region' ) [source] #

Initialize STT spatial transition analysis object.

Parameters :

-
adata ( AnnData ) – Input AnnData with spatial and velocity-related layers.

-
spatial_loc ( str , default='xy_loc' ) – Coordinate key in `adata.obsm `.

-
region ( str , default='Region' ) – Region key in `adata.obs `.

Methods

`__init__ `(adata[, spatial_loc, region])

Initialize STT spatial transition analysis object.

`compute_pathway `(pathway_dict[, n_components])

Compute spatial pathways for cell transitions.

`construct_landscape `([coord_key])

Construct spatial landscape for transition analysis.

`infer_lineage `(**kwargs)

Infer cell lineage relationships from spatial transitions.

`load `(adata, adata_aggr)

Load pre-trained STT model data.

`plot_landscape `(**kwargs)

Plot spatial landscape visualization.

`plot_pathway `([label_fontsize])

Plot spatial transition pathways.

`plot_sankey `(vector1, vector2)

Plot Sankey diagram for cell transitions.

`plot_tensor `(list_attractor, **kwargs)

Plot spatial transition tensors.

`plot_tensor_pathway `(pathway_name, **kwargs)

Plot tensor-based spatial pathways.

`plot_top_genes `(**kwargs)

Plot top genes driving spatial transitions.

`stage_estimate `()

Estimate cell stages using joint clustering of spliced and unspliced data.

`train `([n_states, n_iter, ...])

Train the STT spatial transition model.
