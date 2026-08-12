# omicverse.pl.add_density_contour #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.add_density_contour`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.add_density_contour.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Add KDE-based density contours to an existing matplotlib plot.

## Signature

```text
omicverse.pl. add_density_contour ( ax , embeddings , weights , levels = 'quantile' , n_quantiles = 5 , bw_adjust = 0.3 , cmap_contour = 'Greys' , linewidth = 1.0 , zorder = 10 , fill = False , alpha = 0.4 )
```

## Parameters

- `ax`: – matplotlib.axes.Axes object to draw contours on
- `embeddings`: – 2D coordinate array with shape (n_cells, 2)
- `weights`: – 1D weight array for KDE, will be min-max normalized
- `levels`: (default: 'quantile' ) – Contour level specification - ‘quantile’ or list of values (‘quantile’)
- `n_quantiles`: (default: 5 ) – Number of quantile levels when levels=’quantile’ (5)
- `bw_adjust`: (default: 0.3 ) – Bandwidth adjustment factor for KDE (0.3)
- `cmap_contour`: (default: 'Greys' ) – Colormap for contour lines (‘Greys’)
- `linewidth`: (default: 1.0 ) – Width of contour lines (1.0)
- `zorder`: (default: 10 ) – Drawing order for contours (10)
- `fill`: (default: False ) – Whether to fill contours (False for lines, True for filled)
- `alpha`: (default: 0.4 ) – Transparency for filled contours (0.4)

## Full Documentation

# omicverse.pl.add_density_contour #

omicverse.pl. add_density_contour ( ax , embeddings , weights , levels = 'quantile' , n_quantiles = 5 , bw_adjust = 0.3 , cmap_contour = 'Greys' , linewidth = 1.0 , zorder = 10 , fill = False , alpha = 0.4 ) [source] #

Add KDE-based density contours to an existing matplotlib plot.

Parameters :

-
ax – matplotlib.axes.Axes object to draw contours on

-
embeddings – 2D coordinate array with shape (n_cells, 2)

-
weights – 1D weight array for KDE, will be min-max normalized

-
levels (default: `'quantile' `) – Contour level specification - ‘quantile’ or list of values (‘quantile’)

-
n_quantiles (default: `5 `) – Number of quantile levels when levels=’quantile’ (5)

-
bw_adjust (default: `0.3 `) – Bandwidth adjustment factor for KDE (0.3)

-
cmap_contour (default: `'Greys' `) – Colormap for contour lines (‘Greys’)

-
linewidth (default: `1.0 `) – Width of contour lines (1.0)

-
zorder (default: `10 `) – Drawing order for contours (10)

-
fill (default: `False `) – Whether to fill contours (False for lines, True for filled)

-
alpha (default: `0.4 `) – Transparency for filled contours (0.4)

Returns :

matplotlib contour object for potential colorbar addition

Return type :

cs
