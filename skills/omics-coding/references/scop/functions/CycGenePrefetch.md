# Prefetch cell cycle genes

- Package: scop
- Language: R
- Function: `CycGenePrefetch`
- Source: https://mengxu98.github.io/scop/reference/CycGenePrefetch.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/CycGenePrefetch.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Based on the human cell cycle genes, the cell cycle genes of the corresponding species were captured by homologous gene conversion.

## Signature

```text
CycGenePrefetch( species = "Homo_sapiens", Ensembl_version = NULL, mirror = NULL, max_tries = 5, use_cached_gene = TRUE, verbose = TRUE )
```

## Parameters

- `species`: Latin names for animals, i.e., "Homo_sapiens", "Mus_musculus"
- `Ensembl_version`: An integer specifying the Ensembl version. Default is NULL. If NULL, the latest version will be used.
- `mirror`: Specify an Ensembl mirror to connect to. The valid options here are "www", "uswest", "useast", "asia".
- `max_tries`: The maximum number of attempts to connect with the BioMart service.
- `use_cached_gene`: Whether to use previously cached cell cycle gene conversion results for the species. Default is TRUE.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Prefetch cell cycle genes

## Usage

```text
CycGenePrefetch( species = "Homo_sapiens", Ensembl_version = NULL, mirror = NULL, max_tries = 5, use_cached_gene = TRUE, verbose = TRUE )
```

## Description

Based on the human cell cycle genes, the cell cycle genes of the corresponding species were captured by homologous gene conversion.

## Value

A list of S-phase and G2M-phase genes.

## Examples

```r
ccgenes <- CycGenePrefetch("Homo_sapiens")
str(ccgenes)

ccgenes <- CycGenePrefetch("Mus_musculus")
str(ccgenes)
```
