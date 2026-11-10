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

Request: Remove a projectile when it hits a wall.

Fixture: Fixture with contact callbacks during a physics step.

Evaluator checks: Removal respects lock/lifecycle rules and scores once even with multiple fixtures.

## Case 2

Request: The ball moves differently at different display refresh rates.

Fixture: Existing Forge2DGame with custom stepping code.

Evaluator checks: Finds actual stepping owner; fixes timing without stepping the same world twice.

## Case 3

Request: Make a moving platform carry the player.

Fixture: Existing physical player and platform.

Evaluator checks: Body/contact choices are explained and verified without arbitrary per-frame teleports of dynamic bodies.

## Case 4

Request: Add coin pickup detection to this simple Flame game.

Fixture: Nonphysical game with existing hitboxes.

Evaluator checks: Does not add Forge2D solely for overlap detection.


## Case 5

Request: Contacts stopped firing after overriding createBody in flame_forge2d 0.20.

Fixture: Custom shape construction in the native generation.

Evaluator checks: Uses shape event flags and current callbacks; no legacy FixtureDef repair.

## Case 6

Request: Repeatedly open and permanently close physics game sessions.

Fixture: Native worlds with defined temporary removal versus final teardown.

Evaluator checks: Initializes once as appropriate and destroys final worlds without breaking temporary remounts.

## Case 7

Request: After migration, bodies fall through a chain and friction changed.

Fixture: 0.19-to-0.20 fixture preserving old intended behavior.

Evaluator checks: Checks chain winding, material defaults and physical/render scale using the migration guide.
