# omicverse.single.convert_human_to_mouse_network #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.convert_human_to_mouse_network`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.convert_human_to_mouse_network.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Convert a human-symbol interaction network to mouse symbols.

## Signature

```text
omicverse.single. convert_human_to_mouse_network ( net , server_name = 'asia' )
```

## Parameters

- `net`: ( pd.DataFrame ) – Human network edge table with from and to columns.
- `server_name`: ( str , default='asia' ) – Ensembl Biomart server preference.

## Full Documentation

# omicverse.single.convert_human_to_mouse_network #

omicverse.single. convert_human_to_mouse_network ( net , server_name = 'asia' ) [source] #

Convert a human-symbol interaction network to mouse symbols.

Parameters :

-
net ( pd.DataFrame ) – Human network edge table with `from `and `to `columns.

-
server_name ( str , default='asia' ) – Ensembl Biomart server preference.

Returns :

Converted mouse interaction edge table.

Return type :

pandas.DataFrame
