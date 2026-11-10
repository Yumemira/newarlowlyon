# iOS Game App UI Design Reference — 2024/2025

**Purpose:** Reference knowledge base for generating beautiful iOS game UIs in Flutter using the ADS Framework (AppColors, LayoutStyle, flutter_animate, CustomBounceEffect).

**Last updated:** 2026-04

---

## Table of Contents

1. [Visual Style Catalog](#1-visual-style-catalog)
2. [Color Palettes & Hex Codes](#2-color-palettes--hex-codes)
3. [Typography & Fonts](#3-typography--fonts)
4. [Screen-Type Design Patterns](#4-screen-type-design-patterns)
5. [Animation Patterns & Timing](#5-animation-patterns--timing)
6. [Flutter Implementation Recipes](#6-flutter-implementation-recipes)
7. [Top Game UI References](#7-top-game-ui-references)
8. [Layout & Ergonomics](#8-layout--ergonomics)
9. [iOS 2025 Liquid Glass Trend](#9-ios-2025-liquid-glass-trend)
10. [ADS Framework Integration Cheatsheet](#10-ads-framework-integration-cheatsheet)
11. [Aesthetic Subculture Styles (2024–2025)](#11-aesthetic-subculture-styles-20242025)
12. [Award-Winning Game UI Analysis (2023–2024)](#12-award-winning-game-ui-analysis-20232024)
13. [Specific Screen Deep Dives](#13-specific-screen-deep-dives)
14. [Casual & Hypercasual UI Design Patterns](#14-casual--hypercasual-ui-design-patterns)
15. [App Store / Play Store Marketing UI Patterns](#15-app-store--play-store-marketing-ui-patterns)

---

## 1. Visual Style Catalog

Seven dominant art styles for mobile games in 2025 (source: Zvky Design Studio):

### 1.1 Semi-Realistic Stylized ("Premium Mobile")
- Smooth shading with soft gradients
- Realistic textures on simplified silhouettes
- Glossy, premium renders with ambient occlusion hints
- Best for: RPGs, shooters, high-budget casino
- Color mood: Saturated midtones, bright specular highlights on dark bases
- UI texture: Metallic panels, leather/stone borders

### 1.2 Clean Vector / Esports
- Thick outlines, high-contrast flat shapes
- Minimal gradients — solid fills dominate
- Instant visual clarity; scales perfectly on all screens
- Best for: Casual arcade, competitive mobile, esports
- Color mood: 1–2 bold accent colors on white or near-black
- UI texture: Flat cards, hard shadows

### 1.3 Neon-Tech / Cyber Glow (trending 2024–2025)
- Heavy rim lights and neon outline glow
- High-contrast warm vs. cool color pairing (cyan + magenta, yellow + purple)
- Metallic surfaces with emissive lighting
- Electric FX streaks, lens-flare accents
- Best for: Futuristic shooters, battle-royale, esports
- Color mood: Deep navy/black base + one or two neon accents
- UI texture: HUD-style panels, holographic overlays, scanline patterns

### 1.4 Glassmorphism / Liquid Glass (iOS 2025 apex)
- Frosted semi-transparent panels layered over vibrant backgrounds
- Subtle white border (1–2 px) to define edges
- Background blur sigma 10–20
- Animated refraction responding to device tilt
- Best for: Premium menus, lobby screens, shop overlays
- Color mood: Deep gradient background + white/tinted glass panes

### 1.5 Crystal & Glossy Candy
- Glassy faceted surfaces, subsurface glow
- Vibrant gradients: magenta → yellow, cyan → green
- High-gloss reflections and polished highlights
- Best for: Casual puzzle, slot games, reward screens
- Color mood: Bright saturated pastels over white or off-white

### 1.6 Cute Cartoon Stylized
- Round shapes, soft edges, exaggerated expressions
- Vibrant, approachable colors (no dark base)
- Best for: Casual, puzzle, family games
- Color mood: Pastel primaries — Pixel Pastels palette

### 1.7 Stylized Low-Poly 3D
- Flat shading, minimal textures, geometric silhouettes
- Bold color blocks, sharp edges
- Best for: Open-world, survival, multiplayer
- Color mood: Earthy tones or high-contrast cartoon

---

## 2. Color Palettes & Hex Codes

All palettes follow the **5-color rule**: deep base + surface shade + text neutral + accent 1 + accent 2.

### 2.1 Dark Neon Palettes

**Neon Arcade** (gaming UI, Twitch overlays)
```
Background:  #0B0F1A
Surface:     #1B2A41
Cyan accent: #00F5FF
Purple:      #7C4DFF
Pink:        #FF2DAA
Text:        #F7F7FF
```

**Midnight Neon** (esports, bold techy)
```
Background:  #0A0B10
Surface:     #12151E
Green:       #15FFB5
Blue:        #3D5AFE
Red:         #FF1744
Text:        #B0BEC5
```

**Synthwave Sunset** (retro-futuristic)
```
Background:  #1A1A2E
Surface:     #16213E
Red:         #E94560
Yellow:      #F9ED69
Teal:        #00ADB5
Text:        #E0E0E0
```

**Glitch Cyber Noir** (cyberpunk UI)
```
Background:  #0E0E10
Surface:     #1A1A20
Teal:        #2A9D8F
Purple:      #8E44AD
Orange:      #E76F51
Text:        #F1FAEE
```

**Alien Invasion** (otherworldly intense)
```
Background:  #0B1020
Surface:     #111827
Cyan:        #00FFEA
Sky:         #7DF9FF
Magenta:     #B5179E
Fuchsia:     #F72585
```

### 2.2 Gold / Premium Palettes

**Loot Box Gold** (reward popups, premium)
```
Background:  #1A1423
Surface:     #241830
Gold:        #D4AF37
Amber:       #FF6F00
Teal:        #5BC0BE
Text:        #F8F1E5
```

**Mystic RPG** (character cards, cinematic)
```
Background:  #1B263B
Surface:     #415A77
Silver:      #E0E1DD
Purple:      #C17CFF
Gold:        #FFB703
```

**Dungeon Torch** (fantasy, gritty warm)
```
Background:  #2D1B0E
Surface:     #3D2512
Rust:        #8D5524
Tan:         #D4A373
Gold:        #FFB703
Deep blue:   #1B263B
```

### 2.3 Space / Sci-Fi Palettes

**Sci-Fi Lab** (clinical futuristic)
```
Background:  #0B0F1A
Surface:     #1B2A41
Cyan:        #00B4D8
Light cyan:  #90E0EF
Pale:        #CAF0F8
```

**Space Loot** (cosmic, optimistic)
```
Background:  #0B1026
Surface:     #1A2040
Cyan:        #00D1FF
Green:       #00FFA3
Purple:      #A259FF
Gold:        #FFD166
```

**Space Pixel Art**
```
Space dark:  #172038
Dark green:  #19332D
Dark blue:   #253A5E
Blue:        #3C5E8B
Light blue:  #4F8FBA
Cyan:        #73BED3
Yellow-green:#A8CA58
```

### 2.4 Sports Palettes

**Racing HUD** (fast, precise)
```
Background:  #0B0C10
Surface:     #1F2833
Teal:        #66FCF1
Mint:        #45A29E
Light gray:  #C5C6C7
```

**Ice Arena** (cool, competitive)
```
Background:  #0B1320
Surface:     #142035
Blue:        #1C7ED6
Light blue:  #74C0FC
Pale:        #E7F5FF
Accent:      #A5D8FF
```

**Boss Fight Red** (action HUDs, urgent)
```
Background:  #1C1B22
Surface:     #2A2940
Red:         #FF3B30
Orange:      #FF9500
Yellow:      #FFE66D
Teal:        #2EC4B6
```

### 2.5 Cyberpunk Neon (raw hex set)
```
#00FF00 (matrix green)
#FF00FF (magenta)
#00FFFF (cyan)
#FFFF00 (electric yellow)
#FF1493 (deep pink)
#39FF14 (toxic green)
#7B68EE (medium slate blue)
```

### 2.6 Duolingo Gamification Color Meanings
- Green `#58A700` → success, correct answer
- Red `#FF4B4B` → hearts, mistakes, danger
- Orange `#FF9600` → streaks, fire, urgency
- Yellow `#FFC800` → XP, coins, reward
- Purple `#CE82FF` → leagues, premium

---

## 3. Typography & Fonts

### 3.1 Font Categories for Game UI

| Role | Style | Recommendations |
|------|-------|----------------|
| Game Title / Logo | Bold display, decorative | Bebas Neue, Rajdhani Bold, Exo 2 ExtraBold |
| Score Counter | Monospace or tabular | Rajdhani, Orbitron, Share Tech Mono |
| HUD Elements | Condensed sans | Barlow Condensed, Roboto Condensed, Oswald |
| Body / Dialog | Readable sans | Nunito, Poppins, Inter |
| Fantasy RPG | Serif display | Cinzel, Metamorphous, IM Fell English |
| Sci-Fi | Geometric/futuristic | Orbitron, Exo 2, Audiowide |
| Casual/Kids | Rounded | Fredoka One, Bubblegum Sans, Nunito |

### 3.2 Size Hierarchy (mobile game UI)

```
Game title:     40–56 sp  (Bebas Neue / bold display)
Section header: 24–32 sp  (bold weight)
Score large:    48–72 sp  (monospace / tabular nums)
Score label:    14–16 sp  (semibold, uppercase, tracked)
Button text:    16–18 sp  (bold, uppercase)
Body text:      14–15 sp  (regular)
Caption/badge:  10–12 sp  (medium, uppercase)
HUD small:      11–13 sp  (condensed, high contrast)
```

### 3.3 Score Counter Pattern
- Use `fontFeatures: [FontFeature.tabularFigures()]` for non-jumping numbers
- Animate with `CounterAnimation` or `AnimatedFlipCounter` package
- Color: gold gradient (#FFD700 → #FF8C00) or white with glow
- Add glow using `Stack` with blurred duplicate text (see §6.4)

---

## 4. Screen-Type Design Patterns

### 4.1 Loading Screen

**Pattern: Cinematic + Progress Bar**
- Full-bleed background (gradient or key art)
- Centered game logo with subtle pulse animation (scale 1.0→1.04, 1.2s loop)
- Progress bar: 80% width, rounded pill shape, 8–12 px height
- Progress bar glow: box-shadow / Container with blur overlay
- Tips/lore text rotating below bar (fade in/out, 3s interval)
- **DO NOT** stop at 99% — use fake completion to 100% before navigating

**Layout:**
```
[FULL BG GRADIENT]
  ↓ centered 40%
[GAME LOGO — animated pulse]
  ↓ 48px gap
[PROGRESS BAR — 80% width, pill, glow]
  ↓ 24px gap
[TIP TEXT — 14sp, fading]
  ↓ bottom safe area
[VERSION TEXT — 11sp, muted]
```

**Animation timing:**
- Logo entrance: fadeIn + scaleY 0.8→1.0, 600ms, easeOut
- Progress fill: ease-in start, ease-out to completion
- Tips: crossfade 400ms, 3000ms display

### 4.2 Onboarding / Tutorial Flow

**Key principles:**
- Interactive > text: let player DO the action, not read about it
- Progressive disclosure: introduce mechanics one at a time
- Highlight target element with spotlight + dimmed overlay
- Minimum 3–5 screens for character/world intro
- Skip button always visible (but non-prominent)

**Screen types in game onboarding:**
1. **Splash** — logo + tagline, 2s auto-advance
2. **World intro** — atmospheric art + 1-sentence lore
3. **Character select** (if applicable) — swipeable cards with stats
4. **Interactive tutorial** — spotlight overlay + hand/arrow pointer
5. **First win screen** — mini celebration, reward reveal
6. **Hub intro** — arrows pointing to main nav items

**Visual pattern: Tutorial Spotlight**
```
Stack:
  [GAME CONTENT — full screen]
  [DARK OVERLAY — Colors.black.withOpacity(0.7)]
  [CUTOUT HOLE — BlendMode.clear around target widget]
  [TOOLTIP CARD — glassmorphism, below/above target]
  [HAND POINTER — animated bounce toward target]
```

**Onboarding color:**
- Keep base game colors — do NOT switch to gray
- Spotlight cutout: clean, no border (relies on contrast)
- Tooltip: white or glass card, brand accent border

### 4.3 Main Lobby / Menu Screen

**Layout zones:**
```
TOP (status bar area, 60–80px):
  [Avatar + Level + XP bar] ←left  [Currency coins/gems] ←right

CENTER (hero zone, 45% height):
  [Main CTA button — large, pulsing]
  [Secondary actions — 2–3 smaller buttons]

BOTTOM NAV (safe area bottom):
  [5 tab icons — play, shop, profile, leaderboard, settings]
```

**Clash Royale proven patterns:**
- Yellow for primary CTA (Enter Battle / main action)
- Green for secondary positive actions (Donate, Upgrade)
- Red exclusively for destructive / notifications
- Blue for neutral backgrounds and less important elements
- Bottom navigation always visible for cross-section access
- Card-based content grid with rarity color borders

**Background patterns:**
- Particle system (stars, embers, sparkles) layered behind main content
- Animated character/mascot in hero zone
- Subtle parallax: background moves slower than foreground on scroll/tilt

### 4.4 HUD (In-Game)

**Corner-based layout (standard mobile):**
```
TOP-LEFT:     Health bar + avatar icon
TOP-CENTER:   Timer / round info
TOP-RIGHT:    Score / currency gained
BOTTOM-LEFT:  Ability buttons
BOTTOM-RIGHT: Special/ultimate button (larger)
BOTTOM-CENTER:Joystick or action area
```

**Key HUD principles:**
- Keep minimal — 20% screen real estate max
- All HUD elements in the "safe zone" (44px from edges on notched phones)
- Important info (HP, score) readable at a glance — no squinting
- Use color-coded status (green HP normal, yellow warning, red critical)
- Animate HP bar loss (shake + red flash)
- Allow player customization (size, position) as advanced option

**Mobile HUD safe zone positions (thumb reach):**
- Easy zone (bottom 33%): primary action buttons
- Stretch zone (middle 33%): secondary info displays
- Hard zone (top 33%): passive info only (score, timer)

### 4.5 Leaderboard / Score Screen

**Layout pattern:**
```
[BACKGROUND — dark gradient or game theme art]
[HEADER — "Leaderboard" or "Top Players", large bold]
[#1 PODIUM — larger card, gold border, crown icon, floating]
[#2 RANK CARD — silver border, slightly smaller]
[#3 RANK CARD — bronze border, slightly smaller]
[DIVIDER or separator]
[SCROLLABLE LIST — ranks 4–100]
  Each row: [Rank #] [Avatar] [Name] [Score] [Delta +/-]
[YOUR RANK — sticky bottom card, highlighted]
```

**Rank card visual hierarchy:**
- Gold `#D4AF37` border for #1
- Silver `#C0C0C0` border for #2
- Bronze `#CD7F32` border for #3
- Own row: brand accent color border + subtle glow
- Delta arrows: green ↑ = improving, red ↓ = dropping

**Score counter animation:**
- Count up from 0 to final value on screen enter
- Duration: 1200–1500ms with easeOut curve
- Particle burst when score reaches final value
- Haptic feedback at milestones

### 4.6 Achievement / Badge Screen

**Badge visual anatomy:**
```
[OUTER RING — rarity color: common gray, rare blue, epic purple, legendary gold]
[BADGE BACKGROUND — themed shape: hexagon, shield, star, circle]
[ICON — game-relevant symbol, white/gold]
[RARITY GLOW — box shadow, 8–16px blur, rarity color]
[LOCK OVERLAY — dark translucent for unearned]
```

**Screen layout:**
```
[TITLE "Achievements" + count progress (14/50)]
[CATEGORY TABS — All, Combat, Collection, Social]
[GRID 2–3 columns of badge cards]
  Each card:
    [Badge icon (large, 72–80px)]
    [Achievement name — 13sp bold]
    [Short description — 11sp muted]
    [Progress bar — if partial]
[NEWLY EARNED — animated entrance, gold glow pulsing]
```

**Unlock celebration pattern:**
- Badge scales from 0 to 1.2 then settles at 1.0 (spring bounce)
- Particle burst: gold sparks for legendary, colored for others
- Screen flash: brief white or gold overlay (80ms, opacity 0.3)
- Sound (visual hint via animation for mute): ring/chime implied by shine sweep

### 4.7 Shop / In-App Purchase Screen

**Psychological design patterns:**
- Highlight "best value" option with size offset + badge ("MOST POPULAR")
- Show concrete benefits as numbers: "Save 30%" over abstract value
- Social proof: "12,847 players chose this pack"
- Limited time: countdown timer on sale items (urgency)
- "First purchase" highlight for new players (conversion hook)

**Layout:**
```
[HEADER — "Shop" + current currency balance]
[FEATURED DEAL — hero card, full width, animated shine]
[CATEGORY TABS — Coins, Gems, Bundles, Cosmetics]
[PRODUCT GRID — 2 columns]
  Each card:
    [Product image / icon]
    [Product name]
    [Contents list — quick icons]
    [Price — large bold]
    [Savings badge — "SAVE 40%"]
[RESTORE PURCHASES — small link, legal requirement]
```

**Shop color cues:**
- Sale/discount: red `#FF3B30` or orange badge
- Best value: green `#34C759` or gold badge
- Premium/exclusive: purple with shimmer
- Currency icons: coin = gold, gem = blue/teal, premium = purple

### 4.8 Game Result Screen (Win/Lose)

**WIN pattern:**
```
[GOLDEN RAYS / particle burst — radial from center]
["VICTORY" or "WIN!" — large, bold, gold gradient text]
[Star rating — 1–3 stars, staggered scale-in animation]
[Score / XP gained — counter animation]
[Rewards row — coins, XP, items revealed one by one]
[CTA buttons — "Play Again" (primary) + "Menu" (secondary)]
```

**LOSE pattern:**
```
[MUTED background — desaturated or dark overlay]
["GAME OVER" — red or dark text, no gold]
[Score — shown but not celebrated]
[Tips or "Try Again" message]
[CTA — "Try Again" (primary) + "Menu" (secondary)]
[Optional: watch ad for extra life / retry]
```

**Timing sequence (WIN):**
1. Background rays: 0ms, fadeIn 400ms
2. Title text: 200ms delay, scaleIn + fadeIn 500ms
3. Stars: 500ms, staggered 150ms each, spring bounce
4. Score counter: 800ms, countUp 1200ms
5. Rewards: 1500ms, staggered slide-up 100ms each
6. CTA buttons: 2000ms, fadeIn slideUp 300ms
7. Confetti loop: starts at 200ms, continuous 3s

---

## 5. Animation Patterns & Timing

### 5.1 Universal Animation Timing Guidelines

| Animation Type | Duration | Curve | Notes |
|---------------|----------|-------|-------|
| Page entrance | 350–450ms | easeOut | Slide + fade |
| Modal popup | 300–400ms | easeOutBack | Scale from 0.8 + fade |
| Button tap | 80–120ms | easeInOut | Scale down 0.95, release |
| Score counter | 1000–1500ms | easeOut | Count up from 0 |
| Achievement unlock | 400–600ms | spring | Scale 0→1.2→1.0 |
| List stagger | 80–100ms per item | easeOut | FadeIn + slideX |
| HUD alert | 200ms in, 150ms out | easeOut | Flash or pulse |
| Victory screen | Sequenced (see §4.8) | mixed | Orchestrated timing |
| Loading pulse | 1200ms loop | easeInOut | Scale 1.0→1.04 |
| Tab switch | 200–250ms | easeInOut | Fade crossfade |
| Shine/shimmer sweep | 800–1200ms loop | linear | Left to right |
| Confetti burst | 3000ms | physics | Gravity + spread |
| Coin/XP gain | 600–800ms | easeOutBack | Float up + fade |

### 5.2 Rule: Perception Sweet Spot
- Under 100ms: feels instant (use for touch feedback)
- 100–300ms: feels responsive (use for state changes)
- 300–500ms: feels smooth (use for transitions)
- 500–1000ms: feels deliberate (use for celebrations/reveals)
- Over 1000ms: feels slow (use only for countdowns or cinematic moments)

### 5.3 Particle Effect Recipes

**Victory Confetti:**
- Use `confetti` package: `ConfettiWidget`
- `numberOfParticles: 50`
- `maxBlastForce: 20, minBlastForce: 8`
- `emissionFrequency: 0.05`
- `gravity: 0.2`
- Colors: game brand palette + gold

**Star Burst:**
- Use `newton_particles` with star emitter
- Golden particles + white particles
- `emitDuration: 800ms`, `lifetime: 1500ms`

**Ambient Sparkles (lobby background):**
- Use `particles_flutter` or `particles_network`
- Low particle count (20–40), slow drift
- Opacity 0.3–0.6, small size 2–4px
- Colors: tinted to match palette (not pure white)

**XP/Coin Float-Up:**
- Custom `AnimatedBuilder` or `flutter_animate`
- Start at reward origin, float up 80px
- Fade out in last 30% of animation
- Scale 1.0→0.6 as it rises
- Duration: 700ms, curve: easeOut

### 5.4 Glow Effect Patterns

**Text Glow (neon score):**
```dart
Stack(
  children: [
    // Blur layer (glow)
    Text(score, style: TextStyle(
      color: glowColor.withOpacity(0.6),
      fontSize: 48,
      fontWeight: FontWeight.bold,
    )).animate().blur(begin: 8, end: 8), // static blur
    // Sharp text on top
    Text(score, style: TextStyle(
      color: Colors.white,
      fontSize: 48,
      fontWeight: FontWeight.bold,
    )),
  ],
)
```

**Widget Glow (button/badge):**
```dart
Container(
  decoration: BoxDecoration(
    borderRadius: BorderRadius.circular(16),
    boxShadow: [
      BoxShadow(
        color: accentColor.withOpacity(0.6),
        blurRadius: 20,
        spreadRadius: 2,
      ),
      BoxShadow(
        color: accentColor.withOpacity(0.3),
        blurRadius: 40,
        spreadRadius: 4,
      ),
    ],
  ),
  child: ...,
)
```

### 5.5 Shimmer/Shine Sweep
```dart
// Shine animation across a button or card
ShaderMask(
  shaderCallback: (bounds) => LinearGradient(
    begin: Alignment(-1.0 + shineValue * 2, 0),
    end: Alignment(shineValue * 2, 0),
    colors: [
      Colors.transparent,
      Colors.white.withOpacity(0.3),
      Colors.transparent,
    ],
    stops: [0.0, 0.5, 1.0],
  ).createShader(bounds),
  child: Container(...),
)
// Animate shineValue 0.0→1.0 in 1000ms, repeat with 2000ms pause
```

### 5.6 Spring Bounce for Achievements/Badges
```dart
// With flutter_animate:
badgeWidget
  .animate(onPlay: (c) => c.forward())
  .scale(
    begin: const Offset(0, 0),
    end: const Offset(1, 1),
    duration: 500.ms,
    curve: Curves.elasticOut,
  )
  .fadeIn(duration: 200.ms)
```

---

## 6. Flutter Implementation Recipes

### 6.1 Glassmorphism Card (Game Menu Panel)

```dart
class GlassGameCard extends StatelessWidget {
  final Widget child;
  final double blurSigma;
  final Color tintColor;
  final double borderRadius;

  const GlassGameCard({
    required this.child,
    this.blurSigma = 18,
    this.tintColor = const Color(0x26FFFFFF), // white 15%
    this.borderRadius = 20,
  });

  @override
  Widget build(BuildContext context) {
    return ClipRRect(
      borderRadius: BorderRadius.circular(borderRadius),
      child: BackdropFilter(
        filter: ImageFilter.blur(sigmaX: blurSigma, sigmaY: blurSigma),
        child: Container(
          decoration: BoxDecoration(
            color: tintColor,
            borderRadius: BorderRadius.circular(borderRadius),
            border: Border.all(
              color: Colors.white.withOpacity(0.2),
              width: 1.2,
            ),
          ),
          child: child,
        ),
      ),
    );
  }
}
```

**Performance note:** Use at most 2–3 BackdropFilter widgets per screen. For non-interactive decorative blur, use `ImageFiltered` widget instead — it is cheaper than BackdropFilter.

### 6.2 Neon Gradient Text (Score Display)

```dart
class NeonScoreText extends StatelessWidget {
  final String text;
  final Color glowColor;

  const NeonScoreText({required this.text, required this.glowColor});

  @override
  Widget build(BuildContext context) {
    return Stack(
      alignment: Alignment.center,
      children: [
        // Glow layer
        Text(
          text,
          style: TextStyle(
            fontSize: 64,
            fontWeight: FontWeight.bold,
            fontFamily: 'Orbitron', // or Rajdhani
            foreground: Paint()
              ..color = glowColor.withOpacity(0.7)
              ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 12),
          ),
        ),
        // Gradient text layer
        ShaderMask(
          shaderCallback: (bounds) => LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [Colors.white, glowColor],
          ).createShader(bounds),
          child: Text(
            text,
            style: const TextStyle(
              fontSize: 64,
              fontWeight: FontWeight.bold,
              fontFamily: 'Orbitron',
              color: Colors.white, // required for ShaderMask
            ),
          ),
        ),
      ],
    );
  }
}
```

### 6.3 HUD Health Bar with Animated Depletion

```dart
class GameHealthBar extends StatelessWidget {
  final double healthPercent; // 0.0 to 1.0
  final Color barColor;

  const GameHealthBar({required this.healthPercent, required this.barColor});

  Color get _barColor {
    if (healthPercent > 0.5) return const Color(0xFF4CAF50);      // green
    if (healthPercent > 0.25) return const Color(0xFFFF9800);     // orange
    return const Color(0xFFF44336);                                 // red
  }

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        // Background track
        Container(
          height: 10,
          decoration: BoxDecoration(
            color: Colors.black.withOpacity(0.5),
            borderRadius: BorderRadius.circular(5),
          ),
        ),
        // Animated fill
        AnimatedFractionallySizedBox(
          widthFactor: healthPercent.clamp(0.0, 1.0),
          duration: const Duration(milliseconds: 400),
          curve: Curves.easeOut,
          child: Container(
            height: 10,
            decoration: BoxDecoration(
              color: _barColor,
              borderRadius: BorderRadius.circular(5),
              boxShadow: [
                BoxShadow(
                  color: _barColor.withOpacity(0.6),
                  blurRadius: 8,
                  spreadRadius: 1,
                ),
              ],
            ),
          ),
        ),
      ],
    );
  }
}
```

### 6.4 Dark Radial Gradient Background (Lobby / Result)

```dart
// Typical game screen background with radial spotlight
Container(
  decoration: BoxDecoration(
    gradient: RadialGradient(
      center: const Alignment(0, -0.3), // slightly above center
      radius: 0.85,
      colors: [
        const Color(0xFF1B2A41),  // surface color
        const Color(0xFF0B0F1A),  // deep background
      ],
      stops: const [0.0, 1.0],
    ),
  ),
)

// Or multi-stop cinematic gradient
Container(
  decoration: const BoxDecoration(
    gradient: LinearGradient(
      begin: Alignment.topCenter,
      end: Alignment.bottomCenter,
      colors: [
        Color(0xFF0B1026),
        Color(0xFF1A2040),
        Color(0xFF0B0F1A),
      ],
      stops: [0.0, 0.5, 1.0],
    ),
  ),
)
```

### 6.5 Achievement Badge with Rarity Glow

```dart
class RarityBadge extends StatelessWidget {
  final IconData icon;
  final BadgeRarity rarity;
  final bool isUnlocked;

  Color get _rarityColor => switch (rarity) {
    BadgeRarity.common    => const Color(0xFF9E9E9E),
    BadgeRarity.rare      => const Color(0xFF2196F3),
    BadgeRarity.epic      => const Color(0xFF9C27B0),
    BadgeRarity.legendary => const Color(0xFFFFD700),
  };

  @override
  Widget build(BuildContext context) {
    return AnimatedOpacity(
      opacity: isUnlocked ? 1.0 : 0.35,
      duration: const Duration(milliseconds: 300),
      child: Container(
        width: 80, height: 80,
        decoration: BoxDecoration(
          shape: BoxShape.circle,
          color: const Color(0xFF1B263B),
          border: Border.all(color: _rarityColor, width: 2.5),
          boxShadow: isUnlocked ? [
            BoxShadow(
              color: _rarityColor.withOpacity(0.5),
              blurRadius: 16,
              spreadRadius: 2,
            ),
            BoxShadow(
              color: _rarityColor.withOpacity(0.25),
              blurRadius: 32,
              spreadRadius: 4,
            ),
          ] : null,
        ),
        child: Icon(icon, color: isUnlocked ? _rarityColor : Colors.grey, size: 36),
      ),
    );
  }
}

enum BadgeRarity { common, rare, epic, legendary }
```

### 6.6 Animated Score Counter

```dart
// Using flutter_animate:
Text(
  '${score}',
  style: const TextStyle(fontSize: 48, fontWeight: FontWeight.bold),
)
.animate()
.custom(
  duration: 1200.ms,
  curve: Curves.easeOut,
  builder: (context, value, child) {
    return Text(
      '${(value * targetScore).round()}',
      style: const TextStyle(fontSize: 48, fontWeight: FontWeight.bold),
    );
  },
)

// Or with AnimatedSwitcher for digit flip:
AnimatedSwitcher(
  duration: const Duration(milliseconds: 200),
  transitionBuilder: (child, animation) => ScaleTransition(
    scale: animation,
    child: child,
  ),
  child: Text(
    '$score',
    key: ValueKey(score),
    style: const TextStyle(
      fontSize: 48,
      fontFeatures: [FontFeature.tabularFigures()],
    ),
  ),
)
```

### 6.7 Button Pulse Animation (Main CTA)

```dart
// Infinite slow pulse for the primary game start button:
primaryButton
  .animate(onPlay: (c) => c.repeat(reverse: true))
  .scale(
    begin: const Offset(1.0, 1.0),
    end: const Offset(1.04, 1.04),
    duration: 1200.ms,
    curve: Curves.easeInOut,
  )
  .then()
  .shimmer(duration: 600.ms, color: Colors.white.withOpacity(0.15))
```

### 6.8 Victory Screen Orchestrated Animation

```dart
// Use flutter_animate .animate() with delays for orchestrated entrance:

Column(children: [
  // Background rays — immediate
  RaysWidget().animate().fadeIn(duration: 400.ms),

  // Title
  Text('VICTORY!')
    .animate(delay: 200.ms)
    .scale(begin: Offset(0.5, 0.5), curve: Curves.elasticOut, duration: 600.ms)
    .fadeIn(duration: 300.ms),

  // Stars
  Row(children: List.generate(3, (i) =>
    StarWidget()
      .animate(delay: (500 + i * 150).ms)
      .scale(begin: Offset(0, 0), curve: Curves.elasticOut, duration: 500.ms)
  )),

  // Score
  ScoreWidget()
    .animate(delay: 800.ms)
    .slideY(begin: 0.5, duration: 400.ms, curve: Curves.easeOut)
    .fadeIn(duration: 300.ms),

  // Reward items (staggered)
  ...rewards.mapIndexed((i, reward) =>
    RewardItem(reward)
      .animate(delay: (1500 + i * 100).ms)
      .slideY(begin: 0.3, duration: 350.ms, curve: Curves.easeOut)
      .fadeIn(duration: 250.ms)
  ),

  // CTA Buttons
  ButtonRow()
    .animate(delay: 2000.ms)
    .slideY(begin: 0.4, duration: 400.ms, curve: Curves.easeOut)
    .fadeIn(duration: 300.ms),
])
```

---

## 7. Top Game UI References

### 7.1 Clash Royale (Supercell)
**Distinctive elements:**
- Color system tied to function: yellow=primary CTA, green=positive secondary, red=danger/notification, blue=background
- Bottom tab navigation always visible
- Card-based content with rarity borders (common/rare/epic/legendary)
- In-game HUD: corner-based, minimal — HP top corners, elixir bar at bottom
- Trophy/rank system with clear visual progress
- Chest unlock system: clear countdown timers, slot-based visualization
- Matchmaking loading: animated arena, opponent profile reveal

### 7.2 Duolingo
**Distinctive gamification elements:**
- Color carries meaning (see §2.6)
- Streak fire: character transformation milestone animation (phoenix)
- XP bar always visible, fills with satisfying animation
- League system (5 tiers) with podium visualization
- Hearts system: red hearts in HUD-like position, lose = break animation
- Completion celebration: screen fills, character animates, XP explodes
- Progress path: nodes on a winding path (world map metaphor)
- Nudge notifications: time-based, loss-aversion framing

### 7.3 Chess.com
**Distinctive elements:**
- Clean, distraction-free board — UI shrinks to minimum during play
- Customizable themes (board wood textures, piece sets, background art)
- Move history scrollable sidebar (subtle, not dominant)
- Analysis mode: colored arrows and highlighting on board
- Dark theme as default for premium/focus feel
- Profile system: avatar, rating ELO prominently displayed

### 7.4 Wordle (NYT)
**Distinctive elements:**
- Extreme minimalism — almost no chrome UI, word grid IS the game
- Tile flip animation is core delight: 3D flip reveals color
- Color system (green/yellow/gray) is the entire feedback system
- Daily limitation creates artificial scarcity/ritual
- Share as emoji grid: made it viral

### 7.5 Pattern Summary: What Makes These UIs Distinctive

| Game | Core UI Principle |
|------|-------------------|
| Clash Royale | Function-coded colors + corner HUD + card system |
| Duolingo | Color = emotion + streak identity + celebration rewards |
| Chess.com | Minimal chrome during play + rich customization |
| Wordle | Feedback IS the design — tile animation = UI |
| Any gacha | Rarity glow + chest opening anticipation |
| Any battle royale | Radial minimalist HUD + ping/map in corner |

---

## 8. Layout & Ergonomics

### 8.1 Thumb Reachability Zones (iOS portrait)

```
SCREEN HEIGHT ZONES:

TOP 30% — HARD TO REACH
  → Place: passive info only (score, timer, opponent name)
  → Avoid: tap targets here

MIDDLE 37% — STRETCH ZONE
  → Place: secondary actions, content display
  → Tap targets ok but not ideal

BOTTOM 33% — EASY ZONE
  → Place: primary CTAs, navigation, joystick/action buttons
  → This is where fingers naturally rest
```

**Rule:** Primary game action (attack, submit, next) should always be in bottom 33%.

### 8.2 iOS Safe Areas

- Status bar: 44–59px top (varies by device notch)
- Home indicator: 34px bottom
- Side notch gutters: 0px (full width ok for background, not for tap targets)
- Minimum tap target: 44×44 px (WCAG / Apple HIG requirement)

### 8.3 Bottom Navigation (game hub)

- 5 items maximum (5-tab = common pattern)
- Icon + label at 10–11sp
- Active tab: accent color icon + colored dot/underline
- Inactive: gray muted icon
- Badge (red dot): notification count for shop/mail items
- Height: 49px + safe area bottom

### 8.4 Grid Systems

| Content type | Columns | Gutters | Card radius |
|-------------|---------|---------|-------------|
| Achievements | 3 | 12px | 16px |
| Shop items | 2 | 16px | 20px |
| Card collection | 4 (small) / 3 | 8px / 12px | 12px |
| Level select | 1 (scroll) | 16px | 24px |

---

## 9. iOS 2025 Liquid Glass Trend

Apple unveiled **Liquid Glass** at WWDC 2025 — an evolution of glassmorphism that defines iOS 26.

### 9.1 Core Properties
- **Physically accurate refraction**: glass panels lens and refract content beneath them
- **Real-time responsiveness**: tint, opacity, and contrast adapt dynamically to content and ambient light
- **Bubble-based chrome**: UI elements detach from screen edges into floating bubbles that appear/disappear contextually
- **Metal 4 accelerated**: GPU-driven; smooth on modern devices

### 9.2 Visual Specification
- Background: deep gradient (stays dark)
- Glass panel: `Colors.white.withOpacity(0.12–0.18)` + `ImageFilter.blur(sigma: 16–24)`
- Border: `Colors.white.withOpacity(0.18–0.25)`, width 1.0–1.5
- Corner radius: 20–28px (Apple default 24px for cards)
- Shadow: `Colors.black.withOpacity(0.25)`, blurRadius 20–30

### 9.3 Flutter Implementation (Liquid Glass style)

```dart
// liquid_glass_widgets package (pub.dev) — or custom:
Widget liquidGlassPanel({required Widget child}) {
  return ClipRRect(
    borderRadius: BorderRadius.circular(24),
    child: BackdropFilter(
      filter: ImageFilter.blur(sigmaX: 20, sigmaY: 20),
      child: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [
              Colors.white.withOpacity(0.18),
              Colors.white.withOpacity(0.08),
            ],
          ),
          borderRadius: BorderRadius.circular(24),
          border: Border.all(
            color: Colors.white.withOpacity(0.22),
            width: 1.2,
          ),
        ),
        child: child,
      ),
    ),
  );
}
```

### 9.4 Accessibility Warning
Liquid Glass can create contrast issues on complex backgrounds. In game UI:
- Ensure text over glass has contrast ratio >= 4.5:1
- Always test with white AND dark backgrounds
- Provide a "high contrast" mode that disables blur effects

---

## 10. ADS Framework Integration Cheatsheet

This section maps the above patterns to ADS Framework conventions.

### 10.1 Color Mapping Strategy

Since ADS uses `AppColors` exclusively, create semantic game color slots:

```dart
// Suggested additions to AppColors for game projects:
// Primary game accent (neon/brand)
static const Color gameAccent = Color(0xFF00F5FF); // or brand neon
// Warning / urgency
static const Color gameWarning = Color(0xFFFF9500);
// Danger / enemy / health critical
static const Color gameDanger = Color(0xFFFF3B30);
// Gold / reward
static const Color gameGold = Color(0xFFD4AF37);
// Success / correct
static const Color gameSuccess = Color(0xFF4CAF50);
// XP / progress
static const Color gameXP = Color(0xFFC17CFF);
// Background deep
static const Color gameBgDeep = Color(0xFF0B0F1A);
// Background surface
static const Color gameSurface = Color(0xFF1B2A41);
```

### 10.2 LayoutStyle Conventions for Game UI

```dart
// For game card panels (glass style):
LayoutStyle.card.copyWith(
  borderRadius: BorderRadius.circular(20),
  // Add boxShadow as wrapper Container (per ADS rules)
)

// For game HUD pills:
LayoutStyle.button.copyWith(
  borderRadius: BorderRadius.circular(24), // pill
)
```

### 10.3 flutter_animate Game Patterns

```dart
// Page entrance (all game pages):
pageContent
  .animate()
  .fadeIn(duration: 400.ms)
  .slideY(begin: 0.08, duration: 400.ms, curve: Curves.easeOut)

// Modal entrance:
modalWidget
  .animate()
  .fadeIn(duration: 300.ms)
  .scale(begin: Offset(0.85, 0.85), duration: 400.ms, curve: Curves.easeOutBack)

// Achievement unlock:
badge
  .animate()
  .scale(begin: Offset(0, 0), duration: 500.ms, curve: Curves.elasticOut)
  .fadeIn(duration: 200.ms)

// Staggered list (leaderboard rows):
// Apply in ListView.builder:
rowWidget
  .animate(delay: (index * 80).ms)
  .fadeIn(duration: 300.ms)
  .slideX(begin: -0.15, duration: 300.ms, curve: Curves.easeOut)

// Main CTA pulse:
ctaButton
  .animate(onPlay: (c) => c.repeat(reverse: true))
  .scale(
    begin: Offset(1.0, 1.0),
    end: Offset(1.035, 1.035),
    duration: 1200.ms,
    curve: Curves.easeInOut,
  )
```

### 10.4 CustomBounceEffect for Game Buttons

```dart
// All interactive game cards, buttons, badge taps:
CustomBounceEffect(
  scaleFactor: 0.92, // slightly more dramatic than default for game feel
  onTap: () => handleAction(),
  child: gameButton,
)
```

### 10.5 Package Recommendations for Game UI in Flutter

| Need | Package |
|------|---------|
| Particle effects | `newton_particles` |
| Confetti/victory | `confetti` |
| Ambient background | `particles_flutter` or `animated_background` |
| Glow/aura widget | `aura_box` |
| Shimmer effect | `shimmer` (or flutter_animate .shimmer()) |
| Score counter flip | `animated_flip_counter` |
| Fragment shaders | `flutter_shaders` |
| Animated gradient bg | `animate_gradient` |
| Mesh gradient | `mesh_gradient` |
| Glitch effect | `animated_glitch` |
| Liquid glass native | `liquid_glass_widgets` |

---

## Quick Reference: Common Game Screen Color Setups

### Dark Neon Game (generic)
```
bg: #0B0F1A | surface: #1B2A41 | accent: #00F5FF | gold: #FFD166 | danger: #FF3B30
```

### Fantasy RPG
```
bg: #2D1B0E | surface: #3D2512 | gold: #FFB703 | purple: #C17CFF | silver: #E0E1DD
```

### Sci-Fi/Space
```
bg: #0B1026 | surface: #1A2040 | cyan: #00D1FF | green: #00FFA3 | purple: #A259FF
```

### Sports/Competitive
```
bg: #0B0C10 | surface: #1F2833 | teal: #66FCF1 | white: #F5F5F5 | danger: #FF3B30
```

### Casual/Candy
```
bg: #FFFFFF | surface: #F0F4FF | pink: #FF5DA2 | yellow: #FFC800 | green: #4CAF50
```

---

*Sources used in compiling this reference:*
- [Zvky Design Studio — Top 7 Art Styles 2025](https://www.zvky.com/blogs/articles/top-7-art-styles-dominating-mobile-games-in-2025)
- [media.io — 22 Gaming Color Palettes with Hex](https://www.media.io/color-palette/gaming-color-palette.html)
- [coloruxlab.com — 30+ Neon Color Palettes](https://coloruxlab.com/colors/neon-colors)
- [fluttergems.dev — Effects, Gradients & Shaders packages](https://fluttergems.dev/effects-gradients-shaders/)
- [pub.dev — flutter_animate](https://pub.dev/packages/flutter_animate)
- [pub.dev — newton_particles](https://pub.dev/packages/newton_particles)
- [Glassmorphism in Flutter — Medium](https://medium.com/@rohitsurage/build-beautiful-glassmorphism-ui-in-flutter-a-beginner-to-advanced-guide-023594a473b3)
- [Apple Liquid Glass / iOS 26 — EverydayUX](https://www.everydayux.net/glassmorphism-apple-liquid-glass-interface-design/)
- [Duolingo streak animation — Duolingo Blog](https://blog.duolingo.com/streak-milestone-design-animation/)
- [Duolingo gamification — Orizon](https://www.orizon.co/blog/duolingos-gamification-secrets)
- [Clash Royale UX breakdown — The Rookies](https://www.therookies.co/blog/game-design-ux-best-practices-detailed-breakdown-of-clash-royale/)
- [Game UI Database](https://gameuidatabase.com/)
- [Minimal UI Mobile Game Trends 2025 — LinkedIn](https://www.linkedin.com/pulse/minimal-ui-maximum-impact-mobile-game-trends-2025-sunil-khobragade-x1edf)
- [Mobile Game Design 2024 — Game-Ace](https://game-ace.com/blog/mobile-game-design/)
- [Flutter BackdropFilter docs](https://api.flutter.dev/flutter/widgets/BackdropFilter-class.html)
- [Flutter ShaderMask docs](https://api.flutter.dev/flutter/widgets/ShaderMask-class.html)
- [Fragment Shaders in Flutter — Flutter Docs](https://docs.flutter.dev/ui/design/graphics/fragment-shaders)
- [Smashing Magazine — Animated Progress Indicators](https://www.smashingmagazine.com/2016/12/best-practices-for-animated-progress-indicators/)
- [Thumb zone ergonomics — ParachuteDesign](https://parachutedesign.ca/blog/thumb-zone-ux/)
- [Mobile Game Onboarding — MediumAmol](https://medium.com/@amol346bhalerao/mobile-game-onboarding-top-ux-strategies-that-boost-retention-6ef266f433cb)

---

## 11. Aesthetic Subculture Styles (2024–2025)

Subculture aesthetics from social media (TikTok, Pinterest) are crossing into mobile game UI with growing frequency. Each has a defined visual language.

### 11.1 Cozy / Cottagecore

**Description:** Romanticizes slow, simple rural life — warm, handmade, nostalgic. Exploded in popularity post-2020 as a response to fast-paced stress culture.

**Key visual characteristics:**
- Warm pastel palette: cream, dusty rose, sage green, wheat, lavender
- Soft round edges everywhere (border radius 24–32px)
- Watercolor textures or linen paper backgrounds
- Hand-drawn or sketched icon style (not pixel-perfect)
- Abundant whitespace, never crowded
- Wooden or wicker UI frame textures
- Seasonal nature motifs (mushrooms, flowers, leaves, bees, candles)

**Color palette:**
```
Background:  #FDF6EC  (warm parchment)
Surface:     #F5E6D3  (light wood)
Accent warm: #D4845A  (terracotta)
Accent cool: #8FAF7E  (sage green)
Text:        #4A3728  (dark brown)
Soft pink:   #E8B4B8  (dusty rose)
```

**Representative games:** Stardew Valley (concept), Cozy Grove, Bear and Breakfast, Spiritfarer, Garden Paws

**What works and why:**
- Triggers the biophilia response — natural elements reduce anxiety
- Low contrast = low cognitive load = longer play sessions
- The imperfect/handmade quality signals authenticity and care
- Reward loops feel "earned" not "pushed"

**Flutter implementation:**
- `GoogleFonts.caveat()` or `PermanentMarker` for headers (handwritten feel)
- `BoxDecoration` with `borderRadius: BorderRadius.circular(28)` everywhere
- Background: `Image.asset` with paper/linen texture + warm gradient overlay
- Buttons: rounded, no sharp corners, warm accent fill
- Avoid neon, harsh shadows, or dark backgrounds entirely

---

### 11.2 Dark Academia

**Description:** Inspired by Gothic university life, classic literature, and 19th century European aesthetics. Intellectual, mysterious, warm-dark.

**Key visual characteristics:**
- Deep warm darks: charcoal, espresso, dark burgundy, dark olive
- Parchment/sepia tones for text areas
- Serif or literary fonts (Cinzel, IM Fell English, Playfair Display)
- Candlelight warm accents (amber, gold ochre)
- Aged paper, wax seal, ink textures
- Quill, book, candle, owl motifs
- High contrast text on dark surfaces

**Color palette:**
```
Background:  #1C1510  (charcoal espresso)
Surface:     #2D2218  (dark walnut)
Parchment:   #D4C5A9  (aged paper)
Gold:        #C4993B  (candle gold)
Burgundy:    #6B2D2D  (dark wine)
Text:        #E8DCC8  (cream)
```

**Representative games:** 80 Days, Inkle Studio games, visual novels with mystery themes

**What works and why:**
- Appeals to the "intellectual identity" desire — makes player feel smart
- Warm darks are less eye-fatiguing than cold darks at night
- Serif fonts signal quality and seriousness
- Scarcity/exclusivity feels inherent (not everything is accessible)

**Flutter implementation:**
- `GoogleFonts.cinzel()` for titles, `GoogleFonts.imFellEnglishSc()` for labels
- Dark gradient backgrounds with warm tints (not blue-black — brown-black)
- Dividers as ornamental rules (thin gold line with flourishes using SVG)
- Card backgrounds: parchment tint over base dark

---

### 11.3 Y2K / Retro-Futurism

**Description:** The aesthetic of 1995–2005 technology optimism. Chrome gradients, CRT glow, pixel fonts, and a sense that "the future is already here."

**Key visual characteristics:**
- Chrome/silver metallic gradients
- Holographic or iridescent color shifts (rainbow sheen)
- Grid lines, scan lines, pixel noise overlays
- Bold geometric shapes (triangles, circles, squares)
- Color system: silver + electric blue + magenta + yellow on white or black
- Chunky rounded fonts (Fredoka, Pacifico) OR techno mono (Orbitron, Share Tech Mono)
- CRT scanline overlay texture (subtle)

**Color palette:**
```
Base:        #FFFFFF  or  #0A0A0A
Chrome:      #C0C0C0 → #FFFFFF  (metallic gradient)
Electric:    #0094FF  (bright web blue)
Magenta:     #FF00CC
Yellow:      #FFFF00
Holographic: rainbow gradient (0° → 360° hue rotation)
```

**Representative games:** Pac-Man 256 (glitch retro), Geometry Dash (neon retro), beat-em-ups with nostalgic arcade skin

**What works and why:**
- Millennials and Gen Z both feel nostalgia — Millennials lived it, Gen Z romanticizes it
- High-energy chrome/neon reads as "exciting and dynamic"
- Feels premium in a subversive way — deliberately over-the-top
- Ridge Racer T4 proved yellow + silver can feel both luxury and futuristic simultaneously

**Flutter implementation:**
- `ShaderMask` with rainbow `LinearGradient` for holographic text
- `BoxDecoration` with metallic-look gradient (`Colors.grey[300]` → `Colors.white` → `Colors.grey[400]`)
- Scanline overlay: custom `CustomPainter` drawing horizontal lines every 4px at opacity 0.06
- Chunky outline buttons with 2px border + bright accent fill

---

### 11.4 Chibi / Anime Mobile Game Style

**Description:** Anime-influenced with exaggerated "chibi" proportions (large head:body ratio 1:2). Extremely popular in gacha RPGs. Leverages neoteny psychology (juvenile features = emotional attachment).

**Key visual characteristics:**
- Character proportions: head = 40–50% of total height
- Massive expressive eyes (pupil+iris = 60–70% of eye area)
- 6–8 standardized facial emotion states per character
- Background UI: soft gradient panels, flower/star decorative accents
- Tab bars with character face icons
- "Spark" and "star" particle systems everywhere
- Idol-style poses (dynamic, expressive gestures)
- Character cards: portrait framing, rarity glow border

**Color palette:** Bright, saturated, never dull — but not neon
```
Background:  #1A1B2E  (deep midnight blue — common gacha base)
Surface:     #25263D  (dark panel)
Accent 1:    #FFB347  (warm amber)
Accent 2:    #7EC8E3  (soft sky blue)
Pink:        #FF6B9D  (cute pink)
Gold:        #FFD700  (star/reward gold)
Text:        #FFFFFF + #B8C1EC  (white + soft blue)
```

**Representative games:** AFK Journey, Genshin Impact (somewhat), Honkai: Star Rail, Princess Connect, Blue Archive, Arknights

**What works and why:**
- Neoteny = instant emotional bond ("I want to protect this character")
- 6 facial states cover all gameplay feedback needs visually
- Chibi requires fewer polygons → faster load → better retention
- Subtle changes in eye/brow angles convey strong emotions — superior readability
- The "collect all characters" loop is amplified by design investment in each character

**Flutter implementation:**
- Character display: `Image.asset` with transparent PNG, sized to 60–70% screen height
- Live2D-style idle animation: use `rive` package for spine/rive2 integration
- Rarity cards: `Container` with gradient border (`gradient` in `Border` via custom painter)
- Emotion display: swap character PNG asset on state change with `AnimatedSwitcher`

---

### 11.5 Pixel Art / Retro 8-Bit Style

**Description:** Charming low-resolution aesthetic from 1977–1995 gaming era. Strong nostalgia + uniquely readable at any size.

**Key visual characteristics:**
- Deliberate low-resolution pixel grid (8×8 or 16×16 base tile)
- Hard pixel edges — no anti-aliasing
- Limited color palettes (8–64 colors typical)
- Chunky UI chrome with 2–4px border pixels
- Text uses custom bitmap fonts (Press Start 2P, Pixel Intv)
- Sprite sheets for animation (not smooth tweening)
- Dithering for gradients/shading

**Color palettes (classic systems):**
```
NES-inspired: #000000 #0000AB #AB0000 #ABABAB #FFFFFF
GameBoy:      #0F380F #306230 #8BAC0F #9BBC0F
PICO-8:       #000000 #1D2B53 #7E2553 #008751 #AB5236 #5F574F #C2C3C7 #FFF1E8 #FF004D #FFA300 #FFEC27 #00E436 #29ADFF #83769C #FF77A8 #FFCCAA
```

**Representative games:** Afterplace (Apple Design Awards 2023 winner), Stardew Valley, Dead Cells, Shovel Knight

**What works and why:**
- Nostalgia activates positive memory recall → improved mood → longer sessions
- Pixel constraints force clever, readable design solutions
- Highly distinctive — stands out in App Store thumbnails
- Low file size = fast download = lower drop-off

**Flutter implementation:**
- Set `FilterQuality.none` on all pixel art `Image` widgets (prevents blurring)
- Use `GoogleFonts.pressStart2p()` for text
- Avoid `borderRadius` — use sharp 0px corners everywhere
- Scale factor: use integer scaling only (1x, 2x, 3x) — never fractional
- `Image.asset(filterQuality: FilterQuality.none)` is critical

---

### 11.6 Isometric / Voxel Style

**Description:** 3D-looking 2D art rendered at 45° or true isometric projection. Clean, architectural, satisfying spatial puzzle feeling.

**Key visual characteristics:**
- 45° or 26.57° (true isometric) projection angle
- Consistent voxel cube unit as base element
- Bright ambient colors — usually daytime/midday lighting
- Buildings, towns, resource nodes as primary visual vocabulary
- Clean outlines or no outlines (stylized choice)
- Pastel to saturated medium tones

**Color palette:**
```
Sky:         #87CEEB  (light blue)
Grass:       #7EC850  (medium green)
Stone:       #A0A0A0  (neutral gray)
Wood:        #C4944A  (warm brown)
Highlight:   #FFE566  (warm yellow)
Shadow:      #4A6741  (dark green)
```

**Representative games:** Monument Valley 1 & 2, Townscaper, Isometric Worlds, many simulation titles

**What works and why (Monument Valley analysis):**
- Impossible geometry creates intellectual delight and surprise
- Minimalist controls (single tap) removes friction to the "interesting" part
- No failure state = pure exploration pleasure (different from competition)
- The isometric grid provides inherent visual order that feels satisfying
- Pastel desaturated hues minimize eye strain for long sessions

**Flutter implementation:**
- Canvas-based rendering with `CustomPainter` for isometric grids
- Each "tile" = diamond shape drawn with `Path`
- Use `transform` matrices for isometric projection: `Matrix4.rotationX(0.46) * Matrix4.rotationZ(0.78)`
- For static display: pre-rendered PNG spritesheets

---

## 12. Award-Winning Game UI Analysis (2023–2024)

### 12.1 Apple Design Awards 2024 — Games

| Game | Category Won | Key UI Design Principle |
|------|-------------|------------------------|
| NYT Games | Delight & Fun | Perfect mechanic calibration; minimal chrome; daily ritual design |
| Crayola Adventures | Inclusivity | Inclusive character creation with full narration support; colorful accessible interface |
| Lost in Play | Innovation | Graphic novel aesthetic; handcrafted world details; intuitive interactions with no tutorial text |
| Rytmos | Interaction | Simple drag gesture with progressive complexity; visual feedback through music pathways |
| The Wreck | Social Impact | Visual novel format; thought-bubble UI; emotional interface design |
| Lies of P | Visuals & Graphics | Technical showpiece with volumetric fog, detailed lighting, MetalFX upscaling |
| Blackbox | Spatial Computing | Floating bubble spatial UI; creative level selection (soapy floating bubbles) |

**2024 Finalists worth noting for UI:**
- **Rooms:** Nostalgic 8-bit world with lovingly rendered pixel aesthetic
- **Hello Kitty Island Adventure:** Character-driven multi-platform cozy design
- **Honkai: Star Rail:** RPG visual design — soft menu look, balance of functionality and flavor
- **DEATH STRANDING DIRECTOR'S CUT:** Cinematic visuals on mobile

**Key patterns from 2024 winners:**
1. Accessibility is not optional — winners built inclusivity from the ground up
2. Gameplay mechanics that "could be discovered by accident" score highest for interaction
3. Visual novels/narrative games use UI-as-storytelling (thought bubbles, choice framing)
4. Cozy game aesthetic (Hello Kitty, Crayola) dominates "Delight" category

---

### 12.2 Apple Design Awards 2023 — Games

| Game | Category Won | Key UI Design Principle |
|------|-------------|------------------------|
| stitch. | Inclusivity | Relaxing puzzle pace; color-blindness support; multi-language; gentle vibe |
| Afterplace | Delight & Fun | Vintage pixel adventure; swipe/tap controls (no virtual buttons); quirky hidden rewards |
| Railbound | Interaction | Tap-and-drag rail mechanic; scribbled emotion cloud over misplaced pieces; pristine animation |
| Endling | Social Impact | Eco-social narrative; mix of medium and message |
| Resident Evil: Village | Visuals & Graphics | Console-quality mobile visuals |
| Marvel Snap | Innovation | Short snappy gameplay; card game accessibility breakthrough |

**Key patterns from 2023 winners:**
1. "No virtual buttons" is a strong design signal — physical gestures beat button grids
2. Whimsical micro-feedback (scribbled cloud in Railbound) creates personality
3. Pixel art remains award-worthy — Afterplace proved retro can win in 2023
4. Short session design (Marvel Snap) solves casual vs. depth tension

---

### 12.3 Google Play Best Games 2024

| Award | Game | Design Notes |
|-------|------|-------------|
| Best Game of 2024 | AFK Journey | "Canvas Art Style" — painterly fantasy; one-hand exploration; streamlined idle RPG UI |
| Best Pick Up & Play | Eggy Party | Quirky mini-games; charming art style; instant accessibility |
| Competitive Multiplayer | Squad Busters | Fast-paced; quirky design; team-based visual language |

**AFK Journey (Google Play 2024 winner) — detailed UI analysis:**
- Developers call their style "Canvas Art Style" — evoking the feeling of looking at a beautiful painting
- "Magic storybook" aesthetic: soft gradients, illustrated backgrounds, painterly characters
- One-click resonance for hero leveling eliminates friction at upgrade moments
- Character roster (46+ heroes from 6 races) presented in organized card grid
- Resonating Hall merges inventory + upgrade into one intuitive space
- Mobile-first: full exploration with one hand (rare in the genre)
- Improved on AFK Arena's UI by making systems more approachable and error-proof

---

### 12.4 BAFTA Games Awards 2024

- **Game Design winner:** Dave the Diver — hybrid marine adventure with mixed casual/deep gameplay
- No dedicated mobile category at the 2024 ceremony
- Baldur's Gate 3 dominated with 5 awards (PC/console, not mobile)

**Dave the Diver design notes:**
- Combines two completely different play modes: relaxed exploration + tense management
- UI changes tone completely between the two modes (cozy shop vs. action HUD)
- First South Korean game to win BAFTA Game Design — cross-cultural appeal through universal mechanics

---

## 13. Specific Screen Deep Dives

### 13.1 Character / Hero Selection Screen

**Common patterns (RPG style):**

```
Layout A — Carousel:
  [BIG CHARACTER ART — full height, centered]
  [NAME + CLASS — large typography below art]
  [STATS ROW — 4 icons with values: ATK/DEF/SPD/DIFF]
  [LORE SNIPPET — 2 lines, italic, muted]
  [SWIPE LEFT/RIGHT indicator]
  [SELECT button — primary CTA]

Layout B — Grid / Roster:
  [FILTER TABS — All / Class / Rarity]
  [GRID 3–4 columns of character cards]
    Each card: [Portrait] [Name] [Level] [Rarity glow border]
  [SELECTED CHARACTER panel — side panel or bottom sheet]
    [Full art] [Stats] [Abilities preview] [Select button]
```

**Visual anatomy of a character card:**
- Portrait: face-focused, dramatic lighting, unique pose
- Rarity border: common gray → rare blue → epic purple → legendary gold+glow
- Level badge: bottom corner, small pill
- Locked state: dark overlay + lock icon at 40% opacity
- New/Owned: small badge top-right

**Color psychology for hero selection:**
- Gold rarity = aspirational desire (creates want before seeing stats)
- Purple = mysterious premium (different enough from gold to feel distinct)
- Particle aura on selected character: color matches hero's theme

**Flutter implementation:**
```dart
// Character card with rarity glow
Container(
  decoration: BoxDecoration(
    borderRadius: BorderRadius.circular(16),
    border: Border.all(color: rarityColor, width: 2),
    boxShadow: [
      BoxShadow(
        color: rarityColor.withOpacity(0.4),
        blurRadius: 12,
        spreadRadius: 1,
      ),
    ],
  ),
  child: ClipRRect(
    borderRadius: BorderRadius.circular(14),
    child: Image.asset(heroPortrait, fit: BoxFit.cover),
  ),
)
```

---

### 13.2 World Map / Level Select Screen

**Design patterns:**

```
Type A — Path-based (Candy Crush / Duolingo style):
  Winding illustrated path on themed world art
  Nodes = levels, connected by dotted/solid line
  Completed = star-filled, locked = faded lock icon
  Current = pulsing glow node
  Player avatar "sits" on last completed node

Type B — Area map (RPG overworld):
  Illustrated regions with distinct biome art
  Fog of war for unexplored areas
  Region bosses shown as large icons
  Fast travel points highlighted

Type C — Chapter/Stage grid:
  Grid of stages inside chapter panels
  Chapter unlock = sequential
  Boss level: larger card, red/gold highlight
```

**Motion design for world map:**
- Camera pan to player position on screen load
- Completed node: brief particle burst + checkmark settle
- Fog of war reveal: dissolve animation from edges
- Path unlock: draw animation (line appears progressively)

**Cozy games (Stardew / Animal Crossing style):**
- The map IS the game screen (not a separate screen)
- Minimap only: small corner overlay, tap to zoom out to full map
- Seasons change the visual art of the entire map

---

### 13.3 Daily Reward / Login Bonus Screen

**Standard UI pattern:**

```
[MODAL OVERLAY on main screen — semi-transparent dark bg]
[HEADER — "Daily Login Bonus" or "Come back tomorrow!"]
[REWARD CALENDAR — 7 days or 30 days grid]
  Day tiles: [Day number] [Reward icon] [Reward count]
  Today: highlighted, pulsing glow
  Past: dimmed with checkmark
  Future: slightly dimmed but visible (creates anticipation)
[CLAIM button — primary CTA, gold/yellow]
[Streak counter — "Day 5 streak! +50% bonus"]
```

**Psychology principles in use:**
- Loss aversion: "Come back tomorrow or lose your streak!"
- Variable reward schedule: day 7 always a bigger reward (Skinner box)
- Anticipation visibility: show future rewards so player plans to return
- Streak identity: "I'm a 15-day streak player" becomes self-identity

**Visual design tips:**
- Today's reward tile: scale 1.1× + pulsing border glow (gold or brand accent)
- Streak fire icon: animated flicker (use `flutter_animate` with scale + shimmer loop)
- Claim animation: reward icon flies up from tile toward currency counter in HUD
- "Bonus" label: small red badge on any multiplier reward

**Flutter claim animation:**
```dart
// Reward fly-to-counter animation
rewardIcon
  .animate(delay: 200.ms)
  .moveY(begin: 0, end: -200, duration: 600.ms, curve: Curves.easeInCubic)
  .scaleXY(begin: 1.0, end: 0.3, duration: 600.ms)
  .fadeOut(begin: 0.7, duration: 600.ms)
```

---

### 13.4 Fortune Wheel / Spin to Win Screen

**Design anatomy:**

```
[BACKGROUND — dark radial with dramatic lighting]
[WHEEL — large, center screen, 60–70% width]
  Segments: alternating colors, 6–12 segments
  Segment content: reward icon + text
  Outer border: metallic gold ring
  Center hub: decorative button or logo
  Pointer: arrow/indicator at top (12 o'clock)
[SPIN button — primary CTA, bottom center, large]
[Spin count remaining — "3 spins left today"]
[Previous wins — small scrolling ticker below wheel]
```

**Motion principles for wheel spin:**
- Spin up: ease-in for 300ms (feels like it's gaining momentum)
- Spin peak: constant high velocity for 1–2 seconds (excitement peak)
- Decelerate: long ease-out for 1500–2000ms (anticipation maximized)
- Final tick: wheel "ticks" against pointer with haptic feedback every segment
- Land: brief overshoot + snap back 3–5° (spring physics)
- Win reveal: segment glow + particle burst + reward display

**Psychology:** Brian Knutson (Stanford) research confirms: the brain's pleasure center activates in ANTICIPATION of reward, not receipt. The deceleration phase of the wheel = maximum dopamine window. Deliberately prolonging deceleration to 1.5–2s exploits this.

**Color system for wheel:**
- High-value segments: gold/purple (smaller area = rarer)
- Mid-value: blue/green
- Low-value: gray/white (largest segments visually)
- "JACKPOT": uses unique color (hot pink or rainbow gradient)

---

### 13.5 Chest Opening / Loot Reveal Screen

**Standard pattern (3-phase reveal):**

```
Phase 1 — Chest idle:
  [CHEST on pedestal — animated idle (floating, glowing)]
  [TAP TO OPEN instruction — pulsing text]
  [Chest rarity glow — color matches tier]

Phase 2 — Opening animation:
  [Chest shakes/rattles — 3× strong vibration]
  [Crack of light from seam — beam of light shoots up]
  [Chest lid blows off — physics]
  [Blinding flash frame — white/gold screen fill 80ms]

Phase 3 — Reward reveal:
  [Item appears floating with particle halo]
  [Item name — large, bold, rarity color]
  [Rarity tag — "LEGENDARY" in gold caps]
  [Description — brief flavor text]
  [CLAIM button or CONTINUE]
```

**Key delay design:** The pause between Phase 1 → Phase 2 → Phase 3 is deliberate. Each pause is 300–500ms. This "draws out" the anticipation loop. Removing the delays makes the experience feel cheap.

**Multi-item reveal (gacha pull / 10x pull):**
- Items appear one at a time, staggered 300–400ms
- Each item: quick scale-in + rarity flash
- End: all items displayed simultaneously, highest rarity highlighted
- Background color shifts toward highest rarity color earned

**Flutter chest shake animation:**
```dart
chest.animate(
  onPlay: (c) => c.repeat(count: 3),
).shakeX(hz: 4, amount: 8, duration: 500.ms)
 .then()
 .shake(hz: 6, amount: 12, duration: 300.ms)
```

---

### 13.6 Guild War / PvP Hub Screen

**Layout anatomy:**

```
[BACKGROUND — dramatic war art / arena art]
[YOUR GUILD info — left panel]
  [Guild banner + name + rank]
[VS divider — animated glow slash or collision FX]
[ENEMY GUILD info — right panel]
  [Enemy banner + name + rank]
[BATTLE STATUS — center]
  [Score bars: 2 colored progress bars facing each other]
  [Timer countdown — large, urgent]
[BATTLE LOG — bottom scrollable ticker]
[JOIN BATTLE / VIEW BATTLE button — primary CTA]
```

**Color language:**
- Your guild: brand/player color (blue default)
- Enemy guild: contrasting color (red default)
- Tie state: neutral gray
- Winning: your color expands across center
- Losing: alert flashes + color contracts

**Score visualization patterns:**
- Two bars facing each other from opposite sides (tug-of-war style)
- Absolute scores on each side (not just percentages)
- Delta indicator ("+1,200 pts this hour")

---

### 13.7 Season / Chapter Select Screen

**Design patterns:**

```
Horizontal scroll seasons (Battle Pass style):
  [HEADER — current season name + time remaining]
  [Season art — full-bleed key illustration]
  [Progress track — horizontal line with node markers]
  [Free tier vs Premium tier — two parallel tracks]
  [Locked future content — dimmed with lock]
  [SEASON PASS CTA — prominent if unlocked not purchased]

Chapter select (story game):
  [Chapter cards — large illustrated panels]
  [Status: Complete (star rated) / Current / Locked]
  [Chapter title + brief description]
  [Completion percentage shown]
  [Chapter boss portrait — corner icon on card]
```

**Visual storytelling on chapter cards:**
- Each chapter card = unique illustrated scene from the chapter story
- Completed chapters: desaturated slightly + gold star overlay
- Current chapter: full color, animated border glow
- Future chapters: silhouette only (creates intrigue)

---

## 14. Casual & Hypercasual UI Design Patterns

### 14.1 Core Hypercasual Principles

**The less-is-more doctrine:**
- Single mechanic = single visual focus
- One primary CTA per screen (never two equal-weight buttons)
- Implicit tutorial: arrows, highlights, animated hand pointer — NO text instructions
- Zero-latency feedback: every tap produces visual + audio response within 16ms
- One-tap restart: crucial for flow state retention after failure

**Screen count for hypercasual:**
```
Minimum viable flow:
  Main Menu (1 screen) → Gameplay → Result (1 screen)

Recommended:
  Splash → Main Menu → Gameplay → Result → (optional: Shop/Skin)
```

**Typography rule:** One font, max 2 weights. No serifs. No decorative fonts.

---

### 14.2 Casual Game UI Patterns

**Idle / Clicker game UI:**
```
[MAIN SCREEN — auto-generates currency in view]
  [Big click button or progress zone — center, large]
  [Currency display — top, large, counter always updating]
  [Upgrade shop — bottom scrollable panel]
    Upgrade row: [Icon] [Name] [Level] [Effect] [Cost] [BUY button]
  [Prestige/rebirth — late-game, hidden until threshold]
```

**Key idle game UI principles:**
- Numbers must always be moving (idle games live on the dopamine of seeing numbers grow)
- Use k/M/B abbreviations after 999 (never show 8 digits raw)
- Upgrade cards that become available should animate into view (bounce in)
- "Offline earnings" popup on return = immediate positive reinforcement

**Merge game UI:**
```
[GRID — central focus, 4×4 to 6×7]
  Each cell: item at various merge levels
  Merging: items move together with snap animation
  Next merge preview: ghost item shows what 2+2 will make
[SPAWN button — bottom, produces new item]
[Goal card — shows what to collect for chapter clear]
[MERGE hint — animated arrows when player is stuck]
```

**Runner game HUD:**
```
[Score — top center, large, constantly incrementing]
[Distance or coins — secondary, smaller]
[Power-up indicators — top corners, timer bars]
[Lives/hearts — top right (if applicable)]
[PAUSE button — top right corner, subtle]
```

**Runner HUD color principle:** Everything must be legible at a glance while player is focused on obstacles. Use:
- White text + dark drop shadow (not outline) for score
- Icon-based power-up display (not text)
- Avoid any elements that require reading during play

---

### 14.3 Puzzle Game Minimal UI

**Monument Valley / Alto pattern:**
- UI chrome = nearly zero
- Score/progress shown only between levels
- In-level: no HUD except occasional hint button (small, corner, appears only when idle 30s)
- Transition: the level itself is the interface

**Wordle/Word puzzle pattern:**
- The game grid IS the UI — no separation
- Color-coded feedback replaces all explicit explanations
- Keyboard at bottom = natural thumb zone
- Header: minimal — just title + settings icon

**Flip-tile animation (Wordle style):**
```dart
// 3D flip reveal animation:
TweenAnimationBuilder<double>(
  tween: Tween(begin: 0, end: 1),
  duration: const Duration(milliseconds: 500),
  builder: (context, value, child) {
    return Transform(
      alignment: Alignment.center,
      transform: Matrix4.rotationX(pi * value),
      child: value < 0.5
        ? tile_front
        : Transform(
            transform: Matrix4.rotationX(pi),
            child: tile_back_colored,
          ),
    );
  },
)
```

---

## 15. App Store / Play Store Marketing UI Patterns

### 15.1 App Icon Design Rules (2024–2025)

**What drives installs:**
- Optimizing app icon = up to 25% increase in conversion rate
- Bold single focal element outperforms complex compositions
- Genre color conventions are real: action games use black/red, casual use bright/pastels

**Icon design by genre:**
| Genre | Dominant Colors | Focal Element |
|-------|----------------|---------------|
| Action/Shooter | Black, red, brown | Weapon or explosion |
| RPG/Fantasy | Gold, purple, dark | Hero face or armor |
| Casual Puzzle | Bright, pastel | Character face or key item |
| Simulation/Cozy | Green, warm tones | Structure or character |
| Racing | Red, yellow, metallic | Vehicle or speedlines |
| Word/Trivia | White, blue, yellow | Letter tile or light bulb |

**Icon trends 2024–2025:**
- 3D depth: even "flat" icons now use lighting/shadow to suggest 3D
- Character close-up: a face with expression > a scene every time
- Minimal background: 1–2 color gradient only, character fills 80% of icon
- No text in icon (App Store shows name below)

### 15.2 Screenshot Design Patterns

**Panoramic gallery trend:**
- Multi-screenshots form one continuous image (forces swiping)
- Increases conversion rate up to 40%
- Requires consistent frame/background across all 5 screenshots

**Screenshot anatomy:**
```
Screenshot 1 (hero): Feature the most visually impressive gameplay moment
Screenshot 2: Core mechanic demonstration
Screenshot 3: Progression/reward system
Screenshot 4: Social/multiplayer feature
Screenshot 5: Character/customization (if applicable)

Each screenshot:
  [Device frame OR frameless — frameless performs better in 2024]
  [Key game visual — 70% of area]
  [Short benefit caption — top, 24–28sp, bold, 3–5 words max]
  [Sub-caption — small, optional]
```

**Caption writing rules:**
- Lead with benefit, not feature: "Build epic kingdoms" not "Kingdom building system"
- 3–5 words maximum per headline (proven by A/B testing)
- Use numbers when possible: "100+ levels" > "many levels"

### 15.3 Feature Graphic (Google Play banner)

- 1024×500px horizontal format
- Show key character + game world in one establishing shot
- Text: game title + 1 tagline maximum
- No UI screenshots in feature graphic (only in screenshot slot)
- Must work in both light and dark display contexts on Play Store

---

*Additional sources (sections 11–15):*
- [Zvky Design Studio — Top 7 Art Styles 2025](https://www.zvky.com/blogs/articles/top-7-art-styles-dominating-mobile-games-in-2025)
- [Apple Design Awards 2024](https://developer.apple.com/design/awards/2024/)
- [Apple Design Awards 2023](https://developer.apple.com/design/awards/2023/)
- [Google Play Best of 2024](https://blog.google/products/google-play/google-play-best-apps-games-2024/)
- [BAFTA Games Awards 2024](https://www.bafta.org/games/awards/2024-nominations-winners)
- [AFK Journey art style interview — GamesBeat](https://venturebeat.com/games/how-afk-journey-aims-to-make-anime-into-a-global-art-style/)
- [Honkai: Star Rail UI analysis — Medium](https://medium.com/@acarenatnic/how-honkai-star-rail-fixes-genshin-impacts-ui-problem-6b386d6154f1)
- [Sayonara Wild Hearts — Apple Developer Behind the Design](https://developer.apple.com/news/?id=33kvkagk)
- [Monument Valley design analysis — Nate Bauer](https://nabauer.com/monument-valley-design-analysis/)
- [Florence design — Milanote](https://milanote.com/the-work/lead-designer-of-monument-valley-deconstructs-his-latest-game-florence)
- [Chibi art style — Alibaba Product Insights](https://www.alibaba.com/product-insights/why-is-chibi-art-style-trending-in-mobile-game-designs-now.html)
- [Alto's Odyssey design — Dice.com / IGF road](https://www.dice.com/career-advice/altos-odyssey-winning-mobile-game)
- [Loot box psychology — Behavior Design Medium](https://medium.com/behavior-design/hooked-on-loot-boxes-how-design-gets-us-addicted-79c45faebc05)
- [Hyper-casual UI guide — Supercent Blog](https://medium.com/supercent-blog/designing-ui-of-hyper-casual-games-for-effective-user-experience-dd7c858bec82)
- [App icon trends 2025 — ASOMobile](https://asomobile.net/en/blog/app-icon-trends-and-best-practices-2025/)
- [App Store screenshots guide — Udonis](https://www.blog.udonis.co/mobile-marketing/mobile-games/app-store-screenshots)
- [Color psychology in game UI — Kreafolk](https://kreafolk.com/blogs/news/psychology-of-color-ui-ux-game-design-color-schemes-affect-player-mood)
- [Game UI Database](https://gameuidatabase.com/)
- [Daily login rewards — Beamable](https://beamable.com/blog/inspiring-examples-of-daily-login-rewards-for-your-mobile-game)
- [Y2K game UI — Andrew Lewis / Medium](https://medium.com/design-bootcamp/crafting-a-futuristic-y2k-game-ui-based-on-ridge-racer-and-kylie-minogue-41abd463767b)
- [Glassmorphism Flutter — Vibe Studio](https://vibe-studio.ai/insights/implementing-glassmorphism-effects-in-flutter-uis)

---

## 16. Game-Specific UI Components — Deep Reference

*Added 2026-04. Research from: gameuidatabase.com, wappier.com, maf.ad, adriancrook.com, udonis.co, supersonic.com, tubikstudio.com, deconstructoroffun.com, pub.dev, setproduct.com, ui-patterns.com, tvtropes.org, dev.to, behance.net, dribbble.com*

---

### 16.1 Health / Energy / XP Bars

**Component name:** Segmented Status Bar

**Description:**
A horizontal (or occasionally vertical) progress indicator representing a player resource — HP, energy/stamina, mana, XP, or charge. The bar is the single most ubiquitous game HUD element.

**Visual characteristics:**
- **Pill shape** with `borderRadius >= height/2` (completely rounded ends)
- **Track** (background): dark, 30–50% opacity, same shape as fill
- **Fill**: colored gradient or solid, brighter on top
- **Height**: 8–14px for HUD bars; 20–28px for full-screen progress bars
- **Border**: 1px white or game-color border on the track for separation
- **Glow**: fill has `boxShadow` with the fill color at 50–70% opacity, blurRadius 8–16

**Color coding (universal game language):**
- HP full (>50%): `#4CAF50` green → `#8BC34A` yellow-green
- HP warning (25–50%): `#FF9800` orange
- HP critical (<25%): `#F44336` red — add pulse animation
- Energy/Stamina: `#2196F3` blue or `#00BCD4` cyan
- Mana: `#9C27B0` purple
- XP: `#FFD700` gold or `#CE82FF` purple (Duolingo league style)
- Rage/Charge: `#FF5722` deep orange → `#FFEB3B` yellow gradient

**Animation / Interaction notes:**
- Fill change: `AnimatedFractionallySizedBox`, 400ms, `Curves.easeOut`
- HP drain on hit: red flash overlay (80ms) + shake widget (200ms)
- HP regen: slow fill, 1000ms, linear curve, no shake
- Critical HP: pulsing red border + shake on bar every 2s loop
- XP overflow: green wave fill → mini confetti burst at bar end

**Segment bar pattern (Clash of Clans / RPG boss bars):**
```dart
// Divide HP into N visual segments:
Row(
  children: List.generate(3, (i) {
    final segFill = (hpPercent * 3 - i).clamp(0.0, 1.0);
    return Expanded(
      child: Container(
        margin: EdgeInsets.only(right: i < 2 ? 2 : 0),
        child: AnimatedFractionallySizedBox(
          widthFactor: segFill,
          duration: const Duration(milliseconds: 400),
          curve: Curves.easeOut,
          child: Container(
            height: 12,
            decoration: BoxDecoration(
              color: _barColor,
              borderRadius: BorderRadius.circular(6),
              boxShadow: [BoxShadow(color: _barColor.withOpacity(0.6), blurRadius: 8)],
            ),
          ),
        ),
      ),
    );
  }),
)
```

**Flutter packages:**
- `flutter_animation_progress_bar` — reactive animated bar (pub.dev)
- `percent_indicator` — circular + linear options with gradient support
- `liquid_progress_indicator` — water-like fill effect (for stamina/energy bars)

**Games that use it best:**
- Clash Royale: elixir bar at bottom (blue fill, smooth live update)
- Pokémon GO: HP bar with segment breaks at 50% and 25%
- Diablo Immortal: HP (red) + Shield (yellow) layered bar
- Duolingo: XP bar (purple) always visible at top, celebratory overflow

---

### 16.2 Currency Displays

**Component name:** Currency Pill / Resource Counter

**Description:**
Compact widget showing the player's current balance of one currency type. Always present in the top bar of the lobby/menu screen.

**Visual characteristics:**
- **Pill container**: `BorderRadius.circular(20)`, semi-transparent dark background `rgba(0,0,0,0.5)`
- **Currency icon**: 20–28px icon on the left
- **Amount text**: 16–18sp bold, white or gold
- **Width**: fits content (min 72px)
- **Multiple currencies**: separate pills in a Row, 8px gap

**Standard currency icon colors:**
- Gold / Coins: `#FFD700` → `#FF8C00` gradient (circle with shine highlight)
- Gems / Diamonds: `#00BCD4` cyan or `#2196F3` blue (faceted polygon)
- Premium currency: `#9C27B0` purple gem
- Hearts / Lives: `#F44336` red heart
- Season tokens: `#7C4DFF` deep purple
- Energy lightning: `#FFEB3B` yellow bolt

**Animation / Interaction:**
- Tap on pill: routes to shop screen (300ms slide-up)
- Currency gain: number counts up with `AnimatedFlipCounter` (200ms per digit)
- Currency spend: number counts down + brief red flash on pill (100ms)
- Insufficient funds: pill shakes horizontally (200ms, `Curves.elasticIn`)
- New currency type appears: pill bounces in from off-screen (slideY + scale, 400ms)

**Flutter implementation hint:**
```dart
class CurrencyPill extends StatelessWidget {
  final int amount;
  final Widget icon; // 20x20
  final Color bgColor;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
      decoration: BoxDecoration(
        color: bgColor.withOpacity(0.85),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.white.withOpacity(0.15)),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          icon,
          4.horizontalSpace,
          AnimatedFlipCounter(
            value: amount,
            textStyle: const TextStyle(
              fontSize: 16, fontWeight: FontWeight.bold, color: Colors.white,
              fontFeatures: [FontFeature.tabularFigures()],
            ),
          ),
        ],
      ),
    );
  }
}
```

**Package:** `animated_flip_counter` on pub.dev.

**Games that use it best:**
- Clash Royale: gold + gem top-right, always visible
- Brawl Stars: gems (blue) + coins (gold) + power points (green) — 3 pills
- Candy Crush: lives (red hearts) + gold bars

---

### 16.3 Player Avatar & Profile Card

**Component name:** Avatar Badge Stack / Profile Card

**Avatar size hierarchy:**
- Mini (list/HUD): 32–40px diameter
- Standard (leaderboard row): 44–52px
- Featured (#1 rank): 64–72px
- Profile page: 88–100px

**Visual anatomy:**
- **Shape**: circle (most games) or hexagon (strategy/esports)
- **Frame/border**: 2–3px colored border matching rank tier
- **Level badge**: bottom-right chip, 20–24px, dark bg with white number
- **Online dot**: 8–10px circle top-right, green=online, gray=offline
- **Shadow**: `BoxShadow`, spread 0, blur 12, `Colors.black38`

**Rank tier border colors:**
```dart
// Standard rank progression:
Bronze:   #CD7F32
Silver:   #C0C0C0
Gold:     #D4AF37
Platinum: #00BCD4
Diamond:  #2196F3
Master:   #9C27B0
Champion: #FF6D00 + animated glow
Legend:   animated SweepGradient (gold→purple→red)
```

**Rotating gradient border (Legend rank):**
```dart
AnimatedBuilder(
  animation: _rotationController, // 0→2π, 3s infinite loop
  builder: (context, child) {
    return Container(
      decoration: BoxDecoration(
        shape: BoxShape.circle,
        gradient: SweepGradient(
          colors: [Color(0xFFFFD700), Color(0xFF9C27B0), Color(0xFFFF3B30), Color(0xFFFFD700)],
          transform: GradientRotation(_rotationController.value * 2 * pi),
        ),
      ),
      padding: const EdgeInsets.all(2.5),
      child: CircleAvatar(radius: 44, backgroundImage: ...),
    );
  },
)
```

**Profile Card full layout:**
```
[BACKGROUND — themed gradient for rank tier]
  [AVATAR — 88px, centered, rank border]
  [PLAYER NAME — 18sp bold, white]
  [RANK NAME + ICON — 13sp accent color]
  [STATS ROW — 3 cols: Wins | Streak | Rating]
  [XP PROGRESS BAR]
  [ACTION BUTTONS — Challenge | View Deck | Add Friend]
```

**Games that use it best:**
- Clash of Clans: colored frame per league, trophy count badge
- League of Legends: rank border with ornate tier decorations
- Brawl Stars: Star Player badge + trophy count overlay

---

### 16.4 Inventory / Item Grid

**Visual characteristics:**
- **Cell size**: 72–88px, 3–4 columns on portrait phone
- **Cell shape**: rounded rectangle, `borderRadius: 12–16px`
- **Cell background**: dark semi-transparent (`#1B2A41`-style), or rarity-tinted
- **Rarity border**: 1.5–2px border in rarity color (see §17 Rarity Colors)
- **Quantity badge**: bottom-right corner chip, 12sp, dark bg
- **Lock overlay**: 40% dark overlay + lock icon
- **NEW ribbon**: top-left corner, accent color, "NEW" 10sp text

**Interaction:**
- Tap: expand to item detail modal (scale-in from cell position, 300ms)
- New item: cell enters with `scale(0→1.2→1.0)` spring + golden glow pulse

**Flutter grid implementation:**
```dart
GridView.builder(
  gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
    crossAxisCount: 4,
    crossAxisSpacing: 10,
    mainAxisSpacing: 10,
    childAspectRatio: 0.9,
  ),
  itemBuilder: (ctx, i) => CustomBounceEffect(
    onTap: () => _openItemDetail(items[i]),
    child: ItemCell(item: items[i]),
  ),
)
```

**Games that use it best:**
- Clash Royale: 4 columns, rarity border prominent
- Genshin Impact: character inventory, 4 cols, star rating 1–5
- Diablo Immortal: equipment grid with gem slots overlay

---

### 16.5 Card Deck UI

**Pattern A — Fan/Arc (Hearthstone style):**
- Cards arranged in a slight arc using `Transform.rotate` per card
- Hold = expand card upward for preview
- Card count: 1–10 in hand, spacing collapses automatically

**Pattern B — Horizontal Row (Clash Royale style):**
- 4 cards in "hand" at bottom of battle screen
- Next card visible as ghost behind last slot
- Cards slide left on play, new card slides in from right
- Elixir cost shown as number overlay on card corner

**Card anatomy:**
```
[CARD FRAME — art + border, borderRadius 12]
  [MANA COST — top-left: 28px blue crystal, white number]
  [CARD ART — middle 60%, illustrated]
  [NAME BANNER — center-bottom, gradient texture]
  [CARD NAME — 14sp bold, white/gold]
  [STATS — bottom: Attack (left shield) | Defense (right)]
  [RARITY GEM — bottom-center: gray/blue/purple/gold]
```

**Fan layout with draggable:**
```dart
// Card fan using Transform:
Transform(
  transform: Matrix4.identity()
    ..rotateZ(cardAngle)   // -0.15 to +0.15 radians
    ..translate(0.0, cardLift), // lift hovered card
  alignment: Alignment.bottomCenter,
  child: CardWidget(card: card),
)

// Draggable with snap-back:
Draggable<GameCard>(
  data: card,
  feedback: Transform.scale(scale: 1.1, child: CardWidget(card: card)),
  childWhenDragging: Opacity(opacity: 0.4, child: CardWidget(card: card)),
  child: CardWidget(card: card),
)
```

**Games that use it best:**
- Clash Royale: 4-card hand, live elixir cost check
- Hearthstone: arc hand, 10 cards max, smart tooltip on hover
- Marvel Snap: 7-card hand, location-based targets
- Slay the Spire (mobile): draft-style card reveal

---

### 16.6 Skill Tree / Talent UI

**Node states (4 visual variants):**
- Locked: gray/dark, lock icon, no glow
- Available: highlighted border, pulsing glow
- Unlocked: full color + inner glow + skill icon
- Maxed: gold border + bright fill

**Layout types:**
- Linear: single chain (simple mobile)
- Branching: tree splits into specialization paths
- Circular: central node radiates outward (Diablo 3 passive)
- Hybrid: main trunk with branches (PoE lite)

**Screen layout:**
```
[SCROLLABLE CANVAS — pinch-to-zoom supported]
  [SKILL NODES — absolutely positioned on canvas]
  [CONNECTION LINES — CustomPainter]
[HEADER: "3 Skill Points Available"]
[SELECTED NODE PANEL — slides up from bottom]
  [Name | Level N/N | Description | Cost | Unlock button]
```

**CustomPainter for connection lines:**
```dart
class SkillTreePainter extends CustomPainter {
  final List<SkillConnection> connections;
  @override
  void paint(Canvas canvas, Size size) {
    for (final c in connections) {
      final paint = Paint()
        ..color = c.isUnlocked ? c.color : Colors.grey.shade700
        ..strokeWidth = 2.0
        ..style = PaintingStyle.stroke;
      canvas.drawLine(c.from, c.to, paint);
    }
  }
  @override
  bool shouldRepaint(covariant CustomPainter old) => true;
}
```

**Unlock animation:**
- Node: scale 0.8→1.15→1.0 spring, color transitions gray→accent, glow fades in
- Connection line: draws from parent to child via `strokeDashOffset` animation (500ms)
- Points counter: `AnimatedFlipCounter`, 300ms

---

### 16.7 World Map / Level Select Screen

**Pattern A — Winding Path (Casual/Puzzle, e.g., Candy Crush):**
- Background: illustrated per world/chapter
- Circular nodes on a curved path from bottom to top
- Completed: star fill (1–3 stars), solid fill
- Current: animated pulse + "PLAY" banner
- Locked: gray padlock
- Scrolls vertically as player progresses

**Pattern B — Region Map (Strategy, e.g., Clash of Clans):**
- Top-down illustrated map or stylized world view
- Regions unlock sequentially; conquered = player's flag overlay
- Pan/zoom gesture support

**Winding path implementation:**
```dart
class LevelSelectPath extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      reverse: true, // start from bottom (current level)
      child: SizedBox(
        height: calculatedHeight,
        child: Stack(
          children: [
            Positioned.fill(child: Image.asset('assets/images/world/bg.png', fit: BoxFit.cover)),
            CustomPaint(painter: PathPainter(nodes: levelNodes)),
            ...levelNodes.map((node) => Positioned(
              left: node.x, top: node.y,
              child: LevelNode(level: node, onTap: () => _startLevel(node)),
            )),
          ],
        ),
      ),
    );
  }
}
```

**Games that use it best:**
- Candy Crush: winding path, world themes, metagame goals
- Duolingo: path with character guide, section breaks
- Angry Birds: star-per-level, chapter unlocks

---

### 16.8 Quest / Mission UI

**Types:** Daily (resets 00:00), Weekly (resets Monday), Achievement (permanent), Story (single-completion), Event (time-limited).

**Quest Card anatomy:**
```
[ICON — category symbol (sword/cup/star/social)]
[QUEST NAME — 15sp bold]
[DESCRIPTION — 12sp muted, 2 lines max]
[PROGRESS BAR — partial fill for progressive quests]
[PROGRESS TEXT — "2/5 wins" or "450/1000 XP"]
[REWARD PREVIEW — small icons: coin+200, gem+5]
[CLAIM BUTTON — green, replaces progress when complete]
```

**Visual states:**
- In progress: normal card, progress bar filling
- Complete (unclaimed): golden glow on card, "CLAIM" pulsing
- Claimed: check overlay, reduced opacity, reward animation plays

**Reward fly-to animation (coin to bank):**
```dart
// Pattern: use GlobalKey to get positions of reward item and currency pill
// Launch OverlayEntry with AnimatedBuilder to arc from source to target
// This is the "coin flies to top-right" effect used in all F2P games

void _animateRewardFlyTo(GlobalKey sourceKey, GlobalKey targetKey) {
  final sourceBox = sourceKey.currentContext!.findRenderObject() as RenderBox;
  final targetBox = targetKey.currentContext!.findRenderObject() as RenderBox;
  final sourcePos = sourceBox.localToGlobal(Offset.zero);
  final targetPos = targetBox.localToGlobal(Offset.zero);
  // Insert OverlayEntry, animate position from sourcePos to targetPos
  // Use cubic bezier arc: control point above midpoint
}
```

**Games that use it best:**
- Clash of Clans: magic items daily tasks
- Brawl Stars: daily/weekly quest tabs, reward meter
- Fortnite: seasonal challenges with chapter-by-chapter unlock

---

### 16.9 Notification Badges / Bubble Indicators

**Badge types:**
- **Pure dot** (no number): 8–10px, `#F44336` red, `BoxShape.circle` — "something new"
- **Number badge**: pill shape when count >= 10; max display "99+"
- **"NEW" text badge**: promotional, often blue `#007AFF`

**Position:** Top-right corner of parent icon, slightly overlapping.

**Border:** 1.5–2px white border for visual separation from icon background.

**Flutter implementation:**
```dart
class BadgeWidget extends StatelessWidget {
  final Widget child;
  final int count; // 0 = hidden, -1 = dot only
  final bool showBadge;

  @override
  Widget build(BuildContext context) {
    if (!showBadge || count == 0) return child;
    return Stack(
      clipBehavior: Clip.none,
      children: [
        child,
        Positioned(
          top: -6, right: -6,
          child: Container(
            padding: count == -1 ? null : const EdgeInsets.symmetric(horizontal: 5, vertical: 1),
            height: count == -1 ? 10 : null,
            width: count == -1 ? 10 : null,
            decoration: BoxDecoration(
              color: const Color(0xFFF44336),
              shape: count == -1 ? BoxShape.circle : BoxShape.rectangle,
              borderRadius: count == -1 ? null : BorderRadius.circular(8),
              border: Border.all(color: Colors.white, width: 1.5),
            ),
            child: count == -1 ? null : Text(
              count > 99 ? '99+' : '$count',
              style: const TextStyle(color: Colors.white, fontSize: 10, fontWeight: FontWeight.bold),
            ),
          ).animate().scale(
            begin: const Offset(0, 0),
            curve: Curves.elasticOut,
            duration: 300.ms,
          ),
        ),
      ],
    );
  }
}
```

---

### 16.10 Timer Countdown UI

**Types:**
- In-game turn timer: circular ring, urgent colors
- Chest unlock: `HH:MM:SS` below slot, always visible
- Limited offer: `DD:HH:MM:SS` on shop card with red highlight
- Daily reset: hours until refresh in quest header

**Color transitions as urgency increases:**
- >50% remaining: `#4CAF50` green
- 25–50%: `#FF9800` orange
- <25%: `#F44336` red + pulse loop

**Flutter circular countdown:**
```dart
class CircularCountdownTimer extends StatelessWidget {
  final int secondsRemaining;
  final int totalSeconds;

  double get progress => secondsRemaining / totalSeconds;

  Color get _color {
    if (progress > 0.5) return const Color(0xFF4CAF50);
    if (progress > 0.25) return const Color(0xFFFF9800);
    return const Color(0xFFF44336);
  }

  @override
  Widget build(BuildContext context) {
    return Stack(
      alignment: Alignment.center,
      children: [
        SizedBox(
          width: 56, height: 56,
          child: CircularProgressIndicator(
            value: progress,
            strokeWidth: 6,
            backgroundColor: const Color(0xFF2D2D3A),
            valueColor: AlwaysStoppedAnimation(_color),
          ),
        ),
        Text('$secondsRemaining',
          style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: _color)),
      ],
    );
  }
}
```

**Package:** `circular_countdown_timer` on pub.dev.

---

## 17. Game Monetization UI (Shop / IAP) — Deep Reference

*Sources: wappier.com, maf.ad/blog, javier-barnes-gd.medium.com, yougalchettri.medium.com, deconstructoroffun.com, stripe.com, adapty.io, spaceberry.studio*

---

### 17.1 Shop Screen Architecture

**Standard 6-pack model (industry default):**
- Always offer 6 currency tiers (6 = manageable choice set, per research)
- Price anchoring: show most expensive tier ($99.99) to make mid-tier feel reasonable
- Entry tier: $1.99–$4.99 — first-purchase sweet spot (77% of spenders convert in first 2 weeks)
- Mid tier: $9.99–$19.99 — highest revenue per tier for average payers
- Whale tier: $79.99–$99.99 — ~90% of total IAP revenue comes from top spenders

**Screen layout:**
```
[HEADER: "Shop" + close X + currency balance pills]
[FEATURED DEAL — full-width hero card, animated shine]
  [Limited time: countdown + "SALE!" badge]
  [Price anchored: ~~$19.99~~ NOW $9.99]
[CATEGORY TABS: Currency | Bundles | Cosmetics | Battle Pass]
[PRODUCT GRID — 2 columns]:
  [Card A — smallest]  [Card B]
  [Card C — BEST VALUE] [Card D — MOST POPULAR]
  [Card E]  [Card F — largest]
[RESTORE PURCHASES — small legal link at bottom]
```

**Product card anatomy:**
```
[RARITY-TINTED or gradient BACKGROUND]
  [AMOUNT — large: "500 💰" or "80 💎"]
  [BONUS badge — "+50% BONUS" top-right, accent color]
  [PRODUCT IMAGE — illustrated icon, 60px]
  [PRICE — 20sp bold, white or gold]
  [ORIGINAL PRICE — struck through if on sale]
[BADGE OVERLAY — "BEST VALUE" / "MOST POPULAR" / "LIMITED"]
[CTA — "BUY" button, full card width]
```

**Angled sale badge:**
```dart
Positioned(
  top: 8, right: -4,
  child: Transform.rotate(
    angle: 0.3,
    child: Container(
      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
      color: const Color(0xFFFF3B30),
      child: const Text('SALE',
        style: TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.bold)),
    ),
  ),
)
```

---

### 17.2 Bundle Offer Cards

**Visual hierarchy:**
```
[BACKGROUND ART — character/item, 40% opacity]
[BUNDLE NAME — 18sp bold, white, top-left]
[CONTENTS ROW — 5–8 item icons with quantities]
[ORIGINAL VALUE — struck-through, gray, 14sp]
[SALE PRICE — 24sp bold, gold or green]
[TIMER — "Expires in 2h 14m" countdown, red]
[CTA BUTTON — "GET BUNDLE", full width]
```

**Psychological design tactics used in bundles:**
1. **Anchoring**: original price crossed out, % discount prominent
2. **Decoy**: show inferior bundle first to make target bundle look better
3. **Social proof**: "12,847 players bought this" counter
4. **Loss aversion**: countdown timer + "Limited stock" text
5. **Surprise value**: "You also get: [rare item]" tease
6. **First purchase hook**: first-ever purchase gets 5x bonus — shown only to new payers

---

### 17.3 Badge Design System (Shop)

| Badge | Color | Placement | Psychology |
|-------|-------|-----------|------------|
| BEST VALUE | `#34C759` green or `#D4AF37` gold | Top-center ribbon | Objective value |
| MOST POPULAR | `#007AFF` blue | Top-center ribbon | Social validation |
| LIMITED TIME | `#FF3B30` red | Angled corner | Urgency / scarcity |
| SALE | `#FF9500` orange | Angled corner | Discount framing |
| NEW | `#007AFF` blue | Top-left chip | Discovery |
| STARTER PACK | `#34C759` green | Special badge | Onboarding conversion |

**Badge animation:** Scale `0→1.1→1.0` spring on screen open (300ms). "LIMITED TIME" badge has 2s opacity pulse loop.

---

### 17.4 Battle Pass UI

**Layout architecture:**
```
[HEADER: Season name + days remaining countdown]
[LEVEL PROGRESS BAR: current level (34/100) + XP needed]

FREE TRACK — upper row of tier cards
PREMIUM TRACK — lower row (★ = premium-exclusive)

TIER CARD:
  [TIER NUMBER — small, top]
  [REWARD ICON — 48px centered]
  [REWARD NAME — 11sp muted]
  [CLAIMED overlay — check when past]
  [LOCKED overlay — if not reached]

[UNLOCK PREMIUM — "$9.99" CTA]
```

**Reward tempo design (engagement curve):**
- Tier 1: attractive reward (hook immediately)
- Every tier: small reward (momentum)
- Tiers 10, 25, 50, 75: big spike reward
- Tier 100: exclusive legendary (motivates full completion)

**Flutter horizontal tier track:**
```dart
ListView.builder(
  scrollDirection: Axis.horizontal,
  itemCount: 100,
  itemBuilder: (ctx, tier) {
    final isClaimed = currentLevel > tier;
    final isPremiumOnly = battlePass.premiumOnlyTiers.contains(tier);
    return BattlePassTierCard(
      tier: tier + 1,
      reward: battlePass.rewards[tier],
      isClaimed: isClaimed,
      isCurrent: currentLevel == tier,
      isPremiumOnly: isPremiumOnly,
      hasPremiumAccess: hasPremiumAccess,
    ).animate(delay: (tier * 30).ms).fadeIn(duration: 200.ms);
  },
)
```

**Pricing models:**
- Base pass: $5–$15 range
- Kickstarted (pre-leveled): higher entry price, immediate progress
- Multiple variants: event pass, mode-specific pass
- Subscription wrapping: automatic renewal reduces friction
- Shorter seasons (1 month): maximizes FOMO at season start

**Games that define the format:**
- Fortnite: 100 tiers, horizontal scroll, defined the modern format
- Clash Royale: Pass Royale, combined free+premium track
- PUBG Mobile: outfit-exclusive seasonal rewards
- TFT: thematic deep-space experience with Dark Star frames

---

### 17.5 Subscription / VIP Pass UI (Soft Paywall)

**Screen layout:**
```
[HERO SECTION: premium art + "Go Premium" headline]
[BENEFITS LIST — icon + text, max 7 bullets]:
  ✓ No ads
  ✓ Daily 100 gold bonus
  ✓ 5 exclusive skins
  ✓ 2x XP boost
  ✓ Exclusive profile frame
[PRICING]:
  [Annual: $2.99/mo — "BEST VALUE" green badge]
  [Monthly: $4.99/mo]
[PRIMARY CTA: "Start 7-Day Free Trial"]
[TERMS — 10sp gray, legal requirement]
[CLOSE X — always visible, never hidden]
```

**Key design rules:**
- Single primary color for CTA (brand accent)
- Annual plan shown first, monthly second (anchoring)
- "Start Trial" not "Subscribe" — reduces perceived commitment
- Max 7 bullets — clarity drops beyond this
- Preview before commitment (soft paywall, not hard gate)

**Flutter soft paywall:**
```dart
showModalBottomSheet(
  isScrollControlled: true,
  backgroundColor: Colors.transparent,
  context: context,
  builder: (_) => DraggableScrollableSheet(
    initialChildSize: 0.92,
    minChildSize: 0.5,
    builder: (_, controller) => SubscriptionPaywallSheet(scrollController: controller),
  ),
)
```

---

### 17.6 Chest / Loot Box Opening UI

**Standard opening sequence (Clash Royale model):**
```
1. Chest selection: tap to start opening
2. Chest scales to center (1.0→1.3), light beam appears
3. [TAP/HOLD TO OPEN] prompt
4. Chest shakes: 3 sideways shakes (150ms each)
5. Lid opens: rotateX hinge animation + lid separate
6. Light beam shoots upward (radial gradient expanding)
7. Items fly out one by one (rotateY 180°→0° per card)
8. Rarity glow pulses on each reveal
9. "RARE!" / "EPIC!" text banner if high rarity
10. Cards array at bottom — tap to inspect
11. "Collect All" CTA
```

**Chest rarity visual design:**
- Silver chest: `#C0C0C0` metallic, simple lock
- Gold chest: `#D4AF37` ornate, gems on lid
- Magic chest: `#7C4DFF` purple glow, sparkling
- Super magic: `#FF6D00` orange + gold, animated glow

**Flutter chest open animation:**
```dart
chestWidget
  .animate()
  .shake(hz: 3, offset: const Offset(8, 0), duration: 450.ms)
  .then(delay: 100.ms)
  .scaleY(end: 0.85, duration: 150.ms) // lid squash
  .then()
  .custom(
    duration: 400.ms,
    builder: (ctx, value, child) => Transform(
      transform: Matrix4.identity()..rotateX(-value * pi),
      alignment: Alignment.bottomCenter,
      child: chestLidWidget,
    ),
  )
```

---

### 17.7 Price Anchoring & Psychological Pricing

**Six behavioral economics patterns in game shop UI:**

1. **Anchor Effect**: Display the highest-priced item first. A $99.99 pack makes $9.99 feel trivially cheap. Sort grid by price descending OR feature whale pack as hero card.

2. **Decoy Effect**: Add a "bad deal" pack between entry and mid tier to push players toward mid.
   - Entry ($4.99, 400 coins) → Decoy ($7.99, 500 coins) → Mid ($9.99, 900 coins)
   - Players see Mid as clearly better; Decoy makes the comparison obvious.

3. **Charm Pricing**: $4.99 > $5.00 psychologically. Always: $1.99 / $4.99 / $9.99 / $19.99 / $49.99 / $99.99. Never round numbers.

4. **"Save X%" framing**: Show % saved rather than dollar amount. "Save 67%" feels larger than "Save $6.67". Calculate vs. entry pack (compare to worst deal to maximize %).

5. **Loss aversion**: "Limited time badge + countdown" + "Offer expires in 2h 14m" — refreshes fear of missing out.

6. **Visual size anchoring**: Largest pack card takes 60% more vertical space than smallest. Font size of price: 20–24sp (dominant element). Strike-through original price in muted color.

---

## 18. Social & Competitive UI — Deep Reference

*Sources: udonis.co/leaderboards, ui-patterns.com/leaderboard, cand.land/matchmakingspec, deconstructoroffun.com, gameuidatabase.com*

---

### 18.1 Leaderboard Screen

**Multiple leaderboard types (all should be available):**
- Global: all players worldwide
- Friends: connected friends only
- Weekly: resets Monday (Royal Match / Coin Master model)
- Event: tied to time-limited challenge
- Clan: aggregate clan scores

**Screen layout:**
```
[HEADER: trophy icon + "Leaderboard" + season timer]
[TAB: Global | Friends | Weekly | Event]

[PODIUM — top 3 always visible]:
  [#2 SILVER — left, slightly smaller, silver border]
  [#1 GOLD — center, elevated, crown icon, golden glow]
  [#3 BRONZE — right, slightly smaller, bronze border]
  [Confetti or gold rays behind #1]

[SCROLLABLE LIST — ranks 4+]:
  [RANK#] [AVATAR 40px] [PLAYER NAME 15sp] [SCORE gold] [DELTA ▲/▼]

[MY RANK CARD — sticky bottom]:
  [Same row format + accent border + "↑ 1,234 pts to next rank"]
```

**Delta indicators:**
- `▲+2` = green `#34C759` improving
- `▼-1` = red `#FF3B30` dropping
- `—` = gray `#9E9E9E` no change

**Rank card colors:**
- #1: `#D4AF37` gold border, 20% larger card, crown SVG
- #2: `#C0C0C0` silver border
- #3: `#CD7F32` bronze border
- Own rank row: brand accent background 15% opacity + accent border

**Animated reorder:**
```dart
AnimatedList(
  key: _listKey,
  initialItemCount: leaderboard.length,
  itemBuilder: (ctx, index, animation) => SlideTransition(
    position: animation.drive(Tween(begin: const Offset(-1, 0), end: Offset.zero)),
    child: LeaderboardRow(entry: leaderboard[index], myRank: myRank),
  ),
)
```

**Retention strategies in UI:**
- Milestone reward badges shown at ranks 1, 10, 100 (motivates more players)
- Weekly reset badge: "Season ends in 3 days" urgency
- "Invite Friends" button shown in empty friend leaderboard

**Games that use it best:**
- Coin Master: prominent village-progress leaderboard, milestone rewards
- Royal Match: live refreshing weekly tournament
- Call of Duty Mobile: monthly reset, season-end reward screen
- League of Legends Wild Rift: LP-based ranked ladder, division visualization

---

### 18.2 PvP Matchmaking Screen

**UI structure:**
```
[ANIMATED BACKGROUND — arena art, subtle loop]
["Finding Opponent..." — pulsing 16sp text]
[SEARCH TIMER — "0:23" counting up]

[MY PROFILE — left]:
  [Avatar + level + rank]
  [Name + win rate]

[VS DIVIDER — center]:
  [Animated "VS" — scale pulse]
  [Rotating search ring]

[OPPONENT SLOT — right]:
  [? avatar / rotating silhouette → fills when matched]

[TIPS — bottom rotating 3s interval]
[CANCEL button — secondary styling]
```

**Opponent reveal animation:**
```
1. Spinner stops
2. "FOUND!" text: scale 0.5→1.2→1.0 (300ms, Curves.bounceOut)
3. Opponent silhouette → actual avatar (crossfade 400ms)
4. Opponent name + rating: slideUp 300ms
5. VS divider: rays extend outward
6. 2s hold → battle transition begins
```

**UX rules:**
- Show "Est. wait: <30 seconds" for transparency
- Don't reveal partial opponent data before match confirmed (prevents backing out to reroll)
- Circular progress ring color shifts blue→green as ELO match quality improves
- Anonymous until matched keeps queue fast

**Flutter animated switcher:**
```dart
AnimatedSwitcher(
  duration: const Duration(milliseconds: 600),
  transitionBuilder: (child, anim) => FadeTransition(opacity: anim, child: child),
  child: opponentFound
    ? CircleAvatar(key: const ValueKey('found'), backgroundImage: NetworkImage(opponentAvatarUrl))
    : RotatingSearchAvatar(key: const ValueKey('searching')),
)
```

---

### 18.3 Tournament Bracket UI

**Layout (single elimination):**
```
Round 1    Round 2    Semis    Final    Winner
[Match 1a]
           [Match 2a]
[Match 1b]            [Semi1]
                               [Final]
[Match 1c]            [Semi2]
           [Match 2b]
[Match 1d]
```

**Match card anatomy:**
```
[PLAYER 1]: [Avatar 24px] [Name 12sp] [Score bold]
[DIVIDER]
[PLAYER 2]: [Avatar 24px] [Name 12sp] [Score bold]
```

**Visual cues:**
- Winner row: gold background highlight
- Loser row: 50% opacity dim
- Current active match: pulsing border
- Player's own slot: accent flag/indicator

**InteractiveViewer for zoom/pan:**
```dart
InteractiveViewer(
  boundaryMargin: const EdgeInsets.all(20),
  minScale: 0.5,
  maxScale: 2.0,
  child: SizedBox(
    width: bracketWidth,
    height: bracketHeight,
    child: Stack(
      children: [
        CustomPaint(painter: BracketLinePainter(matches: matches)),
        ...matchPositions.map((pos) => Positioned(
          left: pos.x, top: pos.y,
          child: MatchCard(match: pos.match),
        )),
      ],
    ),
  ),
)
```

---

### 18.4 Clan / Guild UI

**Screen layout (clan overview):**
```
[CLAN BANNER — custom color + emblem + name]
[STATS ROW: Members (42/50) | Trophies | War wins]
[TABS: Members | War | Donations | Chat]

MEMBERS TAB:
  [Filter: All | Elders | Leaders]
  [MEMBER LIST]: Avatar | Name | Role badge | Trophies | Donations

WAR TAB:
  [2-column: Our bases (green) vs Enemy (red)]
  [Stars per attack shown below each base]
  [Attack remaining counter]
```

**Role badges:**
- Leader: gold crown badge
- Elder: silver shield badge
- Member: no badge or simple circle dot

---

### 18.5 Versus / Battle Start Screen

**Sequence:**
```
0ms    — Black screen
500ms  — Background art fades in
500ms  — "VS" crashes from center (scale 2.0→1.0, Curves.bounceOut)
800ms  — Left player card slides from left
900ms  — Right player card slides from right
1200ms — Names/ratings fadeUp
1500ms — Brief hold (player inspects opponent)
2500ms — Battle transition begins
```

**Color language:**
- Left player (you): blue or green tint
- Right player (opponent): red or orange tint
- VS text: white/gold neutral

**Player card anatomy:**
```
[CARD — angled clip or standard rounded rect]
  [Avatar 80px]
  [Player name 18sp bold]
  [Rating 14sp, rank-colored]
  [Win rate / last season rank 12sp muted]
```

---

### 18.6 End-of-Season Reward Screen

**Layout:**
```
[SEASONAL ART BACKGROUND — animated]
[SEASON BADGE — 120px, rank emblem, glow]
[HEADLINE: "Season X Complete!"]
[RANK ACHIEVED: "Gold League III" + rank icon]

[REWARDS REVEAL — one by one, staggered 500ms]:
  Exclusive skin → flies in → lands in grid
  Currency amounts → count up

[STAT SUMMARY]:
  Matches: 247 | Win rate: 58% | Peak rank: #143 | Total XP: 18,450

[NEXT SEASON TEASER]: "Season Y begins in 3 days"
[CTA: "Claim Rewards"]
```

**Season badge animation:**
1. fadeIn + rotate 0→360° (800ms, one revolution only)
2. Settle + glow pulse loop begins (2s)
3. Stats count up from 0 (1200ms each, easeOut)
4. Confetti loop 4s

---

### 18.7 Friend Invite Screen

**Layout:**
```
[HERO ART — 2 characters together]
[HEADLINE: "Play With Friends!"]
[INCENTIVE: "Both get 100 gems when they join"]
[REFERRAL CODE: [YOURCODE] [Copy button]]
[SHARE OPTIONS]: WhatsApp | Telegram | SMS | Copy Link
[CONTACTS LIST — with permission request]
  Each contact: Avatar | Name | [Invite button]
[PENDING INVITES — sent but not joined]
[CLAIMED REWARDS — previous accepted referrals]
```

**Design psychology:**
- Dual incentive (both inviter + invitee get reward) maximizes viral coefficient
- Personalized code (`KATE-10`) feels exclusive vs. generic URL
- Show accepted invites as social proof

**Flutter share:**
```dart
// share_plus package:
await Share.share(
  'Join me in [Game Name]! Use my code $referralCode for 100 gems bonus.\n$referralLink',
  subject: 'Join [Game Name]!',
);
```

---

## 19. Game Onboarding Patterns — Deep Reference

*Sources: adriancrook.com, supersonic.com, appcues.com, inworld.ai, medium.com/@amol346bhalerao, mockplus.com, gameuidatabase.com, GameAnalytics Q1 2024*

---

### 19.1 FTUE (First-Time User Experience) Principles

**Core rules ranked by D1 retention impact:**

1. **Play within 30 seconds** — No login wall. Defer registration. Immediate play.
2. **Teach through doing** — Never a text wall. Force the player to perform the action.
3. **Quick win at minute 1** — Design first challenge to be easy. Victory = dopamine anchor.
4. **Progressive disclosure** — One mechanic per tutorial step. Complexity earned, not dumped.
5. **Skip always available** — Not prominent, but always findable. Respects returning players.
6. **Max 5 forced steps** — After step 5, open the game or lose the player.

**Retention data (GameAnalytics 2024):**
- D1 average: 26–27% retention
- Top performers: 31–33%
- Tutorial completion rate directly drives D7 and D30
- Each tutorial step past step 5: ~15% drop in completion rate

**Non-textual guidance (language-independent):**
- Animated arrows pointing to target element
- Hand/finger icon bouncing toward button
- Highlight glow on interactive element
- Pulsing border on the thing to tap
- Avoid instructional text entirely where possible

---

### 19.2 Spotlight / Coach Mark Tutorial Overlay

**Architecture:**
A full-screen semi-transparent overlay (dark, 70–80% opacity) with a transparent "hole" cut around the target widget. The player can only interact through the hole.

**Package: `tutorial_coach_mark` (pub.dev)**
```dart
TutorialCoachMark(
  targets: [
    TargetFocus(
      identify: "battle_button",
      keyTarget: _battleButtonKey,
      contents: [
        TargetContent(
          align: ContentAlign.top,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text("TAP TO BATTLE!",
                style: TextStyle(color: Colors.white, fontSize: 18, fontWeight: FontWeight.bold)),
              8.verticalSpace,
              Text("Earn trophies and unlock rewards",
                style: TextStyle(color: Colors.white70, fontSize: 13)),
            ],
          ),
        ),
      ],
    ),
  ],
  colorShadow: Colors.black.withOpacity(0.75),
  paddingFocus: 10,
  opacityShadow: 0.8,
  onClickTarget: (target) => _nextStep(),
  onFinish: () => _saveTutorialComplete(),
).show(context: context);
```

**Custom implementation (PathFillType.evenOdd):**
```dart
class SpotlightOverlayPainter extends CustomPainter {
  final Rect highlightRect;
  final Color overlayColor;
  final double borderRadius;

  @override
  void paint(Canvas canvas, Size size) {
    final path = Path()
      ..fillType = PathFillType.evenOdd
      ..addRect(Rect.fromLTWH(0, 0, size.width, size.height))
      ..addRRect(RRect.fromRectAndRadius(highlightRect, Radius.circular(borderRadius)));
    canvas.drawPath(path, Paint()..color = overlayColor);
  }

  @override
  bool shouldRepaint(covariant CustomPainter old) => true;
}
```

**Hand/finger pointer animation:**
```dart
handIcon
  .animate(onPlay: (c) => c.repeat())
  .scale(
    begin: const Offset(1.0, 1.0), end: const Offset(0.85, 0.85),
    duration: 600.ms, curve: Curves.easeInOut,
  )
  .then()
  .scale(begin: const Offset(0.85, 0.85), end: const Offset(1.0, 1.0), duration: 400.ms)
  .slideY(begin: 0, end: 0.1, duration: 600.ms)
```

---

### 19.3 Character / Avatar Selection Screen

**Pattern A — Horizontal Swipe (most common):**
```
[LARGE CHARACTER ART — center, full height]
[SWIPE INDICATORS — dots or side arrows]
[CHARACTER NAME — 22sp bold, bottom]
[ROLE BADGE — "Assassin" / "Support" / "Tank"]
[3 STAT BARS — Speed | Power | Defense (staggered fill)]
[BACKSTORY EXCERPT — 2 lines, collapsible]
[SELECT BUTTON — bottom CTA]
```

**Pattern B — Grid Card (many options):**
```
[GRID 2–3 cols of character cards]
  Selected: accent border + checkmark
  Locked: dim overlay + lock icon
[PREVIEW PANEL — bottom sheet on phone]
  Full art + stats + Select/Unlock CTA
```

**PageView with peek effect:**
```dart
PageView.builder(
  controller: PageController(viewportFraction: 0.85),
  onPageChanged: (i) => setState(() => _selectedIndex = i),
  itemBuilder: (ctx, i) => AnimatedScale(
    scale: i == _selectedIndex ? 1.0 : 0.88,
    duration: const Duration(milliseconds: 300),
    child: CharacterCard(character: characters[i]),
  ),
)
```

**Character reveal animation:**
- New character: `fadeIn + scale(0.95→1.0)`, 300ms
- Stats bars: stagger fill left-to-right, 80ms between each bar
- Name: `slideY(begin: 0.2) + fadeIn`, 200ms

**Psychology:**
- Allow avatar/name selection early: increases ownership = higher D1 retention
- Offer meaningful choice (different roles/playstyles, not just cosmetic)
- Tease locked characters: creates long-term goals
- Let players try 2 characters before committing (reduces decision anxiety)

---

### 19.4 Difficulty Selection UI

**Pattern A — Card buttons:**
```
[EASY 🟢]  [NORMAL ⚪]  [HARD 🔴]  [EXTREME 💀]
```
Each option: rounded card, icon, label, description ("Perfect for new players").
Selected state: accent border + glow.

**Pattern B — Reward-tied slider:**
- Gradient slider: green → yellow → red
- Reward preview updates as difficulty changes
- Higher difficulty = better loot shown
- Notched at named difficulty positions

**Reward incentive display:**
```
Easy:    [Coin icon]    Basic rewards
Normal:  [Coin+]       Standard rewards
Hard:    [Gem icon]    +50% bonus loot
Extreme: [Legendary]   Exclusive reward + title
```

---

### 19.5 Progressive Disclosure Pattern

**Feature unlock by session/level:**
```
Session 1 (Day 1):  Core loop only. No shop, no social, no battle pass.
Session 2–3:        Shop introduced (first purchase prompt). Second mechanic.
Session 4+:         Clan, battle pass, events, full access.
```

**Gating UI implementation:**
- Feature nav icons shown but grayed + lock icon
- Tap shows: "Unlock at Level 5" tooltip
- Progress indicator: current level vs unlock threshold
- When threshold crossed: arrow/spotlight points to newly unlocked feature

**"Wow moment" strategy:**
- Define the game's core delight moment (first PvP win, first legendary pull, first clan join)
- Design tutorial to reach this moment within session 1
- Celebrate maximally: confetti, special animation, push notification opt-in prompt shown here

---

## 20. Rarity Color System Reference

*Standard across: Fortnite, Apex Legends, Destiny, Clash Royale, Diablo, most mobile games. Codified by Diablo (1997), standardized by World of Warcraft (2004).*

| Tier | Name | Color | Hex | Glow Blur |
|------|------|-------|-----|-----------|
| 1 | Common | Gray | `#9E9E9E` | 0 |
| 2 | Uncommon | Green | `#4CAF50` | 8 |
| 3 | Rare | Blue | `#2196F3` | 12 |
| 4 | Epic | Purple | `#9C27B0` | 16 |
| 5 | Legendary | Gold | `#FF8F00` | 24 |
| 6 | Mythic | Red-Orange | `#FF5722` | 32 |
| 7 | Exotic | Animated gradient | — | 40 |

**Design origins:**
- Purple = royalty (historical scarcity of Tyrian dye, expensive for centuries)
- Gold = divine, ultimate power — most universal prestige color
- These associations cross cultures more reliably than other color meanings (though not universally)

**Accessibility:** DO NOT rely solely on color — also use shape, size, or text label. ~8% of male players have color vision deficiency.

**Flutter enum:**
```dart
enum ItemRarity {
  common, uncommon, rare, epic, legendary, mythic, exotic;

  Color get color => switch (this) {
    ItemRarity.common    => const Color(0xFF9E9E9E),
    ItemRarity.uncommon  => const Color(0xFF4CAF50),
    ItemRarity.rare      => const Color(0xFF2196F3),
    ItemRarity.epic      => const Color(0xFF9C27B0),
    ItemRarity.legendary => const Color(0xFFFF8F00),
    ItemRarity.mythic    => const Color(0xFFFF5722),
    ItemRarity.exotic    => const Color(0xFFFFD700),
  };

  double get glowBlur => switch (this) {
    ItemRarity.common    => 0,
    ItemRarity.uncommon  => 8,
    ItemRarity.rare      => 12,
    ItemRarity.epic      => 16,
    ItemRarity.legendary => 24,
    ItemRarity.mythic    => 32,
    ItemRarity.exotic    => 40,
  };

  String get displayName => '${name[0].toUpperCase()}${name.substring(1)}';
}
```

---

## 21. Flutter Packages for Game UI (Extended Reference)

| Feature | Package | Notes |
|---------|---------|-------|
| Tutorial spotlight | `tutorial_coach_mark` | Coach marks, hole cutout overlay |
| Progress bar animated | `flutter_animation_progress_bar` | Reactive H+V bars |
| Liquid progress | `liquid_progress_indicator` | Water-fill effect for energy bars |
| Animated flip counter | `animated_flip_counter` | Digit-by-digit currency animation |
| Circular countdown | `circular_countdown_timer` | Ring countdown with callback |
| Confetti burst | `confetti` | Customizable victory particles |
| Particles ambient | `particles_flutter` | Background sparkles |
| Particles advanced | `newton_particles` | Emitter-based, game-grade |
| Glow widget | `aura_box` | Easy glow/aura wrapper |
| Shimmer | `shimmer` | Loading / shine sweep |
| Animated gradient bg | `animate_gradient` | Moving gradient backgrounds |
| Game engine | `flame` | Full game loop + sprites + collision |
| Lottie animations | `lottie` | After Effects .json animations |
| Rive state machines | `rive` | Character animations, state machines |
| Share native | `share_plus` | Native OS share sheet |
| Sound effects | `audioplayers` | Concurrent audio, low latency |
| Haptics | Built-in `HapticFeedback` | `.lightImpact()` / `.mediumImpact()` |
| Animated background | `animated_background` | Triangle particle, randomized grid |
| Glitch effect | `animated_glitch` | Cyberpunk-style glitch |
| Mesh gradient | `mesh_gradient` | Smooth color blob backgrounds |

---

*Additional sources for sections 16–21:*
- [wappier.com — IAP UI Design Tips](https://wappier.com/in-app-purchase-ui-design/)
- [MAF Blog — Top IAP Trends 2024](https://maf.ad/en/blog/iap-trends-mobile-gaming/)
- [Deconstructor of Fun — Battle Pass Analysis](https://www.deconstructoroffun.com/blog/2022/6/4/battle-passes-analysis)
- [Javier Barnes GD — IAP Pack Design](https://javier-barnes-gd.medium.com/iap-packs-in-mobile-f2p-analysis-and-design-a086c4058481)
- [Yougal Chettri — Behavioral Economics IAP](https://yougalchettri.medium.com/in-app-purchases-3cb16a2548af)
- [Udonis Blog — Leaderboard Design](https://www.blog.udonis.co/mobile-marketing/mobile-games/leaderboards)
- [UI Patterns — Leaderboard](https://ui-patterns.com/patterns/leaderboard)
- [David Candland — Matchmaking UI Spec](http://www.cand.land/matchmakingspec)
- [Supersonic — Tutorial UI](https://supersonic.com/learn/blog/how-to-create-a-tutorial-ui-that-keeps-players-in-the-game/)
- [DEV.to — Flutter Spotlight Overlay](https://dev.to/thanasistraitsis/creating-spotlight-tutorials-in-flutter-the-complete-guide-to-selective-overlays-4iil)
- [Amol Bhalerao — Mobile Game Onboarding UX](https://medium.com/@amol346bhalerao/mobile-game-onboarding-top-ux-strategies-that-boost-retention-6ef266f433cb)
- [Adrian Crook — Mobile Game Onboarding Best Practices](https://adriancrook.com/best-practices-for-mobile-game-onboarding/)
- [Claire Fishman — Color Theory in Game Rarity](https://medium.com/@ClaireFish/how-color-theory-codifies-item-quality-in-video-games-104d8118044)
- [TV Tropes — Color Coded Item Tiers](https://tvtropes.org/pmwiki/pmwiki.php/Main/ColorCodedItemTiers)
- [Tubik Studio — Gamification in UX](https://blog.tubikstudio.com/gamification-in-ux-missions-and-challenges/)
- [The Design Mechanic — Character Selection Case Study](https://medium.com/@TheDesignMechanic/game-ui-case-study-character-selection-optimization-c817be8bf905)
- [Spaceberry — Paywall UX Design](https://spaceberry.studio/blog/ux-design-for-paywalls-and-subscription-models/)
- [GameAnalytics — Q1 2024 Benchmarks](https://www.gameanalytics.com/reports/mobile-games-benchmarks-q1-2024)
- [Watanuxdesign — Clash Royale UX](https://watanuxdesign.medium.com/why-clash-royale-has-one-of-the-best-user-experience-design-part-1-fb9c761042c7)
- [pub.dev — flutter_animate](https://pub.dev/packages/flutter_animate)
- [pub.dev — tutorial_coach_mark](https://pub.dev/packages/tutorial_coach_mark)
- [pub.dev — circular_countdown_timer](https://pub.dev/packages/circular_countdown_timer)
- [pub.dev — animated_flip_counter](https://pub.dev/packages/animated_flip_counter)
- [Game UI Database — All categories](https://gameuidatabase.com/)
