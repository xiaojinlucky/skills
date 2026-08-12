# omicverse.metabol.annotate_peaks #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.annotate_peaks`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.annotate_peaks.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Map a list of m/z peaks to candidate KEGG compounds via adduct search.

## Signature

```text
omicverse.metabol. annotate_peaks ( mz , * , polarity = 'positive' , ppm = 10.0 , custom_adducts = None , mass_db = None )
```

## Parameters

- `mz`: ( ndarray ) – 1-D array of experimental m/z values.
- `polarity`: ( str (default: 'positive' )) – "positive" or "negative" — picks the adduct list. For mixed modes, pass a merged list via custom_adducts .
- `ppm`: ( float (default: 10.0 )) – Mass-matching tolerance in parts per million. 5 ppm is typical for Orbitrap; 10–20 ppm for QTOF.
- `custom_adducts`: ( Optional [ list [ tuple [ str , float , str ]]] (default: None )) – Override the default adduct list. Each entry is (name, delta_mass, sign_str) .
- `mass_db`: ( Optional [ DataFrame ] (default: None )) – Compound master table with at least mw , kegg , name columns. Defaults to ov.metabol.fetch_chebi_compounds() — ~54k ChEBI 3-star compounds with monoisotopic mass and KEGG/HMDB/LIPID MAPS cross-refs. Pass your own DataFrame to restrict the search space (e.g. only lipids, or a curated clinical panel).

## Full Documentation

# omicverse.metabol.annotate_peaks #

omicverse.metabol. annotate_peaks ( mz , * , polarity = 'positive' , ppm = 10.0 , custom_adducts = None , mass_db = None ) [source] #

Map a list of m/z peaks to candidate KEGG compounds via adduct search.

Parameters :

-
mz ( `ndarray `) – 1-D array of experimental m/z values.

-
polarity ( `str `(default: `'positive' `)) – `"positive" `or `"negative" `— picks the adduct list. For mixed modes, pass a merged list via `custom_adducts `.

-
ppm ( `float `(default: `10.0 `)) – Mass-matching tolerance in parts per million. 5 ppm is typical for Orbitrap; 10–20 ppm for QTOF.

-
custom_adducts ( `Optional `[ `list `[ `tuple `[ `str `, `float `, `str `]]] (default: `None `)) – Override the default adduct list. Each entry is `(name, delta_mass, sign_str) `.

-
mass_db ( `Optional `[ `DataFrame `] (default: `None `)) – Compound master table with at least `mw `, `kegg `, `name `columns. Defaults to `ov.metabol.fetch_chebi_compounds() `— ~54k ChEBI 3-star compounds with monoisotopic mass and KEGG/HMDB/LIPID MAPS cross-refs. Pass your own DataFrame to restrict the search space (e.g. only lipids, or a curated clinical panel).

Returns :

One row per (m/z, adduct, candidate KEGG) match. Columns: `mz `(input), `adduct `, `kegg `, `name `, `delta_ppm `. Multiple candidate matches per m/z are normal.

Return type :

pd.DataFrame
