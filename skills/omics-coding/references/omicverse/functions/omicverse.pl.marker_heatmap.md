# omicverse.pl.marker_heatmap #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.marker_heatmap`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.marker_heatmap.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Create a dot plot heatmap showing marker gene expression using PyComplexHeatmap.

## Signature

```text
omicverse.pl. marker_heatmap ( adata , marker_genes_dict = None , groupby = None , color_map = 'RdBu_r' , use_raw = True , standard_scale = 'var' , expression_cutoff = 0.0 , bbox_to_anchor = (5, -0.5) , figsize = (8, 4) , spines = False , fontsize = 12 , show_rownames = True , show_colnames = True , save_path = None , ax = None )
```

## Parameters

- `adata`: ( AnnData ) – Annotated data object with expression data
- `marker_genes_dict`: ( Optional [ dict ] (default: None )) – Dictionary mapping cell types to marker genes
- `groupby`: ( Optional [ str ] (default: None )) – Column name for cell type grouping
- `color_map`: ( str (default: 'RdBu_r' )) – Colormap for expression values
- `use_raw`: ( bool (default: True )) – Whether to use raw expression data
- `standard_scale`: ( str (default: 'var' )) – Expression standardization method
- `expression_cutoff`: ( float (default: 0.0 )) – Minimum expression threshold
- `bbox_to_anchor`: ( tuple (default: (5, -0.5) )) – Legend position
- `figsize`: ( tuple (default: (8, 4) )) – Figure dimensions
- `spines`: ( bool (default: False )) – Whether to show plot spines
- `fontsize`: ( int (default: 12 )) – Font size for labels
- `show_rownames`: ( bool (default: True )) – Whether to display row names
- `show_colnames`: ( bool (default: True )) – Whether to display column names
- `save_path`: ( Optional [ str ] (default: None )) – File path for saving plot
- `ax`: (default: None ) – Existing matplotlib axes object

## Full Documentation

# omicverse.pl.marker_heatmap #

omicverse.pl. marker_heatmap ( adata , marker_genes_dict = None , groupby = None , color_map = 'RdBu_r' , use_raw = True , standard_scale = 'var' , expression_cutoff = 0.0 , bbox_to_anchor = (5, -0.5) , figsize = (8, 4) , spines = False , fontsize = 12 , show_rownames = True , show_colnames = True , save_path = None , ax = None ) [source] #

Create a dot plot heatmap showing marker gene expression using PyComplexHeatmap.

Parameters :

-
adata ( `AnnData `) – Annotated data object with expression data

-
marker_genes_dict ( `Optional `[ `dict `] (default: `None `)) – Dictionary mapping cell types to marker genes

-
groupby ( `Optional `[ `str `] (default: `None `)) – Column name for cell type grouping

-
color_map ( `str `(default: `'RdBu_r' `)) – Colormap for expression values

-
use_raw ( `bool `(default: `True `)) – Whether to use raw expression data

-
standard_scale ( `str `(default: `'var' `)) – Expression standardization method

-
expression_cutoff ( `float `(default: `0.0 `)) – Minimum expression threshold

-
bbox_to_anchor ( `tuple `(default: `(5, -0.5) `)) – Legend position

-
figsize ( `tuple `(default: `(8, 4) `)) – Figure dimensions

-
spines ( `bool `(default: `False `)) – Whether to show plot spines

-
fontsize ( `int `(default: `12 `)) – Font size for labels

-
show_rownames ( `bool `(default: `True `)) – Whether to display row names

-
show_colnames ( `bool `(default: `True `)) – Whether to display column names

-
save_path ( `Optional `[ `str `] (default: `None `)) – File path for saving plot

-
ax (default: `None `) – Existing matplotlib axes object

Returns :

matplotlib.figure.Figure object ax: matplotlib.axes.Axes object

Return type :

fig
