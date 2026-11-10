# Review evidence and production handoff

Conclusion: shared-scene compatibility and identity review must precede batch acceptance.

A useful reference packet includes:
- Global camera contract and candidate/approval status; source gameplay image plus observation notes.
- One approved project style example per relevant material/race; explicit role for each reference.
- Per-building identity card and structural guide for each requested yaw.
- Canvas, pivot, world/pixel scale and lighting contract, with unknowns named.
- Review boards and individual verdicts with evidence, not just “RGBA valid”.

The bundled review_set.py reads a selected manifest, records source SHA-256, image mode/dimensions, alpha range/fractions and thresholded bounds, and emits boards at ONE canvas resize factor. It preserves sources. It cannot recover world scale, camera angles or topology from thumbnails. A nonzero alpha range does not prove clean cutout; matte RGB may be invisible after correct alpha compositing. View dark/bright neutral backgrounds if fringes are suspected.

For final acceptance, place several architecture/race samples on the same ground plane at explicit world pivots/scale; add representative characters if the project provides them. Do not independently fit every alpha bounding box to an equal icon size. Test gameplay zoom and one closer inspection. If the runtime/scene scale is unavailable, label a composite as illustrative and leave scene acceptance open.

Review axes independently:
1. View: shared projection/elevation, consistent ground directions, enough overhead/side information for the requested gameplay view.
2. Identity: same roof topology, entrance/annex/chimney relationships; plausible occlusion in alternate yaws.
3. Style/readability: materials, palette, outlines, detail density, role and race recognizable at game scale.
4. Export: actual transparency, framing, common pivot/scale metadata, no unintended baked background.

A file audit can pass while art fails. An attractive sprite can fail scene compatibility. Do not launch follow-up chats or send a packet externally unless the user authorized that communication; preparing a local packet is sufficient for a skill-building task.
