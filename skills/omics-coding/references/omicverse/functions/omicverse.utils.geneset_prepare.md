# omicverse.utils.geneset_prepare #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.geneset_prepare`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.geneset_prepare.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Load and prepare gene sets from GMT/TXT files for enrichment analysis.

## Signature

```text
omicverse.utils. geneset_prepare ( geneset_path , organism = 'Human' , auto_download = True )
```

## Parameters

- `geneset_path`: ( str ) – Path to geneset file.
- `organism`: ( str ) – Organism name used for gene-symbol case normalization.
- `auto_download`: ( bool , default=True ) – If the path does not exist AND its basename matches a known omicverse pathway resource ( GO_*_2021 , Reactome_2022 , WikiPathway_2021_Human , WikiPathways_2019_Mouse ), call download_pathway_database() to fetch all standard genesets into ./genesets/ and retry. Disable to fail fast offline.

## Full Documentation

# omicverse.utils.geneset_prepare #

omicverse.utils. geneset_prepare ( geneset_path , organism = 'Human' , auto_download = True ) [source] #

Load and prepare gene sets from GMT/TXT files for enrichment analysis.

Parameters :

-
geneset_path ( str ) – Path to geneset file.

-
organism ( str ) – Organism name used for gene-symbol case normalization.

-
auto_download ( bool , default=True ) – If the path does not exist AND its basename matches a known omicverse pathway resource ( `GO_*_2021 `, `Reactome_2022 `, `WikiPathway_2021_Human `, `WikiPathways_2019_Mouse `), call `download_pathway_database() `to fetch all standard genesets into `./genesets/ `and retry. Disable to fail fast offline.

Returns :

Dictionary where keys are pathway names and values are gene symbol lists.

Return type :

dict
