# omicverse.single.download_cellphonedb_database #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.download_cellphonedb_database`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.download_cellphonedb_database.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Download CellPhoneDB database with fallback URLs.

## Signature

```text
omicverse.single. download_cellphonedb_database ( download_path = None , force_download = False )
```

## Parameters

- `download_path`: ( str or None ) – Target path of downloaded cellphonedb.zip file. If None , defaults to $OVAGENT_HOME/data_lake/cellphonedb.zip (so the same cache is shared across ov.Agent sessions).
- `force_download`: ( bool ) – Whether to redownload when file already exists.

## Full Documentation

# omicverse.single.download_cellphonedb_database #

omicverse.single. download_cellphonedb_database ( download_path = None , force_download = False ) [source] #

Download CellPhoneDB database with fallback URLs.

Uses `ov.datasets.download_data_requests `(the standard omicverse downloader, with realistic User-Agent + tqdm progress + caching).

Parameters :

-
download_path ( str or None ) – Target path of downloaded `cellphonedb.zip `file. If `None `, defaults to `$OVAGENT_HOME/data_lake/cellphonedb.zip `(so the same cache is shared across ov.Agent sessions).

-
force_download ( bool ) – Whether to redownload when file already exists.

Returns :

Path to downloaded database archive.

Return type :

str
