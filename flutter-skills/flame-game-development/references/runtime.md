# Runtime decisions

## Timing

Represent speeds per second and durations in seconds or Duration with explicit
conversions. For acceleration, collisions and cooldowns, choose variable dt or a
fixed-step accumulator based on the mechanic and existing engine behavior.
A custom fixed-step loop needs a bounded catch-up policy after stalls; decide
whether excess time is dropped, deferred or represented differently. Do not add a
second world-step loop around a physics engine that already owns stepping.
Replay tests need controlled input, clock and random seed. Seeded randomness alone
does not establish cross-platform determinism.

## Component ownership

`onLoad` is once per component lifetime; `onMount` can happen repeatedly. Do not
initialize a late-final field repeatedly during mounting. Pair repeatable listener
registration with unregistration; do not dispose shared assets from a single enemy.
Removal/addition are lifecycle operations, not an immediate guarantee of readiness.
A reset should explicitly reset score, spawn timers, input and session subscriptions.
Persist durable progress separately from disposable world objects.

## Camera and presentation

Select a viewport strategy based on intended visible play area, aspect ratios and
pixel art requirements. Keep HUD positioning independent of world movement. Test
resize and camera zoom with pointer targeting. Define camera bounds and look-ahead
from level geometry rather than screen pixels scattered through components.

## Collision decision

Hitboxes detect overlap but do not implement a solid-body response. Fast small
objects may tunnel; test swept/raycast approaches supported by the current API,
smaller steps or a physical solver as appropriate. Avoid resolving an event twice
through both a Flame hitbox and a Forge2D contact on the same mechanic.

## Audio integration when requested

Preserve the project's chosen audio backend. Keep loading/caching outside the hot
update loop and define ownership of music, sound effects and their resources. A game
pause and application backgrounding may require different audio behavior; follow the
product's intended policy. Do not create a player/engine on every shot or reinitialize
an existing global audio engine on each scene entry.

If flutter_soloud is selected, inspect its version-matched bundled skills rather than
copying APIs from another audio library. The package documents
`dart run flutter_soloud:skills --check` for checking installed skill freshness.
Installing/updating bundled skills is a separate mutation; do it only within the
user's authorized setup scope and inspect existing local edits first. Do not install
all audio skills automatically just because this runtime skill is used.
Source: https://pub.dev/packages/flutter_soloud#ai-agent-skills

## Host, focus and failure handling

GameWidget.controlled can own a game created by a factory; ordinary GameWidget can
host an instance owned elsewhere. Choose one owner, and inspect the resolved lifecycle
before explicitly disposing it. Game removal and final disposal are different events.
GameWidget does not inherently clip its canvas; embedded games may need clipping and
finite parent constraints. Its errorBuilder handles loading errors, not every future
runtime exception. Async work completed after a scene was replaced must not populate
the new scene or update a disposed UI; use session identity/lifecycle checks.

Represent pause intent independently from the visible overlay. Test menu-open ->
background -> foreground: gameplay must stay paused until the player resumes. Audio
has its own lifecycle policy. A cancelled drag must release the matching pointer only,
not cancel an unrelated movement finger. Event-local positions are already converted
for their receiver; verify the event's coordinate contract before applying a camera
conversion. HUD actions should be reachable by the supported input method and have
Flutter semantics where needed; canvas drawings do not automatically become buttons.

Additional sources checked 2026-09-30:
- https://docs.flame-engine.org/latest/flame/game_widget.html
- https://docs.flame-engine.org/latest/flame/overlays.html
- https://docs.flame-engine.org/latest/flame/inputs/drag_events.html
- https://docs.flutter.dev/ui/accessibility

## Sources

Research baseline: 2026-09-30. Recheck version-sensitive details against the project.
- https://docs.flame-engine.org/latest/flame/components/components.html
- https://docs.flame-engine.org/latest/flame/game.html
- https://docs.flame-engine.org/latest/flame/collision_detection.html
- https://pub.dev/packages/flame
