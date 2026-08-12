# omicverse.metabol.fetch_chebi_compounds #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.fetch_chebi_compounds`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.fetch_chebi_compounds.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Build a compound master table from ChEBI’s flat-file TSVs.

## Signature

```text
omicverse.metabol. fetch_chebi_compounds ( * , cache = True , refresh = False )
```

## Parameters

- `cache`: ( bool (default: True ))
- `refresh`: ( bool (default: False ))

## Full Documentation

# omicverse.metabol.fetch_chebi_compounds #

omicverse.metabol. fetch_chebi_compounds ( * , cache = True , refresh = False ) [source] #

Build a compound master table from ChEBI’s flat-file TSVs.

Downloads + joins three ChEBI distributions from the public EBI FTP (over HTTPS):

-
`compounds.tsv.gz `— ChEBI ID → canonical name

-
`chemical_data.tsv.gz `— monoisotopic mass + formula

-
`database_accession.tsv.gz `— HMDB / KEGG / LipidMaps xrefs

Total download is ~15 MB; the joined parquet cache persists at `~/.cache/omicverse/metabol/chebi_compounds.parquet `. This is the substrate `annotate_peaks() `uses for mummichog mass matching.

Returns :

Columns: `chebi_id `, `name `, `formula `, `mw `(monoisotopic, float), `kegg `, `hmdb `, `lipidmaps `. Rows without a monoisotopic mass are dropped.

Return type :

pd.DataFrame

Parameters :

-
cache ( `bool `(default: `True `))

-
refresh ( `bool `(default: `False `))
