# Паттерны навигации мобильных приложений

## Сравнение подходов

| Паттерн | Плюсы | Минусы | Когда |
|---------|-------|--------|-------|
| **Bottom Tab Bar** | Thumb-friendly, видимость, +65% DAU | Max 5 пунктов | 3-5 основных разделов |
| **Hamburger Menu** | Много пунктов, чистый UI | Скрытость, -50% discoverability | Вторичная навигация |
| **Tab Bar (top)** | Фильтрация контента, скролл | Далеко от thumb-zone | Табы внутри страницы |
| **Bottom Sheet Nav** | Контекстная, flexible | Не для основной навигации | Выбор из опций |
| **Gesture Nav** | Максимум пространства, natural | Discoverable only by learned users | Дополнение к кнопкам |

### Гибридный подход (Best Practice 2025)
Bottom tab bar для основных разделов + hamburger/more для вторичных.
Пример: 4 таба + "More" таб с меню дополнительных разделов.

---

## Master-Detail (Список → Детальная)

**Самый распространённый паттерн в мобильных приложениях.**

### Mobile (Stacked)
```
List Page → push → Detail Page → push → Edit Page
                                      ← back(result)
            ← back
```

### Tablet (Side-by-side)
```
┌──────────────┬──────────────────────┐
│  Master List │   Detail View        │
│  (1/3)       │   (2/3)              │
└──────────────┴──────────────────────┘
```

### Паттерн "Push with Result"
```dart
// Вызов
final result = await Get.toNamed('/edit', arguments: id);
if (result != null) { reload(); }

// Возврат
Get.back(result: updatedData);
```
**Применение:** Add/Edit формы → обновление списка при возврате.

---

## Навигационные жесты

| Жест | Действие | Платформа |
|------|----------|-----------|
| Swipe from left | Back (назад) | iOS (обязательно) |
| System back button | Back | Android |
| Swipe down | Dismiss sheet/modal | Обе |
| Swipe left on item | Reveal actions / Delete | Обе |
| Long press | Context menu / Drag | Обе |

**Правило:** Жест = shortcut. Кнопка = обязательная альтернатива.

---

## Tab Navigation внутри страницы

### TabBar + TabBarView
```
┌─────────────────────────────┐
│ [Tab 1] [Tab 2] [Tab 3]    │  ← TabBar
├─────────────────────────────┤
│                             │
│   Content for Tab 1         │  ← TabBarView
│                             │
└─────────────────────────────┘
```

**Правила:**
- 2-5 табов
- Indicator: underline, fill, или gradient
- Active: accent color, bold
- Inactive: secondary text color
- Swipe между табами (опционально)

### Segmented Control (фильтр в одном view)
- Переключение отображения, не навигация
- 2-4 сегмента
- Общий контент может сохраняться

---

## Bottom Sheet как навигация

### Modal Sheet (Создание/Выбор)
```
Page → open sheet → fill form → submit → close sheet → refresh page
```

### Selection Sheet (Выбор из списка)
```
Settings → tap "Language" → sheet with options → select → close → update setting
```

### Nested Sheet (Вложенные)
```
Activity Sheet → tap "Select Contact" → Contact picker sheet → select → back to Activity Sheet
```
**Осторожно:** Максимум 2 уровня вложенности sheets.

---

## Dialog Navigation

### Confirm + Act
```
User taps "Delete" → Confirm Dialog → "Delete" → action → back(result: true)
```

### Undo Pattern (альтернатива dialog)
```
User taps "Delete" → item removed instantly → Snackbar "Deleted. [Undo]" → 4 sec timeout
```
**Undo лучше dialog** когда действие обратимо — меньше friction.

---

## Deep Navigation

### Переход между связанными сущностями
```
Contact Detail → tap "Reminders" → Reminders Page (pre-selected contact)
Deal Detail → tap contact name → Contact Detail
Member Detail → tap deal → Deal Detail
```

### Передача контекста
- ID через arguments: `goToReminders(arguments: contactId)`
- Pre-populate forms: контроллер читает arguments в onInit
- Не передавать сложные объекты — только ID, подгружать в контроллере

---

## Auth / Onboarding Flow

### Clear-stack навигация
```
Loading → check auth → offAllNamed('/onboarding')  // clear entire stack
Onboarding complete  → offAllNamed('/home')         // clear entire stack
Logout              → offAllNamed('/loading')        // clear entire stack
```

**`offAllNamed`** — очищает весь стек. Пользователь не может нажать "назад" к предыдущему состоянию.

---

## Lazy Loading Controllers

**Проблема:** Не создавать все контроллеры при старте приложения.

**Решение:**
```dart
// В bindings GetPage
binding: BindingsBuilder.put(Controller.new)  // lazy, создаётся при навигации

// В BottomNavShell для табов
if (!Get.isRegistered<DashboardController>()) {
  Get.put(DashboardController());
}
```

**Tab refresh:** При переключении таба вызывать controller.loadData() для обновления.

Sources:
- [Hamburger vs Bottom Nav - Acclaim](https://acclaim.agency/blog/the-future-of-mobile-navigation-hamburger-menus-vs-tab-bars)
- [Mobile Navigation Patterns - UXPin](https://www.uxpin.com/studio/blog/mobile-navigation-patterns-pros-and-cons/)
- [Bottom Navigation Complete Guide](https://blog.appmysite.com/bottom-navigation-bar-in-mobile-apps-heres-all-you-need-to-know/)
- [Master-Detail Pattern](https://appli.io/the-master-detail-interface-pattern/)
- [Destructive Actions UX](https://uxpsychology.substack.com/p/how-to-design-better-destructive)
- [Mobile Navigation UX 2026](https://www.designstudiouiux.com/blog/mobile-navigation-ux/)
- [Tabs UX Best Practices](https://www.eleken.co/blog-posts/tabs-ux)
