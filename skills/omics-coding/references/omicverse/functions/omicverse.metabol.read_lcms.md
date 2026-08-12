# omicverse.metabol.read_lcms #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.read_lcms`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.read_lcms.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Load an LC-MS peak table with m/z / RT feature IDs into AnnData.

## Signature

```text
omicverse.metabol. read_lcms ( path , * , feature_id_sep = '/' , sample_col = None , group_col = None , label_row = None , transpose = True )
```

## Parameters

- `feature_id_sep`: ( str (default: '/' )) – Separator between m/z and RT inside each feature ID. MetaboAnalyst uses "/" for the small demo and "__" for the malaria table; XCMS exports sometimes use "_" .
- `label_row`: ( Optional [ str ] (default: None )) – When the raw file has features in rows, the first “feature” is often a dedicated group-label row (e.g. MetaboAnalyst’s "Label" row with values like "Naive" / "Semi_immue" ). Pass the label of that row here and we’ll lift it into adata.obs['group'] before treating the rest as features.
- `transpose`: ( bool (default: True )) – Default True (peaks-in-rows → samples-in-rows, AnnData orientation).
- `sample_col`: ( Optional [ str ] (default: None )) – Only used when the table is already in samples-in-rows layout; both default to the first column / the first non-sample column.
- `group_col`: ( Optional [ str ] (default: None )) – Only used when the table is already in samples-in-rows layout; both default to the first column / the first non-sample column.
- `path`: ( str | Path )

## Full Documentation

# omicverse.metabol.read_lcms #

omicverse.metabol. read_lcms ( path , * , feature_id_sep = '/' , sample_col = None , group_col = None , label_row = None , transpose = True ) [source] #

Load an LC-MS peak table with `m/z `/ `RT `feature IDs into AnnData.

Handles MetaboAnalyst’s LC-MS demo layout (peaks-in-rows with a dedicated “Label” row above the data), as well as plain wide tables. Feature IDs of the form `<m/z><sep><RT> `(e.g. `"200.1/2926" `or `"85.065__24.64" `) are parsed into numeric `var['m_z'] `/ `var['rt'] `columns so `mummichog_basic() `can consume the AnnData directly.

Parameters :

-
feature_id_sep ( `str `(default: `'/' `)) – Separator between m/z and RT inside each feature ID. MetaboAnalyst uses `"/" `for the small demo and `"__" `for the malaria table; XCMS exports sometimes use `"_" `.

-
label_row ( `Optional `[ `str `] (default: `None `)) – When the raw file has features in rows, the first “feature” is often a dedicated group-label row (e.g. MetaboAnalyst’s `"Label" `row with values like `"Naive" `/ `"Semi_immue" `). Pass the label of that row here and we’ll lift it into `adata.obs['group'] `before treating the rest as features.

-
transpose ( `bool `(default: `True `)) – Default True (peaks-in-rows → samples-in-rows, AnnData orientation).

-
sample_col ( `Optional `[ `str `] (default: `None `)) – Only used when the table is already in samples-in-rows layout; both default to the first column / the first non-sample column.

-
group_col ( `Optional `[ `str `] (default: `None `)) – Only used when the table is already in samples-in-rows layout; both default to the first column / the first non-sample column.

-
path ( `str `| `Path `)
