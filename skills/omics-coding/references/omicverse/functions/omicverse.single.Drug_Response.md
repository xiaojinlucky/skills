# omicverse.single.Drug_Response #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.Drug_Response`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.Drug_Response.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Predict drug sensitivity from single-cell transcriptomes using CaDRReS models.

## Signature

```text
class omicverse.single. Drug_Response ( adata , scriptpath , modelpath , output = './' , model = 'GDSC' , clusters = 'All' , cell = 'A549' , cpus = 4 , n_drugs = 10 )
```

## Parameters

- `adata`: ( AnnData ) – Query single-cell AnnData.
- `scriptpath`: ( str ) – Path to CaDRReS-Sc scripts.
- `modelpath`: ( str ) – Path to pretrained pharmacogenomic model/data resources.
- `output`: ( str , optional ) – Output directory for prediction tables and plots.
- `model`: ( {'GDSC' , 'PRISM'} , optional ) – Pharmacogenomic reference model.
- `clusters`: ( str , optional ) – Cluster subset to analyze ( 'All' uses all cells).
- `cell`: ( str , optional ) – Cell-line context used by the model.
- `cpus`: ( int , optional ) – CPU threads used by downstream steps.
- `n_drugs`: ( int , optional ) – Number of top drugs to report/plot.

## Full Documentation

# omicverse.single.Drug_Response #

class omicverse.single. Drug_Response ( adata , scriptpath , modelpath , output = './' , model = 'GDSC' , clusters = 'All' , cell = 'A549' , cpus = 4 , n_drugs = 10 ) [source] #

Predict drug sensitivity from single-cell transcriptomes using CaDRReS models.

Parameters :

-
adata ( AnnData ) – Query single-cell AnnData.

-
scriptpath ( str ) – Path to CaDRReS-Sc scripts.

-
modelpath ( str ) – Path to pretrained pharmacogenomic model/data resources.

-
output ( str , optional ) – Output directory for prediction tables and plots.

-
model ( {'GDSC' , 'PRISM'} , optional ) – Pharmacogenomic reference model.

-
clusters ( str , optional ) – Cluster subset to analyze ( `'All' `uses all cells).

-
cell ( str , optional ) – Cell-line context used by the model.

-
cpus ( int , optional ) – CPU threads used by downstream steps.

-
n_drugs ( int , optional ) – Number of top drugs to report/plot.

Returns :

Initializes drug-response prediction workflow state.

Return type :

None

Examples

```text
>>> job = ov.single.Drug_Response(adata, scriptpath="CaDRReS-Sc")

```

__init__ ( adata , scriptpath , modelpath , output = './' , model = 'GDSC' , clusters = 'All' , cell = 'A549' , cpus = 4 , n_drugs = 10 ) [source] #

Initialize the Drug_Response class.

Parameters :

-
adata ( anndata.AnnData ) – Input AnnData used for single-cell drug-response prediction.

-
scriptpath ( str ) – Path to cloned `CaDRReS-Sc `script directory.

-
modelpath ( str ) – Path containing pretrained CaDRReS model/data files.

-
output ( str ) – Output directory for prediction tables and figures.

-
model ( str ) – Pharmacogenomic reference model, typically `'GDSC' `or `'PRISM' `.

-
clusters ( str ) – Comma-separated louvain cluster IDs, or `'All' `.

-
cell ( str ) – Cell-line context label used by CaDRReS.

-
cpus ( int ) – Number of CPUs used by downstream routines.

-
n_drugs ( int ) – Number of top drugs displayed in output figures.

Returns :

None

Methods

`__init__ `(adata, scriptpath, modelpath[, ...])

Initialize the Drug_Response class.

`bulk_exp `()

extract the bulk gene expression data.

`cell_death_proportion `()

Predict cell death proportion and cell death percentage at the ref_type dosage

`draw_plot `(df[, n_drug, name, figsize])

plot heatmap of drug response prediction

`drug_info `()

read the drug information.

`figure_output `()

plot figures

`kernel_feature_preparartion `()

kernel feature preparation

`load_model `()

Load the pre-trained model.

`output_result `()

Export predicted drug response tables to CSV files.

`sc_exp `()

Load cluster-specific gene expression profile

`sensitivity_prediction `()

Predict drug sensitivity
