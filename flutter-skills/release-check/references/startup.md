# Startup

## App placement

Require the entire app initialization tree inline inside `runApp(...)`, called
 directly by `main()` in `lib/main.dart`: ScreenUtilInit, providers,
MaterialApp/CupertinoApp/WidgetsApp, routing and other app wrappers. Choose nesting
according to component APIs. `runApp(MyApp())`, a variable or an external factory
is not allowed, even when the App class is in main.dart. Screens and business logic
may remain separate. Inspect `app_main` findings and manually verify completeness
and reachability. Keep the static-scan warning visible after manual review.


## Mandatory loading and onboarding

Every application must have a reachable animated loading screen/state and onboarding.
Verify onboarding on a fresh install or with first-launch state reset, including
completion and the transition into the application. Unreachable widgets or unused
routes do not satisfy either requirement.

Loading must **definitely not be instantaneous**: it must remain visibly on screen
for a perceptible interval even when initialization completes immediately or data
is cached. Require an explicit minimum display duration in the startup flow; a
single frame, immediate redirect, or dependence solely on network/device speed
does not pass. Verify both the duration guard in code and the observed startup
behavior, including a fast/cached launch. A native splash alone does not prove
that this requirement is met.

Visually verify that the loader animation actually plays on the first screen;
an animation declaration in source is insufficient. The script does not check
animation playback. Missing animation is `FAIL`; unavailable runtime observation
is incomplete verification.

Report missing onboarding, missing loading, or instantaneous loading as `FAIL`.
If runtime verification is unavailable, report that coverage as incomplete rather
than claiming a pass from source inspection alone. These are additional manual
checks; report their results separately from the script's JSON counts and exit
code unless the script explicitly implements them. For check-only requests,
report violations without modifying the application.

