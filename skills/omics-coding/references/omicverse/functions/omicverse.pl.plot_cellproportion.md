# omicverse.pl.plot_cellproportion #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.plot_cellproportion`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.plot_cellproportion.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot stacked bar chart showing cell type proportions across groups.

## Signature

```text
omicverse.pl. plot_cellproportion ( adata , celltype_clusters , visual_clusters , visual_li = None , visual_name = '' , figsize = (4, 6) , ticks_fontsize = 12 , labels_fontsize = 12 , legend = False )
```

## Parameters

- `adata`: ( AnnData object )
- `celltype_clusters`: ( Column name for cell types )
- `visual_clusters`: ( Column name for grouping variable )
- `visual_li`: ( List of groups to plot ( None ) )
- `visual_name`: ( Label for x-axis ( '' ) )
- `figsize`: ( Figure size ( ( 4 , 6 ) ) )
- `ticks_fontsize`: ( Font size for tick labels ( 12 ) )
- `labels_fontsize`: ( Font size for axis labels ( 12 ) )
- `legend`: ( Whether to show legend ( False ) )

## Full Documentation

# omicverse.pl.plot_cellproportion #

omicverse.pl. plot_cellproportion ( adata , celltype_clusters , visual_clusters , visual_li = None , visual_name = '' , figsize = (4, 6) , ticks_fontsize = 12 , labels_fontsize = 12 , legend = False ) [source] #

Plot stacked bar chart showing cell type proportions across groups.

Parameters :

-
adata ( AnnData object )

-
celltype_clusters ( Column name for cell types )

-
visual_clusters ( Column name for grouping variable )

-
visual_li ( List of groups to plot ( None ) )

-
visual_name ( Label for x-axis ( '' ) )

-
figsize ( Figure size ( ( 4 , 6 ) ) )

-
ticks_fontsize ( Font size for tick labels ( 12 ) )

-
labels_fontsize ( Font size for axis labels ( 12 ) )

-
legend ( Whether to show legend ( False ) )

Returns :

Tuple of (figure, axes) objects
