# List SCOP external datasets

- Package: scop
- Language: R
- Function: `ListExternalDatasets`
- Source: https://mengxu98.github.io/scop/reference/ListExternalDatasets.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/ListExternalDatasets.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Read a dataset manifest from the external mengxu98/datasets repository or a local mirror. This keeps example data assets out of the SCOP package while still making them discoverable and reproducible.

## Signature

```text
ListExternalDatasets( collection = "Xenium", datasets_base_url = "https://raw.githubusercontent.com/mengxu98/datasets/main" )
```

## Parameters

- `collection`: Dataset collection directory, for example "Xenium".
- `datasets_base_url`: Base URL or local directory containing SCOP dataset collections.

## Full Documentation

# List SCOP external datasets

## Usage

```text
ListExternalDatasets( collection = "Xenium", datasets_base_url = "https://raw.githubusercontent.com/mengxu98/datasets/main" )
```

## Description

Read a dataset manifest from the external mengxu98/datasets repository or a local mirror. This keeps example data assets out of the SCOP package while still making them discoverable and reproducible.

## Value

A data frame parsed from manifest.tsv.

## Examples

```r
\dontrun{
ListExternalDatasets("Xenium")
}
```
