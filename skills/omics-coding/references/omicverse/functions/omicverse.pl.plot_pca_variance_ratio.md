# omicverse.pl.plot_pca_variance_ratio #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.plot_pca_variance_ratio`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.plot_pca_variance_ratio.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot PCA variance ratio to determine optimal number of principal components.

## Signature

```text
omicverse.pl. plot_pca_variance_ratio ( adata , use_rep = 'scaled|original|pca_var_ratios' , n_pcs = 30 , log = False , show = None , save = None )
```

## Parameters

- `adata`: ( AnnData object containing PCA results. )
- `use_rep`: ( Key in adata.uns for variance ratios. Default: 'scaled | original | pca_var_ratios'. )
- `n_pcs`: ( Number of principal components to plot. Default: 30. )
- `log`: ( Whether to use logarithmic scale. Default: False. )
- `show`: ( Show the figure. Default: None. )
- `save`: ( Save the figure to file. Default: None. )

## Full Documentation

# omicverse.pl.plot_pca_variance_ratio #

omicverse.pl. plot_pca_variance_ratio ( adata , use_rep = 'scaled|original|pca_var_ratios' , n_pcs = 30 , log = False , show = None , save = None ) [source] #

Plot PCA variance ratio to determine optimal number of principal components.

Parameters :

-
adata ( AnnData object containing PCA results. )

-
use_rep ( Key in adata.uns for variance ratios. Default: 'scaled | original | pca_var_ratios'. )

-
n_pcs ( Number of principal components to plot. Default: 30. )

-
log ( Whether to use logarithmic scale. Default: False. )

-
show ( Show the figure. Default: None. )

-
save ( Save the figure to file. Default: None. )

Returns :

-
None: Displays or saves the PCA variance ratio plot.

-
Examples – >>> import omicverse as ov >>> # Basic PCA variance ratio plot >>> ov.pp.pca(adata, n_pcs=50) >>> ov.utils.plot_pca_variance_ratio(adata, n_pcs=30) >>> # Custom variance ratios with log scale >>> ov.utils.plot_pca_variance_ratio(adata, n_pcs=50, log=True)
