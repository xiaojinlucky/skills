# Convert a Seurat object to an AnnData object

- Package: scop
- Language: R
- Function: `srt_to_adata`
- Source: https://mengxu98.github.io/scop/reference/srt_to_adata.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/srt_to_adata.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Convert a Seurat object to an AnnData object

## Signature

```text
srt_to_adata( srt, features = NULL, assay_x = "RNA", layer_x = "counts", assay_y = c("spliced", "unspliced"), layer_y = "counts", reductions = NULL, graphs = NULL, neighbors = NULL, convert_tools = FALSE, convert_misc = FALSE, verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `features`: Optional vector of features to include in the anndata object. Default is all features in assay_x.
- `assay_x`: Assay to convert as the main data matrix in the anndata object. Default is "RNA".
- `layer_x`: Layer name for assay_x in the Seurat object. Default is "counts".
- `assay_y`: Assays to convert as layers in the anndata object. Default is c("spliced", "unspliced").
- `layer_y`: Layer names for the assay_y in the Seurat object. Default is "counts".
- `reductions`: Character vector specifying which Seurat reductions to convert into obsm. Default is NULL, which converts all available reductions.
- `graphs`: Character vector specifying which Seurat graphs to convert into obsp. Default is NULL, which converts all available graphs.
- `neighbors`: Character vector specifying which Seurat neighbor objects to convert into obsp. Default is NULL, which converts all available neighbor objects.
- `convert_tools`: Whether to convert the tool-specific data. Default is FALSE.
- `convert_misc`: Whether to convert the miscellaneous data. Default is FALSE.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Convert a Seurat object to an AnnData object

## Usage

```text
srt_to_adata( srt, features = NULL, assay_x = "RNA", layer_x = "counts", assay_y = c("spliced", "unspliced"), layer_y = "counts", reductions = NULL, graphs = NULL, neighbors = NULL, convert_tools = FALSE, convert_misc = FALSE, verbose = TRUE )
```

## Description

Convert a Seurat object to an AnnData object

## Value

A anndata object.

## Examples

```r
\dontrun{
data(pancreas_sub)
adata <- srt_to_adata(pancreas_sub)
adata

# Or save as a h5ad/loom file
adata$write_h5ad(
  "pancreas_sub.h5ad"
)
adata$write_loom(
  "pancreas_sub.loom",
  write_obsm_varm = TRUE
)
}
```
