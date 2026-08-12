# omicverse.pl.branch_streamplot #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.branch_streamplot`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.branch_streamplot.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Render a branch-aware pseudotime stream plot.

## Signature

```text
omicverse.pl. branch_streamplot ( x , branches = None , palette = None , * , group_key = None , pseudotime_key = None , labels = None , trunk_groups = None , branch_groups = None , branch_center = 0.56 , branch_steepness = 11.0 , branch_power = 1.1 , branch_amplitude = 0.28 , n_branches = 2 , bw = 0.15 , pad = 0.035 , count_power = 0.3 , normalize_pseudotime = 'auto' , label_positions = None , figsize = (7.0, 3.5) , xlim = (-0.02, 1.03) , ylim = None , xlabel = 'Pseudotime' , xticks = None , axis_y = 'auto' , axis_arrowprops = None , scale_to = 'auto' , min_visible_width = 0.0001 , label_fontsize = 12 , label_fontweight = 'semibold' , label_outline_width = 5.0 , label_outline_alpha = 0.92 , tick_labelsize = 13 , xlabel_fontsize = 18 , ax = None , show = False , save = None , save_pdf = None )
```

## Parameters

- `x`: ( Union [ ndarray , DataFrame , Any ] ) – Observation table, or a one-dimensional pseudotime grid shared by all precomputed branches.
- `branches`: ( Optional [ Sequence [ Mapping [ str , Any ]]] (default: None )) – Optional sequence of branch dictionaries for advanced precomputed layouts. Each entry must contain: center : array-like centerline with the same length as x
- `palette`: ( Union [ Mapping [ str , str ], Sequence [ str ], str , None ] (default: None )) – Color mapping for labels. Accepts a dict , color sequence, matplotlib colormap name, or None . When omitted, omicverse palettes are used.
- `group_key`: ( Optional [ str ] (default: None )) – Column in x.obs or x containing cell-state labels when plotting directly from annotations.
- `pseudotime_key`: ( Optional [ str ] (default: None )) – Column in x.obs or x containing pseudotime values when plotting directly from annotations.
- `labels`: ( Optional [ Sequence [ str ]] (default: None )) – Optional label order. Categorical order in group_key is used when omitted.
- `trunk_groups`: ( Optional [ Sequence [ str ]] (default: None )) – Labels to place on the shared centerline when plotting from annotations. If omitted, groups are inferred from KDE peak locations.
- `branch_groups`: ( Optional [ Mapping [ str , float ]] (default: None )) – Optional mapping from label to branch amplitude. Positive and negative amplitudes bend branches in opposite directions.
- `branch_center`: ( float (default: 0.56 )) – Parameters controlling the automatic branch centerlines.
- `branch_steepness`: ( float (default: 11.0 )) – Parameters controlling the automatic branch centerlines.
- `branch_power`: ( float (default: 1.1 )) – Parameters controlling the automatic branch centerlines.
- `branch_amplitude`: ( float (default: 0.28 )) – Parameters controlling the automatic branch centerlines.
- `n_branches`: ( int (default: 2 )) – Number of branch amplitudes used when branch_groups is inferred.
- `bw`: ( float (default: 0.15 )) – KDE bandwidth, taper padding, and abundance scaling used for annotation-derived ribbon widths.
- `pad`: ( float (default: 0.035 )) – KDE bandwidth, taper padding, and abundance scaling used for annotation-derived ribbon widths.
- `count_power`: ( float (default: 0.3 )) – KDE bandwidth, taper padding, and abundance scaling used for annotation-derived ribbon widths.
- `normalize_pseudotime`: ( bool | str (default: 'auto' )) – Whether to min-max normalize observed pseudotime before estimating KDE profiles. The default "auto" normalizes only when the default 0-1 grid is used with values outside that range.
- `label_positions`: ( Union [ Mapping [ str , tuple [ float , float , float ]], str , None ] (default: None )) – Optional mapping label -> (x, y, fontsize) for direct text labels.
- `figsize`: ( tuple [ float , float ] (default: (7.0, 3.5) )) – Figure size used when ax is not provided.
- `xlim`: ( tuple [ float , float ] (default: (-0.02, 1.03) )) – Plot limits.
- `ylim`: ( Optional [ tuple [ float , float ]] (default: None )) – Plot limits.
- `xlabel`: ( str (default: 'Pseudotime' )) – X-axis label.
- `xticks`: ( Optional [ Sequence [ float ]] (default: None )) – Tick locations for pseudotime.
- `axis_y`: ( float | str | None (default: 'auto' )) – Y coordinate of the arrow-style pseudotime axis. Set to None to hide it.
- `axis_arrowprops`: ( Optional [ Mapping [ str , Any ]] (default: None )) – Additional keyword arguments passed to Axes.annotate for the axis arrow.
- `scale_to`: ( float | str | None (default: 'auto' )) – Optional maximum branch thickness after rescaling all ribbons together.
- `min_visible_width`: ( float (default: 0.0001 )) – Ribbons thinner than this threshold are omitted for visual stability.
- `label_fontweight`: ( str (default: 'semibold' )) – Text styling for direct labels.
- `label_outline_width`: ( float (default: 5.0 )) – Text styling for direct labels.
- `label_outline_alpha`: ( float (default: 0.92 )) – Text styling for direct labels.
- `tick_labelsize`: ( float (default: 13 )) – Axis text sizes.
- `xlabel_fontsize`: ( float (default: 18 )) – Axis text sizes.
- `ax`: ( Optional [ Axes ] (default: None )) – Existing matplotlib axes. When omitted, a new figure is created.
- `show`: ( bool (default: False )) – Whether to call matplotlib.pyplot.show() .
- `save`: ( Union [ str , Path , None ] (default: None )) – Optional output paths.
- `save_pdf`: ( Union [ str , Path , None ] (default: None )) – Optional output paths.
- `label_fontsize`: ( float (default: 12 ))

## Full Documentation

# omicverse.pl.branch_streamplot #

omicverse.pl. branch_streamplot ( x , branches = None , palette = None , * , group_key = None , pseudotime_key = None , labels = None , trunk_groups = None , branch_groups = None , branch_center = 0.56 , branch_steepness = 11.0 , branch_power = 1.1 , branch_amplitude = 0.28 , n_branches = 2 , bw = 0.15 , pad = 0.035 , count_power = 0.3 , normalize_pseudotime = 'auto' , label_positions = None , figsize = (7.0, 3.5) , xlim = (-0.02, 1.03) , ylim = None , xlabel = 'Pseudotime' , xticks = None , axis_y = 'auto' , axis_arrowprops = None , scale_to = 'auto' , min_visible_width = 0.0001 , label_fontsize = 12 , label_fontweight = 'semibold' , label_outline_width = 5.0 , label_outline_alpha = 0.92 , tick_labelsize = 13 , xlabel_fontsize = 18 , ax = None , show = False , save = None , save_pdf = None ) [source] #

Render a branch-aware pseudotime stream plot.

The main entry point accepts an `obs `table plus `group_key `and `pseudotime_key `and automatically builds the ribbon layout. Advanced users can still pass a pseudotime grid and precomputed branch definitions.

Parameters :

-
x ( `Union `[ `ndarray `, `DataFrame `, `Any `] ) – Observation table, or a one-dimensional pseudotime grid shared by all precomputed branches.

-
branches ( `Optional `[ `Sequence `[ `Mapping `[ `str `, `Any `]]] (default: `None `)) –
Optional sequence of branch dictionaries for advanced precomputed layouts. Each entry must contain:

-
`center `: array-like centerline with the same length as `x `

-
`layers `: ordered `[(label, width), ...] `ribbons for that branch

-
palette ( `Union `[ `Mapping `[ `str `, `str `], `Sequence `[ `str `], `str `, `None `] (default: `None `)) – Color mapping for labels. Accepts a `dict `, color sequence, matplotlib colormap name, or `None `. When omitted, omicverse palettes are used.

-
group_key ( `Optional `[ `str `] (default: `None `)) – Column in `x.obs `or `x `containing cell-state labels when plotting directly from annotations.

-
pseudotime_key ( `Optional `[ `str `] (default: `None `)) – Column in `x.obs `or `x `containing pseudotime values when plotting directly from annotations.

-
labels ( `Optional `[ `Sequence `[ `str `]] (default: `None `)) – Optional label order. Categorical order in `group_key `is used when omitted.

-
trunk_groups ( `Optional `[ `Sequence `[ `str `]] (default: `None `)) – Labels to place on the shared centerline when plotting from annotations. If omitted, groups are inferred from KDE peak locations.

-
branch_groups ( `Optional `[ `Mapping `[ `str `, `float `]] (default: `None `)) – Optional mapping from label to branch amplitude. Positive and negative amplitudes bend branches in opposite directions.

-
branch_center ( `float `(default: `0.56 `)) – Parameters controlling the automatic branch centerlines.

-
branch_steepness ( `float `(default: `11.0 `)) – Parameters controlling the automatic branch centerlines.

-
branch_power ( `float `(default: `1.1 `)) – Parameters controlling the automatic branch centerlines.

-
branch_amplitude ( `float `(default: `0.28 `)) – Parameters controlling the automatic branch centerlines.

-
n_branches ( `int `(default: `2 `)) – Number of branch amplitudes used when `branch_groups `is inferred.

-
bw ( `float `(default: `0.15 `)) – KDE bandwidth, taper padding, and abundance scaling used for annotation-derived ribbon widths.

-
pad ( `float `(default: `0.035 `)) – KDE bandwidth, taper padding, and abundance scaling used for annotation-derived ribbon widths.

-
count_power ( `float `(default: `0.3 `)) – KDE bandwidth, taper padding, and abundance scaling used for annotation-derived ribbon widths.

-
normalize_pseudotime ( `bool `| `str `(default: `'auto' `)) – Whether to min-max normalize observed pseudotime before estimating KDE profiles. The default `"auto" `normalizes only when the default 0-1 grid is used with values outside that range.

-
label_positions ( `Union `[ `Mapping `[ `str `, `tuple `[ `float `, `float `, `float `]], `str `, `None `] (default: `None `)) – Optional mapping `label -> (x, y, fontsize) `for direct text labels.

-
figsize ( `tuple `[ `float `, `float `] (default: `(7.0, 3.5) `)) – Figure size used when `ax `is not provided.

-
xlim ( `tuple `[ `float `, `float `] (default: `(-0.02, 1.03) `)) – Plot limits.

-
ylim ( `Optional `[ `tuple `[ `float `, `float `]] (default: `None `)) – Plot limits.

-
xlabel ( `str `(default: `'Pseudotime' `)) – X-axis label.

-
xticks ( `Optional `[ `Sequence `[ `float `]] (default: `None `)) – Tick locations for pseudotime.

-
axis_y ( `float `| `str `| `None `(default: `'auto' `)) – Y coordinate of the arrow-style pseudotime axis. Set to `None `to hide it.

-
axis_arrowprops ( `Optional `[ `Mapping `[ `str `, `Any `]] (default: `None `)) – Additional keyword arguments passed to `Axes.annotate `for the axis arrow.

-
scale_to ( `float `| `str `| `None `(default: `'auto' `)) – Optional maximum branch thickness after rescaling all ribbons together.

-
min_visible_width ( `float `(default: `0.0001 `)) – Ribbons thinner than this threshold are omitted for visual stability.

-
label_fontweight ( `str `(default: `'semibold' `)) – Text styling for direct labels.

-
label_outline_width ( `float `(default: `5.0 `)) – Text styling for direct labels.

-
label_outline_alpha ( `float `(default: `0.92 `)) – Text styling for direct labels.

-
tick_labelsize ( `float `(default: `13 `)) – Axis text sizes.

-
xlabel_fontsize ( `float `(default: `18 `)) – Axis text sizes.

-
ax ( `Optional `[ `Axes `] (default: `None `)) – Existing matplotlib axes. When omitted, a new figure is created.

-
show ( `bool `(default: `False `)) – Whether to call `matplotlib.pyplot.show() `.

-
save ( `Union `[ `str `, `Path `, `None `] (default: `None `)) – Optional output paths.

-
save_pdf ( `Union `[ `str `, `Path `, `None `] (default: `None `)) – Optional output paths.

-
label_fontsize ( `float `(default: `12 `))

Returns :

Figure and axes containing the branch stream plot.

Return type :

tuple [ matplotlib.figure.Figure , matplotlib.axes.Axes ]
