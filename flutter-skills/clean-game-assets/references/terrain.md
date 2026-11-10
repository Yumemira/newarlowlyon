# Ground continuity

The accepted Last Lantern terrain is NOT a collection of independently generated seamless PNG tiles. Logical corner masks sample a shared texture coordinate field. This avoids raster seams between cells by construction; the overall texture can still need testing at its wrap boundary. The rejected independent AI tilesets are not evidence of seamless output.

For a new game choose based on its renderer:

- Shared ground texture plus corner masks: one world-space coordinate system across adjacent cells, compatible edge masks, deterministic terrain variation. Keep unique plants/stones as transparent props on separate layers.
- Independently baked tiles: enforce matching edge strips, include straight/diagonal/inner/outer transitions, preserve matching corners and test every valid neighbor pair. Generate randomized maps and inspect them at runtime zoom. A nice atlas picture does not prove edge continuity.

Large props spanning cells need one stable world anchor and separate draw bounds; collision cells and drawing bounds are not identical. Sorting at the ground anchor preserves the game's pseudo-3D depth. Keep atmosphere and large light falloff in the runtime layer when baked halo edges would expose the rectangular asset boundary.
