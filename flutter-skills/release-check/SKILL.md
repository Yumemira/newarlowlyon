---
name: release-check
description: "Perform final mobile release acceptance. Run the existing Flutter release auditor for icons, Android signing and test leakage, and verify user journeys on the exact release build. For native iOS, use the platform-specific manual route. Use for $release-check and final release audits, not after routine edits."
---

# Release check

For Flutter, use the maintained artifact auditor: `/Users/davidyolkin/flutterprojects/init_flutter/scripts/check-release.sh` (Python implementation check_release.py). Confirm options with --help. The audit does not itself build, run prepair.sh, regenerate keys or publish. For check-only requests report findings without modifying the app. Already-authorized fixes may correct issues and rebuild/rerun affected checks.

## Read by stage

- Before implementation: only [requirements](references/requirements.md). Do not preload the procedures below.
- At final acceptance: [user journeys and evidence](references/acceptance.md). Use it for Flutter and native iOS.
- When auditing Flutter: [target, invocation and report](references/audit.md), then the applicable verification topics: [startup/app tree](references/startup.md), [six languages](references/localization.md), [images](references/images.md), and [Android SDK/Internet](references/android-sdk.md) and [signing/repository](references/signing.md) when Android exists. Each check remains mandatory when applicable; splitting files is not permission to skip checks.
- When auditing native iOS: [native iOS release checks](references/native-ios.md).
- Custom flavors/icons, unexpected signing or incomplete checks: `/Users/davidyolkin/flutterprojects/init_flutter/docs/release-audit.md`, relevant sections only.

Run the Flutter auditor from the actual application directory. Android final audit includes --gradle; pass --artifact for the exact fresh APK/AAB/IPA. Preserve exit code and JSON:0=passed performed audit;1=issues;2=incomplete/argument failure. Tool errors/timeouts are incomplete. Manual startup/localization/image checks are reported separately unless implemented in the JSON auditor. Do not hide WARN, change tolerances or print credentials. Final report distinguishes source/runtime/artifact coverage and identifies remaining gaps.

For a full release, record the artifact audit and scenario acceptance separately. A passing artifact audit cannot close a failed or unverified required user journey. For a narrow audit, label its scope and preserve applicable findings.
