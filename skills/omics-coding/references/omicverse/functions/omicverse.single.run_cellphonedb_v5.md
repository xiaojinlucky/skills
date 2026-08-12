# omicverse.single.run_cellphonedb_v5 #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.run_cellphonedb_v5`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.run_cellphonedb_v5.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run CellPhoneDB statistical analysis with automatic database download

## Signature

```text
omicverse.single. run_cellphonedb_v5 ( adata , cpdb_file_path , celltype_key = 'celltype' , min_cell_fraction = 0.005 , min_genes = 200 , min_cells = 3 , iterations = 1000 , threshold = 0.1 , pvalue = 0.05 , threads = 10 , output_dir = None , temp_dir = None , cleanup_temp = True , debug = False , separator = '|' , results_key = 'cpdb_results' , comm_key = 'cpdb_comm' , ** kwargs )
```

## Parameters

- `adata`: ( AnnData ) – Annotated data matrix
- `cpdb_file_path`: ( str ) – Path to CellPhoneDB database zip file (REQUIRED) If file doesn’t exist, will attempt automatic download
- `celltype_key`: ( str ) – Column name in adata.obs containing cell type annotations
- `min_cell_fraction`: ( float ) – Minimum fraction of total cells required for a cell type to be included
- `min_genes`: ( int ) – Minimum number of genes required per cell
- `min_cells`: ( int ) – Minimum number of cells required per gene
- `iterations`: ( int ) – Number of shufflings performed in the analysis
- `threshold`: ( float ) – Min % of cells expressing a gene for this to be employed in the analysis
- `pvalue`: ( float ) – P-value threshold to employ for significance
- `threads`: ( int ) – Number of threads to use in the analysis
- `output_dir`: ( str or None ) – Directory to save results. If None, creates temporary directory
- `temp_dir`: ( str or None ) – Directory for temporary files. If None, uses system temp
- `cleanup_temp`: ( bool ) – Whether to clean up temporary files after analysis
- `debug`: ( bool ) – Saves all intermediate tables employed during the analysis
- `separator`: ( str ) – String to employ to separate cells in the results dataframes
- `**kwargs`: ( dict ) – Additional parameters forwarded to cpdb_statistical_analysis_method.call .
- `results_key`: Detected from function signature; no parameter description detected.
- `comm_key`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.single.run_cellphonedb_v5 #

omicverse.single. run_cellphonedb_v5 ( adata , cpdb_file_path , celltype_key = 'celltype' , min_cell_fraction = 0.005 , min_genes = 200 , min_cells = 3 , iterations = 1000 , threshold = 0.1 , pvalue = 0.05 , threads = 10 , output_dir = None , temp_dir = None , cleanup_temp = True , debug = False , separator = '|' , results_key = 'cpdb_results' , comm_key = 'cpdb_comm' , ** kwargs ) [source] #

Run CellPhoneDB statistical analysis with automatic database download

Parameters :

-
adata ( AnnData ) – Annotated data matrix

-
cpdb_file_path ( str ) – Path to CellPhoneDB database zip file (REQUIRED) If file doesn’t exist, will attempt automatic download

-
celltype_key ( str ) – Column name in adata.obs containing cell type annotations

-
min_cell_fraction ( float ) – Minimum fraction of total cells required for a cell type to be included

-
min_genes ( int ) – Minimum number of genes required per cell

-
min_cells ( int ) – Minimum number of cells required per gene

-
iterations ( int ) – Number of shufflings performed in the analysis

-
threshold ( float ) – Min % of cells expressing a gene for this to be employed in the analysis

-
pvalue ( float ) – P-value threshold to employ for significance

-
threads ( int ) – Number of threads to use in the analysis

-
output_dir ( str or None ) – Directory to save results. If None, creates temporary directory

-
temp_dir ( str or None ) – Directory for temporary files. If None, uses system temp

-
cleanup_temp ( bool ) – Whether to clean up temporary files after analysis

-
debug ( bool ) – Saves all intermediate tables employed during the analysis

-
separator ( str ) – String to employ to separate cells in the results dataframes

-
**kwargs ( dict ) – Additional parameters forwarded to `cpdb_statistical_analysis_method.call `.

Returns :

Raw CellPhoneDB result dict and visualization-ready communication AnnData. The same objects are also written to `adata.uns[results_key] `and `adata.uns[comm_key] `so downstream `ov.pl.ccc_* `plots can work directly on the original `adata `.

Return type :

Tuple[ dict , anndata.AnnData ]

Examples

# Basic usage - will download database automatically if needed cpdb_results, adata_cpdb = run_cellphonedb_analysis(

adata, cpdb_file_path=’./cellphonedb.zip’, celltype_key=’celltype_minor’

)

# Advanced usage cpdb_results, adata_cpdb = run_cellphonedb_analysis(

adata, cpdb_file_path=’/path/to/cellphonedb.zip’, celltype_key=’celltype_minor’, min_cell_fraction=0.01, iterations=2000, threads=20

)

Parameters :

-
results_key ( `str `(default: `'cpdb_results' `))

-
comm_key ( `str `(default: `'cpdb_comm' `))
