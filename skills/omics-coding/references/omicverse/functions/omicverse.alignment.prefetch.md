# omicverse.alignment.prefetch #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.prefetch`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.prefetch.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Prefetch SRA accessions with validation.

## Signature

```text
omicverse.alignment. prefetch ( sra_ids , output_dir = 'prefetch' , threads = 4 , jobs = None , max_workers = None , retries = 2 , validate = True , transport = None , location = None , prefetch_path = None , vdb_validate_path = None , link_mode = 'symlink' , auto_install = True , progress_minutes = 1 , force = None )
```

## Parameters

- `sra_ids`: ( Union [ str , Sequence [ str ]] ) – SRR accession (str) or list of accessions.
- `output_dir`: ( str (default: 'prefetch' )) – Output directory for downloaded .sra/.sralite files.
- `threads`: ( int (default: 4 )) – Default concurrency when jobs is not provided (kept for compatibility).
- `jobs`: ( Optional [ int ] (default: None )) – Number of concurrent downloads (preferred).
- `max_workers`: ( Optional [ int ] (default: None )) – Legacy alias for jobs.
- `retries`: ( int (default: 2 )) – Retries per accession.
- `validate`: ( bool (default: True )) – Run vdb-validate on the downloaded file.
- `transport`: ( Optional [ str ] (default: None )) – Optional prefetch –transport value (e.g. ‘https’).
- `location`: ( Optional [ str ] (default: None )) – Optional prefetch –location value (e.g. ‘ncbi’, ‘ena’).
- `prefetch_path`: ( Optional [ str ] (default: None )) – Explicit path to prefetch executable.
- `vdb_validate_path`: ( Optional [ str ] (default: None )) – Explicit path to vdb-validate executable.
- `link_mode`: ( str (default: 'symlink' )) – symlink, hardlink, or copy (fallback).
- `auto_install`: ( bool (default: True )) – Install missing tools automatically when possible.
- `progress_minutes`: ( int (default: 1 )) – Prefetch progress interval in minutes (0 disables progress).
- `force`: ( Optional [ str ] (default: None )) – Optional prefetch force mode: “no”, “yes”, or “all”.

## Full Documentation

# omicverse.alignment.prefetch #

omicverse.alignment. prefetch ( sra_ids , output_dir = 'prefetch' , threads = 4 , jobs = None , max_workers = None , retries = 2 , validate = True , transport = None , location = None , prefetch_path = None , vdb_validate_path = None , link_mode = 'symlink' , auto_install = True , progress_minutes = 1 , force = None ) [source] #

Prefetch SRA accessions with validation.

Parameters :

-
sra_ids ( `Union `[ `str `, `Sequence `[ `str `]] ) – SRR accession (str) or list of accessions.

-
output_dir ( `str `(default: `'prefetch' `)) – Output directory for downloaded .sra/.sralite files.

-
threads ( `int `(default: `4 `)) – Default concurrency when jobs is not provided (kept for compatibility).

-
jobs ( `Optional `[ `int `] (default: `None `)) – Number of concurrent downloads (preferred).

-
max_workers ( `Optional `[ `int `] (default: `None `)) – Legacy alias for jobs.

-
retries ( `int `(default: `2 `)) – Retries per accession.

-
validate ( `bool `(default: `True `)) – Run vdb-validate on the downloaded file.

-
transport ( `Optional `[ `str `] (default: `None `)) – Optional prefetch –transport value (e.g. ‘https’).

-
location ( `Optional `[ `str `] (default: `None `)) – Optional prefetch –location value (e.g. ‘ncbi’, ‘ena’).

-
prefetch_path ( `Optional `[ `str `] (default: `None `)) – Explicit path to prefetch executable.

-
vdb_validate_path ( `Optional `[ `str `] (default: `None `)) – Explicit path to vdb-validate executable.

-
link_mode ( `str `(default: `'symlink' `)) – symlink, hardlink, or copy (fallback).

-
auto_install ( `bool `(default: `True `)) – Install missing tools automatically when possible.

-
progress_minutes ( `int `(default: `1 `)) – Prefetch progress interval in minutes (0 disables progress).

-
force ( `Optional `[ `str `] (default: `None `)) – Optional prefetch force mode: “no”, “yes”, or “all”.
