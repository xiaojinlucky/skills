---
name: HERO-Anti-OverDefense
description: Use when deciding whether a check, hash, edge-case guard, rubric, reviewer step, or extra abstraction is justified by a real reachable risk and can change the next action.
---

# HERO Anti-OverDefense

Use the upstream rules in `RULES.md` as a proportionality check for agent work.

Keep checks that address a real reachable risk, protect data or permissions, or are explicitly required. Remove process that only anticipates hypothetical problems, repeats unchanged evidence, replaces judgment with a rubric, or builds infrastructure without a current consumer.

The upstream examples in `cases/` are counterexamples and calibration material. They do not override a user's explicit safety, validation, or release requirement.
