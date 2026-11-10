# Experiments and tuning

## A useful experiment record

Capture the question, intended audience/control device, current behavior, proposed
change, parameters, short repeatable task, observable evidence and next decision.
This can be a paragraph in the response; do not force a new design document for a
small tuning request. If the project has a spec, maintain its established format.

Example hypothesis: players miss a jump because a press immediately before landing
is discarded. Compare the same section with and without a short input buffer.
Observe missed presses and unintended automatic jumps. Pick the interval from the
control goal and playtest, not a universal magic number. Test pause and restart so
buffered actions cannot survive into an unrelated scene.

## Genre-specific routes

- Platformer: time to apex, horizontal stopping distance, air steering and landing
  feedback. Moving platforms and wall contacts require their own acceptance cases.
- Top-down action: normalized diagonal movement, aim versus travel direction,
  readable attack windup, damage cadence and invulnerability rules.
- Cards/turn-based: legal actions, feedback for unavailable actions, turn transition,
  information visibility and a meaningful choice in a short session.
- Economy/idle: explicit units, sources/sinks, growth assumptions, caps and elapsed
  time policy. Simulate plausible sessions before adding monetization mechanics.

## Sources and limits

Research baseline: 2026-09-30. These design sources supply reasoning, not Flutter APIs.
- Steve Swink, firsthand discussion of control and perception:
  https://www.gamedeveloper.com/design/game-feel-the-secret-ingredient
- Celeste/TowerFall author describes a specialized AABB movement system:
  https://maddymakesgames.com/articles/celeste_and_towerfall_physics/
- Runnable Flutter game starting points: https://github.com/flutter/games

Do not copy Celeste's integer-coordinate constraints into a physics-based game merely
because they worked there. Reuse a principle only when the intended experience fits.

## Practical playtest controls

Choose a target input device early: an action comfortable with a mouse may obstruct
vision or require awkward simultaneous touches on a phone. For relevant mechanics,
consider adjustable sensitivity, remapping and hold/toggle alternatives. Use shape,
text or motion alongside important color cues, and visible feedback alongside sound.
Keep settings persistent when that is within the product's scope.

State a falsifiable observation before testing: e.g. can a new player discover the
exit without coaching? Record misunderstanding separately from timing difficulty.
Do not call a change an A/B result without comparable observations; small informal
samples are directional evidence. Use a short iteration budget and decide whether to
keep, revise or discard the hypothesis. A prototype should have a clear end/reset
condition, including an intentional no-win sandbox if that is the experiment.

Source checked 2026-09-30:
https://gameaccessibilityguidelines.com/basic/
