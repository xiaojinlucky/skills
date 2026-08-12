# Fetch data from the hdf5 file and returns a Seurat object

- Package: scop
- Language: R
- Function: `FetchH5`
- Source: https://mengxu98.github.io/scop/reference/FetchH5.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/FetchH5.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Fetch data from the hdf5 file and returns a Seurat object

## Signature

```text
FetchH5( data_file, meta_file, name = NULL, features = NULL, layer = NULL, assay = NULL, metanames = NULL, reduction = NULL, verbose = TRUE )
```

## Parameters

- `data_file`: The path to the hdf5 file containing the data.
- `meta_file`: The path to the hdf5 file containing the metadata.
- `name`: The name of the dataset in the hdf5 file. If not specified, the function will attempt to find the shared group name in both files.
- `features`: The names of the genes or features to fetch. If specified, only these features will be fetched.
- `layer`: The layer for the counts in the hdf5 file. If not specified, the first layer will be used.
- `assay`: The name of the assay to use. If not specified, the default assay in the hdf5 file will be used.
- `metanames`: The names of the metadata columns to fetch.
- `reduction`: The name of the reduction to fetch.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Fetch data from the hdf5 file and returns a Seurat object

## Usage

```text
FetchH5( data_file, meta_file, name = NULL, features = NULL, layer = NULL, assay = NULL, metanames = NULL, reduction = NULL, verbose = TRUE )
```

## Description

Fetch data from the hdf5 file and returns a Seurat object

## Value

A Seurat object with the fetched data.

## Examples

```r
\dontrun{
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
PrepareSCExplorer(pancreas_sub, base_dir = "./SCExplorer")
srt <- FetchH5(
  data_file = "./SCExplorer/data.hdf5",
  meta_file = "./SCExplorer/meta.hdf5",
  features = c("Ins1", "Ghrl"),
  metanames = c("SubCellType", "Phase"),
  reduction = "UMAP"
)
}
```
