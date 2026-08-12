# omicverse.bulk2single.Bulk2Single #

- Package: omicverse
- Language: Python
- Function: `omicverse.bulk2single.Bulk2Single`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.bulk2single.Bulk2Single.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

VAE-based bulk-to-single framework for reconstructing pseudo single cells from bulk RNA-seq.

## Signature

```text
class omicverse.bulk2single. Bulk2Single ( bulk_data , single_data , celltype_key , bulk_group = None , max_single_cells = 5000 , top_marker_num = 500 , ratio_num = 1 , gpu = 0 )
```

## Parameters

- `bulk_data`: ( pd.DataFrame ) – Bulk expression matrix with genes in rows and samples in columns.
- `single_data`: ( anndata.AnnData ) – Reference single-cell dataset used to learn cell-type expression patterns.
- `celltype_key`: ( str ) – Column in single_data.obs containing cell-type labels.
- `bulk_group`: ( Optional [ Any ] ) – Optional sample grouping information for averaging bulk replicates.
- `max_single_cells`: ( int ) – Maximum number of reference cells retained for model fitting.
- `top_marker_num`: ( int ) – Number of marker genes per cell type used by downstream preparation.
- `ratio_num`: ( int ) – Multiplier controlling total generated cell counts.
- `gpu`: ( Union [ int , str ] ) – Device selector for training (CUDA index, 'mps' , or CPU fallback).

## Full Documentation

# omicverse.bulk2single.Bulk2Single #

class omicverse.bulk2single. Bulk2Single ( bulk_data , single_data , celltype_key , bulk_group = None , max_single_cells = 5000 , top_marker_num = 500 , ratio_num = 1 , gpu = 0 ) [source] #

VAE-based bulk-to-single framework for reconstructing pseudo single cells from bulk RNA-seq.

Parameters :

-
bulk_data ( pd.DataFrame ) – Bulk expression matrix with genes in rows and samples in columns.

-
single_data ( anndata.AnnData ) – Reference single-cell dataset used to learn cell-type expression patterns.

-
celltype_key ( str ) – Column in `single_data.obs `containing cell-type labels.

-
bulk_group ( Optional [ Any ] ) – Optional sample grouping information for averaging bulk replicates.

-
max_single_cells ( int ) – Maximum number of reference cells retained for model fitting.

-
top_marker_num ( int ) – Number of marker genes per cell type used by downstream preparation.

-
ratio_num ( int ) – Multiplier controlling total generated cell counts.

-
gpu ( Union [ int , str ] ) – Device selector for training (CUDA index, `'mps' `, or CPU fallback).

Returns :

Initializes bulk2single deconvolution and simulation workflow.

Return type :

None

Examples

```text
>>> model = ov.bulk2single.Bulk2Single(bulk_data=bulk_data, single_data=single_data, celltype_key="Cell_type")

```

__init__ ( bulk_data , single_data , celltype_key , bulk_group = None , max_single_cells = 5000 , top_marker_num = 500 , ratio_num = 1 , gpu = 0 ) [source] #

Initialize the Bulk2Single class for bulk-to-single-cell deconvolution.

Parameters :

-
bulk_data ( pd.DataFrame ) – Bulk RNA-seq expression matrix. Rows are genes and columns are samples.

-
single_data ( anndata.AnnData ) – Single-cell reference with compatible gene symbols and cell metadata.

-
celltype_key ( str ) – Name of the column in `single_data.obs `that stores cell-type labels.

-
bulk_group ( Optional [ Any ] ) – Optional grouping key/list used to aggregate replicate bulk samples.

-
max_single_cells ( int ) – Maximum number of reference cells used during initialization.

-
top_marker_num ( int ) – Intended number of marker genes per cell type for preprocessing steps.

-
ratio_num ( int ) – Generation ratio used when estimating target cell counts.

-
gpu ( Union [ int , str ] ) – Compute device specification; supports CUDA indices and `'mps' `.

Methods

`__init__ `(bulk_data, single_data, celltype_key)

Initialize the Bulk2Single class for bulk-to-single-cell deconvolution.

`bulk_preprocess_lazy `()

Preprocess bulk RNA-seq data for deconvolution.

`filtered `(generate_adata[, ...])

Filter generated single-cell data by removing low-quality clusters.

`generate `()

Generate synthetic single-cell data from trained VAE model.

`load `(vae_load_dir[, hidden_size])

Load a pre-trained VAE model.

`load_and_generate `(vae_load_dir[, hidden_size])

Load pre-trained VAE model and generate single-cell data.

`load_fraction `(fraction_path)

Load predicted cell-type target numbers from file.

`plot_loss `([figsize])

Plot training loss curve of the VAE model.

`predicted_fraction `([method, sep, scaler, ...])

Predict cell-type fractions from bulk RNA-seq data using deconvolution.

`prepare_input `()

Prepare input data for VAE training.

`save `([vae_save_dir, vae_save_name])

Save the trained VAE model and cell target numbers.

`single_preprocess_lazy `([target_sum])

Preprocess single-cell reference data.

`train `([vae_save_dir, vae_save_name, ...])

Train the VAE model for single-cell data generation.
