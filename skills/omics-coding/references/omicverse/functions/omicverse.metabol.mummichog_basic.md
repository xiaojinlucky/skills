# omicverse.metabol.mummichog_basic #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.mummichog_basic`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.mummichog_basic.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Pure-Python mummichog — pathway enrichment from m/z peaks.

## Signature

```text
omicverse.metabol. mummichog_basic ( mz , pvalue , * , polarity = 'positive' , ppm = 10.0 , significance_cutoff = 0.05 , n_perm = 1000 , min_overlap = 2 , pathways = None , mass_db = None , seed = 0 )
```

## Parameters

- `mz`: ( ndarray ) – m/z value per peak.
- `pvalue`: ( ndarray ) – Per-peak p-value from the upstream univariate test. Peaks with pvalue < significance_cutoff are the “hit” set; the rest form the background.
- `polarity`: ( str (default: 'positive' )) – "positive" or "negative" .
- `ppm`: ( float (default: 10.0 )) – Mass-matching tolerance in ppm. Default 10.
- `significance_cutoff`: ( float (default: 0.05 )) – Threshold that splits mz into hits vs background.
- `n_perm`: ( int (default: 1000 )) – Random permutations for the empirical null p-value. 1000 is fine for tutorials; bump to ≥10000 for publication.
- `min_overlap`: ( int (default: 2 )) – Skip pathways with fewer than this many overlapping compounds.
- `pathways`: ( Optional [ dict [ str , list [ str ]]] (default: None ))
- `mass_db`: ( Optional [ DataFrame ] (default: None ))
- `seed`: ( int (default: 0 ))

## Full Documentation

# omicverse.metabol.mummichog_basic #

omicverse.metabol. mummichog_basic ( mz , pvalue , * , polarity = 'positive' , ppm = 10.0 , significance_cutoff = 0.05 , n_perm = 1000 , min_overlap = 2 , pathways = None , mass_db = None , seed = 0 ) [source] #

Pure-Python mummichog — pathway enrichment from m/z peaks.

Parameters :

-
mz ( `ndarray `) – m/z value per peak.

-
pvalue ( `ndarray `) – Per-peak p-value from the upstream univariate test. Peaks with `pvalue < significance_cutoff `are the “hit” set; the rest form the background.

-
polarity ( `str `(default: `'positive' `)) – `"positive" `or `"negative" `.

-
ppm ( `float `(default: `10.0 `)) – Mass-matching tolerance in ppm. Default 10.

-
significance_cutoff ( `float `(default: `0.05 `)) – Threshold that splits `mz `into hits vs background.

-
n_perm ( `int `(default: `1000 `)) – Random permutations for the empirical null p-value. 1000 is fine for tutorials; bump to ≥10000 for publication.

-
min_overlap ( `int `(default: `2 `)) – Skip pathways with fewer than this many overlapping compounds.

-
pathways ( `Optional `[ `dict `[ `str `, `list `[ `str `]]] (default: `None `))

-
mass_db ( `Optional `[ `DataFrame `] (default: `None `))

-
seed ( `int `(default: `0 `))

Returns :

`pathway `, `overlap `, `set_size `, `pvalue `(empirical), `padj `(BH), `observed_score `.

Return type :

pd.DataFrame
