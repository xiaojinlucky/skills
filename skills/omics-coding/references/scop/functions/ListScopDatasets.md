# ListScopDatasets

- Package: scop
- Language: R
- Function: `ListScopDatasets`
- Source: local://scop/0.8.9/ListScopDatasets
- Source mode: installed SCOP runtime documentation
- Fetched at: 2026-07-22T11:04:16+00:00

## Summary

Read a dataset manifest from the external mengxu98/datasets repository or a local mirror. This keeps example data assets out of the SCOP package while still making them discoverable and reproducible.

## Signature

```text
ListScopDatasets( collection = "Xenium", datasets_base_url = "https://raw.githubusercontent.com/mengxu98/datasets/main" )
```

## Parameters

- `collection`: Dataset collection directory, for example "Xenium" .
- `datasets_base_url`: Base URL or local directory containing SCOP dataset collections.

## Full Documentation

ListScopDatasets R Documentation
## List SCOP external datasets

### Description

Read a dataset manifest from the external `mengxu98/datasets `repository or a local mirror. This keeps example data assets out of the SCOP package while still making them discoverable and reproducible.

### Usage

```text
ListScopDatasets(
collection = "Xenium",
datasets_base_url = "https://raw.githubusercontent.com/mengxu98/datasets/main"
)

```

### Arguments
`collection `
Dataset collection directory, for example `"Xenium" `.
`datasets_base_url `
Base URL or local directory containing SCOP dataset collections.

### Value

A data frame parsed from `manifest.tsv `.

### Examples

```text
## Not run:
ListScopDatasets("Xenium")

## End(Not run)

```
