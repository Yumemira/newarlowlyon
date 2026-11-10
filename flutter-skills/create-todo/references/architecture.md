# Scaffold architecture and worked example

Read when deriving a new architecture or needing a concrete translation example.

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

