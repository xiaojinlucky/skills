# omicverse.space.pySTAligner #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.pySTAligner`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.pySTAligner.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

STAligner for spatial transcriptomics data integration.

## Signature

```text
class omicverse.space. pySTAligner ( adata , hidden_dims = [512, 30] , n_epochs = 1000 , lr = 0.001 , batch_key = 'batch_name' , key_added = 'STAligner' , gradient_clipping = 5 , weight_decay = 0.0001 , margin = 1 , verbose = False , random_seed = 666 , iter_comb = None , knn_neigh = 100 , Batch_list = None , device = torch.device )
```

## Parameters

- `adata`: ( AnnData ) – Combined multi-batch AnnData for integration.
- `hidden_dims`: ( list , default= [ 512 , 30 ] ) – Hidden dimensions of STAligner encoder.
- `n_epochs`: ( int , default=1000 ) – Total training epochs.
- `lr`: ( float , default=0.001 ) – Optimizer learning rate.
- `batch_key`: ( str , default='batch_name' ) – Batch column in adata.obs .
- `key_added`: ( str , default='STAligner' ) – Output embedding key in adata.obsm .
- `gradient_clipping`: ( float , default=5 ) – Max norm for gradient clipping.
- `weight_decay`: ( float , default=0.0001 ) – L2 regularization term.
- `margin`: ( float , default=1 ) – Margin used in triplet loss during alignment.
- `verbose`: ( bool , default=False ) – Whether to print detailed training logs.
- `random_seed`: ( int , default=666 ) – Random seed for reproducibility.
- `iter_comb`: ( list , optional ) – Batch-pair list for MNN comparison.
- `knn_neigh`: ( int , default=100 ) – K for mutual nearest-neighbor search.
- `Batch_list`: ( list , optional ) – Per-batch AnnData list aligned to batch_key .
- `device`: ( torch.device , default=auto cuda/cpu ) – Device used for model training.

## Full Documentation

# omicverse.space.pySTAligner #

class omicverse.space. pySTAligner ( adata , hidden_dims = [512, 30] , n_epochs = 1000 , lr = 0.001 , batch_key = 'batch_name' , key_added = 'STAligner' , gradient_clipping = 5 , weight_decay = 0.0001 , margin = 1 , verbose = False , random_seed = 666 , iter_comb = None , knn_neigh = 100 , Batch_list = None , device = torch.device ) [source] #

STAligner for spatial transcriptomics data integration.

STAligner is a deep learning method for integrating spatial transcriptomics data across different experimental conditions, technologies, and developmental stages. It combines graph neural networks with mutual nearest neighbors to preserve both transcriptional and spatial relationships during integration.

The method works by: 1. Constructing spatial neighborhood graphs 2. Learning batch-invariant embeddings 3. Aligning similar regions across batches 4. Preserving spatial organization 5. Enabling cross-condition comparison

Parameters :

-
adata ( AnnData ) – Combined multi-batch AnnData for integration.

-
hidden_dims ( list , default= [ 512 , 30 ] ) – Hidden dimensions of STAligner encoder.

-
n_epochs ( int , default=1000 ) – Total training epochs.

-
lr ( float , default=0.001 ) – Optimizer learning rate.

-
batch_key ( str , default='batch_name' ) – Batch column in `adata.obs `.

-
key_added ( str , default='STAligner' ) – Output embedding key in `adata.obsm `.

-
gradient_clipping ( float , default=5 ) – Max norm for gradient clipping.

-
weight_decay ( float , default=0.0001 ) – L2 regularization term.

-
margin ( float , default=1 ) – Margin used in triplet loss during alignment.

-
verbose ( bool , default=False ) – Whether to print detailed training logs.

-
random_seed ( int , default=666 ) – Random seed for reproducibility.

-
iter_comb ( list , optional ) – Batch-pair list for MNN comparison.

-
knn_neigh ( int , default=100 ) – K for mutual nearest-neighbor search.

-
Batch_list ( list , optional ) – Per-batch AnnData list aligned to `batch_key `.

-
device ( torch.device , default=auto cuda/cpu ) – Device used for model training.

-
Attributes –

adata: AnnData

Combined data containing all batches

model: STAligner

Neural network model for integration

loader: DataLoader

PyTorch geometric data loader

device: torch.device

Computing device (GPU/CPU)

optimizer: torch.optim.Optimizer

Adam optimizer for training

-
Examples –

```text
>>> import scanpy as sc
>>> import omicverse as ov
>>> # Load data
>>> adata1 = sc.read_visium(...)
>>> adata2 = sc.read_visium(...)
>>> # Construct spatial networks
>>> ov.space.Cal_Spatial_Net(adata1, rad_cutoff=100)
>>> ov.space.Cal_Spatial_Net(adata2, rad_cutoff=100)
>>> # Combine data
>>> adata = adata1.concatenate(adata2)
>>> # Initialize STAligner
>>> staligner = ov.space.pySTAligner(
... adata=adata,
... batch_key='batch',
... Batch_list=[adata1, adata2]
... )
>>> # Train model
>>> staligner.train()
>>> # Get integrated embeddings
>>> embeddings = staligner.predicted()

```

__init__ ( adata , hidden_dims = [512, 30] , n_epochs = 1000 , lr = 0.001 , batch_key = 'batch_name' , key_added = 'STAligner' , gradient_clipping = 5 , weight_decay = 0.0001 , margin = 1 , verbose = False , random_seed = 666 , iter_comb = None , knn_neigh = 100 , Batch_list = None , device = torch.device ) [source] #

Initialize STAligner spatial integration model.

This method sets up the STAligner model by: 1. Processing input data 2. Constructing graph neural networks 3. Initializing optimization parameters 4. Preparing batch alignment strategy

Parameters :

-
adata ( AnnData ) – Combined AnnData with batch labels in `obs[batch_key] `.

-
hidden_dims ( list , default= [ 512 , 30 ] ) – Hidden dimensions of STAligner neural network.

-
n_epochs ( int , default=1000 ) – Number of training epochs.

-
lr ( float , default=0.001 ) – Learning rate for Adam.

-
batch_key ( str , default='batch_name' ) – Batch label column in `adata.obs `.

-
key_added ( str , default='STAligner' ) – Output key for final embedding in `adata.obsm `.

-
gradient_clipping ( float , default=5 ) – Maximum gradient norm.

-
weight_decay ( float , default=0.0001 ) – L2 regularization coefficient.

-
margin ( float , default=1 ) – Triplet-loss margin.

-
verbose ( bool , default=False ) – Print detailed logs when `True `.

-
random_seed ( int , default=666 ) – Random seed.

-
iter_comb ( list , optional ) – Batch combinations for pairwise alignment.

-
knn_neigh ( int , default=100 ) – MNN neighbor count.

-
Batch_list ( list , optional ) – List of per-batch AnnData objects.

-
device ( torch.device , default=auto cuda/cpu ) – Compute device for model.

-
Notes –
-
Requires pre-computed spatial networks

-
GPU acceleration recommended for large datasets

-
Batch_list order must match batch_key order

-
Memory usage scales with dataset size

-
Consider reducing knn_neigh for large datasets

Methods

`__init__ `(adata[, hidden_dims, n_epochs, lr, ...])

Initialize STAligner spatial integration model.

`predicted `()

Generate and store the final embedding from trained STAligner model.

`train `()

Train the STAligner spatial integration model.
