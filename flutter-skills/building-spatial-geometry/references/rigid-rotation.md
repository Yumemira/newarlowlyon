# Rigid game-world rotations and depth

Conclusion: different orientations come from one building rotated on the ground, with its dimensions and camera fixed. A change of projected width is an effect to verify, not a target to force.

For a world pivot C and local point P, use `P' = C + Rz(yaw)*(P-C)` with the same proper rotation for every wall, roof, annex and landmark. Preserve lengths, footprint area, height, handedness and relative attachment transforms. A rotation matrix satisfies `R.T @ R = I` and `det(R)=+1`. Nonuniform scaling, shear, reflection, rotating the image canvas and independently moving the annex cannot substitute for yaw.

Keep projection, camera pose, orthographic scale or perspective lens/distance, resolution and common pivot fixed. For a requested quarter-turn demonstration use 0/90/180/270 degrees; this illustrates the method and does not claim a particular game's undocumented rotation increment or the project's final camera. Filenames such as horizontal/vertical do not authorize stretching the artwork to align its bounding box.

Project the whole rotated model. In camera coordinates depth is the component along the viewing direction; screen Y alone is insufficient for roof/chimney/annex occlusion. Render intersecting geometry with an actual depth buffer. If assembling 2D layers, derive visibility from matching depth geometry and disclose limitations; one average depth value per large intersecting face cannot solve all overlaps.

The formerly far wall can become near, an annex can disappear behind the main body and the apparent chimney side can switch. Their building-local coordinates must stay unchanged. Do not move features back into view, keep the same facade facing the viewer, or mirror a finished sprite to imitate the opposite side. Hidden geometry must be designed once and labelled as inferred.

Verification: record the designed mesh plus child transforms before rotating; compare them across views. Check the assembly's world transform for rigidity, distances/height as appropriate, camera invariance, contacts and rendered visibility. The fixture now tests nonuniform compression and an independently relocated annex as failures. Its hash checks consistency with the frozen design, not the correctness of an arbitrary original design.

For painted results compare projected structural landmarks and occlusions with the guide at fixed scale. Different alpha bounding boxes are normal across rotations; independently stretching or fitting each output can hide a deformation. A PNG set with matching filenames and transparency is not evidence of correct rotations.
