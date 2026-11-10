# Return the right bundle

Paths/commands below are relative to the skill root, not this references directory.

### 6. Return the right bundle

For a single sheet, expect:

- `raw-sheet.png`
- `raw-sheet-clean.png`
- `sheet-transparent.png`
- frame PNGs
- `animation.gif`
- `prompt-used.txt`
- `pipeline-meta.json`
- optional `godot-sprite3d.json` when `--godot-world-height` is supplied
- `godot-sprite3d-bundle.json` for a multi-action Godot unit

For `player_sheet`, expect:

- transparent 4x4 sheet
- 16 frame PNGs
- direction strips
- 4 direction GIFs

For `spell_bundle` or `unit_bundle`, create one folder per asset in the bundle.

For `hero_action_bundle`, expect:

- one raw and processed sheet per action
- per-action frame PNGs and GIFs for visual QC
- separate projectile / muzzle / slash / impact assets when the hero shoots, casts, or uses wide melee effects
- optional assembled `engine-atlas-transparent.png` only after per-action QC passes
- one shared `character-scale-profile.json` for grounded body actions when cross-action scale consistency matters

