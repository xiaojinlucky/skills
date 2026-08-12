# OmicOS Integration Policy

OmicOS is an internal reference layer for `omics-coding`, not an authority layer.
The authority order is:

1. User-confirmed biological question, object format, grouping, and expected outputs.
2. OmicVerse/SCOP local function and parameter docs.
3. Official tutorial, official notebook, vignette, or official API docs for
   OmicVerse/SCOP workflows and any third-party backend.
4. OmicOS skill route cards as workflow reminders.
5. OmicOS `agent_index.tsv` and `agent_route_cards/*.md` as routing and
   handoff reminders.
6. Generic fallback utilities only after native or wrapper options are rejected.

Use OmicOS route cards as workflow reminders only; this applies to both skill
route cards and agent route cards.

## Hard Gates

- OmicOS may suggest a workflow branch, but it must not override OmicVerse/SCOP
  function docs, parameter docs, package versions, or official tutorial choices.
- OmicOS agent cards may suggest a specialist, handoff, or review gate, but they
  must not become an execution authority or method source.
- Before formal analysis code or any real analysis run, the route must be
  confirmed by the user and recorded in `scratch/analysis_route_confirmed.json`.
- That confirmation file must record `analysis_stage`, `dataset_id`,
  `input_files`, `input_fingerprints`, `output_files`, `official_sources`,
  `doc_paths`, `source_urls`, `planned_functions`, `key_parameters`,
  `package_versions`, `visualization_gate`, `omicos_route_role`,
  `confirmed_by_user`, `user_confirmation`, `confirmed_at`, `project_root`,
  `allowed_commands`, and `allowed_files` for the exact current route.
- `allowed_commands` and `allowed_files` are both required. They must be exact
  commands and exact files. Do not use glob patterns, parent directories, broad
  project roots, or catch-all shell fragments as authorization.
- A route pass is narrow. It does not authorize a different dataset, method,
  package, visualization family, analysis stage, input file, output file,
  parameter set, function, command, or route role.

## Role Meanings

| route_role | meaning |
|---|---|
| route_card | Can be used as a compact workflow reminder after authority docs are checked. |
| candidate_reminder | Can remind the agent to search a method family, but never selects the method alone. |
| glue_helper | Can help with file I/O, reshaping, export, or small object handling. |
| fallback_only | Can only be used after analysis-native or wrapper options are checked and rejected. |
| excluded_from_core | Preserved for audit, not used for formal omics route planning. |

## Agent Layer Meanings

`agent_index.tsv` and `agent_route_cards/*.md` are strict-omics routing aids.
They include only data acquisition, strategy planning, single-cell analysis,
spatial omics, general omics analysis, phylogenomics, and review-gate agents.
Writing, viewer, structural biology, molecular-biology utility, generic memory,
and broad selector agents are excluded from the omics-coding route layer.

Agent route roles:

| agent route_role | meaning |
|---|---|
| route_card | Can suggest the matching specialist route after OmicVerse/SCOP docs are checked. |
| candidate_reminder | Can remind the agent to consider a branch, but cannot select methods alone. |
| review_only | Can challenge completed work; cannot start, approve, or execute analysis. |

## Confirmation Meanings

| requires_official_confirmation | meaning |
|---|---|
| always | Any formal use must go through official source review, user confirmation, and `analysis_route_confirmed.json`. |
| conditional | Confirmation is required when the step affects an analysis result, evidence figure, statistic, biological conclusion, or object matrix. |
| not_core_analysis | Only pure export, pure layout, or smoke-test use; if it touches formal analysis outputs, treat as `conditional`. |

## Murphy Acceptance Questions

Before using any OmicOS-derived card, ask:

1. Could this bypass an official tutorial or function doc?
2. Could this replace a native OmicVerse/SCOP plot with a custom fallback plot?
3. Could this treat pooled cells as biological replicates?
4. Could this hide version or backend differences?
5. Could this make generated/model-inferred output look directly observed?

If any answer is yes, stop and return to the relevant `omics-coding` gate.
