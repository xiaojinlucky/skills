# omicverse.metabol.corr_network_plot #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.corr_network_plot`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.corr_network_plot.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Draw an edge DataFrame as a NetworkX spring-layout plot.

## Signature

```text
omicverse.metabol. corr_network_plot ( edges_df , * , ax = None , figsize = (6.5, 5.5) , layout = 'spring' , node_size = 70 , node_color = 'white' , node_edge_color = '34495e' , edge_width_scale = 2.5 , r_column = 'r' , seed = 0 , with_labels = True , label_font_size = 7 )
```

## Parameters

- `edges_df`: ( pd.DataFrame ) – Output of corr_network() — needs columns feature_a , feature_b and r (or whatever r_column points at).
- `layout`: ( {'spring' , 'circular' , 'kamada_kawai'} , default 'spring' ) – NetworkX layout algorithm.
- `node_size`: ( int (default: 70 )) – Standard styling. White-fill / dark-edge nodes read better in publications than filled ones because labels overlay legibly.
- `node_color`: ( str (default: 'white' )) – Standard styling. White-fill / dark-edge nodes read better in publications than filled ones because labels overlay legibly.
- `node_edge_color`: ( str (default: '#34495e' )) – Standard styling. White-fill / dark-edge nodes read better in publications than filled ones because labels overlay legibly.
- `edge_width_scale`: ( float ) – Multiplier on |r| for edge width (so |r|=1 is the thickest edge in the figure).
- `r_column`: ( str , default 'r' ) – Column to read for edge correlations. Switch to 'r_a' / 'r_b' if you’re plotting one half of a DGCA result.
- `with_labels`: ( bool , default True ) – Toggle metabolite labels.
- `label_font_size`: ( int , default 7 ) – Label size — reduce for dense graphs.
- `seed`: ( int ) – RNG seed for the spring-layout (only matters when layout='spring' ).
- `ax`: ( Optional [ Axes ] (default: None ))
- `figsize`: ( tuple [ float , float ] (default: (6.5, 5.5) ))

## Full Documentation

# omicverse.metabol.corr_network_plot #

omicverse.metabol. corr_network_plot ( edges_df , * , ax = None , figsize = (6.5, 5.5) , layout = 'spring' , node_size = 70 , node_color = 'white' , node_edge_color = '#34495e' , edge_width_scale = 2.5 , r_column = 'r' , seed = 0 , with_labels = True , label_font_size = 7 ) [source] #

Draw an edge DataFrame as a NetworkX spring-layout plot.

Renders the output of `omicverse.metabol.corr_network() `as a correlation graph: nodes are metabolites, edges are pairs whose Spearman / Pearson `|r| `exceeded the network’s threshold. Edge colour encodes the sign of the correlation (red = positive, blue = negative); edge width is proportional to `|r| `.

Parameters :

-
edges_df ( pd.DataFrame ) – Output of `corr_network() `— needs columns `feature_a `, `feature_b `and `r `(or whatever `r_column `points at).

-
layout ( {'spring' , 'circular' , 'kamada_kawai'} , default 'spring' ) – NetworkX layout algorithm.

-
node_size ( `int `(default: `70 `)) – Standard styling. White-fill / dark-edge nodes read better in publications than filled ones because labels overlay legibly.

-
node_color ( `str `(default: `'white' `)) – Standard styling. White-fill / dark-edge nodes read better in publications than filled ones because labels overlay legibly.

-
node_edge_color ( `str `(default: `'#34495e' `)) – Standard styling. White-fill / dark-edge nodes read better in publications than filled ones because labels overlay legibly.

-
edge_width_scale ( float ) – Multiplier on `|r| `for edge width (so `|r|=1 `is the thickest edge in the figure).

-
r_column ( str , default 'r' ) – Column to read for edge correlations. Switch to `'r_a' `/ `'r_b' `if you’re plotting one half of a DGCA result.

-
with_labels ( bool , default True ) – Toggle metabolite labels.

-
label_font_size ( int , default 7 ) – Label size — reduce for dense graphs.

-
seed ( int ) – RNG seed for the spring-layout (only matters when `layout='spring' `).

-
ax ( `Optional `[ `Axes `] (default: `None `))

-
figsize ( `tuple `[ `float `, `float `] (default: `(6.5, 5.5) `))

Returns :

-
(fig, ax) tuple. If `edges_df `is empty, draws a centred

-
”no edges” placeholder and returns the empty axes.
