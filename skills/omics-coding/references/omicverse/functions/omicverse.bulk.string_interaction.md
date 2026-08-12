# omicverse.bulk.string_interaction #

- Package: omicverse
- Language: Python
- Function: `omicverse.bulk.string_interaction`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.bulk.string_interaction.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Analyze protein-protein interaction network using STRING database.

## Signature

```text
omicverse.bulk. string_interaction ( gene , species )
```

## Parameters

- `gene`: ( list ) – List of gene names for PPI analysis.
- `species`: ( int ) – NCBI taxon identifiers (e.g. Human is 9606, see STRING organisms).

## Full Documentation

# omicverse.bulk.string_interaction #

omicverse.bulk. string_interaction ( gene , species ) [source] #

Analyze protein-protein interaction network using STRING database.

Parameters :

-
gene ( `list `) – List of gene names for PPI analysis.

-
species ( `int `) – NCBI taxon identifiers (e.g. Human is 9606, see STRING organisms).

Returns :

DataFrame containing protein-protein interaction data with columns stringId_A, stringId_B, preferredName_A, preferredName_B, ncbiTaxonId, score, nscore, fscore, pscore, ascore, escore, dscore, tscore.

Return type :

res
