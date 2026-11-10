# Audit

This invocation applies to Flutter applications. For native iOS, follow [native iOS release checks](native-ios.md).

## Choose the target

Resolve the requested application to its actual directory containing `pubspec.yaml`, using the current task context. Read applicable project instructions. The toolkit root is not the application. If the target cannot be inferred among multiple apps, ask for the project; never default to `shiftlore` merely because it was the development example.

Use the script's `--help` to confirm options. Read the detailed behavior document when handling custom launcher configs, flavors, unexpected signing results or incomplete checks. This audit alone does not require reinitializing Spec Kit or changing the application.

Use an explicit `--icon` when the user names the reference image. Otherwise preserve the script's reference selection. For flavors, inspect the project's launcher config and use `--icon-config` as appropriate; intentional platform/brand variants need separate assessment.


## Run the audit

For the requested final audit, include `--gradle` when the project has Android, so the result evaluates effective signing rather than just searching Gradle text. The user's request to run this check covers the normal Gradle signingReport invocation; it may update caches/download dependencies, but does not build the app. Respect an explicit offline/no-execution constraint and report the resulting coverage gap.

Run from the target project, passing its absolute path. Prefer the Bash entry point, which selects uv and isolated Python dependencies. Use structured JSON output for reliable interpretation:

```bash
/Users/davidyolkin/flutterprojects/init_flutter/scripts/check-release.sh \
  /absolute/path/to/project --gradle --json
```

If the user supplied a build or this task produced one, add `--artifact /absolute/path/to/exact-release.apk`; repeat for AAB/IPA as needed. All paths must identify the actual target, not placeholders.

If no artifact is specified, inspect existing outputs and build context to identify a release corresponding to the current work. Do not silently select a stale file or a debug APK. Report a missing/unverified artifact when provenance is unclear. Build a new release only if the existing task authorizes building; a request to check alone does not require creating a new build. Do not run `prepair.sh`, regenerate a key, modify icons or initiate publishing as part of an audit.

Preserve the process exit code and parse the report even for nonzero exits:

- `0`: no detected failures or incomplete checks in the performed audit.
- `1`: issues found; warnings may also be present.
- `2`: incomplete verification, or argument errors if no JSON report exists.

Tool failures, malformed output, timeouts, missing dependencies and unavailable signing tools are incomplete verification, never successful checks. Do not suppress warnings or raise image tolerance simply to obtain a clean report. Never print credentials or raw signing command output that could expose them.


## Report and follow up

Answer in the user's language. Name the project and exact artifacts checked, summarize PASS/FAIL/WARN counts, explain actionable failures with file paths, and state what remains unverified. Include key modification/creation dates when available, distinguishing filesystem birthtime, mtime and keytool entry creation date; ctime is not creation time.

Do not claim that tests cannot have entered the release ‘in any way’: static/marker scans cannot prove absence of arbitrary stripped or obfuscated test code. Do not claim source icon checks verify compiled resource overrides/Assets.car, or Android keystore checks verify iOS provisioning. Report these boundaries when relevant, using the actual script findings.

For check-only requests, report findings without modifying the application. If fixes are already authorized in the ongoing task, fix relevant issues and rerun affected checks; rebuild the exact release first when necessary and authorized. A successful old artifact scan does not validate new source changes. Keep unresolved issues and incomplete coverage explicit in the final result.

For full release acceptance, attach the [user journey matrix](acceptance.md) for the exact build. Keep artifact, runtime and scenario results distinct.
