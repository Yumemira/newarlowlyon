---
name: flame-game-development
description: "Implement or fix Flame scenes, components, camera, input and game lifecycle in Flutter. Use for Flame runtime work; ordinary Flutter screens and standalone game design do not require it."
---

# Flame Game Development

Deliver a playable, bounded change that fits the existing game. Read
[Runtime decisions](references/runtime.md) for lifecycle, timing or scene work.

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

1. Identify the world, camera, input owner and Flutter host. Reuse the current game
   instance across host rebuilds unless the requested behavior is a fresh session.
2. Keep frame-driven simulation in the game/component loop. Publish coarse events
   such as health, score and scene changes to the existing UI state mechanism.
3. Choose collision detection for overlap events; choose a physical solver only
   when the mechanic needs physical response. Do not add Forge2D for every hitbox.
4. Implement ownership explicitly: who loads assets, owns subscriptions, resets
   state, removes components and disposes the game/session.
5. Exercise the affected gameplay path plus relevant restart, pause/resume or
   remount behavior. Run scoped analysis and tests under the project's conventions.

## Runtime rules

- Distinguish one-time loading from repeatable mounting. A component added to the
  tree can still be loading; await the relevant readiness condition before access.
- Keep render free of gameplay mutations. Use elapsed time deliberately; multiplying
  by dt alone does not guarantee identical collision or integration outcomes.
- Separate world, viewport and screen coordinates. Convert screen positions when needed
  for world targeting; event-local positions may already be converted. Flutter
  overlays use screen layout.
- Clear transient input on loss of focus or cancellation. A pause overlay must not
  accidentally pass actions into the world; check host lifecycle handling as well.
- A collection, kill or scene transition should occur once for its gameplay event,
  even if multiple shapes or callbacks report contact.
- Prefer simple components first. Add pooling, batching or spatial indexing in
  response to a measured workload, with reset behavior verified.

## Host and pause boundaries

An overlay is presentation, not an automatic simulation pause. Preserve independent
pause reasons (user menu, focus loss, app lifecycle) so returning to the foreground
cannot resume a user-paused game. Use the host's supported game ownership mechanism,
including GameWidget.controlled where appropriate. Provide loading/failure behavior
when changing startup. Match the coordinate space already supplied by an input event;
do not transform component-local coordinates a second time. Track simultaneous touch
controls by pointer identity and release them on cancel as well as end.

## Delivery

Explain the player-visible change, affected lifecycle behavior and checks actually
performed. Do not claim device performance from a debug launch. Use the separate
quality workflow only when profiling or a broader game audit is part of the task.

## Skill maintenance

Use [Evaluation cases](references/evaluation.md) when validating this skill itself;
these are not a mandatory full suite for every game edit.
