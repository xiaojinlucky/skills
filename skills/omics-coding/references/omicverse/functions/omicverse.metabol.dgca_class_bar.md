# omicverse.metabol.dgca_class_bar #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.dgca_class_bar`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.dgca_class_bar.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Bar chart of DC-class counts (+/+, +/0, +/-, -/+, …).

## Signature

```text
omicverse.metabol. dgca_class_bar ( dc_df , * , ax = None , figsize = (6.0, 3.5) , log = True )
```

## Parameters

- `dc_df`: ( pd.DataFrame ) – Output of omicverse.metabol.dgca() — needs the dc_class column.
- `log`: ( bool , default True ) – Log-scale the y-axis (counts often span orders of magnitude).
- `ax`: ( Optional [ Axes ] (default: None )) – Standard matplotlib hooks.
- `figsize`: ( tuple [ float , float ] (default: (6.0, 3.5) )) – Standard matplotlib hooks.

## Full Documentation

# omicverse.metabol.dgca_class_bar #

omicverse.metabol. dgca_class_bar ( dc_df , * , ax = None , figsize = (6.0, 3.5) , log = True ) [source] #

Bar chart of DC-class counts (+/+, +/0, +/-, -/+, …).

Summarises the rewiring profile from `omicverse.metabol.dgca() `. Each pair of metabolites is assigned a class encoding the sign of their correlation in group A and group B ( + , - , 0 for significant positive, significant negative, or non-significant). Symmetric reversals ( `+/- `and `-/+ `) get the same red colour because they’re the strongest rewiring signal; `+/+ `/ `-/- `are concordant (no rewiring); `0/0 `(no signal in either group) is greyed out and pushed to the right.

Parameters :

-
dc_df ( pd.DataFrame ) – Output of `omicverse.metabol.dgca() `— needs the `dc_class `column.

-
log ( bool , default True ) – Log-scale the y-axis (counts often span orders of magnitude).

-
ax ( `Optional `[ `Axes `] (default: `None `)) – Standard matplotlib hooks.

-
figsize ( `tuple `[ `float `, `float `] (default: `(6.0, 3.5) `)) – Standard matplotlib hooks.

Return type :

(fig, ax) tuple.
