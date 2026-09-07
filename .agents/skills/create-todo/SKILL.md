---
name: create-todo
description: Create a compile-ready, TODO-only Flutter/Dart project scaffold from a free-form idea, product description, or implementation plan. Interpret the idea, derive the architecture, and generate the required folders, files, classes, fields, constructors, interfaces, abstract/base classes, method signatures, state boundaries, and test seams without implementing business behavior. Use when the user asks for /create-todo, $create-todo, a project skeleton, an OOP/Clean Code scaffold, or a Flutter/Dart architecture blueprint.
---

# Create TODO Scaffold

Treat a free-form idea, product description, or implementation plan as the input
specification. First interpret the idea, then build its structural skeleton and stop
before behavior implementation. The result must make ownership, dependencies, data
flow, design intent, assumptions, and future implementation order explicit while
remaining syntactically valid and compile-ready.

## Workflow

1. Read the complete idea or plan and the repository's `AGENTS.md`/local instructions.
2. Translate the idea into a compact design brief before editing:
   - product goal and target user;
   - main user actions/events and expected state transitions;
   - domain concepts, data sources, persistence, and external integrations;
   - required screens/views and their view models;
   - constraints, risks, and conservative assumptions.
3. Inspect `pubspec.yaml`, `analysis_options.yaml`, SDK constraints, existing folders,
   state-management choice, routing, dependency injection, and neighboring features.
4. Derive a minimal symbol map: files, types, members, dependencies, data flow, and
   integration points. Do not create layers or abstractions with no responsibility.
5. Choose the smallest architecture tier that satisfies the feature:
   - small: `View -> ViewModel -> Repository`;
   - medium: add `Service` and explicit data/domain models;
   - complex: add `Domain`, use cases, value objects, or commands only for complex,
     shared, or independently testable rules.
6. Create the scaffold with patch-based edits. Preserve unrelated user changes.
7. Run formatting and a syntax/static-analysis check. Run targeted tests only when the
   repository already has a meaningful test harness; do not create fake passing tests.
8. Report the interpreted idea, assumptions, created files and responsibilities, the
   dependency direction, the abstraction rationale, the TODO implementation order, and
   the validation result. Explicitly state that runtime behavior is unfinished.

### Example of the expected behavior

For an input such as “сделай приложение для учёта тренировок”, first infer a compact
brief: users create workouts, view progress, and edit entries; the feature needs workout
state, a repository boundary, and a view model. Then create the smallest appropriate
file/class map. Each generated concrete symbol receives an explanatory TODO, for example:

```dart
// TODO(S1): Add the workout state owner here. Keep the collection private so that
// ViewModel commands cannot mutate entries directly; expose read-only snapshots and
// explicit add/update/remove methods. S2 and S3 depend on this boundary.
class WorkoutRepository {
  List<Object> get workouts {
    // TODO(S1): Return a read-only snapshot of the source-of-truth collection and
    // enforce invariants through explicit add/update/remove methods.
    throw UnimplementedError('TODO(S1)');
  }
}
```

The TODO describes the intended design, ownership, contract, dependencies, and future
implementation order. Do not fill in repository logic, persistence, widgets, or event
effects in this step.

## Flutter Architecture Default

Use the existing architecture when one is present. For a new or ambiguous Flutter
feature, use this separation unless the requirements justify a smaller design:

- `ui/<feature>/...`: views, widgets, and view models. Views render state and forward
  user actions; they do not contain data access or business rules.
- `data/repositories/...`: repository contracts and implementations. Repositories are
  the source of truth, own caching/error/retry decisions, and expose domain models.
- `data/services/...`: API, database, filesystem, or platform wrappers. Services hold
  no application state and expose typed `Future`/`Stream` boundaries.
- `domain/...`: entities, value objects, and use cases only when rules are complex,
  shared, or would otherwise crowd view models.
- `di/...`: dependency registrations and composition roots. Do not instantiate concrete
  services inside widgets or view models.
- `test/...`: seams for services, repositories, view models, and views. Add only
  structural test TODOs when tests are requested or mandated by the project.

Prefer the Flutter team's UI/data separation, repository/service boundaries, MVVM
view/view-model pairing, unidirectional data flow, dependency injection, and abstract
repository contracts. Adapt the choice to the project; do not add `ChangeNotifier`,
Provider, Riverpod, BLoC, or another package when the project already uses a different
state solution.

## Dependency Direction

Keep dependencies flowing inward toward stable contracts and domain rules:

```text
UI -> ViewModel/Commands -> Domain contracts -> Repository contract
                                                    ^
                              Repository implementation -> Service
```

Do not import UI types into data/domain layers, do not make repositories depend on one
another, and do not introduce cycles. If a feature needs data from multiple repositories,
combine it in a view model or domain layer rather than coupling repositories together.


## OOP and Clean-Code Rules

- Apply SOLID as a design heuristic, not a file-count target. Use single responsibility
  when it gives a class one cohesive reason to change.
- Apply open/closed and dependency inversion selectively at volatile boundaries such as network,
  storage, clock, platform APIs, and repositories. Depend on contracts from higher
  layers, inject implementations, and avoid service locators in leaf classes.
- Apply interface segregation: expose small role-specific contracts instead of a large
  "god interface". Create an interface when it represents a replaceable boundary,
  test seam, or stable public contract; do not create interfaces for every data class.
- Respect substitutability: an implementation must honor the contract's inputs,
  outputs, error semantics, nullability, and lifecycle expectations.
- Prefer composition over inheritance. Use a base class only when shared invariants or
  behavior genuinely belong to every subtype; use `abstract base class` for controlled
  extension and `abstract interface class` for a pure contract when the SDK constraint
  is Dart 3+. For older SDKs, use a compatible `abstract class` contract.
- Use `sealed`/`final`/`interface`/`base` modifiers to communicate and enforce intended
  extension. Use `implements` for contracts and `extends` only for real specialization.
- Keep names intention-revealing and methods focused. Avoid boolean flags that combine
  unrelated modes, speculative abstractions, mutable global state, and deep nesting.
- Do not create a layer, interface, base class, use case, or mapper unless it has a
  separate responsibility, a real replacement/test seam, or a stable architectural
  boundary. Explain each non-obvious abstraction in the final report.

## Idea-to-Scaffold Translation

When the request is only an idea, do not wait for a formal specification if a safe
architecture can be inferred. Make conservative assumptions, record them in the final
report, and encode unresolved product decisions as ordered TODOs. Map the idea as follows:

- user goal -> feature/module boundary;
- user action -> view event, command, or view-model method;
- application state -> immutable state model plus its single owner;
- business rule -> domain method or use-case contract when complexity justifies it;
- external data -> service contract and repository policy;
- screen -> view and view-model pair;
- navigation -> route declaration/integration TODO, without wiring unfinished behavior;
- persistence/integration -> repository/service contract and composition-root TODO.

Create the files needed to show this design, but do not invent undocumented product
features merely to fill the architecture. If the idea is ambiguous, choose the least
surprising option and mark the decision as an assumption or TODO.

## Data Encapsulation Contract

Treat data storage and data processing as separate responsibilities:

- Store mutable state behind private fields or private collections owned by the data
  class/repository. Never expose a mutable list/map/set for callers to mutate directly.
- Expose read-only views, immutable value objects, streams, or snapshots for reads.
- For collections, use `List.unmodifiable`, `UnmodifiableListView`, immutable models,
  or a defensive snapshot rather than returning mutable storage.
- Expose explicit public methods for every allowed mutation (`add`, `update`, `remove`,
  `refresh`, etc.). Validate invariants inside the owner; callers must not assign fields
  or reach into storage.
- Event handlers, view models, commands, and controllers may request mutations only
  through those public methods. They may read returned values/snapshots but must not
  alter the owner's variables directly.
- Keep service I/O separate from repository policy and keep presentation state separate
  from domain/data state. Mark TODOs at each future boundary.

## Model Rules

- Make DTOs, entities, and value objects immutable by default with `final` fields and
  `const` constructors where possible. Add `copyWith` and value equality only when the
  project convention or the feature requires them.
- Keep API/serialization DTOs out of the UI. A repository or mapper converts DTOs into
  domain/application models before exposing them upward.
- Keep mutable state in one owner class. View models, commands, and event handlers may
  request changes through public methods, but must not mutate repository/model storage.

## Dart Scaffold Rules

- Use sound null safety. Avoid `!` and fake `null` values as placeholders.
- Use `const` constructors and immutable fields where valid; prefer `final` members.
- For abstract methods, omit bodies; they do not need placeholder TODO bodies. For
  unfinished concrete classes or methods, include a specific
  `// TODO(Sn): ...` and `throw UnimplementedError('TODO(Sn)')`; never return fake success.
- Every unfinished concrete class or method must have a specific TODO describing the behavior,
  inputs/outputs, failure cases, and relevant lifecycle or integration constraints. The
  TODO must also explain the design intent: why this type owns the responsibility, what
  it must not do, which contract it uses, and which later TODO depends on it.
- Keep imports, exports, generic types, visibility, and annotations valid. Never hand-edit
  generated files; add a TODO at the source/schema or generator integration instead.
- For `StatefulWidget`, define lifecycle ownership and disposal TODOs. After async gaps,
  leave a TODO or guard for `mounted`/`context.mounted` before state or context use.
- Do not register, route, schedule, or call unfinished components at runtime. Add a TODO
  at the future composition-root integration point.

## Validation and Completion Boundary

Run the narrowest relevant checks and report any unavailable tool or pre-existing
failure instead of hiding it. Detect the package type first:

- `dart format --output=none --set-exit-if-changed <changed Dart files>`
- `dart analyze` for Dart packages, or `flutter analyze` for Flutter packages
- `dart test` for Dart packages, or `flutter test` for Flutter packages with tests
- targeted tests first, then the full suite when the change is cross-cutting

Do not run Flutter commands when `pubspec.yaml` is absent or the project is not a
Flutter package. Do not create a test that passes only because its body is empty.

## Scaffold Report

Include a concise final report containing:

- the interpreted idea, assumptions, open decisions, and proposed user flow;
- the generated file tree and responsibility of each file;
- the chosen architecture tier and why larger tiers were not added;
- each interface/base class, its reason, and whether it uses `implements` or `extends`;
- the dependency direction and data ownership/mutation boundary;
- ordered TODO identifiers and the intended implementation sequence;
- validation commands and their results.

## Completion Boundary

Stop after the architecture scaffold exists, TODOs are concrete and ordered, and the
permitted format/analyze check succeeds. Do not implement behavior, networking,
persistence, algorithms, migrations, secrets, or user-visible flows in this command.

## Source Basis

The Flutter-specific boundaries follow the official Flutter architecture guidance:
[architecture recommendations](https://docs.flutter.dev/app-architecture/recommendations),
[architecture guide](https://docs.flutter.dev/app-architecture/guide), and
[Dart design guidance](https://dart.dev/effective-dart/design). These are applied as
context-sensitive defaults, not as a reason to add unnecessary abstraction.
