# omicverse.pl.single_group_boxplot #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.single_group_boxplot`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.single_group_boxplot.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

adata (AnnData object): The data object containing the information for plotting. groupby (str): The variable used for grouping the data. color (str): The variable used for coloring the data points. type_color_dict (dict): A dictionary mapping group categories to specific colors. title (str): The title for the plot. ylabel (str): The label for the y-axis. kruskal_test (bool): Whether to perform a Kruskal-Wallis test and display the p-value on the plot. figsize (tuple): The size of the plot figure in inches (width, height). x_ticks_plot (bool): Whether to display x-axis tick labels. legend_plot (bool): Whether to display a legend for the groups. bbox_to_anchor (tuple): The position of the legend bbox (x, y) in axes coordinates. save (bool): Whether to save the plot to a file. point_number (int): The number of data points to be plotted for each group. save_pathway (str): The file path for saving the plot (if save is True). sort (bool): Whether to sort the groups based on their mean values. scatter_kwargs (dict): Additional keyword arguments for customizing the scatter plot. ax (matplotlib.axes.Axes): A pre-existing axes object for plotting (optional).

## Signature

```text
omicverse.pl. single_group_boxplot ( adata , groupby = '' , color = '' , type_color_dict = None , title = '' , ylabel = '' , kruskal_test = False , figsize = (4, 4) , x_ticks_plot = False , legend_plot = True , bbox_to_anchor = (1, 0.55) , save = False , point_number = 5 , save_pathway = '' , sort = True , scatter_kwargs = None , ax = None , fontsize = 12 )
```

## Parameters

- `groupby`: ( str (default: '' ))
- `color`: ( str (default: '' ))
- `type_color_dict`: ( Optional [ dict ] (default: None ))
- `title`: ( str (default: '' ))
- `ylabel`: ( str (default: '' ))
- `kruskal_test`: ( bool (default: False ))
- `figsize`: ( tuple (default: (4, 4) ))
- `x_ticks_plot`: ( bool (default: False ))
- `legend_plot`: ( bool (default: True ))
- `bbox_to_anchor`: ( tuple (default: (1, 0.55) ))
- `save`: ( bool (default: False ))
- `point_number`: ( int (default: 5 ))
- `save_pathway`: ( str (default: '' ))
- `sort`: ( bool (default: True ))
- `scatter_kwargs`: ( Optional [ dict ] (default: None ))
- `adata`: Detected from function signature; no parameter description detected.
- `ax`: Detected from function signature; no parameter description detected.
- `fontsize`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.pl.single_group_boxplot #

omicverse.pl. single_group_boxplot ( adata , groupby = '' , color = '' , type_color_dict = None , title = '' , ylabel = '' , kruskal_test = False , figsize = (4, 4) , x_ticks_plot = False , legend_plot = True , bbox_to_anchor = (1, 0.55) , save = False , point_number = 5 , save_pathway = '' , sort = True , scatter_kwargs = None , ax = None , fontsize = 12 ) [source] #

adata (AnnData object): The data object containing the information for plotting. groupby (str): The variable used for grouping the data. color (str): The variable used for coloring the data points. type_color_dict (dict): A dictionary mapping group categories to specific colors. title (str): The title for the plot. ylabel (str): The label for the y-axis. kruskal_test (bool): Whether to perform a Kruskal-Wallis test and display the p-value on the plot. figsize (tuple): The size of the plot figure in inches (width, height). x_ticks_plot (bool): Whether to display x-axis tick labels. legend_plot (bool): Whether to display a legend for the groups. bbox_to_anchor (tuple): The position of the legend bbox (x, y) in axes coordinates. save (bool): Whether to save the plot to a file. point_number (int): The number of data points to be plotted for each group. save_pathway (str): The file path for saving the plot (if save is True). sort (bool): Whether to sort the groups based on their mean values. scatter_kwargs (dict): Additional keyword arguments for customizing the scatter plot. ax (matplotlib.axes.Axes): A pre-existing axes object for plotting (optional).

Examples

ov.pl.single_group_boxplot(adata,groupby=’clusters’,

color=’Sox_aucell’, type_color_dict=dict(zip(pd.Categorical(adata.obs[‘clusters’]).categories, adata.uns[‘clusters_colors’])), x_ticks_plot=True, figsize=(5,4), kruskal_test=True, ylabel=’Sox_aucell’, legend_plot=False, bbox_to_anchor=(1,1), title=’Expression’, scatter_kwargs={‘alpha’:0.8,’s’:10,’marker’:’o’},

point_number=15, sort=False, save=False, )

Parameters :

-
groupby ( `str `(default: `'' `))

-
color ( `str `(default: `'' `))

-
type_color_dict ( `Optional `[ `dict `] (default: `None `))

-
title ( `str `(default: `'' `))

-
ylabel ( `str `(default: `'' `))

-
kruskal_test ( `bool `(default: `False `))

-
figsize ( `tuple `(default: `(4, 4) `))

-
x_ticks_plot ( `bool `(default: `False `))

-
legend_plot ( `bool `(default: `True `))

-
bbox_to_anchor ( `tuple `(default: `(1, 0.55) `))

-
save ( `bool `(default: `False `))

-
point_number ( `int `(default: `5 `))

-
save_pathway ( `str `(default: `'' `))

-
sort ( `bool `(default: `True `))

-
scatter_kwargs ( `Optional `[ `dict `] (default: `None `))
