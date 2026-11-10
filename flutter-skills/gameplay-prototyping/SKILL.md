---
name: gameplay-prototyping
description: "Prototype or tune game mechanics, difficulty, progression and control feel. Use for gameplay experiments and balancing; routine engine fixes or asset export do not require it."
---

# Gameplay Prototyping

Turn an idea or playtest complaint into a small playable experiment with observable
success criteria. Read [Experiments and tuning](references/experiments.md) when
choosing metrics, controls or progression changes.

## Establish the experiment

Use the provided genre, reference games, platform and constraints. Ask only for
missing information that changes the experiment; otherwise state a reversible
assumption. Preserve the user's concept instead of redesigning it into a favored genre.
Describe the player action, immediate feedback, consequence and repeat loop. Identify
what the prototype tests: comprehensibility, precision, pacing, challenge or choice.

## Build and tune

- Start from an existing mechanic or the smallest playable slice. Placeholder shapes
  are appropriate when art is not the hypothesis; do not require image generation.
- Expose a small set of relevant parameters with units and useful ranges. Change one
  causal group at a time so observations can be attributed to a change.
- Distinguish responsiveness, forgiveness and difficulty. Input buffering, coyote
  time, acceleration and variable jump height are optional platformer techniques,
  not universal requirements for every game.
- Tune feedback to clarify game state. Camera shake, flashes, hit-stop and audio
  should have bounded intensity and support the project's reduced-motion settings.
- Separate mathematical balance from player experience. A simulation can expose
  dominant choices or economy growth but cannot prove a game is enjoyable.
- Implement in the project's engine when asked for a working game; a conversation
  visualization is useful for exploration but is not a delivered Flutter build.

## Accessible and observable controls

For the mechanic being changed, consider touch reach, simultaneous actions, remapping,
hold-versus-toggle behavior, text readability and alternatives to color-only or
sound-only cues. Preserve the game's intended challenge while removing unnecessary
input barriers. Do not turn a small tuning task into an unrelated accessibility
redesign. Include an unassisted first attempt and a short teach/practice sequence
when evaluating a new mechanic; distinguish misunderstood rules from poor execution.

## Evaluate and deliver

Use a repeatable scenario and document initial versus changed parameters, actual
observations and remaining uncertainty. For new mechanics, offer a short playtest
with neutral tasks rather than coaching the tester through every action. Do not
invent player feedback, success rates or retention metrics.

When writing code, follow project lifecycle and Flutter/Dart instructions. Keep
persistent configuration separate from runtime world objects. Do not impose a new
state-management library or analytics service for a small experiment.

Use [Evaluation cases](references/evaluation.md) to assess this skill itself.
