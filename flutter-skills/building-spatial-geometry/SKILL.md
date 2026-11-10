---
name: building-spatial-geometry
description: Construct and verify coherent building volumes, roofs, attachments and alternate views for illustrated game sprites using an explicit 3D blockout and fixed camera. Use for architectural geometry errors, floating roofs, inconsistent facades or buildings that change shape between orientations; preserve the project's painted style.
---

# Building spatial geometry

For rough silhouettes and image-generation guides, use $building-sketch-guide and stop here. Coarse masses and a visual framing/overlap check suffice. Load the construction/audit workflow below for a concrete geometry defect or detailed asset task, not automatically for every draft.

Use explicit volumes as the source of spatial truth; a plausible painting does not establish consistent construction. Preserve the accepted art style and existing assets. For a new functional building, establish its own design rather than inheriting the reference house footprint; use $building-design-diversity when appropriate. Identity preservation across yaws does not require unrelated building types to share a design. Blockouts here are construction guides, not substitutes for requested finished illustrated art.

## Game-view target

When the request concerns a shared settlement view or Norland-like top-side framing, establish the project camera/reference packet with $settlement-building-art-direction if available. Keep the default three-quarter visual goal separate from exact screen-horizontal/vertical headings. The bundled isometric study validates construction only; it does not establish the project camera. Record identity landmarks before rotations, particularly gable ends and the wall carrying the entrance.

## Construct

Inspect the project entrypoints and actual building references. Establish the camera first; use $calibrate-game-camera if available, or record the projection, world axes, elevation/azimuth, pixel scale and unresolved camera assumptions yourself.

Read [construction.md](references/construction.md) for wall/roof planes, face-local details and contacts. Write a compact building contract: footprint, wall/eave/ridge heights, roof types and pitches, overhang, attachments, openings, asymmetrical landmarks, ground pivot. Mark measured, inferred and designed dimensions separately. Hidden structure from one sprite is an assumption to keep consistent, not a recovered fact.

Build walls and roofs from shared dimensions. Place doors/windows in their wall's local coordinates. Group the complete building under a common world pivot and rotate the group; never regenerate independent geometry per view. Use actual depth rendering for intersecting forms; average face sorting cannot resolve all intersections. Curved/fantasy roofs still need coherent surfaces, contacts and cross-sections.

For alternate game orientations, read [rigid-rotation.md](references/rigid-rotation.md). Preserve physical dimensions and child attachment transforms; reject nonuniform compression, shear, mirrors and screen-space resizing as substitutes for rotation. Recompute depth/occlusion after each world yaw. The fixture now presents a facade-facing view, side, diagonal and a reverse diagnostic with one elevated camera. Its local entrance wall is +X; other buildings must define their own front. These views demonstrate the method, not a game's exact camera or step size.

The bundled Blender fixture is a runnable training/example scaffold for a rectangular gabled house with porch and chimney, not a universal house generator. Adapt its construction/audit to the actual architecture; do not shoehorn rounded or branching buildings into it.

```sh
<blender> -b --factory-startup --python-exit-code 1 \
  --python <skill>/scripts/build_fixture.py -- \
  --config <skill>/assets/house.json --out /absolute/qa-directory
```

Find the installed Blender through PATH or known application locations and inspect its version. The fixture was executed on Blender 5.0.1; other versions require capability checks. It chooses an available render engine by introspection. No live bridge or third-party Blender addon is required.

## Verify and paint

Read [quality-gates.md](references/quality-gates.md). Verify contacts on actual geometry, not only parameter declarations or axis-aligned bounds. Render the required orientations and an additional reverse/oblique diagnostic view. Keep scale/pivot/camera fixed, and compare landmark identity and dimensions. Inspect every image for impossible joins, omitted faces, z-fighting, clipping, and style drift. Numeric success alone cannot approve architecture or artwork.

Only after the neutral geometry works, apply materials/paint or pass its rendered guide to the image tool alongside the accepted style reference. Use the imagegen skill for raster generation/editing. Independently inspect the painted output against the guide; if it moves roof/wall landmarks outside the declared tolerances, correct it or retain the reliable render as a paintover base. Do not claim a prompt guarantees geometry. If repeated painting changes the construction, stop that route and report the unresolved defect.

Deliver editable geometry, camera/asset contract, consistent renders, actual QA report and defects still open. Do not overwrite approved production sprites with these studies or mark art accepted because geometry passed. Sources and the review of public skills: [sources.md](references/sources.md).
