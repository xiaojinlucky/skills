# omicverse.alignment.vsearch.filter_quality #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.vsearch.filter_quality`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.vsearch.filter_quality.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Filter merged FASTQs and write per-sample FASTA with labels.

## Signature

```text
omicverse.alignment.vsearch. filter_quality ( merged , output_dir , max_ee = 1.0 , min_len = 0 , max_len = 0 , trunc_len = 0 , max_ns = 0 , threads = 4 , jobs = None , extra_args = None , vsearch_path = None , auto_install = True , overwrite = False )
```

## Parameters

- `merged`: ( Union [ Sequence [ Dict [ str , str ]], Sequence [ str ], Sequence [ Tuple [ str , str ]]] )
- `output_dir`: ( str )
- `max_ee`: ( float (default: 1.0 ))
- `min_len`: ( int (default: 0 ))
- `max_len`: ( int (default: 0 ))
- `trunc_len`: ( int (default: 0 ))
- `max_ns`: ( int (default: 0 ))
- `threads`: ( int (default: 4 ))
- `jobs`: ( Optional [ int ] (default: None ))
- `extra_args`: ( Optional [ Sequence [ str ]] (default: None ))
- `vsearch_path`: ( Optional [ str ] (default: None ))
- `auto_install`: ( bool (default: True ))
- `overwrite`: ( bool (default: False ))

## Full Documentation

# omicverse.alignment.vsearch.filter_quality #

omicverse.alignment.vsearch. filter_quality ( merged , output_dir , max_ee = 1.0 , min_len = 0 , max_len = 0 , trunc_len = 0 , max_ns = 0 , threads = 4 , jobs = None , extra_args = None , vsearch_path = None , auto_install = True , overwrite = False ) [source] #

Filter merged FASTQs and write per-sample FASTA with labels.

Accepts:

-
list of dicts from `merge_pairs() `with keys `sample `and `merged `

-
list of `(sample, merged_path) `tuples

-
list of fastq paths (sample name derived from filename)

Output per sample: `output_dir/<sample>/<sample>_filt.fasta `with headers relabeled `<sample>.<n> `so downstream `--otutabout `can resolve sample identity from the read label prefix.

Parameters :

-
merged ( `Union `[ `Sequence `[ `Dict `[ `str `, `str `]], `Sequence `[ `str `], `Sequence `[ `Tuple `[ `str `, `str `]]] )

-
output_dir ( `str `)

-
max_ee ( `float `(default: `1.0 `))

-
min_len ( `int `(default: `0 `))

-
max_len ( `int `(default: `0 `))

-
trunc_len ( `int `(default: `0 `))

-
max_ns ( `int `(default: `0 `))

-
threads ( `int `(default: `4 `))

-
jobs ( `Optional `[ `int `] (default: `None `))

-
extra_args ( `Optional `[ `Sequence `[ `str `]] (default: `None `))

-
vsearch_path ( `Optional `[ `str `] (default: `None `))

-
auto_install ( `bool `(default: `True `))

-
overwrite ( `bool `(default: `False `))
