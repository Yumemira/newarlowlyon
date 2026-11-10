# Version and gameplay boundaries

## 3.x versus 4.x

Bonfire 4 restructures many mixins into `WithFeature` plus a feature API object.
For example the migration guide maps Jumper/jump to WithJumper/jumper.jump and
PathFinding/setupPathFinding to WithPathFinding/pathFinding.setup. These are migration
examples, not permission to upgrade the app. Read the installed definitions first.
Movement keeps direct access but its API was also rewritten; old methods/fields can
be removed even when the mixin name remains unchanged. Follow the release-specific
migration table rather than mechanically prefixing every method with a feature name.

## Gameplay integration

Choose AI behavior appropriate to scale: simple explicit states can be easier to
verify than a complex tree for one enemy. Pathfinding needs walkability consistent
with collision geometry and handling for unreachable/removed targets. Visibility,
attack range and path distance are distinct concepts.

Normalize intended movement so diagonals do not unintentionally become faster; first
check what Bonfire already normalizes to avoid applying normalization twice. Directional
animation should follow the movement/aim policy selected by the game. Define idle
facing and attack interruption explicitly when the feature needs them.

Progress such as collected quest items should use stable domain identifiers rather
than storing live NPC/component instances. Separate the state required across maps
from camera, sprites, listeners and transient attacks that belong to one scene.

## Sources

Research baseline: 2026-09-30. Default-branch documentation can advance beyond releases.
- https://pub.dev/packages/bonfire
- https://github.com/RafaelBarbosatec/bonfire
- https://github.com/RafaelBarbosatec/bonfire/blob/master/MIGRATION_3_TO_4.md
Use the repository's actual default branch/version tag if that path moves.

## Navigation and interaction edge cases

The published 4.0.0 path-finding implementation queries barriers with a configurable
visibility filter (`useOnlyVisibleBarriers` in the implementation's configuration).
Inspect its actual public signature/default before use. Camera movement must not make
an intended solid barrier cease to matter to a long-distance route. Test unreachable
goals, a target removed while moving and a route that crosses the visible area boundary.
Invalidate/recalculate when necessary rather than continuously replanning without need.

For NPC interaction, distinguish proximity detection, explicit interaction and dialog
state. Decide whether enemies continue to simulate during conversation. On close, clear
consumed/held input so a dialog-confirm press cannot become an unintended attack. Keep
localized text, choice IDs and quest state separate from rendered strings; reward
transactions should follow the game's intended one-time/repeatable quest semantics.
Test an already-completed quest and a loaded save, not only the first conversation.

Sources checked 2026-09-30:
- https://pub.dev/packages/bonfire/versions/4.0.0
- https://github.com/RafaelBarbosatec/bonfire/blob/master/lib/mixins/path_finding/path_finding_api.dart
- https://github.com/RafaelBarbosatec/bonfire/blob/master/MIGRATION_3_TO_4.md
Published archive source was inspected; default-branch code may change afterwards.
