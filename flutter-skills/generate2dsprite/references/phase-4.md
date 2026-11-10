# Postprocess locally

Paths/commands below are relative to the skill root, not this references directory.

### 4. Postprocess locally

Run `<skill-dir>/scripts/generate2dsprite.py process` on the raw image.

The processor is intentionally low-level. The agent chooses:

- `rows` / `cols`
- `fit_scale`
- `align`
- `shared_scale`
- `component_mode`
- `component_padding`
- `scale_strategy`
- `edge_touch` rejection strategy

Use the processor to gather QC metadata, not to make aesthetic decisions for you.

For hero action bundles, process each action grid as its own sheet before any final atlas assembly. Use `component_mode=largest` for body-only hero grids. Use `component_mode=all` only for projectile, impact, aura, slash FX, or intentionally detached FX sheets, not for fixed-cell hero body attacks that need stable body scale.

Use `--scale-strategy preserve --align feet` for grounded hero/player body sheets when the raw art already has acceptable scale but bbox-fit would shrink the character because of a long weapon, extended pose, cape, or integrated melee effect. Preserve mode applies one uniform raw-cell-to-output scale to every frame, including one shared safety margin, then translates each detected subject to the shared anchor. It never applies a different bbox-fit scale per frame. Use the default `fit` strategy for compact bodies, creatures, projectiles, impacts, and intentionally normalized FX.

For a character with multiple actions, write a scale profile only after an accepted reference action passes QC:

```bash
python3 <skill-dir>/scripts/generate2dsprite.py process \
  --input <accepted-run-raw.png> \
  --target player --mode run --rows 2 --cols 3 \
  --output-dir <run-dir> \
  --cell-size 128 --fit-scale 0.80 \
  --align feet --scale-strategy preserve --component-mode largest \
  --strict-qc --write-scale-profile <bundle>/character-scale-profile.json \
  --profile-name <character-name> --max-profile-scale-drift 0.08
```

Process later actions with `--scale-profile <bundle>/character-scale-profile.json`. Profile values override per-command scale, anchor, trim, and component defaults so actions cannot silently use different output magnification. Keep using the same generation grid geometry and character anchor sheet when possible; a processing profile cannot repair a model-generated anatomy-scale change.

When integrating a processed grid as a Godot `Sprite3D`, request a world-height contract instead of hand-tuning each action in the game:

```bash
python3 <skill-dir>/scripts/generate2dsprite.py process \
  --input <raw-sheet.png> \
  --target player --mode idle --rows 2 --cols 3 \
  --output-dir <action-dir> \
  --cell-size 256 --fit-scale 0.84 \
  --align feet --scale-strategy preserve --component-mode largest \
  --strict-qc --max-body-scale-cv 0.08 --max-anchor-y-std 0.05 \
  --duration 125 --godot-world-height 0.70
```

This writes `godot-sprite3d.json` beside the frames. The reference action derives `recommended_pixel_size` from the QC-measured mean subject height and stores it in the scale profile. Later actions processed with that profile reuse the exact pixel size, so crouching, recoil, hurt, and creature silhouette changes remain real pose changes instead of being normalized back to the reference height. The contract also converts the shared output origin to Godot's `Sprite3D.offset`, lists animation frames, and records timing. Reuse the same `world_height` and scale profile for every compatible action in one bundle.

After all actions pass QC, build one Godot animation bundle:

```bash
python3 <skill-dir>/scripts/generate2dsprite.py build-godot-bundle \
  --action idle=<bundle>/idle/godot-sprite3d.json \
  --action move=<bundle>/move/godot-sprite3d.json \
  --action attack=<bundle>/attack/godot-sprite3d.json \
  --action hurt=<bundle>/hurt/godot-sprite3d.json \
  --default-action idle --one-shot attack --one-shot hurt \
  --output <bundle>/godot-sprite3d-bundle.json
```

The bundle validates cross-action world height and `pixel_size`, stores relative contract paths, and declares loop versus one-shot playback. Treat a bundle drift failure as an asset-generation or wrong-profile error; do not compensate with per-action runtime scale.

