# Release constraints — know before implementing

This is the startup contract; detailed verification is read only at release time. Explicit current user instructions take priority; report any conflict rather than weakening the audit. For a narrow change to an existing app, preserve its agreed scope: this document is not authorization to add onboarding, languages or rebrand the whole product. A separately requested full audit still reports every applicable gap; fixes require the task’s authorization.

Flutter-specific rules below apply to Flutter targets. For native iOS apply the agreed project requirements and the native audit route at release.

- App initialization is inline in runApp(...) called by main() in lib/main.dart: all app wrappers/routing. Screens and business logic remain separate.
- Reachable animated loading and onboarding are mandatory. Loading has an explicit perceptible minimum duration even on fast/cached launches; a native splash alone is insufficient. Verify the animation visually. Onboarding completes into the app.
- Exactly six fully translated languages: en, de, es, fr, it, vi. Effective locales/selector/strings must agree, without untranslated fallback.
- Android Gradle direct integer literals: compileSdk=36, targetSdk=36, minSdk=24, including flavor overrides. No inherited expressions.
- All source images live in nonempty assets/images/, including launcher/splash inputs; an empty directory or .gitkeep alone is insufficient. Every image recursively under assets/ has width at most512px, height unrestricted, aspect ratio/transparency/animation preserved. Generated platform outputs are separate.
- Android INTERNET permission must be declared in android/app/src/main/AndroidManifest.xml; debug/profile declarations alone are insufficient.
- Android keystore and populated key.properties must exist inside the Git repository, be tracked and not match ignore rules. Resolve storeFile using the actual Gradle wiring: file(...) from android/app/, rootProject.file(...) from android/. Keep credentials out of logs and app artifacts.
- Plan meaningful validation, a fresh artifact and genuine screenshots. Tests/QA seed data must not leak into ordinary startup. Credentials must not appear in reports or packaged app assets.

The audit procedure and tools are in SKILL.md and its topic routes. This summary does not prove PASS; actual source/runtime/artifact verification is performed at release.

Plan acceptance evidence for core journeys and risky transitions, including permission denial, persisted settings, empty forms and controls at supported sizes. Check these on the delivered build before calling the release ready.
