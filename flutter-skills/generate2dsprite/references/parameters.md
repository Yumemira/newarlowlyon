# Parameters and defaults

## Parameters

Infer these from the user request:

- `asset_type`: `player` | `npc` | `creature` | `character` | `spell` | `projectile` | `impact` | `prop` | `summon` | `fx`
- `action`: `single` | `idle` | `cast` | `attack` | `shoot` | `jump` | `hurt` | `combat` | `walk` | `run` | `hover` | `charge` | `projectile` | `impact` | `explode` | `death`
- `view`: `topdown` | `side` | `3/4`
- `sheet`: `auto` | `2x2` | `2x3` | `2x4` | `3x3` | `3x4` | `4x4` | `5x5` | `custom_grid` | `strip_1x3` | `strip_1x4`
- `frames`: `auto` or explicit count
- `bundle`: `single_asset` | `unit_bundle` | `spell_bundle` | `combat_bundle` | `line_bundle` | `hero_action_bundle` | `engine_atlas`
- `effect_policy`: `all` | `largest`
- `anchor`: `center` | `bottom` | `feet`
- `scale_strategy`: `fit` | `preserve`
- `scale_profile`: `none` | `create_from_accepted_action` | `reuse_existing`
- `margin`: `tight` | `normal` | `safe`
- `art_style`: pixel_art | clean_hd | pixel_inspired | retro_pixel | map_style | project-native
- `reference`: `none` | `attached_image` | `generated_image` | `local_file`
- `layout_guide`: `none` | `geometry` | `character_anchor`
- `runtime_contract`: `none` | `godot_sprite3d`
- `world_height`: desired in-engine subject height when a runtime contract is requested
- `prompt`: the user's theme or visual direction
- `role`: only when the asset is clearly an NPC role
- `name`: optional output slug

Read [references/modes.md](modes.md) when the request is ambiguous.

## Defaults

- `idle`
  - small or medium actor -> `2x2`
  - large creature or boss -> `3x3`
- `cast` -> prefer `2x3`
- `projectile` -> prefer `2x2` for short animated loops; use row strips only when the engine specifically requires a strip, and assemble that strip after QC when practical
- `impact` / `explode` -> prefer `2x2`
- `walk`
  - topdown actor -> `4x4` for four-direction walk
  - side-view asset -> `2x2`
- controllable hero or main player with multiple actions -> `hero_action_bundle`
  - generate one action per raw multi-row grid sheet, not as a raw `1x4` strip
  - attack/shoot/cast body sheets are body-only by default; wide slash arcs, muzzle flashes, projectiles, trails, dust, and hit impacts are separate FX/projectile/impact sheets
  - if the weapon must stay integrated and there is no separate FX layer, use `--scale-strategy preserve --align feet` instead of bbox-fit normalization
  - default 4-frame action grid is `2x2`
  - use `2x3` for 6-frame actions and `2x4`, `3x3`, `3x4`, or `4x4` for longer actions
  - do not generate a mixed-action raw `4x4`, `5x5`, or custom atlas
  - assemble the final atlas only as a deterministic delivery step if the game requires it
- `4x4`, `5x5`, and custom grids
  - use as raw generation only for one coherent long action sequence, canonical directional locomotion, prop packs, or tileset-like atlases
  - use as delivery atlases for mixed actions only after separate action sheets pass QC
- use `shared_scale` by default for any multi-frame asset where frame-to-frame consistency matters
- use `largest` component mode for hero/player body grids; use `all` for separate FX/projectile/impact sheets
- use `scale_strategy=preserve` for grounded hero/player melee attacks with integrated weapons or wide body poses that would shrink under bbox-fit normalization; use `fit` for normal compact sheets and FX

