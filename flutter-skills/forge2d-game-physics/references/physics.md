# Physics decisions

## World integration

Flame's bridge provides Forge2DGame/BodyComponent integration. Read [Native API boundary](native-api.md) for the 0.20/0.15 generation. The exact construction,
world configuration and stepping APIs depend on package versions. Read installed
source or versioned API docs before writing constructor arguments. Do not substitute
Box2D C/C++ documentation for Dart signatures or claim every upstream feature exists.

## Scale and motion

Pick reasonable physical sizes, then map them through the camera. A 128-pixel texture
need not represent a 128-unit body. Verify the bridge's axis/gravity convention instead
of assuming a screen Y direction from a different engine. Convert drag targets and
spawn locations through world coordinates.

Use static bodies for immovable geometry, dynamic bodies for solver-controlled
motion and kinematic bodies where supported and appropriate for prescribed movement.
Sensors produce contact information without the corresponding solid response.
Restitution/friction affect contacts, but perceived behavior also depends on scale,
step rate and velocity. Adjust them in a controlled fixture.

## Time and mutations

A bounded fixed-step policy may improve stability, but existing engine stepping must
remain the single authority. Large catch-up loops after a background gap can freeze
the UI. Decide the resume policy explicitly. Reapply forces at the correct simulation
cadence; do not repeatedly apply a one-shot impulse on every rendered frame.
Use the engine's supported deferred removal/update mechanism when the world is locked.
When pooling a component, verify that its body, contacts and references are reset;
reusing a destroyed body reference is not valid pooling.

## Sources

Research baseline: 2026-09-30.
- https://docs.flame-engine.org/latest/bridge_packages/flame_forge2d/forge2d.html
- https://pub.dev/packages/flame_forge2d
- https://pub.dev/packages/forge2d
