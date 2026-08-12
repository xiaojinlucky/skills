# omicverse.utils.get_gene_annotation #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.get_gene_annotation`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.get_gene_annotation.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Annotate adata.var by merging with gene-level GTF attributes.

## Signature

```text
omicverse.utils. get_gene_annotation ( adata , var_by = None , gtf = None , gtf_by = None , by_func = None )
```

## Parameters

- `adata`: ( Input dataset. )
- `var_by`: (Specify a column in adata.var used to merge with GTF attributes,) – otherwise adata.var_names is used by default.
- `gtf`: ( Path to the GTF file. )
- `gtf_by`: (Specify a field in the GTF attributes used to merge with adata.var ,) – e.g. “gene_id”, “gene_name”.
- `by_func`: ( Specify an element-wise function used to transform merging fields , ) – e.g. removing suffix in gene IDs.

## Full Documentation

# omicverse.utils.get_gene_annotation #

omicverse.utils. get_gene_annotation ( adata , var_by = None , gtf = None , gtf_by = None , by_func = None ) [source] #

Annotate `adata.var `by merging with gene-level GTF attributes.

Parameters :

-
adata ( Input dataset. )

-
var_by (Specify a column in `adata.var `used to merge with GTF attributes,) – otherwise `adata.var_names `is used by default.

-
gtf ( Path to the GTF file. )

-
gtf_by (Specify a field in the GTF attributes used to merge with `adata.var `,) – e.g. “gene_id”, “gene_name”.

-
by_func ( Specify an element-wise function used to transform merging fields , ) – e.g. removing suffix in gene IDs.

Note

The genomic locations are converted to 0-based as specified in bed format rather than 1-based as specified in GTF format.
