---
name: forge2d-game-physics
description: "Implement or debug Forge2D physics in Flutter/Flame games: bodies, contacts, joints and simulation timing. Use for physical response; simple overlap detection does not require a physics engine."
---

# Forge2D Game Physics

Implement a stable physical mechanic using the project's resolved Forge2D API.
Read [Physics decisions](references/physics.md) for units, stepping and contacts.

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

## Select the API generation first

flame_forge2d 0.20 / Forge2D 0.15 introduced native Box2D v3 bindings and a new API.
Older projects use a pure-Dart generation with fixtures. For current-generation
initialization, shapes, opt-in contact events and native world disposal, read
[Native API boundary](references/native-api.md). Never mix examples from these two
generations or treat a package upgrade as an incidental repair.

## Workflow

1. Identify who owns the physics world and advances it. In an existing Forge2DGame,
   inspect its stepping implementation before adding any accumulator or substeps.
2. Establish the coordinate system, world-to-screen scale, camera and intended body
   sizes. Separate physical units from image pixels and UI coordinates.
3. Choose body types, shapes, sensors, mass/density, collision filters and joints from
   the intended interaction. Use supported force/impulse APIs for dynamic motion;
   reserve direct transforms for deliberate teleport/reset behavior.
4. Handle contact events at the gameplay level. Multiple shapes (fixtures in older releases) may create multiple
   callbacks; implement per-attack/per-target or cooldown semantics as required.
5. Schedule structural world mutations safely relative to simulation callbacks and
   the version's world-lock rules. Do not destroy a live body midway through a locked
   solver callback.
6. Verify the mechanic, pause/resume, reset and affected edge cases. For fast small
   bodies test supported continuous-collision settings rather than assuming immunity
   to tunneling. State observed limits.

## Scope and delivery

Do not migrate a working arcade controller to physics unless the user asks or the
mechanic requires it. Avoid combining separate collision systems for the same response.
Report unit/step decisions and behavior tests; do not promise deterministic networking
from fixed timestep alone. Pure physics tests may use tolerances appropriate to the
resolved solver and platform.

Use [Evaluation cases](references/evaluation.md) when validating this skill.
