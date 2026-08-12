# omicverse.micro.Alpha.run #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.Alpha.run`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.Alpha.run.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Compute the requested alpha metrics.

## Signature

```text
Alpha. run ( metrics = ('shannon', 'observed_otus') , write_to_obs = True , tree_key = 'tree' )
```

## Parameters

- `metrics`: ( Union [ str , Sequence [ str ]] (default: ('shannon', 'observed_otus') ))
- `write_to_obs`: ( bool (default: True ))
- `tree_key`: ( str (default: 'tree' ))

## Full Documentation

# omicverse.micro.Alpha.run #

Alpha. run ( metrics = ('shannon', 'observed_otus') , write_to_obs = True , tree_key = 'tree' ) [source] #

Compute the requested alpha metrics.

Returns a DataFrame indexed by sample with one column per metric. By default the result is also merged into `adata.obs `with the same column names.

Parameters :

-
metrics ( `Union `[ `str `, `Sequence `[ `str `]] (default: `('shannon', 'observed_otus') `))

-
write_to_obs ( `bool `(default: `True `))

-
tree_key ( `str `(default: `'tree' `))
