# omicverse.metabol.read_metaboanalyst #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.read_metaboanalyst`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.read_metaboanalyst.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Load a MetaboAnalyst-format CSV into AnnData.

## Signature

```text
omicverse.metabol. read_metaboanalyst ( path , * , group_col , sample_col = None , transpose = False )
```

## Parameters

- `path`: ( str | Path ) – CSV path or URL.
- `group_col`: ( str ) – Name of the factor column holding case/control labels. Required; copied to adata.obs['group'] .
- `sample_col`: ( Optional [ str ] (default: None )) – Name of the sample-ID column. If None , the first column is used (matches the MetaboAnalyst default).
- `transpose`: ( bool (default: False )) – Set to True if your CSV has samples in columns and metabolites in rows — we’ll transpose before wrapping.

## Full Documentation

# omicverse.metabol.read_metaboanalyst #

omicverse.metabol. read_metaboanalyst ( path , * , group_col , sample_col = None , transpose = False ) [source] #

Load a MetaboAnalyst-format CSV into AnnData.

MetaboAnalyst’s canonical bulk-upload layout is:

```text
Patient ID,Muscle loss,Metabolite1,Metabolite2,...
PIF_1,cachexic,40.85,62.23,...
PIF_2,control,29.46,58.13,...

```

— samples in rows, one factor (group) column, rest are metabolite concentrations. `group_col `is required (no default) because every MetaboAnalyst dataset uses a different column name ( `"Muscle loss" `for the Eisner-2010 cachexia demo, `"Label" `for most others). Pass the exact column header from your CSV.

Parameters :

-
path ( `str `| `Path `) – CSV path or URL.

-
group_col ( `str `) – Name of the factor column holding case/control labels. Required; copied to `adata.obs['group'] `.

-
sample_col ( `Optional `[ `str `] (default: `None `)) – Name of the sample-ID column. If `None `, the first column is used (matches the MetaboAnalyst default).

-
transpose ( `bool `(default: `False `)) – Set to True if your CSV has samples in columns and metabolites in rows — we’ll transpose before wrapping.

Returns :

`adata.X `is `n_samples × n_metabolites `floats; `obs `carries the group label; `var `is empty initially.

Return type :

AnnData
