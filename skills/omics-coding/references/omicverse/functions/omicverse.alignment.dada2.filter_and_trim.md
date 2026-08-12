# omicverse.alignment.dada2.filter_and_trim #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.dada2.filter_and_trim`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.dada2.filter_and_trim.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Quality-trim each sample’s FASTQs to output_dir/<sample>/ .

## Signature

```text
omicverse.alignment.dada2. filter_and_trim ( samples , output_dir , trunc_len = 0 , max_ee = 2.0 , trunc_q = 2 , min_len = 20 , max_n = 0 , overwrite = False )
```

## Parameters

- `samples`: ( Union [ Tuple [ str , str , Optional [ str ]], Sequence [ Tuple [ str , str , Optional [ str ]]]] )
- `output_dir`: ( str )
- `trunc_len`: ( Union [ int , Tuple [ int , int ]] (default: 0 ))
- `max_ee`: ( Union [ float , Tuple [ float , float ]] (default: 2.0 ))
- `trunc_q`: ( int (default: 2 ))
- `min_len`: ( int (default: 20 ))
- `max_n`: ( int (default: 0 ))
- `overwrite`: ( bool (default: False ))

## Full Documentation

# omicverse.alignment.dada2.filter_and_trim #

omicverse.alignment.dada2. filter_and_trim ( samples , output_dir , trunc_len = 0 , max_ee = 2.0 , trunc_q = 2 , min_len = 20 , max_n = 0 , overwrite = False ) [source] #

Quality-trim each sample’s FASTQs to output_dir/<sample>/ .

Accepts `(sample, fq1, fq2) `tuples; `fq2 `may be None (single-end).

Parameters :

-
samples ( `Union `[ `Tuple `[ `str `, `str `, `Optional `[ `str `]], `Sequence `[ `Tuple `[ `str `, `str `, `Optional `[ `str `]]]] )

-
output_dir ( `str `)

-
trunc_len ( `Union `[ `int `, `Tuple `[ `int `, `int `]] (default: `0 `))

-
max_ee ( `Union `[ `float `, `Tuple `[ `float `, `float `]] (default: `2.0 `))

-
trunc_q ( `int `(default: `2 `))

-
min_len ( `int `(default: `20 `))

-
max_n ( `int `(default: `0 `))

-
overwrite ( `bool `(default: `False `))
