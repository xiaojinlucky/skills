# omicverse.bulk.pyTCGA #

- Package: omicverse
- Language: Python
- Function: `omicverse.bulk.pyTCGA`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.bulk.pyTCGA.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

TCGA (The Cancer Genome Atlas) data analysis module.

## Signature

```text
class omicverse.bulk. pyTCGA ( gdc_sample_sheep , gdc_download_files , clinical_cart )
```

## Parameters

- `gdc_sample_sheep`: ( str )
- `gdc_download_files`: ( str )
- `clinical_cart`: ( str )

## Full Documentation

# omicverse.bulk.pyTCGA #

class omicverse.bulk. pyTCGA ( gdc_sample_sheep , gdc_download_files , clinical_cart ) [source] #

TCGA (The Cancer Genome Atlas) data analysis module.

This class provides comprehensive functionality for downloading, processing, and analyzing TCGA genomic and clinical data.

Parameters :

-
gdc_sample_sheep ( `str `)

-
gdc_download_files ( `str `)

-
clinical_cart ( `str `)

__init__ ( gdc_sample_sheep , gdc_download_files , clinical_cart ) [source] #

Initialize TCGA analysis module.

Parameters :

-
gdc_sample_sheep ( `str `) – Path to TCGA Sample Sheet TSV file

-
gdc_download_files ( `str `) – Path to downloaded TCGA data files directory

-
clinical_cart ( `str `) – Path to TCGA clinical data tar.gz file

Methods

`__init__ `(gdc_sample_sheep, ...)

Initialize TCGA analysis module.

`adata_init `()

`adata_meta_init `([var_names, obs_names])

Initialize AnnData metadata.

`adata_read `(path)

Read AnnData object from file.

`expression_init `()

Initialize expression matrices for TCGA data.

`index_init `()

Initialize gene indices for AnnData construction.

`matrix_construct `()

Construct AnnData object from expression matrices.

`matrix_normalize `(data)

Normalize expression matrix using DESeq2 method.

`survial_analysis_all `()

Perform survival analysis for all genes in the dataset.

`survial_init `()

Initialize survival analysis data.

`survival_analysis `(gene[, layer, plot, ...])

Perform survival analysis for a specific gene.
