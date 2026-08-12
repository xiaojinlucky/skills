# omicverse.bulk2single.BulkTrajBlend #

- Package: omicverse
- Language: Python
- Function: `omicverse.bulk2single.BulkTrajBlend`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.bulk2single.BulkTrajBlend.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Integrate bulk and single-cell information to infer transitional cell-state trajectories.

## Signature

```text
class omicverse.bulk2single. BulkTrajBlend ( bulk_seq , single_seq , celltype_key , bulk_group = None , max_single_cells = 5000 , top_marker_num = 500 , ratio_num = 1 , gpu = 0 )
```

## Parameters

- `bulk_seq`: ( pd.DataFrame ) – Bulk expression matrix with genes in rows and samples in columns.
- `single_seq`: ( anndata.AnnData ) – Reference single-cell dataset used to define cell identities.
- `celltype_key`: ( str ) – Column name in single_seq.obs containing cell-type labels.
- `bulk_group`: ( Optional [ Any ] ) – Optional grouping key/list for averaging bulk replicates.
- `max_single_cells`: ( int ) – Maximum number of reference cells retained for model fitting.
- `top_marker_num`: ( int ) – Number of top marker genes used in Bulk2Single preparation.
- `ratio_num`: ( int ) – Ratio controlling generated cell numbers per cell type.
- `gpu`: ( Union [ int , str ] ) – Compute device specification (CUDA index, 'mps' , or CPU fallback).

## Full Documentation

# omicverse.bulk2single.BulkTrajBlend #

class omicverse.bulk2single. BulkTrajBlend ( bulk_seq , single_seq , celltype_key , bulk_group = None , max_single_cells = 5000 , top_marker_num = 500 , ratio_num = 1 , gpu = 0 ) [source] #

Integrate bulk and single-cell information to infer transitional cell-state trajectories.

Parameters :

-
bulk_seq ( pd.DataFrame ) – Bulk expression matrix with genes in rows and samples in columns.

-
single_seq ( anndata.AnnData ) – Reference single-cell dataset used to define cell identities.

-
celltype_key ( str ) – Column name in `single_seq.obs `containing cell-type labels.

-
bulk_group ( Optional [ Any ] ) – Optional grouping key/list for averaging bulk replicates.

-
max_single_cells ( int ) – Maximum number of reference cells retained for model fitting.

-
top_marker_num ( int ) – Number of top marker genes used in Bulk2Single preparation.

-
ratio_num ( int ) – Ratio controlling generated cell numbers per cell type.

-
gpu ( Union [ int , str ] ) – Compute device specification (CUDA index, `'mps' `, or CPU fallback).

Returns :

Initializes bulk-trajectory blending workflow.

Return type :

None

Examples

```text
>>> bulktb = ov.bulk2single.BulkTrajBlend(bulk_seq=bulk, single_seq=adata, celltype_key="celltype")

```

__init__ ( bulk_seq , single_seq , celltype_key , bulk_group = None , max_single_cells = 5000 , top_marker_num = 500 , ratio_num = 1 , gpu = 0 ) [source] #

Initialize BulkTrajBlend for trajectory inference and cell blending.

Parameters :

-
bulk_seq ( pd.DataFrame ) – Bulk RNA-seq matrix with genes as rows and samples as columns.

-
single_seq ( anndata.AnnData ) – Single-cell reference AnnData used for cell-state prior information.

-
celltype_key ( str ) – Column in `single_seq.obs `that stores cell-type annotation.

-
bulk_group ( Optional [ Any ] ) – Optional grouping used to aggregate bulk replicates.

-
max_single_cells ( int ) – Maximum number of single cells used in internal Bulk2Single model.

-
top_marker_num ( int ) – Number of marker genes per cell type used during preparation.

-
ratio_num ( int ) – Cell-number ratio used when converting fractions into target counts.

-
gpu ( Union [ int , str ] ) – Compute device selector for VAE/GNN workflows.

Returns :

None

Methods

`__init__ `(bulk_seq, single_seq, celltype_key)

Initialize BulkTrajBlend for trajectory inference and cell blending.

`bulk_preprocess_lazy `()

Preprocess bulk RNA-seq data for trajectory analysis.

`gnn_configure `([use_rep, neighbor_rep, gpu, ...])

Configure Graph Neural Network for trajectory and transition state analysis.

`gnn_generate `()

Generate overlapping cell communities representing transition states.

`gnn_load `(gnn_load_dir[, thresh])

Load a pre-trained GNN model for trajectory analysis.

`gnn_train `([thresh, gnn_save_dir, gnn_save_name])

Train the GNN model for trajectory and transition state inference.

`interpolation `(celltype[, adata])

Interpolate trajectory communities back to original data space.

`single_preprocess_lazy `([target_sum])

Preprocess single-cell reference data for trajectory analysis.

`vae_configure `([cell_target_num])

Configure the VAE model for bulk-to-single-cell generation.

`vae_generate `([highly_variable_genes, ...])

Generate trajectory-aware single-cell data with quality filtering.

`vae_load `(vae_load_dir[, hidden_size])

Load a pre-trained VAE model for trajectory analysis.

`vae_train `([vae_save_dir, vae_save_name, ...])

Train the VAE model for trajectory-aware single-cell generation.
