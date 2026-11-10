# Cinematic Motion Implementation Template

Use after selecting an entry from [Cinematic Animation Catalog](CINEMATIC_ANIMATION_CATALOG.md). Rename every `FeatureMotion*` symbol to the selected interaction and map visual values to the target app's `AppColors`, `AppDuration`, and geometry tokens.

## 1. Deterministic timeline

```dart
import 'package:flutter/foundation.dart';

enum FeatureMotionPhase {
  idle,
  tracking,
  commit,
  moving,
  settle,
  complete,
  reverse,
  retry,
  cancel,
}

enum FeatureMotionQuality { full, weakDevice }

@immutable
class FeatureMotionFrame {
  const FeatureMotionFrame({
    required this.phase,
    required this.exposure,
    required this.travel,
    required this.emphasis,
  });

  final FeatureMotionPhase phase;
  final double exposure;
  final double travel;
  final double emphasis;
}

abstract final class FeatureMotionTimeline {
  static double interval(double value, double begin, double end) =>
      ((value.clamp(0.0, 1.0) - begin) / (end - begin)).clamp(0.0, 1.0);

  static FeatureMotionFrame frameAt(
    double progress, {
    required bool armed,
    bool tracking = false,
    bool reversing = false,
    bool retrying = false,
    bool cancelled = false,
    bool reduceMotion = false,
    FeatureMotionQuality quality = FeatureMotionQuality.full,
  }) {
    final value = progress.clamp(0.0, 1.0);
    if (cancelled) return _zero(FeatureMotionPhase.cancel);
    if (retrying) return _zero(FeatureMotionPhase.retry);
    if (reversing) return _zero(FeatureMotionPhase.reverse);
    if (!armed) {
      return _zero(
        tracking ? FeatureMotionPhase.tracking : FeatureMotionPhase.idle,
      );
    }
    if (reduceMotion || value >= 1) {
      return const FeatureMotionFrame(
        phase: FeatureMotionPhase.complete,
        exposure: 1,
        travel: 1,
        emphasis: 1,
      );
    }

    final travel = interval(value, .16, .78);
    return FeatureMotionFrame(
      phase:
          value < .16
              ? FeatureMotionPhase.commit
              : value < .78
              ? FeatureMotionPhase.moving
              : FeatureMotionPhase.settle,
      exposure: interval(value, 0, .35),
      travel: travel,
      emphasis:
          quality == FeatureMotionQuality.full
              ? interval(value, .52, 1)
              : 0,
    );
  }

  static FeatureMotionFrame _zero(FeatureMotionPhase phase) =>
      FeatureMotionFrame(
        phase: phase,
        exposure: 0,
        travel: 0,
        emphasis: 0,
      );
}
```

## 2. One-shot handoff

Use only when continuity crosses route/widget ownership.

```dart
@immutable
class FeatureMotionHandoffData {
  const FeatureMotionHandoffData({required this.entityId});

  final String entityId;
}

abstract final class FeatureMotionHandoff {
  static FeatureMotionHandoffData? _active;

  static bool arm(FeatureMotionHandoffData data) {
    if (_active != null) return false;
    _active = data;
    return true;
  }

  static FeatureMotionHandoffData? consume(String entityId) {
    final active = _active;
    if (active?.entityId != entityId) return null;
    _active = null;
    return active;
  }

  static void clear() => _active = null;
}
```

## 3. Safe action ownership

```dart
Future<void> commit() async {
  if (_committing) return;
  setState(() => _committing = true);
  try {
    await Future.wait<void>([
      durableAction(),
      if (!MediaQuery.disableAnimationsOf(context))
        _motion.forward(from: 0),
    ]);
  } catch (_) {
    if (mounted && !MediaQuery.disableAnimationsOf(context)) {
      await _motion.reverse();
    }
    rethrow;
  } finally {
    if (mounted) setState(() => _committing = false);
  }
}
```

Rules:

- Call `commit` from an interaction callback, never from `build`, `Obx`, or a painter.
- Do not start the same entrance animation from both loading completion and page data refresh.
- If navigation uses an outer Hero, return the inner visual child directly:

```dart
if (context.findAncestorWidgetOfExactType<Hero>() != null) return child;
return Hero(tag: heroTag, child: child);
```

## 4. Lifecycle ownership

- Create controller/listeners in `initState`.
- Stop nonessential animation on `paused` and `inactive`.
- Resume only if the durable action is still active.
- Dispose controller, focus node, scroll listener, notifier listener, and binding observer.
- Check `mounted` after every awaited operation before touching widget state.

## 5. Required tests

### Pure timeline

- idle and tracking outputs;
- every phase boundary just before/at/after the threshold;
- `progress < 0` and `progress > 1` clamping;
- complete state;
- reverse, cancel, and retry;
- reduced motion;
- weak-device removal of secondary effects;
- all opacity/layout values remain bounded.

### Real widget

- one gesture invokes one durable action;
- animation does not replay after data refresh;
- failure reverses and retry remains reachable;
- disposal during motion causes no exception;
- pause/resume is safe;
- compact width, 200% text, long locale, and alternate DPR do not overflow;
- ancestor Hero does not produce a nested Hero assertion;
- disabled animations still expose the final semantic state.

## 6. Promotion gate

Promote a project animation into shared `dart_files/` only when:

1. project-specific colors, copy, model names, and routes are removed;
2. API accepts semantic inputs rather than a feature controller;
3. the pure timeline has boundary coverage;
4. one real interaction test exists;
5. reduced motion, weak-device, error reverse, lifecycle, and nested-Hero behavior are documented.
