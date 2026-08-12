# omicverse.alignment.featureCount #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.featureCount`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.featureCount.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run featureCounts on BAM files.

## Signature

```text
omicverse.alignment. featureCount ( bam_items , gtf , output_dir = 'counts' , threads = 8 , jobs = None , max_workers = None , simple = True , merge_matrix = True , quiet = True , gene_mapping = False , gene_map = None , gene_name_field = 'gene_name' , overwrite = False , featurecounts_path = None , auto_install = True , strict = False , auto_fix = True )
```

## Parameters

- `bam_items`: ( Union [ Tuple [ str , str ], Tuple [ str , str , bool ], Sequence [ Tuple [ str , str ]], Sequence [ Tuple [ str , str , bool ]]] ) – Single tuple (sample, bam[, is_paired]) or list of tuples.
- `gtf`: ( str ) – GTF annotation file.
- `output_dir`: ( str (default: 'counts' )) – Output directory for count files.
- `threads`: ( int (default: 8 )) – Threads per featureCounts job.
- `jobs`: ( Optional [ int ] (default: None )) – Concurrent jobs.
- `max_workers`: ( Optional [ int ] (default: None )) – Legacy alias for jobs.
- `simple`: ( bool (default: True )) – Simplify output to gene_id + counts.
- `merge_matrix`: ( bool (default: True )) – Merge per-sample count files into a single CSV matrix (multiple samples only).
- `quiet`: ( bool (default: True )) – Suppress featureCounts command output.
- `gene_mapping`: ( bool (default: False )) – Map gene_id to gene_name when exporting simplified counts/matrix.
- `gene_map`: ( Union [ Mapping [ str , str ], str , None ] (default: None )) – Optional mapping dict or file (TSV/CSV or GTF) for gene_id -> gene_name.
- `gene_name_field`: ( str (default: 'gene_name' )) – Attribute name in GTF for gene name (default: gene_name).
- `overwrite`: ( bool (default: False )) – If True, rerun featureCounts and regenerate outputs even if files exist.
- `featurecounts_path`: ( Optional [ str ] (default: None )) – Explicit path to featureCounts.
- `auto_install`: ( bool (default: True )) – Install missing tools automatically when possible.
- `strict`: ( bool (default: False )) – If True, raise errors; otherwise return error messages per sample.
- `auto_fix`: ( bool (default: True )) – If True, attempt simple retries (e.g. rerun without paired flags).

## Full Documentation

# omicverse.alignment.featureCount #

omicverse.alignment. featureCount ( bam_items , gtf , output_dir = 'counts' , threads = 8 , jobs = None , max_workers = None , simple = True , merge_matrix = True , quiet = True , gene_mapping = False , gene_map = None , gene_name_field = 'gene_name' , overwrite = False , featurecounts_path = None , auto_install = True , strict = False , auto_fix = True ) [source] #

Run featureCounts on BAM files.

Parameters :

-
bam_items ( `Union `[ `Tuple `[ `str `, `str `], `Tuple `[ `str `, `str `, `bool `], `Sequence `[ `Tuple `[ `str `, `str `]], `Sequence `[ `Tuple `[ `str `, `str `, `bool `]]] ) – Single tuple (sample, bam[, is_paired]) or list of tuples.

-
gtf ( `str `) – GTF annotation file.

-
output_dir ( `str `(default: `'counts' `)) – Output directory for count files.

-
threads ( `int `(default: `8 `)) – Threads per featureCounts job.

-
jobs ( `Optional `[ `int `] (default: `None `)) – Concurrent jobs.

-
max_workers ( `Optional `[ `int `] (default: `None `)) – Legacy alias for jobs.

-
simple ( `bool `(default: `True `)) – Simplify output to gene_id + counts.

-
merge_matrix ( `bool `(default: `True `)) – Merge per-sample count files into a single CSV matrix (multiple samples only).

-
quiet ( `bool `(default: `True `)) – Suppress featureCounts command output.

-
gene_mapping ( `bool `(default: `False `)) – Map gene_id to gene_name when exporting simplified counts/matrix.

-
gene_map ( `Union `[ `Mapping `[ `str `, `str `], `str `, `None `] (default: `None `)) – Optional mapping dict or file (TSV/CSV or GTF) for gene_id -> gene_name.

-
gene_name_field ( `str `(default: `'gene_name' `)) – Attribute name in GTF for gene name (default: gene_name).

-
overwrite ( `bool `(default: `False `)) – If True, rerun featureCounts and regenerate outputs even if files exist.

-
featurecounts_path ( `Optional `[ `str `] (default: `None `)) – Explicit path to featureCounts.

-
auto_install ( `bool `(default: `True `)) – Install missing tools automatically when possible.

-
strict ( `bool `(default: `False `)) – If True, raise errors; otherwise return error messages per sample.

-
auto_fix ( `bool `(default: `True `)) – If True, attempt simple retries (e.g. rerun without paired flags).
