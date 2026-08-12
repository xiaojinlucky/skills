# Run scFEA flux estimation for a Seurat object

- Package: scop
- Language: R
- Function: `RunscFEA`
- Source: https://mengxu98.github.io/scop/reference/RunscFEA.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunscFEA.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run scFEA flux estimation for a Seurat object

## Signature

```text
RunscFEA( srt, assay = NULL, layer = "data", species = c("human", "mouse"), n_epoch = 100, sc_imputation = FALSE, assay_flux = "scFEAflux", assay_balance = "scFEAbalance", store_metadata = FALSE, data_dir = NULL, seed = 16, max_cells = NULL, verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: Assay to use as expression matrix. Default is `DefaultAssay(srt)`.
- `layer`: Assay layer to use. Default is `"data"`.
- `species`: One of `"human"` or `"mouse"`, selecting the M168 scFEA files.
- `n_epoch`: Number of scFEA training epochs.
- `sc_imputation`: Whether to run MAGIC imputation inside the scFEA backend.
- `assay_flux`: Name of the assay storing module flux scores.
- `assay_balance`: Name of the assay storing metabolite balance scores.
- `store_metadata`: Whether to also append flux and balance values to `srt@meta.data`.
- `data_dir`: Optional directory containing scFEA M168 CSV resources. If `NULL`, files are downloaded from `mengxu98/datasets` and cached with `tools::R_user_dir("scop", "data")`.
- `seed`: Random seed passed to R and the Python scFEA backend.
- `max_cells`: Maximum number of cells used for GNN training. When the input has more cells, a random subset is sampled for training and the trained model predicts fluxes for all cells in batches. This drastically reduces peak memory for large datasets. Set `NULL` (default) to train on all cells, matching the original upstream behaviour. A value such as `20000` can be useful on machines with 16-32 GiB RAM.
- `verbose`: Whether to print progress messages.

## Full Documentation

# Run scFEA flux estimation for a Seurat object

## Usage

```text
RunscFEA( srt, assay = NULL, layer = "data", species = c("human", "mouse"), n_epoch = 100, sc_imputation = FALSE, assay_flux = "scFEAflux", assay_balance = "scFEAbalance", store_metadata = FALSE, data_dir = NULL, seed = 16, max_cells = NULL, verbose = TRUE )
```

## Description

Run scFEA flux estimation for a Seurat object

## Value

A Seurat object with `assay_flux`, `assay_balance`, and `srt@tools[["scFEA"]]`.
