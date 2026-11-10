# Boost/Optimization Animation Patterns

Premium fullscreen overlay animations for optimization/boost processes.

## Architecture

### Overlay Approach
- Use `OverlayEntry` to display fullscreen animation on top of everything
- Insert on boost start, remove on boost end
- `Obx` inside OverlayEntry watches controller state reactively

```dart
void _startBoost(BuildContext context) {
  late OverlayEntry overlayEntry;
  overlayEntry = OverlayEntry(
    builder: (_) => Obx(() {
      if (!controller.isBoostRunning.value) {
        WidgetsBinding.instance.addPostFrameCallback((_) {
          overlayEntry.remove();
        });
        return const SizedBox.shrink();
      }
      return BoostOverlay(
        progress: controller.boostProgress.value,
        stepLabel: controller.boostStep.value,
      );
    }),
  );
  Overlay.of(context).insert(overlayEntry);
  controller.boost();
}
```

### Controller Pattern
- `boostProgress` (0.0 → 1.0) — overall progress
- `boostStep` — current step label for display
- Smooth progress with micro-increments:

```dart
Future<void> _boostStep(String step, double target) async {
  boostStep.value = step;
  final start = boostProgress.value;
  const steps = 8;
  final increment = (target - start) / steps;
  for (int i = 0; i < steps; i++) {
    await Future.delayed(const Duration(milliseconds: 50));
    boostProgress.value = start + increment * (i + 1);
  }
}
```

## Animation Layers (bottom to top)

### 1. Floating Particles
- `CustomPainter` with deterministic random (seed=42)
- 30-50 particles orbiting center at varying radii
- Colors: primary, secondary, boostGradientEnd with varied alpha
- `MaskFilter.blur` for soft glow
- Particle count increases with boost progress

### 2. Outer Glow Ring
- Pulsating `BoxShadow` with dual colors
- `AnimationController` duration: 2000ms, reverse: true
- Alpha oscillates 0.3 ↔ 0.8

### 3. Scan Line (radar sweep)
- Rotating cone/sector via `Path.arcTo` (30° arc)
- `RadialGradient` fill: transparent center → faded primary edge
- Leading edge: thin line from center to top
- Rotation: 3s full cycle

### 4. Rotating Ring Segments
- Outer ring: 24 segments, every 3rd brighter (0.4 vs 0.15 alpha)
- Inner ring: 16 segments, counter-rotating at 0.7x speed
- Different colors: primary (outer) vs boostGradientEnd (inner)

### 5. Progress Arc
- Pulsating scale (0.95 ↔ 1.08, 1500ms)
- `SweepGradient` shader: primary → secondary → primary
- Glowing dot at arc endpoint with `MaskFilter.blur`
- Background track ring (surface color)

### 6. Center Content
- `TweenAnimationBuilder<double>` for smooth percentage counter (600ms)
- `AnimatedSwitcher` for step label transitions (400ms fade+slideY)

### 7. Step Progress Bar (bottom)
- `LinearProgressIndicator` with smooth tween
- Step labels below: active (primary, bold), done (secondary), pending (tertiary)
- `AnimatedDefaultTextStyle` for smooth label transitions

## AnimationControllers Summary

| Controller | Duration | Behavior |
|-----------|----------|----------|
| rotation | 4s | repeat() |
| pulse | 1.5s | repeat(reverse: true) |
| scan | 3s | repeat() |
| particle | 6s | repeat() |
| glow | 2s | repeat(reverse: true) |

## Color Scheme
- Primary glow: `AppColors.primary` (cyan)
- Secondary accents: `AppColors.secondary` (green)
- Background: `AppColors.bgDark` at 0.92 alpha
- Ring segments: `AppColors.boostGradientEnd` (blue)

## Key Design Principles
1. **Layered depth** — multiple transparent layers create premium feel
2. **Counter-rotation** — opposing rotations add visual complexity
3. **Pulsation** — breathing effect on progress ring feels alive
4. **Smooth transitions** — step labels slide in, numbers tween
5. **Deterministic particles** — seed-based random for consistent render
6. **Color harmony** — gradient from cyan → green across the arc
