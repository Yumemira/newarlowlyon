# Generate the raw image

Paths/commands below are relative to the skill root, not this references directory.

### 3. Generate the raw image

Use built-in `image_gen`.

Do not use Three.js, Canvas, SVG, HTML/CSS, PIL drawing, or other code-generated art as the raw sprite source. These are acceptable only for runtime display, debug overlays, deterministic layout guides, or postprocessing already-generated images.

After generation:

- find the raw PNG under `$CODEX_HOME/generated_images/...`
- copy or reference it from the working output folder
- keep the original generated image in place

