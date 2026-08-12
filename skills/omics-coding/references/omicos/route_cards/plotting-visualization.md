# OmicVerse visualization for bulk, color systems, and single-cell data

- Source raw material: `../raw_skills/plotting-visualization/SOURCE.md`
- Domain: `omicverse_visualization`
- Route role: `candidate_reminder`
- Object route: `analysis_result_or_anndata`
- Primary authority: OmicVerse/SCOP plotting function docs
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

- This only expands search terms or reminds the agent of a method family.
- It cannot choose a method, function, parameter, backend, or figure family without authority docs.

## Murphy Checks

- Does this route bypass OmicVerse/SCOP or official third-party docs?
- Does it turn a generic plotting/statistics helper into a core evidence step?
- Does it depend on an object, layer, batch column, sample column, species, or backend
  that has not been confirmed?
- Does it make model-inferred or database-derived output sound directly observed?

## Risk Note

Treat as a reminder to find native plotting docs, not as a standalone plotting authority.
