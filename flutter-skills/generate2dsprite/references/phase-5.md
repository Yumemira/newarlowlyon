# QC the result

Paths/commands below are relative to the skill root, not this references directory.

### 5. QC the result

Check:

- did any frame touch the cell edge
- did any frame resize differently than intended
- did detached effects become noise
- does the sheet still read as one coherent animation
- for hero/player body actions, does the body height match the accepted idle/run scale within roughly 10-15%
- for fixed-cell runtimes, did a wide weapon trail or FX arc shrink the body inside the cell
- for preserve-scale runs, are feet/bottom anchors aligned without any `paste_clamped` frames
- for grounded high-value body sheets, does `qc_summary.body_scale_cv` stay at or below about `0.08` and `qc_summary.anchor_y_std` at or below about `0.05`
- for rooted boss idles, do the feet and pelvis remain fixed while motion comes from compression, glow, shoulders, and attached secondary elements
- for ground-contact FX, is the authored ignition/baseline stable even when flame tips, embers, or effect height change
- for multi-action bundles, does `qc_summary.profile_body_scale_drift` stay within the scale profile limit, normally `0.08`

If not, rerun with different processor settings or regenerate the raw sheet.

Strict QC distinguishes raw source-cell contact from processed output contact. Prefer regeneration when a body part is visibly clipped. If visual review confirms the raw subject is complete and only an antialiased or harmless contour touches the source-cell boundary, use `--allow-source-edge-touch`; it never permits output-edge contact, paste clamping, or empty frames.

For elongated creature attacks, any `paste_clamped_frames` or `output_edge_touch_frames` means the raw sheet must be regenerated with the shared-silhouette-envelope contract above. Do not use `--allow-source-edge-touch` until clamp and processed-output edge contact are both zero and visual review confirms the full snout, paws, weapon, wings, or tail are intact.

For grounded high-value humanoid player/hero body actions, run strict QC after generation-first scale control:

```bash
python3 <skill-dir>/scripts/generate2dsprite.py process \
  --input <raw-sheet.png> \
  --target player \
  --mode attack \
  --output-dir <out-dir> \
  --rows 2 \
  --cols 3 \
  --align feet \
  --scale-strategy preserve \
  --component-mode largest \
  --strict-qc \
  --max-body-scale-cv 0.08 \
  --max-anchor-y-std 0.05
```

These numeric gates are for grounded humanoid body actions, not jumps, knockback, projectiles, impacts, floating actors, creatures whose attack strongly changes silhouette/posture, or intentionally changing-scale FX. A failed gate is a regeneration signal; do not hide generation drift with per-frame scale normalization.

For ground-contact FX, prefer `component_mode=largest` when detached embers would corrupt the contact anchor. Accept a looser action-specific `max_anchor_y_std` only after visual review confirms a fixed baseline, zero output-edge contact, zero paste clamping, and correct in-engine placement. Do not loosen the grounded-character defaults globally.

Cross-action scale-profile drift is a generation QC signal. Preserve legitimate crouching, recoil, and compressed pose bboxes; inspect borderline hurt or knockback sheets visually instead of applying per-frame resize. For ordinary idle, run, walk, and grounded body attacks, reject unexplained profile drift.

