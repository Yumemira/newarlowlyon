# Coherent architectural construction

Conclusion: derive connected parts from common surfaces and dimensions, then project the complete model.

Use a ground footprint in XY and named heights in Z. For a symmetric gable with ridge along X, wall depth D, eave H and ridge R:

`z_roof(y)=R - (R-H)*abs(y)/(D/2)`.

With horizontal overhang O, evaluate that same plane at y=±(D/2+O); extending the eave horizontally without extending the slope creates a kink. A slab thickness measured vertically differs from thickness measured along its normal: declare which. The example uses vertical thickness T, top at z_roof+T, underside at z_roof, meeting the wall top without coincident exposed surfaces.

A hip roof consists of planes whose ridges/hips are actual shared intersection edges. For intersecting wings solve the roof planes' equality for their valley; do not hide a discontinuity with a beam. A lean-to annex needs a defined high connection and low support line. Turrets, domes and curved roofs need section curves and thickness, not contradictory local slopes.

Represent a wall detail as `P(u,v)=origin + u*wall_tangent + v*world_up + epsilon*normal`. Use the same face transform for frame, shutters and glazing. A painted dark rectangle can represent a closed window in a guide; a visible doorway revealing interior needs an actual opening and wall thickness. Do not advertise solid decorative slabs as functional interiors.

A chimney's bottom must penetrate the roof locally, and its upper end emerge above it. Posts need ground/foundation contact and a measured roof/beam seat. Declare intended joints and penetrations; an AABB overlap does not prove surface contact. A watertight component does not prove absence of intersections or correct assembled geometry.

In Blender set dimensions deliberately (cube size vs half-extents matters), evaluate modifier output for measurements, and use object references rather than accidental active selection. Apply transforms only when required by a modifier/export contract; blanket resetting origins can destroy a shared pivot. Do not globally smooth architectural normals or guess subdivision shrinkage compensation percentages: use support loops/creases/bevels as appropriate and measure evaluated surfaces.
