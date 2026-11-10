# Write the prompt manually

Paths/commands below are relative to the skill root, not this references directory.

### 2. Write the prompt manually

Use [references/prompt-rules.md](prompt-rules.md).

Choose `art_style` before writing the prompt:

- Use `pixel_art` or `retro_pixel` for classic sprites, 16-bit RPG actors, and requests that explicitly ask for pixel art.
- Use `clean_hd` for map props or assets intended to match clean hand-painted HD maps.
- Use `pixel_inspired` only when the user wants a pixel-adjacent look without retro chunkiness.
- Use `map_style` or `project-native` when an existing map, game, or reference should define the style.

If a reference is involved:

- Make the reference visible first. For local paths, use `view_image`; for freshly generated references, rely on the image already shown in context.
- State the reference role explicitly: preserve identity/style, create an animation sheet for the same subject, create an evolution/variant, or derive a matching prop/FX.
- Preserve the stable identity markers from the reference: silhouette, palette, face/eye features, costume marks, major accessories, and material language.
- Let only the requested action or evolution change. Do not redesign the subject unless the user asks.
- Still require exact sheet shape, solid magenta background, frame containment, and same scale across frames.

Keep the strict parts:

- solid `#FF00FF` background
- exact sheet shape
- same character or asset identity across frames
- same camera distance and standing-equivalent anatomical scale across body frames; natural pose bboxes may change, but the model must not zoom individual poses
- explicit containment: nothing may cross cell edges

Mixed-action atlas guardrail:

- Do not ask `image_gen` to generate unrelated action rows in one raw sheet, such as `row 1 idle, row 2 run, row 3 shoot, row 4 jump`, for a controllable hero or main character.
- Do not ask `image_gen` to generate raw single-row action strips such as `1x4 idle`, `1x4 run`, `1x4 shoot`, or `1x4 jump` for a controllable hero, character, creature, NPC, enemy, summon, or animated prop.
- If an engine needs a combined `4x4`, `5x5`, custom atlas, or row-strip delivery format, generate the action grids separately, process and QC them separately, then assemble the delivery atlas deterministically.
- Exceptions are canonical directional locomotion sheets, one continuous long action sequence, prop packs, tileset-like atlases, and low-stakes compact enemy combat sheets. These still need one coherent prompt and visual QC.
- Keep projectile, muzzle flash, impact, dust trails, and detached FX in separate sheets unless they are intentionally part of the same action silhouette and remain tightly attached.
- For controllable heroes and main characters, "tightly attached" is not enough when the effect makes the action bbox much wider or taller than idle/run. Split wide slash arcs, muzzle flashes, long weapon trails, dust clouds, and impact bursts into separate FX sheets by default.

Animated body grid guardrail:

- `1x4` and other raw single-row sheets are not valid defaults for animated bodies. This includes players, controllable heroes, creatures, NPCs, enemies, summons, animated props, and body-attached combat actions.
- Use `2x2` for 4-frame body actions. This is the default for idle, short attack, shoot body, jump, hurt, hover, and compact side-view walk/run actions.
- Use `2x3` for 6-frame body actions such as cast, attack, summon, run, charge, or transformation.
- Use `2x4`, `3x3`, `3x4`, or `4x4` for longer body actions. Prefer a compact grid over a long row.
- For 4-direction top-down walk, `4x4` can remain a raw generation shape because it is a canonical directional locomotion sheet, not four unrelated action rows.
- If final runtime needs a row strip, assemble it after QC from the processed multi-row grid frames.
- Keep the character centered in every cell. The body centerline should stay near the cell center, feet/bottom anchor should stay on the same y-position when visible, and the subject should occupy only the central safe area with generous magenta padding.
- For attack, shoot, cast, charge, and other body actions, the body height should stay close to the accepted idle/run body height. If a fixed-cell runtime is being used, reject body-action output when the body appears more than about 10-15% smaller than idle/run, even if `edge_touch_frames` is empty.

Map prop pack guardrail:

- Use square `2x2`, `3x3`, and `4x4` raw prop packs only for compact props such as rocks, shrubs, barrels, crates, lamps, small signs, pots, debris, and small ornaments.
- Do not use square prop packs for wide or collision-critical map objects: floors, platforms, ledges, terrain chunks, bridges, wall runs, ladders, roads, rails, pipes, long spike traps, gates, doors, buildings, large trees, checkpoints, exits, or build pads.
- Use one-by-one generation for unique, large, important, tall, irregular, or collision-aligned props.
- Use `1x3` or `1x4` strips for repeatable platform/floor assets, with left cap, middle repeat, right cap, and optional slope/corner/end variant.
- Use custom wide cells for multiple similar wide objects. The grid must state explicit non-square cell dimensions and must not mix compact props with platform/terrain objects.
- If a square prop pack fails due to edge touch or bad cropping, do not solve it by relaxing QC. Reclassify the object and regenerate with a more suitable sheet shape.

If a layout guide is useful, generate one before calling built-in `image_gen`:

```bash
python3 <skill-dir>/scripts/make_layout_guide.py \
  --rows <rows> \
  --cols <cols> \
  --cell-width 384 \
  --cell-height 384 \
  --output <run-dir>/references/<rows>x<cols>-layout-guide.png
```

Then make the guide visible in the conversation context and tell `image_gen` to use it only for invisible slot count, spacing, centering, and safe padding. The output must not reproduce guide boxes, safe-area rectangles, center marks, labels, borders, or guide background.

Use layout guides deliberately:

- recommended for `prop_pack_3x3`, `prop_pack_4x4`, tileset-like atlases, fixed multi-row animation grids, and non-directional 16-frame action sequences such as casting, summoning, charging, death, or transformation
- optional for `3x3` large idle and high-value showcase loops when previous generations drift in scale or spacing
- not the default for `4x4` four-direction walk sheets, because the guide can make directional poses too conservative; use it only after an unguided run fails layout or edge safety

For grounded high-value character actions, an abstract box guide is weaker than a character anchor sheet. After accepting a neutral/idle master frame, create the anchor sheet:

```bash
python3 <skill-dir>/scripts/make_anchor_layout.py \
  --input <accepted-master-frame.png> \
  --rows 2 \
  --cols 3 \
  --cell-width 512 \
  --cell-height 512 \
  --subject-height-ratio 0.66 \
  --feet-ratio 0.82 \
  --output <run-dir>/references/attack-anchor-2x3.png
```

Make both the master frame and anchor sheet visible to built-in `image_gen`. State that the master locks identity/style and the anchor sheet locks slot positions, camera distance, standing-equivalent scale, body root, feet line, and padding. Ask the model to change only the action poses and never reproduce guides, borders, labels, or separators.

