---
name: clean-game-assets
description: Generate and prepare clean transparent 2D game sprites, props and animation sheets with safe cell margins, stable anchors and visual fringe checks. Use when the user wants asset quality like Last Lantern or complains about dirty edges, cropped poses, halos or frame jitter. Code-drawn glyphs and simple effects should stay vector/code based when that better fits the project.
---

# Clean Game Assets

Reproduce the asset preparation principles used for Last Lantern, while matching the current project's style and runtime. Do not promise artifact-free generation: inspect each result and reject broken sheets.

## Choose the source

- Raster characters, vegetation, rocks and painted effects: use the available built-in image generation tool; read its applicable imagegen skill/tool instructions. Inspect supplied local references before generating. Prefer native alpha (`transparent_background: true`) for isolated painted assets. A checkerboard painted into RGB is not transparency.
- Glyphs, thin geometric lines, moving light heads and simple glow effects: retain or build code/vector drawings when requested as game behavior. These avoid background fringe and support continuous animation. Do not substitute procedural drawings for requested illustrated sprite art.
- Opaque ground textures: do not remove their background. Read [terrain.md](references/terrain.md) when continuity or randomized tile placement matters.

## Generation contract

Separate each action into a small multi-row sheet (typically 2×2 for four frames or 3×2 for six). Fix the grid, row-major order, scale, camera angle, light direction and palette in the prompt. Keep the full subject within the central 60–70% of each cell, including wings and every animated pose; no object, lettering, separators or unrelated particles should cross cell boundaries. Split large halos/projectiles into independent FX assets rather than shrinking the character to fit them.

Use the accepted idle frame as a visual reference for subsequent actions. Keep grounded objects anchored at their base, airborne actors at a stable body landmark, and expanding effects at their intended origin. Preserve deliberate squash/stretch and flight motion. Do not normalize every frame independently by bounding-box size.

Preserve the unmodified generated sheet plus exact prompt, dimensions and source association. If limbs cross cells or strong pixels reach the boundary, regenerate or repack from intact isolated frames. Do not hide cropped anatomy with erosion or a mask.

## Export and inspect

Use the project's existing export mechanism. Maintain fixed frame rectangles, durations, row-major order and per-frame pivots. Resize the whole sheet with transparent-aware filtering; preserve integer frame boundaries. Atlas filtering requires transparent gutters or suitable extrusion, not sampling adjacent frames. Inspect downscaled exports, not just large originals.

Run the bundled read-only artwork audit (Pillow required; prefer the project's existing Python environment):

```bash
python3 <skill-dir>/scripts/audit_sheet.py PATH/character.png --cols 3 --rows 2 --out PATH/qa-character
```

Alternatively `--metadata PATH/character.json` reads the ordered frame rectangles. The audit emits JSON, RGBA memory estimates and contact sheets over dark, white, gray and magenta backgrounds. Read its exit status and report, then view the contact PNGs. It measures containment; it cannot decide whether artwork, anatomy, animation or anchors look right.

Review every frame at game scale: dark and bright fringes, stray islands, actual alpha, cell containment, consistent apparent body size, intended anchor and first/last loop continuity. Play the animation and inspect it in the real scene with lighting, camera and transparency compositing enabled.

Last Lantern had faint residual alpha at cell edges. A roughly 1.8% runtime gutter fade was acceptable there only after confirming that opaque subject pixels were outside that band. This is a project-specific fallback, not a universal cleanup threshold. Prefer correcting the export when possible; do not erase intended wings, smoke or glow. Native alpha is the default here; use chroma key only when the actual source requires it and inspect desaturated/magenta fringes afterward.

Deliver accepted files, frame/pivot metadata and QA evidence. Describe regeneration or any remaining jitter honestly. Follow existing engine lifecycle and asset-loading conventions; no new package or engine is needed solely for clean artwork.

Resolve `<skill-dir>` to this installed skill directory; helper paths are not relative to the application working directory.
