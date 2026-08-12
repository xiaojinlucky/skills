# omicverse.single.gptcelltype_local #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.gptcelltype_local`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.gptcelltype_local.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Annotate cell types with a local instruction-tuned LLM.

## Signature

```text
omicverse.single. gptcelltype_local ( input , tissuename = None , speciename = 'human' , model_name = 'Qwen/Qwen2-7B-Instruct' , topgenenumber = 10 )
```

## Parameters

- `input`: ( dict or pandas.DataFrame ) – Marker definition per cluster. Accepts either a dict[cluster_id -> list[str]] of marker genes, or a DE table with cluster , names , logfoldchanges columns.
- `tissuename`: ( str or None , default=None ) – Tissue context included in the prompt.
- `speciename`: ( str , default='human' ) – Species context string included in the prompt.
- `model_name`: ( str , default='Qwen/Qwen2-7B-Instruct' ) – Local Hugging Face model name or path used for generation.
- `topgenenumber`: ( int , default=10 ) – Maximum number of marker genes retained per cluster.

## Full Documentation

# omicverse.single.gptcelltype_local #

omicverse.single. gptcelltype_local ( input , tissuename = None , speciename = 'human' , model_name = 'Qwen/Qwen2-7B-Instruct' , topgenenumber = 10 ) [source] #

Annotate cell types with a local instruction-tuned LLM.

Parameters :

-
input ( dict or pandas.DataFrame ) – Marker definition per cluster. Accepts either a `dict[cluster_id -> list[str]] `of marker genes, or a DE table with `cluster `, `names `, `logfoldchanges `columns.

-
tissuename ( str or None , default=None ) – Tissue context included in the prompt.

-
speciename ( str , default='human' ) – Species context string included in the prompt.

-
model_name ( str , default='Qwen/Qwen2-7B-Instruct' ) – Local Hugging Face model name or path used for generation.

-
topgenenumber ( int , default=10 ) – Maximum number of marker genes retained per cluster.

Returns :

Mapping from cluster ID to predicted cell type name.

Return type :

dict

Examples

```text
>>> markers = {"0": ["CD3D", "IL7R"], "1": ["NKG7", "GNLY"]}
>>> res = gptcelltype_local(markers, tissuename="PBMC", speciename="human")

```
