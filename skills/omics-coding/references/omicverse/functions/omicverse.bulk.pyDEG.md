# omicverse.bulk.pyDEG #

- Package: omicverse
- Language: Python
- Function: `omicverse.bulk.pyDEG`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.bulk.pyDEG.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Differential-expression analysis helper for bulk RNA-seq count tables.

## Signature

```text
class omicverse.bulk. pyDEG ( raw_data )
```

## Parameters

- `raw_data`: ( pd.DataFrame ) – Raw count matrix with genes in rows and samples in columns.

## Full Documentation

# omicverse.bulk.pyDEG #

class omicverse.bulk. pyDEG ( raw_data ) [source] #

Differential-expression analysis helper for bulk RNA-seq count tables.

Parameters :

raw_data ( pd.DataFrame ) – Raw count matrix with genes in rows and samples in columns.

__init__ ( raw_data ) [source] #

Initialize the pyDEG class.

Parameters :

raw_data ( `DataFrame `) – The raw data to be processed.

Returns :

None

Methods

`__init__ `(raw_data)

Initialize the pyDEG class.

`continuous_deg `(trait[, covariates, alpha, ...])

Differential expression against a CONTINUOUS sample-level trait.

`deg_analysis `(group1, group2[, method, ...])

Differential expression analysis.

`drop_duplicates_index `()

Drop the duplicated index of data.

`foldchange_set `([fc_threshold, ...])

Set fold-change and p-value thresholds to classify differentially expressed genes as up-regulated, down-regulated, or not significant.

`normalize `()

Normalize the data using DESeq2 method.

`plot_boxplot `(genes, treatment_groups, ...[, ...])

Plot the boxplot of genes from dds data

`plot_volcano `([figsize, pval_name, fc_name, ...])

Generate a volcano plot for the differential gene expression analysis results.

`ranking2gsea `([rank_max, rank_min])

Ranking the result of dds data for gsea analysis

`timecourse_deg `(time[, group, block, ...])

Time-course / longitudinal differential-expression analysis.
