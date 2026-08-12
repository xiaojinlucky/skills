# omicverse.single.load_human_prior_interaction_network #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.load_human_prior_interaction_network`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.load_human_prior_interaction_network.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Load one of the packaged human prior interaction networks.

## Signature

```text
omicverse.single. load_human_prior_interaction_network ( dataset = 'nichenet' , only_directed = False , force_download = False )
```

## Parameters

- `dataset`: ( str , default='nichenet' ) – Network source name.
- `only_directed`: ( bool , default=False ) – Keep only directed edges when edge-direction information exists.
- `force_download`: ( bool , default=False ) – Force redownload even when local cache exists.

## Full Documentation

# omicverse.single.load_human_prior_interaction_network #

omicverse.single. load_human_prior_interaction_network ( dataset = 'nichenet' , only_directed = False , force_download = False ) [source] #

Load one of the packaged human prior interaction networks.

Parameters :

-
dataset ( str , default='nichenet' ) – Network source name.

-
only_directed ( bool , default=False ) – Keep only directed edges when edge-direction information exists.

-
force_download ( bool , default=False ) – Force redownload even when local cache exists.

Returns :

Two-column edge table with `from `and `to `gene symbols.

Return type :

pandas.DataFrame
