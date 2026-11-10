---
name: building-sketch-guide
description: Build economical Blender massing sketches and consistent game views as structural guides for later illustrated building images. Use for rough building concepts, silhouette tests and race sets; detailed mesh production and exact reference-camera recovery are separate tasks.
---

# Building sketch guide

The deliverable is a clear architectural sketch that helps generate beautiful painted art later. Model the silhouette and spatial relationships, not the finished illustration.

- Read the project's current task card and camera preset. Inspect only relevant art references; prefer one small reference board for a set. Reuse known source paths and scripts. Do not reload research histories or all building skills.
  If the task names an approved racial architecture passport, read only that race's card and implement its massing, supports, roofs and openings in the sketch. Earlier PNG architecture does not override it. Keep different functions architecturally distinct; props alone cannot establish racial identity.
- Keep body, roof, entrance and major wings. Usually a handful of masses is enough; add a mass only if it changes silhouette or a meaningful overlap. Omit individual boards, bricks, spokes, fittings, shingles, vegetation and interior machinery. Distinguish races through proportions, roof shape and mass arrangement, not tiny accessories or recoloring one house.
- Reuse a saved camera. Record whether it is proposed or accepted. Norland-like means the project's elevated game view; do not invent an exact Norland calibration. Facade and sides are whole-model world rotations, with camera and scale fixed.
  Honor its `projection` field: ORTHO and PERSP both render 3D. When perspective is requested, preserve elevation/yaws and set lens/distance explicitly; do not silently force ORTHO in the renderer.
- Use the bundled renderer with compact JSON. Read [scripts/render.py](scripts/render.py) only when changing it. `--help` gives the schema. It makes box/gable/hip/vault/ellipsoid/cylinder/cone forms, saves editable scenes and renders requested yaws. Prefer a small batch over rewriting a generator.

```sh
/Applications/Blender.app/Contents/MacOS/Blender -b --factory-startup --python-exit-code 1 --python /Users/davidyolkin/.codex/skills/building-sketch-guide/scripts/render.py -- --config /absolute/sketch.json --out /absolute/output
```

- Use Workbench and modest resolution. A compact report checks rigidity and framing. Review the completed batch once on one shared-scale board and report likeness/geometry doubts. Do not enter repeated visual rerender/review loops; make further artistic revisions when requested. Fix blocking execution errors needed to produce the batch. Do not perform per-vertex projection proofs, dense ray grids, multi-fault audits or token telemetry on every design.
  Make the board with `python3 <this-skill>/scripts/board.py /absolute/output`; Pillow is needed outside Blender. The board preserves the common canvas scale.
- For handoff retain `.blend`, input JSON, guides and a short art brief: intended silhouette, wall/roof material families, style-reference path, focal feature. Treat guides as geometry, accepted project art as painting/style. Broad color areas suffice in the sketch. Do not present primitive renders as finished painted sprites. When actual raster generation is requested, use building-guide-paintover with imagegen and compare the result against these guides.
- Keep chat output to results and failures. Logs and numeric details stay in files. Token measurement is optional when requested: capture start/end once and distinguish context growth from cumulative input. Do not browse documentation, reread skills or inspect account/session logs solely to estimate routine work.

If a draft has a concrete roof/contact problem, open only the relevant construction reference in building-spatial-geometry. Camera fitting, architectural-detail production and material painting load their own skill only when that stage is actually requested.
