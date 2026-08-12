# omicverse.bulk.geneset_plot_multi #

- Package: omicverse
- Language: Python
- Function: `omicverse.bulk.geneset_plot_multi`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.bulk.geneset_plot_multi.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot multiple enrichment result tables in a unified dot-clustermap panel.

## Signature

```text
omicverse.bulk. geneset_plot_multi ( enr_dict , colors_dict , num = 5 , fontsize = 10 , fig_title = '' , fig_xlabel = 'Fractions of genes' , figsize = (2, 4) , cmap = 'YlGnBu' , text_knock = 5 , text_maxsize = 20 , ax = None )
```

## Parameters

- `enr_dict`: ( dict [ str , pandas.DataFrame ] ) – Mapping from group/condition name to enrichment result DataFrame.
- `colors_dict`: ( dict [ str , str ] ) – Color mapping for each group in enr_dict .
- `num`: ( int , optional ) – Number of top terms taken from each group.
- `fontsize`: ( int , optional ) – Base font size for labels and legends.
- `fig_title`: ( str , optional ) – Figure title.
- `fig_xlabel`: ( str , optional ) – X-axis label.
- `figsize`: ( tuple , optional ) – Figure size.
- `cmap`: ( str , optional ) – Colormap used for enrichment significance values.
- `text_knock`: ( int , optional ) – Trim length applied to long term names.
- `text_maxsize`: ( int , optional ) – Maximum wrapped text size for term labels.
- `ax`: ( matplotlib.axes.Axes | None , optional ) – Existing axis; if None a new figure/axis is created.

## Full Documentation

# omicverse.bulk.geneset_plot_multi #

omicverse.bulk. geneset_plot_multi ( enr_dict , colors_dict , num = 5 , fontsize = 10 , fig_title = '' , fig_xlabel = 'Fractions of genes' , figsize = (2, 4) , cmap = 'YlGnBu' , text_knock = 5 , text_maxsize = 20 , ax = None ) [source] #

Plot multiple enrichment result tables in a unified dot-clustermap panel.

Parameters :

-
enr_dict ( dict [ str , pandas.DataFrame ] ) – Mapping from group/condition name to enrichment result DataFrame.

-
colors_dict ( dict [ str , str ] ) – Color mapping for each group in `enr_dict `.

-
num ( int , optional ) – Number of top terms taken from each group.

-
fontsize ( int , optional ) – Base font size for labels and legends.

-
fig_title ( str , optional ) – Figure title.

-
fig_xlabel ( str , optional ) – X-axis label.

-
figsize ( tuple , optional ) – Figure size.

-
cmap ( str , optional ) – Colormap used for enrichment significance values.

-
text_knock ( int , optional ) – Trim length applied to long term names.

-
text_maxsize ( int , optional ) – Maximum wrapped text size for term labels.

-
ax ( matplotlib.axes.Axes | None , optional ) – Existing axis; if `None `a new figure/axis is created.

Returns :

The rendered Marsilea dot-heatmap board (call `.save(path) `or access `.figure `to export). Rows are pathway terms; dot size = gene count, dot colour = -log10 adjusted-p; rows are split/coloured by group.

Return type :

marsilea.SizedHeatmap
