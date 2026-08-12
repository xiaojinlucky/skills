# Single Cell Differential Expression

- Source raw material: `../raw_skills/single-cell-differential-expression/SOURCE.md`
- Domain: `single_cell_differential_expression`
- Route role: `route_card`
- Object route: `annotated_anndata_with_groups`
- Primary authority: OmicVerse/SCOP function docs and selected method official docs
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

- Use this as route ordering help only after OmicVerse/SCOP and official docs are checked.
- It cannot override version checks, function docs, parameter docs, visualization gates, or route confirmation.

## Murphy Checks

- Does this route bypass OmicVerse/SCOP or official third-party docs?
- Does it turn a generic plotting/statistics helper into a core evidence step?
- Does it depend on an object, layer, batch column, sample column, species, or backend
  that has not been confirmed?
- Does it make model-inferred or database-derived output sound directly observed?

## Risk Note

Confirm contrast, cell type scope, covariates, and replicate strategy.
