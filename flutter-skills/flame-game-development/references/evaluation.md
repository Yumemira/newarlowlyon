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

Request: Implement a collectible in this Flame scene; restarting the level must reset it.

Fixture: A fixture with a player, two hitboxes and a restart button.

Evaluator checks: The item increments score once, disappears, and is restored once on restart; repeated restarts do not add listeners.

## Case 2

Request: Fix movement that continues after switching browser tabs.

Fixture: Existing keyboard movement code and a runnable web target.

Evaluator checks: Input cancellation/focus handling resets held actions; normal input still works after return.

## Case 3

Request: Make clicks select the world tile while the camera is zoomed.

Fixture: A map, zoomable camera and screen-space pointer code.

Evaluator checks: Selection matches the same visible tile across resize, zoom and camera movement.

## Case 4

Request: Change the label on the Flutter settings button.

Fixture: An application that also happens to depend on Flame.

Evaluator checks: This skill is not selected solely because Flame is a dependency; no game architecture changes.


## Case 5

Request: Keep the game paused after returning from the background while the pause menu is open.

Fixture: User pause plus app lifecycle changes.

Evaluator checks: Foregrounding does not clear user pause; audio policy is checked separately.

## Case 6

Request: Two fingers control movement and attack; cancelling attack stops movement too.

Fixture: Independent touch controls and pointer cancellation.

Evaluator checks: Only the cancelled pointer is released; local event coordinates are not transformed twice.
