# omicverse.space.pySTAGATE #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.pySTAGATE`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.pySTAGATE.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

A class representing the PyTorch implementation of STAGATE (Spatial Transcriptomics Analysis using Graph Attention autoEncoder).

## Signature

```text
class omicverse.space. pySTAGATE ( adata , num_batch_x , num_batch_y , spatial_key = ['X', 'Y'] , batch_size = 1 , rad_cutoff = 200 , num_epoch = 1000 , lr = 0.001 , weight_decay = 0.0001 , hidden_dims = [512, 30] , device = 'cuda:0' )
```

## Parameters

- `adata`: ( AnnData ) – Spatial AnnData with coordinates and expression matrix.
- `num_batch_x`: ( int ) – Number of tiles along x-axis for mini-batch graph construction.
- `num_batch_y`: ( int ) – Number of tiles along y-axis for mini-batch graph construction.
- `spatial_key`: ( list , default= [ 'X' , 'Y' ] ) – Coordinate columns in adata.obs used to build spatial graph.
- `batch_size`: ( int , default=1 ) – Number of tiled graphs per optimization step.
- `rad_cutoff`: ( int , default=200 ) – Radius cutoff when constructing spatial neighbors.
- `num_epoch`: ( int , default=1000 ) – Number of training epochs.
- `lr`: ( float , default=0.001 ) – Learning rate for Adam optimizer.
- `weight_decay`: ( float , default=1e-4 ) – L2 regularization strength.
- `hidden_dims`: ( list , default= [ 512 , 30 ] ) – Hidden-layer sizes of STAGATE encoder.
- `device`: ( str , default='cuda:0' ) – Device specifier; falls back to CPU when CUDA is unavailable.

## Full Documentation

# omicverse.space.pySTAGATE #

class omicverse.space. pySTAGATE ( adata , num_batch_x , num_batch_y , spatial_key = ['X', 'Y'] , batch_size = 1 , rad_cutoff = 200 , num_epoch = 1000 , lr = 0.001 , weight_decay = 0.0001 , hidden_dims = [512, 30] , device = 'cuda:0' ) [source] #

A class representing the PyTorch implementation of STAGATE (Spatial Transcriptomics Analysis using Graph Attention autoEncoder).

Parameters :

-
adata ( AnnData ) – Spatial AnnData with coordinates and expression matrix.

-
num_batch_x ( int ) – Number of tiles along x-axis for mini-batch graph construction.

-
num_batch_y ( int ) – Number of tiles along y-axis for mini-batch graph construction.

-
spatial_key ( list , default= [ 'X' , 'Y' ] ) – Coordinate columns in `adata.obs `used to build spatial graph.

-
batch_size ( int , default=1 ) – Number of tiled graphs per optimization step.

-
rad_cutoff ( int , default=200 ) – Radius cutoff when constructing spatial neighbors.

-
num_epoch ( int , default=1000 ) – Number of training epochs.

-
lr ( float , default=0.001 ) – Learning rate for Adam optimizer.

-
weight_decay ( float , default=1e-4 ) – L2 regularization strength.

-
hidden_dims ( list , default= [ 512 , 30 ] ) – Hidden-layer sizes of STAGATE encoder.

-
device ( str , default='cuda:0' ) – Device specifier; falls back to CPU when CUDA is unavailable.

-
Attributes –

device: torch.device

Device where the model is running.

loader: DataLoader

PyTorch DataLoader for batch processing.

model: STAGATE

The STAGATE model instance.

optimizer: torch.optim.Adam

Adam optimizer for model training.

adata: AnnData

Input annotated data matrix.

data: torch_geometric.data.Data

PyTorch geometric data object.

-
Notes – The STAGATE model is designed for analyzing spatial transcriptomics data by incorporating spatial information through a graph attention autoencoder architecture.

-
Examples –

```text
>>> import scanpy as sc
>>> import omicverse as ov
>>> adata = sc.read_h5ad('spatial_data.h5ad')
>>> stagate = ov.space.pySTAGATE(adata, num_batch_x=3, num_batch_y=2)
>>> stagate.train()
>>> stagate.predicted()

```

__init__ ( adata , num_batch_x , num_batch_y , spatial_key = ['X', 'Y'] , batch_size = 1 , rad_cutoff = 200 , num_epoch = 1000 , lr = 0.001 , weight_decay = 0.0001 , hidden_dims = [512, 30] , device = 'cuda:0' ) [source] #

Initialize STAGATE training components.

Parameters :

-
adata ( AnnData ) – Spatial AnnData for representation learning.

-
num_batch_x ( int ) – Number of x-axis tiles for batch graph generation.

-
num_batch_y ( int ) – Number of y-axis tiles for batch graph generation.

-
spatial_key ( list , default= [ 'X' , 'Y' ] ) – Coordinate columns in `adata.obs `.

-
batch_size ( int , default=1 ) – Number of tiled samples per gradient step.

-
rad_cutoff ( int , default=200 ) – Radius cutoff for neighborhood graph construction.

-
num_epoch ( int , default=1000 ) – Number of epochs for training.

-
lr ( float , default=0.001 ) – Learning rate for optimizer.

-
weight_decay ( float , default=1e-4 ) – Weight decay for optimizer.

-
hidden_dims ( list , default= [ 512 , 30 ] ) – Hidden dimensions for STAGATE network.

-
device ( str , default='cuda:0' ) – Compute device string.

Methods

`__init__ `(adata, num_batch_x, num_batch_y[, ...])

Initialize STAGATE training components.

`cal_pSM `([n_neighbors, resolution, ...])

Calculate the pseudo-spatial map using diffusion pseudotime (DPT) algorithm.

`predicted `()

Generate STAGATE representations and reconstruction values for all cells.

`train `()

Train the STAGATE model using the configured parameters.
