# omicverse.pl.complexheatmap #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.complexheatmap`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.complexheatmap.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Generate a complex annotated heatmap using PyComplexHeatmap.

## Signature

```text
omicverse.pl. complexheatmap ( adata , groupby = '' , figsize = (6, 10) , layer = None , use_raw = False , var_names = None , gene_symbols = None , standard_scale = None , col_color_bars = None , col_color_labels = None , left_color_bars = None , left_color_labels = None , right_color_bars = None , right_color_labels = None , marker_genes_dict = None , index_name = '' , value_name = '' , cmap = 'parula' , xlabel = None , ylabel = None , label = '' , save = False , save_pathway = '' , legend_gap = 7 , legend_hpad = 0 , show = False , left_add_text = False , col_split_gap = 1 , row_split_gap = 1 , col_height = 4 , left_height = 4 , right_height = 4 , col_cluster = False , row_cluster = False , row_split = None , col_split = None , legend = True , plot_legend = True , right_fontsize = 12 )
```

## Parameters

- `adata`: – Annotated data object containing expression data
- `groupby`: (default: '' ) – Grouping variable for cell categorization
- `figsize`: (default: (6, 10) ) – Figure dimensions as (width, height)
- `layer`: ( Optional [ str ] (default: None )) – Data layer to use for expression values
- `use_raw`: ( bool (default: False )) – Whether to use raw expression data
- `var_names`: (default: None ) – List of genes to include in heatmap
- `gene_symbols`: (default: None ) – Gene symbol column name
- `standard_scale`: ( Optional [ str ] (default: None )) – Standardization method - ‘obs’, ‘var’, or None
- `col_color_bars`: ( Optional [ dict ] (default: None )) – Color mapping dictionary for column annotations
- `col_color_labels`: ( Optional [ dict ] (default: None )) – Color mapping for column labels
- `left_color_bars`: ( Optional [ dict ] (default: None )) – Color mapping for left annotations
- `left_color_labels`: ( Optional [ dict ] (default: None )) – Color mapping for left labels
- `right_color_bars`: ( Optional [ dict ] (default: None )) – Color mapping for right annotations
- `right_color_labels`: ( Optional [ dict ] (default: None )) – Color mapping for right labels
- `marker_genes_dict`: ( Optional [ dict ] (default: None )) – Dictionary mapping cell types to marker genes
- `index_name`: ( str (default: '' )) – Name for index column in melted data
- `value_name`: ( str (default: '' )) – Name for value column in melted data
- `cmap`: ( str (default: 'parula' )) – Colormap for heatmap values
- `xlabel`: ( Optional [ str ] (default: None )) – X-axis label
- `ylabel`: ( Optional [ str ] (default: None )) – Y-axis label
- `label`: ( str (default: '' )) – Plot label
- `save`: ( bool (default: False )) – Whether to save the plot
- `save_pathway`: ( str (default: '' )) – File path for saving
- `legend_gap`: ( int (default: 7 )) – Gap between legend items
- `legend_hpad`: ( int (default: 0 )) – Horizontal padding for legend
- `show`: ( bool (default: False )) – Whether to display the plot
- `left_add_text`: ( bool (default: False )) – Whether to add text to left annotations
- `col_split_gap`: ( int (default: 1 )) – Gap between column splits
- `row_split_gap`: ( int (default: 1 )) – Gap between row splits
- `col_height`: ( int (default: 4 )) – Height of column annotations
- `left_height`: ( int (default: 4 )) – Height of left annotations
- `right_height`: ( int (default: 4 )) – Height of right annotations
- `col_cluster`: ( bool (default: False )) – Whether to cluster columns
- `row_cluster`: ( bool (default: False )) – Whether to cluster rows
- `row_split`: (default: None ) – Row splitting variable
- `col_split`: (default: None ) – Column splitting variable
- `legend`: ( bool (default: True )) – Whether to show legend
- `plot_legend`: ( bool (default: True )) – Whether to plot legend
- `right_fontsize`: ( int (default: 12 )) – Font size for right annotations

## Full Documentation

# omicverse.pl.complexheatmap #

omicverse.pl. complexheatmap ( adata , groupby = '' , figsize = (6, 10) , layer = None , use_raw = False , var_names = None , gene_symbols = None , standard_scale = None , col_color_bars = None , col_color_labels = None , left_color_bars = None , left_color_labels = None , right_color_bars = None , right_color_labels = None , marker_genes_dict = None , index_name = '' , value_name = '' , cmap = 'parula' , xlabel = None , ylabel = None , label = '' , save = False , save_pathway = '' , legend_gap = 7 , legend_hpad = 0 , show = False , left_add_text = False , col_split_gap = 1 , row_split_gap = 1 , col_height = 4 , left_height = 4 , right_height = 4 , col_cluster = False , row_cluster = False , row_split = None , col_split = None , legend = True , plot_legend = True , right_fontsize = 12 ) [source] #

Generate a complex annotated heatmap using PyComplexHeatmap.

Parameters :

-
adata – Annotated data object containing expression data

-
groupby (default: `'' `) – Grouping variable for cell categorization

-
figsize (default: `(6, 10) `) – Figure dimensions as (width, height)

-
layer ( `Optional `[ `str `] (default: `None `)) – Data layer to use for expression values

-
use_raw ( `bool `(default: `False `)) – Whether to use raw expression data

-
var_names (default: `None `) – List of genes to include in heatmap

-
gene_symbols (default: `None `) – Gene symbol column name

-
standard_scale ( `Optional `[ `str `] (default: `None `)) – Standardization method - ‘obs’, ‘var’, or None

-
col_color_bars ( `Optional `[ `dict `] (default: `None `)) – Color mapping dictionary for column annotations

-
col_color_labels ( `Optional `[ `dict `] (default: `None `)) – Color mapping for column labels

-
left_color_bars ( `Optional `[ `dict `] (default: `None `)) – Color mapping for left annotations

-
left_color_labels ( `Optional `[ `dict `] (default: `None `)) – Color mapping for left labels

-
right_color_bars ( `Optional `[ `dict `] (default: `None `)) – Color mapping for right annotations

-
right_color_labels ( `Optional `[ `dict `] (default: `None `)) – Color mapping for right labels

-
marker_genes_dict ( `Optional `[ `dict `] (default: `None `)) – Dictionary mapping cell types to marker genes

-
index_name ( `str `(default: `'' `)) – Name for index column in melted data

-
value_name ( `str `(default: `'' `)) – Name for value column in melted data

-
cmap ( `str `(default: `'parula' `)) – Colormap for heatmap values

-
xlabel ( `Optional `[ `str `] (default: `None `)) – X-axis label

-
ylabel ( `Optional `[ `str `] (default: `None `)) – Y-axis label

-
label ( `str `(default: `'' `)) – Plot label

-
save ( `bool `(default: `False `)) – Whether to save the plot

-
save_pathway ( `str `(default: `'' `)) – File path for saving

-
legend_gap ( `int `(default: `7 `)) – Gap between legend items

-
legend_hpad ( `int `(default: `0 `)) – Horizontal padding for legend

-
show ( `bool `(default: `False `)) – Whether to display the plot

-
left_add_text ( `bool `(default: `False `)) – Whether to add text to left annotations

-
col_split_gap ( `int `(default: `1 `)) – Gap between column splits

-
row_split_gap ( `int `(default: `1 `)) – Gap between row splits

-
col_height ( `int `(default: `4 `)) – Height of column annotations

-
left_height ( `int `(default: `4 `)) – Height of left annotations

-
right_height ( `int `(default: `4 `)) – Height of right annotations

-
col_cluster ( `bool `(default: `False `)) – Whether to cluster columns

-
row_cluster ( `bool `(default: `False `)) – Whether to cluster rows

-
row_split (default: `None `) – Row splitting variable

-
col_split (default: `None `) – Column splitting variable

-
legend ( `bool `(default: `True `)) – Whether to show legend

-
plot_legend ( `bool `(default: `True `)) – Whether to plot legend

-
right_fontsize ( `int `(default: `12 `)) – Font size for right annotations

Returns :

PyComplexHeatmap ClusterMapPlotter object

Return type :

cm
