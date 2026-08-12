# omicverse.alignment.cutadapt #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.cutadapt`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.cutadapt.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run cutadapt to remove amplicon PCR primers.

## Signature

```text
omicverse.alignment. cutadapt ( samples , primer_fwd , primer_rev = None , output_dir = 'cutadapt' , threads = 4 , jobs = None , output_gzip = None , discard_untrimmed = True , min_length = 50 , max_n = 0 , extra_args = None , cutadapt_path = None , auto_install = True , overwrite = False )
```

## Parameters

- `samples`: ( Union [ Tuple [ str , str , Optional [ str ]], Sequence [ Tuple [ str , str , Optional [ str ]]]] ) – (sample, fq1, fq2) tuple, list of such tuples, or 1-2 FASTQ paths.
- `primer_fwd`: ( str ) – Forward primer sequence (5’ anchor on R1). IUPAC ambiguity allowed. Common 16S V4 choice: GTGYCAGCMGCCGCGGTAA (515F Parada).
- `primer_rev`: ( Optional [ str ] (default: None )) – Reverse primer (5’ anchor on R2). For V4: GGACTACNVGGGTWTCTAAT (806R Apprill).
- `output_dir`: ( str (default: 'cutadapt' )) – Output directory; per-sample subdirs are created under it.
- `threads`: ( int (default: 4 )) – Threads per cutadapt invocation.
- `jobs`: ( Optional [ int ] (default: None )) – Concurrent sample jobs (default: CPU/2, capped by sample count).
- `output_gzip`: ( Optional [ bool ] (default: None )) – Force gzipped output; None follows input suffix.
- `discard_untrimmed`: ( bool (default: True )) – Drop read pairs where primers were not found (standard for 16S).
- `min_length`: ( int (default: 50 )) – Minimum post-trim length; pairs shorter than this are dropped.
- `max_n`: ( Optional [ int ] (default: 0 )) – Maximum ambiguous bases allowed per read ( None disables filter).
- `extra_args`: ( Optional [ Sequence [ str ]] (default: None )) – Additional cutadapt CLI arguments appended verbatim.
- `cutadapt_path`: ( Optional [ str ] (default: None )) – Explicit path to cutadapt executable.
- `auto_install`: ( bool (default: True )) – Try to install via conda when missing.
- `overwrite`: ( bool (default: False )) – Re-run and overwrite existing outputs.

## Full Documentation

# omicverse.alignment.cutadapt #

omicverse.alignment. cutadapt ( samples , primer_fwd , primer_rev = None , output_dir = 'cutadapt' , threads = 4 , jobs = None , output_gzip = None , discard_untrimmed = True , min_length = 50 , max_n = 0 , extra_args = None , cutadapt_path = None , auto_install = True , overwrite = False ) [source] #

Run cutadapt to remove amplicon PCR primers.

Parameters :

-
samples ( `Union `[ `Tuple `[ `str `, `str `, `Optional `[ `str `]], `Sequence `[ `Tuple `[ `str `, `str `, `Optional `[ `str `]]]] ) – `(sample, fq1, fq2) `tuple, list of such tuples, or 1-2 FASTQ paths.

-
primer_fwd ( `str `) – Forward primer sequence (5’ anchor on R1). IUPAC ambiguity allowed. Common 16S V4 choice: `GTGYCAGCMGCCGCGGTAA `(515F Parada).

-
primer_rev ( `Optional `[ `str `] (default: `None `)) – Reverse primer (5’ anchor on R2). For V4: `GGACTACNVGGGTWTCTAAT `(806R Apprill).

-
output_dir ( `str `(default: `'cutadapt' `)) – Output directory; per-sample subdirs are created under it.

-
threads ( `int `(default: `4 `)) – Threads per cutadapt invocation.

-
jobs ( `Optional `[ `int `] (default: `None `)) – Concurrent sample jobs (default: CPU/2, capped by sample count).

-
output_gzip ( `Optional `[ `bool `] (default: `None `)) – Force gzipped output; `None `follows input suffix.

-
discard_untrimmed ( `bool `(default: `True `)) – Drop read pairs where primers were not found (standard for 16S).

-
min_length ( `int `(default: `50 `)) – Minimum post-trim length; pairs shorter than this are dropped.

-
max_n ( `Optional `[ `int `] (default: `0 `)) – Maximum ambiguous bases allowed per read ( `None `disables filter).

-
extra_args ( `Optional `[ `Sequence `[ `str `]] (default: `None `)) – Additional cutadapt CLI arguments appended verbatim.

-
cutadapt_path ( `Optional `[ `str `] (default: `None `)) – Explicit path to `cutadapt `executable.

-
auto_install ( `bool `(default: `True `)) – Try to install via conda when missing.

-
overwrite ( `bool `(default: `False `)) – Re-run and overwrite existing outputs.
