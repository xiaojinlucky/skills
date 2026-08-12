# omicverse.single.gene_trends #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.gene_trends`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.gene_trends.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Fit and visualize smooth feature trends along pseudotime.

## Signature

```text
class omicverse.single. gene_trends ( adata , pseudotime , var_names )
```

## Parameters

- `adata`: ( AnnData ) – AnnData containing pseudotime and feature matrix.
- `pseudotime`: ( str ) – adata.obs key used for temporal ordering.
- `var_names`: ( sequence of str ) – Feature names to model along pseudotime.

## Full Documentation

# omicverse.single.gene_trends #

class omicverse.single. gene_trends ( adata , pseudotime , var_names ) [source] #

Fit and visualize smooth feature trends along pseudotime.

Parameters :

-
adata ( AnnData ) – AnnData containing pseudotime and feature matrix.

-
pseudotime ( str ) – `adata.obs `key used for temporal ordering.

-
var_names ( sequence of str ) – Feature names to model along pseudotime.

Returns :

Initializes trend analysis configuration.

Return type :

None

Examples

```text
>>> gt_obj = ov.single.gene_trends(adata_aucs, "pt_via", var_name)

```

__init__ ( adata , pseudotime , var_names ) [source] #

Initialize the gene_trends analysis based on pseudotime

Parameters :

-
adata ( AnnData object )

-
pseudotime ( str , the column name of pseudotime in adata.obs )

-
var_names ( list , the list of gene name to calculate )

Methods

`__init__ `(adata, pseudotime, var_names)

Initialize the gene_trends analysis based on pseudotime

`cal_border_cell `(adata, pseudotime, cluster_key)

Calculate the border cell of each cluster

`calculate `([n_convolve])

Calculate the trends of gene with pseudotime

`get_border_gene `(adata, cluster_key, ...[, ...])

Get the border gene between two clusters

`get_heatmap `()

Get the data of heatmap of trends

`get_kendalltau `()

Get the kendalltau of trends

`get_kernel_gene `(adata, cluster_key, cluster)

Get the kernel gene of cluster

`get_linregress `()

Get the linregress of trends

`get_multi_border_gene `(adata, cluster_key[, ...])

Get the border gene between two clusters for all clusters

`get_multi_kernel_gene `(adata, cluster_key[, ...])

Get the kernel gene of cluster for all clusters

`get_special_border_gene `(adata, cluster_key, ...)

Get the special border gene between two clusters

`get_special_kernel_gene `(adata, cluster_key, ...)

Get the special kernel gene of cluster

`plot_trend `([figsize, max_threshold, color, ...])

Plot the trends of gene with pseudotime
