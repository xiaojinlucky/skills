# Convert CCC results to a LIANA-like table

- Package: scop
- Language: R
- Function: `ccc_to_liana`
- Source: https://mengxu98.github.io/scop/reference/ccc_to_liana.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/ccc_to_liana.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Convert CCC results to a LIANA-like table

## Signature

```text
ccc_to_liana( srt, method = NULL, condition = NULL, dataset = 1, slot.name = "net", signaling = NULL, pairLR.use = NULL, sender.use = NULL, receiver.use = NULL, ligand.use = NULL, receptor.use = NULL, interaction.use = NULL, thresh = 0.05, result = c("primary", "consensus", "legacy", "raw"), aggregate = TRUE, sample_col = NULL, score_col = "score", pvalue_col = "pvalue" )
```

## Parameters

- `srt`: A Seurat object.
- `method`: Communication result type to use.
- `condition`: Result name or comparison name.
- `dataset`: Dataset index or name.
- `slot.name`: CellChat slot name.
- `signaling`: Signaling pathway to focus on.
- `pairLR.use`: Specific ligand-receptor pair(s) to keep.
- `sender.use`: Sender cell types to keep.
- `receiver.use`: Receiver cell types to keep.
- `ligand.use`: Ligands to keep.
- `receptor.use`: Receptors to keep.
- `interaction.use`: Interaction names to keep.
- `thresh`: Significance threshold used when extracting communication results.
- `result`: LIANA result representation to export. "primary" prefers the official consensus, "consensus" requires it, "legacy" uses scop's historical post-processing, and "raw" uses method-specific rows.
- `aggregate`: Whether to aggregate duplicate source-target-ligand-receptor rows. This should usually stay TRUE for OmicVerse compatibility.
- `sample_col`: Optional column used as sample/context/dataset key. If NULL, the first available column among "sample", "context", "condition", and "dataset" is used.
- `score_col`: Column used as the exported communication score.
- `pvalue_col`: Column used as the exported p-value/rank-like support.

## Full Documentation

# Convert CCC results to a LIANA-like table

## Usage

```text
ccc_to_liana( srt, method = NULL, condition = NULL, dataset = 1, slot.name = "net", signaling = NULL, pairLR.use = NULL, sender.use = NULL, receiver.use = NULL, ligand.use = NULL, receptor.use = NULL, interaction.use = NULL, thresh = 0.05, result = c("primary", "consensus", "legacy", "raw"), aggregate = TRUE, sample_col = NULL, score_col = "score", pvalue_col = "pvalue" )
```

## Description

Convert CCC results to a LIANA-like table

## Value

A data frame with LIANA/LIANA+ compatible columns: source, target, ligand_complex, receptor_complex, score, and pvalue, plus scop/OV-friendly metadata.
