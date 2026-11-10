# Infer the asset plan

Paths/commands below are relative to the skill root, not this references directory.

### 1. Infer the asset plan

Pick the smallest useful output.

Examples:

- controllable hero with four directions -> `player` + `player_sheet`
- side-view controllable hero with idle/run/shoot/jump -> `player` + `hero_action_bundle`
  - idle grid sheet, usually `2x2` for 4 frames
  - run grid sheet, usually `2x2` or `2x3` depending on needed frame count
  - shoot grid sheet with body/weapon only, usually `2x2`
  - jump grid sheet, usually `2x2`
  - projectile / muzzle flash as separate assets when needed
  - optional assembled engine atlas after per-action QC
- side-view controllable hero with melee attack -> `player` + `hero_action_bundle`
  - attack body grid sheet, usually `2x2` or `2x3`, body-only
  - slash arc / weapon trail as a separate `fx` sheet when the attack needs a wide visual effect
  - impact spark as a separate `impact` sheet when hits need feedback
- healer overworld NPC -> `npc` + `single_asset` or `unit_bundle`
- large boss idle loop -> `creature` + `idle` + `3x3`
- wizard throwing a magic orb -> `spell_bundle`
  - caster cast sheet
  - projectile loop
  - impact burst
- monster line request -> `line_bundle`
  - plan 1-3 forms
  - per form, make the sheets the request actually needs

