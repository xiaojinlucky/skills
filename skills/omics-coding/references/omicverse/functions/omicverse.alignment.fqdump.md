# omicverse.alignment.fqdump #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.fqdump`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.fqdump.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Convert SRA accessions to FASTQ.

## Signature

```text
omicverse.alignment. fqdump ( sra_ids , output_dir = 'fastq' , threads = 8 , memory = '4G' , temp_dir = None , gzip = False , library_layout = 'auto' , jobs = None , max_workers = None , retries = 2 , sra_dir = None , fasterq_path = None , auto_install = True , force = False )
```

## Parameters

- `sra_ids`: ( Union [ str , Sequence [ str ]] ) – SRR accession (str) or list of accessions.
- `output_dir`: ( str (default: 'fastq' )) – Output directory for FASTQ files (per-sample subdir).
- `threads`: ( int (default: 8 )) – Threads per fasterq-dump job.
- `memory`: ( str (default: '4G' )) – Memory limit passed to –mem (e.g. ‘4G’).
- `temp_dir`: ( Optional [ str ] (default: None )) – Temporary directory root for fasterq-dump.
- `gzip`: ( bool (default: False )) – Compress FASTQ outputs with pigz/gzip.
- `library_layout`: ( str (default: 'auto' )) – ‘auto’, ‘single’, or ‘paired’.
- `jobs`: ( Optional [ int ] (default: None )) – Concurrent jobs.
- `max_workers`: ( Optional [ int ] (default: None )) – Legacy alias for jobs.
- `retries`: ( int (default: 2 )) – Retries per accession.
- `sra_dir`: ( Optional [ str ] (default: None )) – Directory containing prefetched .sra/.sralite files.
- `fasterq_path`: ( Optional [ str ] (default: None )) – Explicit path to fasterq-dump.
- `force`: ( bool (default: False )) – Force overwrite existing output files (adds –force).
- `auto_install`: ( bool (default: True )) – Install missing tools automatically when possible.

## Full Documentation

# omicverse.alignment.fqdump #

omicverse.alignment. fqdump ( sra_ids , output_dir = 'fastq' , threads = 8 , memory = '4G' , temp_dir = None , gzip = False , library_layout = 'auto' , jobs = None , max_workers = None , retries = 2 , sra_dir = None , fasterq_path = None , auto_install = True , force = False ) [source] #

Convert SRA accessions to FASTQ.

Parameters :

-
sra_ids ( `Union `[ `str `, `Sequence `[ `str `]] ) – SRR accession (str) or list of accessions.

-
output_dir ( `str `(default: `'fastq' `)) – Output directory for FASTQ files (per-sample subdir).

-
threads ( `int `(default: `8 `)) – Threads per fasterq-dump job.

-
memory ( `str `(default: `'4G' `)) – Memory limit passed to –mem (e.g. ‘4G’).

-
temp_dir ( `Optional `[ `str `] (default: `None `)) – Temporary directory root for fasterq-dump.

-
gzip ( `bool `(default: `False `)) – Compress FASTQ outputs with pigz/gzip.

-
library_layout ( `str `(default: `'auto' `)) – ‘auto’, ‘single’, or ‘paired’.

-
jobs ( `Optional `[ `int `] (default: `None `)) – Concurrent jobs.

-
max_workers ( `Optional `[ `int `] (default: `None `)) – Legacy alias for jobs.

-
retries ( `int `(default: `2 `)) – Retries per accession.

-
sra_dir ( `Optional `[ `str `] (default: `None `)) – Directory containing prefetched .sra/.sralite files.

-
fasterq_path ( `Optional `[ `str `] (default: `None `)) – Explicit path to fasterq-dump.

-
force ( `bool `(default: `False `)) – Force overwrite existing output files (adds –force).

-
auto_install ( `bool `(default: `True `)) – Install missing tools automatically when possible.
