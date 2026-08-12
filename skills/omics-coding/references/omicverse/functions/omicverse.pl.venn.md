# omicverse.pl.venn #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.venn`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.venn.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Create a Venn diagram to visualize set overlaps.

## Signature

```text
omicverse.pl. venn ( sets = {} , out = './' , palette = 'bgrc' , ax = False , ext = 'png' , dpi = 300 , fontsize = None , bbox_to_anchor = (0.5, 0.99) , nc = 2 , cs = 4 , figsize = (4, 4) )
```

## Parameters

- `sets`: ( dict ) – Dictionary mapping set names to Python sets. 2 or 3 sets use matplotlib-venn ; 4 or more fall back to venny4py .
- `out`: ( str ) – Output directory for saved figure ( venny4py fallback only).
- `palette`: ( str or list ) – Colors for the set circles. A string such as 'bgrc' is treated as a sequence of single-letter matplotlib colors; a list is used as-is.
- `ax`: ( matplotlib.axes.Axes or bool ) – Existing axes to draw into; if False a new figure/axes is created.
- `ext`: ( str ) – Output file extension ( venny4py fallback only).
- `dpi`: ( int ) – Resolution of saved image ( venny4py fallback only).
- `fontsize`: ( float or None ) – Font size for the subset counts and set names. When None it follows plt.rcParams['font.size'] so the labels match the rest of a figure rather than a hard-coded size.
- `bbox_to_anchor`: ( tuple ) – Legend anchor position ( venny4py fallback only).
- `nc`: ( int ) – Number of legend columns ( venny4py fallback only).
- `cs`: ( float ) – Legend font size ( venny4py fallback only).
- `figsize`: ( tuple ) – Figure size used when ax is False and a new figure is created.

## Full Documentation

# omicverse.pl.venn #

omicverse.pl. venn ( sets = {} , out = './' , palette = 'bgrc' , ax = False , ext = 'png' , dpi = 300 , fontsize = None , bbox_to_anchor = (0.5, 0.99) , nc = 2 , cs = 4 , figsize = (4, 4) ) [source] #

Create a Venn diagram to visualize set overlaps.

For 2 or 3 sets this draws area-proportional circles via `matplotlib-venn `( `venn2 `/ `venn3 `) so the numbers sit inside clean, correctly scaled regions instead of the non-proportional ellipses of the `venn `package. This follows the approach of cnsplots (Farid Rashidi, BSD-3-Clause); the implementation here is independent. `matplotlib-venn `only supports 2 or 3 sets, so 4+ sets fall back to the `venny4py `backend.

Parameters :

-
sets ( dict ) – Dictionary mapping set names to Python sets. 2 or 3 sets use `matplotlib-venn `; 4 or more fall back to `venny4py `.

-
out ( str ) – Output directory for saved figure ( `venny4py `fallback only).

-
palette ( str or list ) – Colors for the set circles. A string such as `'bgrc' `is treated as a sequence of single-letter matplotlib colors; a list is used as-is.

-
ax ( matplotlib.axes.Axes or bool ) – Existing axes to draw into; if `False `a new figure/axes is created.

-
ext ( str ) – Output file extension ( `venny4py `fallback only).

-
dpi ( int ) – Resolution of saved image ( `venny4py `fallback only).

-
fontsize ( float or None ) – Font size for the subset counts and set names. When `None `it follows `plt.rcParams['font.size'] `so the labels match the rest of a figure rather than a hard-coded size.

-
bbox_to_anchor ( tuple ) – Legend anchor position ( `venny4py `fallback only).

-
nc ( int ) – Number of legend columns ( `venny4py `fallback only).

-
cs ( float ) – Legend font size ( `venny4py `fallback only).

-
figsize ( tuple ) – Figure size used when `ax `is `False `and a new figure is created.

Returns :

The axes the diagram was drawn into (or the passed-in `ax `).

Return type :

matplotlib.axes.Axes or bool
