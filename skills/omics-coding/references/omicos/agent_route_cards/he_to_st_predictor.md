# H&E → ST Predictor

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/he_to_st_predictor.json`
- Category: `spatial_analysis`
- Tier: `pro`
- Agent role: `spatial_analysis`
- Route role: `candidate_reminder`
- Primary authority: OmicVerse/SCOP function docs plus official package/tutorial docs
- Official confirmation: `always`

OmicOS agent is not an authority layer. Use this card only as an internal
routing and handoff reminder after OmicVerse/SCOP and official docs have been
checked.

## Use When

Use only as a candidate-search reminder for H&E-to-spatial-transcriptomics questions. Candidate search terms or possible method families include STPath, HEST-FM, STFlow, and iStar, but model choice requires OmicVerse/SCOP and official documentation confirmation before any route is selected.

## NOT-FOR

Not for treating predicted spatial expression as measured ST or replacing real spatial transcriptomics QC.

## Handoff

Hand off predicted matrices to spatial_omics_orchestrator only with prediction provenance clearly marked.

## Source Skills And Toolsets

- Skills: spatial-he-to-st-prediction, spatial-data-io-loading, spatial-publication-plots, spatial-variable-genes, gene-id-conversion, report-html-generation, notebook-export, office-tools
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory

## Role Boundaries

- This agent card only expands routing options or prompts a specialist handoff.
- It cannot select functions, parameters, models, or plots without OmicVerse/SCOP and official source review.

## Murphy Checks

- Could this agent bypass OmicVerse/SCOP or official package docs?
- Could this agent turn a planning suggestion into executed analysis without
  Formal Analysis Route Confirmation?
- Could this agent hide missing object schema, species, genome build, sample
  design, layer, modality, batch, or version checks?
- Could this agent make model-inferred, database-derived, or review-only output
  sound directly observed?

## Risk Note

H&E-derived expression is model output, not measured transcriptomics; report model, training domain, and uncertainty.
