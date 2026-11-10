# Spatial acceptance and failure tests

Conclusion: keep numeric construction checks and visible quality checks independent.

1. Inspect the requested camera model and coordinate convention. Compare the renderer's projected test points with the analytic camera basis. Freeze resolution, scale and pivot across views.
2. Check meaningful geometry: positive dimensions; eave below ridge; intended overhang; nondegenerate faces; closed structural components where closure is intended. Thin decorative cards may legitimately be open. For modifier-heavy geometry inspect evaluated meshes, not only original control vertices.
3. Check declared contacts on actual surfaces using rays/BVH/mesh distance. Probe multiple locations: one central ray cannot establish a whole roof's contact. Check both roof slopes, chimney penetration, supporting posts and ground plane. Broad-phase bounds alone are insufficient.
4. Rotate one assembly to all required views plus a reverse/oblique holdout. Verify local geometry/landmarks unchanged; normals, occlusion and feature identity sensible. Render before painting. Check transparent pixels and alpha bounds after export.
5. LOOK at each rendered and painted view at full size and game scale. Catch z-fighting, impossible valleys, reversed slopes, repeated/missing windows, hovering parts and painterly deviations. A green report is not art acceptance.

The example build_fixture.py audits its 14 closed components, six eave ray probes, two post contacts, chimney penetration, 3% vertex framing margin, local-geometry identity, camera-basis agreement, nonblank RGBA export and border pixels. It intentionally does NOT certify arbitrary self-intersections, all mesh topology, engineering safety, subtle alpha fringes or painted similarity. Additional architecture needs additional relevant probes.

Reproduce negative controls:

```
<blender> -b --factory-startup --python-exit-code 1 --python <skill>/scripts/build_fixture.py -- --config <skill>/assets/house.json --out /tmp/fault-study --audit-only --fault floating-roof
```

Also use `floating-post`, `missing-roof`, `clipped`, `squashed`, `swapped-annex`. Each should write a failing report and exit nonzero. Baseline must pass. Use a fresh output directory for each test so old renders cannot be mistaken for current results. The default helper is a study fixture, not a replacement for QA of the user's actual building.

Full reproducible regression runner (baseline renders + six negative controls):

```
python <skill>/scripts/test_fixture.py --blender /absolute/path/to/blender --out /absolute/qa-directory
```

Rotation update: the current default study uses front/side/diagonal plus reverse (0/270/315/180 with azimuth 0 and a +X front). The earlier four-oblique-quarter-turn study remains only historical method evidence. The audit also checks a proper rigid assembly matrix and frozen mesh/child-transform signatures from before fault injection. This rejects anisotropic compression and relocation of an annex, while not claiming the original design or the project camera is correct.
