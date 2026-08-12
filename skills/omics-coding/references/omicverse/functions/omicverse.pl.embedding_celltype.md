# omicverse.pl.embedding_celltype #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.embedding_celltype`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.embedding_celltype.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot embedding with celltype color by omicverse.

## Signature

```text
omicverse.pl. embedding_celltype ( adata , figsize = (6, 4) , basis = 'umap' , celltype_key = 'major_celltype' , title = None , celltype_range = (2, 9) , embedding_range = (3, 10) , xlim = -1000 )
```

## Parameters

- `adata`: ( AnnData ) – AnnData object
- `figsize`: ( tuple (default: (6, 4) )) – tuple, optional (default=(6,4)) Figure size
- `basis`: ( str (default: 'umap' )) – str, optional (default=’umap’) Embedding method
- `celltype_key`: ( str (default: 'major_celltype' )) – str, optional (default=’major_celltype’) Celltype key in adata.obs
- `title`: ( Optional [ str ] (default: None )) – str, optional (default=None) Figure title
- `celltype_range`: ( tuple (default: (2, 9) )) – tuple, optional (default=(2,9)) Celltype range to plot
- `embedding_range`: ( tuple (default: (3, 10) )) – tuple, optional (default=(3,10)) Embedding range to plot
- `xlim`: ( int (default: -1000 )) – int, optional (default=-1000) X axis limit

## Full Documentation

# omicverse.pl.embedding_celltype #

omicverse.pl. embedding_celltype ( adata , figsize = (6, 4) , basis = 'umap' , celltype_key = 'major_celltype' , title = None , celltype_range = (2, 9) , embedding_range = (3, 10) , xlim = -1000 ) [source] #

Plot embedding with celltype color by omicverse.

Parameters :

-
adata ( `AnnData `) – AnnData object

-
figsize ( `tuple `(default: `(6, 4) `)) – tuple, optional (default=(6,4)) Figure size

-
basis ( `str `(default: `'umap' `)) – str, optional (default=’umap’) Embedding method

-
celltype_key ( `str `(default: `'major_celltype' `)) – str, optional (default=’major_celltype’) Celltype key in adata.obs

-
title ( `Optional `[ `str `] (default: `None `)) – str, optional (default=None) Figure title

-
celltype_range ( `tuple `(default: `(2, 9) `)) – tuple, optional (default=(2,9)) Celltype range to plot

-
embedding_range ( `tuple `(default: `(3, 10) `)) – tuple, optional (default=(3,10)) Embedding range to plot

-
xlim ( `int `(default: `-1000 `)) – int, optional (default=-1000) X axis limit

Returns :

figure and axis ax: axis

Return type :

fig
