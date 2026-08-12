---
name: omics-coding
description: Use this skill when planning, writing, reviewing, or fixing code for single-cell analysis, spatial transcriptomics, spatial multi-omics, or omics workflows where OmicVerse, SCOP, or analysis-native package functions may cover methods or visualizations. Trigger before choosing methods, writing AnnData/Seurat pipelines, selecting analysis-native or CNS-common visualization routes, plotting result objects, or using ggplot2/matplotlib/seaborn for custom omics figures. For omics-related scientific figures, choose analysis-native or CNS-common figure forms first; all visible figure text must be English; do not add subtitles, caption-like text, or explanatory conclusion text inside the image; and write confirmed routes as direct analysis code instead of redundant defensive scaffolding.
---

# Omics Coding

## Purpose

Use this skill to prevent AI-written omics code from inventing methods when OmicVerse or SCOP already covers the task. The normal route is: clarify the analysis goal, check both packages, read the local index, open the matching function docs, then write simple code.

## Core Rule

Unless the user explicitly specifies one package or language, check both OmicVerse and SCOP before choosing a route.

- Use OmicVerse for Python and AnnData routes when it has the better function for the task.
- Use SCOP for R and Seurat routes when it has the better function for the task.
- If both can do the task, compare fit by data object, function maturity, documentation clarity, required inputs, output format, and whether the project already uses Python or R.
- If neither package covers the core method, say which step is not covered before using another package.
- Do not reimplement core single-cell, spatial, multi-omics, integration, annotation, communication, trajectory, enrichment, or visualization algorithms when a suitable OmicVerse or SCOP function exists.
- For visualization, prefer analysis-native plotting over custom plotting. Analysis-native means the function belongs to the package that produced the result, that package's mature companion visualization package, or an OmicVerse/SCOP wrapper that consumes or faithfully represents the result object or result table.
- For publication-oriented figures, first choose a CNS-style common figure form that matches the question, then tune the analysis-native plotting parameters. The saved figure must follow the digital-master visual rule: readable large fonts, sufficient inch-based canvas, balanced legend, pure-vector UMAP / dense scatter points with tiny visible point size, and final PDF/SVG review. Rasterized dense points are only a separate performance-compromise export when the user explicitly asks for it. Do not choose decorative or AI-overannotated plots just because they look rich.
- Ordinary glue code is allowed: reading confirmed paths, arranging result tables, saving outputs, and small plotting adjustments. Check columns only at a real external-input boundary or when the choice changes result meaning; do not add a generic validation layer around a fixed route.

## Confirmed-route directness

Once the user, project artifacts, and official docs have fixed the input object, metadata columns, keys, package route, and outputs, write the main path directly. Treat the confirmed route as a contract; do not re-prove it inside the analysis script.

- Avoid validation scaffolding that only restates the contract: `required_*`, `missing_*`, `overlap_*`, `valid_*`, or `checked_*` variables; `if (...) stop(...)`; `assert*`; broad `tryCatch`/`try/except`; fallback, automatic repair, skip, or early return.
- For a fixed input, call `qread`, `merge`, SCOP, OmicVerse, Seurat, Scanpy, or other selected functions directly. If the contract is actually broken, let the base or package call expose the original error chain.
- Use `table`, `head`, `print`, and object summaries as inspect points, not runtime gates. If something is not confirmed, inspect it before writing the route; do not replace the decision with a guard.
- Keep branches that change result semantics: biological filtering, label mapping, genuinely different input shapes, trust-boundary checks, data-loss protection, and user-requested tolerant batch processing. The rule is not “remove every `if`”; it is “make every branch carry real result responsibility.”
- If the project names an existing script and output structure, extend that script at the relevant location. Do not create a parallel one-off script for route confirmation or validation. `analysis_route_confirmed.json` is planning/audit evidence, not runtime input or a reason to add another executable layer.

For example, after the input objects and replacement columns are confirmed, write the object transformation directly:

```r
pancreas_sub <- subset(pancreas, !level1 %in% c("Ductal", "Acinar"))
pancreas_sub$celltype <- as.character(pancreas_sub$level1)
epi_sub$celltype <- as.character(epi_sub$level2_round2)
pancreas_new <- merge(pancreas_sub, epi_sub)
```

Do not wrap this route in repeated required-column, duplicate-cell, object-identity, or `stop()` checks when those premises belong to the confirmed input contract.

## OmicOS Internal Reference Layer

OmicOS is not an authority layer. It is an internal workflow-reference layer derived from the OmicOS skills and strict omics agents under `references/omicos/`. Use it to remember likely route branches, specialist handoffs, input object expectations, and Murphy-style risk checks, not to select functions from memory.

Authority order:

1. User-confirmed biological question, input object, grouping, species, and expected outputs.
2. OmicVerse/SCOP local function and parameter docs.
3. Official tutorial, official notebook, vignette, or official API docs for OmicVerse/SCOP workflows and any third-party backend.
4. OmicOS skill index, strict omics agent index, and route cards as workflow reminders.
5. Generic fallback helpers only after native or wrapper options are checked and rejected.

Search OmicOS only after the first OmicVerse/SCOP candidate pass:

- `references/omicos/skill_index.tsv`: one row per OmicOS skill with route role, domain, object route, authority source, and risk note.
- `references/omicos/agent_index.tsv`: one row per strict omics OmicOS agent with route role, NOT-FOR scope, handoff target, authority source, and risk note.
- `references/omicos/integration_policy.md`: authority order and Murphy acceptance checks.
- `references/omicos/route_cards/*.md`: compact route reminders. Open only the 1-3 cards matching the current task.
- `references/omicos/agent_route_cards/*.md`: compact agent handoff reminders. Open only the 1-2 cards that clarify routing or review responsibility.
- `references/omicos/raw_skills/*/SOURCE.md`: preserved source material. Open raw files only when the compact route card is insufficient.
- `references/omicos/raw_agents/`: selected OmicOS public agent JSON plus runtime roster for audit. Open raw files only when the compact agent card is insufficient.

Role rules:

- `route_card`: may guide workflow ordering after function docs are checked.
- `candidate_reminder`: may expand search terms or remind the agent to inspect a method family.
- `glue_helper`: only for I/O, reshaping, export, or small object handling around verified analysis functions.
- `fallback_only`: only after analysis-native or wrapper functions are checked and rejected.
- `excluded_from_core`: preserved for audit, not used for formal route planning.
- Agent `route_card`: may suggest a matching specialist route after function docs are checked.
- Agent `candidate_reminder`: may expand possible route branches but cannot select methods alone.
- Agent `review_only`: may challenge completed work but cannot start, approve, or execute analysis.

Before using any OmicOS-derived note, ask the Murphy question: "If this route fails, how would it fail silently?" Stop if the answer is: bypassing official docs, replacing native plots with custom plots, ignoring sample-level design, hiding version differences, or treating model/database output as directly observed evidence.

## Formal Analysis Route Confirmation

For a new formal analysis route, confirm the official route with the user before writing or running real analysis. After that confirmation, record `scratch/analysis_route_confirmed.json` in the current project root with:

- `analysis_stage`
- `dataset_id`
- `input_files`
- `input_fingerprints`
- `output_files`
- `official_sources`
- `doc_paths`
- `source_urls`
- `planned_functions`
- `key_parameters`
- `package_versions`
- `visualization_gate`
- `omicos_route_role`
- `confirmed_by_user`
- `user_confirmation`
- `confirmed_at`
- `project_root`
- `allowed_commands`
- `allowed_files`

Both `allowed_commands` and `allowed_files` are required. They must be exact commands and exact files. Do not use glob patterns, parent directories, broad project roots, or catch-all shell fragments as authorization.

This pass is narrow. It authorizes only the specific route, dataset, analysis stage, package, functions, parameters, visualization family, route role, input files, output files, and commands recorded in that JSON file. It does not authorize a different analysis stage, visualization family, package backend, dataset, input file, output file, function, parameter set, command, or route role.

If the route is already confirmed and the user names an existing script for a direct append, do not create a new route-confirmation file merely to gate that append. Reuse the existing project record when one exists; never read the record as runtime input or turn it into a second executable validation layer.

## Function Discovery Rule

Function discovery must balance high recall with low token use. Do broad search locally, then show the model only a small candidate set.

- Do not rely on the user's exact words or one `grep` command.
- Generate search terms from the task text, English method names, common package or algorithm names, likely parameter names, and expected plot/output types.
- Search `function_index.tsv` and `parameter_index.tsv` first because they are cheap to scan.
- If the first pass returns too few matches, only unrelated matches, or a method-sensitive decision, search function Markdown files by filename and matching lines before opening full docs.
- Open full function docs only for the shortlisted candidates, normally 3-8 functions.
- Treat indexes as recall tools, not proof. Final selection requires reading the function doc and checking the function or parameter in the local runtime when runnable code depends on it.
- If no OmicVerse or SCOP candidate survives this process, state the uncovered step before considering third-party packages.

Use this shortlist shape when reporting function discovery:

| function | package | matched terms | doc path | likely use | reject reason |
|---|---|---|---|---|---|

Leave `reject reason` empty for candidates still under consideration. Do not paste long documentation excerpts into the answer.

## Multi-Step Goal Function Plan (hard gate)

When the goal has more than one analysis step (e.g. QC -> normalization -> integration -> clustering -> annotation -> differential -> enrichment -> communication -> trajectory -> figures), do not search functions for only the first step and then write the rest from memory. Function-search adherence must not decay across steps.

- First decompose the goal into ordered analysis steps.
- Run the Function Discovery Rule for EVERY step, including the figure step.
- Present ONE combined per-step plan table BEFORE writing analysis code, and let the user confirm it.

| step | task | candidate OmicVerse/SCOP function(s) | local availability | chosen | note |
|---|---|---|---|---|---|

- `local availability` comes from `function_index.tsv` / doc lookup or a runtime check, never from memory.
- Every step gets its own row. A step with no OmicVerse/SCOP candidate must say so on its row, then go through the Third-Party Package Fallback Gate.
- Do not start coding any step while later steps still have empty candidate cells.

Rationalizations that are NOT allowed:
- "I'll look up the later steps when I reach them" — later steps are exactly where the search silently stops; plan all steps up front.
- "This step is obvious / standard" — still check the index once and write the verified function name.
- "Same as a previous project" — re-verify against the local index for this run; best-fit functions and versions change.

## Analysis-Native Visualization Gate

Any task that creates a figure, figure set, PPT, or HTML report for omics results must check analysis-native visualization before writing custom plotting code.

Analysis-native visualization is decided by result provenance and object format, not by whether a function name contains the method name. Many workflows reuse the same plotting family with different objects and parameters. For example, cell-cell communication results from CellChat, LIANA/LIANA-py, NicheNet, MultiNicheNet, or cell2cell may all be shown through network, bubble, heatmap, dot, circle, or river-style plotting families. The correct question is:

`Which result object/table is this, which plotting family is designed for it, and which mode/parameter makes the plot represent this analysis?`

Use this priority order:

1. Plotting functions from the package that produced the result object or result table.
2. Official or mature companion visualization functions for that package.
3. OmicVerse or SCOP wrappers that directly consume, convert, or faithfully represent that result.
4. Basic plotting packages such as ggplot2, matplotlib, seaborn, pheatmap, ComplexHeatmap, or plotly only after the previous options fail or the user explicitly asks for a custom summary figure.

Before custom plotting for a core evidence figure, fill this table:

| figure question | analysis source | result object/table | visualization family | native/wrapper function checked | key mode/parameter | decision | reject reason |
|---|---|---|---|---|---|---|---|

`decision` must be `use_analysis_native`, `split_analysis_native`, or `custom_after_reject`. Leave `reject reason` empty when using or splitting analysis-native plots.

## CNS-Style Figure Route Gate

Before writing plotting code, choose a figure form that is common in CNS-level omics papers and matches the evidence being shown. This gate decides the route; `bio-code-style` handles the final plotting code style.

Use this route map:

| figure question | preferred common form |
|---|---|
| Where are cells or expression located? | UMAP/tSNE/spatial feature plot with shared scale when comparing panels |
| Which markers define clusters or cell types? | Dotplot, heatmap, violin, or compact marker panel |
| How does abundance change by condition or stage? | Sample-level proportion plot, box/violin with sample points, stacked composition only when composition is the message |
| Which genes or pathways are enriched? | Dotplot, barplot, ridge only when it improves term readability, enrichment map only for pathway relationships |
| How does a score/loading/activity vary? | Box/violin/line trend with sample-level points or heatmap when matrix structure matters |
| What is the ligand-receptor or communication pattern? | Native bubble/network/heatmap/circle plot selected by sender-receiver question |
| What is the trajectory or pseudotime pattern? | Native trajectory embedding, gene trend line, branch heatmap, or lineage-aware dot/heatmap |
| What is a matrix/module/factor pattern? | Heatmap with traceable row/column order and stable annotations |

Route rules:

- **Non-negotiable user rule: every visible text element inside every figure must be English.** This includes titles, axis titles, tick labels, legend titles and labels, annotations, facet strips, panel-specific text, statistical labels, colorbar labels, pathway or functional-term labels, and labels automatically generated by native plotting functions. R/Python code comments and surrounding Chinese reports may remain Chinese, but exported images may not contain Chinese figure text.
- Default visual style is single-figure report mode: one very short object/metric title is allowed. The title should be like `Macrophage fraction`, `CXCL12 expression`, or `Module score`; do not include comparison phrases or conclusions.
- For formal paper panel output, omit the main title unless the user asks for it; use panel labels outside or at the panel corner.
- **Non-negotiable user rule**: never include a subtitle in any omics figure. Do not use `subtitle`, and do not repurpose a subtitle for method, sample size, comparison, or conclusion text. If a native function supplies one by default, explicitly clear it or choose an equally native mode without it. A title is optional; if retained, it must be only a short object/metric label.
- Never plan caption-style text inside the image. Biological interpretation belongs in the report text, figure legend, or narration.
- Layout must follow reading order: left or top introduces the object/metric, center shows main data, right or bottom provides compact supporting legend/statistics only when needed.
- Color must encode meaning: stable discrete colors for cell types and groups, ordered palettes for disease stage, single or diverging gradients for expression/module scores, minimal accent colors for key stages or cell groups.
- Group order is part of the analysis route. Stages follow biological progression; cell types follow biological classes; genes follow gene set, pathway, factor loading, differential strength, or a declared ordering rule.
- For multi-panel comparisons, require aligned panel size, shared scales when comparing expression/intensity, consistent font sizes, stable legends, and fixed export dimensions.
- For code-generated publication plots, never translate "Nature format" into 89 mm / 183 mm code canvases or 6-7 pt fonts. Use `bio-code-style` digital-master defaults first, then let Illustrator/PPT scale the finished PDF/SVG.
- For single-cell statistical evidence, prefer sample-level proportions/scores/means for key claims. Do not treat pooled cells as biological replicates.
- Default statistics are minimal `P = ...` or `FDR = ...` labels for key comparisons only. Use star labels only when the user explicitly asks.

If a package-native plot cannot meet this standard after tuning size, palette, labels, legend, scale, and panel splitting, state the limitation and ask whether to use a custom plot or a different CNS-style figure form.

### Wrapped Function Rule

SCOP and OmicVerse often wrap several methods through shared visualization functions. Do not reject a wrapper because the function name is generic. Open the function documentation and check:

- accepted input object or table format
- conversion helpers such as `*_to_adata`, `*_to_liana`, or communication AnnData builders
- mode/type arguments that switch between network, heatmap, bubble, dot, circle, pathway, source-target, ligand-receptor, or group views
- grouping, pathway, ligand, receptor, sender, receiver, cell type, condition, and layout parameters
- whether the wrapper preserves the result semantics or only draws a generic summary

If a wrapper preserves the result semantics, it counts as analysis-native for this workflow. If it discards the method-specific meaning, mark it as rejected and say which meaning is lost.

### Wrapper Doc-Read Requirement (hard gate)

OmicVerse/SCOP visualization is often one function whose `mode`/`type` parameter switches between network, bubble, heatmap, circle, chord, dot, and group views, with many sender/receiver/signaling/layout parameters. Wrapper parameter names differ from the original method (e.g. CellChat `sources.use` is not the OmicVerse wrapper's parameter name).

Before writing plotting code for any wrapper or analysis-native plotting function, you MUST open its local doc (`references/omicverse/functions/*.md` or `references/scop/functions/*.md`) and fill this from the doc, not from memory:

| plotting function | doc path | mode/type values (from doc) | key parameter names (exact, from doc) | chosen mode + params |
|---|---|---|---|---|

- The mode/type values and parameter names must be quoted from the doc you just opened, not recalled from a similar function.
- If you cannot list the function's mode/type options and its exact parameter names from its doc, you have not read it — open it before writing any plotting code.
- Pick the mode/parameters that make the plot answer THIS figure question (e.g. a directional sender->receiver question favors a chord/network mode over a flat bubble).
- Do not assume a parameter exists because another package's plotting function has it; verify the exact name in this function's doc, and in the local runtime when the code must run.

### Custom Plot CHECKPOINT

🔴 CHECKPOINT / STOP: For core evidence figures, do not write ggplot2/matplotlib/seaborn custom plotting code until the gate table is shown and the user confirms the custom route.

Custom plotting is allowed without this checkpoint only for:

- small glue figures that are not the main evidence, such as sample counts, QC summaries, file manifests, or pipeline overview schematics
- final layout panels that arrange already-generated analysis-native figures without redrawing their data
- minimal label, crop, legend, or layout adjustments that do not replace the package-owned visual encoding

When custom plotting is allowed, state:

`Custom plot allowed because: <analysis-native functions checked>; <why they cannot answer this figure question>; role=<main evidence|summary bridge|layout only>.`

## Third-Party Package Fallback Gate

Use another analysis package only after OmicVerse and SCOP have both been checked and the uncovered step is named plainly. This is a hard gate for packages such as LIANA, cell2cell, CellChat, NicheNet, decoupler, CellRank, scVelo, Seurat extensions, Scanpy extensions, or any other non-OmicVerse/non-SCOP route.

Before writing formal code or running analysis with a third-party package:

1. Search OmicVerse and SCOP local indexes first and state the missing or weaker step.
2. Find the third-party package's official tutorial, vignette, notebook, or official documentation for the exact route.
3. Open the official function documentation and parameter documentation for the candidate analysis and visualization functions.
4. If the package has many moving parts or will be reused, save the relevant function/parameter notes locally in the project or task context instead of relying on memory.
5. Present the user with the official tutorial URL, official workflow order, candidate functions, key parameters, expected outputs, native visualization options, and why OmicVerse/SCOP are not enough.
6. Wait for the user to confirm that the official tutorial and route are correct. Do not write formal analysis code, run the analysis, or design a substitute plotting/storytelling route before confirmation.

If no official tutorial covers the task, say that directly and ask whether to proceed from official API docs, source code, papers, or a custom route. Community blogs, old notebooks, and memory are not enough unless the user explicitly accepts them.

## Runtime Environments And Documentation Lifecycle

Treat a method's runtime as part of the formal analysis route, not as an afterthought. Before route confirmation, inventory the exact Python/R runtime, package, version, and non-package dependency needed by every selected backend. Follow `references/environment-lifecycle.md` for the decision record and verification commands.

1. If a selected package is outdated, unloadable, or its local runtime differs from the docs that will guide code, first make the smallest relevant package/dependency repair. Then verify the package imports or loads and the exact planned functions and parameters exist at runtime.
2. Refresh the function, parameter, and index docs after an update when a changed version can affect runnable code. For OmicVerse/SCOP use `scripts/update_docs.py`; for a reusable third-party backend, save official route/function/parameter notes and register them in the third-party indexes before formal code.
3. Dry-run dependency resolution before changing a shared analysis environment. Do not install a backend that upgrades core dependencies (for example Python, AnnData, TensorFlow, JAX, R, Seurat, or Rcpp) into an existing working OmicVerse/SCOP environment unless that change is itself the confirmed route. A package found in another R library or Python environment is not proof that it is available in the selected formal runtime.
4. If the backend is valuable and its dependency boundary conflicts with a shared environment, create or reuse a named isolated environment. Record its path, versions, verification command, data hand-off format, and intended scope in `references/runtime_index.tsv`.
5. Apply the cost rule: do not provision a large environment merely to repeat evidence already covered by a lower-cost valid route. Do provision an isolated environment when it provides an independent method needed for the current claim or a durable method the user intends to reuse.
6. After a third-party environment passes its smoke test, update `references/third_party_function_index.tsv`, `references/third_party_parameter_index.tsv`, and its local note under `references/third_party/`. Do not record an environment as usable before import/load and function-signature checks pass.
7. When a third-party convenience wrapper breaks after a host-object upgrade, first look for the package's lower-level documented input constructor or data hand-off. Use that bridge only after a full official-example smoke test passes in the intended runtime; do not downgrade a shared core dependency merely to preserve the convenience wrapper. Record the bridge and its re-verification command in the third-party note and runtime index.

Before reusing a registered third-party backend, read its matching note under `references/third_party/`. The note is a route reminder, not a substitute for checking its current official tutorial and local function signature.

Use the user's fixed local environments before running package checks or analysis code:

- OmicVerse runs in conda env `omicverse`.
- SCOP runs in conda env `seurat_v5`.

最后验证的运行时基线（2026-08-03）是：OmicVerse 2.3.1 / Python 3.10.14 / `anndata` 0.11.4 / `zarr` 2.18.3，SCOP 0.9.0 / R 4.4.3 / Seurat 5.4.0 / SeuratObject 5.3.0。这个基线会变化，正式使用前仍要运行 `scripts/check_versions.py`。

Verify with direct environment commands instead of guessing:

```bash
conda run -n omicverse python -c "import omicverse as ov; print(getattr(ov, '__version__', 'unknown'))"
conda run -n seurat_v5 Rscript -e 'cat(as.character(utils::packageVersion("scop")), "\n")'
```

When writing runnable code, keep the package route and runtime aligned: Python/AnnData OmicVerse code should run under `omicverse`; R/Seurat SCOP code should run under `seurat_v5`.

## Official OmicVerse Skill Bridge

When the confirmed route is Python/AnnData, inspect the installed official `omicverse-skills` catalog before writing a new workflow:

```bash
conda run -n omicverse python -c "from omicverse_skills import list_skills; print(len(list_skills())); print([s['slug'] for s in list_skills() if 'single-cell' in s['slug']][:20])"
conda run -n omicverse python -c "from omicverse_skills import load_skill_text; print(load_skill_text('single-cell-preprocessing'))"
```

Use it to borrow stage boundaries, input/output contracts, official sources, and small acceptance smoke tests. Do not copy the whole catalog into this skill, and do not copy teaching-only `try/except`, repeated field checks, or automatic degradation into fixed-route analysis code. The local package, official function docs, project artifacts, and user-confirmed route remain the authority.

The separate `omicclaw` project is useful as an optional architecture reference for gateway, session, workspace, and provenance design. It is not a required Codex/Positron runtime dependency. The Python catalog cannot select an R/SCOP route.

The official OmicOS / OmicOS-Bio workflow adds a useful execution skeleton: `ingest -> plan -> execute -> verify -> deliver`. Borrow its read-only data inventory, explicit biological decision points, checkpoint read-back, sample/donor-level statistics, and evidence-chain delivery. Do not make its cloud account, subscription tier, remote gateway, or automatic recovery behavior a required dependency for Codex/Positron, and do not let an agent choose the biological comparability or batch field by itself.

For the adopted tool set and the developer/user/evaluator evidence model, read `references/tooling-and-evidence.md`.

## Version And Description Match Rule

Before using the generated latest-docs index for runnable code, check whether local packages match the current upstream package metadata. For OmicVerse this means the PyPI version. For SCOP this means both `Version` and `Date` from the upstream GitHub `DESCRIPTION`, because SCOP may update source and docs while keeping the same package version.

```bash
python3 scripts/check_versions.py
```

If the local package version or SCOP `DESCRIPTION Date` differs from the upstream value, warn the user before writing code that depends on the latest docs. Use plain wording like:

`本机 OmicVerse/SCOP 版本或 SCOP DESCRIPTION 日期低于最新文档来源，最新文档里的部分函数或参数可能不能运行。建议先更新环境，或按本机版本改写代码。`

Do not silently write code from latest docs when the local package is older. If the user wants to continue without updating, verify the exact function and parameter in the local environment before using it.

Also check dependency boundaries before upgrading a single dependency. For example, if the local OmicVerse environment pins `anndata<0.12`, do not independently install a newer AnnData just because the wider scverse ecosystem has moved on. Seurat v5 multi-layer assays likewise require an object/layer decision before code; a later `if/stop` block is not a substitute for that decision.

For the currently verified SCOP 0.9.0 route, use `RunStandardWorkflow()`, `RunIntegration()`, `RunscDblFinder()`, `Runscds()`, `RunScrublet()`, and `RunDoubletDetection()` in new code. The older `standard_scop()`, `integration_scop()`, and `db_*` names are compatibility entry points and may warn before their planned removal; spatial routes must also check the current `image` and coordinate-space contract in the local function doc. See `references/tooling-and-evidence.md` for the compact change note.

## Workflow

1. Read local project rules first: `AGENTS.md` or `CLAUDE.md`, then `CONTEXT.md` if present.
2. Clarify the biological question, input object, species, grouping columns, and expected outputs. Ask one question if these are unclear.
3. Build a task-specific search-term set before searching. Include user terms, English method terms, common algorithm/package names, likely parameter names, and expected output or plot terms.
4. Search the local indexes for both analysis and visualization functions:
   - `references/function_index.tsv` for function names, summaries, package, source URL, and local doc path.
   - `references/parameter_index.tsv` for parameter names and the local function doc path.
5. If index matches are weak or incomplete, search function Markdown filenames and matching lines before opening full docs.
6. Make a short candidate table and remove obvious mismatches by input object, required metadata, output type, and package route.
7. Open only the docs that match the current task:
   - `references/omicverse/functions/*.md`
   - `references/scop/functions/*.md`
8. Compare OmicVerse and SCOP options before coding unless the user has already fixed the route.
9. Run `python3 scripts/check_versions.py` before formal route confirmation or code. If local and latest versions differ, or SCOP `DESCRIPTION Date` differs, warn the user and do not assume latest-docs APIs exist locally.
10. For a Python route, inspect `omicverse-skills` and use its stage/source/acceptance notes selectively; do not treat its catalog as a second authority layer.
11. Search `references/omicos/skill_index.tsv` for matching route reminders only after the OmicVerse/SCOP pass. Open at most 1-3 matching route cards unless the user explicitly asks for broader review.
12. If routing or review responsibility is still unclear, search `references/omicos/agent_index.tsv` and open at most 1-2 matching `references/omicos/agent_route_cards/*.md`.
13. Treat OmicOS skill and agent route cards as workflow reminders. They cannot override function docs, official tutorials, runtime version checks, route confirmation, or the visualization gate.
14. If OmicVerse/SCOP are not enough, run the Third-Party Package Fallback Gate above and wait for user confirmation before coding or execution.
15. For any figure output, run the Analysis-Native Visualization Gate before writing plotting code. Keep core evidence figures on analysis-native visualization unless the gate justifies a custom plot and the user confirms it.
16. For publication-oriented plots, run the CNS-Style Figure Route Gate before deciding the plot family, panel order, color semantics, grouping order, and statistics route.
17. For a new formal route, present the official sources, planned functions, key parameters, and OmicOS skill/agent route-card notes to the user, then record the confirmation with the fields in Formal Analysis Route Confirmation. If the route is already confirmed and the user names an existing script, continue in that script without creating a duplicate confirmation file.
18. Write direct analysis code with explicit inputs and outputs. Keep core analysis on selected package functions.
19. Before claiming code is ready, verify package availability in the correct environment or document the exact missing package/version.

## How To Search

Use shell search against the generated index instead of guessing from memory:

```bash
grep -i "trajectory" references/function_index.tsv
grep -i "groupby" references/parameter_index.tsv
grep -i "cellchat" references/function_index.tsv references/parameter_index.tsv
grep -Ei "communication|cellchat|liana|nichenet|ccc|ligand" references/function_index.tsv references/parameter_index.tsv
grep -Ei "plot|heatmap|umap|group.by|palette|legend.position|figsize" references/function_index.tsv references/parameter_index.tsv
grep -Ei "dot|bubble|network|circle|river|sankey|pathway|sender|receiver|source|target|ligand|receptor|width|height|nrow|ncol" references/function_index.tsv references/parameter_index.tsv
grep -Ei "trajectory|communication|integration|annotation|spatial|metabol|microbiome|velocity|scenic|deconvolution|visualization|export" references/omicos/skill_index.tsv
grep -Ei "single_cell|spatial|bulk|metabolomics|microbiome|proteomics|epigenomics|trajectory|communication|review|handoff" references/omicos/agent_index.tsv
```

Use a small method dictionary to expand common tasks. Add terms from the user's exact question when needed; do not dump this full list into the chat response.

| task | required search terms |
|---|---|
| Cell communication | `communication`, `ccc`, `ligand`, `receptor`, `cellchat`, `liana`, `nichenet`, `network`, `circle`, `bubble`, `heatmap` |
| Trajectory or pseudotime | `trajectory`, `pseudotime`, `monocle`, `slingshot`, `palantir`, `velocity`, `paga`, `lineage`, `stream` |
| Batch integration | `integration`, `harmony`, `scanorama`, `scvi`, `liger`, `mnn`, `bbknn`, `batch`, `correct` |
| Cell annotation | `annotation`, `celltype`, `marker`, `singler`, `celltypist`, `scmap`, `label transfer`, `reference` |
| Spatial analysis | `spatial`, `visium`, `xenium`, `neighbor`, `deconvolution`, `STAGATE`, `cellloc`, `spot`, `spatial variable` |
| Enrichment | `enrichment`, `GSEA`, `GSVA`, `pathway`, `ORA`, `gene set`, `aucell`, `metabolism` |
| Differential testing | `differential`, `DE`, `marker`, `wilcoxon`, `DEtest`, `volcano`, `proportion`, `composition` |
| Gene regulatory network | `GRN`, `SCENIC`, `GENIE3`, `GRNBoost2`, `cisTarget`, `regulon`, `transcription factor` |

Escalate search in this order:

1. Search `function_index.tsv` and `parameter_index.tsv`.
2. Search function Markdown filenames and matching lines.
3. Open only the shortlisted function Markdown files.
4. Check local function signatures or package availability in `omicverse` or `seurat_v5`.
5. Run a minimal smoke test only when the function choice or parameter behavior is uncertain and runnable inputs are available.

When a parameter appears in several functions, open the function docs before using it. The same parameter name can mean different things in different functions.

Some OmicVerse pages provide a function signature but no parameter-description section. In that case `parameter_index.tsv` includes the parameter name with the meaning `Detected from function signature; no parameter description detected.` Treat that as a lookup hint only: open the function Markdown, read the signature and full documentation, and verify the exact parameter in the local environment before relying on it in runnable code.

## Updating Docs

The bundled script rebuilds local docs and indexes from the current online documentation:

```bash
python3 scripts/update_docs.py --package all
```

For a fast smoke test:

```bash
python3 scripts/update_docs.py --package all --limit 2
```

If the SCOP pkgdown site is unstable, use the upstream Rd docs from GitHub:

```bash
python3 scripts/update_docs.py --package all --scop-source github
```

The script writes one Markdown file per function and generates parameter-level indexes. Run it about every half month, or before a method-sensitive task where current docs matter.

The `--limit` command is only a smoke test. Do not use its partial output as the canonical local index. If a full refresh cannot reach an upstream source, preserve the existing complete snapshot and report the failed source instead of treating a partial fetch as a successful update.

## Output Discipline

- State the selected package and function names before presenting runnable code.
- Keep explanations short: why this package, why this function, and which local doc path was used.
- If using a non-OmicVerse or non-SCOP method, state the uncovered step first, cite the official tutorial/API docs used, and state that the user confirmed the third-party route.
- If using a custom plot, state the analysis-native functions or wrappers rejected, the reject reason, and whether the custom plot is main evidence, summary bridge, or layout only.
- Do not silently use old APIs when the generated docs show a newer name or parameter.
- Do not turn route confirmation, package-doc review, or Murphy review into runtime validation scaffolding. Once the route is confirmed, keep the implementation direct and let real package errors remain visible.

## Visualization Discipline

When generating any figure, figure set, PPT, or HTML report for omics analysis, choosing a native plotting function is not enough. The function and parameters must fit the actual figure content, and the saved result must be visually reviewed before delivery.

- Start from CNS-common figure forms. Avoid decorative, overly novel, or AI-overannotated plots when a standard UMAP, dotplot, violin/box with sample points, heatmap, enrichment dotplot, trajectory plot, or communication bubble/network answers the question better.
- Pick visualization functions by the question being answered: use feature embedding plots for spatial distribution, statistical plots for group comparisons, heatmaps for matrix patterns, enrichment plots for terms, and native trajectory or interaction plots when those methods own the result.
- For core evidence plots, start from visualization functions that understand the result object or result table. Do not first extract a result table and redraw the same result with ggplot2/matplotlib/seaborn.
- Tune the native plotting parameters for readability: split crowded panels, reduce the number of features or terms per figure, increase width/height for many facets or long labels, set `nrow`/`ncol` deliberately, and avoid forcing many unrelated panels into one compressed plot.
- For single-cell UMAP, tSNE, spatial points, or other dense scatter plots above ~50,000 points, default to pure vector discrete points. In R, use `geom_point()` or the native plotting function's vector point layer and tune `size` / `pt.size` around `0.1`-`0.4` for hundreds of thousands of cells; in Python, use the normal vector scatter layer and tune `s` to the equivalent tiny visible size. Do not switch the dense point layer to raster mode unless the user explicitly asks for a separate performance-compromise preview.
- Do not accept native default titles, subtitles, captions, rainbow palettes, random group order, or unreadable legends as final. A subtitle is always a release blocker: clear it before export, then verify its absence in the rendered PDF/PNG. Override other defaults when the function allows it; otherwise state the limitation.
- Treat any non-English visible figure text as a release blocker. Before delivery, inspect the rendered PDF/PNG and verify that titles, axes, ticks, legends, annotations, facet labels, and automatically generated labels are all English.
- Do not accept distorted figures. A figure is not done just because it saved successfully.
- After any visualization is generated, open or render representative final images and check the actual display effect. This review must include aspect ratio, readable text, unclipped labels, non-crowded facets, visible axes, and legends that do not cover the data.
- For HTML reports, validation must include visual review of the embedded figures, not only counting `<img>` tags. Check that aspect ratios are preserved, text is readable, labels are not clipped, legends do not cover data, and panels are not squeezed.
- If a native plotting function cannot produce a readable figure for the current content, either split the result into several native plots or clearly state why a small custom plot is needed.
- Before final delivery, revise any compressed, stretched, clipped, crowded, or unreadable figure; do not hand off a report or plot set that has not passed visual review.

## Custom Plot Red Flags

Stop and return to the Analysis-Native Visualization Gate when any of these appear:

| red flag | required correction |
|---|---|
| Extracting a CellChat, LIANA/LIANA-py, NicheNet, MultiNicheNet, cell2cell, enrichment, trajectory, spatial, regulon, or marker result table only to recreate a standard network, bubble, heatmap, dotplot, UMAP, spatial, trajectory, or enrichment plot | Use the analysis package, companion package, or OmicVerse/SCOP wrapper first |
| Rejecting SCOP or OmicVerse because the wrapper function name is generic | Check input format, conversion helper, visualization family, and mode parameters first |
| Saying a custom plot is clearer before trying native parameters | Tune native or wrapper parameters and re-render first |
| Treating an ugly first render as proof native visualization failed | Split panels, adjust size, labels, legend, palette, layout, and selected features, then re-render |
| Using ggplot2/matplotlib/seaborn as the main evidence plot without rejecting analysis-native options | Ask user to confirm custom replacement |
