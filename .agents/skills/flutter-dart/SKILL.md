---
name: flutter-dart
description: Generate, modify, and review Dart and Flutter code using idiomatic null-safe APIs, the project's existing architecture and dependencies, Flutter lifecycle rules, responsive UI patterns, and appropriate automated tests. Use for any Flutter or Dart task involving .dart files, pubspec.yaml, widget trees, state management, platform integration, performance, or code generation.
---

# Flutter & Dart

Apply these rules whenever generating or changing Flutter/Dart code. Preserve the
project's existing architecture and state-management approach; do not introduce a
new framework or dependency unless the task requires it and the choice is justified.

## Workflow

1. Inspect `pubspec.yaml`, `analysis_options.yaml`, the Flutter/Dart SDK constraint,
   neighboring features, and existing tests before editing.
2. Follow existing naming, folder, routing, dependency-injection, and state patterns.
3. Implement the smallest cohesive change with sound null safety and clear ownership
   of state and resources.
4. Add or update unit, widget, integration, or golden tests at the appropriate layer.
5. Format and validate the affected package. Prefer `dart format`, `dart analyze`,
   and `flutter test`; use the project's prescribed commands when they differ.

## Implementation Rules

- Keep code sound-null-safe. Avoid `!` unless the invariant is local and explicit;
  prefer guards, pattern matching, or typed helpers.
- Prefer immutable data and small focused widgets/classes. Use `const` constructors,
  `const` collections, and `const` widgets wherever they are valid.
- Keep `build` side-effect free and cheap. Never perform network, disk, or state
  mutations from `build`; move them to lifecycle methods, controllers, or services.
- Give state a clear owner. Dispose `AnimationController`, `TextEditingController`,
  `FocusNode`, streams, timers, and subscriptions in `dispose`.
- After every `await`, check lifecycle validity before using a `BuildContext` or
  mutating a `State` object (`context.mounted` or `mounted` as appropriate).
- Use stable keys only when identity matters (reordered/dynamic children, forms,
  restoration, or tests). Do not add keys mechanically.
- Keep business logic out of widgets. Extract domain/data concerns into the existing
  application layers and expose explicit loading, success, empty, and error states.
- Use `ListView.builder`/slivers for large or unbounded lists, avoid repeated work in
  item builders, and preserve state intentionally when children are reordered.
- Handle accessibility and responsive layouts: semantic labels, tappable targets,
  text scaling, localization, safe areas, and compact/large screen constraints.
- Respect generated-code boundaries. Update the source/schema and run the project's
  generator; do not hand-edit generated files unless the repository explicitly does so.

## Dependencies and Platform Code

- Do not upgrade dependencies casually. Change constraints only when needed, then use
  the repository's package-management command and review the resulting lockfile.
- Prefer platform-agnostic Dart first. When platform code is required, keep Android,
  iOS, web, desktop, and conditional imports aligned and document platform limits.
- Preserve existing API contracts, serialization formats, and public exports unless
  the request explicitly includes a breaking change.

## Validation Checklist

Run the narrowest relevant checks and report any unavailable tool or pre-existing
failure instead of hiding it:

- `dart format --output=none --set-exit-if-changed <changed Dart files>`
- `dart analyze` (or `flutter analyze` for Flutter packages)
- `flutter test` for widget/application changes; add `--coverage` only when required
- targeted tests first, then the full suite when the change is cross-cutting
