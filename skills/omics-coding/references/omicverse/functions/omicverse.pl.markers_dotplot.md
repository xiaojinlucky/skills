# omicverse.pl.markers_dotplot #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.markers_dotplot`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.markers_dotplot.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Dot plot of marker genes — clean drop-in for rank_genes_groups_dotplot() .

## Signature

```text
omicverse.pl. markers_dotplot ( adata , groupby = None , key = None , n_genes = 5 , groups = None , standard_scale = 'var' , cmap = 'Spectral_r' , dendrogram = False , min_logfoldchange = None , use_raw = None , layer = None , figsize = None , show = None , save = None , return_fig = False , ** kwds )
```

## Parameters

- `adata`: ( AnnData ) – Annotated data matrix.
- `groupby`: ( str or None , default=None ) – Key in adata.obs to group by. If None , uses adata.uns[key]['params']['groupby'] .
- `key`: ( str or None , default=None ) – Key in adata.uns containing rank_genes_groups results.
- `n_genes`: ( int , default=5 ) – Number of top marker genes shown per group.
- `groups`: ( str or Sequence [ str ] or None , default=None ) – Subset of groups to include.
- `standard_scale`: ( {'var' , 'group'} or None , default='var' ) – Standardization mode for color values.
- `cmap`: ( Colormap or str or None , default='Spectral_r' ) – Colormap for mean expression.
- `dendrogram`: ( bool , default=False ) – Whether to include a dendrogram.
- `min_logfoldchange`: ( float or None , default=None ) – Minimum log-fold-change threshold for marker inclusion.
- `use_raw`: ( bool or None , default=None ) – Whether to use adata.raw values.
- `layer`: ( str or None , default=None ) – Layer used for expression values.
- `figsize`: ( tuple [ float , float ] or None , default=None ) – Figure size in inches.
- `show`: ( bool or None , default=None ) – Whether to display the figure.
- `save`: ( str or bool or None , default=None ) – Save option/path.
- `return_fig`: ( bool , default=False ) – Whether to return the generated plot object.
- `**kwds`: – Additional keyword arguments forwarded to dotplot() .
- `Returns`: – Figure or axes object when return_fig=True or show=False ; None otherwise.
- `Examples`: – >>> import omicverse as ov >>> ov . single . find_markers ( adata , groupby = 'leiden' , method = 'cosg' ) >>> ov . pl . markers_dotplot ( adata , groupby = 'leiden' , n_genes = 5 ) >>> # Using wilcoxon results stored under a different key >>> ov . single . find_markers ( adata , groupby = 'leiden' , method = 'wilcoxon' , ... key_added = 'wilcoxon_markers' ) >>> ov . pl . markers_dotplot ( adata , groupby = 'leiden' , key = 'wilcoxon_markers' )

## Full Documentation

# omicverse.pl.markers_dotplot #

omicverse.pl. markers_dotplot ( adata , groupby = None , key = None , n_genes = 5 , groups = None , standard_scale = 'var' , cmap = 'Spectral_r' , dendrogram = False , min_logfoldchange = None , use_raw = None , layer = None , figsize = None , show = None , save = None , return_fig = False , ** kwds ) [source] #

Dot plot of marker genes — clean drop-in for `rank_genes_groups_dotplot() `.

Wraps `rank_genes_groups_dotplot() `with more convenient defaults: `standard_scale='var' `, `cmap='Spectral_r' `, and `dendrogram=False `.

Parameters :

-
adata ( AnnData ) – Annotated data matrix.

-
groupby ( str or None , default=None ) – Key in `adata.obs `to group by. If `None `, uses `adata.uns[key]['params']['groupby'] `.

-
key ( str or None , default=None ) – Key in `adata.uns `containing `rank_genes_groups `results.

-
n_genes ( int , default=5 ) – Number of top marker genes shown per group.

-
groups ( str or Sequence [ str ] or None , default=None ) – Subset of groups to include.

-
standard_scale ( {'var' , 'group'} or None , default='var' ) – Standardization mode for color values.

-
cmap ( Colormap or str or None , default='Spectral_r' ) – Colormap for mean expression.

-
dendrogram ( bool , default=False ) – Whether to include a dendrogram.

-
min_logfoldchange ( float or None , default=None ) – Minimum log-fold-change threshold for marker inclusion.

-
use_raw ( bool or None , default=None ) – Whether to use `adata.raw `values.

-
layer ( str or None , default=None ) – Layer used for expression values.

-
figsize ( tuple [ float , float ] or None , default=None ) – Figure size in inches.

-
show ( bool or None , default=None ) – Whether to display the figure.

-
save ( str or bool or None , default=None ) – Save option/path.

-
return_fig ( bool , default=False ) – Whether to return the generated plot object.

-
**kwds – Additional keyword arguments forwarded to `dotplot() `.

-
Returns – Figure or axes object when `return_fig=True `or `show=False `; `None `otherwise.

-
Examples –

```text
>>> import omicverse as ov
>>> ov.single.find_markers(adata, groupby='leiden', method='cosg')
>>> ov.pl.markers_dotplot(adata, groupby='leiden', n_genes=5)
>>> # Using wilcoxon results stored under a different key
>>> ov.single.find_markers(adata, groupby='leiden', method='wilcoxon',
... key_added='wilcoxon_markers')
>>> ov.pl.markers_dotplot(adata, groupby='leiden', key='wilcoxon_markers')

```
