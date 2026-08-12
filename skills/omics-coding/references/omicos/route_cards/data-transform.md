# Data Transformation (Universal)

- Source raw material: `../raw_skills/data-transform/SOURCE.md`
- Domain: `data_wrangling`
- Route role: `glue_helper`
- Object route: `generic_table`
- Primary authority: project data contract
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

- This is glue only. It may handle metadata, tables, export, or object plumbing around verified methods.
- It must not replace core analysis, core visualization, statistical testing, normalization, filtering, scaling, or biological interpretation.
- If it changes an expression/count/intensity matrix or evidence figure, return to Formal Analysis Route Confirmation.

## Murphy Checks

- Does this route bypass OmicVerse/SCOP or official third-party docs?
- Does it turn a generic plotting/statistics helper into a core evidence step?
- Does it depend on an object, layer, batch column, sample column, species, or backend
  that has not been confirmed?
- Does it make model-inferred or database-derived output sound directly observed?

## Risk Note

Use only for metadata or table reshape. Expression normalization, filtering, scaling, log transform, CPM, or other matrix-changing transforms require OmicVerse/SCOP or a confirmed official route.
