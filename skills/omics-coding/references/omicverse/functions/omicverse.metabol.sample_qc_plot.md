# omicverse.metabol.sample_qc_plot #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.sample_qc_plot`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.sample_qc_plot.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Scatter of Hotelling T² vs DModX with critical-value lines.

## Signature

```text
omicverse.metabol. sample_qc_plot ( qc_df , * , ax = None , figsize = (5.0, 4.0) , normal_color = '2980b9' , outlier_color = 'c0392b' )
```

## Parameters

- `qc_df`: ( pd.DataFrame ) – Output of omicverse.metabol.sample_qc() — must contain T2 , DModX , T2_crit , DModX_crit and is_outlier .
- `normal_color`: ( str (default: '#2980b9' )) – Hex / named colours for the two populations.
- `outlier_color`: ( str (default: '#c0392b' )) – Hex / named colours for the two populations.
- `ax`: ( Optional [ Axes ] (default: None )) – Standard matplotlib hooks.
- `figsize`: ( tuple [ float , float ] (default: (5.0, 4.0) )) – Standard matplotlib hooks.

## Full Documentation

# omicverse.metabol.sample_qc_plot #

omicverse.metabol. sample_qc_plot ( qc_df , * , ax = None , figsize = (5.0, 4.0) , normal_color = '#2980b9' , outlier_color = '#c0392b' ) [source] #

Scatter of Hotelling T² vs DModX with critical-value lines.

Standard SIMCA-style outlier diagnostic. Each sample is one point; the dashed grey lines are the alpha-level (default 0.95) critical values from `omicverse.metabol.sample_qc() `. Samples above either line are flagged — Hotelling T² captures distance from the PCA centre (within-model outliers), DModX captures distance to the PCA hyperplane (off-model outliers).

Parameters :

-
qc_df ( pd.DataFrame ) – Output of `omicverse.metabol.sample_qc() `— must contain `T2 `, `DModX `, `T2_crit `, `DModX_crit `and `is_outlier `.

-
normal_color ( `str `(default: `'#2980b9' `)) – Hex / named colours for the two populations.

-
outlier_color ( `str `(default: `'#c0392b' `)) – Hex / named colours for the two populations.

-
ax ( `Optional `[ `Axes `] (default: `None `)) – Standard matplotlib hooks.

-
figsize ( `tuple `[ `float `, `float `] (default: `(5.0, 4.0) `)) – Standard matplotlib hooks.

Return type :

(fig, ax) tuple.
