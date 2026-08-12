# Run scATAC quality control metrics

- Package: scop
- Language: R
- Function: `RunATACQC`
- Source: https://mengxu98.github.io/scop/reference/RunATACQC.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunATACQC.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Calculate common scATAC QC metrics and optionally filter cells by thresholds.

## Signature

```text
RunATACQC( srt, assay = NULL, tss.positions = NULL, blacklist = NULL, fast = TRUE, min_pct_reads_in_peaks = NULL, min_TSS_enrichment = NULL, max_nucleosome_signal = NULL, max_blacklist_ratio = NULL, verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `tss.positions`: TSS positions passed to Signac::TSSEnrichment.
- `blacklist`: A GRanges blacklist used to compute blacklist_ratio.
- `fast`: Whether to use the fast mode in Signac::TSSEnrichment.
- `min_pct_reads_in_peaks, min_TSS_enrichment, max_nucleosome_signal, max_blacklist_ratio`: Optional thresholds used for filtering cells.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Run scATAC quality control metrics

## Usage

```text
RunATACQC( srt, assay = NULL, tss.positions = NULL, blacklist = NULL, fast = TRUE, min_pct_reads_in_peaks = NULL, min_TSS_enrichment = NULL, max_nucleosome_signal = NULL, max_blacklist_ratio = NULL, verbose = TRUE )
```

## Description

Calculate common scATAC QC metrics and optionally filter cells by thresholds.

## Value

A Seurat object with QC metadata added.

## Examples

```r
\donttest{
data("pbmcmultiome_sub", package = "scop")
pbmcmultiome_sub <- RunATACQC(
  pbmcmultiome_sub,
  assay = "peaks",
  fast = TRUE
)
}
```
