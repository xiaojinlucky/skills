# List cached databases

- Package: scop
- Language: R
- Function: `ListDB`
- Source: https://mengxu98.github.io/scop/reference/ListDB.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/ListDB.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Retrieves information about databases based on a given species and database name.

## Signature

```text
ListDB(species = c("Homo_sapiens", "Mus_musculus"), db = NULL)
```

## Parameters

- `species`: A character vector of species for which to retrieve database information. Default is c("Homo_sapiens", "Mus_musculus").
- `db`: The pattern to match against the database names. Default is NULL, which matches all databases.

## Full Documentation

# List cached databases

## Usage

```text
ListDB(species = c("Homo_sapiens", "Mus_musculus"), db = NULL)
```

## Description

Retrieves information about databases based on a given species and database name.

## Value

A data frame containing information about the databases, including a Species column and a DB column.

## Examples

```r
ListDB(species = "Homo_sapiens")
ListDB(species = c("Homo_sapiens", "Mus_musculus"))
ListDB(species = "Mus_musculus", db = "GO_BP")
```
