# omicverse.alignment.vsearch.uchime3_denovo #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.vsearch.uchime3_denovo`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.vsearch.uchime3_denovo.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

De novo chimera detection / removal on UNOISE3 ASVs.

## Signature

```text
omicverse.alignment.vsearch. uchime3_denovo ( asvs_fasta , output_dir , vsearch_path = None , auto_install = True , overwrite = False )
```

## Parameters

- `asvs_fasta`: ( str )
- `output_dir`: ( str )
- `vsearch_path`: ( Optional [ str ] (default: None ))
- `auto_install`: ( bool (default: True ))
- `overwrite`: ( bool (default: False ))

## Full Documentation

# omicverse.alignment.vsearch.uchime3_denovo #

omicverse.alignment.vsearch. uchime3_denovo ( asvs_fasta , output_dir , vsearch_path = None , auto_install = True , overwrite = False ) [source] #

De novo chimera detection / removal on UNOISE3 ASVs.

Note that UNOISE3 already applies a lightweight chimera filter; running `uchime3_denovo `as a second pass is a conservative extra step.

Note

vsearch’s `--uchime3_denovo `is intentionally single-threaded upstream, so there is no `threads= `parameter (unlike the other wrappers in this module).

Parameters :

-
asvs_fasta ( `str `)

-
output_dir ( `str `)

-
vsearch_path ( `Optional `[ `str `] (default: `None `))

-
auto_install ( `bool `(default: `True `))

-
overwrite ( `bool `(default: `False `))
