# BulkTrajBlend trajectory interpolation

- Source raw material: `../raw_skills/bulk-trajblend-interpolation/SOURCE.md`
- Domain: `bulk_trajectory_interpolation`
- Route role: `candidate_reminder`
- Object route: `bulk_and_single_cell_developmental_series`
- Primary authority: OmicVerse function docs and method paper or official docs
- Official confirmation: `always`

## How To Use

1. Clarify the user question, input object, species, grouping columns, and outputs.
2. Search `references/function_index.tsv` and `references/parameter_index.tsv` first.
3. Open the shortlisted OmicVerse/SCOP docs and verify exact function and parameters.
4. Use this OmicOS card only as a workflow reminder.
5. Complete the Analysis-Native Visualization Gate before any fallback or custom figure.
6. Before formal code or analysis run, complete Formal Analysis Route Confirmation and write
   `scratch/analysis_route_confirmed.json` for this exact route.

## Role Boundaries

- This only expands search terms or reminds the agent of a method family.
- It cannot choose a method, function, parameter, backend, or figure family without authority docs.

## Murphy Checks

- Does this route bypass OmicVerse/SCOP or official third-party docs?
- Does it turn a generic plotting/statistics helper into a core evidence step?
- Does it depend on an object, layer, batch column, sample column, species, or backend
  that has not been confirmed?
- Does it make model-inferred or database-derived output sound directly observed?

## Risk Note

Generated intermediate states are model outputs, not directly observed cells.
