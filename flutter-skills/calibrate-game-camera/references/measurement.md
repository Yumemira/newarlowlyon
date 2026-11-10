# Measure, fit, challenge

Conclusion: an orthographic fit is useful only if structural evidence supports it. Save the original and an overlay of the actual chosen lines.

Use >=2 well-separated segments per family, ideally 3–5 and >=50 pixels long. Twelve pixels is merely the helper's hard rejection floor. Mark X/Y as perpendicular WORLD directions; roof pitch lines are unsuitable. Structural ridges can count only if demonstrably horizontal. For a tilted/curved building, isolate a valid subvolume or change the model.

The helper uses median slopes and an unoriented circular mean to check parallelism. A default 2° maximum within-family deviation is a diagnostic starting point, not an aesthetic standard. An outlier is not automatically discarded; verify annotation or acknowledge inconsistent drawing. To assess uncertainty, perturb endpoint positions by the estimated marking error (e.g. ±2 px), refit, and report an angle range. Large angle uncertainty means use longer edges or another reference.

Optional `scale_reference` is `{"edge":[[u0,v0],[u1,v1]],"world_length":3}` for a true vertical of known length. Inventing a door's real height does not recover measured scale; label that assumption. Mirror, roll, anisotropic resizing and perspective can invalidate the canonical solution. Weak perspective cannot reliably be excluded from a single small sprite.

Freeze a camera manifest with projection, axes, angle range, roll, canvas, units, scale, pivot and annotation provenance. Fit one camera to the intended common scene; do not independently resize each building until it looks similar.

A useful initial blockout acceptance target is structural landmark RMS <=2 px at a 256 px asset and max <=4 px, with observed annotation uncertainty recorded. These are proposed working tolerances, not project decisions. Measure only corresponding visible architecture: foliage/shadow/paint fringe should not define the building silhouette. A tolerance smaller than annotation error is meaningless.

For painted outputs compare eave/ridge endpoints, wall bases, entrance corners and chimney anchoring at fixed scale. Do not silently rescale or warp the result to pass. Preserve the intended stylization where it does not break the shared camera; explicitly document any deliberate local departure.
