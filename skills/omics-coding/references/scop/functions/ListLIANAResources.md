# List LIANA ligand-receptor resources

- Package: scop
- Language: R
- Function: `ListLIANAResources`
- Source: https://mengxu98.github.io/scop/reference/ListLIANAResources.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/ListLIANAResources.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Lists the resources exposed by the installed LIANA backend. `Consensus` and `MouseConsensus` are curated ligand-receptor resources; they are distinct from LIANA's multi-method rank aggregation.

## Signature

```text
ListLIANAResources(species = NULL)
```

## Parameters

- `species`: Optional species filter.

## Full Documentation

# List LIANA ligand-receptor resources

## Usage

```text
ListLIANAResources(species = NULL)
```

## Description

Lists the resources exposed by the installed LIANA backend. `Consensus` and `MouseConsensus` are curated ligand-receptor resources; they are distinct from LIANA's multi-method rank aggregation.

## Value

A data frame describing the resources available from LIANA.
