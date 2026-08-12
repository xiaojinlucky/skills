# omicverse.pl.dynamic_trends #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.dynamic_trends`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.dynamic_trends.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot GAM-fitted pseudotime trends for one or more genes.

## Signature

```text
omicverse.pl. dynamic_trends ( result , genes = None , * , groups = None , datasets = None , compare_features = False , compare_groups = False , add_line = True , add_interval = True , add_point = False , point_color_by = None , point_palette = None , split_time = None , shared_trunk = False , trunk_color = '3C5488' , trunk_alpha = 0.25 , trunk_linewidth = None , line_palette = None , line_palcolor = None , line_style_by = None , line_styles = None , figsize = (3, 3) , nrows = None , ncols = None , scatter_size = 8 , scatter_alpha = 0.2 , linewidth = 2.0 , legend = True , legend_outside = True , legend_loc = None , legend_bbox_to_anchor = None , legend_fontsize = None , legend_ncol = 1 , sharey = False , xlabel = 'Pseudotime' , ylabel = 'Expression' , title = None , title_fontsize = None , add_grid = True , grid_alpha = 0.3 , grid_linewidth = 0.6 , show = None , return_axes = False , return_fig = False , ax = None , verbose = True )
```

## Parameters

- `result`: – Result returned by ov.single.dynamic_features() .
- `genes`: (default: None ) – Gene name or list of gene names to plot. When None , all fitted genes available in result are shown.
- `groups`: (default: None ) – Optional fitted group names to include when result contains multiple lineages, cell types, or conditions.
- `datasets`: (default: None ) – Backward-compatible alias of groups . Prefer groups in new code.
- `compare_features`: ( bool (default: False )) – Whether to compare multiple selected features on the same panel. When enabled for a single fitted group, the default panel title is left blank to avoid generic titles such as adata .
- `compare_groups`: ( bool (default: False )) – Whether to compare multiple fitted groups on the same panel. Groups are the fitted series labels returned by ov.single.dynamic_features() , for example lineages, cell types, or condition names.
- `add_line`: ( bool (default: True )) – Whether to draw the fitted GAM trend lines.
- `add_interval`: ( bool (default: True )) – Whether to draw confidence interval ribbons when available.
- `add_point`: ( bool (default: False )) – Whether to overlay observed expression values. This requires that result was computed with ov.single.dynamic_features() using store_raw=True .
- `point_color_by`: ( Optional [ str ] (default: None )) – Optional column in the stored raw point table used to color observed points independently from the fitted line colors. This enables views such as a single global trend line with points colored by State or subtype . Requires add_point=True and ov.single.dynamic_features(..., store_raw=True, raw_obs_keys=[...]) .
- `point_palette`: (default: None ) – Optional palette used when point_color_by is categorical.
- `split_time`: ( Union [ float , dict [ str , float ], None ] (default: None )) – Optional pseudotime position used to render branch-aware comparisons. When provided together with compare_groups=True , each group trend is clipped to pseudotime >= split_time . This can be supplied as a scalar applied to every panel, or as a mapping keyed by gene / panel name with an optional 'default' fallback.
- `shared_trunk`: ( bool (default: False )) – Whether to draw a shared pre-split trunk when split_time is provided. The trunk is computed as the mean fitted curve across the compared groups for each gene before the split point, giving a generic branch-aware view that can be reused across Monocle, Slingshot, Palantir, CellRank, and other trajectory methods.
- `trunk_color`: ( str (default: '#3C5488' )) – Color used for the shared trunk line when shared_trunk=True and a single feature is shown on a panel.
- `trunk_alpha`: ( float (default: 0.25 )) – Alpha transparency used for the shared trunk confidence ribbon.
- `trunk_linewidth`: ( Optional [ float ] (default: None )) – Optional line width used for the shared trunk. Defaults to linewidth when unset.
- `line_palette`: (default: None ) – Optional named matplotlib colormap or palette-like sequence describing line colors.
- `line_palcolor`: (default: None ) – Explicit color mapping or sequence overriding line_palette .
- `line_style_by`: ( Optional [ str ] (default: None )) – Optional semantic used to vary line styles when a comparison panel contains multiple series. Choose from 'features' or 'groups' .
- `line_styles`: (default: None ) – Optional line-style mapping or sequence used with line_style_by .
- `figsize`: ( tuple (default: (3, 3) )) – Size of each panel in inches. For multi-gene plots this is interpreted as the per-panel size before tiling.
- `nrows`: ( Optional [ int ] (default: None )) – Number of subplot rows for multi-panel layouts.
- `ncols`: ( Optional [ int ] (default: None )) – Number of subplot columns for multi-gene layouts.
- `scatter_size`: ( float (default: 8 )) – Marker size used for observed points when add_point=True .
- `scatter_alpha`: ( float (default: 0.2 )) – Alpha transparency for observed points when add_point=True .
- `linewidth`: ( float (default: 2.0 )) – Line width for fitted trend curves.
- `legend`: ( bool (default: True )) – Whether to draw a legend on each axis.
- `legend_outside`: ( bool (default: True )) – Whether to place the legend outside the plotting area on the right. Kept for backward compatibility; prefer legend_loc in new code.
- `legend_loc`: ( Union [ str , int , None ] (default: None )) – Legend location. Use 'right margin' for the Scanpy/OmicVerse-style outside-right legend, or any Matplotlib legend location such as 'best' or 'upper center' .
- `legend_bbox_to_anchor`: ( Optional [ tuple ] (default: None )) – Optional Matplotlib bbox_to_anchor used together with legend_loc for precise placement.
- `legend_fontsize`: ( Union [ float , str , None ] (default: None )) – Optional legend font size.
- `legend_ncol`: ( int (default: 1 )) – Number of legend columns.
- `sharey`: ( bool (default: False )) – Whether subplots should share the y-axis in multi-gene layouts.
- `xlabel`: ( str (default: 'Pseudotime' )) – Label used for the x-axis.
- `ylabel`: ( str (default: 'Expression' )) – Label used for the y-axis.
- `title`: (default: None ) – Optional title applied to the plotted axis or axes. Pass a list/tuple to specify per-panel titles in multi-panel layouts. By default, panel titles use the plotted gene or group label automatically. Pass '' to hide titles explicitly.
- `title_fontsize`: ( Optional [ float ] (default: None )) – Font size used for panel or figure titles. When None , matplotlib’s default title size is used.
- `add_grid`: ( bool (default: True )) – Whether to draw a light background grid.
- `grid_alpha`: ( float (default: 0.3 )) – Alpha transparency used for the background grid.
- `grid_linewidth`: ( float (default: 0.6 )) – Line width used for the background grid.
- `show`: ( Optional [ bool ] (default: None )) – Whether to call plt.show() before returning. By default, plots are shown only when neither return_fig nor return_axes is requested.
- `return_axes`: ( bool (default: False )) – Whether to return the created axis or axes. When False and return_fig=False , the function returns None to avoid notebook repr noise.
- `return_fig`: ( bool (default: False )) – Whether to return the figure together with the created axes.
- `ax`: (default: None ) – Existing matplotlib axis used when plotting a single gene.
- `verbose`: ( bool (default: True )) – Whether to print a short plotting summary.

## Full Documentation

# omicverse.pl.dynamic_trends #

omicverse.pl. dynamic_trends ( result , genes = None , * , groups = None , datasets = None , compare_features = False , compare_groups = False , add_line = True , add_interval = True , add_point = False , point_color_by = None , point_palette = None , split_time = None , shared_trunk = False , trunk_color = '#3C5488' , trunk_alpha = 0.25 , trunk_linewidth = None , line_palette = None , line_palcolor = None , line_style_by = None , line_styles = None , figsize = (3, 3) , nrows = None , ncols = None , scatter_size = 8 , scatter_alpha = 0.2 , linewidth = 2.0 , legend = True , legend_outside = True , legend_loc = None , legend_bbox_to_anchor = None , legend_fontsize = None , legend_ncol = 1 , sharey = False , xlabel = 'Pseudotime' , ylabel = 'Expression' , title = None , title_fontsize = None , add_grid = True , grid_alpha = 0.3 , grid_linewidth = 0.6 , show = None , return_axes = False , return_fig = False , ax = None , verbose = True ) [source] #

Plot GAM-fitted pseudotime trends for one or more genes.

Parameters :

-
result – Result returned by `ov.single.dynamic_features() `.

-
genes (default: `None `) – Gene name or list of gene names to plot. When `None `, all fitted genes available in `result `are shown.

-
groups (default: `None `) – Optional fitted group names to include when `result `contains multiple lineages, cell types, or conditions.

-
datasets (default: `None `) – Backward-compatible alias of `groups `. Prefer `groups `in new code.

-
compare_features ( `bool `(default: `False `)) – Whether to compare multiple selected features on the same panel. When enabled for a single fitted group, the default panel title is left blank to avoid generic titles such as `adata `.

-
compare_groups ( `bool `(default: `False `)) – Whether to compare multiple fitted groups on the same panel. Groups are the fitted series labels returned by `ov.single.dynamic_features() `, for example lineages, cell types, or condition names.

-
add_line ( `bool `(default: `True `)) – Whether to draw the fitted GAM trend lines.

-
add_interval ( `bool `(default: `True `)) – Whether to draw confidence interval ribbons when available.

-
add_point ( `bool `(default: `False `)) – Whether to overlay observed expression values. This requires that `result `was computed with `ov.single.dynamic_features() `using `store_raw=True `.

-
point_color_by ( `Optional `[ `str `] (default: `None `)) – Optional column in the stored raw point table used to color observed points independently from the fitted line colors. This enables views such as a single global trend line with points colored by `State `or `subtype `. Requires `add_point=True `and `ov.single.dynamic_features(..., store_raw=True, raw_obs_keys=[...]) `.

-
point_palette (default: `None `) – Optional palette used when `point_color_by `is categorical.

-
split_time ( `Union `[ `float `, `dict `[ `str `, `float `], `None `] (default: `None `)) – Optional pseudotime position used to render branch-aware comparisons. When provided together with `compare_groups=True `, each group trend is clipped to `pseudotime >= split_time `. This can be supplied as a scalar applied to every panel, or as a mapping keyed by gene / panel name with an optional `'default' `fallback.

-
shared_trunk ( `bool `(default: `False `)) – Whether to draw a shared pre-split trunk when `split_time `is provided. The trunk is computed as the mean fitted curve across the compared groups for each gene before the split point, giving a generic branch-aware view that can be reused across Monocle, Slingshot, Palantir, CellRank, and other trajectory methods.

-
trunk_color ( `str `(default: `'#3C5488' `)) – Color used for the shared trunk line when `shared_trunk=True `and a single feature is shown on a panel.

-
trunk_alpha ( `float `(default: `0.25 `)) – Alpha transparency used for the shared trunk confidence ribbon.

-
trunk_linewidth ( `Optional `[ `float `] (default: `None `)) – Optional line width used for the shared trunk. Defaults to `linewidth `when unset.

-
line_palette (default: `None `) – Optional named matplotlib colormap or palette-like sequence describing line colors.

-
line_palcolor (default: `None `) – Explicit color mapping or sequence overriding `line_palette `.

-
line_style_by ( `Optional `[ `str `] (default: `None `)) – Optional semantic used to vary line styles when a comparison panel contains multiple series. Choose from `'features' `or `'groups' `.

-
line_styles (default: `None `) – Optional line-style mapping or sequence used with `line_style_by `.

-
figsize ( `tuple `(default: `(3, 3) `)) – Size of each panel in inches. For multi-gene plots this is interpreted as the per-panel size before tiling.

-
nrows ( `Optional `[ `int `] (default: `None `)) – Number of subplot rows for multi-panel layouts.

-
ncols ( `Optional `[ `int `] (default: `None `)) – Number of subplot columns for multi-gene layouts.

-
scatter_size ( `float `(default: `8 `)) – Marker size used for observed points when `add_point=True `.

-
scatter_alpha ( `float `(default: `0.2 `)) – Alpha transparency for observed points when `add_point=True `.

-
linewidth ( `float `(default: `2.0 `)) – Line width for fitted trend curves.

-
legend ( `bool `(default: `True `)) – Whether to draw a legend on each axis.

-
legend_outside ( `bool `(default: `True `)) – Whether to place the legend outside the plotting area on the right. Kept for backward compatibility; prefer `legend_loc `in new code.

-
legend_loc ( `Union `[ `str `, `int `, `None `] (default: `None `)) – Legend location. Use `'right margin' `for the Scanpy/OmicVerse-style outside-right legend, or any Matplotlib legend location such as `'best' `or `'upper center' `.

-
legend_bbox_to_anchor ( `Optional `[ `tuple `] (default: `None `)) – Optional Matplotlib `bbox_to_anchor `used together with `legend_loc `for precise placement.

-
legend_fontsize ( `Union `[ `float `, `str `, `None `] (default: `None `)) – Optional legend font size.

-
legend_ncol ( `int `(default: `1 `)) – Number of legend columns.

-
sharey ( `bool `(default: `False `)) – Whether subplots should share the y-axis in multi-gene layouts.

-
xlabel ( `str `(default: `'Pseudotime' `)) – Label used for the x-axis.

-
ylabel ( `str `(default: `'Expression' `)) – Label used for the y-axis.

-
title (default: `None `) – Optional title applied to the plotted axis or axes. Pass a list/tuple to specify per-panel titles in multi-panel layouts. By default, panel titles use the plotted gene or group label automatically. Pass `'' `to hide titles explicitly.

-
title_fontsize ( `Optional `[ `float `] (default: `None `)) – Font size used for panel or figure titles. When `None `, matplotlib’s default title size is used.

-
add_grid ( `bool `(default: `True `)) – Whether to draw a light background grid.

-
grid_alpha ( `float `(default: `0.3 `)) – Alpha transparency used for the background grid.

-
grid_linewidth ( `float `(default: `0.6 `)) – Line width used for the background grid.

-
show ( `Optional `[ `bool `] (default: `None `)) – Whether to call `plt.show() `before returning. By default, plots are shown only when neither `return_fig `nor `return_axes `is requested.

-
return_axes ( `bool `(default: `False `)) – Whether to return the created axis or axes. When `False `and `return_fig=False `, the function returns `None `to avoid notebook repr noise.

-
return_fig ( `bool `(default: `False `)) – Whether to return the figure together with the created axes.

-
ax (default: `None `) – Existing matplotlib axis used when plotting a single gene.

-
verbose ( `bool `(default: `True `)) – Whether to print a short plotting summary.

Returns :

Returns `None `by default after drawing so notebook cells do not print raw axis representations. When `return_axes=True `, returns the created axis or axes. When `return_fig=True `, returns `(figure, axes) `.

Return type :

None | matplotlib.axes.Axes | list [ matplotlib.axes.Axes ] | tuple
