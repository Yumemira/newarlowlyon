# Projection and walk-cycle reference notes

Read when designing or transferring locomotion, especially for top-down and three-quarter views.

## Establish the projection

A sprite frame is a 2D projection of a 3D pose. Identify screen-up and how depth is represented. In orthographic or tile-RPG views, depth does not automatically shrink a sprite as in perspective projection; artists communicate depth with overlap, visible surfaces, shading, relative placement, and deliberate foreshortening. Keep projection conventions stable across frames.

For a foot moving toward the camera, the projected leg can look shorter even while the foot moves upward on screen. A convincing raised step can need coordinated cues: the knee bends and moves relative to the pelvis; shin length and angle change; the raised boot moves upward and may appear larger or show more of its top; the airborne leg overlaps the support leg; the support foot stays planted while weight transfers; the torso/pelvis shifts in a small consistent arc.

The screen directions depend on camera. Inspect a matching reference instead of applying a universal rule like “nearer always means bigger.”

## Read a walk cycle

A cycle commonly moves through contact → down/weight acceptance → passing → up/push-off, then repeats with the opposite leg. Some game sheets use another cadence or omit/repeat poses. Follow the actual source timing and order.

In frontal or three-quarter views, inspect which leg is nearer, which knee is visible, how boot overlaps shin, and whether the boot top is visible. In a top-down game, walking may read mostly as depth-row stepping rather than a frontal camera walk. Pick a reference with the game's camera.

Track:
- root/pelvis anchor and deliberate body bob;
- shoulder/hip counter-swing;
- left/right knee and ankle landmarks;
- contact foot versus airborne foot;
- overlap order and visible top/side of each boot;
- screen-space displacement through the loop.

A planted foot can move relative to the body as hips pass over it; do not force both shoes onto one image-wide baseline. Lock the character world pivot, not a changing silhouette box.

## Source and transfer record

For each action, record source URL/creator/license, camera/view, frame count/order, source cell rectangles, duration if known, and loop convention. Keep source pixels or links intact where redistribution permits. If the reference is only a diagram or prose, call the output inspired by it, not an exact transfer.

Create a pose table: frame index, phase, root, pelvis, knees, ankles, support foot, raised foot, and key overlap. Compare generated transfers side-by-side at equal scale. If generation changes gait, isolate and repair offending poses rather than blindly re-exporting the whole sheet.

## Useful reference families

- University animation sheets for contact/down/passing/up and loop timing.
- Openly licensed game sprites with documented frame grids/directions.
- Frame-by-frame footage from the same camera angle.
- 3D mannequins only when camera, projection choice and ground plane stay fixed.

Do not treat one example as universal anatomy. Stylized pixel characters may exaggerate knee lift or foot size for readability; preserve the art direction while maintaining a coherent spatial path.
