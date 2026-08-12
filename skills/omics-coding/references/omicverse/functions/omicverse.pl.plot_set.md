# omicverse.pl.plot_set #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.plot_set`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.plot_set.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Configure plotting settings for OmicVerse.

## Signature

```text
omicverse.pl. plot_set ( verbosity = 3 , dpi = 80 , facecolor = 'white' , font_path = None , ipython_format = 'retina' , dpi_save = 300 , transparent = None , scanpy = True , fontsize = 14 , color_map = None , figsize = None , vector_friendly = True , show_monitor = True )
```

## Parameters

- `verbosity`: ( int ) – Scanpy verbosity level.
- `dpi`: ( int ) – Figure DPI for on-screen rendering.
- `facecolor`: ( str ) – Figure and axes background color.
- `font_path`: ( str or None ) – Optional custom font path or keyword (for example 'arial' ).
- `ipython_format`: ( str ) – Inline backend display format in IPython.
- `dpi_save`: ( int ) – DPI for saved figures.
- `transparent`: ( bool or None ) – Whether saved figures use transparent background.
- `scanpy`: ( bool ) – Whether to apply scanpy rcParams preset.
- `fontsize`: ( int ) – Global font size used in plotting styles.
- `color_map`: ( str or None ) – Default colormap.
- `figsize`: ( int or None ) – Default figure size; scalar values are converted to square tuple.
- `vector_friendly`: ( bool ) – Whether to prefer vector-friendly rasterization behavior.
- `show_monitor`: ( bool ) – Whether runtime monitor messages are shown.

## Full Documentation

# omicverse.pl.plot_set #

omicverse.pl. plot_set ( verbosity = 3 , dpi = 80 , facecolor = 'white' , font_path = None , ipython_format = 'retina' , dpi_save = 300 , transparent = None , scanpy = True , fontsize = 14 , color_map = None , figsize = None , vector_friendly = True , show_monitor = True ) [source] #

Configure plotting settings for OmicVerse.

Parameters :

-
verbosity ( int ) – Scanpy verbosity level.

-
dpi ( int ) – Figure DPI for on-screen rendering.

-
facecolor ( str ) – Figure and axes background color.

-
font_path ( str or None ) – Optional custom font path or keyword (for example `'arial' `).

-
ipython_format ( str ) – Inline backend display format in IPython.

-
dpi_save ( int ) – DPI for saved figures.

-
transparent ( bool or None ) – Whether saved figures use transparent background.

-
scanpy ( bool ) – Whether to apply scanpy rcParams preset.

-
fontsize ( int ) – Global font size used in plotting styles.

-
color_map ( str or None ) – Default colormap.

-
figsize ( int or None ) – Default figure size; scalar values are converted to square tuple.

-
vector_friendly ( bool ) – Whether to prefer vector-friendly rasterization behavior.

-
show_monitor ( bool ) – Whether runtime monitor messages are shown.

Returns :

Applies global plotting configuration.

Return type :

None
