# Современные решения в области анимаций для мобильных приложений

## Философия анимаций 2025-2026

> Каждая анимация должна решать задачу. Если она не направляет, не подтверждает и не объясняет — убери её.

**Ключевой сдвиг 2026:** Фокус сместился с "красиво" на "функционально полезно". Motion — это коммуникация, не декорация.

**Принципы:**
- Анимация следует физике реального мира (ускорение, замедление, инерция)
- Consistency: кнопки, иконки, меню ведут себя предсказуемо
- Performance first: минимум overdraw, vector > bitmap, кэширование
- 75% приложений к концу 2025 внедрили micro-interactions как стандарт

---

## Material Design Motion System

### Easing Curves (Кривые анимации)

| Curve | Описание | Когда |
|-------|----------|-------|
| **Standard (ease-in-out)** | Быстро ускоряется, плавно замедляется | Перемещение на экране, стандартные переходы |
| **Deceleration (ease-out)** | Входит на полной скорости, плавно останавливается | Появление элемента на экране |
| **Acceleration (ease-in)** | Медленно ускоряется, уходит быстро | Исчезновение элемента с экрана |
| **Sharp (ease-in-out fast)** | Быстрое ускорение и замедление | Элементы, которые могут вернуться |

### Ключевое правило
Асимметричное ускорение и замедление = натуральное движение. Механическое линейное движение = плохо.

---

## Длительности анимаций

### По типу действия

| Действие | Длительность | Примечание |
|----------|-------------|------------|
| **Button tap feedback** | 100-150ms | Мгновенный отклик |
| **Micro-interaction** | 150-300ms | Достаточно чтобы заметить, не задерживает |
| **Page transition** | 300-400ms | Стандарт для мобильных |
| **Complex transition** | 400-600ms | Появление модалок, сложных элементов |
| **Emphasis animation** | 600-800ms | Смена контекста, hero-переходы |
| **Background / loop** | 1500-3000ms | Pulse, shimmer, бесконечные циклы |
| **Splash / onboarding** | < 3-5 сек | Максимум для splash-анимации |

### По размеру движения (Mobile)
- **Маленькие** (icon, button): 150-200ms
- **Средние** (card, section): 300-400ms
- **Большие** (page, full-screen): 400-600ms

---

## Анимации по типу экрана

### 1. Loading / Splash Screen

**Skeleton + Shimmer (лучший подход):**
```
┌──────────────────────┐
│ ████████░░░░░░░░░░░░ │  ← shimmer wave слева направо
│ ████████████░░░░░░░░ │
│ ████░░░░░░░░░░░░░░░░ │
└──────────────────────┘
```
- Wave (shimmer) > pulse — воспринимается на 65% быстрее
- Скорость: медленная, плавная (как Google iOS app)
- Skeleton повторяет реальный layout страницы
- Использовать когда загрузка > 2 сек

**Branded Splash:**
- Custom animation логотипа (Lottie/Rive)
- Rotating rings, progress bars (CustomPainter)
- Parallax-слои с 3D perspective
- **Пример connect_pro_caller:** `_AnimatedLogoRing` (SweepGradient rotation 3000ms) + `_GlowingProgressBar` (1500ms moving glow)

**Современные тренды:**
- Lottie-анимация вместо статичного лого
- Gradient mesh backgrounds
- Morphing shapes

---

### 2. Onboarding

**PageView с 3D perspective:**
```dart
// 3D-поворот слайдов при свайпе
Matrix4.setEntry(3, 2, 0.001)..rotateY(angle)
// Scale зависит от позиции в PageView
```

**Стандартные анимации:**
- Skip button: FadeIn 400ms
- Dot indicators: animated color/size transition
- Content: FadeIn + SlideY per slide
- **CTA на последнем слайде:** pulse (scale 1.0→1.03, 1500ms loop) + shimmer

**Parallax:**
- Background перемещается медленнее foreground
- Floating particles animation
- Слои с разной скоростью создают глубину

**Carousel подходы:**
- Горизонтальный PageView с parallax
- Stack с 3D transforms (perspective)
- Cards с разным масштабом по позиции

---

### 3. Dashboard

**AnimatedCounter для метрик:**
```
0 ──count up──→ 1,247
```
- Плавное "считание" от 0 до целевого значения
- Форматирование: 1K, 1.2M для больших чисел
- Длительность: 800-1200ms, ease-out curve
- Stagger между карточками: 80ms delay

**Metric Cards:**
```dart
.animate()
  .fadeIn(duration: ms400, delay: Duration(milliseconds: 80 * index))
  .scale(begin: Offset(0.85, 0.85), end: Offset(1, 1),
         curve: Curves.easeOutBack)
```

**Sparkline Charts:**
- Draw animation: path рисуется слева направо
- Длительность: 1000-1500ms
- Ease-out curve

---

### 4. Списки

**Staggered Entry (Каскадное появление):**
```dart
// Каждый элемент появляется с задержкой
.fadeIn(duration: ms400, delay: Duration(milliseconds: 60 * index))
.slideX(begin: 0.1, end: 0, duration: ms400)
```

| Тип списка | Delay per item | Direction |
|-----------|---------------|-----------|
| Contacts, Templates | 60ms | SlideX (from right) |
| Dashboard metrics | 80ms | Scale (from center) |
| Team grid | 80ms | SlideY (from bottom) |
| Pipeline columns | 80ms | SlideX (from right) |
| Settings sections | 150ms | SlideY (from bottom) |

**AnimationLimiter:** Предотвращает анимацию элементов, которые не видны в первом фрейме (важно для scrollable списков).

**Dismissible (Swipe-to-delete):**
```
┌────────────────────────────┐
│ Contact Card          ←──swipe──  │ 🗑 DELETE │
└────────────────────────────┘
```
- Direction: endToStart (свайп влево)
- Background: красный + иконка удаления
- ResizeDuration: анимация схлопывания высоты
- Confirm dialog или Snackbar с Undo

---

### 5. Detail Pages

**Header animation:**
```dart
.animate()
  .fadeIn(duration: ms400)
  .scale(begin: Offset(0.95, 0.95), end: Offset(1, 1))
```

**Sections stagger:**
```dart
// Каждая секция с нарастающим delay
Section 1: fadeIn + slideY(0.05), delay: 0ms
Section 2: fadeIn + slideY(0.05), delay: 150ms
Section 3: fadeIn + slideY(0.05), delay: 300ms
```

**Hero animation (shared element):**
```dart
// Список
Hero(tag: 'avatar_$id', child: Avatar())
// Detail page
Hero(tag: 'avatar_$id', child: LargeAvatar())
// Flutter автоматически анимирует size + position
```

---

### 6. Bottom Sheets

**Появление:**
```dart
.animate()
  .fadeIn(duration: ms400)
  .slideY(begin: 0.1, end: 0, duration: ms400)
```

**Spring Physics:**
- DampingRatio: контроль "пружинистости"
- Stiffness: контроль скорости
- Gesture-driven: pan gesture обновляет offset в реальном времени
- Snap points: sheet "прилипает" к определённым высотам

**Backdrop:**
- BackdropFilter blur: 10-20px
- Background dim: 50% black overlay
- Animate blur from 0 to target

---

### 7. Tabs

**Content transition:**
- CrossFade между табами: 300ms с 100ms overlap
- **НЕ использовать slide** — вызывает пространственную дезориентацию
- Indicator: animated translateX для горизонтального скольжения
- Duration: < 300ms чтобы не ощущалось как lag

**Tab indicator:**
```dart
TabBar(
  indicator: BoxDecoration(
    gradient: accentGradient,
    borderRadius: BorderRadius.circular(8.sp),
  ),
)
// Indicator плавно скользит между табами
```

---

### 8. Формы

**Inline validation:**
```
✓ Email valid     ← fadeIn green check, 200ms
✗ Required field  ← fadeIn red error, shake 100ms
```

**Submit button loading:**
```
[  Save  ] → tap → [ ⟳ ] → success → [ ✓ Done ]
               scale down    spin     scale up + color change
```

**Keyboard appear:**
- Content scrolls up smoothly
- Bottom sheet adjusts height animated

---

## Анимации UI-компонентов

### Button Feedback

| Тип | Анимация | Длительность |
|-----|----------|-------------|
| **Bounce (CustomBounceEffect)** | Scale 1.0→0.95→1.0 | 100-150ms |
| **Ripple (Material)** | Expanding circle from tap point | 300ms |
| **Scale** | Scale 1.0→0.9→1.0 | 150ms |
| **Color shift** | Background color transition | 200ms |
| **Pulse (CTA)** | Scale 1.0→1.03→1.0, loop | 1500ms |
| **Shimmer (CTA)** | Gradient sweep overlay, loop | 2000ms |

**Best practice:** CustomBounceEffect для ВСЕХ интерактивных элементов (не GestureDetector).

### FAB Animation
```dart
// Появление
.animate()
  .fadeIn(duration: ms400, delay: ms500)
  .scale(begin: Offset(0.5, 0.5), end: Offset(1, 1))

// Speed Dial
// FAB → tap → 3-6 sub-FABs appear with stagger
```

### Dialog / Modal
```
Appear:  fadeIn(300ms) + scale(0.8→1.0, 300ms) + backdrop blur(0→10px)
Dismiss: fadeOut(200ms) + scale(1.0→0.95, 200ms) + backdrop blur(10→0px)
```

### Snackbar
```
Enter:  slideY from bottom (300ms, deceleration curve)
Exit:   slideY to bottom (200ms, acceleration curve) OR fadeOut
```

### Pull-to-Refresh
```
Pull:     indicator appears, rotates with pull distance
Release:  indicator spins, content refreshes
Complete: indicator slides up and disappears
```

---

## Progress Indicators

### Circular (Indeterminate)
- Stroke grows/shrinks по кругу
- Continuous rotation
- Цвет: accentCyan

### Circular (Determinate)
- Ring прогресса с gradient
- Glow effect на конце
- AnimatedCounter с процентом в центре
- **Пример:** CircularProgressRing с gradient + glow

### Linear
- Bar заполняется слева направо
- Shimmer на заполненной части
- Цвет: gradient от accent к secondary

### Step Indicator
- Dots/circles для шагов
- Active step: filled + scale up
- Completed: checkmark + color
- Connected lines между шагами

---

## Celebration / Success Animations

**Когда:** Завершение задачи, достижение, успешное действие.

### Confetti
- Цветные частицы разлетаются от центра
- Duration: 2-3 секунды
- Lottie или flutter_confetti package
- **Пример connect_pro_caller:** Color overlay 15% opacity, FadeIn 150ms → FadeOut 500ms

### Success Checkmark
```
○ → circle draws → ✓ appears → scale bounce
```
- Lottie animation популярен
- Duration: 800-1200ms

### Haptic Feedback
- Лёгкая вибрация при успехе
- HapticFeedback.lightImpact() в Flutter
- Тренд 2025-2026: multi-sensory feedback

---

## Scroll-Based Animations

### Collapsing Header (SliverAppBar)
```
Scroll ↑: Header shrinks, title moves to toolbar, image fades
Scroll ↓: Header expands back
```
- Parallax: background moves slower than content
- Opacity: image fades as header collapses
- Title: morphs from large to small

### Reveal on Scroll
```
Element below viewport → scroll into view → fadeIn + slideY
```
- Trigger: element enters viewport
- Animation: 400ms fadeIn + slideY(0.05→0)
- Только один раз (не при каждом scroll)

### Parallax Layers
```
Layer 1 (background): scroll * 0.3
Layer 2 (middle):     scroll * 0.6
Layer 3 (foreground): scroll * 1.0
```

---

## Drag & Drop

**Pipeline/Kanban:**
```
Idle state:        normal card
Long press (200ms): card lifts (scale 1.05x, shadow appears)
Dragging:          card follows finger, original spot = 0.3 opacity
Over drop zone:    zone highlights
Drop:              card snaps to position (spring animation)
Celebration:       if final stage → overlay flash
```

**Microstates:**
1. **Idle** — normal appearance
2. **Hover/Long press** — subtle lift, shadow
3. **Grab** — scale up 1.05x, strong shadow
4. **Move** — follows finger, original fades
5. **Drop** — spring snap to target

---

## Инструменты и библиотеки

### flutter_animate
Декларативная анимация с цепочками:
```dart
widget
  .animate()
  .fadeIn(duration: ms400)
  .slideY(begin: 0.1)
  .scale(begin: Offset(0.9, 0.9))
  .then(delay: ms200)  // chain
  .shimmer(duration: ms1500)
```
**Когда:** Стандартные UI-анимации, stagger, page entry.

### Lottie
- JSON-анимации из After Effects
- Lightweight, hardware-accelerated
- Cross-platform (iOS, Android, Web)
- **Когда:** Loading indicators, success animations, illustrations, icons
- **Осторожно:** Дизайнить с учётом ограничений платформы

### Rive
- Runtime-анимации (интерактивные, настраиваемые в коде)
- State machines для сложной логики
- **Когда:** Interactive characters, game elements, complex UI states
- **Отличие от Lottie:** Rive = интерактивный, Lottie = playback only

### Flutter Built-in

| Класс | Когда |
|-------|-------|
| **AnimatedContainer** | Простые property changes |
| **AnimatedOpacity** | Fade in/out |
| **AnimatedPositioned** | Перемещение в Stack |
| **AnimatedCrossFade** | Переключение между двумя widgets |
| **AnimatedSwitcher** | Замена widget с transition |
| **Hero** | Shared element между страницами |
| **AnimationController** | Полный контроль, explicit animations |
| **TweenAnimationBuilder** | Кастомные tween без controller |
| **AnimatedList** | Анимация add/remove в списке |

### Physics-Based
```dart
SpringSimulation(spring, start, end, velocity)
FlingSimulation(drag, position, velocity)
```
- Natural-feeling motion
- Bottom sheet gesture-driven анимации
- Bounce effects
- Throw/fling для swipe

---

## Паттерны анимаций connect_pro_caller (Reference)

| Контекст | Анимация | Параметры |
|----------|----------|-----------|
| Page entry | FadeIn | 400ms |
| List stagger | FadeIn + SlideX | 60-80ms per item |
| Metric cards | FadeIn + Scale | 0.85→1.0, easeOutBack, stagger 80ms |
| CTA button | Scale pulse + Shimmer | 1.0→1.03, 1500ms loop |
| Sheet entry | FadeIn + SlideY | 0.1→0, 400ms |
| Detail sections | FadeIn + SlideY | 0.05→0, stagger 150ms |
| Header | FadeIn + Scale | 0.95→1.0, 400ms |
| Title | FadeIn + SlideY | -0.2→0, 400ms |
| FAB | FadeIn + Scale | 0.5→1.0, delay 500ms |
| Celebration | Overlay + FadeIn/Out | 150ms in, 500ms out |
| 3D onboarding | Matrix4 rotateY | perspective 0.001 |
| Loading ring | Continuous rotation | 3000ms, SweepGradient |
| Progress bar | Moving glow | 1500ms |

---

## Чеклист анимаций при создании экрана

- [ ] Page entry: fadeIn 400ms
- [ ] Список: staggered fadeIn + slide (60-80ms per item)
- [ ] Cards: fadeIn + scale с easeOutBack
- [ ] FAB: fadeIn + scale с delay 500ms
- [ ] Bottom sheet: fadeIn + slideY
- [ ] Кнопки: CustomBounceEffect (не GestureDetector)
- [ ] CTA: pulse + shimmer (loop)
- [ ] Loading: Skeleton + Shimmer (не spinner)
- [ ] Empty state: анимированная иконка
- [ ] Dialogs: fadeIn + scale + backdrop blur
- [ ] Success: celebration/checkmark animation
- [ ] Pull-to-refresh: animated indicator
- [ ] Tab switch: crossfade (НЕ slide)
- [ ] Counters: animated count-up

Sources:
- [UI/UX Evolution 2026: Micro-Interactions & Motion](https://primotech.com/ui-ux-evolution-2026-why-micro-interactions-and-motion-matter-more-than-ever/)
- [UI Animation Trends 2026 - Ripplix](https://www.ripplix.com/blog/principles-of-animation-ui-design)
- [Motion - Apple HIG](https://developer.apple.com/design/human-interface-guidelines/motion)
- [Easing and Duration - Material Design 3](https://m3.material.io/styles/motion/easing-and-duration)
- [Motion - Material Design](https://m2.material.io/design/motion/understanding-motion.html)
- [Flutter Animations Introduction](https://docs.flutter.dev/ui/animations)
- [Advanced Flutter Animations - Semaphore](https://semaphore.io/blog/flutter-animations)
- [Flutter Staggered Animations](https://docs.flutter.dev/ui/animations/staggered-animations)
- [Flutter Animate Package](https://pub.dev/packages/flutter_animate)
- [Lottie Flutter Package](https://pub.dev/packages/lottie)
- [Rive & Lottie in Flutter](https://medium.com/@ravipatel84184/elevate-your-flutter-app-with-advanced-animations-a-guide-to-using-rive-and-lottie-d7398aae0958)
- [Skeleton Screens 101 - NN/g](https://www.nngroup.com/articles/skeleton-screens/)
- [Skeleton Loading Design - LogRocket](https://blog.logrocket.com/ux-design/skeleton-loading-screen-design/)
- [Motion UI Trends 2025](https://epixs.in/motion-ui-micro-interactions-2025/)
- [12 Micro Animation Examples 2025](https://bricxlabs.com/blogs/micro-interactions-2025-examples)
- [Flutter Button Press Animation](https://flutterassets.com/create-button-press-animation-flutter-examples/)
- [Dismissible Widget - Flutter](https://docs.flutter.dev/cookbook/gestures/dismissible)
- [Spring Animation - Android](https://developer.android.com/develop/ui/views/animations/spring-animation)
- [Mobile App Animations - Justinmind](https://www.justinmind.com/ui-design/mobile-app-animations)
- [Hero Animations - Flutter](https://docs.flutter.dev/ui/animations/hero-animations)
- [Flutter Page Route Animation](https://docs.flutter.dev/cookbook/animation/page-route-animation)
- [Micro-Interactions in Flutter](https://attentioninsight.com/boost-user-engagement-with-micro-interactions-in-flutter/)
- [Confetti Flutter Package](https://fluttergems.dev/packages/confetti/)
- [Progress Indicators - Flutter](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)
- [Advanced Animations Mobile](https://www.wildnetedge.com/blogs/advanced-mobile-ui-animations-to-boost-app-engagement)
