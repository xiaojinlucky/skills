# LoadScopDataset

- Package: scop
- Language: R
- Function: `LoadScopDataset`
- Source: local://scop/0.8.9/LoadScopDataset
- Source mode: installed SCOP runtime documentation
- Fetched at: 2026-07-22T11:04:16+00:00

## Summary

Download a dataset listed in mengxu98/datasets , validate its size and sha256 checksum when the manifest provides them, cache it under tools::R_user_dir("scop", "data") , and return the R object.

## Signature

```text
LoadScopDataset( dataset, collection = "Xenium", cache_dir = NULL, datasets_base_url = "https://raw.githubusercontent.com/mengxu98/datasets/main", update = FALSE, return_path = FALSE, verbose = TRUE )
```

## Parameters

- `dataset`: Dataset id from the collection manifest.
- `collection`: Dataset collection directory, for example "Xenium" .
- `cache_dir`: Directory used to cache downloaded files. If NULL , uses ⁠tools::R_user_dir("scop", "data")/datasets/<collection>⁠ .
- `datasets_base_url`: Base URL or local directory containing SCOP dataset collections.
- `update`: Whether to redownload the file even when a valid cached copy is available.
- `return_path`: Whether to return the cached file path instead of reading the R object.
- `verbose`: Whether to print progress messages.

## Full Documentation

LoadScopDataset R Documentation
## Load a SCOP external dataset

### Description

Download a dataset listed in `mengxu98/datasets `, validate its size and sha256 checksum when the manifest provides them, cache it under `tools::R_user_dir("scop", "data") `, and return the R object.

### Usage

```text
LoadScopDataset(
dataset,
collection = "Xenium",
cache_dir = NULL,
datasets_base_url = "https://raw.githubusercontent.com/mengxu98/datasets/main",
update = FALSE,
return_path = FALSE,
verbose = TRUE
)

```

### Arguments
`dataset `
Dataset id from the collection manifest.
`collection `
Dataset collection directory, for example `"Xenium" `.
`cache_dir `
Directory used to cache downloaded files. If `NULL `, uses `⁠tools::R_user_dir("scop", "data")/datasets/<collection>⁠ `.
`datasets_base_url `
Base URL or local directory containing SCOP dataset collections.
`update `
Whether to redownload the file even when a valid cached copy is available.
`return_path `
Whether to return the cached file path instead of reading the R object.
`verbose `
Whether to print progress messages.

### Value

The loaded R object, or a file path when `return_path = TRUE `.

### Examples

```text
## Not run:
xenium <- LoadScopDataset("xenium_human_pancreas_sub", collection = "Xenium")
SpatialSpotPlot(xenium, group.by = "nCount_Xenium")

## End(Not run)

```
