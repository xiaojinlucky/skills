# omicverse.single.download_cl #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.download_cl`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.download_cl.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

📥 Download Cell Ontology file from multiple sources with automatic fallback

## Signature

```text
omicverse.single. download_cl ( output_dir = 'new_ontology' , filename = 'cl.json' )
```

## Parameters

- `output_dir`: ( str , optional ) – Directory to save the file (default: “new_ontology”)
- `filename`: ( str , optional ) – Output filename (default: “cl.json”)

## Full Documentation

# omicverse.single.download_cl #

omicverse.single. download_cl ( output_dir = 'new_ontology' , filename = 'cl.json' ) [source] #

📥 Download Cell Ontology file from multiple sources with automatic fallback

This is a standalone function that downloads cl.json from multiple sources: 1. Official OBO Library (direct JSON) 2. OSS Mirror for Chinese users (ZIP format) 3. Google Drive backup (ZIP format)

Parameters :

-
output_dir ( str , optional ) – Directory to save the file (default: “new_ontology”)

-
filename ( str , optional ) – Output filename (default: “cl.json”)

Returns :

-
success ( bool ) – True if download successful, False otherwise

-
file_path ( str or None ) – Path to downloaded file if successful

Examples

```text
>>> success, file_path = download_cl()
>>> if success:
... print(f"Downloaded to: {file_path}")

```

```text
>>> success, file_path = download_cl("my_data", "cell_ontology.json")

```
