# omicverse.single.gptcelltype #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.gptcelltype`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.gptcelltype.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Annotate cluster cell types with a remote LLM service.

## Signature

```text
omicverse.single. gptcelltype ( input , tissuename = None , speciename = 'human' , provider = 'qwen' , model = 'qwen-plus' , topgenenumber = 10 , base_url = None )
```

## Parameters

- `input`: ( dict or pandas.DataFrame ) – Cluster marker input. Use either a dict[cluster_id -> list[str]] of marker genes, or a DE result table containing cluster , names , and logfoldchanges columns.
- `tissuename`: ( str or None , default=None ) – Tissue context provided to the model prompt (for example, PBMC or brain).
- `speciename`: ( str , default='human' ) – Species context string included in the prompt.
- `provider`: ( str , default='qwen' ) – LLM provider preset used to infer default API endpoint. Supported values are 'openai' , 'kimi' , and 'qwen' .
- `model`: ( str , default='qwen-plus' ) – Chat-completion model name used by the selected provider.
- `topgenenumber`: ( int , default=10 ) – Number of top marker genes retained per cluster before prompting.
- `base_url`: ( str or None , default=None ) – Custom chat-completion endpoint base URL. If None , it is selected from provider .

## Full Documentation

# omicverse.single.gptcelltype #

omicverse.single. gptcelltype ( input , tissuename = None , speciename = 'human' , provider = 'qwen' , model = 'qwen-plus' , topgenenumber = 10 , base_url = None ) [source] #

Annotate cluster cell types with a remote LLM service.

Parameters :

-
input ( dict or pandas.DataFrame ) – Cluster marker input. Use either a `dict[cluster_id -> list[str]] `of marker genes, or a DE result table containing `cluster `, `names `, and `logfoldchanges `columns.

-
tissuename ( str or None , default=None ) – Tissue context provided to the model prompt (for example, PBMC or brain).

-
speciename ( str , default='human' ) – Species context string included in the prompt.

-
provider ( str , default='qwen' ) – LLM provider preset used to infer default API endpoint. Supported values are `'openai' `, `'kimi' `, and `'qwen' `.

-
model ( str , default='qwen-plus' ) – Chat-completion model name used by the selected provider.

-
topgenenumber ( int , default=10 ) – Number of top marker genes retained per cluster before prompting.

-
base_url ( str or None , default=None ) – Custom chat-completion endpoint base URL. If `None `, it is selected from `provider `.

Returns :

When `AGI_API_KEY `is available, returns `dict[cluster_id -> celltype] `. Otherwise returns the generated prompt text for manual use.

Return type :

dict or str

Examples

```text
>>> markers = {"0": ["MS4A1", "CD79A"], "1": ["NKG7", "PRF1"]}
>>> res = gptcelltype(markers, tissuename="PBMC", speciename="human")
>>> adata.obs["gpt_celltype"] = adata.obs["leiden"].map(res)

```
