# omicverse.pl.ccc_network_plot #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.ccc_network_plot`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.ccc_network_plot.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot cell-cell communication networks with multiple graph styles.

## Signature

```text
omicverse.pl. ccc_network_plot ( adata , * , plot_type = 'circle' , comparison_adata = None , display_by = 'aggregation' , sender_use = None , receiver_use = None , signaling = None , interaction_use = None , pair_lr_use = None , result_uns_key = 'liana_res' , score_key = 'specificity_rank' , pvalue_key = 'specificity_rank' , inverse_score = True , inverse_pvalue = False , classification = None , classification_reference = 'cellchat' , classification_fallback = 'family' , pvalue_threshold = 0.05 , value = 'sum' , top_n = None , ligand = None , receptor = None , normalize_to_sender = True , rotate_names = True , min_interaction_threshold = 0.0 , node_positions = None , embedding_points = None , palette = None , ncols = None , nrows = None , figsize = (7, 7) , title = None , verbose = True , show = False , save = False )
```

## Parameters

- `adata`: ( anndata.AnnData ) – Communication AnnData produced by the OmicVerse CCC workflow, or a regular AnnData containing a LIANA result table in adata.uns[result_uns_key] . LIANA inputs are adapted internally to the communication format expected by ccc_* .
- `plot_type`: ( str , default="circle" ) – Network style to render. Supported values include aggregated circle views, pathway-filtered circle networks, interaction flow plots, bipartite ligand-receptor layouts, embedding-based networks, differential comparison networks, chord summaries, and diffusion-style visualizations.
- `comparison_adata`: ( anndata.AnnData or None , default=None ) – Second communication AnnData used by plot_type='diff_network' to compute differential edges between two conditions.
- `display_by`: ( {"aggregation" , "interaction"} , default="aggregation" ) – Whether to summarize networks at the signaling/pathway aggregation level or at the individual interaction level when the chosen plot_type supports both.
- `sender_use`: ( str , sequence of str , or None , default=None ) – Optional sender cell types to keep in the plot.
- `receiver_use`: ( str , sequence of str , or None , default=None ) – Optional receiver cell types to keep in the plot.
- `signaling`: ( str , sequence of str , or None , default=None ) – Signaling pathway name or names to visualize. Required by several pathway-specific network views.
- `interaction_use`: ( str , sequence of str , or None , default=None ) – Interaction names to keep when plotting interaction-level networks.
- `pair_lr_use`: ( str , sequence of str , or None , default=None ) – Ligand-receptor pair identifiers used to filter individual or interaction-focused plots.
- `result_uns_key`: ( str , default="liana_res" ) – adata.uns key searched when adata is not already a communication AnnData.
- `score_key`: ( str , default="specificity_rank" ) – Columns used when auto-converting LIANA results.
- `pvalue_key`: ( str , default="specificity_rank" ) – Columns used when auto-converting LIANA results.
- `inverse_score`: ( bool , default= ( True , False ) ) – Whether the LIANA score or p-value columns should be inverted during automatic conversion.
- `inverse_pvalue`: ( bool , default= ( True , False ) ) – Whether the LIANA score or p-value columns should be inverted during automatic conversion.
- `classification`: ( str , mapping , or None , default=None ) – Optional LIANA classification override used only during automatic conversion.
- `classification_reference`: ( str , pandas.DataFrame , or None , default="cellchat" ) – Reference used to backfill pathway labels during automatic LIANA conversion.
- `classification_fallback`: ( str or None , default="family" ) – Fallback pathway label strategy used during automatic LIANA conversion.
- `pvalue_threshold`: ( float , default=0.05 ) – Maximum p-value retained as a significant communication event.
- `value`: ( {"sum" , "mean" , "max" , "count"} , default="sum" ) – Aggregation statistic used when communication strengths are collapsed before plotting.
- `top_n`: ( int or None , default=None ) – Number of top pathways, interactions, or pairs retained for plot types that rank results before drawing. Circle-style network views keep all significant edges by default; flow-style views use an internal default of 20 when top_n is omitted.
- `ligand`: ( str or None , default=None ) – Ligand name used by ligand-centric plots such as bipartite or ligand-receptor chord views.
- `receptor`: ( str , sequence of str , or None , default=None ) – Receptor name or names used by receptor-specific network views.
- `normalize_to_sender`: ( bool , default=True ) – Whether to normalize outgoing edge contributions per sender before plotting chord-style networks.
- `rotate_names`: ( bool , default=True ) – Whether to rotate node labels to follow the circle in chord-like layouts.
- `min_interaction_threshold`: ( float , default=0.0 ) – Minimum edge weight shown in focused or thresholded network views.
- `node_positions`: ( mapping , array-like , or None , default=None ) – Precomputed node coordinates used by embedding_network or other layouts that require explicit positions.
- `embedding_points`: ( array-like or None , default=None ) – Optional background embedding coordinates plotted together with embedding_network edges.
- `palette`: ( mapping , sequence , or None , default=None ) – Color palette used for cell types, pathways, or nodes.
- `ncols`: ( int or None , default=None ) – Number of subplot columns used by multi-panel network views such as individual_outgoing and individual_incoming . When omitted, a plot-specific default is used.
- `nrows`: ( int or None , default=None ) – Number of subplot rows used by multi-panel network views such as individual_outgoing and individual_incoming . When omitted, the value is inferred from ncols and the number of selected panels.
- `figsize`: ( tuple of float , default= ( 7 , 7 ) ) – Figure size in inches.
- `title`: ( str or None , default=None ) – Custom title for the generated figure. When omitted, a plot-specific default title is used.
- `verbose`: ( bool , default=True ) – Reserved for method-specific progress output. Network views remain silent by default; this parameter keeps the ccc_* API uniform.
- `show`: ( bool , default=False ) – Whether to immediately display the figure.
- `save`: ( str or bool , default=False ) – File path for saving the figure, or False to skip saving.

## Full Documentation

# omicverse.pl.ccc_network_plot #

omicverse.pl. ccc_network_plot ( adata , * , plot_type = 'circle' , comparison_adata = None , display_by = 'aggregation' , sender_use = None , receiver_use = None , signaling = None , interaction_use = None , pair_lr_use = None , result_uns_key = 'liana_res' , score_key = 'specificity_rank' , pvalue_key = 'specificity_rank' , inverse_score = True , inverse_pvalue = False , classification = None , classification_reference = 'cellchat' , classification_fallback = 'family' , pvalue_threshold = 0.05 , value = 'sum' , top_n = None , ligand = None , receptor = None , normalize_to_sender = True , rotate_names = True , min_interaction_threshold = 0.0 , node_positions = None , embedding_points = None , palette = None , ncols = None , nrows = None , figsize = (7, 7) , title = None , verbose = True , show = False , save = False ) [source] #

Plot cell-cell communication networks with multiple graph styles.

Parameters :

-
adata ( anndata.AnnData ) – Communication AnnData produced by the OmicVerse CCC workflow, or a regular AnnData containing a LIANA result table in `adata.uns[result_uns_key] `. LIANA inputs are adapted internally to the communication format expected by `ccc_* `.

-
plot_type ( str , default="circle" ) – Network style to render. Supported values include aggregated circle views, pathway-filtered circle networks, interaction flow plots, bipartite ligand-receptor layouts, embedding-based networks, differential comparison networks, chord summaries, and diffusion-style visualizations.

-
comparison_adata ( anndata.AnnData or None , default=None ) – Second communication AnnData used by `plot_type='diff_network' `to compute differential edges between two conditions.

-
display_by ( {"aggregation" , "interaction"} , default="aggregation" ) – Whether to summarize networks at the signaling/pathway aggregation level or at the individual interaction level when the chosen `plot_type `supports both.

-
sender_use ( str , sequence of str , or None , default=None ) – Optional sender cell types to keep in the plot.

-
receiver_use ( str , sequence of str , or None , default=None ) – Optional receiver cell types to keep in the plot.

-
signaling ( str , sequence of str , or None , default=None ) – Signaling pathway name or names to visualize. Required by several pathway-specific network views.

-
interaction_use ( str , sequence of str , or None , default=None ) – Interaction names to keep when plotting interaction-level networks.

-
pair_lr_use ( str , sequence of str , or None , default=None ) – Ligand-receptor pair identifiers used to filter individual or interaction-focused plots.

-
result_uns_key ( str , default="liana_res" ) – `adata.uns `key searched when `adata `is not already a communication AnnData.

-
score_key ( str , default="specificity_rank" ) – Columns used when auto-converting LIANA results.

-
pvalue_key ( str , default="specificity_rank" ) – Columns used when auto-converting LIANA results.

-
inverse_score ( bool , default= ( True , False ) ) – Whether the LIANA score or p-value columns should be inverted during automatic conversion.

-
inverse_pvalue ( bool , default= ( True , False ) ) – Whether the LIANA score or p-value columns should be inverted during automatic conversion.

-
classification ( str , mapping , or None , default=None ) – Optional LIANA classification override used only during automatic conversion.

-
classification_reference ( str , pandas.DataFrame , or None , default="cellchat" ) – Reference used to backfill pathway labels during automatic LIANA conversion.

-
classification_fallback ( str or None , default="family" ) – Fallback pathway label strategy used during automatic LIANA conversion.

-
pvalue_threshold ( float , default=0.05 ) – Maximum p-value retained as a significant communication event.

-
value ( {"sum" , "mean" , "max" , "count"} , default="sum" ) – Aggregation statistic used when communication strengths are collapsed before plotting.

-
top_n ( int or None , default=None ) – Number of top pathways, interactions, or pairs retained for plot types that rank results before drawing. Circle-style network views keep all significant edges by default; flow-style views use an internal default of 20 when `top_n `is omitted.

-
ligand ( str or None , default=None ) – Ligand name used by ligand-centric plots such as `bipartite `or ligand-receptor chord views.

-
receptor ( str , sequence of str , or None , default=None ) – Receptor name or names used by receptor-specific network views.

-
normalize_to_sender ( bool , default=True ) – Whether to normalize outgoing edge contributions per sender before plotting chord-style networks.

-
rotate_names ( bool , default=True ) – Whether to rotate node labels to follow the circle in chord-like layouts.

-
min_interaction_threshold ( float , default=0.0 ) – Minimum edge weight shown in focused or thresholded network views.

-
node_positions ( mapping , array-like , or None , default=None ) – Precomputed node coordinates used by `embedding_network `or other layouts that require explicit positions.

-
embedding_points ( array-like or None , default=None ) – Optional background embedding coordinates plotted together with `embedding_network `edges.

-
palette ( mapping , sequence , or None , default=None ) – Color palette used for cell types, pathways, or nodes.

-
ncols ( int or None , default=None ) – Number of subplot columns used by multi-panel network views such as `individual_outgoing `and `individual_incoming `. When omitted, a plot-specific default is used.

-
nrows ( int or None , default=None ) – Number of subplot rows used by multi-panel network views such as `individual_outgoing `and `individual_incoming `. When omitted, the value is inferred from `ncols `and the number of selected panels.

-
figsize ( tuple of float , default= ( 7 , 7 ) ) – Figure size in inches.

-
title ( str or None , default=None ) – Custom title for the generated figure. When omitted, a plot-specific default title is used.

-
verbose ( bool , default=True ) – Reserved for method-specific progress output. Network views remain silent by default; this parameter keeps the `ccc_* `API uniform.

-
show ( bool , default=False ) – Whether to immediately display the figure.

-
save ( str or bool , default=False ) – File path for saving the figure, or `False `to skip saving.

Returns :

A `(fig, ax) `tuple containing the Matplotlib figure and the main axes used for the rendered network.

Return type :

tuple
