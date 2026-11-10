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

Request: The jump feels floaty. Improve it without changing the level.

Fixture: Existing jump controller, target device and short test level.

Evaluator checks: A bounded parameter change, measurable apex/landing behavior, preserved level geometry and explicit playtest uncertainty.

## Case 2

Request: Prototype a card mechanic; no real-time action.

Fixture: Rules sketch and an existing Flutter screen.

Evaluator checks: A playable turn loop with legal/illegal action feedback; no forced Flame/physics dependency.

## Case 3

Request: Balance these two upgrades using the supplied session data.

Fixture: Upgrade formulas and real session observations.

Evaluator checks: Units and assumptions are explicit; proposed balance is distinguished from unmeasured enjoyment.

## Case 4

Request: Repair this missing asset path.

Fixture: A failing asset import.

Evaluator checks: This skill is not selected for a pure file-path repair.


## Case 5

Request: The game communicates danger only by red flashes and a sound. Improve readability.

Fixture: Existing mechanic and a request for accessible cues.

Evaluator checks: Adds a suitable alternate cue without inventing playtest results or replacing the mechanic.

## Case 6

Request: Players do not understand the first puzzle. Test whether the rules are clear.

Fixture: Puzzle prototype and an unassisted first-attempt script.

Evaluator checks: Separates rule comprehension from execution difficulty and defines evidence before tuning.
