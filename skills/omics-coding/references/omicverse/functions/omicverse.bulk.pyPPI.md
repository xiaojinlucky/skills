# omicverse.bulk.pyPPI #

- Package: omicverse
- Language: Python
- Function: `omicverse.bulk.pyPPI`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.bulk.pyPPI.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Protein-protein interaction (PPI) analysis wrapper based on STRING.

## Signature

```text
class omicverse.bulk. pyPPI ( gene , species , gene_type_dict , gene_color_dict , score = 0.4 )
```

## Parameters

- `gene`: ( list ) – Gene symbols used as seed nodes for building the interaction network.
- `species`: ( int ) – NCBI taxonomy id (e.g., 9606 for human).
- `gene_type_dict`: ( dict ) – Mapping from gene symbol to category/type used in node styling.
- `gene_color_dict`: ( dict ) – Mapping from gene symbol to display color.
- `score`: ( float , default=0.4 ) – Minimum confidence score for retaining interactions.

## Full Documentation

# omicverse.bulk.pyPPI #

class omicverse.bulk. pyPPI ( gene , species , gene_type_dict , gene_color_dict , score = 0.4 ) [source] #

Protein-protein interaction (PPI) analysis wrapper based on STRING.

Parameters :

-
gene ( list ) – Gene symbols used as seed nodes for building the interaction network.

-
species ( int ) – NCBI taxonomy id (e.g., 9606 for human).

-
gene_type_dict ( dict ) – Mapping from gene symbol to category/type used in node styling.

-
gene_color_dict ( dict ) – Mapping from gene symbol to display color.

-
score ( float , default=0.4 ) – Minimum confidence score for retaining interactions.

__init__ ( gene , species , gene_type_dict , gene_color_dict , score = 0.4 ) [source] #

Initialize protein-protein interaction analysis.

Parameters :

-
gene ( `list `) – List of gene names for PPI analysis

-
species ( `int `) – NCBI taxon identifiers (e.g. Human is 9606, see STRING organisms)

-
gene_type_dict ( `dict `) – Dictionary mapping gene names to gene types

-
gene_color_dict ( `dict `) – Dictionary mapping gene names to colors for visualization

-
score ( `float `(default: `0.4 `)) – Threshold for protein interaction confidence (default: 0.4)

Methods

`__init__ `(gene, species, gene_type_dict, ...)

Initialize protein-protein interaction analysis.

`interaction_analysis `()

Perform protein-protein interaction analysis.

`plot_network `(**kwargs)

Plot protein-protein interaction network.
