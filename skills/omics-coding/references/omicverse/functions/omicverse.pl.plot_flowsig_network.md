# omicverse.pl.plot_flowsig_network #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.plot_flowsig_network`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.plot_flowsig_network.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Create a flowsig network visualization showing GEM modules and gene flows.

## Signature

```text
omicverse.pl. plot_flowsig_network ( flow_network , gem_plot , figsize = (8, 4) , curve_awarg = {'eps': 2} , node_shape = {'GEM': '^', 'Receptor': 'o', 'Sender': 'o'} , ** kwargs )
```

## Parameters

- `flow_network`: ( nx.Graph ) – FlowSig graph containing GEM, sender, and receptor nodes.
- `gem_plot`: ( list ) – GEM module subset to include in rendered subgraph.
- `figsize`: ( tuple ) – Figure size for network plot.
- `curve_awarg`: ( dict ) – Optional keyword arguments for curved-edge drawing.
- `node_shape`: ( dict ) – Mapping from node class to marker shape.
- `**kwargs`: – Additional arguments passed to plot_curve_network .

## Full Documentation

# omicverse.pl.plot_flowsig_network #

omicverse.pl. plot_flowsig_network ( flow_network , gem_plot , figsize = (8, 4) , curve_awarg = {'eps': 2} , node_shape = {'GEM': '^', 'Receptor': 'o', 'Sender': 'o'} , ** kwargs ) [source] #

Create a flowsig network visualization showing GEM modules and gene flows.

Parameters :

-
flow_network ( nx.Graph ) – FlowSig graph containing GEM, sender, and receptor nodes.

-
gem_plot ( list ) – GEM module subset to include in rendered subgraph.

-
figsize ( tuple ) – Figure size for network plot.

-
curve_awarg ( dict ) – Optional keyword arguments for curved-edge drawing.

-
node_shape ( dict ) – Mapping from node class to marker shape.

-
**kwargs – Additional arguments passed to `plot_curve_network `.

Returns :

Figure and axes of the FlowSig network plot.

Return type :

Tuple[ matplotlib.figure.Figure , matplotlib.axes.Axes ]
