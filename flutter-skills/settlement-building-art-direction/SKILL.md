---
name: settlement-building-art-direction
description: Keep a settlement game's building sprites in a shared elevated three-quarter view, with consistent camera, scale and architectural identity across races and orientations. Use when assets look like unrelated product illustrations, a Norland-like overhead side view is requested, or a batch needs art-direction and cross-view review.
---

# Settlement building art direction

For rough massing/image-generation guides, use $building-sketch-guide and stop here. Reuse the project's saved camera and relevant style references; the detailed reference-packet/review workflow below is for actual art direction or final-set review, not every sketch.

Treat buildings as parts of one playable scene. A beautiful isolated illustration or correct generic isometric blockout does not establish the intended game view. Preserve the project's painted style. Preserve individual architectural identity across views of the SAME building; allow distinct architecture for different functions.

## Establish the visual target

Read the project's art/research entrypoint, relevant plan and actual source PNGs. Inspect the requested building and a diverse sample (straight gable, organic roof, round/dome and different races). Compare original and alternate views; previous contact sheets may have independently resized thumbnails and hidden scale problems. An approved palette is not approval of the camera or every existing sprite.

When Norland is the reference, inspect gameplay screenshots from an official gallery, distinguish camera observations from exact inferred angles, and preserve source URLs. “Top-side, roughly three-quarter” specifies a visual goal, not automatically true isometry, a 2:1 diamond, 45° camera elevation or two visible wall planes in every possible rotation. Do not import another game's architecture or claim its camera matrix from visual memory.

Read [camera-contract.md](references/camera-contract.md) to separate global camera, object yaw and screen alignment. Use $calibrate-game-camera for actual measurement if available. If its canonical solver is degenerate for a near-axis-aligned view, use more evidence/an appropriate model; never invent a fit or rotate the artwork to satisfy it.

## Architectural variety

Use $building-design-diversity when different functions repeat the same house or need richer material treatment. Keep camera/brushwork coherent while allowing different footprints, roof systems, structure and finish. Mark reference houses as examples of rendering language rather than mandatory designs. Cross-view identity constraints apply within each building, not across unrelated functions.

## Define a small reference packet

For reusable resource/functional props or a requested front/side/diagonal review, read [spatial-prop-kits.md](references/spatial-prop-kits.md). A set of four diagonal headings is not a substitute for explicitly named front, side and diagonal views. Modular 3D props improve placement/depth control; keep per-building architectural invention and verify final painted exports separately.

Save one candidate camera/scene contract, named world axes, canvas/pixel scale/pivot, accepted style examples and per-building identity landmarks. Label unresolved values as unknown or proposed. Match the camera before accepting a pilot; do not batch-generate other races first. Supply reference roles explicitly: gameplay image for view, project art for painting/materials, structural guide for geometry. One picture should not silently override all roles.

Read [view-identity.md](references/view-identity.md) before generating rotations. Use $building-spatial-geometry for a persistent blockout when needed. Compare gables, entrances, wing attachment and chimney position in local building coordinates, allowing proper occlusion in each view. A roof's visible area alone cannot identify camera elevation; roof pitch, yaw and dimensions also affect it.

## Review the set

Run `python <skill>/scripts/review_set.py manifest.json --out /absolute/review` to create side-by-side boards and file evidence. See the script docstring for manifest format. Pillow is required. The same source-image factor is used for every canvas; this is NOT verified world scale. Missing views stay missing. Do not treat `review-required` as a pass.

For exploratory color/value/silhouette size studies, run `python <skill>/scripts/review_readability.py manifest.json --out /absolute/study`. Its manifest contains root and items with label/path. It independently fits assets to probe boxes and cannot verify world scale. Use $stylized-building-materials for unclear material response or excessive surface noise when available.

Read [handoff-and-review.md](references/handoff-and-review.md). Review individual buildings AND a shared scene at intended gameplay zoom. Separate camera mismatch, identity/geometry drift, style drift and export defects so the correction targets the actual cause. Inspect alpha on neutral backgrounds; a viewer's black backdrop or latent RGB gradient does not prove a background defect.

Deliver the camera/reference packet, a pilot or inspection evidence, identified defects and remaining unknowns. Existing production files stay intact unless their correction is requested. Skill preparation and inspection do not imply artistic acceptance, corrected PNGs, or permission to message other chats.
