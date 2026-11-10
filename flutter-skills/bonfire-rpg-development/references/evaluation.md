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

Request: Fix this movement bug in our Bonfire 3.x project without upgrading.

Fixture: Locked 3.x app and a movement regression.

Evaluator checks: Uses the installed API, preserves dependency versions and tests the bug.

## Case 2

Request: Add a melee enemy to our Bonfire 4.x project.

Fixture: 4.x app with player and collision map.

Evaluator checks: Uses compatible feature APIs, respects cooldown, handles target removal and unreachable positions.

## Case 3

Request: Add an exit to the next map and preserve quest progress.

Fixture: Two maps and existing progress storage.

Evaluator checks: Exactly one transition, valid target spawn, preserved domain progress and cleaned-up old scene.

## Case 4

Request: Build a Flutter card hand with drag and drop.

Fixture: No Bonfire dependency or RPG requirement.

Evaluator checks: Does not introduce Bonfire for a non-RPG task.


## Case 5

Request: An enemy takes a path through a wall just outside the camera.

Fixture: 4.x pathfinding with filtered barrier queries.

Evaluator checks: Checks visibility-filter configuration and tests camera movement without conflating visibility and walkability.

## Case 6

Request: Closing a quest dialog attacks the NPC and sometimes awards twice.

Fixture: Dialog input plus completed-quest/save fixtures.

Evaluator checks: Consumed input does not leak; reward semantics survive reopening and reloading.
