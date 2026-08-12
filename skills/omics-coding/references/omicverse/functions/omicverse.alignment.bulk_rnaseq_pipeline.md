# omicverse.alignment.bulk_rnaseq_pipeline #

- Package: omicverse
- Language: Python
- Function: `omicverse.alignment.bulk_rnaseq_pipeline`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.alignment.bulk_rnaseq_pipeline.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run a complete bulk RNA-seq pipeline from SRA accessions or local FASTQs.

## Signature

```text
omicverse.alignment. bulk_rnaseq_pipeline ( sra_ids = None , samples = None , genome_dir = 'star_index' , gtf = 'genes.gtf' , output_dir = 'pipeline_output' , genome_fasta_files = None , threads = 8 , memory = '50G' , jobs = None , skip_download = False , skip_qc = False , gzip_fastq = True , gene_mapping = True , auto_install = True , overwrite = False )
```

## Parameters

- `sra_ids`: ( str or list of str , optional ) – SRA accession IDs to download. Required unless samples is provided.
- `samples`: ( tuple or list of tuples , optional ) – Pre-existing FASTQ sample tuples (name, fq1, fq2_or_None) . When provided, the download step is skipped automatically.
- `genome_dir`: ( str ) – Path to (or for) the STAR genome index directory.
- `gtf`: ( str ) – Path to the GTF annotation file.
- `output_dir`: ( str ) – Root output directory. Sub-directories are created per step.
- `genome_fasta_files`: ( list of str , optional ) – Genome FASTA file(s) for auto-building the STAR index.
- `threads`: ( int ) – Threads per tool invocation.
- `memory`: ( str ) – Memory limit for STAR BAM sorting (e.g. '50G' ).
- `jobs`: ( int , optional ) – Number of concurrent jobs. None auto-detects.
- `skip_download`: ( bool ) – Skip the prefetch + fqdump steps (requires samples ).
- `skip_qc`: ( bool ) – Skip the fastp QC step.
- `gzip_fastq`: ( bool ) – Compress FASTQ output from fqdump.
- `gene_mapping`: ( bool ) – Map gene_id to gene_name in featureCounts output.
- `auto_install`: ( bool ) – Auto-install missing CLI tools via conda/mamba.
- `overwrite`: ( bool ) – Force re-run even when outputs already exist.

## Full Documentation

# omicverse.alignment.bulk_rnaseq_pipeline #

omicverse.alignment. bulk_rnaseq_pipeline ( sra_ids = None , samples = None , genome_dir = 'star_index' , gtf = 'genes.gtf' , output_dir = 'pipeline_output' , genome_fasta_files = None , threads = 8 , memory = '50G' , jobs = None , skip_download = False , skip_qc = False , gzip_fastq = True , gene_mapping = True , auto_install = True , overwrite = False ) [source] #

Run a complete bulk RNA-seq pipeline from SRA accessions or local FASTQs.

The pipeline chains: `prefetch `-> `fqdump `-> `fastp `-> `STAR `-> `featureCount `.

Parameters :

-
sra_ids ( str or list of str , optional ) – SRA accession IDs to download. Required unless samples is provided.

-
samples ( tuple or list of tuples , optional ) – Pre-existing FASTQ sample tuples `(name, fq1, fq2_or_None) `. When provided, the download step is skipped automatically.

-
genome_dir ( str ) – Path to (or for) the STAR genome index directory.

-
gtf ( str ) – Path to the GTF annotation file.

-
output_dir ( str ) – Root output directory. Sub-directories are created per step.

-
genome_fasta_files ( list of str , optional ) – Genome FASTA file(s) for auto-building the STAR index.

-
threads ( int ) – Threads per tool invocation.

-
memory ( str ) – Memory limit for STAR BAM sorting (e.g. `'50G' `).

-
jobs ( int , optional ) – Number of concurrent jobs. `None `auto-detects.

-
skip_download ( bool ) – Skip the prefetch + fqdump steps (requires samples ).

-
skip_qc ( bool ) – Skip the fastp QC step.

-
gzip_fastq ( bool ) – Compress FASTQ output from fqdump.

-
gene_mapping ( bool ) – Map gene_id to gene_name in featureCounts output.

-
auto_install ( bool ) – Auto-install missing CLI tools via conda/mamba.

-
overwrite ( bool ) – Force re-run even when outputs already exist.

Returns :

Merged gene-level count matrix (genes x samples).

Return type :

pandas.DataFrame
