# omicverse.single.dynamic_features #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.dynamic_features`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.dynamic_features.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Fit GAM-based pseudotime trends for one or more datasets or groups.

## Signature

```text
omicverse.single. dynamic_features ( data , genes = None , pseudotime = 'pseudotime' , * , groupby = None , groups = None , layer = None , use_raw = False , subsets = None , weights = None , distribution = 'normal' , link = 'identity' , n_splines = 8 , spline_order = 3 , grid_size = 200 , confidence_level = 0.95 , min_cells = 20 , min_variance = 1e-08 , store_raw = False , raw_obs_keys = None , key_added = 'dynamic_features' , verbose = True )
```

## Parameters

- `data`: ( Union [ AnnData , Mapping [ str , AnnData ]] ) – A single AnnData object or a mapping of dataset names to AnnData objects.
- `genes`: ( Union [ str , Sequence [ str ], None ] (default: None )) – Feature names to model. When None , genes are inferred from the available features in the supplied datasets.
- `pseudotime`: ( str (default: 'pseudotime' )) – Column in adata.obs containing pseudotime values.
- `groupby`: ( Union [ Mapping [ str , str ], str , None ] (default: None )) – Optional obs column used to split each dataset into separate trend groups, such as cell types or lineages. Each group is fitted as its own comparable series. The chosen key is recorded in the result tables as groupby_key .
- `groups`: ( Union [ Sequence [ str ], Mapping [ str , Sequence [ str ]], None ] (default: None )) – Optional subset of group labels to keep when groupby is provided.
- `layer`: ( Optional [ str ] (default: None )) – Optional layer name used as the expression source.
- `use_raw`: ( bool (default: False )) – Whether to read expression values from adata.raw .
- `subsets`: ( Union [ Sequence [ str ], Mapping [ str , Sequence [ str ]], None ] (default: None )) – Optional cell subsets to retain before fitting, either globally or per dataset.
- `weights`: ( Union [ str , Sequence [ float ], Mapping [ str , Any ], None ] (default: None )) – Optional sample weights, provided as an obs key, array-like values, or per-dataset mapping. For grouped or multi-dataset inputs, mappings may be keyed by the final plotted dataset label or by the source dataset name.
- `distribution`: ( str (default: 'normal' )) – GAM response distribution passed to pygam .
- `link`: ( str (default: 'identity' )) – Link function paired with distribution .
- `n_splines`: ( int (default: 8 )) – Number of spline basis functions.
- `spline_order`: ( int (default: 3 )) – Order of the spline basis.
- `grid_size`: ( int (default: 200 )) – Number of pseudotime grid points used to evaluate fitted curves.
- `confidence_level`: ( float (default: 0.95 )) – Confidence level used to compute fitted intervals.
- `min_cells`: ( int (default: 20 )) – Minimum number of valid cells required to fit a model.
- `min_variance`: ( float (default: 1e-08 )) – Minimum variance required for a feature to be modeled.
- `store_raw`: ( bool (default: False )) – Whether to include per-cell raw observations in the returned result. This must be enabled if downstream plotting should overlay individual points, for example via ov.pl.dynamic_trends() with add_point=True .
- `raw_obs_keys`: ( Union [ str , Sequence [ str ], Mapping [ str , Union [ str , Sequence [ str ]]], None ] (default: None )) – Optional obs columns to copy into the stored raw point table when store_raw=True . This is useful for downstream point coloring in ov.pl.dynamic_trends() , for example raw_obs_keys=['State'] . When data is a mapping, this may also be a mapping from dataset name to the desired obs keys.
- `key_added`: ( str | None (default: 'dynamic_features' )) – Optional key used to store outputs in adata.uns for single-dataset inputs.
- `verbose`: ( bool (default: True )) – Whether to print progress information during fitting.

## Full Documentation

# omicverse.single.dynamic_features #

omicverse.single. dynamic_features ( data , genes = None , pseudotime = 'pseudotime' , * , groupby = None , groups = None , layer = None , use_raw = False , subsets = None , weights = None , distribution = 'normal' , link = 'identity' , n_splines = 8 , spline_order = 3 , grid_size = 200 , confidence_level = 0.95 , min_cells = 20 , min_variance = 1e-08 , store_raw = False , raw_obs_keys = None , key_added = 'dynamic_features' , verbose = True ) [source] #

Fit GAM-based pseudotime trends for one or more datasets or groups.

Parameters :

-
data ( `Union `[ `AnnData `, `Mapping `[ `str `, `AnnData `]] ) – A single `AnnData `object or a mapping of dataset names to AnnData objects.

-
genes ( `Union `[ `str `, `Sequence `[ `str `], `None `] (default: `None `)) – Feature names to model. When `None `, genes are inferred from the available features in the supplied datasets.

-
pseudotime ( `str `(default: `'pseudotime' `)) – Column in `adata.obs `containing pseudotime values.

-
groupby ( `Union `[ `Mapping `[ `str `, `str `], `str `, `None `] (default: `None `)) – Optional `obs `column used to split each dataset into separate trend groups, such as cell types or lineages. Each group is fitted as its own comparable series. The chosen key is recorded in the result tables as `groupby_key `.

-
groups ( `Union `[ `Sequence `[ `str `], `Mapping `[ `str `, `Sequence `[ `str `]], `None `] (default: `None `)) – Optional subset of group labels to keep when `groupby `is provided.

-
layer ( `Optional `[ `str `] (default: `None `)) – Optional layer name used as the expression source.

-
use_raw ( `bool `(default: `False `)) – Whether to read expression values from `adata.raw `.

-
subsets ( `Union `[ `Sequence `[ `str `], `Mapping `[ `str `, `Sequence `[ `str `]], `None `] (default: `None `)) – Optional cell subsets to retain before fitting, either globally or per dataset.

-
weights ( `Union `[ `str `, `Sequence `[ `float `], `Mapping `[ `str `, `Any `], `None `] (default: `None `)) – Optional sample weights, provided as an obs key, array-like values, or per-dataset mapping. For grouped or multi-dataset inputs, mappings may be keyed by the final plotted dataset label or by the source dataset name.

-
distribution ( `str `(default: `'normal' `)) – GAM response distribution passed to `pygam `.

-
link ( `str `(default: `'identity' `)) – Link function paired with `distribution `.

-
n_splines ( `int `(default: `8 `)) – Number of spline basis functions.

-
spline_order ( `int `(default: `3 `)) – Order of the spline basis.

-
grid_size ( `int `(default: `200 `)) – Number of pseudotime grid points used to evaluate fitted curves.

-
confidence_level ( `float `(default: `0.95 `)) – Confidence level used to compute fitted intervals.

-
min_cells ( `int `(default: `20 `)) – Minimum number of valid cells required to fit a model.

-
min_variance ( `float `(default: `1e-08 `)) – Minimum variance required for a feature to be modeled.

-
store_raw ( `bool `(default: `False `)) – Whether to include per-cell raw observations in the returned result. This must be enabled if downstream plotting should overlay individual points, for example via `ov.pl.dynamic_trends() `with `add_point=True `.

-
raw_obs_keys ( `Union `[ `str `, `Sequence `[ `str `], `Mapping `[ `str `, `Union `[ `str `, `Sequence `[ `str `]]], `None `] (default: `None `)) – Optional `obs `columns to copy into the stored raw point table when `store_raw=True `. This is useful for downstream point coloring in `ov.pl.dynamic_trends() `, for example `raw_obs_keys=['State'] `. When `data `is a mapping, this may also be a mapping from dataset name to the desired obs keys.

-
key_added ( `str `| `None `(default: `'dynamic_features' `)) – Optional key used to store outputs in `adata.uns `for single-dataset inputs.

-
verbose ( `bool `(default: `True `)) – Whether to print progress information during fitting.

Returns :

Container holding fitted trends, summary statistics, and optional raw observations for downstream visualization and filtering. The returned tables use:

`dataset `

Final plotted series label used for comparison.

`source_dataset `

Original dataset key before any group splitting. This column is included only when the input contains multiple datasets.

`groupby_key `

The `obs `column used for grouping, if any.

`group `

The concrete group label (for example a cell type or lineage).

Return type :

DynamicFeaturesResult
