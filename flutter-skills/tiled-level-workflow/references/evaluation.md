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

Request: Add a second entrance to this level.

Fixture: Map with one entrance and an existing spawn-ID schema.

Evaluator checks: Second entrance is selectable; validator does not enforce an invented single-spawn rule.

## Case 2

Request: Fix collisions shifted below the visible tiles.

Fixture: Tile objects with non-default alignment/layer offsets.

Evaluator checks: Collision matches actual rendered geometry; offset is derived from format rather than a magic correction.

## Case 3

Request: Load this map with an external tileset.

Fixture: Nested TMX/TSX/image paths and a Flutter project.

Evaluator checks: All resources resolve in the built app; errors identify a missing resource.

## Case 4

Request: Change HUD text color.

Fixture: Game using Tiled but no map changes.

Evaluator checks: Map workflow does not activate merely because Tiled is present.


## Case 5

Request: A flipped tile from our second tileset has the wrong collision.

Fixture: Multiple tilesets, high-bit GID flags and matching geometry.

Evaluator checks: Resolves local ID and applies the same transform to collision once.

## Case 6

Request: Load a point spawn in a negative-coordinate map chunk.

Fixture: Supported infinite map with zero-size point object.

Evaluator checks: Preserves negative origin and accepts valid point geometry; does not assume finite-map dimensions.
