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

Request: Check this atlas before importing it.

Fixture: PNG plus JSON with a frame extending beyond the texture.

Evaluator checks: Helper fails with the named frame and offending geometry, without modifying either file.

## Case 2

Request: The run animation jitters after trimming.

Fixture: Trimmed frames with different offsets and an atlas-aware loader.

Evaluator checks: Original canvas/offset metadata is respected; preview verifies a stable pivot rather than padding blindly.

## Case 3

Request: Use a grid sheet; our loader cannot rotate frames.

Fixture: Packed atlas with rotated frames.

Evaluator checks: Rotation is surfaced; export/loader choice respects the constraint and is verified in-engine.

## Case 4

Request: Generate a standalone landscape illustration.

Fixture: Text-only art prompt, no game import requirement.

Evaluator checks: Image-generation workflow handles it; atlas checks and Flutter changes are not imposed.


## Case 5

Request: Import an animation with 80 ms and 200 ms frames and a reverse tag.

Fixture: Aseprite export plus the actual importer.

Evaluator checks: Preserves ordering, variable duration and reverse behavior; verifies millisecond conversion.

## Case 6

Request: Validate this supposedly untrimmed atlas.

Fixture: trimmed=false with sourceSize smaller than the packed frame.

Evaluator checks: Validator rejects contradictory geometry; does not silently certify the file.
