# omicverse.alignment.STAR #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.STAR`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.STAR.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run STAR alignment.

## Signature

```text
omicverse.alignment. STAR ( samples , genome_dir , output_dir = 'star' , threads = 8 , memory = '50G' , jobs = None , max_workers = None , gtf = None , gtf_feature = 'exon' , sjdb_overhang = None , genome_fasta_files = None , auto_index = True , strict = False , genome_generate_threads = None , genome_generate_sjdb_overhang = None , genome_generate_gtf_feature = None , genome_generate_extra_args = None , extra_args = None , star_path = None , auto_install = True , overwrite = False )
```

## Parameters

- `samples`: ( Union [ Tuple [ str , str ], Tuple [ str , str , Optional [ str ]], Sequence [ Tuple [ str , str ]], Sequence [ Tuple [ str , str , Optional [ str ]]]] ) – Single sample tuple (sample, fq1[, fq2]) or list of such tuples.
- `genome_dir`: ( str ) – STAR genome index directory.
- `output_dir`: ( str (default: 'star' )) – Output directory for per-sample STAR outputs.
- `threads`: ( int (default: 8 )) – Threads per STAR job.
- `memory`: ( str (default: '50G' )) – Memory limit for BAM sorting (e.g. ‘50G’).
- `jobs`: ( Optional [ int ] (default: None )) – Concurrent jobs.
- `max_workers`: ( Optional [ int ] (default: None )) – Legacy alias for jobs.
- `gtf`: ( Optional [ str ] (default: None )) – Optional GTF for splice junctions.
- `gtf_feature`: ( Optional [ str ] (default: 'exon' )) – GTF feature name for exons (default: exon).
- `sjdb_overhang`: ( Optional [ int ] (default: None )) – Optional SJDB overhang.
- `genome_fasta_files`: ( Union [ str , Sequence [ str ], None ] (default: None )) – FASTA file(s) for auto-building STAR index if missing.
- `auto_index`: ( bool (default: True )) – If True, attempt to build STAR index automatically when missing.
- `strict`: ( bool (default: False )) – If True, raise errors; otherwise return error messages per sample.
- `genome_generate_threads`: ( Optional [ int ] (default: None )) – Threads for genomeGenerate (defaults to threads).
- `genome_generate_sjdb_overhang`: ( Optional [ int ] (default: None )) – sjdbOverhang used during genomeGenerate (defaults to sjdb_overhang).
- `genome_generate_gtf_feature`: ( Optional [ str ] (default: None )) – GTF feature name used during genomeGenerate (defaults to gtf_feature).
- `genome_generate_extra_args`: ( Optional [ Sequence [ str ]] (default: None )) – Extra args for genomeGenerate.
- `extra_args`: ( Optional [ Sequence [ str ]] (default: None )) – Additional STAR CLI arguments.
- `star_path`: ( Optional [ str ] (default: None )) – Explicit path to STAR executable.
- `auto_install`: ( bool (default: True )) – Install missing tools automatically when possible.
- `overwrite`: ( bool (default: False )) – If True, rerun STAR and overwrite existing outputs.

## Full Documentation

# omicverse.alignment.STAR #

omicverse.alignment. STAR ( samples , genome_dir , output_dir = 'star' , threads = 8 , memory = '50G' , jobs = None , max_workers = None , gtf = None , gtf_feature = 'exon' , sjdb_overhang = None , genome_fasta_files = None , auto_index = True , strict = False , genome_generate_threads = None , genome_generate_sjdb_overhang = None , genome_generate_gtf_feature = None , genome_generate_extra_args = None , extra_args = None , star_path = None , auto_install = True , overwrite = False ) [source] #

Run STAR alignment.

Parameters :

-
samples ( `Union `[ `Tuple `[ `str `, `str `], `Tuple `[ `str `, `str `, `Optional `[ `str `]], `Sequence `[ `Tuple `[ `str `, `str `]], `Sequence `[ `Tuple `[ `str `, `str `, `Optional `[ `str `]]]] ) – Single sample tuple (sample, fq1[, fq2]) or list of such tuples.

-
genome_dir ( `str `) – STAR genome index directory.

-
output_dir ( `str `(default: `'star' `)) – Output directory for per-sample STAR outputs.

-
threads ( `int `(default: `8 `)) – Threads per STAR job.

-
memory ( `str `(default: `'50G' `)) – Memory limit for BAM sorting (e.g. ‘50G’).

-
jobs ( `Optional `[ `int `] (default: `None `)) – Concurrent jobs.

-
max_workers ( `Optional `[ `int `] (default: `None `)) – Legacy alias for jobs.

-
gtf ( `Optional `[ `str `] (default: `None `)) – Optional GTF for splice junctions.

-
gtf_feature ( `Optional `[ `str `] (default: `'exon' `)) – GTF feature name for exons (default: exon).

-
sjdb_overhang ( `Optional `[ `int `] (default: `None `)) – Optional SJDB overhang.

-
genome_fasta_files ( `Union `[ `str `, `Sequence `[ `str `], `None `] (default: `None `)) – FASTA file(s) for auto-building STAR index if missing.

-
auto_index ( `bool `(default: `True `)) – If True, attempt to build STAR index automatically when missing.

-
strict ( `bool `(default: `False `)) – If True, raise errors; otherwise return error messages per sample.

-
genome_generate_threads ( `Optional `[ `int `] (default: `None `)) – Threads for genomeGenerate (defaults to threads).

-
genome_generate_sjdb_overhang ( `Optional `[ `int `] (default: `None `)) – sjdbOverhang used during genomeGenerate (defaults to sjdb_overhang).

-
genome_generate_gtf_feature ( `Optional `[ `str `] (default: `None `)) – GTF feature name used during genomeGenerate (defaults to gtf_feature).

-
genome_generate_extra_args ( `Optional `[ `Sequence `[ `str `]] (default: `None `)) – Extra args for genomeGenerate.

-
extra_args ( `Optional `[ `Sequence `[ `str `]] (default: `None `)) – Additional STAR CLI arguments.

-
star_path ( `Optional `[ `str `] (default: `None `)) – Explicit path to STAR executable.

-
auto_install ( `bool `(default: `True `)) – Install missing tools automatically when possible.

-
overwrite ( `bool `(default: `False `)) – If True, rerun STAR and overwrite existing outputs.
