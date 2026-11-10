---
name: todo-release
description: Find and implement every actionable TODO comment in a specified project's first-party source code, using mandatory current web research for each distinct requirement, then verify the project, rescan for TODOs, review the resulting code for risks, and produce a sourced completion report. Use when the user invokes $todo-release, selects todo-release from the slash-command skill list, or asks Codex to finish TODO-planned functionality across a project.
---

# TODO Release

Convert TODO-planned source code into finished functionality. Do not treat deleting or rewriting a marker as implementation.

## Establish Scope

1. Use the project path supplied after invocation. If none is supplied, use the current project root.
2. Read all applicable repository instructions before modifying anything. Follow required specification, planning, ownership, testing, packaging, and language rules even when they add stages to this workflow.
3. Inspect repository status and preserve unrelated user changes.
4. Search first-party source files for case-insensitive line comments matching `//\s*TODO\b`, including tracked and relevant untracked source files.
5. Exclude `.git`, dependency caches, build outputs, generated sources, vendored or third-party code, minified files, runtime data, and external submodules unless the user explicitly includes them.
6. Build an inventory with file, line, exact requirement, affected component, dependencies, and verification method. Re-run the search immediately before editing so line references are current.

Do not silently widen a path to its parent workspace or other repositories. If the project contains independent modules, obey local ownership rules and process them in dependency order.

## Research Every TODO

Perform internet search before implementing each distinct TODO or tightly related TODO cluster. The user requires Google-style web research; use the available web search capability and do not rely on memory alone.

- Form a query from the language, framework and exact technical requirement.
- Prefer primary sources: official documentation, specifications, maintainers' repositories, release notes, standards, and original papers.
- Check that guidance matches the project's exact dependency and runtime versions.
- Compare plausible approaches when correctness, performance, compatibility, security, or operational cost differs materially.
- Choose the simplest robust solution consistent with the existing architecture. “Optimal” means best for this project, not newest or most elaborate.
- Keep the supporting URLs and the decision rationale for the final report.
- Never copy untrusted snippets blindly. Adapt the design to local conventions and inspect licenses when reuse goes beyond an ordinary idiom.

If web access is unavailable, stop before implementation and report that the mandatory research condition cannot be satisfied.

## Implement

1. Resolve TODOs in dependency order and in small coherent batches.
2. Inspect call sites, public contracts, configuration, data flow, threading, error handling, and lifecycle before changing a TODO location.
3. Implement the complete described behavior, including validation, failure paths, cleanup, concurrency constraints, compatibility, and operator-facing diagnostics required by the project.
4. Add or update tests only when requested or allowed by repository instructions. Never violate a project rule that limits automated tests.
5. Remove the TODO marker only after its requirement is fully implemented. Preserve explanatory comments that still add value without labeling finished work as TODO.
6. Do not replace TODOs with `FIXME`, placeholder exceptions, fake values, empty bodies, suppressed warnings, commented-out code, or unconditional success.
7. Do not implement materially ambiguous requirements by guessing. Exhaust local context and research first; ask the user only when different interpretations would change behavior or public contracts.
8. Do not publish, deploy, push, migrate live data, or modify runtime data unless the user separately authorizes that action.

## Verify

After each coherent batch, run the narrowest repository-approved verification. At the end:

1. Run the required compile or packaging command for every affected module.
2. Run only tests and static checks permitted by local instructions.
3. Inspect the full diff for accidental edits, incomplete branches, placeholder behavior, debug output, secrets, compatibility breaks, and unnecessary complexity.
4. Re-run the original TODO search over the same scoped first-party sources.
5. Search for common disguised leftovers relevant to the language, including `FIXME`, `UnsupportedOperationException`, `NotImplemented`, `return null`, empty handlers, or equivalent placeholders. Evaluate matches rather than deleting legitimate code mechanically.
6. Review correctness, security, concurrency, performance, resource handling, error recovery, API/config/schema compatibility, and operational observability.

Completion requires zero unresolved in-scope TODO markers, successful permitted verification, and no known critical correctness blocker. If any TODO cannot be completed, state that the release is incomplete and report the exact blocker; never claim success based only on a clean text search.

## Report

Write the final report in the user's language and include:

- completion status and project path;
- inventory count found, implemented, excluded, and unresolved;
- concise summary by file or component;
- verification commands and outcomes;
- final TODO rescan result and any suspicious-placeholder findings;
- problems discovered, fixes made, and residual risks;
- source links grouped with the decisions they supported.

Lead with blockers or remaining risks. When everything is complete, say explicitly that no in-scope TODO comments remain.
