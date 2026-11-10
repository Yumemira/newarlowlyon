# Стили дизайна мобильных приложений по категориям

Справочник по ключевым подходам к дизайну для разных типов приложений: строгих, игровых, ярких, формальных, минималистичных и специализированных.

---

## 1. Строгий / Формальный (Corporate / Business)

**Когда:** Финтех, банкинг, CRM, B2B-инструменты, юридические, корпоративные приложения.

**Примеры:** Revolut, Robinhood, Freshworks CRM, Bloomberg, SAP.

### Цвета
- Основа: тёмно-синий (#1A237E), серый (#37474F), белый
- Акценты: сдержанный голубой (#1976D2), зелёный (#388E3C) для успеха
- **Никогда:** ярких/кислотных цветов, градиентов-радуг
- Палитра: 2-3 цвета максимум, neutral base

### Типография
- Sans-serif: Inter, SF Pro, Roboto — чистый, профессиональный
- Чёткая иерархия: H1 жирный, body regular, caption light
- Размеры: крупнее стандарта для читаемости данных (16-18sp body)
- Числа: tabular (моноширинные) для таблиц и финансов

### Элементы UI
- Карточки: минимальный border-radius (8-12sp), тонкие borders
- Иконки: линейные (outlined), не filled
- Кнопки: прямоугольные или слабо скруглённые, solid fill
- Таблицы и графики: чёткие, data-dense
- Формы: строгие лейблы, inline validation

### Анимации
- Минимум анимаций — только функциональные
- Fade transitions 200-300ms
- Никаких bounce, pulse, shimmer на CTA
- Graphs: плавное рисование линий

### Навигация
- Bottom tabs или sidebar для desktop
- Чёткая breadcrumb навигация
- Structured settings с группировкой

### Trust-паттерны
- Security badges, encryption indicators
- Last login info, device activity
- Biometric verification для высокорисковых действий
- Padlock icons рядом с sensitive fields

---

## 2. Игровой / Геймифицированный (Playful / Gamified)

**Когда:** Образовательные, фитнес, habit-tracking, детские, развлекательные приложения.

**Примеры:** Duolingo, Habitica, Fitbit, CRED, Starbucks Rewards.

### Цвета
- Яркие, насыщенные: зелёный (#4CAF50), оранжевый (#FF9800), фиолетовый (#9C27B0)
- Gradient backgrounds для энергии
- Цветовое кодирование: уровни, достижения, прогресс
- Допустим полный спектр — но с балансом (не 10 цветов одновременно)

### Типография
- Rounded sans-serif: Nunito, Poppins, Comfortaa
- Крупные, жирные заголовки
- Fun titles можно с custom/display шрифтами
- Emoji допустимы в UI

### Элементы UI
- Большие скруглённые кнопки (border-radius: 16-24sp)
- Badges, stars, streaks, level indicators
- Progress bars с цветовой заливкой
- Avatar/character система
- Spin-the-wheel, scratch cards, confetti
- Leaderboards с ranking

### Анимации
- **Обязательны и обильны!**
- Bounce на кнопках, scale на карточках
- Confetti при достижении цели
- Pulse на streak indicators
- Celebration: particles, color flash, звуковые эффекты
- Animated mascot/character
- Haptic feedback при наградах
- Progress fill animations

### Навигация
- Bottom nav с animated icons
- Стилизованные tab indicators
- Quest/journey-based flow (шаги)
- Reward screens после действий

### Gamification-паттерны
- XP + Levels: ощущение прогресса
- Daily Streaks: retention hook
- Leaderboards: соревнование
- Badges: visual milestones
- Challenges: limited-time events
- In-app currency: gems, coins, stars

---

## 3. Яркий / Смелый (Vibrant / Bold)

**Когда:** Lifestyle, social, creative tools, молодёжные, стартапы.

**Примеры:** Instagram, Spotify (gradients), Canva, Figma.

### Цвета
- Neon accents: electric blue (#00B4FF), hot pink (#FF1493), lime green (#76FF03)
- Bold gradients: мульти-цветные переходы
- Dark background + neon accents — самый популярный тренд 2025-2026
- High contrast, высокая насыщенность

### Типография
- Modern sans-serif: Manrope, Space Grotesk, Plus Jakarta Sans
- Extra bold заголовки (800-900 weight)
- Крупные размеры (24-40sp для hero titles)
- Gradient text — допустим для акцентов

### Элементы UI
- Скруглённые cards (16-24sp radius)
- Glow shadows (accent color с alpha)
- Glassmorphism: blur + transparency
- Animated gradients как backgrounds
- Bold CTAs: gradient fill, large, prominent

### Анимации
- Shimmer и glow эффекты
- Gradient mesh animations
- Parallax на scroll
- Scale + fade для page transitions
- Staggered list с выраженным slide (0.15+)
- Animated gradient backgrounds

### Навигация
- Bottom nav с glow active indicator
- Floating nav elements
- Gesture-heavy navigation

---

## 4. Минималистичный / Элегантный (Minimalist / Clean)

**Когда:** Productivity, notes, premium tools, lifestyle, wellness.

**Примеры:** Notion, Todoist, Things 3, Bear, Bumble, Calm.

### Цвета
- Neutral base: off-white (#FAFAFA), warm grey (#E8E4E0)
- 1-2 accent colors: muted sage (#9CAF88), dusty blue (#7B9CC7), terracotta (#C77B5B)
- Нет ярких/кислотных цветов
- Много white space

### Типография
- Clean sans-serif: SF Pro, Inter, System fonts
- Тонкие weights для body (300-400)
- Чёткая иерархия через size, не через boldness
- Letter-spacing чуть шире для заголовков

### Элементы UI
- Минимум borders (dividers вместо card borders)
- Subtle shadows или вообще без теней
- Большой padding и white space
- Иконки: thin-line, monochrome
- Toggle switches: простые, аккуратные

### Анимации
- Минимум и утончённость
- Fade only, 200-300ms
- Никаких bounce, glow, particles
- Subtle scale на tap (0.98)
- Crossfade между состояниями

### Навигация
- Tab bar: минимальный, текст-only или thin icons
- Sidebar (desktop/tablet)
- Keyboard shortcuts для power users
- Quick-entry: мгновенный ввод без лишних шагов

### Ключевой принцип
> "Лучший интерфейс — тот, которого не замечаешь"

---

## 5. Premium / Luxury (Роскошный)

**Когда:** Fashion, luxury e-commerce, VIP-сервисы, premium subscription.

**Примеры:** Net-a-Porter, Gucci app, luxury hotel booking.

### Цвета
- Dark base: чёрный (#0A0A0A), deep charcoal (#1C1C1C)
- Gold/champagne accents: (#D4AF37), (#C9B38B)
- Muted jewel tones: sapphire (#2B4570), emerald (#1B5E20), burgundy (#800020)
- Монохром + один акцент

### Типография
- **Serif для заголовков:** Didot, Playfair Display, Cormorant Garamond
- Sans-serif для body: light weights (300-400)
- Generous letter-spacing (0.05-0.1em для headers)
- Большие размеры, много воздуха между строками (line-height: 1.6-1.8)

### Элементы UI
- Full-bleed фотографии высокого качества
- Минимум UI-элементов: контент = дизайн
- Тонкие линии-разделители (0.5px, 10% opacity)
- Кнопки: outlined (тонкий border) или minimal fill
- Hero images с gradient overlay для текста

### Анимации
- Медленные, плавные, "дорогие"
- Fade 400-600ms
- Parallax на hero images
- Reveal on scroll (элегантное появление)
- Никаких bounce, confetti, быстрых переходов
- Image zoom on tap/hover

### Навигация
- Hamburger menu (скрытый, чистый main screen)
- Full-screen navigation overlay
- Минимальный bottom nav (или отсутствует)
- Gesture-based browsing

---

## 6. Neobrutalism (Необрутализм)

**Когда:** Creative agencies, indie apps, experimental, portfolio, разработчик-tools.

**Примеры:** Gumroad, Figma community, indie games.

### Цвета
- Яркие, плоские: жёлтый (#FFD600), розовый (#FF6B9D), голубой (#4FC3F7)
- Чёрный для контуров и текста
- Белый/светлый фон
- Нет градиентов! Flat, solid fills
- High contrast между элементами

### Типография
- **Огромная, доминирующая**
- Mono или bold sans-serif: Space Mono, JetBrains Mono, Clash Display
- Всё caps для заголовков (иногда)
- Нарочито "сырая" иерархия

### Элементы UI
- **Толстые чёрные borders (2-4px)**
- Hard shadows (offset, не blur): `box-shadow: 4px 4px 0px #000`
- Прямые углы или минимальный radius
- Raw, "незавершённый" вид
- Карточки: thick border + solid shadow
- Кнопки: chunky, oversized, thick stroke

### Анимации
- Минимум или нарочито "дёрганые"
- Instant transitions (без smooth easing)
- Hover: shadow shift (4px → 2px)
- Click: scale down + shadow remove
- Никакого glassmorphism или blur

### Навигация
- Visible, upfront — ничего не скрывать
- Large tap targets
- Простая структура

### Ключевой принцип
> "Намеренная грубость. Каждый элемент заявляет о себе."

---

## Специализированные стили по индустриям

### 7. Фитнес / Здоровье (Fitness / Health)

**Цвета:** Dark bg (#121212) + neon green (#00E676), electric blue (#00B0FF), orange (#FF6D00)
**Типография:** Bold condensed sans-serif (Oswald, Bebas Neue), крупные числа для метрик
**UI:** Progress rings, activity cards, workout timers, streak counters
**Анимации:** Energetic — pulse на активных метриках, animated progress fill, celebration при достижении goal
**Фишка:** High contrast для читаемости в gym/outdoors, dark mode по умолчанию

**Примеры:** Nike Run Club (neon на чёрном), Strava (dark + orange), Fitbit (colorful progress)

---

### 8. Медицина / Здравоохранение (Healthcare)

**Цвета:** Спокойные — light blue (#E3F2FD), soft green (#E8F5E9), white base, grey accents
**Типография:** Readable, accessible — Noto Sans, Open Sans, 16sp+ body, high contrast
**UI:** Чистые формы, крупные touch targets, accessibility-first, security badges
**Анимации:** Минимальные, спокойные — fade only, никаких резких движений
**Фишка:** Trust > Design. Padlock icons, encryption indicators, biometric prompts.

**Примеры:** MyChart, Ada Health, Calm (wellness crossover)

---

### 9. Еда / Доставка (Food / Delivery)

**Цвета:** Тёплые — red (#D32F2F), orange (#FF8F00), warm yellow (#FFC107), cream (#FFF8E1)
**Типография:** Friendly rounded: Poppins, Nunito. Крупные prices, clear menu labels
**UI:** Hero food photos (крупные, аппетитные), menu cards с thumbnail, cart badge, quantity stepper
**Анимации:** Add-to-cart animation (fly to cart icon), smooth scroll menu categories, rating stars
**Фишка:** Фото решают всё — high-res, consistent styling, warm lighting

**Примеры:** UberEats (card-based), DoorDash, Zomato (red accent)

---

### 10. Музыка / Стриминг (Music / Streaming)

**Цвета:** Dark immersive (#121212), dynamic gradients от album art, green accent (#1DB954 Spotify)
**Типография:** Clean sans-serif, light weights. Album titles bold, metadata thin
**UI:** Full-screen player, album art hero, floating mini-player, horizontal scroll playlists
**Анимации:** Crossfade между треками, animated progress bar, visualizer/waveform, smooth page transitions
**Фишка:** Content IS the UI — album art определяет цветовую палитру экрана

**Примеры:** Spotify (dark + green), Apple Music (dynamic colors), Tidal (premium dark)

---

### 11. Путешествия / Бронирование (Travel / Booking)

**Цвета:** Nature-inspired — sky blue (#03A9F4), ocean (#006064), sand (#FFF3E0), sunset gradient
**Типография:** Friendly, clear: Montserrat, Source Sans. Bold для destination names
**UI:** Immersive hero images, destination cards с overlay text, interactive maps, date pickers, price comparison cards
**Анимации:** Image parallax, card flip для деталей, smooth calendar scroll, booking confirmation celebration
**Фишка:** Imagery > UI — фотографии вдохновляют и продают

**Примеры:** Airbnb (immersive photos), Booking.com (data-dense), Skyscanner (card UI)

---

### 12. Образование / Обучение (Education / Learning)

**Цвета:** Friendly — light blue (#BBDEFB), soft purple (#CE93D8), green (#A5D6A7), warm white
**Типография:** Readable, approachable: Nunito, Lato. Крупный body для длинного чтения
**UI:** Course cards, progress bars, quiz interfaces, video player, lesson checklist
**Анимации:** Gamified: XP gain, progress fill, correct/incorrect feedback, badge unlock
**Фишка:** Engagement через gamification + чистота для focus на контенте

**Примеры:** Duolingo (gamified), Coursera (clean academic), Khan Academy (friendly)

---

### 13. Новости / Медиа (News / Editorial)

**Цвета:** Neutral — white (#FFFFFF), light grey (#F5F5F5), dark text (#212121), red accent для breaking
**Типография:** **Serif для заголовков:** Georgia, Merriweather, Noto Serif. Sans-serif для body: 16sp+, high line-height (1.6)
**UI:** Text-heavy, card-based feed, category tabs, reading mode, save/bookmark
**Анимации:** Минимальные — fade для page transitions, subtle для tab switching. Ничего отвлекающего от чтения
**Фишка:** Typography IS the design. Content readability > visual effects

**Примеры:** NYT app (serif + clean), Medium (reading focus), BBC News (structured)

---

### 14. E-Commerce / Магазин (Shopping)

**Цвета:** Brand-dependent. Нейтральный base + brand accent для CTA. Красный/оранжевый для скидок
**Типография:** Clean sans-serif. Bold prices, strike-through для old price. Tabular numbers
**UI:** Product grid (2 колонки), product cards (image + title + price + rating), filters, cart, checkout flow
**Анимации:** Add-to-cart fly animation, image gallery swipe, price count-down, loading skeleton для product grid
**Фишка:** Conversion-focused — каждый элемент ведёт к покупке. Persistent bottom CTA bar

**Примеры:** Amazon (data-dense), ASOS (visual-heavy), Nike (brand + product)

---

### 15. Соцсети (Social Media)

**Цвета:** Platform brand colors + neutral content area. Dark mode popular
**Типография:** System fonts для speed. Username bold, content regular, metadata caption
**UI:** Infinite feed, stories carousel, floating compose FAB, reactions, comments thread
**Анимации:** Heart/like animation, story ring progress, pull-to-refresh, double-tap like, story transition
**Фишка:** Content-first — UI уходит на второй план. Engagement loops. Video fullscreen

**Примеры:** Instagram (visual-first), TikTok (video-first), Twitter/X (text-first)

---

## Сводная таблица стилей

| Стиль | Radius | Тени | Borders | Анимации | Цвета | Шрифт |
|-------|--------|------|---------|----------|-------|-------|
| Строгий | 8-12sp | Subtle | Thin 1px | Minimal fade | Navy+grey | Sans regular |
| Игровой | 16-24sp | Colored glow | Bold colored | Abundant bounce | Bright multi | Rounded bold |
| Яркий | 16-24sp | Neon glow | Minimal | Shimmer+glow | Neon+gradient | Modern extra-bold |
| Минимал | 8-12sp | None/subtle | None/dividers | Fade only | Muted neutral | Thin sans |
| Premium | 0-8sp | None | Ultra-thin | Slow elegant | Dark+gold | Serif headers |
| Neobrutalist | 0-4sp | Hard offset | Thick 2-4px | Instant/none | Flat bright | Mono/bold |
| Фитнес | 12-16sp | Neon glow | Minimal | Energetic pulse | Dark+neon | Condensed bold |
| Медицина | 12-16sp | Subtle | Light | Calm fade | Blue+green+white | Accessible sans |
| Еда | 16-20sp | Warm soft | Minimal | Cart+scroll | Warm red+orange | Friendly rounded |
| Музыка | 8-16sp | None | None | Crossfade+vis | Dark+dynamic | Light sans |
| Travel | 16-20sp | Soft | Overlay | Parallax+flip | Nature tones | Friendly sans |
| Education | 12-16sp | Soft | Light | Gamified | Soft friendly | Readable rounded |
| Новости | 4-8sp | None | Dividers | Minimal | Neutral+red | Serif headlines |
| E-Commerce | 8-12sp | Subtle | Light | Cart+skeleton | Brand+CTA | Clean tabular |
| Соцсети | 12-20sp | None | Minimal | Heart+story | Platform brand | System fonts |

Sources:
- [Fintech UI Trust Examples - Eleken](https://www.eleken.co/blog-posts/trusted-fintech-ui-examples)
- [Business App Designs - SoftKraft](https://www.softkraft.co/business-app-design/)
- [App Gamification Examples - Plotline](https://www.plotline.so/blog/mobile-app-gamification-examples)
- [Gamification in UX - Tubik](https://blog.tubikstudio.com/gamification-in-ux-increasing-user-engagement/)
- [Color Trends 2026 - Envato](https://elements.envato.com/learn/color-scheme-trends-in-mobile-app-design)
- [Neon Gradients UI Trends](https://thevisualcommunicationguy.com/2025/02/25/neon-gradients-and-3d-colors-latest-ui-ux-trends/)
- [Minimalist App Design - SEM Nexus](https://semnexus.com/less-is-more-minimalist-app-design-interface/)
- [Neobrutalism Definition - NN/g](https://www.nngroup.com/articles/neobrutalism/)
- [Neo-Brutalism 2025 - Clover](https://www.clovertechnology.co/insights/how-neo-brutalism-took-over-digital-design-in-2025)
- [Fitness App Design - DesignRush](https://www.designrush.com/best-designs/apps/trends/fitness-app-design-examples)
- [Healthcare UI Design 2026 - Eleken](https://www.eleken.co/blog-posts/user-interface-design-for-healthcare-applications)
- [Food Delivery App Design](https://uistudioz.com/top-10-inspiring-food-delivery-app-ui-ux-designs/)
- [Music Streaming App Design - Mockplus](https://www.mockplus.com/blog/post/music-app-design)
- [Travel App Design Trends - G & Co](https://www.g-co.agency/insights/top-travel-mobile-app-design-trends-ui-inspiration)
- [E-Learning App Design - Shakuro](https://shakuro.com/blog/e-learning-app-design-and-how-to-make-it-better)
- [Kids App Design - AufaitUX](https://www.aufaitux.com/blog/ui-ux-designing-for-children/)
- [News Typography - Toptal](https://www.toptal.com/designers/typography/typography-for-mobile-apps)
- [E-Commerce Product Cards](https://www.heyinnovations.com/resources/product-card)
- [Social Media UX - Komodo](https://www.komododigital.co.uk/insights/how-social-media-apps-ux-ui-are-designed-to-engage-and-be-addictive/)
- [Luxury Fonts - Monotype](https://www.monotype.com/resources/expertise/fonts-and-luxury-brands-fashion)
- [Dark Mobile App UI - Hongkiat](https://www.hongkiat.com/blog/dark-mobile-app-ui/)
- [App Colors 2026 - DesignRush](https://www.designrush.com/best-designs/apps/trends/app-colors)
