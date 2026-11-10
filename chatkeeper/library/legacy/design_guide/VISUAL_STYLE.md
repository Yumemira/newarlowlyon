# Визуальные стили и тренды мобильного дизайна

## 1. Glassmorphism (Стеклоформизм)

**Суть:** Полупрозрачные элементы с backdrop blur, имитирующие матовое стекло.

**Ключевые свойства:**
- Background blur (10-20px)
- Transparency (поверхность 5-15% opacity)
- Subtle border (1px, white 10-20% opacity)
- Мягкие тени (не жёсткие)
- Фон частично виден сквозь элементы

**Применение:**
- Cards и containers
- Bottom navigation bar
- Bottom sheets
- Overlays и modals

**2025-2026 тренд:**
- Apple "Liquid Glass" (iOS 26/WWDC 2025) — glassmorphism как системный стиль
- Samsung One UI 7 — frosted glass + gradients
- Glassmorphism доминирует в UI design 2025

**Когда использовать:** Dark themes, яркие/градиентные фоны, premium-приложения
**Осторожно:** Контраст текста! Читаемость — приоритет над эстетикой.

---

## 2. Neumorphism (Неоморфизм / Soft UI)

**Суть:** Мягкие тени и подсветки создают иллюзию "вдавленности" или "выпуклости" элементов.

**Ключевые свойства:**
- Background = surface (один цвет)
- Два box-shadow: светлый (top-left) + тёмный (bottom-right)
- Минимальный контраст между элементом и фоном
- "Soft" и "tactile" ощущение

**Neumorphism 2.0 (2025):**
- Сильнее контраст для accessibility
- Используется как акцент, не весь UI
- Комбинируется с чёткой типографикой
- Подходит для: кнопки, sliders, toggles, cards

**Осторожно:** Плохая accessibility в чистом виде. Комбинируй с чёткими границами.

---

## 3. Dark Theme

**Суть:** Тёмный фон, светлый текст, акцентные цвета.

**Правила:**
- Фон: **НЕ чёрный (#000)**, а тёмно-серый (#121212 по Google)
- Контраст текст/фон: минимум 4.5:1 (WCAG AA)
- Большой текст: минимум 3:1
- Акценты: desaturated (200-50 range), не яркие насыщенные
- Тени на сером видны лучше чем на чёрном

**Палитра dark theme:**
- Surface: #121212 → #1E1E1E → #2C2C2C (elevation levels)
- Text: white 87% (primary), 60% (secondary), 38% (disabled)
- Accent: lighter tones для читаемости

**Обязательно:** Давать пользователю выбор (auto/light/dark)

---

## 4. Цветовая теория

### Типы палитр
| Тип | Описание | Когда |
|-----|----------|-------|
| Monochromatic | Оттенки одного цвета | Минималистичные приложения |
| Analogous | 3 соседних на круге | Спокойные, гармоничные |
| Complementary | Противоположные | Контрастные, яркие |
| Triadic | 3 равноудалённых | Динамичные, игровые |

### Правило 60-30-10
- **60%** доминантный (фон)
- **30%** вторичный (карточки, секции)
- **10%** акцент (CTA, индикаторы)

### Тренды 2026
- Dark mode + bold accents
- High-contrast accessibility палитры
- Soft gradients и duotones
- Jewel tones (изумрудный, рубиновый)
- Soft-tech pastels

---

## 5. Типография

**Правила:**
- Минимум 16px для body text на мобильных
- Line-height: 1.4-1.6x размера шрифта
- Максимум 2 font families в приложении
- Размеры кратны 4px grid (12, 14, 16, 20, 24, 32)

**Иерархия:**
| Уровень | Размер | Weight | Применение |
|---------|--------|--------|------------|
| H1 | 28-32sp | 700-800 | Заголовок страницы |
| H2 | 20-24sp | 600-700 | Заголовок секции |
| H3 | 16-18sp | 600 | Подзаголовок |
| Body | 14-16sp | 400-500 | Основной текст |
| Caption | 10-12sp | 400 | Подписи, мета |

---

## 6. Spacing System (8pt Grid)

**Базовый unit:** 8px (или 4px для fine-tuning)

**Стандартные значения:**
| Token | Значение | Применение |
|-------|----------|------------|
| xs | 4px | Минимальный gap |
| sm | 8px | Внутренний padding элемента |
| md | 16px | Стандартный padding карточки |
| lg | 24px | Между секциями |
| xl | 32px | Между блоками |
| xxl | 48px | Верх/низ страницы |

**Screen margins:** 16-20px на мобильных
**Touch targets:** минимум 44px (Apple) / 48dp (Android)

---

## 7. Micro-animations

**Правила:**
- 150-300ms для micro-interactions
- 300-500ms для page transitions
- Анимация = коммуникация, не декорация
- +33% user satisfaction (исследования)

**Стандартные:**
| Контекст | Длительность | Тип |
|----------|-------------|-----|
| Button tap | 100-150ms | Scale/Opacity |
| Page entry | 300-400ms | FadeIn + SlideY |
| List item | 60-80ms per item | Staggered FadeIn |
| Modal appear | 250-400ms | FadeIn + Scale |
| Dismiss | 200-300ms | FadeOut + SlideY |

**Flutter-specific:**
- Implicit animations (AnimatedContainer, AnimatedOpacity) для простых
- flutter_animate для декларативных цепочек
- Hero для shared element transitions

---

## 8. Accessibility

**WCAG 2.2 Mobile:**
- Contrast: 4.5:1 normal text, 3:1 large text
- Touch targets: 44x44px minimum + spacing
- Не полагаться только на цвет (добавлять иконки)
- Up-event для действий (не down-event)
- Жесты: всегда альтернативная кнопка
- Font resizing support
- Screen reader labels

Sources:
- [Glassmorphism 2025 - Medium](https://medium.com/design-bootcamp/glassmorphism-the-2015-design-trend-9d1f60d68ba2)
- [Liquid Glass UI iOS 26](https://www.designmonks.co/blog/liquid-glass-ui)
- [Neumorphism Complete Guide 2026](https://www.bighuman.com/blog/neumorphism)
- [Dark Mode Guide 2026](https://appinventiv.com/blog/guide-on-designing-dark-mode-for-mobile-app/)
- [Color Palette 2026 - IxDF](https://ixdf.org/literature/article/ui-color-palette)
- [8pt Grid System](https://www.thedesignership.com/blog/the-ultimate-spacing-guide-for-ui-designers)
- [Flutter Animations Guide](https://medium.com/@flutter-app/animations-micro-interactions-in-flutter-make-your-ui-delightful-592fb9da6e11)
- [WCAG Mobile Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Mobile_accessibility_checklist)
- [Color Trends 2026](https://elements.envato.com/learn/color-scheme-trends-in-mobile-app-design)
- [Typography in Design Systems](https://www.designsystems.com/typography-guides/)
