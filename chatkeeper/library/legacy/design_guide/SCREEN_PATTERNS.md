# Паттерны дизайна экранов мобильных приложений

## 1. Loading / Splash Screen

**Задача:** Первое впечатление + маскировка загрузки данных.

**Подходы:**
- **Skeleton Screen (лучший):** Wireframe-заглушки, повторяющие layout будущего контента. Shimmer-анимация (волна слева направо). Используют: YouTube, Facebook, LinkedIn, Google
- **Branded Splash:** Логотип + прогресс-бар. Допустимо для < 3 секунд
- **Animated Loading:** Custom-анимация бренда. Для приложений с длительной инициализацией

**Best practices:**
- Shimmer wave лучше пульсации — воспринимается быстрее на 65%
- Скорость анимации: медленная и плавная (как в Google iOS app)
- Skeleton должен повторять реальный layout (не абстрактные плашки)

---

## 2. Onboarding

**Задача:** Показать ценность, не перегрузив.

**Типы:**
- **Benefits-oriented:** 3-4 слайда с ключевыми преимуществами (PageView)
- **Interactive:** Пользователь сразу пробует функции с подсказками
- **Progressive/Contextual:** Фичи объясняются по мере обнаружения (tooltips, hotspots)

**Best practices:**
- Максимум 3-5 слайдов, < 60 секунд всего
- Skip button ВСЕГДА доступна
- Показывай ценность сразу, не заставляй ждать
- Dot indicators для прогресса
- CTA на последнем слайде крупнее и с акцентом (pulse, gradient)
- Хороший онбординг повышает retention на 50%

---

## 3. Dashboard / Home

**Задача:** Обзор ключевых данных + быстрый доступ к действиям.

**Структура:**
1. Greeting section (опционально, персонализация)
2. KPI cards (2x2 grid или горизонтальный scroll)
3. Quick actions (1-3 кнопки)
4. Recent activity / Timeline
5. Upcoming tasks / Reminders

**Best practices:**
- 3-6 ключевых метрик максимум
- Mobile: single-column, приоритетные метрики сверху
- Cards как building blocks — каждая карточка = 1 метрика
- Pull-to-refresh для обновления
- AnimatedCounter для числовых значений
- Shimmer loading для всех секций

---

## 4. List Page (Список)

**Задача:** Просмотр, поиск, фильтрация коллекции.

**Структура:**
1. Search bar (sticky или с auto-hide)
2. Filter chips / tabs (горизонтальный scroll)
3. Sort control (кнопка или dropdown)
4. List items (cards или rows)
5. FAB для создания нового элемента
6. Empty state при отсутствии данных

**Best practices:**
- Staggered entry анимация (60-80ms per item)
- Dismissible swipe-to-delete с confirm dialog
- Pull-to-refresh
- Lazy loading: 10-30 items, потом "Load more"
- Bottom padding 100sp+ для FAB
- Фильтры: основные видны, расширенные в drawer/sheet

**Варианты layout:**
- **ListView** — стандарт для большинства списков
- **GridView 2 колонки** — для карточек с визуальным акцентом (team members, products)
- **Horizontal scroll** — для категорий, рекомендаций

---

## 5. Detail Page (Детальная)

**Задача:** Полная информация о сущности + действия над ней.

**Два подхода:**

### A. С табами (для сложных сущностей)
- Header card (avatar/image + title + subtitle)
- Quick action buttons row
- TabBar (3-5 табов)
- TabBarView с контентом

**Когда:** Contact Detail (Info/Activity/Deals/Notes), Member Detail

### B. Scroll-секции (для простых сущностей)
- Back button + title
- Секции в GlassCard/Card стопкой
- Action buttons внизу

**Когда:** Deal Detail, Campaign Detail, Template Detail

**Best practices:**
- Header анимация: FadeIn + Scale
- Секции: staggered FadeIn + SlideY
- Quick actions в thumb-zone
- Edit/Delete через навигацию или dialog

---

## 6. Form Page (Форма)

**Задача:** Ввод или редактирование данных.

**Структура:**
1. AppBar с back и title (Create/Edit)
2. Single-column form
3. Submit button (full-width, sticky bottom)
4. Keyboard-aware layout

**Best practices:**
- Один столбец всегда на мобильных
- Label над полем (не placeholder-only)
- Авто-клавиатура по типу поля (numeric, email, etc.)
- Inline validation после потери фокуса (не при вводе!)
- Ошибки: под полем, красный цвет + иконка
- Loading state на submit button
- При сохранении: `Get.back(result: data)` — возврат результата

---

## 7. Settings Page

**Задача:** Управление настройками приложения.

**Структура:**
- Profile header card
- Секции настроек (grouped)
- Icon + Label + Value + Chevron pattern
- Toggle switches для бинарных настроек
- Bottom sheets для выбора из списка
- Danger zone (красные действия) внизу

**Best practices:**
- Группировка по смыслу с заголовками секций
- Краткие подписи ("Уведомления", не "Настроить уведомления")
- Progressive disclosure: базовые видны, дополнительные по запросу
- Search для приложений с 15+ настройками

---

## 8. Profile Page

**Задача:** Информация о пользователе и управление аккаунтом.

**Элементы:**
- Avatar (с возможностью смены)
- Name + Role/Status
- Quick stats (followers, activity, level)
- Action buttons (Edit, Share)
- Activity feed / History
- Settings shortcut

**Best practices:**
- Avatar в thumb-zone или центрирован
- Edit profile — отдельная form page
- Минимум информации на главном экране, подробности по tap

---

## 9. Empty State

**Задача:** Не оставлять пользователя перед пустым экраном.

**4 типа:**
1. **First use** — первый визит, нет данных
2. **User cleared** — пользователь всё удалил
3. **No results** — поиск/фильтр ничего не нашёл
4. **Error state** — ошибка загрузки

**Структура:**
- Иконка или иллюстрация
- Заголовок (что произошло)
- Описание (что делать)
- CTA button (добавить, попробовать снова)

**Best practices:**
- Один message per screen — не перегружай
- CTA должен быть очевидным следующим шагом
- Анимированная иконка лучше статичной
- Сохраняй layout страницы (header, nav остаются)

Sources:
- [Skeleton Screens 101 - NN/g](https://www.nngroup.com/articles/skeleton-screens/)
- [Mobile App Onboarding Guide 2026](https://vwo.com/blog/mobile-app-onboarding-guide/)
- [Empty State UX - Eleken](https://www.eleken.co/blog-posts/empty-state-ux)
- [Settings Design Patterns](https://bricxlabs.com/blogs/settings-page-ui-examples)
- [Profile Page Design](https://www.eleken.co/blog-posts/profile-page-design)
- [Dashboard Design Best Practices](https://www.justinmind.com/ui-design/dashboard-design-best-practices-ux)
- [Form UI Design 2026](https://ixdf.org/literature/article/ui-form-design)
- [Mobile UX Design Examples](https://www.eleken.co/blog-posts/mobile-ux-design-examples)
