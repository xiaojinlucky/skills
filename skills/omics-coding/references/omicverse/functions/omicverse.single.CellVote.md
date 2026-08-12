# omicverse.single.CellVote #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.CellVote`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.CellVote.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Ensemble cell-type annotation manager with multiple backends.

## Signature

```text
class omicverse.single. CellVote ( adata )
```

## Parameters

- `adata`: ( AnnData ) – Query single-cell AnnData to annotate.

## Full Documentation

# omicverse.single.CellVote #

class omicverse.single. CellVote ( adata ) [source] #

Ensemble cell-type annotation manager with multiple backends.

Parameters :

adata ( AnnData ) – Query single-cell AnnData to annotate.

__init__ ( adata ) [source] #

Methods

`__init__ `(adata)

`gbi_anno `()

Annotate clusters using GPTBioInsightor.

`gpt_anno `()

Annotate cells using GPT based approach.

`popv_anno `(ref_adata, ref_labels_key, ...[, ...])

Annotate cells using PopV.

`scMulan_anno `()

Annotate cells with the scMulan large language model.

`scsa_anno `()

Annotate cells using the SCSA pipeline.

`vote `([clusters_key, cluster_markers, ...])

Generate consensus cell-type labels by LLM arbitration.
