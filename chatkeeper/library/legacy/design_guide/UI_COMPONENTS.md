# Паттерны UI-компонентов мобильных приложений

## 1. Bottom Navigation Bar

**Когда:** Приложение с 3-5 основными разделами.

**Правила:**
- 3-5 пунктов (не больше!)
- Icon + label (иконки без подписей = угадывание)
- Active state: filled icon + accent color + glow/shadow
- Persistent — не скрывается при скролле
- Каждый пункт ведёт на destination напрямую (не меню, не popup)
- Badge для уведомлений: маленький, top-right угол иконки

**Bottom nav > Hamburger menu:**
- +65% daily active users (Redbooth case)
- +70% session time
- Thumb-reachable на больших экранах
- Видимость = обнаруживаемость фичей

**Реализация:** IndexedStack (persist state) или PageView (анимация переключения)

---

## 2. Bottom Sheet

**Когда:** Вторичный контент, выбор из опций, быстрые формы.

**Типы:**
- **Modal** — блокирует фон, для фокусных задач
- **Non-modal** — фон доступен, для доп. информации

**Структура:**
1. Drag handle (визуальная подсказка что можно смахнуть)
2. Title + close button
3. Scrollable content
4. Action button (full-width)
5. Keyboard padding

**Best practices:**
- maxHeight: 85% экрана
- Background частично видна (пользователь знает где он)
- +25-30% engagement vs traditional modals
- Dismiss: swipe down, tap backdrop, close button
- Для mobile: CTA в thumb-zone

---

## 3. Card (Карточка)

**Когда:** Группировка связанной информации в единый контейнер.

**Почему карточки работают:**
- Chunked content = сканируемость
- Responsive: легко масштабируются
- Модульность: одна карточка = одна единица информации

**Типы:**
- **Info card** — метрика/KPI (Dashboard)
- **List card** — элемент в списке (Contact, Deal)
- **Content card** — контент с медиа (Netflix, Instagram)
- **Action card** — карточка с CTA (Onboarding, Promotion)

**Best practices:**
- Одна идея на карточку
- Corner radius: 12-20sp
- Padding: 12-20sp
- Тень или border для визуального отделения
- Tap на всю карточку (не мелкие кнопки внутри)

---

## 4. Tab Bar / Segmented Control

**Tab Bar** — переключение между разделами одной страницы.
**Segmented Control** — фильтрация контента в одном view.

**Правила:**
- 2-5 табов максимум
- Если не помещаются: scrollable tabs
- Active indicator: underline, fill, или gradient
- Label + optional icon
- Контент меняется мгновенно (без loading при переключении если данные есть)

**Отличие:**
- Tabs: разный контент в каждом табе
- Segmented: один тип контента, разные фильтры

---

## 5. FAB (Floating Action Button)

**Когда:** Одно главное действие на экране (Create, Add, Compose).

**Правила Material Design:**
- Один FAB на экран
- Только позитивные действия (Create, Share, Navigate)
- Размер: 56dp standard, 40dp mini
- Отступ от края: минимум 16dp
- Не перекрывает важный контент
- Не кладите badge поверх FAB

**Варианты:**
- **Regular:** icon only, круглый
- **Extended:** icon + text, pill shape
- **Speed Dial:** раскрывается в 3-6 sub-actions

---

## 6. Dialog (Диалог)

**Когда:** Подтверждение критичного/деструктивного действия.

**Best practices:**
- Чем реже — тем эффективнее (не злоупотреблять!)
- Текст кнопки = действие ("Удалить аккаунт", не "Да")
- Деструктивная кнопка: красный акцент
- Краткий текст: что случится + последствия
- Undo вместо confirm — если действие обратимо

**Типология:**
- **Confirm:** стандартная, Cancel + Action
- **Destructive:** Cancel + Red Action, с описанием последствий
- **High-friction:** ввод текста для подтверждения ("Type DELETE to confirm")

---

## 7. Snackbar / Toast

**Snackbar** — уведомление + опциональное действие (Undo).
**Toast** — только информация, без действий.

**Правила:**
- Один на экране одновременно
- Длительность: 3-4 секунды
- Позиция: bottom (над bottom nav)
- Текст: 20-30 слов максимум
- Snackbar с Undo — лучше чем confirm dialog для обратимых действий

---

## 8. Search + Filter + Sort

**Search:**
- Sticky или prominent position
- Авто-suggestions при вводе
- Recent searches

**Filter:**
- Chip bar для основных (3-4 фильтра)
- Drawer/Sheet для расширенных
- Показывать кол-во результатов

**Sort:**
- Dropdown или bottom sheet
- Активный sort отображается в UI

---

## 9. Pull-to-Refresh

**Когда:** Списки с динамическим контентом.

**Правила:**
- Визуальный feedback при pull (индикатор)
- Threshold не слишком маленький (случайные срабатывания) и не слишком большой
- Не использовать на pan-контенте (карты, canvas)
- Анимация обновления

---

## 10. Gesture Navigation

**Основные жесты:**
- **Tap** — выбор
- **Swipe horizontal** — навигация (back, dismiss, reveal actions)
- **Swipe vertical** — scroll, pull-to-refresh, dismiss sheet
- **Long press** — контекстное меню, drag & drop
- **Pinch** — zoom

**Правила:**
- Жест НИКОГДА не должен быть единственным способом действия
- Всегда backup: кнопка/меню для той же функции
- Consistent across app
- iOS: swipe-from-left = back (обязательно)

Sources:
- [Bottom Navigation Guide 2025](https://blog.appmysite.com/bottom-navigation-bar-in-mobile-apps-heres-all-you-need-to-know/)
- [Bottom Sheets - NN/g](https://www.nngroup.com/articles/bottom-sheet/)
- [Card UI Best Practices - Mobbin](https://mobbin.com/glossary/card)
- [FAB - Material Design 3](https://m3.material.io/components/floating-action-button/overview)
- [Confirmation Dialogs - NN/g](https://www.nngroup.com/articles/confirmation-dialog/)
- [Snackbar vs Toast](https://medium.com/design-bootcamp/ux-blueprint-01-snackbar-vs-toast-decoding-the-subtle-differences-in-design-systems-8ad82ff61115)
- [Search Sort Filter - Smashing Magazine](https://www.smashingmagazine.com/2012/04/ui-patterns-for-mobile-apps-search-sort-filter/)
- [Gesture Navigation Best Practices](https://www.sidekickinteractive.com/designing-your-app/gesture-navigation-in-mobile-apps-best-practices/)
- [Tabs UX - Eleken](https://www.eleken.co/blog-posts/tabs-ux)
