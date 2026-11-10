---
name: bonfire-rpg-development
description: "Implement or fix Bonfire RPG movement, combat, NPCs, navigation and map transitions. Use in Bonfire projects or when Bonfire is selected; do not force it on other game genres."
---

# Bonfire RPG Development

Use Bonfire's existing RPG facilities without mixing incompatible generations of
its APIs. Read [Version and gameplay boundaries](references/bonfire.md) before
editing movement/mixins or interpreting older examples.

## Project and version boundary

Honor the user's scope and the nearest project instructions. Resolve the actual
application root before editing; inspect its SDK, pubspec.yaml, pubspec.lock and
relevant source. Apply the project's Flutter/Dart conventions when changing Dart.
Do not upgrade packages, introduce a new state manager, or create a new application
just to apply this skill. For a new project, follow the workspace's initialization
and location rules. A scaffold-only request remains scaffold-only.

Use API documentation matching resolved dependencies. A website's `latest` or a
repository's default branch may differ from the installed release; check source or
versioned API docs when signatures matter. State assumptions and unavailable checks.

## Workflow

1. Establish the resolved Bonfire/Flame versions and inspect a nearby working player
   or enemy implementation. Select matching examples and migration documentation.
2. Reuse the package's facilities for movement, directional animation, attacks,
   sensors and pathfinding where they match the requested behavior. Keep inventory,
   quests and durable progress independent of disposable world components.
3. Make AI states and transition conditions explicit. Separate detection, navigation,
   attack cooldown and loss of target. Bound repeated pathfinding work to the actual
   need instead of recalculating paths on every frame without reason.
4. Define damage semantics: source, target, amount, eligibility/cooldown and death.
   Prevent unintended duplicate damage from overlapping fixtures or callbacks while
   preserving deliberately repeated area/contact damage.
5. For map transitions, resolve the target spawn, dispose old session listeners and
   avoid multiple transitions from a held interaction or repeated contact event.
6. Test the affected scenario: blocked routes, target removal, diagonal movement,
   attack cadence or scene restart. Confirm target-platform support with a real
   build when required; package badges alone are not evidence of a tested web game.

## Visibility and interaction boundaries

Camera visibility, AI awareness and collision availability are different. When tuning
navigation, inspect whether the query includes only visible barriers; test an offscreen
obstacle and camera movement before optimizing. For NPC dialogs, explicitly decide
whether world simulation continues and prevent the opening input from also attacking
or selecting the first answer. Treat quest rewards and transition requests as domain
events with defined repeat behavior, not as side effects of rebuilding dialog widgets.

## Delivery

Report implemented behavior, relevant package version, state/lifecycle decisions and
checks performed. Do not upgrade a 3.x project to 4.x as an incidental bug fix.
Use Tiled guidance only for actual map/schema work; do not assume flame_tiled imports
are interchangeable with the map API used by this Bonfire project.

Use [Evaluation cases](references/evaluation.md) for skill validation.
