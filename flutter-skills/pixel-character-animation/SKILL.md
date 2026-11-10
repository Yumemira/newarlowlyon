---
name: pixel-character-animation
description: Create 2D pixel-art characters and readable, pose-faithful sprite animations from researched visual references, especially perspective-aware walk cycles.
---

# 2D Character Animation

Create coherent game-ready 2D character art and animation. Use this skill for pose-faithful character animation and adapting reference motion to another character. Static character art and general sheets use the appropriate image/sprite skill without mandatory motion-reference research. Pair with `clean-game-assets` for transparent raster export and sheet QA when available.

## Workflow

1. **Identify the game's view.** Inspect existing art and establish whether the camera is top-down, three-quarter, side-on, isometric, or frontal. Keep that view fixed through all frames. For an existing character, inspect its accepted design and preserve silhouette, palette, equipment, scale, and anchor.

2. **Choose animation mode.** For reference transfer, find a motion reference. For original animation without requested reference matching, establish deliberate key poses and timing; skip source-frame mapping/comparison and do not claim transferred fidelity. **Motion reference:** Browse for a clear, legally usable reference with the same view and action. Prefer original animation sheets, frame-by-frame videos, openly licensed game assets, or educational diagrams. Check the source, exact frame order, camera, cell layout, and license. Save the source and attribution when the reference is kept in the project. A different-view reference can teach timing, but cannot directly supply screen-space poses.

3. **Read the motion before drawing.** Label key poses and their order. For a walk, identify contact, down/weight acceptance, passing, and up/push-off for each side. Track pelvis/root, shoulder line, knees, ankles, hands, and planted foot. Record which limb is near/far, overlaps, foot lift, and torso bob. Read [references/space-and-walk-cycles.md](references/space-and-walk-cycles.md) only for locomotion/walk or perspective problems.

4. **Make a pose map.** For every source frame, note its rectangle and screen-space joint landmarks. Establish one consistent root/pivot. Keep source order and pose count during transfer. Do not infer motion from a contact sheet alone if a frame-by-frame preview or original sheet is available.

5. **Design the character into those poses.** Use built-in image generation for illustrated raster art. Supply character design and motion reference, assigning each a clear role. Explicitly ask to preserve each source pose, limb side, overlap, raised-foot height, projected segment length, camera and cell. Work in small batches when that improves consistency. Do not ask a generator to invent motion while also transferring it.

6. **Export without changing the performance.** Preserve frame order, fixed cell rectangles, deliberate root movement and transparent margins. Correct row offsets from measured source positions; confirm dimensions before assuming a uniform grid. Do not center each frame by its bounding box, align every boot to one baseline, or resize poses individually: these erase weight shifts and foot lift. Add interpolated frames only after key poses read correctly. Never duplicate frames merely to reach a requested count.

7. **Review in motion.** Create a contact sheet and loop at gameplay scale. Compare each transferred frame beside its source, then inspect the whole cycle including its wrap. Check apparent scale, root stability, foot lift, support leg, overlap, torso bob, limb side, foot sliding, and camera consistency. Show the user the preview and plainly identify remaining defects.

8. **Run asset QA.** When available, use `clean-game-assets` to audit alpha, edge contamination, containment, anchors and fringes. Technical audit complements visual motion review; it cannot prove a gait is convincing. Preserve generated originals, exact prompts, source association, export metadata and QA evidence.

## Acceptance

Accept a motion transfer only when pose order and meaningful joint motion match the reference, support exchanges as intended, raised limbs retain perspective cues, frames share a deliberate pivot and scale, and the loop reads at gameplay size. If generated poses fail, keep them as candidates and refine key poses; sheet cleanliness alone is not animation quality.

## Boundaries

- Match the requested art style and game camera; do not impose pixel art on other media.
- Respect reference licenses and preserve attribution and applicable share-alike terms.
- Keep frame count and playback duration separate. More frames do not automatically improve smoothness.
- Use frame-by-frame references for faithful pose transfer. Prose alone cannot verify source pose coordinates.
- Follow project engine conventions for integration; this skill creates art and animation assets, not unrelated gameplay.
