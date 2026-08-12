# omicverse.pl.boxplot #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.boxplot`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.boxplot.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Create a boxplot with jittered points to visualize data distribution across categories.

## Signature

```text
omicverse.pl. boxplot ( data , hue , x_value = None , y_value = None , width = 0.3 , title = '' , figsize = (6, 3) , palette = None , fontsize = 10 , legend_bbox = (1, 0.55) , legend_ncol = 1 , hue_order = None , * , x = None , y = None , ax = None , show_points = True )
```

## Parameters

- `data`: ( pd.DataFrame ) – Input table containing grouping and numeric columns.
- `hue`: ( str ) – Column name used for color grouping.
- `x_value`: ( str ) – Column name used as x-axis category. x is accepted as an alias, which is what the sibling table-first plots ( barplot , stripplot , violinplot ) call it.
- `y_value`: ( str ) – Column name containing numeric values. y is accepted as an alias.
- `width`: ( float ) – Width of each box element.
- `title`: ( str ) – Plot title.
- `figsize`: ( tuple ) – Figure size passed to matplotlib. Ignored when ax is given — the axes already has a size, and resizing its figure would rescale every other panel sharing it.
- `palette`: ( list or None ) – Color list for hue groups; default palette is used when None .
- `fontsize`: ( int ) – Base font size for ticks/labels.
- `legend_bbox`: ( tuple ) – Legend anchor position.
- `legend_ncol`: ( int ) – Number of legend columns.
- `hue_order`: ( list or None ) – Explicit order of hue categories.
- `x`: ( str ) – Aliases for x_value / y_value . Keyword-only.
- `y`: ( str ) – Aliases for x_value / y_value . Keyword-only.
- `ax`: ( matplotlib.axes.Axes or None ) – Draw into this axes instead of creating a figure. Keyword-only, so every existing positional call is unaffected. Pass one of multipanel() ’s panels here to place the boxplot inside a larger figure.
- `show_points`: ( bool ) – Overlay jittered raw points on each box. True (default) keeps the existing look; False draws boxes only, for a clean multi-panel figure.

## Full Documentation

# omicverse.pl.boxplot #

omicverse.pl. boxplot ( data , hue , x_value = None , y_value = None , width = 0.3 , title = '' , figsize = (6, 3) , palette = None , fontsize = 10 , legend_bbox = (1, 0.55) , legend_ncol = 1 , hue_order = None , * , x = None , y = None , ax = None , show_points = True ) [source] #

Create a boxplot with jittered points to visualize data distribution across categories.

Parameters :

-
data ( pd.DataFrame ) – Input table containing grouping and numeric columns.

-
hue ( str ) – Column name used for color grouping.

-
x_value ( str ) – Column name used as x-axis category. `x `is accepted as an alias, which is what the sibling table-first plots ( `barplot `, `stripplot `, `violinplot `) call it.

-
y_value ( str ) – Column name containing numeric values. `y `is accepted as an alias.

-
width ( float ) – Width of each box element.

-
title ( str ) – Plot title.

-
figsize ( tuple ) – Figure size passed to matplotlib. Ignored when `ax `is given — the axes already has a size, and resizing its figure would rescale every other panel sharing it.

-
palette ( list or None ) – Color list for hue groups; default palette is used when `None `.

-
fontsize ( int ) – Base font size for ticks/labels.

-
legend_bbox ( tuple ) – Legend anchor position.

-
legend_ncol ( int ) – Number of legend columns.

-
hue_order ( list or None ) – Explicit order of hue categories.

-
x ( str ) – Aliases for `x_value `/ `y_value `. Keyword-only.

-
y ( str ) – Aliases for `x_value `/ `y_value `. Keyword-only.

-
ax ( matplotlib.axes.Axes or None ) – Draw into this axes instead of creating a figure. Keyword-only, so every existing positional call is unaffected. Pass one of `multipanel() `’s panels here to place the boxplot inside a larger figure.

-
show_points ( bool ) – Overlay jittered raw points on each box. `True `(default) keeps the existing look; `False `draws boxes only, for a clean multi-panel figure.

Returns :

Figure and axes of generated boxplot. The pair is returned in both cases — when `ax `was supplied the figure is simply the one that axes already belongs to — so the return shape never depends on how the function was called.

Return type :

Tuple[ matplotlib.figure.Figure , matplotlib.axes.Axes ]
