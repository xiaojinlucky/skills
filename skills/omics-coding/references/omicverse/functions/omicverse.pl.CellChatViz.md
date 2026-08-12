# omicverse.pl.CellChatViz #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.CellChatViz`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.CellChatViz.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Visualization helper for CellPhoneDB cell-cell communication outputs.

## Signature

```text
class omicverse.pl. CellChatViz ( adata , palette = None )
```

## Parameters

- `adata`: ( AnnData ) – AnnData containing CellPhoneDB interaction results.
- `palette`: ( dict or sequence or None ) – Color mapping used for sender/receiver cell types.

## Full Documentation

# omicverse.pl.CellChatViz #

class omicverse.pl. CellChatViz ( adata , palette = None ) [source] #

Visualization helper for CellPhoneDB cell-cell communication outputs.

Parameters :

-
adata ( AnnData ) – AnnData containing CellPhoneDB interaction results.

-
palette ( dict or sequence or None ) – Color mapping used for sender/receiver cell types.

Returns :

Initializes visualization state for interaction and pathway-level plotting.

Return type :

None

Examples

```text
>>> viz = ov.pl.CellChatViz(adata_cpdb, palette=color_dict)

```

__init__ ( adata , palette = None ) [source] #

Initialize with CellPhoneDB AnnData object

Parameters :

-
adata ( AnnData ) – AnnData with CellPhoneDB outputs: `obs `includes sender/receiver, `layers `includes pvalues/means.

-
palette ( dict or list or None ) – Optional color mapping. Dict uses explicit cell-type keys; list is mapped to sorted cell types.

Methods

`__init__ `(adata[, palette])

Initialize with CellPhoneDB AnnData object

`analyze_pathway_statistics `(pathway_stats[, ...])

Analyze and display detailed pathway statistics

`computeNetSimilarity `([similarity_type, k, ...])

计算信号网络之间的相似性（类似CellChat的computeNetSimilarity功能）

`compute_aggregated_network `([...])

Compute aggregated cell communication network

`compute_communication_prob `([...])

Calculate cell-cell communication probability matrix (similar to CellChat's prob matrix)

`compute_network_similarity `([method])

Compute pairwise similarity between pathway-specific networks.

`compute_pathway_communication `([method, ...])

Calculate pathway-level cell communication strength (similar to CellChat methods)

`compute_pathway_network `([pvalue_threshold])

Compute one sender-receiver matrix per signaling pathway.

`demo_curved_arrows `([signaling_pathway, ...])

Demo function to show curved arrow effects

`extractEnrichedLR `(signaling[, ...])

Extract all significant L-R pairs in the specified signaling pathway (Similar to CellChat's extractEnrichedLR function)

`get_ligand_receptor_pairs `([...])

Get all significant ligand-receptor pair lists

`get_signaling_matrix `([pattern, signaling, ...])

Get signaling strength matrix

`get_signaling_pathways `([min_interactions, ...])

Get all significant signaling pathway lists using statistically more reliable methods to combine p-values from multiple L-R pairs

`get_significant_pathways_v2 `([...])

Determine significant pathways based on pathway-level communication strength (more aligned with CellChat logic)

`identifyCommunicationPatterns `([pattern, k, ...])

识别细胞通信模式使用NMF分解（类似CellChat的identifyCommunicationPatterns功能）

`identifyOverExpressedGenes `(signaling[, ...])

识别在特定模式中过表达的基因

`identify_signaling_role `([pattern, ...])

Score cell types by their signaling roles in the communication network.

`mean `([count_min])

Compute mean expression matrix for cell-cell interactions (like CellChat)

`netAnalysis_computeCentrality `([signaling, ...])

Calculate network centrality metrics (imitating CellChat's netAnalysis_computeCentrality function)

`netAnalysis_contribution `(signaling[, ...])

Calculate the contribution of each ligand-receptor pair to the overall signaling pathway and visualize (Similar to CellChat's netAnalysis_contribution function)

`netAnalysis_signalingRole_heatmap `([pattern, ...])

Create a heatmap to analyze the signaling roles of cell populations (outgoing or incoming contribution) Use Marsilea for modern heatmap visualization

`netAnalysis_signalingRole_network `([...])

Visualize signaling roles of cell populations (imitating CellChat's netAnalysis_signalingRole_network function)

`netAnalysis_signalingRole_network_marsilea `([...])

使用Marsilea创建高级信号角色热图（CellChat风格的netAnalysis_signalingRole_network）

`netAnalysis_signalingRole_scatter `([...])

Create 2D scatter plot to visualize cell signaling roles

`netEmbedding `([method, n_components, figsize])

Embed pathway similarity into low-dimensional space and cluster pathways.

`netVisual_aggregate `(signaling[, layout, ...])

Draw an aggregated communication network for selected signaling pathways.

`netVisual_bubble `([sources, targets, ...])

Plot pathway-level communication as a bubble matrix.

`netVisual_bubble_lr `([sources_use, ...])

Create bubble plot to visualize specific ligand-receptor pairs in cell-cell communication Similar to netVisual_bubble_marsilea but focuses on specific L-R pairs instead of pathways

`netVisual_bubble_marsilea `([sources_use, ...])

Create advanced bubble plot using Marsilea's SizedHeatmap to visualize cell-cell communication Similar to CellChat's netVisual_bubble function, but uses SizedHeatmap to make circle size more meaningful

`netVisual_chord `(matrix[, title, threshold, ...])

Plot a polar chord-like diagram for cell-cell communication.

`netVisual_chord_LR `([ligand_receptor_pairs, ...])

Create chord diagram visualization for specific ligand-receptor pairs (mimicking CellChat's ligand-receptor level analysis)

`netVisual_chord_cell `([signaling, ...])

Create chord diagram visualization using mpl-chord-diagram (mimicking CellChat's netVisual_chord_cell function)

`netVisual_chord_gene `([sources_use, ...])

Draw a chord diagram of all ligand-receptor pairs for specific cell types as senders (gene-level) Each sector represents a ligand or receptor, ligands use sender color, receptors use receiver color

`netVisual_circle `(matrix[, title, ...])

Circular network visualization (similar to CellChat's circle plot) Uses sender cell type colors as edge gradient colors

`netVisual_circle_focused `(matrix[, title, ...])

Draw focused circular network diagram, showing only cell types with actual interactions

`netVisual_diffusion `([similarity_type, ...])

可视化信号网络相似性和扩散模式

`netVisual_heatmap `(matrix[, title, cmap, ...])

Visualize a communication matrix as a sender-receiver heatmap.

`netVisual_heatmap_marsilea `([signaling, ...])

Draw a CellChat-style communication heatmap with Marsilea.

`netVisual_heatmap_marsilea_focused `([...])

Draw a focused Marsilea heatmap keeping only active cell types.

`netVisual_hierarchy `([pathway_name, sources, ...])

Visualize directed communication as a two-layer hierarchy plot.

`netVisual_individual `(signaling[, ...])

Visualize cell-cell communication mediated by individual ligand-receptor pairs (Similar to CellChat's netVisual_individual function)

`netVisual_individual_circle `([...])

Plot one outgoing communication circle per cell type.

`netVisual_individual_circle_incoming `([...])

Plot one incoming communication circle per cell type.

`netVisual_signaling_heatmap `([pattern, ...])

Use Marsilea to create a signaling pathway heatmap, showing signaling strength of cell types

`netVisual_single_circle `(cell_type[, ...])

Plot communication circle for one selected cell type.

`plot_all_visualizations `([pvalue_threshold, ...])

Generate all major visualization plots

`pvalue `([count_min])

Compute p-value matrix for cell-cell interactions (like CellChat)

`selectK `([pattern, k_range, nrun, ...])

选择NMF分解的最优K值（类似CellChat的selectK功能）
