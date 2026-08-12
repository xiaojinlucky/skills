# omicverse.alignment.vsearch.dereplicate #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.vsearch.dereplicate`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.vsearch.dereplicate.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Combine + dereplicate filtered FASTAs → one uniques.fasta .

## Signature

```text
omicverse.alignment.vsearch. dereplicate ( filtered , output_dir , min_uniq = 2 , threads = 4 , extra_args = None , vsearch_path = None , auto_install = True , overwrite = False )
```

## Parameters

- `filtered`: ( Union [ Sequence [ Dict [ str , str ]], Sequence [ str ]] )
- `output_dir`: ( str )
- `min_uniq`: ( int (default: 2 ))
- `threads`: ( int (default: 4 ))
- `extra_args`: ( Optional [ Sequence [ str ]] (default: None ))
- `vsearch_path`: ( Optional [ str ] (default: None ))
- `auto_install`: ( bool (default: True ))
- `overwrite`: ( bool (default: False ))

## Full Documentation

# omicverse.alignment.vsearch.dereplicate #

omicverse.alignment.vsearch. dereplicate ( filtered , output_dir , min_uniq = 2 , threads = 4 , extra_args = None , vsearch_path = None , auto_install = True , overwrite = False ) [source] #

Combine + dereplicate filtered FASTAs → one `uniques.fasta `.

The concatenated file `combined.fasta `is also written; downstream `usearch_global() `uses it to build the sample × ASV count matrix because it preserves per-read sample labels.

Parameters :

-
filtered ( `Union `[ `Sequence `[ `Dict `[ `str `, `str `]], `Sequence `[ `str `]] )

-
output_dir ( `str `)

-
min_uniq ( `int `(default: `2 `))

-
threads ( `int `(default: `4 `))

-
extra_args ( `Optional `[ `Sequence `[ `str `]] (default: `None `))

-
vsearch_path ( `Optional `[ `str `] (default: `None `))

-
auto_install ( `bool `(default: `True `))

-
overwrite ( `bool `(default: `False `))
