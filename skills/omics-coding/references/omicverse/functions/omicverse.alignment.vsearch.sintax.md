# omicverse.alignment.vsearch.sintax #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.vsearch.sintax`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.vsearch.sintax.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Taxonomy assignment via SINTAX.

## Signature

```text
omicverse.alignment.vsearch. sintax ( asvs_fasta , db_fasta , output_dir , cutoff = 0.8 , strand = 'both' , threads = 4 , extra_args = None , vsearch_path = None , auto_install = True , overwrite = False )
```

## Parameters

- `asvs_fasta`: ( str ) – Query ASV FASTA.
- `db_fasta`: ( str ) – Required path to a SINTAX-formatted reference FASTA (headers must encode taxonomy as ;tax=d:...,p:...,c:...; ). Must be explicitly provided — no $HOME fallback. See omicverse.alignment.fetch_silva() .
- `cutoff`: ( float (default: 0.8 )) – Bootstrap confidence threshold (default 0.8). Stored in SINTAX output as two columns: raw classifications and cutoff-filtered classifications.
- `strand`: ( str (default: 'both' )) – plus | minus | both .
- `output_dir`: ( str )
- `threads`: ( int (default: 4 ))
- `extra_args`: ( Optional [ Sequence [ str ]] (default: None ))
- `vsearch_path`: ( Optional [ str ] (default: None ))
- `auto_install`: ( bool (default: True ))
- `overwrite`: ( bool (default: False ))

## Full Documentation

# omicverse.alignment.vsearch.sintax #

omicverse.alignment.vsearch. sintax ( asvs_fasta , db_fasta , output_dir , cutoff = 0.8 , strand = 'both' , threads = 4 , extra_args = None , vsearch_path = None , auto_install = True , overwrite = False ) [source] #

Taxonomy assignment via SINTAX.

Parameters :

-
asvs_fasta ( `str `) – Query ASV FASTA.

-
db_fasta ( `str `) – Required path to a SINTAX-formatted reference FASTA (headers must encode taxonomy as `;tax=d:...,p:...,c:...; `). Must be explicitly provided — no `$HOME `fallback. See `omicverse.alignment.fetch_silva() `.

-
cutoff ( `float `(default: `0.8 `)) – Bootstrap confidence threshold (default 0.8). Stored in SINTAX output as two columns: raw classifications and cutoff-filtered classifications.

-
strand ( `str `(default: `'both' `)) – `plus `| `minus `| `both `.

-
output_dir ( `str `)

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
