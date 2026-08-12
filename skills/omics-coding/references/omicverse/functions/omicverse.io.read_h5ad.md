# omicverse.io.read_h5ad #

- Package: omicverse
- Language: Python
- Function: `omicverse.io.read_h5ad`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.io.read_h5ad.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Read an .h5ad file.

## Signature

```text
omicverse.io. read_h5ad ( filename , ** kwargs )
```

## Parameters

- `filename`: ( str or pathlib.Path ) – Path to the input .h5ad file.
- `**kwargs`: – Additional keyword arguments forwarded to anndata.read_h5ad() .

## Full Documentation

# omicverse.io.read_h5ad #

omicverse.io. read_h5ad ( filename , ** kwargs ) [source] #

Read an `.h5ad `file.

Parameters :

-
filename ( str or pathlib.Path ) – Path to the input `.h5ad `file.

-
**kwargs – Additional keyword arguments forwarded to `anndata.read_h5ad() `.

Returns :

Loaded AnnData object. 若文件由 `read_visium_hd_seg() `生成，将自动从 `obs['geometry'] `重建 GeoDataFrame 并写入 `` uns[‘spatial’][sample][‘geometries’]``（需安装 geopandas）。

Return type :

anndata.AnnData
