# omicverse.bulk.Matrix_ID_mapping #

- Package: omicverse
- Language: Python
- Function: `omicverse.bulk.Matrix_ID_mapping`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.bulk.Matrix_ID_mapping.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Map gene IDs in the input data to gene symbols using a reference table.

## Signature

```text
omicverse.bulk. Matrix_ID_mapping ( data , gene_ref_path , keep_unmapped = True , auto_download = True )
```

## Parameters

- `data`: ( DataFrame ) – The input data containing gene IDs as index.
- `gene_ref_path`: ( str ) – The path to the reference table containing the mapping from gene IDs to gene symbols.
- `keep_unmapped`: ( bool (default: True )) – Whether to keep genes that are not found in the mapping table. If True, unmapped genes retain their original IDs. If False, unmapped genes are removed (original behavior). Default: True.
- `auto_download`: ( bool (default: True )) – If the reference at gene_ref_path is missing AND its basename matches a known omicverse pair ( pair_GRCh38.tsv , pair_GRCh37.tsv , pair_GRCm39.tsv , pair_danRer11.tsv ), call ov.utils.download_geneid_annotation_pair() to fetch the standard pairs into ./genesets/ and resolve from there.

## Full Documentation

# omicverse.bulk.Matrix_ID_mapping #

omicverse.bulk. Matrix_ID_mapping ( data , gene_ref_path , keep_unmapped = True , auto_download = True ) [source] #

Map gene IDs in the input data to gene symbols using a reference table.

Parameters :

-
data ( `DataFrame `) – The input data containing gene IDs as index.

-
gene_ref_path ( `str `) – The path to the reference table containing the mapping from gene IDs to gene symbols.

-
keep_unmapped ( `bool `(default: `True `)) – Whether to keep genes that are not found in the mapping table. If True, unmapped genes retain their original IDs. If False, unmapped genes are removed (original behavior). Default: True.

-
auto_download ( `bool `(default: `True `)) – If the reference at `gene_ref_path `is missing AND its basename matches a known omicverse pair ( `pair_GRCh38.tsv `, `pair_GRCh37.tsv `, `pair_GRCm39.tsv `, `pair_danRer11.tsv `), call `ov.utils.download_geneid_annotation_pair() `to fetch the standard pairs into `./genesets/ `and resolve from there.

Returns :

The input data with gene IDs mapped to gene symbols.

Return type :

data
