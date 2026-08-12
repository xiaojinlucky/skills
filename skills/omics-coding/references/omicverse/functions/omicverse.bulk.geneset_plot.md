# omicverse.bulk.geneset_plot #

- Package: omicverse
- Language: Python
- Function: `omicverse.bulk.geneset_plot`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.bulk.geneset_plot.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot enrichment results as a bubble plot.

## Signature

```text
omicverse.bulk. geneset_plot ( enrich_res , num = 10 , node_size = [5, 10, 15] , cax_loc = [2, 0.55, 0.5, 0.02] , cax_fontsize = 12 , fig_title = '' , fig_xlabel = 'Fractions of genes' , figsize = (2, 4) , cmap = 'YlGnBu' , text_knock = 5 , text_maxsize = 20 , bbox_to_anchor_used = (-0.45, -13) , node_diameter = 10 , custom_ticks = [5, 10] , ax = None )
```

## Parameters

- `enrich_res`: ( pandas.DataFrame ) – Enrichment result table from geneset_enrichment / pyGSEA.enrichment .
- `num`: ( int , optional ) – Number of top enriched terms to display.
- `node_size`: ( list [ int ] , optional ) – Bubble-size legend entries.
- `cax_loc`: ( list [ float ] , optional ) – Colorbar axis rectangle [left,bottom,width,height] .
- `cax_fontsize`: ( int , optional ) – Font size for colorbar and legend text.
- `fig_title`: ( str , optional ) – Plot title.
- `fig_xlabel`: ( str , optional ) – X-axis label.
- `figsize`: ( tuple , optional ) – Figure size.
- `cmap`: ( str , optional ) – Colormap for enrichment significance.
- `text_knock`: ( int , optional ) – Truncation parameter for long term names.
- `text_maxsize`: ( int , optional ) – Maximum text length/size control for term labels.
- `bbox_to_anchor_used`: ( tuple , optional ) – Legend anchor coordinates.
- `node_diameter`: ( int , optional ) – Bubble size scale factor.
- `custom_ticks`: ( list [ int ] , optional ) – Custom colorbar ticks.
- `ax`: ( matplotlib.axes.Axes | None , optional ) – Existing axis to draw on.

## Full Documentation

# omicverse.bulk.geneset_plot #

omicverse.bulk. geneset_plot ( enrich_res , num = 10 , node_size = [5, 10, 15] , cax_loc = [2, 0.55, 0.5, 0.02] , cax_fontsize = 12 , fig_title = '' , fig_xlabel = 'Fractions of genes' , figsize = (2, 4) , cmap = 'YlGnBu' , text_knock = 5 , text_maxsize = 20 , bbox_to_anchor_used = (-0.45, -13) , node_diameter = 10 , custom_ticks = [5, 10] , ax = None ) [source] #

Plot enrichment results as a bubble plot.

Parameters :

-
enrich_res ( pandas.DataFrame ) – Enrichment result table from `geneset_enrichment `/ `pyGSEA.enrichment `.

-
num ( int , optional ) – Number of top enriched terms to display.

-
node_size ( list [ int ] , optional ) – Bubble-size legend entries.

-
cax_loc ( list [ float ] , optional ) – Colorbar axis rectangle `[left,bottom,width,height] `.

-
cax_fontsize ( int , optional ) – Font size for colorbar and legend text.

-
fig_title ( str , optional ) – Plot title.

-
fig_xlabel ( str , optional ) – X-axis label.

-
figsize ( tuple , optional ) – Figure size.

-
cmap ( str , optional ) – Colormap for enrichment significance.

-
text_knock ( int , optional ) – Truncation parameter for long term names.

-
text_maxsize ( int , optional ) – Maximum text length/size control for term labels.

-
bbox_to_anchor_used ( tuple , optional ) – Legend anchor coordinates.

-
node_diameter ( int , optional ) – Bubble size scale factor.

-
custom_ticks ( list [ int ] , optional ) – Custom colorbar ticks.

-
ax ( matplotlib.axes.Axes | None , optional ) – Existing axis to draw on.

Returns :

Axis containing enrichment bubble plot.

Return type :

matplotlib.axes.Axes
