---
name: generate2dsprite
description: "Generate and postprocess general 2D game assets and animation sheets: pixel-art sprites, clean HD map props, creatures, characters, NPCs, spells, projectiles, impacts, props, summons, and transparent GIF exports. Use when Codex should infer the asset plan from a natural-language request, match a reference or map art style, call built-in `image_gen` for solid-magenta raw sheets, and use the local processor only for chroma-key cleanup, frame extraction, alignment, QC, and transparent exports."
---


# Generate2dsprite

Use this skill for self-contained 2D sprite or animation assets.

When a larger game or playable prototype needs sprites, use this skill for the visible sprite assets and keep runtime/game assembly separate. Do not replace requested sprite assets with code-drawn placeholders.

## Agent Rules

- Decide the asset plan yourself. Do not force the user to spell out sheet size, frame count, or bundle structure when the request already implies them.
- Do not pack unrelated actions into one raw generated sheet just to satisfy a `4x4`, `5x5`, or custom engine atlas. A raw generated sheet should represent one action family, one continuous sequence, one canonical directional locomotion sheet, or one prop/asset pack.
- For controllable heroes, main characters, and high-value player assets with multiple actions, generate separate per-action grid sheets first, QC each action, then deterministically assemble the engine-required atlas only after the grids pass visual review.
- For controllable heroes, main characters, and high-value player body actions, default attack/shoot/cast body sheets to body-only. Do not include large slash arcs, muzzle flashes, projectiles, impact bursts, detached dust, long trails, or wide detached FX in the body sheet. Generate those as separate `fx`, `projectile`, or `impact` sheets and layer them in the game.
- Only include wide attack FX in the same raw body sheet when the target runtime explicitly supports wider per-action cells plus per-action origin/anchor metadata. Otherwise, a wide FX bbox will force the body to shrink inside the fixed cell.
- When a grounded hero/player attack must keep an integrated weapon in the body sheet and there is no runtime FX layer, process it with `scale_strategy=preserve` and `align=feet` by default. This preserves raw-cell scale, translates frames to a shared feet line, and avoids bbox-fit shrinking from long swords, spears, weapon trails, capes, or wide melee poses.
- Write the art prompt yourself. Do not default to the prompt-builder script.
- Use built-in `image_gen` for every raw image.
- Do not create raw sprite art with Three.js, Canvas, SVG, HTML/CSS drawing, PIL shape drawing, procedural geometry, placeholder primitives, or code-rendered screenshots. Runtime code may display finished generated assets, and scripts may make layout guides or postprocess generated images, but requested sprite art must originate from built-in `image_gen`.
- When the user provides or implies a visual reference, use built-in image edit/reference semantics only after the reference image is visible in the conversation context. If the reference is a local file, call `view_image` first; do not rely on a filesystem path in the prompt as the visual reference.
- Do not force pixel art when the asset is a map prop for `$generate2dmap` or when the user/project requests a different style. Match the map or reference style first.
- Use the script only as a deterministic processor: magenta cleanup, frame splitting, component filtering, scaling, alignment, QC metadata, transparent sheet export, and GIF export.
- Do not use scripts to generate the creative image prompt. If a legacy prompt-builder command exists, treat it as historical compatibility only, not the normal skill workflow.
- Layout guides are allowed only as deterministic geometry references for image generation. They may show slot count, spacing, centering, and safe padding, but must never define the creative art direction.
- Treat script flags as execution primitives chosen by the agent, not user-facing hardcoded workflow.
- If a generated sheet touches cell edges, drifts in scale, or breaks a projectile / impact loop, either reprocess with better primitive settings or regenerate the raw sheet.
- Do not use raw single-row sheets such as `1x4`, `1x6`, `1x8`, or `1xN` for characters, players, controllable heroes, creatures, NPCs, enemies, summons, animated props, or any asset where a body/subject must stay centered. Single-row raw generation is too likely to drift horizontally and crop inconsistently.
- For animated body assets, use a multi-row grid by default: 4 frames -> `2x2`, 6 frames -> `2x3`, 8 frames -> `2x4`, 9 frames -> `3x3`, 12 frames -> `3x4` or `4x3`, 16 frames -> `4x4`.
- If a game engine needs a final single-row strip or mixed atlas, first generate and QC the action as a multi-row grid, then assemble the delivery strip/atlas deterministically.
- In every animated body grid prompt, require the subject body to stay centered in each cell, full body inside the central 60% to 70% safe area, consistent scale across cells, stable feet/bottom anchor line when applicable, and no limbs, weapons, hair, capes, dust, muzzle flashes, or detached FX crossing cell edges.
- For hero attack body prompts, explicitly require body height and body scale to match the accepted idle/run sheets, stable feet/bottom anchor, weapon kept close enough to avoid widening the body bbox, and no detached slash arc or screen-space attack effect.
- For elongated quadrupeds, serpentine creatures, and actors whose tail or attack extension nearly fills a cell, add a shared-silhouette-envelope contract to action prompts: keep the torso center fixed, keep every pose inside the same central 70% to 72% width/height box, tuck tails and long appendages inward, and express pounces or bites through in-place compression/extension instead of translating the whole body across the cell. "Generous margin" alone is not a reliable containment instruction for these silhouettes.
- For massive grounded bosses, lock the feet and pelvis against lateral translation in idle prompts. Express weight through vertical torso compression, chest/core pulse, shoulder settling, and secondary motion of attached ornaments; do not use whole-body left/right sway as the idle beat.
- For ground-contact environmental FX such as fire, write one explicit shared ignition/baseline coordinate into the prompt and forbid baked ground plates. Treat tip-height variation as animation, not anchor drift; visually verify the contact line and use an FX-specific anchor threshold instead of applying humanoid feet gates.
- For high-value grounded player/hero body actions, prefer a character anchor sheet when consistent scale or feet placement matters: repeat one accepted master frame at the intended size and feet line in every cell, then use that sheet as a scale/root template while asking built-in `image_gen` to change only the poses. Do not use a grounded anchor sheet for jumps, knockback, airborne motion, projectiles, or FX.
- For a multi-action character bundle, create one scale profile from an accepted idle or run sheet, then process every grounded body action with that profile. The profile locks output cell size, one shared raw-cell scale, anchor, trimming, and component rules across actions. Do not choose a new `fit_scale` per action.
- For map prop packs, classify props before choosing a grid. Square `2x2`, `3x3`, and `4x4` packs are only for compact props. Do not put platforms, floors, bridges, walls, ladders, gates, doors, long hazards, wide/tall props, collision-bearing objects, or tileset/strip pieces into square prop packs; use one-by-one, `1x3`/`1x4` strips, custom wide cells, or a tileset-like atlas instead.
- Keep the solid `#FF00FF` background rule unless the user explicitly wants a different processing workflow.


## Stage routes

Use [parameters/defaults](references/parameters.md) only to resolve request-specific options. Preserve user choices.

- Stage 1 — [Infer the asset plan](references/phase-1.md); read when executing this stage, not all stages upfront.
- Stage 2 — [Write the prompt manually](references/phase-2.md); read when executing this stage, not all stages upfront.
- Stage 3 — [Generate the raw image](references/phase-3.md); read when executing this stage, not all stages upfront.
- Stage 4 — [Postprocess locally](references/phase-4.md); read when executing this stage, not all stages upfront.
- Stage 5 — [QC the result](references/phase-5.md); read when executing this stage, not all stages upfront.
- Stage 6 — [Return the right bundle](references/phase-6.md); read when executing this stage, not all stages upfront.

## Resources

- `references/modes.md`: asset, action, bundle, and sheet selection
- `references/prompt-rules.md`: manual prompt patterns and containment rules
- `scripts/generate2dsprite.py`: postprocess primitive for cleanup, extraction, alignment, QC, and GIF export
- `scripts/make_anchor_layout.py`: repeat an accepted character frame into a fixed scale/root generation template
- `scripts/make_layout_guide.py`: create abstract geometry-only guides for prop packs and suitable grids
