# Omics Coding Local Index

- Fetched at: 2026-08-03T14:16:23+00:00
- Package argument: all
- Function rows: 743
- Parameter rows: 9752

## Counts

- omicverse: 411 function docs
- scop: 332 function docs

## Files

- `function_index.tsv`: one row per function.
- `parameter_index.tsv`: one row per parameter occurrence.
- `omicverse/functions/*.md`: OmicVerse function docs.
- `scop/functions/*.md`: SCOP function docs.
- `tooling-and-evidence.md`: official tool bridge and evidence triage rules.

## Refresh

Run from the skill directory:

```bash
python3 scripts/update_docs.py --package all
```

<!-- omicos-reference:begin -->
## OmicOS Reference Layer

- OmicOS raw skills: 60
- OmicOS strict omics agents: 32
- `omicos/skill_index.tsv`: one row per OmicOS skill with route role and risk note.
- `omicos/agent_index.tsv`: one row per strict omics OmicOS agent with routing, NOT-FOR, handoff, and risk note.
- `omicos/integration_policy.md`: authority order and Murphy acceptance checks.
- `omicos/route_cards/*.md`: compact workflow reminders; use only after OmicVerse/SCOP function discovery.
- `omicos/agent_route_cards/*.md`: compact agent handoff reminders; not an authority layer.
- `omicos/raw_agents/`: selected public agent JSON plus runtime roster for audit.
<!-- omicos-reference:end -->
