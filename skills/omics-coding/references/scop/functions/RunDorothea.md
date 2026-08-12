# Run DoRothEA transcription factor activity inference

- Package: scop
- Language: R
- Function: `RunDorothea`
- Source: https://mengxu98.github.io/scop/reference/RunDorothea.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunDorothea.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run DoRothEA transcription factor activity inference

## Signature

```text
RunDorothea( srt, assay = NULL, layer = "data", species = c("Homo_sapiens", "Mus_musculus"), input_species = NULL, geneID_from_IDtype = "symbol", geneID_to_IDtype = "symbol", homolog_params = list(), confidence = c("A", "B", "C"), regulons = NULL, method = c("ulm", "viper", "wmean"), minsize = 5, options = list(), assay_name = "dorothea", new_assay = TRUE, add_meta = TRUE, verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `layer`: Assay layer used as the expression matrix.
- `species`: Species used to select bundled DoRothEA regulons. DoRothEA only provides human and mouse regulons. For other input species, set input_species and project expression values to this regulon species through homologous gene conversion before activity inference.
- `input_species`: Species of the input expression features. If NULL, the input is assumed to use the same gene namespace as species. When this differs from species, expression features are converted with ConvertHomologs before DoRothEA activity inference.
- `geneID_from_IDtype, geneID_to_IDtype`: Gene identifier types passed to ConvertHomologs for cross-species projection. For bundled DoRothEA regulons, geneID_to_IDtype should normally remain "symbol".
- `homolog_params`: Additional named arguments passed to ConvertHomologs when input_species differs from species, such as Ensembl_version, biomart, mirror, max_tries, multi_mapping, and collapse_fun.
- `confidence`: DoRothEA confidence levels to keep.
- `regulons`: Optional regulon table with tf, target, mor, and confidence columns. If NULL, bundled dorothea_hs or dorothea_mm data are loaded from the dorothea package.
- `method`: Activity inference backend from decoupleR.
- `minsize`: Minimum regulon size passed to decoupleR.
- `options`: Additional named options passed to the selected decoupleR function.
- `assay_name`: Name of the assay used to store TF activity scores.
- `new_assay`: Whether to store TF activity scores as a new assay.
- `add_meta`: Whether to also write TF activity scores to srt@meta.data with the assay_name prefix for direct plotting with {[=FeatureDimPlot]{FeatureDimPlot()}}.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Run DoRothEA transcription factor activity inference

## Usage

```text
RunDorothea( srt, assay = NULL, layer = "data", species = c("Homo_sapiens", "Mus_musculus"), input_species = NULL, geneID_from_IDtype = "symbol", geneID_to_IDtype = "symbol", homolog_params = list(), confidence = c("A", "B", "C"), regulons = NULL, method = c("ulm", "viper", "wmean"), minsize = 5, options = list(), assay_name = "dorothea", new_assay = TRUE, add_meta = TRUE, verbose = TRUE )
```

## Description

Run DoRothEA transcription factor activity inference

## Value

A Seurat object with DoRothEA results stored in srt@tools[["Dorothea"]], optionally TF activity scores stored in srt@meta.data, and optionally a TF activity assay when new_assay = TRUE. For cross-species runs, the homolog projection summary is stored in srt@tools[["Dorothea"]]$homolog_conversion.

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(
  pancreas_sub,
  verbose = FALSE
)

pancreas_sub <- RunDorothea(
  pancreas_sub,
  layer = "counts",
  species = "Mus_musculus",
  confidence = c("A", "B", "C"),
  method = "ulm",
  minsize = 5,
  new_assay = FALSE
)

pancreas_sub@tools$Dorothea$regulon_summary
head(pancreas_sub@tools$Dorothea$result)

activity_cols <- head(
  grep("^dorothea_", colnames(pancreas_sub@meta.data), value = TRUE),
  2
)
head(pancreas_sub@meta.data[, activity_cols, drop = FALSE])

FeatureDimPlot(
  pancreas_sub,
  features = activity_cols,
  reduction = "StandardUMAP2D",
  ncol = 2
)
```
