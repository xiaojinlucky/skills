# omicverse.single.pathway_enrichment_plot #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.pathway_enrichment_plot`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.pathway_enrichment_plot.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Visualize the pathway enrichment analysis results as a heatmap.

## Signature

```text
omicverse.single. pathway_enrichment_plot ( enrich_res , term_num = 5 , return_table = False , figsize = (3, 10) , plot_title = '' , ** kwds )
```

## Parameters

- `enrich_res`: ( pd.DataFrame ) – DataFrame returned by pathway_enrichment .
- `term_num`: ( int ) – Number of top terms kept per cluster.
- `return_table`: ( bool ) – Whether to return pivot/heatmap table instead of plotting.
- `figsize`: ( tuple ) – Figure size for heatmap.
- `plot_title`: ( str ) – Heatmap title.
- `**kwds`: – Additional keyword arguments forwarded to sns.heatmap .

## Full Documentation

# omicverse.single.pathway_enrichment_plot #

omicverse.single. pathway_enrichment_plot ( enrich_res , term_num = 5 , return_table = False , figsize = (3, 10) , plot_title = '' , ** kwds ) [source] #

Visualize the pathway enrichment analysis results as a heatmap.

Parameters :

-
enrich_res ( pd.DataFrame ) – DataFrame returned by `pathway_enrichment `.

-
term_num ( int ) – Number of top terms kept per cluster.

-
return_table ( bool ) – Whether to return pivot/heatmap table instead of plotting.

-
figsize ( tuple ) – Figure size for heatmap.

-
plot_title ( str ) – Heatmap title.

-
**kwds – Additional keyword arguments forwarded to `sns.heatmap `.

Returns :

-
matplotlib.axes.Axes or pd.DataFrame – Heatmap axes, or table when `return_table=True `.

-
Examples – >>> res = pathway_enrichment(adata, pathways_dict) >>> pathway_enrichment_plot(res, term_num=10, return_table=True, figsize=(6,12), cmap=’Blues’)
