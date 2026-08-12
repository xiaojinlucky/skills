# omicverse.bulk2single.bulk2single_plot_correlation #

- Package: omicverse
- Language: Python
- Function: `omicverse.bulk2single.bulk2single_plot_correlation`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.bulk2single.bulk2single_plot_correlation.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot correlation matrix between reference and generated single-cell data.

## Signature

```text
omicverse.bulk2single. bulk2single_plot_correlation ( single_data , generate_single_data , celltype_key , return_table = False , figsize = (6, 6) , cmap = 'RdBu_r' )
```

## Parameters

- `single_data`: ( anndata.AnnData ) – Original single-cell reference AnnData.
- `generate_single_data`: ( anndata.AnnData ) – Generated single-cell AnnData for comparison.
- `celltype_key`: ( str ) – Cell-type column used to group cells before correlation.
- `return_table`: ( bool ) – If True , return numeric correlation matrix instead of plotting.
- `figsize`: ( tuple ) – Figure size passed to matplotlib.
- `cmap`: ( str ) – Colormap used for heatmap rendering.

## Full Documentation

# omicverse.bulk2single.bulk2single_plot_correlation #

omicverse.bulk2single. bulk2single_plot_correlation ( single_data , generate_single_data , celltype_key , return_table = False , figsize = (6, 6) , cmap = 'RdBu_r' ) [source] #

Plot correlation matrix between reference and generated single-cell data.

Compares expression patterns of cell types between original single-cell reference and bulk2single generated data using marker gene correlations.

Parameters :

-
single_data ( anndata.AnnData ) – Original single-cell reference AnnData.

-
generate_single_data ( anndata.AnnData ) – Generated single-cell AnnData for comparison.

-
celltype_key ( str ) – Cell-type column used to group cells before correlation.

-
return_table ( bool ) – If `True `, return numeric correlation matrix instead of plotting.

-
figsize ( tuple ) – Figure size passed to matplotlib.

-
cmap ( str ) – Colormap used for heatmap rendering.

Returns :

Correlation matrix when `return_table=True `; otherwise figure and axes.

Return type :

numpy.ndarray or Tuple[ matplotlib.figure.Figure , matplotlib.axes.Axes ]
