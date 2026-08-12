# omicverse.pl.bardotplot #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.bardotplot`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.bardotplot.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Create a combined bar-and-dot summary plot by groups.

## Signature

```text
omicverse.pl. bardotplot ( adata , groupby , color , figsize = (8, 3) , return_values = False , fontsize = 12 , xlabel = '' , ylabel = '' , xticks_rotation = 90 , ax = None , bar_kwargs = None , scatter_kwargs = None )
```

## Parameters

- `adata`: ( AnnData ) – AnnData containing expression/metadata used for plotting.
- `groupby`: ( str ) – Grouping column in adata.obs .
- `color`: ( str ) – Feature in adata.var_names or adata.obs to summarize.
- `figsize`: ( tuple , default= ( 8 , 3 ) ) – Figure size.
- `return_values`: ( bool , default=False ) – Whether to return computed grouped values instead of plotting.
- `fontsize`: ( int , default=12 ) – Font size.
- `xlabel`: ( str , default='' ) – X-axis label.
- `ylabel`: ( str , default='' ) – Y-axis label.
- `xticks_rotation`: ( int , default=90 ) – Rotation angle of x tick labels.
- `ax`: ( matplotlib.axes.Axes , optional ) – Existing axis for plotting.
- `bar_kwargs`: ( dict , optional ) – Keyword arguments forwarded to plt.bar .
- `scatter_kwargs`: ( dict , optional ) – Keyword arguments forwarded to plt.scatter .

## Full Documentation

# omicverse.pl.bardotplot #

omicverse.pl. bardotplot ( adata , groupby , color , figsize = (8, 3) , return_values = False , fontsize = 12 , xlabel = '' , ylabel = '' , xticks_rotation = 90 , ax = None , bar_kwargs = None , scatter_kwargs = None ) [source] #

Create a combined bar-and-dot summary plot by groups.

Parameters :

-
adata ( AnnData ) – AnnData containing expression/metadata used for plotting.

-
groupby ( str ) – Grouping column in `adata.obs `.

-
color ( str ) – Feature in `adata.var_names `or `adata.obs `to summarize.

-
figsize ( tuple , default= ( 8 , 3 ) ) – Figure size.

-
return_values ( bool , default=False ) – Whether to return computed grouped values instead of plotting.

-
fontsize ( int , default=12 ) – Font size.

-
xlabel ( str , default='' ) – X-axis label.

-
ylabel ( str , default='' ) – Y-axis label.

-
xticks_rotation ( int , default=90 ) – Rotation angle of x tick labels.

-
ax ( matplotlib.axes.Axes , optional ) – Existing axis for plotting.

-
bar_kwargs ( dict , optional ) – Keyword arguments forwarded to `plt.bar `.

-
scatter_kwargs ( dict , optional ) – Keyword arguments forwarded to `plt.scatter `.

Returns :

Grouped values when `return_values=True `; otherwise plotting handles.

Return type :

pandas.DataFrame or tuple
