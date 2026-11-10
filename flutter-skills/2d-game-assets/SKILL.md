---
name: 2d-game-assets
description: "Prepare and integrate 2D game sprites, animation sheets and texture atlases. Use for game-asset export or validation; standalone illustration generation belongs to an image tool."
---

# 2D Game Assets

Deliver assets and metadata that the game's actual loader can consume. Read
[Asset contract](references/asset-contract.md) before choosing an export layout.

## Workflow

1. Inspect source artwork, loader, target platforms and existing asset conventions.
   Establish frame dimensions, coordinate origin, pivot, animation names/durations,
   pixel-art filtering and the supported atlas schema.
2. Preserve editable originals. Generate exports into the project's established
   destination; do not overwrite the sole source image or edit generated Dart files.
3. Choose regular grid sheets for a grid loader, or packed atlases only when the
   loader supports their trimming/rotation metadata. Keep collider geometry explicit
   rather than automatically deriving gameplay hitboxes from every visible pixel.
4. For new bitmap artwork, use the available image-generation skill/tool if applicable.
   Inspect the result; matching characters, seamless tiles and animation continuity
   are verification tasks, not guaranteed properties of a generated image.
5. Check metadata and file references, then inspect the animation inside the actual
   game at intended scale. Look for pivot jitter, edge bleeding, clipping and blur.

## Read-only atlas check

For Aseprite/TexturePacker-style JSON hash or array frames referencing a PNG image:

```sh
python3 <skill-dir>/scripts/check_atlas.py /absolute/path/atlas.json
```

Resolve `<skill-dir>` to this skill's installed directory. The helper uses the Python
standard library, never edits assets and exits nonzero on malformed data. It checks
PNG dimensions, frame bounds, trim geometry, durations when present, and animation
tag ranges, including contradictory untrimmed geometry. It warns on packed rotation,
multipage/scale metadata and hash-frame ordering because loader support must be verified.
It does not decode PNG pixels, detect visual seams, enforce a GPU memory budget or
prove compatibility with an arbitrary loader. See its `--help` for the supported scope.
For another atlas format, inspect its schema instead of forcing it through this helper.

## Playback semantics

Preserve exported frame order, per-frame duration and tag direction/repeat semantics.
Convert Aseprite milliseconds to the runtime's expected time unit explicitly. Atlas
packing order or alphabetical frame names are not an animation timeline. Validate
empty/duplicate frames and multipage atlas support against the importer. A warning
from the helper requires a loader-specific decision, not a claim of full compatibility.

## Delivery

Report source/export locations, import format, checks performed and any visual work
still unverified. Keep provenance/license information for third-party assets when
available. Never invent permission or license terms for a downloaded asset.

Use [Evaluation cases](references/evaluation.md) when testing this skill itself.
