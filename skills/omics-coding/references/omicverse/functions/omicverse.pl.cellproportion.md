# omicverse.pl.cellproportion #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.cellproportion`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.cellproportion.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot cell proportion of each cell type in each visual cluster.

## Signature

```text
omicverse.pl. cellproportion ( adata , celltype_clusters , groupby , groupby_li = None , figsize = (4, 6) , ticks_fontsize = 12 , labels_fontsize = 12 , ax = None , legend = False , legend_awargs = None , transpose = False , save = None , ** kwargs )
```

## Parameters

- `adata`: ( AnnData ) – AnnData object.
- `celltype_clusters`: ( str ) – Cell type clusters.
- `groupby`: ( str ) – Visual clusters.
- `groupby_li`: (default: None ) – Visual cluster list. (None)
- `figsize`: ( tuple (default: (4, 6) )) – Figure size. ((4,6))
- `ticks_fontsize`: ( int (default: 12 )) – Ticks fontsize. (12)
- `labels_fontsize`: ( int (default: 12 )) – Labels fontsize. (12)
- `ax`: (default: None ) – Matplotlib axes object. (None)
- `legend`: ( bool (default: False )) – Whether to show legend. (False)
- `legend_awargs`: (default: None ) – Legend arguments. ({‘ncol’:1})
- `transpose`: ( bool (default: False )) – Whether to transpose the plot (horizontal bars). (False)
- `save`: Detected from function signature; no parameter description detected.
- `**kwargs`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.pl.cellproportion #

omicverse.pl. cellproportion ( adata , celltype_clusters , groupby , groupby_li = None , figsize = (4, 6) , ticks_fontsize = 12 , labels_fontsize = 12 , ax = None , legend = False , legend_awargs = None , transpose = False , save = None , ** kwargs ) [source] #

Plot cell proportion of each cell type in each visual cluster.

Parameters :

-
adata ( `AnnData `) – AnnData object.

-
celltype_clusters ( `str `) – Cell type clusters.

-
groupby ( `str `) – Visual clusters.

-
groupby_li (default: `None `) – Visual cluster list. (None)

-
figsize ( `tuple `(default: `(4, 6) `)) – Figure size. ((4,6))

-
ticks_fontsize ( `int `(default: `12 `)) – Ticks fontsize. (12)

-
labels_fontsize ( `int `(default: `12 `)) – Labels fontsize. (12)

-
ax (default: `None `) – Matplotlib axes object. (None)

-
legend ( `bool `(default: `False `)) – Whether to show legend. (False)

-
legend_awargs (default: `None `) – Legend arguments. ({‘ncol’:1})

-
transpose ( `bool `(default: `False `)) – Whether to transpose the plot (horizontal bars). (False)

Returns :

None

Accepts a `pandas.DataFrame `of per-observation metadata wherever an `AnnData `is expected — the frame is used as `.obs `. See `omicverse.pl.accepts_frame() `.

Parameters :

save ( `Optional `[ `str `] (default: `None `))
