---
name: building-guide-paintover
description: Turn existing 3D building guides into polished raster art in the user's selected style, with bounded generation calls and a visual geometry check. Use when the render determines architecture/camera and another image determines painting style; not for building the 3D model or inventing a new design.
---

# Building guide paintover

Edit the guide into a finished illustration. Geometry comes from the guide; the user's chosen example controls style. Prompts/reference images do not provide a hard geometry lock.

## Minimal packet

Read only the task, this skill and the built-in imagegen execution rules. Reuse the existing `.blend`/view PNGs, camera/yaws and one user-selected style image. Do not reload building research, rebuild architecture or read every art skill. If the style choice is already established, use it without asking again. A prior experiment is not automatic style approval.

When the task supplies an approved racial architecture passport, include a short observed/implemented summary in the image prompt: structural character, roofs/openings, material/finish cues. The 3D guide must already embody its major forms; do not invent passport masses during paintover. Earlier art may supply brushwork but not override the passport with its old architecture. Small profession cues supplement, not replace, this racial identity.

Inspect inputs once. Check the named entrance wall/yaws and whether roofs/overlaps are unambiguous. Report a concrete guide defect instead of letting the image model invent its repair. For unclear flat guides, reuse [scripts/guide.py](scripts/guide.py): it renders neutral masses with object outlines from the same scene/camera. Its `--help` describes use. Keep the original guide if already clear; do not add another render by habit.

Take required views from the actual task; a two-view example does not replace a requested diagonal. Before generation name the chosen views in the job manifest. Keep the saved camera as truth; changing the model/camera afterward to match a drifting illustration invalidates the comparison.

## Generate

### One-house turnaround experiment

After the failed independent-view pilots, test one building as ONE requested three-view sheet: facade, side, diagonal together. Use scripts/packet.py to make a common-scale geometry sheet and a small material-only style board from selected surface crops of the user's actual style image. Inspect these two inputs once. Crops must exclude whole building silhouettes/compositions; preserve the original style file. Do not confuse this experimental mode with producing several distinct assets in one call. Do not change the 3D camera to make a drifting result look correct.

Request one image_gen edit of the sheet, preserving left/center/right view order, all three projected building shapes, roof/wall ratios, straight structural edges and overlaps. The second image supplies brushwork/material finish only, not architecture/camera. No labels or new building volumes; detail existing surfaces and include the small professional accents described below when relevant. One initial call, no automatic retries, one final guide/result comparison. Report actual failure honestly. This mode is unproven; independent PNG views still use the per-view mode below when requested. Read the scripts only if adapting them; their --help documents usage.

### Separate requested views

- Use built-in image_gen through imagegen. Load local inputs with view_image before editing. First referenced image is the selected-view edit target, second the chosen style image. Label roles explicitly. Use supported referenced_image_paths for available local paths, never invented mask/fidelity/seed controls.
- One call per requested view, no speculative alternatives. Use the same short style description across views. Add a previously generated view only when needed for material identity, with its role explicitly excluding camera/geometry; do not attach every previous result.
- Use this compact prompt, replacing brackets with observed facts:

```
Use case: style-transfer. Edit image 1 into finished [user-selected medium/style], using image 2 for painting/material language only. Image 1 is the architecture and camera: retain its building silhouette, projected roof/ridge/eave lines, wall proportions, entrance, major attachments and near/far overlaps. Apply surface detail within those existing volumes. [Profession: a few relevant tools/materials/work-yard accents and their consistent locations, if this is a professional building.] [One specific overlap or landmark if ambiguous.] Do not copy the style reference's composition or add building volumes. Keep the view/framing; [requested background/alpha]. Guide contours are construction cues, not decorative seams. Palette/brushwork/detail density: [brief observed style].
```

Details may enrich the existing surfaces; they must not create new roofs, canopies, windows on hidden walls or rearranged wings. Follow the supplied projection, including perspective convergence; do not blindly demand vertical/parallel lines on a PERSP guide. Prefer one meaningful view over a crowded sheet of unrelated buildings.

### Professional identity

For a professional building, include a few readable cues of its actual purpose, not just richer wall textures. Take the profession from the task/source; ordinary housing does not acquire an invented trade. Examples, not a universal checklist: woodcutter — axe in a chopping block, stacked logs and a small tree/work yard; hunter — bow/quiver and hides on a modest drying rack. Choose appropriate tools, raw materials or products for other professions, adapted to the selected racial style.

These are image-generation accents, not a new detailed 3D modeling task. Small props and a restrained yard may extend beyond the guide's building outline; the architecture, camera, roofs and major masses remain fixed. Keep accents within the frame, secondary to the house, with ground/support contact and without blocking the entrance. Do not turn the sprite into a large landscape or add structural wings/roofs for props.

State their locations briefly in building-relative terms and keep them consistent across facade/side/diagonal, allowing natural occlusion. Do not move a tool to a different wall merely to keep it visible. Avoid tiny clutter or giving every profession the same barrels/crates; the purpose should read at game scale.

## Finish once

Save raw outputs and exact prompts/reference roles. Inspect one comparison of guides/results for silhouette, roof lines, main overlaps, identity across views and selected style; for professional buildings also note whether the trade cues read and stay consistent. Compare at common scale; do not warp either image to hide drift. State whether geometry/style actually passed, with concrete doubts. Avoid pixel-proof/ray-grid audits and long critique loops.

Check apparent camera height through roof/wall projected proportions and visible top surfaces, not a prompt's degree number. Straight architectural edges must remain straight with the guide's convergence; perspective is not permission for bent walls, skewed doors or inconsistent roof planes. If a pilot visibly changes these, the method has failed geometry even when its style is attractive. A neutral outlined guide plus role-separated prompt has already shown this failure; do not batch-regenerate hoping that stricter wording will lock geometry. Any requested next experiment should be confined to one building/needed views until its actual outcome supports scaling.

Default: deliver the generated views and doubts after this check. Further corrections are a separate requested step; for an explicitly requested correction, change only the named defect and preserve the same guide/style. Do not silently spend calls until an image happens to fit. Keep transparent output alpha when requested.

For workspace assets retain raw PNGs, final paths and a small manifest of inputs/prompts/results. Count image_gen calls; do not invent its internal token usage or claim that shorter text guarantees cheaper image generation. Budget for two views is two initial calls, not a guaranteed monetary cost. [Evidence and limitations](references/evidence.md) are optional unless discussing reliability.

When separate view PNGs are requested from a turnaround, leave clear transparent vertical gaps and save facade/side/diagonal next to the untouched raw sheet. Reuse the project's splitter if supplied; cut through actual transparent gaps, preserve alpha/pixel scale, and record source rectangles/canvas offsets. Report inseparable or clipped panels rather than silently cutting artwork. Raster slicing does not establish a game-world pivot. If the user reserves version selection, keep exports staged and never replace source assets until that selection is explicit.
