# Map contract

## Minimal schema decisions

Define semantic classes and typed properties only as needed. An example is a PlayerSpawn
point with a stable spawnId, and a LevelExit rectangle with targetLevel and targetSpawn.
These names are suggestions, not a universal schema. Reuse existing project names.
Specify whether multiple spawns are valid and how a default is selected; do not
universally enforce exactly one spawn on a multi-entry level.

Keep Tiled's generated numeric object IDs distinct from application-level identifiers
intended to survive content edits. Validate cross-level targets and required assets.
Use typed bool/int/float/file/object properties where the loader understands them.
Unknown optional decorative properties need not invalidate an otherwise usable map.

## Coordinates and paths

Object placement depends on shape, tile alignment, layer offsets, map orientation
and tileset settings. Do not assume every object uses a top-left origin. Test a
representative rectangle, polygon and tile object against rendered geometry.
External TSX/image/template paths can be relative to their owning file. Ensure nested
resources are included in the Flutter asset bundle. Preserve source file casing for
case-sensitive targets. Infinite maps/chunks require explicit importer support.

## Runtime checks

Validate spawn clearance, portal destination, camera bounds, draw ordering and collision
geometry in a tiny fixture before expanding a level. A JSON/XML parser accepting a
file does not prove its properties are interpreted correctly by the game engine.

## Sources

Research baseline: 2026-09-30; verify support in the resolved importer release.
- https://doc.mapeditor.org/en/latest/manual/custom-properties/
- https://doc.mapeditor.org/en/latest/manual/objects/
- https://doc.mapeditor.org/en/stable/reference/json-map-format/
- https://docs.flame-engine.org/latest/bridge_packages/flame_tiled/flame_tiled.html

## IDs, transformations and inheritance

A tile GID is local to its map, not a stable cross-level identifier. For custom raw
GID decoding, clear all four high flag bits before lookup, including the hexagonal
rotation bit in non-hex maps. Zero denotes an empty cell. Select the tileset with the
largest firstgid not exceeding the decoded GID, then derive its local tile ID.
Use the map orientation's transform order for both rendering and collision shapes;
do not strip flags and lose the visual transform. Existing importers may already do
this, so inspect their output before adding conversion.

Group layers contribute offsets/visibility and may nest. Resolve template defaults,
tileset properties and instance overrides according to the format/importer. If a
loader cannot resolve templates, use a supported detached export and verify equivalent
properties. Infinite-map chunks can start at negative tile coordinates; fixed map
width/height alone cannot define their playable bounds. Point spawn objects can have
zero dimensions, unlike rectangular collision regions. Distinguish class/type fields
and supported typed properties by export version rather than renaming every field.

Additional sources checked 2026-09-30:
- https://doc.mapeditor.org/en/stable/reference/global-tile-ids/
- https://doc.mapeditor.org/en/stable/reference/json-map-format/
- https://doc.mapeditor.org/en/latest/manual/using-templates/
