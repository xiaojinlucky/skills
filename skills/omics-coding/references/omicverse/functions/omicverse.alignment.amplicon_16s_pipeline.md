# omicverse.alignment.amplicon_16s_pipeline #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.amplicon_16s_pipeline`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.amplicon_16s_pipeline.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run the full 16S amplicon pipeline.

## Signature

```text
omicverse.alignment. amplicon_16s_pipeline ( fastq_dir = None , samples = None , workdir = None , db_fasta = None , * , primer_fwd = None , primer_rev = None , backend = 'vsearch' , threads = 4 , jobs = None , merge_max_diffs = 10 , merge_min_overlap = 16 , filter_max_ee = 1.0 , filter_min_len = 0 , filter_max_len = 0 , derep_min_uniq = 2 , unoise_alpha = 2.0 , unoise_minsize = 2 , chimera_removal = True , otutab_identity = 0.97 , sintax_cutoff = 0.8 , sintax_strand = 'both' , sample_metadata = None , overwrite = False )
```

## Parameters

- `fastq_dir`: ( Optional [ str ] (default: None )) – Directory containing paired Illumina FASTQs. Samples are auto-discovered by R1/R2 naming. Mutually exclusive with samples .
- `samples`: ( Optional [ Sequence [ Tuple [ str , str , Optional [ str ]]]] (default: None )) – Explicit list of (sample, fq1, fq2) tuples (fq2 may be None for single-end). Mutually exclusive with fastq_dir .
- `workdir`: ( Optional [ str ] (default: None )) – Root directory for all intermediate files. No $HOME fallback.
- `db_fasta`: ( Optional [ str ] (default: None )) – Path to a SINTAX-formatted 16S reference FASTA ( .fa or .fa.gz ). If None , taxonomy assignment is skipped.
- `primer_fwd`: ( Optional [ str ] (default: None )) – PCR primer sequences. When both are provided, cutadapt() runs first; otherwise primer trimming is skipped (e.g. the mothur MiSeq SOP test dataset ships with primers already removed).
- `primer_rev`: ( Optional [ str ] (default: None )) – PCR primer sequences. When both are provided, cutadapt() runs first; otherwise primer trimming is skipped (e.g. the mothur MiSeq SOP test dataset ships with primers already removed).
- `backend`: ( str (default: 'vsearch' )) – 'vsearch' (default) — UNOISE3 via vsearch. 'dada2' — pure-Python DADA2 via omicverse.alignment.dada2_pipeline() (needs pip install pydada2 ). 'emu' / 'qiime2' still raise NotImplementedError .
- `threads`: ( int (default: 4 )) – CPU parallelism.
- `jobs`: ( Optional [ int ] (default: None )) – CPU parallelism.
- `overwrite`: ( bool (default: False )) – If True, re-run each step regardless of existing outputs.
- `merge_max_diffs`: ( int (default: 10 ))
- `merge_min_overlap`: ( int (default: 16 ))
- `filter_max_ee`: ( float (default: 1.0 ))
- `filter_min_len`: ( int (default: 0 ))
- `filter_max_len`: ( int (default: 0 ))
- `derep_min_uniq`: ( int (default: 2 ))
- `unoise_alpha`: ( float (default: 2.0 ))
- `unoise_minsize`: ( int (default: 2 ))
- `chimera_removal`: ( bool (default: True ))
- `otutab_identity`: ( float (default: 0.97 ))
- `sintax_cutoff`: ( float (default: 0.8 ))
- `sintax_strand`: ( str (default: 'both' ))
- `sample_metadata`: ( Optional [ DataFrame ] (default: None ))

## Full Documentation

# omicverse.alignment.amplicon_16s_pipeline #

omicverse.alignment. amplicon_16s_pipeline ( fastq_dir = None , samples = None , workdir = None , db_fasta = None , * , primer_fwd = None , primer_rev = None , backend = 'vsearch' , threads = 4 , jobs = None , merge_max_diffs = 10 , merge_min_overlap = 16 , filter_max_ee = 1.0 , filter_min_len = 0 , filter_max_len = 0 , derep_min_uniq = 2 , unoise_alpha = 2.0 , unoise_minsize = 2 , chimera_removal = True , otutab_identity = 0.97 , sintax_cutoff = 0.8 , sintax_strand = 'both' , sample_metadata = None , overwrite = False ) [source] #

Run the full 16S amplicon pipeline.

Parameters :

-
fastq_dir ( `Optional `[ `str `] (default: `None `)) – Directory containing paired Illumina FASTQs. Samples are auto-discovered by R1/R2 naming. Mutually exclusive with `samples `.

-
samples ( `Optional `[ `Sequence `[ `Tuple `[ `str `, `str `, `Optional `[ `str `]]]] (default: `None `)) – Explicit list of `(sample, fq1, fq2) `tuples (fq2 may be None for single-end). Mutually exclusive with `fastq_dir `.

-
workdir ( `Optional `[ `str `] (default: `None `)) – Root directory for all intermediate files. No `$HOME `fallback.

-
db_fasta ( `Optional `[ `str `] (default: `None `)) – Path to a SINTAX-formatted 16S reference FASTA ( `.fa `or `.fa.gz `). If `None `, taxonomy assignment is skipped.

-
primer_fwd ( `Optional `[ `str `] (default: `None `)) – PCR primer sequences. When both are provided, `cutadapt() `runs first; otherwise primer trimming is skipped (e.g. the mothur MiSeq SOP test dataset ships with primers already removed).

-
primer_rev ( `Optional `[ `str `] (default: `None `)) – PCR primer sequences. When both are provided, `cutadapt() `runs first; otherwise primer trimming is skipped (e.g. the mothur MiSeq SOP test dataset ships with primers already removed).

-
backend ( `str `(default: `'vsearch' `)) – `'vsearch' `(default) — UNOISE3 via vsearch. `'dada2' `— pure-Python DADA2 via `omicverse.alignment.dada2_pipeline() `(needs `pip install pydada2 `). `'emu' `/ `'qiime2' `still raise `NotImplementedError `.

-
threads ( `int `(default: `4 `)) – CPU parallelism.

-
jobs ( `Optional `[ `int `] (default: `None `)) – CPU parallelism.

-
overwrite ( `bool `(default: `False `)) – If True, re-run each step regardless of existing outputs.

-
merge_max_diffs ( `int `(default: `10 `))

-
merge_min_overlap ( `int `(default: `16 `))

-
filter_max_ee ( `float `(default: `1.0 `))

-
filter_min_len ( `int `(default: `0 `))

-
filter_max_len ( `int `(default: `0 `))

-
derep_min_uniq ( `int `(default: `2 `))

-
unoise_alpha ( `float `(default: `2.0 `))

-
unoise_minsize ( `int `(default: `2 `))

-
chimera_removal ( `bool `(default: `True `))

-
otutab_identity ( `float `(default: `0.97 `))

-
sintax_cutoff ( `float `(default: `0.8 `))

-
sintax_strand ( `str `(default: `'both' `))

-
sample_metadata ( `Optional `[ `DataFrame `] (default: `None `))

Returns :

Samples × ASVs matrix with taxonomy / sequence / confidence in `var `. Sample metadata (if provided) is merged into `obs `.

Return type :

anndata.AnnData
