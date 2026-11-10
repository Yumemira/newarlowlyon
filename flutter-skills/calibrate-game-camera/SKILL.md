---
name: calibrate-game-camera
description: Measure and match building or prop sprite camera angles from structural reference edges; distinguish orthographic, dimetric and perspective views and diagnose wrong elevation, rotation or scale. Use before generating alternate architectural views or when the user reports a wrong viewpoint.
---

# Calibrate game camera

When the task reuses a saved camera and does not request a new fit, load that preset and stop here. For sketch views use $building-sketch-guide. Do not remeasure references or rerun calibration studies on routine rotations.

Make the viewpoint measurable before adding painted detail. Read the project's art/research entrypoint and only the relevant camera/asset contract. A research reference is not an approved camera specification.

## Reference and measurements

Inspect the actual reference at full size and target game scale. Preserve the source. Record image dimensions, pixel coordinates and uncertainty for at least two independent edges in each structural X/Y/Z family. Use floor edges, horizontal beams/eaves and vertical wall corners. A sloping roof rake is NOT a ground-plane axis. Separate buildings with different orientations; do not fit them as one family. Avoid shadows, foliage and stylized chipped edges.

Read [projection.md](references/projection.md) for the coordinate convention, equations and the difference between 35.264° elevation and Blender's complementary camera tilt. If parallel families converge, verticals tilt or the reference is deliberately inconsistent, do not force the simple orthographic solver to return a camera. Use an appropriate perspective/roll model or document a measured approximation. One image cannot establish exact scale, hidden geometry or unique handedness.

Run the standard-library helper with manually checked annotations:

```sh
python <skill>/scripts/camera.py edges.json --out camera-fit.json --overlay reference.png
python <skill>/scripts/test_camera.py
```

`edges.json` has `x_edges`, `y_edges`, `z_edges`, each a list of `[[u0,v0],[u1,v1]]`, with v down. The current solver supports orthographic, zero roll, X negative slope and Y positive slope, canonical first quadrant. Read [measurement.md](references/measurement.md) for annotation, uncertainty and acceptance. Overlay requires Pillow; fitting does not. Exit 1 rejects this model, not the artwork. `candidate` is a hypothesis, not artistic approval.

## Scene-wide art direction

For a settlement-wide or Norland-like elevated three-quarter presentation, use $settlement-building-art-direction when available to establish the reference hierarchy and shared camera contract. A canonical isometric fixture is not evidence for the game camera. Treat near-axis-aligned references as potentially ill-conditioned for this solver, not automatically wrong. Distinguish changes of object yaw from changes of camera elevation; roof area alone cannot separate them.

## Freeze the camera

Save projection, azimuth/elevation relative to named world axes, roll, world units, pixel scale, resolution, common pivot and evidence paths. To rotate a building, rotate its whole model in world XY around Z. Keep the camera, dimensions, scale and canvas fixed. Horizontal/vertical screen orientation of a long axis is not generally object yaw 0°/90°; derive yaw from the camera basis. Never rotate the finished PNG in its image plane to simulate another view.

For game-map orientations, horizontal/vertical labels normally identify headings rather than permission to force screen-aligned silhouettes. Never compress one dimension or independently reposition features to make those labels look right. Apparent near/far order must be recomputed from the rotated geometry in the same camera, not guessed from image Y.

Render a neutral blockout and overlay measured structural lines/landmarks. Compare corresponding lengths and silhouette at common scale; independently fitted bounding boxes can hide errors. Correct camera before geometry, geometry before decoration. If using generative painting, pass the blockout and accepted style reference separately, then remeasure the painted result: text instructions do not lock geometry.

Deliver camera manifest, annotation overlay, measured deviations and an honest remaining uncertainty. Use $building-spatial-geometry when multiple roofs, wall contacts or persistent alternate-view geometry need construction.
