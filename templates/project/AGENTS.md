# Project Instructions

This is a project-local Flutter/Dart workspace.

## Local Spec Kit

Use only the Spec Kit state and Codex skills inside this project:

- `.specify/` contains specifications, workflows, templates, and feature state.
- `.agents/skills/` contains the Codex/Spec Kit skills for this project.
- `.agents/skills/flutter-dart/SKILL.md` governs Flutter/Dart implementation.
- `.agents/skills/create-todo/SKILL.md` governs TODO-only project scaffolding.

Do not search for or modify Spec Kit state in a parent workspace. New specifications,
plans, tasks, and generated scaffolds belong to this project's own directories.

## Flutter/Dart Rules

Inspect `pubspec.yaml`, `analysis_options.yaml`, and neighboring features before editing.
Preserve sound null safety, the existing state-management choice, widget lifecycle rules,
data encapsulation, and the project's architecture. Keep UI, view-model, repository, and
service responsibilities separate. Run the narrowest relevant `dart`/`flutter` format,
analyze, and test commands after changes.

## Scaffold Rule

For an idea-to-structure request, use `$create-todo` (or `/create-todo` in the UI). Create
compile-ready files and specific `// TODO` markers explaining design intent, ownership,
contracts, dependencies, edge cases, and implementation order. Do not implement runtime
behavior during scaffolding.
