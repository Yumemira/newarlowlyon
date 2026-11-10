# Test and measurement protocol

## Reproducible correctness

Drive a clock or explicit simulation steps rather than wall-clock sleeps in unit
scenarios. For async component loading, wait for readiness instead of assuming one
pump is sufficient. Avoid unbounded pumpAndSettle for a continuously running game.
Derive tolerances from the mechanic; variable-step integration and cross-platform
floating point need not be bit-identical. Use fixed seeds to reproduce randomized
scenarios while also exercising additional seeds where random variation matters.

Useful invariants: one pickup awards once; cooldown prevents unintended repeated
hits; invalid actions preserve state; restart returns to the initial session state;
a removed component no longer receives input; persisted progress survives restart.

## Performance protocol

Use the same scene, device, build mode and workload before/after a change. Separate
cold loading from warmed steady-state behavior; retain both if startup is the issue.
At 60 Hz a frame interval is about 16.67 ms; at 120 Hz about 8.33 ms. These are frame
intervals, not a promise that each thread may consume the whole interval freely.
Record slow frames and distributions where available, not just average FPS.
Distinguish raster cost, Dart/UI cost, shader/loading hitches, GC and audio work.

Track repeated enter/exit cycles to investigate leaks. A stable-looking single heap
snapshot cannot prove absence of leaks. If the target device is unavailable, run
available correctness checks and report the missing performance measurement.

## Sources

Research baseline: 2026-09-30.
- https://docs.flutter.dev/perf/ui-performance
- https://docs.flutter.dev/tools/devtools/performance
- https://docs.flutter.dev/testing/overview
- https://pub.dev/packages/flame_test

## Persistence and packaged runtime checks

When saving progress is in scope, distinguish transient world state, settings and
critical durable progress. Verify behavior after a real cold start and after an
interrupted/failed write; use the storage system's actual guarantees. Shared preferences
is suitable for simple settings but does not guarantee durable storage for critical
data. Do not rewrite storage architecture as a side effect of an unrelated test.
A save schema change needs a previous-version fixture and a corrupt/missing-data path.

When testing assets/native plugins, exercise a built target as appropriate: debug hot
reload can conceal stale resources; browser hosting can expose path, case, CORS or
WASM problems. Audio startup may need a user gesture. Record what was simulated and
what ran against a real backend. Accessibility checks should cover relevant menu/HUD
focus, text scaling and semantic labels, plus gameplay cues that rely only on color
or sound. Visual goldens need controlled fonts, viewport and rendering environment;
review the image diff instead of regenerating baselines to erase an unexplained failure.

For automated performance captures, use the SDK's documented integration_test tracing
workflow when supported and save the trace/summary. Browser performance needs browser
instrumentation. A long session can expose memory/thermal effects missed by a brief
warm run; use a soak scenario when the reported issue concerns long play.

Additional sources checked 2026-09-30:
- https://docs.flutter.dev/cookbook/testing/integration/profiling
- https://docs.flutter.dev/cookbook/persistence/key-value
- https://docs.flutter.dev/ui/accessibility
