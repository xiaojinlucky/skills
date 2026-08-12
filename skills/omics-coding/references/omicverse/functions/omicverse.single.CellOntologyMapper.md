# omicverse.single.CellOntologyMapper #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.CellOntologyMapper`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.CellOntologyMapper.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Map free-text cell-type annotations to the Cell Ontology (CL) via NLP.

## Signature

```text
class omicverse.single. CellOntologyMapper ( cl_obo_file = None , embeddings_path = None , model_name = 'all-mpnet-base-v2' , local_model_dir = None , auto_download = True )
```

## Parameters

- `cl_obo_file`: ( str , optional ) – 📄 Cell Ontology OBO file path
- `embeddings_path`: ( str , optional ) – 💾 Pre-computed embeddings file path
- `model_name`: ( str ) – 🤖 Sentence Transformer model name
- `local_model_dir`: ( str , optional ) – 📁 Local directory to save downloaded models (avoid default cache)
- `auto_download`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.single.CellOntologyMapper #

class omicverse.single. CellOntologyMapper ( cl_obo_file = None , embeddings_path = None , model_name = 'all-mpnet-base-v2' , local_model_dir = None , auto_download = True ) [source] #

Map free-text cell-type annotations to the Cell Ontology (CL) via NLP.

Sentence-transformer encoder over the CL terms; cosine-similarity matching of every annotated cell name to the closest ontology term. Optional add-ons:

-
Abbreviation expansion (LLM-driven, optional) — turns `"TIL-1" `into `"tissue-resident memory CD8+ T cell" `before matching, dramatically improving recall on author-shorthand labels.

-
Cell Taxonomy resource (Jin et al. 2023) — a second ontology keyed by species + tissue, with marker genes; provides `map_*_with_taxonomy `variants.

-
Marker-gene search — find ontology terms whose marker set overlaps your cluster’s top-N markers ( search_by_marker ).

Lifecycle: construct with a CL OBO file (or download via `download_cl() `); the encoder is loaded lazily on first `map_* `call. Pre-computed sentence embeddings can be cached via `embeddings_path `to skip the ~30 s encode step on repeated calls.

## Typical workflow #

```text
>>> ov.single.download_cl(output_dir='cl_dir', filename='cl.json')
>>> mapper = ov.single.CellOntologyMapper(
... cl_obo_file='cl_dir/cl.json',
... embeddings_path='cl_dir/ontology_embeddings.pkl',
... local_model_dir='./my_models',
... )
>>> results = mapper.map_adata(adata, cell_name_col='cell_label')
>>> mapper.print_mapping_summary(results, top_n=15)

```

## Adds (after `map_adata `) #

-
`adata.obs['cell_ontology'] `— best-match CL term name.

-
`adata.obs['cell_ontology_cl_id'] `— CL ID (e.g. `CL:0000084 `).

-
`adata.obs['cell_ontology_score'] `— cosine similarity.

Use `map_adata_with_expansion(...) `when annotations contain abbreviations and `setup_llm_expansion `has been configured. Use `map_adata_with_taxonomy(...) `when species + tissue context is needed (Cell Taxonomy adds species-aware mappings).

__init__ ( cl_obo_file = None , embeddings_path = None , model_name = 'all-mpnet-base-v2' , local_model_dir = None , auto_download = True ) [source] #

🚀 Initialize CellOntologyMapper

Parameters :

-
cl_obo_file ( str , optional ) – 📄 Cell Ontology OBO file path

-
embeddings_path ( str , optional ) – 💾 Pre-computed embeddings file path

-
model_name ( str ) – 🤖 Sentence Transformer model name

-
local_model_dir ( str , optional ) – 📁 Local directory to save downloaded models (avoid default cache)

Methods

`__init__ `([cl_obo_file, embeddings_path, ...])

🚀 Initialize CellOntologyMapper

`browse_ontology_by_category `([categories, ...])

📂 Browse ontology cell types by category

`check_ontology_status `()

🔍 Check ontology data status and provide diagnostic information

`clear_abbreviation_cache `()

🗑️ Clear abbreviation cache

`create_ontology_resources `(cl_obo_file[, ...])

🔨 Create ontology resources from OBO file

`download_model `()

📥 Manually download and load the model

`expand_abbreviations `(cell_names[, ...])

🔄 Expand cell type abbreviations

`find_similar_cells `(cell_name[, top_k])

🔍 Find ontology cell types most similar to given cell name

`find_similar_cells_taxonomy `(cell_name[, ...])

🧬 Find taxonomy cell types most similar to given cell name

`get_cell_info `(cell_name)

ℹ️ Get detailed information for specific cell type

`get_cell_info_taxonomy `(cell_name[, species])

🧬 Get detailed taxonomy information for specific cell type

`get_ontology_statistics `()

📊 Get ontology statistics

`get_statistics `(mapping_results)

📊 Get mapping statistics

`list_ontology_cells `([max_display, return_all])

📋 List all cell types in the ontology

`load_cell_taxonomy_resource `(taxonomy_file[, ...])

📊 Load Cell Taxonomy resource as additional ontology

`load_embeddings `(embeddings_path)

📥 Load embeddings from file

`load_ontology_mappings `(popv_json_path)

📋 Load ontology ID mappings from cl_popv.json file

`map_adata `(adata[, cell_name_col, threshold, ...])

🧬 Map cell names in AnnData object to ontology

`map_adata_with_expansion `(adata[, ...])

🧬 Perform ontology mapping with abbreviation expansion on AnnData

`map_adata_with_taxonomy `(adata[, ...])

🧬 Apply taxonomy-enhanced mapping to AnnData object

`map_cells `(cell_names[, threshold, ...])

🎯 Map cell names to ontology with optional LLM-enhanced selection

`map_cells_with_expansion `(cell_names[, ...])

🔄 First expand abbreviations, then perform ontology mapping with optional LLM selection

`map_cells_with_taxonomy `(cell_names[, ...])

🔄 Enhanced cell mapping using both ontology and taxonomy

`print_mapping_summary `(mapping_results[, top_n])

📋 Print mapping summary

`print_mapping_summary_taxonomy `(mapping_results)

📋 Print comprehensive mapping summary with taxonomy information

`print_mapping_summary_with_ids `(mapping_results)

📋 Print mapping summary with ontology IDs

`save_embeddings `([output_path])

💾 Save embeddings to file

`save_mapping_results `(mapping_results, ...)

💾 Save mapping results to file

`search_by_marker `(markers[, species, top_k])

🎯 Search cell types by gene markers using taxonomy resource

`search_ontology_cells `(keyword[, ...])

🔍 Search cell types containing specific keywords in the ontology

`set_local_model `(model_path)

🏠 Set local model path

`set_model `(model_name[, local_model_dir])

🎯 Set model name and local save directory

`setup_llm_expansion `([api_type, api_key, ...])

🤖 Setup LLM API for abbreviation expansion

`show_expansion_summary `(mapping_results)

📊 Show abbreviation expansion summary

`test_abbreviation_detection `([test_cases])

🧪 Test abbreviation detection with various examples
