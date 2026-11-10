---
name: rescrinit
description: "Perform a full Flutter application reskin/rebrand: replace the visual system, images, copy, localization values, and translation keys while preserving business behavior and validating that legacy keys and design remnants are gone."
---

# Rescrinit — full application reskin

Use this skill when the user invokes `/rescrinit` or asks for a complete redesign/rebrand of an existing Flutter app. A rescrinit is a controlled migration of the app's identity, not a single theme-color change.

## Input

Interpret the command arguments as the desired direction, for example:

```text
/rescrinit dark graphite with emerald accents, calm productivity tone
```

If the direction is incomplete, infer a coherent proposal from the existing app and state assumptions before implementation. Ask only when a missing choice would materially change the product identity or required assets.

## Non-negotiable rules

- Preserve routes, domain behavior, storage, permissions, data models, API contracts, and state-management architecture unless explicitly requested otherwise.
- Inspect `AGENTS.md`, the nearest `pubspec.yaml`, the project's Flutter skill, and the current theme/localization architecture before editing Dart.
- Treat the new palette and typography as tokenized design-system changes. Eliminate direct legacy color literals and obsolete theme aliases from production code.
- Rewrite user-facing copy, not only its translation. Keep placeholders, plural forms, and interpolation semantics intact.
- Rename translation keys everywhere: every locale map, static/dynamic lookup, `.tr`, `.trParams`, `.trPlural`, generated/localization helpers, tests, fixtures, and application-contract documentation. Do not keep old keys as compatibility aliases unless explicitly requested.
- Use a generated, reviewable old-to-new key map and apply replacements longest-first to avoid prefix collisions.
- Replace or restyle images and brand assets only after inventorying consumers, dimensions, and semantic role. Never invent a binary asset silently; use ImageGen when an image is required and available, otherwise leave a tracked asset task.
- Keep `.rescrinit/` as working evidence until final validation and the completion report are recorded.

## Workflow

### 1. Baseline and inventory

Create or refresh `.rescrinit/` with:

- `metadata.json` — request, direction, timestamp, project, baseline status, counters, and stage.
- `analysis/structure.json` — routes, screens, widgets, dialogs, sheets, empty/loading/error states, and transient surfaces.
- `analysis/keys.json` — every locale key and value, locale list, placeholders, plurals, and parity gaps.
- `analysis/usages.json` — every translation usage and source location, including dynamic templates.
- `analysis/images.json` — raster/vector assets, dimensions, consumers, brand relevance, and replacement status.
- `analysis/colors.json` — theme tokens, hardcoded color literals, and their consumers.

Use repository search and source inspection, not guesses. Record unrelated pre-existing changes in `metadata.json`; do not overwrite them.

### 2. Design contract

Before broad edits, define and persist:

- `color_palette.json` with semantic roles (surface, text, accent, control, focus, disabled, success, warning, error) and contrast expectations;
- typography, shape, elevation, motion, and component direction;
- copy voice, naming conventions, and the new translation-key namespace/pattern;
- asset replacement list plus prompts or acceptance criteria.

Cover the app shell, navigation, forms, overlays, charts, illustrations, onboarding, PDF/print output, launcher/splash metadata, and semantic states where present.

### 3. Specification artifacts

Use the repository's Spec Kit flow when available. Resolve and reuse the assigned active feature through the project Spec Kit flow, honoring explicit SPECIFY_FEATURE_DIRECTORY before feature.json. Create a new feature only when the task actually requires one, persist its selection (project-relative inside the app), then refresh AI_INDEX.md. The selected feature contains at minimum `spec.md`, `plan.md`, `tasks.md`, and validation notes. State explicitly that this is a full rescrinit, list preserved contracts, and include acceptance criteria for zero old-key references and locale parity.

### 4. Implementation order

1. Establish design tokens and theme authority.
2. Migrate shared layouts, components, pages, painters, gradients, charts, and interaction states.
3. Rewrite copy and generate the complete `mappings/key_rename_map.json`.
4. Rename locale keys and all usages atomically in longest-first batches; after each batch run a key/reference audit.
5. Replace approved images/icons/illustrations and update asset declarations and platform metadata.
6. Update PDF/export and other non-widget visual surfaces.
7. Remove obsolete aliases, literals, old brand names, and stale compatibility code.

Do not mix a route or business-logic rewrite into the rescrinit. If a visual requirement exposes a behavior bug, document it separately and keep the scope boundary explicit.

### 5. Validation gates

Run the project's formatter, analyzer, and relevant tests. At minimum verify:

- every locale has the same new key set;
- placeholders and plurals match across locales;
- zero old keys are defined or referenced in first-party app code;
- no forbidden legacy colors, brand names, or old asset references remain;
- representative screens and transient states render correctly at text scaling and narrow/wide sizes;
- contrast passes for text, icons, controls, focus, disabled, and semantic states;
- PDF/print, splash, launcher, and image assets match the new identity;
- route, storage, permissions, state, and regression tests remain green.

Prefer targeted Flutter tests first, then the full prescribed suite. Capture commands, counters, failures, screenshots/goldens, and unresolved items in `.rescrinit/validation/` and the feature completion report.

## Completion standard

Do not claim completion while any of these remain: old translation keys in source or locale files, locale-set mismatch, unreviewed brand assets, unexplained legacy colors, failing analyzer/tests, or missing validation evidence. Finish with a concise report containing changed surfaces, key rename counts, locale/asset counts, validation commands and results, and explicitly listed follow-up work.

## Document navigation

If AI_INDEX.md exists, follow only this task’s routes. Put requirements, architecture and validation evidence in their existing owners, link sections instead of reproducing them. Refresh the project map after creating/moving documentation; do not generate a second project overview solely for this workflow.
