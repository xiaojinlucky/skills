# omicverse.pl.add_palue #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.add_palue`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.add_palue.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Add p-value annotation with connecting line to a matplotlib plot.

## Signature

```text
omicverse.pl. add_palue ( ax , line_x1 , line_x2 , line_y , text_y , text , fontsize = 11 , fontcolor = '000000' , horizontalalignment = 'center' )
```

## Parameters

- `ax`: – matplotlib.axes.Axes object to add annotation to
- `line_x1`: – Starting x-coordinate of connecting line
- `line_x2`: – Ending x-coordinate of connecting line
- `line_y`: – Y-coordinate of connecting line
- `text_y`: – Y-offset for text placement above line
- `text`: – Text to display (typically p-value)
- `fontsize`: (default: 11 ) – Font size for text (11)
- `fontcolor`: (default: '#000000' ) – Color for line and text (‘#000000’)
- `horizontalalignment`: (default: 'center' ) – Text horizontal alignment (‘center’)

## Full Documentation

# omicverse.pl.add_palue #

omicverse.pl. add_palue ( ax , line_x1 , line_x2 , line_y , text_y , text , fontsize = 11 , fontcolor = '#000000' , horizontalalignment = 'center' ) [source] #

Add p-value annotation with connecting line to a matplotlib plot.

Parameters :

-
ax – matplotlib.axes.Axes object to add annotation to

-
line_x1 – Starting x-coordinate of connecting line

-
line_x2 – Ending x-coordinate of connecting line

-
line_y – Y-coordinate of connecting line

-
text_y – Y-offset for text placement above line

-
text – Text to display (typically p-value)

-
fontsize (default: `11 `) – Font size for text (11)

-
fontcolor (default: `'#000000' `) – Color for line and text (‘#000000’)

-
horizontalalignment (default: `'center' `) – Text horizontal alignment (‘center’)

Returns :

Adds annotation directly to the axes

Return type :

None
