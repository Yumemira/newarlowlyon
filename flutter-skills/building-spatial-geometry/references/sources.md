# Sources and public skill review

Conclusion: use first-principles camera geometry and executable local evidence; public skill claims need checking. Reviewed 2026-10-26; public branch links are mutable. No third-party skill code was copied or installed. Helpers here are original implementations.

Primary learning sources:
- [MIT, Imaging](https://visionbook.mit.edu/imaging.html), §5.3: perspective and orthographic models. Supports model distinction, not the camera of any particular game.
- [CMU 16-385, camera models](https://www.cs.cmu.edu/~16385/s18/lectures/lecture9.pdf): affine/orthographic camera context. Not a method to recover invisible walls.
- [Blender manual, projections](https://docs.blender.org/manual/id/3.0/editors/3dview/navigate/projections.html): viewport projection differs from render camera setting; historical manual. Local Blender 5.0.1 introspection and actual renders establish tested API behavior here.
- [Scratchapixel, orthographic matrix](https://www.scratchapixel.com/lessons/3d-basic-rendering/perspective-and-orthographic-projection-matrix/orthographic-projection-matrix.html): camera-space coordinates and framing context.

Public skill candidates (author descriptions are not independent validation):
- [ProfRino/blender-assembly](https://github.com/ProfRino/Blender-MCP-Assembly-Skill): useful focus on joints and dimensional errors. Do not adopt its arbitrary 10–15% subdivision overshoot, single-axis overlap as contact proof, or unconditional origin reset/smoothing.
- [mattjamo/bpy_skill](https://github.com/mattjamo/bpy_skill): executable build/inspect loop; version-specific claims require local checks. Useful general machinery, not a measured sprite camera contract.
- [capybala18/capybala-bpy-skill](https://github.com/capybala18/capybala-bpy-skill): broad operating manual; hardware/version assumptions and mandatory stylistic proportions are unsuitable as project-wide rules.
- [mehh/isometric-objects](https://gist.github.com/mehh/b2aa7b990f1d4fa0d6e06fcefc38f2ee): public description proposes one projection function, but fixed technical illustration styling is not the game's painted style. Gist body was not fetched successfully; no full-code audit claimed.

The official curated openai/skills list was checked: no specialized building-camera/roof-construction skill appeared. Search is not exhaustive and does not establish that no suitable public skill exists.
