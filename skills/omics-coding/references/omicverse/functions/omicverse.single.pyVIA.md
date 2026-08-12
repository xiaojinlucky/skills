# omicverse.single.pyVIA #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.pyVIA`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.pyVIA.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

VIA-based trajectory inference and lineage visualization wrapper.

## Signature

```text
class omicverse.single. pyVIA ( adata , adata_key = 'X_pca' , adata_ncomps = 80 , basis = 'X_umap' , clusters = '' , dist_std_local = 2 , jac_std_global = 0.15 , labels = None , keep_all_local_dist = 'auto' , too_big_factor = 0.4 , resolution_parameter = 1.0 , partition_type = 'ModularityVP' , small_pop = 10 , jac_weighted_edges = True , knn = 30 , n_iter_leiden = 5 , random_seed = 42 , num_threads = -1 , distance = 'l2' , time_smallpop = 15 , super_cluster_labels = False , super_node_degree_list = False , super_terminal_cells = False , x_lazy = 0.95 , alpha_teleport = 0.99 , root_user = None , preserve_disconnected = True , dataset = '' , super_terminal_clusters = [] , is_coarse = True , csr_full_graph = '' , csr_array_locally_pruned = '' , ig_full_graph = '' , full_neighbor_array = '' , full_distance_array = '' , df_annot = None , preserve_disconnected_after_pruning = False , secondary_annotations = None , pseudotime_threshold_TS = 30 , cluster_graph_pruning_std = 0.15 , visual_cluster_graph_pruning = 0.15 , neighboring_terminal_states_threshold = 3 , num_mcmc_simulations = 1300 , piegraph_arrow_head_width = 0.1 , piegraph_edgeweight_scalingfactor = 1.5 , max_visual_outgoing_edges = 2 , via_coarse = None , velocity_matrix = None , gene_matrix = None , velo_weight = 0.5 , edgebundle_pruning = None , A_velo = None , CSM = None , edgebundle_pruning_twice = False , pca_loadings = None , time_series = False , time_series_labels = None , knn_sequential = 10 , knn_sequential_reverse = 0 , t_diff_step = 1 , single_cell_transition_matrix = None , embedding_type = 'via-mds' , do_compute_embedding = False , color_dict = None , user_defined_terminal_cell = [] , user_defined_terminal_group = [] , do_gaussian_kernel_edgeweights = False , RW2_mode = False , working_dir_fp = '/home/shobi/Trajectory/Datasets/' )
```

## Parameters

- `adata`: ( AnnData )
- `adata_key`: ( str (default: 'X_pca' ))
- `adata_ncomps`: ( int (default: 80 ))
- `basis`: ( str (default: 'X_umap' ))
- `clusters`: ( str (default: '' ))
- `dist_std_local`: ( float (default: 2 ))
- `labels`: ( Optional [ ndarray ] (default: None ))
- `too_big_factor`: ( float (default: 0.4 ))
- `resolution_parameter`: ( float (default: 1.0 ))
- `partition_type`: ( str (default: 'ModularityVP' ))
- `small_pop`: ( int (default: 10 ))
- `jac_weighted_edges`: ( bool (default: True ))
- `knn`: ( int (default: 30 ))
- `n_iter_leiden`: ( int (default: 5 ))
- `random_seed`: ( int (default: 42 ))
- `super_cluster_labels`: ( bool (default: False ))
- `super_node_degree_list`: ( bool (default: False ))
- `super_terminal_cells`: ( bool (default: False ))
- `x_lazy`: ( float (default: 0.95 ))
- `alpha_teleport`: ( float (default: 0.99 ))
- `preserve_disconnected`: ( bool (default: True ))
- `dataset`: ( str (default: '' ))
- `super_terminal_clusters`: ( list (default: [] ))
- `csr_full_graph`: ( ndarray (default: '' ))
- `preserve_disconnected_after_pruning`: ( bool (default: False ))
- `secondary_annotations`: ( Optional [ list ] (default: None ))
- `pseudotime_threshold_TS`: ( int (default: 30 ))
- `cluster_graph_pruning_std`: ( float (default: 0.15 ))
- `visual_cluster_graph_pruning`: ( float (default: 0.15 ))
- `max_visual_outgoing_edges`: ( int (default: 2 ))
- `time_series_labels`: ( Optional [ list ] (default: None ))
- `knn_sequential`: ( int (default: 10 ))
- `knn_sequential_reverse`: ( int (default: 0 ))
- `t_diff_step`: ( int (default: 1 ))
- `embedding_type`: ( str (default: 'via-mds' ))
- `do_compute_embedding`: ( bool (default: False ))
- `color_dict`: ( Optional [ dict ] (default: None ))
- `user_defined_terminal_cell`: ( list (default: [] ))
- `user_defined_terminal_group`: ( list (default: [] ))
- `do_gaussian_kernel_edgeweights`: ( bool (default: False ))
- `RW2_mode`: ( bool (default: False ))
- `working_dir_fp`: ( str (default: '/home/shobi/Trajectory/Datasets/' ))
- `jac_std_global`: Detected from function signature; no parameter description detected.
- `keep_all_local_dist`: Detected from function signature; no parameter description detected.
- `num_threads`: Detected from function signature; no parameter description detected.
- `distance`: Detected from function signature; no parameter description detected.
- `time_smallpop`: Detected from function signature; no parameter description detected.
- `root_user`: Detected from function signature; no parameter description detected.
- `is_coarse`: Detected from function signature; no parameter description detected.
- `csr_array_locally_pruned`: Detected from function signature; no parameter description detected.
- `ig_full_graph`: Detected from function signature; no parameter description detected.
- `full_neighbor_array`: Detected from function signature; no parameter description detected.
- `full_distance_array`: Detected from function signature; no parameter description detected.
- `df_annot`: Detected from function signature; no parameter description detected.
- `neighboring_terminal_states_threshold`: Detected from function signature; no parameter description detected.
- `num_mcmc_simulations`: Detected from function signature; no parameter description detected.
- `piegraph_arrow_head_width`: Detected from function signature; no parameter description detected.
- `piegraph_edgeweight_scalingfactor`: Detected from function signature; no parameter description detected.
- `via_coarse`: Detected from function signature; no parameter description detected.
- `velocity_matrix`: Detected from function signature; no parameter description detected.
- `gene_matrix`: Detected from function signature; no parameter description detected.
- `velo_weight`: Detected from function signature; no parameter description detected.
- `edgebundle_pruning`: Detected from function signature; no parameter description detected.
- `A_velo`: Detected from function signature; no parameter description detected.
- `CSM`: Detected from function signature; no parameter description detected.
- `edgebundle_pruning_twice`: Detected from function signature; no parameter description detected.
- `pca_loadings`: Detected from function signature; no parameter description detected.
- `time_series`: Detected from function signature; no parameter description detected.
- `single_cell_transition_matrix`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.single.pyVIA #

class omicverse.single. pyVIA ( adata , adata_key = 'X_pca' , adata_ncomps = 80 , basis = 'X_umap' , clusters = '' , dist_std_local = 2 , jac_std_global = 0.15 , labels = None , keep_all_local_dist = 'auto' , too_big_factor = 0.4 , resolution_parameter = 1.0 , partition_type = 'ModularityVP' , small_pop = 10 , jac_weighted_edges = True , knn = 30 , n_iter_leiden = 5 , random_seed = 42 , num_threads = -1 , distance = 'l2' , time_smallpop = 15 , super_cluster_labels = False , super_node_degree_list = False , super_terminal_cells = False , x_lazy = 0.95 , alpha_teleport = 0.99 , root_user = None , preserve_disconnected = True , dataset = '' , super_terminal_clusters = [] , is_coarse = True , csr_full_graph = '' , csr_array_locally_pruned = '' , ig_full_graph = '' , full_neighbor_array = '' , full_distance_array = '' , df_annot = None , preserve_disconnected_after_pruning = False , secondary_annotations = None , pseudotime_threshold_TS = 30 , cluster_graph_pruning_std = 0.15 , visual_cluster_graph_pruning = 0.15 , neighboring_terminal_states_threshold = 3 , num_mcmc_simulations = 1300 , piegraph_arrow_head_width = 0.1 , piegraph_edgeweight_scalingfactor = 1.5 , max_visual_outgoing_edges = 2 , via_coarse = None , velocity_matrix = None , gene_matrix = None , velo_weight = 0.5 , edgebundle_pruning = None , A_velo = None , CSM = None , edgebundle_pruning_twice = False , pca_loadings = None , time_series = False , time_series_labels = None , knn_sequential = 10 , knn_sequential_reverse = 0 , t_diff_step = 1 , single_cell_transition_matrix = None , embedding_type = 'via-mds' , do_compute_embedding = False , color_dict = None , user_defined_terminal_cell = [] , user_defined_terminal_group = [] , do_gaussian_kernel_edgeweights = False , RW2_mode = False , working_dir_fp = '/home/shobi/Trajectory/Datasets/' ) [source] #

VIA-based trajectory inference and lineage visualization wrapper.

Parameters :

-
adata ( `AnnData `)

-
adata_key ( `str `(default: `'X_pca' `))

-
adata_ncomps ( `int `(default: `80 `))

-
basis ( `str `(default: `'X_umap' `))

-
clusters ( `str `(default: `'' `))

-
dist_std_local ( `float `(default: `2 `))

-
labels ( `Optional `[ `ndarray `] (default: `None `))

-
too_big_factor ( `float `(default: `0.4 `))

-
resolution_parameter ( `float `(default: `1.0 `))

-
partition_type ( `str `(default: `'ModularityVP' `))

-
small_pop ( `int `(default: `10 `))

-
jac_weighted_edges ( `bool `(default: `True `))

-
knn ( `int `(default: `30 `))

-
n_iter_leiden ( `int `(default: `5 `))

-
random_seed ( `int `(default: `42 `))

-
super_cluster_labels ( `bool `(default: `False `))

-
super_node_degree_list ( `bool `(default: `False `))

-
super_terminal_cells ( `bool `(default: `False `))

-
x_lazy ( `float `(default: `0.95 `))

-
alpha_teleport ( `float `(default: `0.99 `))

-
preserve_disconnected ( `bool `(default: `True `))

-
dataset ( `str `(default: `'' `))

-
super_terminal_clusters ( `list `(default: `[] `))

-
csr_full_graph ( `ndarray `(default: `'' `))

-
preserve_disconnected_after_pruning ( `bool `(default: `False `))

-
secondary_annotations ( `Optional `[ `list `] (default: `None `))

-
pseudotime_threshold_TS ( `int `(default: `30 `))

-
cluster_graph_pruning_std ( `float `(default: `0.15 `))

-
visual_cluster_graph_pruning ( `float `(default: `0.15 `))

-
max_visual_outgoing_edges ( `int `(default: `2 `))

-
time_series_labels ( `Optional `[ `list `] (default: `None `))

-
knn_sequential ( `int `(default: `10 `))

-
knn_sequential_reverse ( `int `(default: `0 `))

-
t_diff_step ( `int `(default: `1 `))

-
embedding_type ( `str `(default: `'via-mds' `))

-
do_compute_embedding ( `bool `(default: `False `))

-
color_dict ( `Optional `[ `dict `] (default: `None `))

-
user_defined_terminal_cell ( `list `(default: `[] `))

-
user_defined_terminal_group ( `list `(default: `[] `))

-
do_gaussian_kernel_edgeweights ( `bool `(default: `False `))

-
RW2_mode ( `bool `(default: `False `))

-
working_dir_fp ( `str `(default: `'/home/shobi/Trajectory/Datasets/' `))

__init__ ( adata , adata_key = 'X_pca' , adata_ncomps = 80 , basis = 'X_umap' , clusters = '' , dist_std_local = 2 , jac_std_global = 0.15 , labels = None , keep_all_local_dist = 'auto' , too_big_factor = 0.4 , resolution_parameter = 1.0 , partition_type = 'ModularityVP' , small_pop = 10 , jac_weighted_edges = True , knn = 30 , n_iter_leiden = 5 , random_seed = 42 , num_threads = -1 , distance = 'l2' , time_smallpop = 15 , super_cluster_labels = False , super_node_degree_list = False , super_terminal_cells = False , x_lazy = 0.95 , alpha_teleport = 0.99 , root_user = None , preserve_disconnected = True , dataset = '' , super_terminal_clusters = [] , is_coarse = True , csr_full_graph = '' , csr_array_locally_pruned = '' , ig_full_graph = '' , full_neighbor_array = '' , full_distance_array = '' , df_annot = None , preserve_disconnected_after_pruning = False , secondary_annotations = None , pseudotime_threshold_TS = 30 , cluster_graph_pruning_std = 0.15 , visual_cluster_graph_pruning = 0.15 , neighboring_terminal_states_threshold = 3 , num_mcmc_simulations = 1300 , piegraph_arrow_head_width = 0.1 , piegraph_edgeweight_scalingfactor = 1.5 , max_visual_outgoing_edges = 2 , via_coarse = None , velocity_matrix = None , gene_matrix = None , velo_weight = 0.5 , edgebundle_pruning = None , A_velo = None , CSM = None , edgebundle_pruning_twice = False , pca_loadings = None , time_series = False , time_series_labels = None , knn_sequential = 10 , knn_sequential_reverse = 0 , t_diff_step = 1 , single_cell_transition_matrix = None , embedding_type = 'via-mds' , do_compute_embedding = False , color_dict = None , user_defined_terminal_cell = [] , user_defined_terminal_group = [] , do_gaussian_kernel_edgeweights = False , RW2_mode = False , working_dir_fp = '/home/shobi/Trajectory/Datasets/' ) [source] #

Initialize a pyVIA trajectory inference model.

Parameters :

-
adata ( anndata.AnnData ) – Input single-cell AnnData object.

-
adata_key ( str , default='X_pca' ) – Key in `adata.obsm `used as low-dimensional input for VIA graph construction.

-
adata_ncomps ( int , default=80 ) – Number of components retained from `adata.obsm[adata_key] `.

-
basis ( str , default='X_umap' ) – Embedding key in `adata.obsm `used for plotting and trajectory overlays.

-
clusters ( str , default='' ) – Column name in `adata.obs `storing initial cluster/cell-type labels.

-
dist_std_local ( float , default=2 ) – Local pruning strength for PARC/VIA graph edges.

-
jac_std_global ( float , default=0.15 ) – Global Jaccard-based pruning threshold.

-
labels ( numpy.ndarray , optional ) – Optional external labels used instead of `adata.obs[clusters] `.

-
keep_all_local_dist ( str or bool , default='auto' ) – Whether to keep all local distances before pruning.

-
too_big_factor ( float , default=0.4 ) – Re-partition clusters larger than this fraction of total cells.

-
resolution_parameter ( float , default=1.0 ) – Leiden/PARC partition resolution.

-
partition_type ( str , default='ModularityVP' ) – Graph partition strategy passed to PARC/VIA.

-
small_pop ( int , default=10 ) – Minimum cluster size considered stable.

-
jac_weighted_edges ( bool , default=True ) – Whether to weight graph edges by Jaccard overlap.

-
knn ( int , default=30 ) – Number of nearest neighbors used to build the cell graph.

-
n_iter_leiden ( int , default=5 ) – Number of Leiden refinement iterations.

-
random_seed ( int , default=42 ) – Random seed for reproducible graph partitioning.

-
num_threads ( int , default=-1 ) – Number of CPU threads; `-1 `lets backend decide automatically.

-
distance ( str , default='l2' ) – Distance metric used in neighbor search.

-
time_smallpop ( int , default=15 ) – Iteration/time control for handling small populations.

-
super_cluster_labels ( bool , default=False ) – Whether to compute super-cluster labels on top of base clusters.

-
super_node_degree_list ( bool , default=False ) – Whether to expose super-node degree statistics.

-
super_terminal_cells ( bool , default=False ) – Whether to infer terminal states at super-cluster granularity.

-
x_lazy ( float , default=0.95 ) – Lazy random-walk parameter controlling self-transition probability.

-
alpha_teleport ( float , default=0.99 ) – Teleportation probability for Markov diffusion.

-
root_user ( list , optional ) – User-defined root cell indices or root groups for pseudotime orientation.

-
preserve_disconnected ( bool , default=True ) – Keep disconnected graph components during trajectory construction.

-
dataset ( str , default='' ) – Dataset/root mode flag used by VIA internals.

-
super_terminal_clusters ( list , default= [ ] ) – User-provided terminal super-cluster IDs.

-
is_coarse ( bool , default=True ) – Whether current model is coarse stage in a coarse-to-fine workflow.

-
csr_full_graph ( numpy.ndarray or scipy.sparse matrix , optional ) – Optional precomputed full graph adjacency.

-
csr_array_locally_pruned ( numpy.ndarray or scipy.sparse matrix , optional ) – Optional precomputed locally pruned graph.

-
ig_full_graph ( igraph.Graph , optional ) – Optional pre-built igraph object.

-
full_neighbor_array ( numpy.ndarray , optional ) – Optional precomputed neighbor index array.

-
full_distance_array ( numpy.ndarray , optional ) – Optional precomputed neighbor distance array.

-
df_annot ( pandas.DataFrame , optional ) – Cell annotation table used by VIA plotting and summaries.

-
preserve_disconnected_after_pruning ( bool , default=False ) – Whether to retain disconnected components after graph pruning.

-
secondary_annotations ( list , optional ) – Additional annotation tracks for visualization.

-
pseudotime_threshold_TS ( int , default=30 ) – Threshold used in terminal-state calling for time-series mode.

-
cluster_graph_pruning_std ( float , default=0.15 ) – Pruning strength for cluster-level graph.

-
visual_cluster_graph_pruning ( float , default=0.15 ) – Additional pruning for visualized cluster graph.

-
neighboring_terminal_states_threshold ( int , default=3 ) – Merge threshold for nearby terminal states.

-
num_mcmc_simulations ( int , default=1300 ) – Number of random-walk/MCMC simulations for lineage probabilities.

-
piegraph_arrow_head_width ( float , default=0.1 ) – Arrow head width in pie-chart trajectory graph.

-
piegraph_edgeweight_scalingfactor ( float , default=1.5 ) – Edge-width scaling in pie-chart trajectory graph.

-
max_visual_outgoing_edges ( int , default=2 ) – Maximum outgoing edges per node in visual graph rendering.

-
via_coarse ( object , optional ) – Optional coarse VIA model used for hierarchical runs.

-
velocity_matrix ( numpy.ndarray , optional ) – RNA velocity matrix used to orient transitions.

-
gene_matrix ( numpy.ndarray , optional ) – Expression matrix aligned with `velocity_matrix `.

-
velo_weight ( float , default=0.5 ) – Relative weight of velocity-informed transitions.

-
edgebundle_pruning ( float , optional ) – Pruning threshold before edge bundling.

-
A_velo ( numpy.ndarray , optional ) – Cluster-level velocity transition matrix.

-
CSM ( Any , optional ) – Optional custom transition/similarity matrix.

-
edgebundle_pruning_twice ( bool , default=False ) – Whether to apply two-pass pruning before edge bundling.

-
pca_loadings ( numpy.ndarray , optional ) – PCA loadings used in velocity projection.

-
time_series ( bool , default=False ) – Whether to enable time-series constraints.

-
time_series_labels ( list , optional ) – Ordered temporal labels per cell.

-
knn_sequential ( int , default=10 ) – Number of forward temporal neighbors ( `t `to `t+1 `).

-
knn_sequential_reverse ( int , default=0 ) – Number of reverse temporal neighbors ( `t `to `t-1 `).

-
t_diff_step ( int , default=1 ) – Maximum temporal step size allowed in sequential KNN links.

-
single_cell_transition_matrix ( Any , optional ) – Optional precomputed single-cell transition matrix.

-
embedding_type ( str , default='via-mds' ) – Embedding algorithm used by VIA (for example `'via-mds' `).

-
do_compute_embedding ( bool , default=False ) – Whether to compute VIA embedding during initialization.

-
color_dict ( dict , optional ) – Mapping from category to plotting color.

-
user_defined_terminal_cell ( list , default= [ ] ) – User-defined terminal cell indices.

-
user_defined_terminal_group ( list , default= [ ] ) – User-defined terminal cluster/group labels.

-
do_gaussian_kernel_edgeweights ( bool , default=False ) – Whether to use Gaussian-kernel edge weights.

-
RW2_mode ( bool , default=False ) – Enable RW2 random-walk mode in VIA.

-
working_dir_fp ( str , default='/home/shobi/Trajectory/Datasets/' ) – Working directory used by VIA for intermediate files.

Methods

`__init__ `(adata[, adata_key, adata_ncomps, ...])

Initialize a pyVIA trajectory inference model.

`get_piechart_dict `([label, clusters])

Get cluster composition dictionary for pie chart visualization.

`get_pseudotime `([adata])

Extract the pseudotime values computed by VIA.

`plot_clustergraph `(gene_list[, arrow_head, ...])

Plot cluster graph with aggregated gene-expression nodes.

`plot_gene_trend `([gene_list, figsize, ...])

Plot smoothed gene trends along VIA pseudotime.

`plot_gene_trend_heatmap `(gene_list[, ...])

Plot lineage-specific heatmaps of gene trends.

`plot_lineage_probability `([clusters, basis, ...])

Plot lineage membership probabilities in embedding space.

`plot_piechart_graph `([clusters, type_data, ...])

Plot two subplots with clustergraph representation showing cluster composition and pseudotime/gene expression.

`plot_stream `([clusters, basis, density_grid, ...])

Plot streamlines of inferred cell-state flow on embedding.

`plot_trajectory_gams `([clusters, basis, ...])

Project coarse VIA trajectories onto embedding.

`run `()

Calculate the VIA graph and pseudotime.
