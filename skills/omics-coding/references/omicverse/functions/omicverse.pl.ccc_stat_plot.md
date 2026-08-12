# omicverse.pl.ccc_stat_plot #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.ccc_stat_plot`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.ccc_stat_plot.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot communication summaries, distributions, and pathway statistics.

## Signature

```text
omicverse.pl. ccc_stat_plot ( adata , * , plot_type = 'bar' , comparison_adata = None , source_adata = None , source_groupby = None , display_by = 'aggregation' , sender_use = None , receiver_use = None , signaling = None , interaction_use = None , pair_lr_use = None , result_uns_key = 'liana_res' , score_key = 'specificity_rank' , pvalue_key = 'specificity_rank' , inverse_score = True , inverse_pvalue = False , classification = None , classification_reference = 'cellchat' , classification_fallback = 'family' , pvalue_threshold = 0.05 , group_by = 'interaction' , compare_by = 'overall' , measure = 'weight' , pattern = 'all' , idents_use = None , facet_by = None , value = 'sum' , top_n = 20 , min_receiver_flow = 0.0 , pathway_method = 'mean' , min_lr_pairs = 1 , min_expression = 0.1 , strength_threshold = 0.5 , min_significant_pairs = 1 , palette = None , measures = None , cmap = 'RdYlBu_r' , figsize = (8, 5) , title = None , verbose = True , show = False , save = False )
```

## Parameters

- `adata`: ( anndata.AnnData ) – Communication AnnData produced by the OmicVerse CCC workflow, or a regular AnnData containing a LIANA result table in adata.uns[result_uns_key] . LIANA inputs are adapted internally to the communication format expected by ccc_* .
- `plot_type`: ( str , default="bar" ) – Summary view to render. Supported values include bar plots, sankey diagrams, score distributions, signaling role analyses, pathway summaries, ligand-receptor contribution plots, differential comparisons, and pathway gene-expression summaries.
- `comparison_adata`: ( anndata.AnnData or None , default=None ) – Second communication AnnData used by comparison-style summary plots.
- `source_adata`: ( anndata.AnnData or None , default=None ) – Expression AnnData used by plot_type='gene' to summarize pathway gene expression across groups.
- `source_groupby`: ( str or None , default=None ) – Observation column in source_adata.obs used to group cells before plotting gene-expression summaries.
- `display_by`: ( {"aggregation" , "interaction"} , default="aggregation" ) – Whether to summarize results at the signaling/pathway level or at the interaction level.
- `sender_use`: ( str , sequence of str , or None , default=None ) – Optional sender cell types retained in sender-aware summary plots.
- `receiver_use`: ( str , sequence of str , or None , default=None ) – Optional receiver cell types retained in receiver-aware summary plots.
- `signaling`: ( str , sequence of str , or None , default=None ) – Signaling pathway name or names to visualize.
- `interaction_use`: ( str , sequence of str , or None , default=None ) – Interaction names used to restrict interaction-level statistics.
- `pair_lr_use`: ( str , sequence of str , or None , default=None ) – Ligand-receptor pair identifiers used by pair-specific statistics.
- `result_uns_key`: ( str , default="liana_res" ) – adata.uns key searched when adata is not already a communication AnnData.
- `score_key`: ( str , default="specificity_rank" ) – Columns used when auto-converting LIANA results.
- `pvalue_key`: ( str , default="specificity_rank" ) – Columns used when auto-converting LIANA results.
- `inverse_score`: ( bool , default= ( True , False ) ) – Whether the LIANA score or p-value columns should be inverted during automatic conversion.
- `inverse_pvalue`: ( bool , default= ( True , False ) ) – Whether the LIANA score or p-value columns should be inverted during automatic conversion.
- `classification`: ( str , mapping , or None , default=None ) – Optional LIANA classification override used only during automatic conversion.
- `classification_reference`: ( str , pandas.DataFrame , or None , default="cellchat" ) – Reference used to backfill pathway labels during automatic LIANA conversion.
- `classification_fallback`: ( str or None , default="family" ) – Fallback pathway label strategy used during automatic LIANA conversion.
- `pvalue_threshold`: ( float , default=0.05 ) – Maximum p-value retained as a significant communication event.
- `group_by`: ( {"interaction" , "classification" , "pair" , "sender" , "receiver"} , default="interaction" ) – Category used to group communication events in bar, box, violin, or contribution summaries.
- `compare_by`: ( {"overall" , "celltype"} , default="overall" ) – Comparison mode used by summary plots that contrast communication patterns across cell types or globally.
- `measure`: ( {"weight" , "count"} , default="weight" ) – Communication quantity summarized by applicable statistical plots.
- `pattern`: ( {"outgoing" , "incoming" , "all"} , default="all" ) – Signaling role direction used by role-based summaries.
- `idents_use`: ( str , sequence of str , or None , default=None ) – Optional subset of identities retained in role-change or comparison plots.
- `facet_by`: ( {"sender" , "receiver"} or None , default=None ) – Split compatible plots by sender or receiver.
- `value`: ( {"sum" , "mean" , "max" , "count"} , default="sum" ) – Aggregation statistic used to summarize communication strengths before plotting.
- `top_n`: ( int , default=20 ) – Number of top pathways, interactions, or pairs retained in ranked summaries.
- `min_receiver_flow`: ( float , default=0.0 ) – Minimum total flow required for a receiver node to be retained in Sankey plots. This is mainly useful for plot_type='sankey', display_by='interaction' when many tiny receiver nodes make the right side unreadable.
- `pathway_method`: ( str , default="mean" ) – Method used to summarize multiple ligand-receptor pairs into pathway level scores.
- `min_lr_pairs`: ( int , default=1 ) – Minimum number of ligand-receptor pairs required for a pathway to be retained in pathway summaries.
- `min_expression`: ( float , default=0.1 ) – Minimum grouped expression threshold used by pathway-level summaries.
- `strength_threshold`: ( float , default=0.5 ) – Minimum pathway strength retained in pathway summary statistics.
- `min_significant_pairs`: ( int , default=1 ) – Minimum number of significant ligand-receptor pairs required for a pathway to be highlighted.
- `palette`: ( mapping , sequence , or None , default=None ) – Color palette used for cell types, pathways, or groups.
- `measures`: ( sequence of str or None , default=None ) – Role-network measures to display, such as outgoing or incoming centrality summaries.
- `cmap`: ( str , default="RdYlBu_r" ) – Colormap used by heatmap-like statistical summaries.
- `figsize`: ( tuple of float , default= ( 8 , 5 ) ) – Figure size in inches.
- `title`: ( str or None , default=None ) – Custom title for the generated figure. When omitted, a plot-specific default title is used.
- `verbose`: ( bool , default=True ) – Whether pathway-summary style plots should print progress messages and summary tables. This currently affects plot_type='pathway_summary' .
- `show`: ( bool , default=False ) – Whether to immediately display the figure.
- `save`: ( str or bool , default=False ) – File path for saving the figure, or False to skip saving.

## Full Documentation

# omicverse.pl.ccc_stat_plot #

omicverse.pl. ccc_stat_plot ( adata , * , plot_type = 'bar' , comparison_adata = None , source_adata = None , source_groupby = None , display_by = 'aggregation' , sender_use = None , receiver_use = None , signaling = None , interaction_use = None , pair_lr_use = None , result_uns_key = 'liana_res' , score_key = 'specificity_rank' , pvalue_key = 'specificity_rank' , inverse_score = True , inverse_pvalue = False , classification = None , classification_reference = 'cellchat' , classification_fallback = 'family' , pvalue_threshold = 0.05 , group_by = 'interaction' , compare_by = 'overall' , measure = 'weight' , pattern = 'all' , idents_use = None , facet_by = None , value = 'sum' , top_n = 20 , min_receiver_flow = 0.0 , pathway_method = 'mean' , min_lr_pairs = 1 , min_expression = 0.1 , strength_threshold = 0.5 , min_significant_pairs = 1 , palette = None , measures = None , cmap = 'RdYlBu_r' , figsize = (8, 5) , title = None , verbose = True , show = False , save = False ) [source] #

Plot communication summaries, distributions, and pathway statistics.

Parameters :

-
adata ( anndata.AnnData ) – Communication AnnData produced by the OmicVerse CCC workflow, or a regular AnnData containing a LIANA result table in `adata.uns[result_uns_key] `. LIANA inputs are adapted internally to the communication format expected by `ccc_* `.

-
plot_type ( str , default="bar" ) – Summary view to render. Supported values include bar plots, sankey diagrams, score distributions, signaling role analyses, pathway summaries, ligand-receptor contribution plots, differential comparisons, and pathway gene-expression summaries.

-
comparison_adata ( anndata.AnnData or None , default=None ) – Second communication AnnData used by comparison-style summary plots.

-
source_adata ( anndata.AnnData or None , default=None ) – Expression AnnData used by `plot_type='gene' `to summarize pathway gene expression across groups.

-
source_groupby ( str or None , default=None ) – Observation column in `source_adata.obs `used to group cells before plotting gene-expression summaries.

-
display_by ( {"aggregation" , "interaction"} , default="aggregation" ) – Whether to summarize results at the signaling/pathway level or at the interaction level.

-
sender_use ( str , sequence of str , or None , default=None ) – Optional sender cell types retained in sender-aware summary plots.

-
receiver_use ( str , sequence of str , or None , default=None ) – Optional receiver cell types retained in receiver-aware summary plots.

-
signaling ( str , sequence of str , or None , default=None ) – Signaling pathway name or names to visualize.

-
interaction_use ( str , sequence of str , or None , default=None ) – Interaction names used to restrict interaction-level statistics.

-
pair_lr_use ( str , sequence of str , or None , default=None ) – Ligand-receptor pair identifiers used by pair-specific statistics.

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
group_by ( {"interaction" , "classification" , "pair" , "sender" , "receiver"} , default="interaction" ) – Category used to group communication events in bar, box, violin, or contribution summaries.

-
compare_by ( {"overall" , "celltype"} , default="overall" ) – Comparison mode used by summary plots that contrast communication patterns across cell types or globally.

-
measure ( {"weight" , "count"} , default="weight" ) – Communication quantity summarized by applicable statistical plots.

-
pattern ( {"outgoing" , "incoming" , "all"} , default="all" ) – Signaling role direction used by role-based summaries.

-
idents_use ( str , sequence of str , or None , default=None ) – Optional subset of identities retained in role-change or comparison plots.

-
facet_by ( {"sender" , "receiver"} or None , default=None ) – Split compatible plots by sender or receiver.

-
value ( {"sum" , "mean" , "max" , "count"} , default="sum" ) – Aggregation statistic used to summarize communication strengths before plotting.

-
top_n ( int , default=20 ) – Number of top pathways, interactions, or pairs retained in ranked summaries.

-
min_receiver_flow ( float , default=0.0 ) – Minimum total flow required for a receiver node to be retained in Sankey plots. This is mainly useful for `plot_type='sankey', display_by='interaction' `when many tiny receiver nodes make the right side unreadable.

-
pathway_method ( str , default="mean" ) – Method used to summarize multiple ligand-receptor pairs into pathway level scores.

-
min_lr_pairs ( int , default=1 ) – Minimum number of ligand-receptor pairs required for a pathway to be retained in pathway summaries.

-
min_expression ( float , default=0.1 ) – Minimum grouped expression threshold used by pathway-level summaries.

-
strength_threshold ( float , default=0.5 ) – Minimum pathway strength retained in pathway summary statistics.

-
min_significant_pairs ( int , default=1 ) – Minimum number of significant ligand-receptor pairs required for a pathway to be highlighted.

-
palette ( mapping , sequence , or None , default=None ) – Color palette used for cell types, pathways, or groups.

-
measures ( sequence of str or None , default=None ) – Role-network measures to display, such as outgoing or incoming centrality summaries.

-
cmap ( str , default="RdYlBu_r" ) – Colormap used by heatmap-like statistical summaries.

-
figsize ( tuple of float , default= ( 8 , 5 ) ) – Figure size in inches.

-
title ( str or None , default=None ) – Custom title for the generated figure. When omitted, a plot-specific default title is used.

-
verbose ( bool , default=True ) – Whether pathway-summary style plots should print progress messages and summary tables. This currently affects `plot_type='pathway_summary' `.

-
show ( bool , default=False ) – Whether to immediately display the figure.

-
save ( str or bool , default=False ) – File path for saving the figure, or `False `to skip saving.

Returns :

A `(fig, ax) `tuple containing the Matplotlib figure and the main axes used for the rendered statistical summary.

Return type :

tuple
