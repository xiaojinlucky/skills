# omicverse.utils.gtf_to_pair_tsv #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.gtf_to_pair_tsv`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.gtf_to_pair_tsv.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Convert GTF file to gene ID mapping pairs TSV format.

## Signature

```text
omicverse.utils. gtf_to_pair_tsv ( gtf_path , output_path , gene_id_version = True )
```

## Parameters

- `gtf_path`: ( str ) – Path to input GTF file.
- `output_path`: ( str ) – Path for output TSV file.
- `gene_id_version`: ( bool ) – Whether to keep version numbers in gene IDs.

## Full Documentation

# omicverse.utils.gtf_to_pair_tsv #

omicverse.utils. gtf_to_pair_tsv ( gtf_path , output_path , gene_id_version = True ) [source] #

Convert GTF file to gene ID mapping pairs TSV format.

Parameters :

-
gtf_path ( str ) – Path to input GTF file.

-
output_path ( str ) – Path for output TSV file.

-
gene_id_version ( bool ) – Whether to keep version numbers in gene IDs.

Returns :

Number of unique genes written to output file.

Return type :

int

Examples

```text
>>> import omicverse as ov
>>> # Convert GTF to mapping pairs
>>> gene_count = ov.utils.gtf_to_pair_tsv('genes.gtf', 'gene_pairs.tsv')
>>> # Use converted file for gene mapping
>>> data = ov.bulk.Matrix_ID_mapping(data, 'gene_pairs.tsv')

```
