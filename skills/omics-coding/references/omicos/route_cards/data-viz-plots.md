# Data Visualization (Universal)

- Source raw material: `../raw_skills/data-viz-plots/SOURCE.md`
- Domain: `generic_visualization`
- Route role: `fallback_only`
- Object route: `generic_table_or_array`
- Primary authority: analysis-native plotting docs after native options are rejected
- Official confirmation: `conditional`

## How To Use

1. Clarify the user question, input object, species, grouping columns, and outputs.
2. Search `references/function_index.tsv` and `references/parameter_index.tsv` first.
3. Open the shortlisted OmicVerse/SCOP docs and verify exact function and parameters.
4. Use this OmicOS card only as a workflow reminder.
5. Complete the Analysis-Native Visualization Gate before any fallback or custom figure.
6. Before formal code or analysis run, complete Formal Analysis Route Confirmation and write
   `scratch/analysis_route_confirmed.json` for this exact route.

## Role Boundaries

- This is fallback only. Use it only after native/wrapper functions are checked, rejected with reasons, and the user confirms the custom route.
- For figures, the Analysis-Native Visualization Gate must be completed first.
- For formal analysis, the Formal Analysis Route Confirmation file is required.

## Murphy Checks

- Does this route bypass OmicVerse/SCOP or official third-party docs?
- Does it turn a generic plotting/statistics helper into a core evidence step?
- Does it depend on an object, layer, batch column, sample column, species, or backend
  that has not been confirmed?
- Does it make model-inferred or database-derived output sound directly observed?

## Risk Note

Custom matplotlib/seaborn must not replace core evidence plots without the visualization gate.
