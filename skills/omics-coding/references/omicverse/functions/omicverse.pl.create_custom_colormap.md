# omicverse.pl.create_custom_colormap #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.create_custom_colormap`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.create_custom_colormap.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Build a transparent-to-opaque LinearSegmentedColormap of a single colour.

## Signature

```text
omicverse.pl. create_custom_colormap ( cell_color , * , name = 'custom_transparent' , N = 100 )
```

## Parameters

- `cell_color`: ( str or tuple ) – Base colour — any matplotlib-recognised spec (hex, name, RGB tuple).
- `name`: (str, default 'custom_transparent' ) – Registered colormap name.
- `N`: ( int , default 100 ) – Number of quantisation levels in the returned colormap.

## Full Documentation

# omicverse.pl.create_custom_colormap #

omicverse.pl. create_custom_colormap ( cell_color , * , name = 'custom_transparent' , N = 100 ) [source] #

Build a transparent-to-opaque LinearSegmentedColormap of a single colour.

The colormap maps value 0 to the given colour at alpha 0 (fully transparent) and value 1 to alpha 1 (fully opaque), keeping the RGB channels constant. Useful for overlaying one cell-type / marker density over a morphology image without masking it — low values disappear into the background, high values pop in the base colour.

Parameters :

-
cell_color ( str or tuple ) – Base colour — any matplotlib-recognised spec (hex, name, RGB tuple).

-
name (str, default `'custom_transparent' `) – Registered colormap name.

-
N ( int , default 100 ) – Number of quantisation levels in the returned colormap.

Returns :

A colormap whose alpha channel grows linearly from 0 to 1.

Return type :

matplotlib.colors.LinearSegmentedColormap
