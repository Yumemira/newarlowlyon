# Acceptance on the release build

Apply to final mobile release acceptance. Select applicable scenarios from the product requirements, known defects and actual user journeys. For a targeted check, cover the affected flow and shared dependencies. Use the real application with isolated QA data. Include a clean launch without demo seeding. Record the exact build, device or simulator, OS, locale, orientation, and relevant settings. Use the release app where possible and identify any debug-only evidence.

## Required coverage when applicable

- Permissions and dependencies. Test allowed, denied, unavailable and recovery paths for each dependency used by a key journey. Deny permission, relaunch, start the dependent flow and an unrelated flow. Look for repeated alerts, wrong prompts and cross-feature blocking. Compare notification scheduling and background behavior with the project requirements.
- State and persistence. Set a known value, change a related setting, confirm and cancel in separate runs. Inspect both the expected change and neighboring values. Kill and reopen the app and verify persisted state. Include migration when the release changes storage or is an upgrade.
- Forms and destructive actions. Test empty and whitespace-only input, valid submission, drafts, invalid values, cancel, and delete. Check visible reasons for disabled actions, confirmation or usable undo for data loss, and a useful default title. Test real actions and results, including quick-add controls.
- Numbers and time. Test absent readings, invalid zero records, nonzero durations under a minute and normal sessions. Compare active screen, summary and history. Check local date defaults across midnight and daylight changes when relevant. Missing data and measured zero are distinct states.
- Layout and contrast. Reach and tap the last actionable control at compact sizes, with large text and keyboard or overlays present. Verify supported tablet orientations and window widths. Check actual foreground/background pairs for relevant text and states, including field placeholders in sheets. For normal text use at least 4.5:1 where the project requires that threshold. Record the pairs and measurements. Decorative styling alone does not show an actionable control is reachable.
- Localized behavior. Verify visible controls and validation messages, singular/plural, dates/units and language names. Open and close sheets, check back/cancel, and follow the complete journey through its result. Cover high-risk locales and any explicitly required full locale matrix.

## Evidence and verdict

For each required scenario record ID, initial state, action, expected behavior, observed behavior, exact build/environment and evidence path. Use a recording or a meaningful test for interactions and persistence; a screenshot can establish appearance. Include failures and retests. Use PASS, FAIL, NOT VERIFIED or N/A with a concrete reason. Separate simulator/test-injected data from physical sensors, background delivery, signing and installation. Use accepted limitations only when the scope or user explicitly allows them.

Report artifact audit and scenario verdict independently. A failed required scenario blocks readiness. An unverified required scenario leaves readiness incomplete until verified or explicitly excluded from scope. After a change rerun the affected scenarios and rebuild or recheck artifacts as needed. Retain an accurate distinction between earlier evidence and the final build. Report check-only findings without edits. Build or fix within already authorized scope.
