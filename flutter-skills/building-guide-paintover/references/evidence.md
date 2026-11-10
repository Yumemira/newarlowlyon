# Evidence and limits

The first human-house project experiment used explicit geometry/style roles and paintover prompts, yet changed roof proportions/overlaps and added a canopy; a side correction still left drift. Making those prompts longer is not established as a solution.

This workflow proposes clearer neutral structural edges, a short role-separated edit prompt, and a predictable call budget. The guide renderer can be validated deterministically; better fidelity and lower total generation cost require an actual comparison pilot and must not be claimed from the skill alone.

The subsequent nine-human-house pilot also used neutral outlined guides. The user reported a lower apparent camera and warped straight architecture; comparison of the base facade confirmed changed roof/wall proportions. Thus this input improvement has not solved geometry preservation. A missing diagonal was also a task-coverage error. Record these failures before reusing/scaling the method; they are not fixed by validation of the helper script.

[OpenAI image prompting](https://developers.openai.com/api/docs/guides/image-prompting) covers reference roles and preservation in edits. [Image generation documentation](https://developers.openai.com/api/docs/guides/image-generation) notes composition/consistency limitations; even image masks are guidance rather than guaranteed exact boundaries. Those API descriptions are not a promise that the built-in tool exposes masks, input-fidelity settings, model selection, seeds, or depth/normal conditioning. Use only controls actually offered by the active tool.

A neutral outlined render communicates visible surface boundaries. It is not a ControlNet/depth-map constraint and does not lock the image model to a mesh. A style sample's architecture can still leak into the result. Uniform registration is acceptable for inspection; anisotropic fitting, perspective warping, or hiding defects by clipping does not establish preserved geometry.

Shorter prompts save text/context; image input/output processing and retries also affect total cost. Report measured call counts and tool-provided usage only. Paired-view sheets or one common style reference might help consistency, but are experiments, not proven savings or the default for separate requested PNG assets.
