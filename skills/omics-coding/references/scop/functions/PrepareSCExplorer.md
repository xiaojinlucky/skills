# Prepare Seurat objects for the SCExplorer

- Package: scop
- Language: R
- Function: `PrepareSCExplorer`
- Source: https://mengxu98.github.io/scop/reference/PrepareSCExplorer.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/PrepareSCExplorer.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

This function prepares one or multiple Seurat objects for the SCExplorer app. It takes a Seurat object or a list of Seurat objects as input and outputs two hdf5 files: one for the data and one for the metadata.

## Signature

```text
PrepareSCExplorer( object, base_dir = "SCExplorer", data_file = "data.hdf5", meta_file = "meta.hdf5", assays = "RNA", layers = c("counts", "data"), ignore_nlevel = 100, write_tools = FALSE, write_misc = FALSE, compression_level = 6, overwrite = FALSE, verbose = TRUE )
```

## Parameters

- `object`: A Seurat object or a list of Seurat objects.
- `base_dir`: The base directory where the SCExplorer hdf5 files will be written. Default is "SCExplorer".
- `data_file`: Path to the output data file. If not provided, the file will be named "data.hdf5" in the current directory.
- `meta_file`: Path to the output meta file. If not provided, the file will be named "meta.hdf5" in the current directory.
- `assays`: The assays to include in the data file. Default is "RNA".
- `layers`: The layers to include in the data file. Default is "data".
- `ignore_nlevel`: The number of levels above which a metadata field will be ignored. Default is 100.
- `write_tools`: Whether to write the tools information to the meta file. Default is FALSE.
- `write_misc`: Whether to write the miscellaneous information to the meta file. Default is FALSE.
- `compression_level`: Compression level for the HDF5 dataset. Default is 6.
- `overwrite`: Whether to overwrite existing data in the data file. Default is TRUE.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Prepare Seurat objects for the SCExplorer

## Usage

```text
PrepareSCExplorer( object, base_dir = "SCExplorer", data_file = "data.hdf5", meta_file = "meta.hdf5", assays = "RNA", layers = c("counts", "data"), ignore_nlevel = 100, write_tools = FALSE, write_misc = FALSE, compression_level = 6, overwrite = FALSE, verbose = TRUE )
```

## Description

This function prepares one or multiple Seurat objects for the SCExplorer app. It takes a Seurat object or a list of Seurat objects as input and outputs two hdf5 files: one for the data and one for the metadata.

## Examples

```r
\dontrun{
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
PrepareSCExplorer(pancreas_sub, base_dir = "./SCExplorer")
}
```
