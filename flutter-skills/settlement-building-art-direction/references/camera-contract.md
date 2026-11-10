# One camera, several object headings

Conclusion: global projection, object orientation on the ground and screen alignment are different choices. Keep them separately named.

Record `projection`, world axes/up, `azimuth_deg`, `elevation_deg`, roll, units, pixel scale, resolution, pivot, annotation provenance/uncertainty and `status` (proposed/measured/approved). Unknown numbers remain null. “Approximate three-quarter” is a user visual requirement; precise numerical values need evidence. An elevation guessed from a roof's apparent size is insufficient.

For this project's current direction, the default presentation is an elevated top-side view: roof tops and wall heights read together, with depth and grounded construction. This does not establish a mandatory exact angle. Confirm using representative gameplay framing, not an isolated spinning product.

For the orthographic convention in calibrate-game-camera, a local ground axis at yaw p projects as `(sin(p-a), sin(e)*cos(p-a))`, where a is camera azimuth and e its elevation. Exact screen-horizontal occurs at p=a±90°, exact screen-vertical at p=a modulo 180°. A box then may expose only one wall plane. This alone does NOT prove the camera moved.

Map-axis 90° turns normally preserve an oblique presentation under an oblique camera; naming those variants “horizontal/vertical” does not require their ridge to align exactly with screen X/Y. Preserve legacy filenames as aliases and record actual world yaw separately. The user clarified on 2026-10-27 that these must behave as real game-world rotations, not compressed variants with confused near/far relationships. Earlier screen-alignment wording must not justify shape fitting, independent scaling or altered attachments. The project's numerical camera and rotation increment remain unapproved; do not assert a specific Norland step from memory.

For a round building yaw is read from entrance, annex and asymmetric detail, not from its circular footprint. Never deform an object to make a circular silhouette “vertical”. Do not yaw each subcomponent to keep all decorations facing the viewer.

Before scaling production, compare camera candidates on the SAME simple building at fixed dimensions, pivot and pixel scale, then inspect that camera with several actual architectures. This avoids mistaking shape changes for camera changes. A mathematical isometric demo is a camera candidate only, not the project's visual reference.
