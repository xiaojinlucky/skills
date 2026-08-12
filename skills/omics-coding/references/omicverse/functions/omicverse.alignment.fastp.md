# omicverse.alignment.fastp #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.fastp`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.fastp.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run fastp QC.

## Signature

```text
omicverse.alignment. fastp ( samples , output_dir = 'fastp' , threads = 8 , jobs = None , max_workers = None , output_gzip = None , extra_args = None , fastp_path = None , auto_install = True , overwrite = False )
```

## Parameters

- `samples`: ( Union [ Tuple [ str , str , Optional [ str ]], Sequence [ Tuple [ str , str , Optional [ str ]]]] ) – (sample, fq1, fq2) tuple, list of such tuples, or a list of 1/2 FASTQ paths.
- `output_dir`: ( str (default: 'fastp' )) – Output directory for cleaned FASTQs (per-sample subdir).
- `threads`: ( int (default: 8 )) – Threads per fastp job.
- `jobs`: ( Optional [ int ] (default: None )) – Concurrent jobs.
- `max_workers`: ( Optional [ int ] (default: None )) – Legacy alias for jobs.
- `output_gzip`: ( Optional [ bool ] (default: None )) – Force output gzip; None follows input fq1 suffix.
- `extra_args`: ( Optional [ Sequence [ str ]] (default: None )) – Additional fastp CLI arguments.
- `fastp_path`: ( Optional [ str ] (default: None )) – Explicit path to fastp executable.
- `auto_install`: ( bool (default: True )) – Install missing tools automatically when possible.
- `overwrite`: ( bool (default: False )) – If True, rerun fastp and overwrite existing outputs.

## Full Documentation

# omicverse.alignment.fastp #

omicverse.alignment. fastp ( samples , output_dir = 'fastp' , threads = 8 , jobs = None , max_workers = None , output_gzip = None , extra_args = None , fastp_path = None , auto_install = True , overwrite = False ) [source] #

Run fastp QC.

Parameters :

-
samples ( `Union `[ `Tuple `[ `str `, `str `, `Optional `[ `str `]], `Sequence `[ `Tuple `[ `str `, `str `, `Optional `[ `str `]]]] ) – (sample, fq1, fq2) tuple, list of such tuples, or a list of 1/2 FASTQ paths.

-
output_dir ( `str `(default: `'fastp' `)) – Output directory for cleaned FASTQs (per-sample subdir).

-
threads ( `int `(default: `8 `)) – Threads per fastp job.

-
jobs ( `Optional `[ `int `] (default: `None `)) – Concurrent jobs.

-
max_workers ( `Optional `[ `int `] (default: `None `)) – Legacy alias for jobs.

-
output_gzip ( `Optional `[ `bool `] (default: `None `)) – Force output gzip; None follows input fq1 suffix.

-
extra_args ( `Optional `[ `Sequence `[ `str `]] (default: `None `)) – Additional fastp CLI arguments.

-
fastp_path ( `Optional `[ `str `] (default: `None `)) – Explicit path to fastp executable.

-
auto_install ( `bool `(default: `True `)) – Install missing tools automatically when possible.

-
overwrite ( `bool `(default: `False `)) – If True, rerun fastp and overwrite existing outputs.
