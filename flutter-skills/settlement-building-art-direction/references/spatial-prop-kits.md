# Spatial prop kits and named views

Conclusion: editable 3D masters can be instanced around a building, sharing camera, scale, light and depth. A library of flat PNG cutouts cannot provide unseen sides by itself.

Separate reusable raw resources (wood, stone, metal, crystal, clay, textiles), functional equipment (forge, loom, workbench), architectural modules (brackets, columns, windows) and small decoration. Reuse detail and equipment to reduce work without making unrelated functions reuse the same complete house. Select assemblies for each culture from inspected project references; label unapproved material/lore assignments as proposals.

Each 3D master needs a meaningful local ground/contact pivot, named axes, declared units, editable geometry/materials, stable asset ID and intended attachment surface. Keep source masters separate from positioned instances. Store placement transforms and any material variants; change geometry where a variant needs a different shape instead of recoloring everything. Large resource piles need their own shape/volume, not a scaled image.

Place props in world or building-local space as appropriate. Building-mounted props rotate with their host; world piles around a building rotate with the assembly only when the brief says that whole arrangement rotates. A static town scene's ground props need not move when a building is turned. Preserve contacts and compute occlusion in 3D.

The user clarified on 2026-10-27 that the review should show the chosen facade facing the viewer, the side, and a diagonal view at the same elevated camera. Four oblique quarter-turns alone do not demonstrate this. Define a building-local front first; derive side at +/-90 degrees and diagonal at +/-45 from that front. Exact signs depend on the visible side desired. This is named-view construction, not a claim about Norland's undocumented camera or rotation grid.

Present those three views at common scale and add reverse diagnostics separately if needed. Never change yaw and camera simultaneously to make each image individually attractive. A plain 3D pilot validates assembly; its low-detail materials are not the finished painted project style.

For painted exports retain the geometry, camera, alpha and optional depth/object masks as spatial controls. Image generation may still change the guide; inspect its results. Do not claim that modular props guarantee correct final painting. Deliver an editable source library and independent asset exports, not just a flattened showcase PNG.
