# omicverse.single.pySIMBA #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.pySIMBA`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.pySIMBA.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

SIMBA wrapper for single-cell batch integration and graph-embedding construction.

## Signature

```text
class omicverse.single. pySIMBA ( adata , workdir = 'simba_result' )
```

## Parameters

- `adata`: ( AnnData ) – Input AnnData with batch labels in obs .
- `workdir`: ( str , optional ) – Directory used by SIMBA to store intermediate files and outputs.

## Full Documentation

# omicverse.single.pySIMBA #

class omicverse.single. pySIMBA ( adata , workdir = 'simba_result' ) [source] #

SIMBA wrapper for single-cell batch integration and graph-embedding construction.

Parameters :

-
adata ( AnnData ) – Input AnnData with batch labels in `obs `.

-
workdir ( str , optional ) – Directory used by SIMBA to store intermediate files and outputs.

Returns :

Initializes SIMBA runtime and stores input data/workspace.

Return type :

None

Examples

```text
>>> simba_object = ov.single.pySIMBA(adata, workdir)

```

__init__ ( adata , workdir = 'simba_result' ) [source] #

Initialize SIMBA object for batch correction and multimodal analysis.

Parameters :

-
adata ( anndata.AnnData ) – Input AnnData containing single-cell profiles and batch labels.

-
workdir ( str ) – Working directory used by SIMBA for intermediate files.

Methods

`__init__ `(adata[, workdir])

Initialize SIMBA object for batch correction and multimodal analysis.

`batch_correction `([use_precomputed])

Perform batch correction using the trained SIMBA model.

`check_simba `()

Check if SIMBA package has been installed.

`gen_graph `([n_components, k, copy, dirname])

Generate the graph structure for batch correction.

`load `([model_path])

Load a pre-trained SIMBA model for batch correction.

`preprocess `([batch_key, min_n_cells, method, ...])

Preprocess the AnnData object for SIMBA analysis.

`train `([num_workers, auto_wd, save_wd, output])

Train the SIMBA model for batch correction.
