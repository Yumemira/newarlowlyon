---
name: flutter-game-quality
description: "Test gameplay scenarios or diagnose performance and lifecycle bugs in Flutter games. Use for game QA, regressions or profiling; do not run a full audit after every minor edit."
---

# Flutter Game Quality

Produce reproducible evidence about game correctness or performance and fix issues
within the requested scope. Read [Test and measurement protocol](references/protocol.md)
for selecting a test layer or interpreting performance results.

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

## Select the relevant checks

- Rules and progression: pure Dart tests with controlled time and randomness.
- Flame components: the resolved flame_test API and explicit component readiness.
- Flutter host/HUD: widget tests for overlays, navigation and state transitions.
- Full session: integration/playtest for loading, input, defeat/victory, restart,
  background/foreground and saved progress when those paths are relevant.
- Rendering: targeted screenshots/goldens plus actual visual inspection. A passing
  golden does not establish frame timing, input latency or enjoyment.

## Diagnose before optimizing

Define a repeatable scene, input sequence and workload. Record SDK/package versions,
device, OS, renderer/build mode, screen refresh target and measurement duration.
For mobile performance use profile mode on a physical device. Web measurements must
use an appropriate browser/build workflow; do not assume mobile profiling commands
apply unchanged. Mark unavailable target measurements as unverified.

Inspect UI/raster frame times, outliers, allocation/GC behavior and retained resources
as relevant. Average FPS alone can hide hitches. Use measurements to choose a narrow
change, then repeat the same scenario. Do not claim a speedup from different scenes
or prescribe pooling/isolate work without evidence of the bottleneck.

## Coverage selected by the feature

For persistence work, test cold restart, a missing/corrupt save and a supported schema
migration; a normal scene reset is not a persistence test. For controls, include touch
cancellation/multitouch and focus restoration where supported. Check readable HUD and
semantics when changing interface interactions. Native physics/audio require their
real backend initialization in integration tests; a passing fake cannot verify native
cleanup or a browser's audio/WASM startup. Select the relevant cases, not all cases
for every edit.

## Completion

Report passed checks, observed failures, fixes, exact measurement conditions and
remaining coverage gaps. Keep pre-existing failures separate from new regressions.
After relevant checks pass, broaden testing only for a new risk or cross-cutting change.
A release-signing/icon audit is a separate workflow; use it when requested, not as a
substitute for gameplay tests.

Use [Evaluation cases](references/evaluation.md) when assessing this skill itself.
