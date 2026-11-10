# Native API boundary

Checked against published flame_forge2d 0.20.0 and forge2d 0.15.1 on 2026-09-30.
Apply this only to this API generation; inspect the project's lockfile first.

## Startup and lifetime

Native targets require a C toolchain; web loads WASM. Initialize Forge2D before making
a raw World. Forge2DGame performs initialization during onLoad; preserve that base
lifecycle. Standalone worlds and tests must initialize explicitly. Native world state
belongs to its creating isolate; pass serializable data, not live handles, to workers.
A final teardown must release the native world. Removal from the Flame tree alone
keeps the physics world reusable. Do not destroy it on a temporary route change if
the game intends to reuse it. Invalid body/shape handles must not be retained.

Published source evidence:
- https://pub.dev/documentation/flame_forge2d/0.20.0/flame_forge2d/Forge2DWorld-class.html
- https://pub.dev/documentation/forge2d/0.15.1/forge2d/World-class.html
- https://pub.dev/packages/forge2d/versions/0.15.1

## Shape/contact migration

Fixtures become shapes. Custom body construction must enable the needed contact or
sensor events; automatic bridge setup does not cover every override. Raw world events
are read after stepping, while solver callbacks have different mutation restrictions.
Check validity on delayed/end events. Do not rely on a final endContact during body
destruction to release gameplay state.

## Behavioral migration traps

Physical render scale uses metersToPixels separately from camera zoom. Friction defaults
and one-sided chain behavior changed: verify explicit material settings and chain
winding with a falling-body fixture. Match units to engine tolerances; tiny bodies can
produce apparently premature contacts. LiquidFun particles are absent in this generation.
Substeps are not an independent frame accumulator; let one owner advance the world.

Migration sources (main can advance beyond published releases):
- https://docs.flame-engine.org/main/bridge_packages/flame_forge2d/migration.html
- https://docs.flame-engine.org/main/other_modules/forge2d/migration.html
