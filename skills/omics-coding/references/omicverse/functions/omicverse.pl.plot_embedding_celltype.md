# omicverse.pl.plot_embedding_celltype #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.plot_embedding_celltype`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.plot_embedding_celltype.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Create combined embedding plot with cell type legend and counts.

## Signature

```text
omicverse.pl. plot_embedding_celltype ( adata , figsize = (6, 4) , basis = 'umap' , celltype_key = 'major_celltype' , title = None , celltype_range = (2, 9) , embedding_range = (3, 10) , xlim = -1000 )
```

## Parameters

- `adata`: ( AnnData object )
- `figsize`: ( Figure size ( ( 6 , 4 ) ) )
- `basis`: ( Embedding basis name ( 'umap' ) )
- `celltype_key`: ( Column name for cell types ( 'major_celltype' ) )
- `title`: ( Plot title ( None ) )
- `celltype_range`: ( Grid range for cell type panel ( ( 2 , 9 ) ) )
- `embedding_range`: ( Grid range for embedding panel ( ( 3 , 10 ) ) )
- `xlim`: ( X-axis limit for counts ( -1000 ) )

## Full Documentation

# omicverse.pl.plot_embedding_celltype #

omicverse.pl. plot_embedding_celltype ( adata , figsize = (6, 4) , basis = 'umap' , celltype_key = 'major_celltype' , title = None , celltype_range = (2, 9) , embedding_range = (3, 10) , xlim = -1000 ) [source] #

Create combined embedding plot with cell type legend and counts.

Parameters :

-
adata ( AnnData object )

-
figsize ( Figure size ( ( 6 , 4 ) ) )

-
basis ( Embedding basis name ( 'umap' ) )

-
celltype_key ( Column name for cell types ( 'major_celltype' ) )

-
title ( Plot title ( None ) )

-
celltype_range ( Grid range for cell type panel ( ( 2 , 9 ) ) )

-
embedding_range ( Grid range for embedding panel ( ( 3 , 10 ) ) )

-
xlim ( X-axis limit for counts ( -1000 ) )

Returns :

Tuple of (figure, [embedding_axis, celltype_axis])
