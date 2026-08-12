# Convert homologous gene symbols in expression objects

- Package: scop
- Language: R
- Function: `ConvertHomologs`
- Source: https://mengxu98.github.io/scop/reference/ConvertHomologs.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/ConvertHomologs.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Convert feature names between species with GeneConvert and collapse duplicated target homologs by summing expression values. The Seurat method rebuilds the selected assay from the converted counts matrix and keeps cell metadata and spatial images when present.

## Signature

```text
ConvertHomologs( object, species_from, species_to, geneID_from_IDtype = "symbol", geneID_to_IDtype = "symbol", assay = NULL, layer = "counts", multi_mapping = c("first"), keep_unmapped = FALSE, collapse_fun = c("sum"), Ensembl_version = NULL, biomart = NULL, mirror = NULL, max_tries = 5, verbose = TRUE ) ConvertHomologs{Seurat}( object, species_from, species_to, geneID_from_IDtype = "symbol", geneID_to_IDtype = "symbol", assay = NULL, layer = "counts", multi_mapping = c("first"), keep_unmapped = FALSE, collapse_fun = c("sum"), Ensembl_version = NULL, biomart = NULL, mirror = NULL, max_tries = 5, verbose = TRUE ) ConvertHomologs{matrix}( object, species_from, species_to, geneID_from_IDtype = "symbol", geneID_to_IDtype = "symbol", assay = NULL, layer = "counts", multi_mapping = c("first"), keep_unmapped = FALSE, collapse_fun = c("sum"), Ensembl_version = NULL, biomart = NULL, mirror = NULL, max_tries = 5, verbose = TRUE ) ConvertHomologs{Matrix}( object, species_from, species_to, geneID_from_IDtype = "symbol", geneID_to_IDtype = "symbol", assay = NULL, layer = "counts", multi_mapping = c("first"), keep_unmapped = FALSE, collapse_fun = c("sum"), Ensembl_version = NULL, biomart = NULL, mirror = NULL, max_tries = 5, verbose = TRUE ) ConvertHomologs{default}( object, species_from, species_to, geneID_from_IDtype = "symbol", geneID_to_IDtype = "symbol", assay = NULL, layer = "counts", multi_mapping = c("first"), keep_unmapped = FALSE, collapse_fun = c("sum"), Ensembl_version = NULL, biomart = NULL, mirror = NULL, max_tries = 5, verbose = TRUE )
```

## Parameters

- `object`: A Seurat object or a gene-by-cell matrix.
- `species_from`: Latin names for animals of the input geneID. e.g. "Homo_sapiens", "Mus_musculus".
- `species_to`: Latin names for animals of the output geneID. e.g. "Homo_sapiens", "Mus_musculus".
- `geneID_from_IDtype`: Gene ID type of the input geneID. e.g. "symbol", "ensembl_id", "entrez_id"
- `geneID_to_IDtype`: Gene ID type(s) to convert to. e.g. "symbol", "ensembl_id", "entrez_id".
- `assay`: Assay to convert when object is a Seurat object. If NULL, the default assay is used.
- `layer`: Assay layer used for conversion. Default "counts".
- `multi_mapping`: How to handle source genes mapped to multiple target homologs. "first" keeps the first target homolog for each source gene.
- `keep_unmapped`: Whether to keep unmapped source genes with their original names.
- `collapse_fun`: Function used to collapse duplicated target homologs. Currently only "sum" is supported.
- `Ensembl_version`: An integer specifying the Ensembl version. Default is NULL. If NULL, the latest version will be used.
- `biomart`: The name of the BioMart database that you want to connect to. Possible options include "ensembl", "protists_mart", "fungi_mart", and "plants_mart".
- `mirror`: Specify an Ensembl mirror to connect to. The valid options here are "www", "uswest", "useast", "asia".
- `max_tries`: The maximum number of attempts to connect with the BioMart service.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Convert homologous gene symbols in expression objects

## Usage

```text
ConvertHomologs( object, species_from, species_to, geneID_from_IDtype = "symbol", geneID_to_IDtype = "symbol", assay = NULL, layer = "counts", multi_mapping = c("first"), keep_unmapped = FALSE, collapse_fun = c("sum"), Ensembl_version = NULL, biomart = NULL, mirror = NULL, max_tries = 5, verbose = TRUE ) ConvertHomologs{Seurat}( object, species_from, species_to, geneID_from_IDtype = "symbol", geneID_to_IDtype = "symbol", assay = NULL, layer = "counts", multi_mapping = c("first"), keep_unmapped = FALSE, collapse_fun = c("sum"), Ensembl_version = NULL, biomart = NULL, mirror = NULL, max_tries = 5, verbose = TRUE ) ConvertHomologs{matrix}( object, species_from, species_to, geneID_from_IDtype = "symbol", geneID_to_IDtype = "symbol", assay = NULL, layer = "counts", multi_mapping = c("first"), keep_unmapped = FALSE, collapse_fun = c("sum"), Ensembl_version = NULL, biomart = NULL, mirror = NULL, max_tries = 5, verbose = TRUE ) ConvertHomologs{Matrix}( object, species_from, species_to, geneID_from_IDtype = "symbol", geneID_to_IDtype = "symbol", assay = NULL, layer = "counts", multi_mapping = c("first"), keep_unmapped = FALSE, collapse_fun = c("sum"), Ensembl_version = NULL, biomart = NULL, mirror = NULL, max_tries = 5, verbose = TRUE ) ConvertHomologs{default}( object, species_from, species_to, geneID_from_IDtype = "symbol", geneID_to_IDtype = "symbol", assay = NULL, layer = "counts", multi_mapping = c("first"), keep_unmapped = FALSE, collapse_fun = c("sum"), Ensembl_version = NULL, biomart = NULL, mirror = NULL, max_tries = 5, verbose = TRUE )
```

## Description

Convert feature names between species with GeneConvert and collapse duplicated target homologs by summing expression values. The Seurat method rebuilds the selected assay from the converted counts matrix and keeps cell metadata and spatial images when present.

## Value

A converted object of the same high-level type as object. The mapping table is stored in @tools$ConvertHomologs for Seurat objects and in the "ConvertHomologs" attribute for matrix inputs.

## Examples

```r
data(pancreas_sub)
pancreas_human <- ConvertHomologs(
  pancreas_sub,
  species_from = "Mus_musculus",
  species_to = "Homo_sapiens"
)
rownames(pancreas_human)[1:5]
```
