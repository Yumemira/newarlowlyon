# Projection and orientation

Conclusion: projection is a coordinate transform, not an adjective such as “isometric”. Here Z is up; camera position relative to target has azimuth a from +X towards +Y and elevation e above XY; image v points down, no roll. Angles below enter trig functions in radians.

For P=(x,y,z), scale s and image origin (u0,v0):

```
u = u0 + s*(-sin(a)*x + cos(a)*y)
v = v0 + s*(sin(e)*cos(a)*x + sin(e)*sin(a)*y - cos(e)*z)
```

These are dot products with orthonormal camera right/up axes. Translation of the target changes origin only. Perspective adds depth-dependent division and cannot be emulated by changing this single s. Orthographic assumptions follow [MIT, Imaging §5.3.2](https://visionbook.mit.edu/imaging.html); equations above are derived for our explicit axes.

For ground X/Y edge slopes mx,my in this convention:

```
mx = -sin(e)*cot(a)
my = sin(e)*tan(a)
sin(e)^2 = -mx*my
```

For canonical a in (0,90°), mx<0,my>0:
`e=asin(sqrt(-mx*my))`, `a=atan(sqrt(-my/mx))`.
Edge labels/handedness require architectural evidence. Nearly vertical/horizontal families make this inversion ill-conditioned. The solver does not recover roll or perspective.

At a=45°, true isometry has e=asin(1/sqrt(3))≈35.264°: three unit axes have equal projected lengths, ground lines slope ±1/sqrt(3), i.e. 30° to image horizontal. A 2:1 diamond has ground slopes ±0.5 and e=30°, a dimetric projection. Neither is an automatic requirement for a painted game.

Blender cameras look along local -Z with local +Y up: aim using `(target-location).to_track_quat('-Z','Y')`. Elevation 35.264° is complementary to 54.736° tilt from the world vertical. Do not paste either number into arbitrary Euler components.

A local long axis rotated by world yaw p projects as `(sin(p-a), sin(e)*cos(p-a))`. Thus p=a+90° gives screen-horizontal, p=a gives screen-vertical. Freeze the camera and rotate the model, including porch/chimney. This is not screen-plane rotation.
