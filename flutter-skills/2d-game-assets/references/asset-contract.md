# Asset contract

## Decide before export

Record only relevant facts: image format, dimensions, sheet layout, pixels per game
unit, filtering, pivot, animation names, frame durations and looping behavior.
A sprite's logical canvas and packed rectangle are different when trimming is used.
The renderer needs the untrimmed size and trim offset to keep a stable pivot.
Rotated packing is safe only if the consumer decodes the rotation convention.

Regular-grid loaders require cell dimensions and spacing consistent with the export.
Packed loaders use explicit frame rectangles. Do not silently replace one format
with the other. Verify whether names include file extensions and whether the loader
expects JSON hash or array frames. Test one animation before exporting an entire set.

## Export and rendering

Aseprite supports batch export, JSON data, tags, trimming, padding and edge extrusion.
Use the installed tool's help before choosing version-sensitive flags. Do not require
Aseprite if existing resources can be handled without it. Image generation edits
should use the supported image tool; this skill's helper only inspects metadata.
Padding/extrusion can reduce sampling artifacts but must agree with atlas coordinates.
Pixel art usually needs a deliberate nearest-neighbor/integer-scale policy; judge it
at target scale and during camera motion, not just enlarged in an image viewer.

A decoded RGBA8 image is approximately width * height * 4 bytes before additional
copies, mipmaps and engine overhead. Compressed file size is not GPU-memory use.
Measure the target workload before deciding atlas count or a texture-size budget.

## Validation helper scope

Accepted JSON: top-level `frames` as a name-to-record object, or an array of records
with `filename`; each record has integer `frame.x/y/w/h`. `meta.image` names a PNG
relative to the JSON file. Optional `meta.size`, `duration`, `rotated`, `trimmed`,
`sourceSize`, `spriteSourceSize` and `meta.frameTags` are checked when supplied.
An optional `--image` overrides the image path. Other fields are ignored, not certified.
The PNG check validates signature and IHDR metadata only; inspect actual decoded pixels
in the engine or image viewer. Shared rectangles are permitted for deduplicated frames.

## Sources

Research baseline: 2026-09-30; confirm the actual exporter and importer versions.
- https://www.aseprite.org/docs/cli/
- https://www.aseprite.org/api/command/ExportSpriteSheet
- https://github.com/flame-engine/flame (sprite and atlas bridge packages)

## Animation semantics and export coverage

Aseprite frame durations are milliseconds; Flame animation step times use seconds.
Preserve variable durations when present. Reverse/ping-pong tags need explicit playback
handling; do not assume an importer reads tags merely because it reads rectangles.
Do not alphabetically sort hash keys (frame_10 can precede frame_2). Prefer explicit
ordered frames; when interpreting indexed tags over a JSON hash, check that producer
and consumer preserve the same ordering. Empty frames can represent intentional
pauses or invisible poses; duplicate frames may intentionally share texture rectangles.

Verify whether the export contains multiple texture pages, scale variants, slices or
pivots outside the simple trim metadata. The helper checks one texture; it warns on
related_multi_packs and non-unit scale, and does not certify slice/pivot semantics.
For UI exports, inspect legibility at device scale and against actual backgrounds.
Do not silently crop original logical canvases to reduce file size.

Sources checked 2026-09-30:
- https://www.aseprite.org/docs/cli/ (JSON formats, list-tags, frame ranges, duplicates)
- https://docs.flame-engine.org/latest/flame/components/sprite_components.html
