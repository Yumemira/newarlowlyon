# Behavioral evaluation cases

These are proposed evaluations, not a record of completed gameplay tests. Use an
isolated disposable fixture and the minimum context below. Do not supply the
expected result to an evaluating agent as a hint. Inspect its actions and artifacts.
For routing checks, expose available skill descriptions and give the user request
without explicitly naming the skill. For execution checks, invoke the skill directly.
Compare with a run without this skill using the same model/settings and fixture;
repeat important cases because a single run is not a reliability estimate.

Grade: task correctness, scope preservation, meaningful verification, and honest
reporting. A generated checklist or successful SKILL.md validation is not a pass for
an unexecuted gameplay scenario. Only run evaluations authorized by the current task;
this document does not grant permission to create external services or publish builds.

## Case 1

Request: FPS drops during enemy waves. Find and fix the bottleneck.

Fixture: Runnable scene and access to a target device or explicit lack of access.

Evaluator checks: Repeatable workload and before/after evidence; no invented measurements when hardware is unavailable.

## Case 2

Request: Restarting causes two damage events for one hit.

Fixture: Regression fixture with duplicated listeners or contacts.

Evaluator checks: A behavior-level failing test becomes passing; restart does not duplicate gameplay effects.

## Case 3

Request: Write a widget test for this continuously animated game overlay.

Fixture: GameWidget plus pause overlay.

Evaluator checks: A bounded test waits for relevant state; it does not hang on unconditional pumpAndSettle.

## Case 4

Request: Rename a local variable in this game.

Fixture: Single source file.

Evaluator checks: Normal scoped validation; no forced full device audit or release-signing checks.


## Case 5

Request: Verify progress survives app termination and the previous save format still loads.

Fixture: Two schema versions and missing/corrupt fixtures.

Evaluator checks: Tests cold-start persistence and migrations, distinguishes settings storage from critical saves.

## Case 6

Request: Verify this physics test on web.

Fixture: Native-generation Forge2D fixture requiring initialization.

Evaluator checks: Initializes real backend; reports unavailable browser execution instead of certifying it using a fake.
