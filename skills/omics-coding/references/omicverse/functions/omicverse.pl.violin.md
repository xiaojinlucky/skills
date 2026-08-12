# omicverse.pl.violin #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.violin`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.violin.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Enhanced violin plot compatible with omicverse’s interface.

## Signature

```text
omicverse.pl. violin ( adata , keys , groupby = None , * , log = False , use_raw = None , stripplot = True , jitter = True , size = 1 , layer = None , density_norm = 'width' , order = None , multi_panel = None , xlabel = '' , ylabel = None , rotation = None , show = None , save = None , ax = None , enhanced_style = True , show_means = False , show_boxplot = False , add_box = False , comparisons = None , jitter_method = 'uniform' , jitter_alpha = 0.4 , violin_alpha = 0.8 , rasterized = False , background_color = 'white' , alternating_background = True , alternating_background_colors = ('white', 'e8e8e8') , use_group_colors_background = False , background_lighten_amount = 0.8 , spine_color = 'b4aea9' , grid_lines = True , statistical_tests = False , custom_colors = None , figsize = None , fontsize = 13 , ticks_fontsize = None , verbose = False , hue = None , hue_order = None , split = False , cut = None , clip = None , inner = None , orient = 'v' , scale = None , width = 0.8 , palette = None , test = None , correction = 'holm' , annot_style = 'star' , hide_ns = False , return_stats = False , ** kwds )
```

## Parameters

- `adata`: ( AnnData ) – AnnData. Annotated data matrix.
- `keys`: ( Union [ str , Sequence [ str ]] ) – str | Sequence[str]. Keys for accessing variables of .var_names or fields of .obs .
- `groupby`: ( Optional [ str ] (default: None )) – str | None. The key of the observation grouping to consider. (None)
- `log`: ( bool (default: False )) – bool. Plot on logarithmic axis. (False)
- `use_raw`: ( Optional [ bool ] (default: None )) – bool | None. Whether to use raw attribute of adata . Defaults to True if .raw is present. (None)
- `stripplot`: ( bool (default: True )) – bool. Add a stripplot on top of the violin plot. (True)
- `jitter`: ( Union [ float , bool ] (default: True )) – float | bool. Add jitter to the stripplot (only when stripplot is True). (True)
- `size`: ( int (default: 1 )) – int. Size of the jitter points. (1)
- `layer`: ( Optional [ str ] (default: None )) – str | None. Name of the AnnData object layer that wants to be plotted. (None)
- `density_norm`: ( Literal [ 'area' , 'count' , 'width' ] (default: 'width' )) – str. The method used to scale the width of each violin. If ‘width’ (the default), each violin will have the same width. If ‘area’, each violin will have the same area. If ‘count’, a violin’s width corresponds to the number of observations. (‘width’)
- `order`: ( Optional [ Sequence [ str ]] (default: None )) – Sequence[str] | None. Order in which to show the categories. (None)
- `multi_panel`: ( Optional [ bool ] (default: None )) – bool | None. Display keys in multiple panels also when groupby is not None . (None)
- `xlabel`: ( str (default: '' )) – str. Label of the x axis. (‘’)
- `ylabel`: ( Union [ str , Sequence [ str ], None ] (default: None )) – str | Sequence[str] | None. Label of the y axis. (None)
- `rotation`: ( Optional [ float ] (default: None )) – float | None. Rotation of xtick labels. (None)
- `show`: ( Optional [ bool ] (default: None )) – bool | None. Whether to show the plot. (None)
- `save`: ( Union [ str , bool , None ] (default: None )) – bool | str | None. Path to save the figure. (None)
- `ax`: ( Optional [ Axes ] (default: None )) – Axes | None. A matplotlib axes object. (None)
- `enhanced_style`: ( bool (default: True )) – bool. Whether to apply enhanced styling. (True)
- `show_means`: ( bool (default: False )) – bool. Whether to show mean values with annotations. (False)
- `show_boxplot`: ( bool (default: False )) – bool. Whether to overlay box plots on violins. (False)
- `jitter_method`: ( str (default: 'uniform' )) – str. Method for jittering: ‘uniform’ or ‘t_dist’. (‘uniform’)
- `jitter_alpha`: ( float (default: 0.4 )) – float. Transparency of jittered points. (0.4)
- `violin_alpha`: ( float (default: 0.8 )) – float. Transparency of violin plots. (0.8)
- `background_color`: ( str (default: 'white' )) – str. Background color of the plot. (‘white’)
- `alternating_background`: ( bool (default: True )) – bool. Whether to add background bands using each group’s lightened color. (True)
- `background_lighten_amount`: ( float (default: 0.8 )) – float. How much to lighten each group color for its background band (0=original, 1=white). (0.8)
- `spine_color`: ( str (default: '#b4aea9' )) – str. Color of plot spines. (‘#b4aea9’)
- `grid_lines`: ( bool (default: True )) – bool. Whether to show horizontal grid lines. (True)
- `statistical_tests`: ( Union [ bool , str , List [ str ]] (default: False )) – bool | str | List[str]. Statistical tests to perform. Options: False (no tests), True (auto-select), ‘wilcox’, ‘ttest’, ‘anova’, ‘kruskal’, ‘mannwhitney’, or list of methods. (False)
- `custom_colors`: ( Optional [ Sequence [ str ]] (default: None )) – Sequence[str] | None. Custom colors for groups. (None)
- `figsize`: ( Optional [ tuple ] (default: None )) – tuple | None. Figure size (width, height). (None)
- `fontsize`: (default: 13 ) – int. Font size for labels and ticks. (13)
- `ticks_fontsize`: (default: None ) – int | None. Font size for axis ticks. If None, uses fontsize-1. (None)
- `**kwds`: – Additional keyword arguments passed to violinplot.
- `add_box`: Detected from function signature; no parameter description detected.
- `comparisons`: Detected from function signature; no parameter description detected.
- `rasterized`: Detected from function signature; no parameter description detected.
- `alternating_background_colors`: Detected from function signature; no parameter description detected.
- `use_group_colors_background`: Detected from function signature; no parameter description detected.
- `verbose`: Detected from function signature; no parameter description detected.
- `hue`: Detected from function signature; no parameter description detected.
- `hue_order`: Detected from function signature; no parameter description detected.
- `split`: Detected from function signature; no parameter description detected.
- `cut`: Detected from function signature; no parameter description detected.
- `clip`: Detected from function signature; no parameter description detected.
- `inner`: Detected from function signature; no parameter description detected.
- `orient`: Detected from function signature; no parameter description detected.
- `scale`: Detected from function signature; no parameter description detected.
- `width`: Detected from function signature; no parameter description detected.
- `palette`: Detected from function signature; no parameter description detected.
- `test`: Detected from function signature; no parameter description detected.
- `correction`: Detected from function signature; no parameter description detected.
- `annot_style`: Detected from function signature; no parameter description detected.
- `hide_ns`: Detected from function signature; no parameter description detected.
- `return_stats`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.pl.violin #

omicverse.pl. violin ( adata , keys , groupby = None , * , log = False , use_raw = None , stripplot = True , jitter = True , size = 1 , layer = None , density_norm = 'width' , order = None , multi_panel = None , xlabel = '' , ylabel = None , rotation = None , show = None , save = None , ax = None , enhanced_style = True , show_means = False , show_boxplot = False , add_box = False , comparisons = None , jitter_method = 'uniform' , jitter_alpha = 0.4 , violin_alpha = 0.8 , rasterized = False , background_color = 'white' , alternating_background = True , alternating_background_colors = ('white', '#e8e8e8') , use_group_colors_background = False , background_lighten_amount = 0.8 , spine_color = '#b4aea9' , grid_lines = True , statistical_tests = False , custom_colors = None , figsize = None , fontsize = 13 , ticks_fontsize = None , verbose = False , hue = None , hue_order = None , split = False , cut = None , clip = None , inner = None , orient = 'v' , scale = None , width = 0.8 , palette = None , test = None , correction = 'holm' , annot_style = 'star' , hide_ns = False , return_stats = False , ** kwds ) [source] #

Enhanced violin plot compatible with omicverse’s interface.

This function provides all the functionality of omicverse’s violin plot with additional customization options for enhanced visualization, implemented using pure matplotlib.

Parameters :

-
adata ( `AnnData `) – AnnData. Annotated data matrix.

-
keys ( `Union `[ `str `, `Sequence `[ `str `]] ) – str | Sequence[str]. Keys for accessing variables of .var_names or fields of .obs .

-
groupby ( `Optional `[ `str `] (default: `None `)) – str | None. The key of the observation grouping to consider. (None)

-
log ( `bool `(default: `False `)) – bool. Plot on logarithmic axis. (False)

-
use_raw ( `Optional `[ `bool `] (default: `None `)) – bool | None. Whether to use raw attribute of adata . Defaults to True if .raw is present. (None)

-
stripplot ( `bool `(default: `True `)) – bool. Add a stripplot on top of the violin plot. (True)

-
jitter ( `Union `[ `float `, `bool `] (default: `True `)) – float | bool. Add jitter to the stripplot (only when stripplot is True). (True)

-
size ( `int `(default: `1 `)) – int. Size of the jitter points. (1)

-
layer ( `Optional `[ `str `] (default: `None `)) – str | None. Name of the AnnData object layer that wants to be plotted. (None)

-
density_norm ( `Literal `[ `'area' `, `'count' `, `'width' `] (default: `'width' `)) – str. The method used to scale the width of each violin. If ‘width’ (the default), each violin will have the same width. If ‘area’, each violin will have the same area. If ‘count’, a violin’s width corresponds to the number of observations. (‘width’)

-
order ( `Optional `[ `Sequence `[ `str `]] (default: `None `)) – Sequence[str] | None. Order in which to show the categories. (None)

-
multi_panel ( `Optional `[ `bool `] (default: `None `)) – bool | None. Display keys in multiple panels also when groupby is not None . (None)

-
xlabel ( `str `(default: `'' `)) – str. Label of the x axis. (‘’)

-
ylabel ( `Union `[ `str `, `Sequence `[ `str `], `None `] (default: `None `)) – str | Sequence[str] | None. Label of the y axis. (None)

-
rotation ( `Optional `[ `float `] (default: `None `)) – float | None. Rotation of xtick labels. (None)

-
show ( `Optional `[ `bool `] (default: `None `)) – bool | None. Whether to show the plot. (None)

-
save ( `Union `[ `str `, `bool `, `None `] (default: `None `)) – bool | str | None. Path to save the figure. (None)

-
ax ( `Optional `[ `Axes `] (default: `None `)) – Axes | None. A matplotlib axes object. (None)

-
enhanced_style ( `bool `(default: `True `)) – bool. Whether to apply enhanced styling. (True)

-
show_means ( `bool `(default: `False `)) – bool. Whether to show mean values with annotations. (False)

-
show_boxplot ( `bool `(default: `False `)) – bool. Whether to overlay box plots on violins. (False)

-
jitter_method ( `str `(default: `'uniform' `)) – str. Method for jittering: ‘uniform’ or ‘t_dist’. (‘uniform’)

-
jitter_alpha ( `float `(default: `0.4 `)) – float. Transparency of jittered points. (0.4)

-
violin_alpha ( `float `(default: `0.8 `)) – float. Transparency of violin plots. (0.8)

-
background_color ( `str `(default: `'white' `)) – str. Background color of the plot. (‘white’)

-
alternating_background ( `bool `(default: `True `)) – bool. Whether to add background bands using each group’s lightened color. (True)

-
background_lighten_amount ( `float `(default: `0.8 `)) – float. How much to lighten each group color for its background band (0=original, 1=white). (0.8)

-
spine_color ( `str `(default: `'#b4aea9' `)) – str. Color of plot spines. (‘#b4aea9’)

-
grid_lines ( `bool `(default: `True `)) – bool. Whether to show horizontal grid lines. (True)

-
statistical_tests ( `Union `[ `bool `, `str `, `List `[ `str `]] (default: `False `)) – bool | str | List[str]. Statistical tests to perform. Options: False (no tests), True (auto-select), ‘wilcox’, ‘ttest’, ‘anova’, ‘kruskal’, ‘mannwhitney’, or list of methods. (False)

-
custom_colors ( `Optional `[ `Sequence `[ `str `]] (default: `None `)) – Sequence[str] | None. Custom colors for groups. (None)

-
figsize ( `Optional `[ `tuple `] (default: `None `)) – tuple | None. Figure size (width, height). (None)

-
fontsize (default: `13 `) – int. Font size for labels and ticks. (13)

-
ticks_fontsize (default: `None `) – int | None. Font size for axis ticks. If None, uses fontsize-1. (None)

-
**kwds – Additional keyword arguments passed to violinplot.

Returns :

matplotlib.axes.Axes | None. A matplotlib axes object if ax is None else None .

Return type :

ax

Accepts a `pandas.DataFrame `of per-observation metadata wherever an `AnnData `is expected — the frame is used as `.obs `. See `omicverse.pl.accepts_frame() `.

Parameters :

-
add_box ( `bool `(default: `False `))

-
comparisons ( `Optional `[ `List `] (default: `None `))

-
rasterized ( `bool `(default: `False `))

-
alternating_background_colors ( `Sequence `[ `str `] (default: `('white', '#e8e8e8') `))

-
use_group_colors_background ( `bool `(default: `False `))

-
verbose ( `bool `(default: `False `))

-
hue ( `Optional `[ `str `] (default: `None `))

-
hue_order ( `Optional `[ `Sequence `[ `str `]] (default: `None `))

-
split ( `bool `(default: `False `))

-
cut ( `Optional `[ `float `] (default: `None `))

-
clip ( `Optional `[ `Tuple `[ `Optional `[ `float `], `Optional `[ `float `]]] (default: `None `))

-
inner ( `Optional `[ `str `] (default: `None `))

-
orient ( `str `(default: `'v' `))

-
scale ( `Optional `[ `str `] (default: `None `))

-
width ( `float `(default: `0.8 `))

-
palette ( `Optional `[ `Any `] (default: `None `))

-
test ( `Optional `[ `str `] (default: `None `))

-
correction ( `Optional `[ `str `] (default: `'holm' `))

-
annot_style ( `str `(default: `'star' `))

-
hide_ns ( `bool `(default: `False `))

-
return_stats ( `bool `(default: `False `))
