# omicverse.alignment.parallel_fastq_dump #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.parallel_fastq_dump`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.parallel_fastq_dump.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Download SRA data in parallel using parallel-fastq-dump.

## Signature

```text
omicverse.alignment. parallel_fastq_dump ( sra_id , threads = 1 , outdir = '.' , tmpdir = None , min_spot_id = 1 , max_spot_id = None , split_files = False , gzip = False , ** kwargs )
```

## Parameters

- `sra_id`: ( str ) – SRA accession ID (for example SRR2244401 ).
- `threads`: ( int , optional ) – Number of parallel threads used by parallel-fastq-dump .
- `outdir`: ( str , optional ) – Output directory for downloaded FASTQ files.
- `tmpdir`: ( str | None , optional ) – Temporary directory for chunk/intermediate files.
- `min_spot_id`: ( int , optional ) – Minimum SRA spot ID to download.
- `max_spot_id`: ( int | None , optional ) – Maximum SRA spot ID to download. None downloads all remaining spots.
- `split_files`: ( bool , optional ) – Split paired-end reads into separate *_1 / *_2 FASTQ files.
- `gzip`: ( bool , optional ) – Compress output FASTQ files using gzip.
- `**kwargs`: – Additional flags passed through to parallel-fastq-dump .

## Full Documentation

# omicverse.alignment.parallel_fastq_dump #

omicverse.alignment. parallel_fastq_dump ( sra_id , threads = 1 , outdir = '.' , tmpdir = None , min_spot_id = 1 , max_spot_id = None , split_files = False , gzip = False , ** kwargs ) [source] #

Download SRA data in parallel using parallel-fastq-dump.

This function wraps the parallel-fastq-dump tool to download sequencing data from NCBI SRA (Sequence Read Archive) in parallel for faster downloads.

Parameters :

-
sra_id ( str ) – SRA accession ID (for example `SRR2244401 `).

-
threads ( int , optional ) – Number of parallel threads used by `parallel-fastq-dump `.

-
outdir ( str , optional ) – Output directory for downloaded FASTQ files.

-
tmpdir ( str | None , optional ) – Temporary directory for chunk/intermediate files.

-
min_spot_id ( int , optional ) – Minimum SRA spot ID to download.

-
max_spot_id ( int | None , optional ) – Maximum SRA spot ID to download. `None `downloads all remaining spots.

-
split_files ( bool , optional ) – Split paired-end reads into separate `*_1 `/ `*_2 `FASTQ files.

-
gzip ( bool , optional ) – Compress output FASTQ files using gzip.

-
**kwargs – Additional flags passed through to `parallel-fastq-dump `.

Returns :

-
dict[str,str|int] – Download metadata including input parameters and discovered output FASTQ paths.

-
Examples – >>> import omicverse as ov >>> # Download SRA data with 4 threads and split files >>> result = ov.alignment.parallel_fastq_dump( … sra_id=’SRR2244401’, … threads=4, … outdir=’fastq_output/’, … split_files=True, … gzip=True … ) >>> # Download with spot range limit >>> result = ov.alignment.parallel_fastq_dump( … sra_id=’SRR2244401’, … threads=8, … outdir=’fastq_output/’, … min_spot_id=1, … max_spot_id=100000, … split_files=True, … gzip=True … )
