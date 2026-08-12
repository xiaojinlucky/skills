# omicverse.pl.plot_grouped_fractions #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.plot_grouped_fractions`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.plot_grouped_fractions.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot grouped cell-fraction summaries as stacked bars.

## Signature

```text
omicverse.pl. plot_grouped_fractions ( res , obs , group_key , color_dict = None , agg = 'mean' , normalize = True , figsize = (4, 4) , * , ax = None )
```

## Parameters

- `res`: ( pd.DataFrame ) – Predicted cell-fraction matrix with samples as rows and cell types as columns.
- `obs`: ( pd.DataFrame ) – Sample metadata table aligned to res index.
- `group_key`: ( str ) – Metadata column used to group samples (for example severity/condition).
- `color_dict`: ( dict or None ) – Mapping from cell-type names to colors. If provided, column order follows keys.
- `agg`: ( str ) – Group aggregation method: 'mean' , 'median' , or 'sum' .
- `normalize`: ( bool ) – Whether each grouped row is normalized to sum to 1.
- `figsize`: ( tuple ) – Figure size passed to pandas/matplotlib plotting backend. Ignored when ax is given: pandas would call set_size_inches on the axes’ figure, which would resize the caller’s whole multi-panel canvas.
- `ax`: ( matplotlib.axes.Axes or None ) – Draw into this axes instead of creating a figure. Keyword-only, so existing positional calls are unaffected.

## Full Documentation

# omicverse.pl.plot_grouped_fractions #

omicverse.pl. plot_grouped_fractions ( res , obs , group_key , color_dict = None , agg = 'mean' , normalize = True , figsize = (4, 4) , * , ax = None ) [source] #

Plot grouped cell-fraction summaries as stacked bars.

Parameters :

-
res ( pd.DataFrame ) – Predicted cell-fraction matrix with samples as rows and cell types as columns.

-
obs ( pd.DataFrame ) – Sample metadata table aligned to `res `index.

-
group_key ( str ) – Metadata column used to group samples (for example severity/condition).

-
color_dict ( dict or None ) – Mapping from cell-type names to colors. If provided, column order follows keys.

-
agg ( str ) – Group aggregation method: `'mean' `, `'median' `, or `'sum' `.

-
normalize ( bool ) – Whether each grouped row is normalized to sum to 1.

-
figsize ( tuple ) – Figure size passed to pandas/matplotlib plotting backend. Ignored when `ax `is given: pandas would call `set_size_inches `on the axes’ figure, which would resize the caller’s whole multi-panel canvas.

-
ax ( matplotlib.axes.Axes or None ) – Draw into this axes instead of creating a figure. Keyword-only, so existing positional calls are unaffected.

Returns :

Axes containing the grouped stacked-bar chart.

Return type :

matplotlib.axes.Axes
