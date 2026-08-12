# Convert a Seurat object to an .h5ad file

- Package: scop
- Language: R
- Function: `srt_to_h5ad`
- Source: https://mengxu98.github.io/scop/reference/srt_to_h5ad.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/srt_to_h5ad.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Convert a Seurat object to an .h5ad file

## Signature

```text
srt_to_h5ad( srt, path, features = NULL, assay_x = "RNA", layer_x = "counts", assay_y = c("spliced", "unspliced"), layer_y = "counts", reductions = NULL, graphs = NULL, neighbors = NULL, convert_tools = FALSE, convert_misc = FALSE, overwrite = FALSE, verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `path`: Path to the output .h5ad file.
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
- `overwrite`: Whether to overwrite an existing file. Default is FALSE.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Convert a Seurat object to an .h5ad file

## Usage

```text
srt_to_h5ad( srt, path, features = NULL, assay_x = "RNA", layer_x = "counts", assay_y = c("spliced", "unspliced"), layer_y = "counts", reductions = NULL, graphs = NULL, neighbors = NULL, convert_tools = FALSE, convert_misc = FALSE, overwrite = FALSE, verbose = TRUE )
```

## Description

Convert a Seurat object to an .h5ad file

## Value

Invisibly returns the normalized path of the written file.

## Examples

```r
\dontrun{
data(pancreas_sub)
srt_to_h5ad(pancreas_sub, "pancreas_sub.h5ad")
}
```
