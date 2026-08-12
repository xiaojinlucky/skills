# omicverse.single.get_obs_value #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.get_obs_value`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.get_obs_value.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Transfer per-cell annotations/statistics to metacells.

## Signature

```text
omicverse.single. get_obs_value ( ad , adata , groupby , type = 'int' )
```

## Parameters

- `ad`: Detected from function signature; no parameter description detected.
- `adata`: Detected from function signature; no parameter description detected.
- `groupby`: Detected from function signature; no parameter description detected.
- `type`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.single.get_obs_value #

omicverse.single. get_obs_value ( ad , adata , groupby , type = 'int' ) [source] #

Transfer per-cell annotations/statistics to metacells.

Looks at `adata.obs['metacell_id'] `(new schema) or `'SEACell' `(legacy) for the cell → metacell mapping.
