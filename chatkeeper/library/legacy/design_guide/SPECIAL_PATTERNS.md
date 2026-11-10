# Специальные паттерны дизайна

## 1. Drag & Drop / Kanban Board

**Когда:** Управление задачами, pipeline, сортировка.

**Mobile-специфика:**
- `LongPressDraggable` (200ms delay) — не обычный tap
- Увеличенные drop zones на мобильных
- Feedback: scale 1.05x + opacity, тень
- ChildWhenDragging: opacity 0.3
- Fallback: swipe-to-move или стрелки для мелких экранов

**Microstates:** idle → hover → grab → move → drop (каждый визуально отличается)

**Celebration:** overlay с цветом при успешном drop в финальный этап.

---

## 2. Infinite Scroll / Lazy Loading / Pagination

| Подход | Когда | Плюсы | Минусы |
|--------|-------|-------|--------|
| **Infinite scroll** | Ленты, соцсети | Нет прерываний | Нет контроля, тяжело вернуться |
| **Load more** | Каталоги, списки | Контроль, лёгкость | Требует tap |
| **Pagination** | Таблицы, результаты | Чёткая позиция | Много кликов |

**Оптимальная стратегия для мобильных:**
1. Загрузить 10-30 items
2. Lazy-load ещё 10-30 при скролле
3. После 50-100 items — кнопка "Load more"
4. Virtual scrolling для > 100 items

---

## 3. Atomic Design System

**5 уровней:**
1. **Atoms** — кнопки, иконки, текст, инпуты
2. **Molecules** — поле ввода + label, card header
3. **Organisms** — форма, header, card list
4. **Templates** — layout страницы без реальных данных
5. **Pages** — конкретная страница с данными

**Design Tokens — основа системы:**
- Colors: палитра + semantic (primary, error, surface)
- Typography: sizes, weights, line-heights
- Spacing: 4/8pt grid values
- Elevation: shadows, z-index
- Border radius: набор значений
- Duration: animation timings

---

## 4. Performance Patterns

### Skeleton Loading
- Layout skeleton повторяет реальную структуру
- Shimmer wave слева направо (не пульсация)
- Медленная плавная анимация

### Image Optimization
- Lazy load изображений (только viewport)
- Placeholder → blur → full image
- Правильные размеры (не грузить 4K для 100px thumbnail)

### List Performance
- Virtual scrolling (render только видимое)
- Recycle view holders
- Debounce search input (300-500ms)
- Кэширование результатов

---

## 5. Responsive / Adaptive Design

### Mobile-First подход
1. Начинай с mobile (375px)
2. Масштабируй для tablet
3. Адаптируй для desktop

### Breakpoints
| Устройство | Width | Columns | Margin |
|-----------|-------|---------|--------|
| Mobile | < 600px | 4 | 16px |
| Tablet | 600-1024px | 8 | 24px |
| Desktop | > 1024px | 12 | 32px |

### Адаптивные паттерны
- **Stacked → Side-by-side:** List + Detail на tablet
- **Grid columns:** 2 на mobile → 3-4 на tablet
- **Navigation:** Bottom tabs → Side rail → Full sidebar
- **Typography:** Scale factor per breakpoint

---

## 6. Parallax / Hero Header

**Когда:** Landing, profile, detail pages с визуальным акцентом.

**Mobile осторожно:**
- Parallax может быть тяжёлым для performance
- Рассмотреть отключение на mobile
- Альтернатива: SliverAppBar с collapsing header

---

## 7. Timeline / Activity Feed

**Структура:**
- Вертикальная линия-коннектор
- Circular dot/avatar на линии
- Content card справа от линии
- Timestamp

**Best practices:**
- Цветовое кодирование по типу активности
- Staggered анимация при появлении
- Filter bar сверху (по типу, по дате)
- Quick add widget для быстрого добавления

---

## 8. Calendar View

**Подходы:**
- **Month grid** — обзор месяца с индикаторами
- **Week strip** — горизонтальный скролл недели
- **Day detail** — расписание на день

**Toggle:** Переключение calendar ↔ list view

---

## 9. AI-Персонализация (Тренд 2025-2026)

**Что адаптируется:**
- Контент на dashboard (по частоте использования)
- Порядок элементов в списках (по релевантности)
- Suggestions (на основе паттернов использования)
- UI layout (упрощение для новичков, power-mode для экспертов)

**Принцип:** AI адаптирует, но пользователь контролирует.

Sources:
- [Drag and Drop UX - LogRocket](https://blog.logrocket.com/ux-design/drag-and-drop-ui-examples/)
- [Pagination vs Infinite Scroll - Smashing Magazine](https://www.smashingmagazine.com/2016/03/pagination-infinite-scrolling-load-more-buttons/)
- [Atomic Design - Brad Frost](https://atomicdesign.bradfrost.com/chapter-2/)
- [Spacing & Grids - designsystems.com](https://www.designsystems.com/space-grids-and-layouts/)
- [Mobile App Design Trends 2026](https://www.designveloper.com/blog/mobile-app-design-trends/)
- [Flutter Design Patterns 2025](https://medium.com/@fahadbhatt/top-10-flutter-design-patterns-you-should-know-in-2025-0fed92b80a52)
- [Dashboard KPI Design](https://growth-onomics.com/how-to-design-mobile-kpi-dashboards/)
