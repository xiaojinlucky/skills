# omicverse.pl.rank_genes_groups_dotplot #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.rank_genes_groups_dotplot`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.rank_genes_groups_dotplot.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Create a dot plot from rank_genes_groups results.

## Signature

```text
omicverse.pl. rank_genes_groups_dotplot ( adata , plot_type = 'dotplot' , * , groups = None , n_genes = None , groupby = None , values_to_plot = None , var_names = None , min_logfoldchange = None , key = None , show = None , save = None , return_fig = False , gene_symbols = None , ** kwds )
```

## Parameters

- `adata`: ( AnnData ) – AnnData Annotated data matrix.
- `plot_type`: ( str (default: 'dotplot' )) – str Currently only ‘dotplot’ is supported.
- `groups`: ( Union [ str , Sequence [ str ], None ] (default: None )) – str or list of str, optional Groups to include in the plot.
- `n_genes`: ( Optional [ int ] (default: None )) – int, optional Number of genes to include in the plot.
- `groupby`: ( Optional [ str ] (default: None )) – str, optional Key in adata.obs to group by.
- `values_to_plot`: ( Optional [ str ] (default: None )) – str, optional Key in rank_genes_groups results to plot (e.g. ‘logfoldchanges’, ‘scores’).
- `var_names`: ( Union [ Sequence [ str ], Mapping [ str , Sequence [ str ]], None ] (default: None )) – str or list of str or dict, optional Variables to include in the plot. Can be: - A list of gene names: [‘gene1’, ‘gene2’, …] - A dictionary mapping group names to gene lists: {‘group1’: [‘gene1’, ‘gene2’], ‘group2’: [‘gene3’, ‘gene4’]} When a dictionary is provided, genes will be grouped and labeled accordingly in the plot.
- `min_logfoldchange`: ( Optional [ float ] (default: None )) – float, optional Minimum log fold change to include in the plot.
- `key`: ( Optional [ str ] (default: None )) – str, optional Key in adata.uns to use for rank_genes_groups results.
- `show`: ( Optional [ bool ] (default: None )) – bool, optional Whether to show the plot.
- `save`: ( Optional [ bool ] (default: None )) – bool, optional Whether to save the plot.
- `return_fig`: ( bool (default: False )) – bool Whether to return the figure object.
- `gene_symbols`: ( Optional [ str ] (default: None )) – str, optional Key for gene symbols in adata.var .
- `**kwds`: ( Any ) – dict Additional keyword arguments to pass to dotplot.

## Full Documentation

# omicverse.pl.rank_genes_groups_dotplot #

omicverse.pl. rank_genes_groups_dotplot ( adata , plot_type = 'dotplot' , * , groups = None , n_genes = None , groupby = None , values_to_plot = None , var_names = None , min_logfoldchange = None , key = None , show = None , save = None , return_fig = False , gene_symbols = None , ** kwds ) [source] #

Create a dot plot from rank_genes_groups results.

Parameters :

-
adata ( `AnnData `) – AnnData Annotated data matrix.

-
plot_type ( `str `(default: `'dotplot' `)) – str Currently only ‘dotplot’ is supported.

-
groups ( `Union `[ `str `, `Sequence `[ `str `], `None `] (default: `None `)) – str or list of str, optional Groups to include in the plot.

-
n_genes ( `Optional `[ `int `] (default: `None `)) – int, optional Number of genes to include in the plot.

-
groupby ( `Optional `[ `str `] (default: `None `)) – str, optional Key in adata.obs to group by.

-
values_to_plot ( `Optional `[ `str `] (default: `None `)) – str, optional Key in rank_genes_groups results to plot (e.g. ‘logfoldchanges’, ‘scores’).

-
var_names ( `Union `[ `Sequence `[ `str `], `Mapping `[ `str `, `Sequence `[ `str `]], `None `] (default: `None `)) – str or list of str or dict, optional Variables to include in the plot. Can be: - A list of gene names: [‘gene1’, ‘gene2’, …] - A dictionary mapping group names to gene lists: {‘group1’: [‘gene1’, ‘gene2’], ‘group2’: [‘gene3’, ‘gene4’]} When a dictionary is provided, genes will be grouped and labeled accordingly in the plot.

-
min_logfoldchange ( `Optional `[ `float `] (default: `None `)) – float, optional Minimum log fold change to include in the plot.

-
key ( `Optional `[ `str `] (default: `None `)) – str, optional Key in adata.uns to use for rank_genes_groups results.

-
show ( `Optional `[ `bool `] (default: `None `)) – bool, optional Whether to show the plot.

-
save ( `Optional `[ `bool `] (default: `None `)) – bool, optional Whether to save the plot.

-
return_fig ( `bool `(default: `False `)) – bool Whether to return the figure object.

-
gene_symbols ( `Optional `[ `str `] (default: `None `)) – str, optional Key for gene symbols in adata.var .

-
**kwds ( `Any `) – dict Additional keyword arguments to pass to dotplot.

Returns :

If return_fig is True, returns the figure object. If show is False, returns the rendered Matplotlib figure.

Examples

```text
>>> # Basic usage with top genes
>>> ov.pl.rank_genes_groups_dotplot(adata, n_genes=5)

```

```text
>>> # Using logfoldchanges for coloring
>>> ov.pl.rank_genes_groups_dotplot(adata, n_genes=5, values_to_plot='logfoldchanges')

```

```text
>>> # Grouping genes manually
>>> gene_groups = {
... 'Group1': ['gene1', 'gene2'],
... 'Group2': ['gene3', 'gene4']
... }
>>> ov.pl.rank_genes_groups_dotplot(adata, var_names=gene_groups)

```
