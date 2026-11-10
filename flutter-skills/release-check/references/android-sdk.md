# Android Sdk

## Android SDK versions

Require direct integer literals in the application's Android Gradle settings:
`compileSdk = 36`, `targetSdk = 36`, and `minSdk = 24`.
Do not accept `flutter.compileSdkVersion`, `flutter.targetSdkVersion`,
`flutter.minSdkVersion`, variables, version catalogs, strings, expressions or
other numeric values. The script reports these as `FAIL` under `android_sdk`.
Groovy `*SdkVersion 36` / `*SdkVersion(36)` forms are accepted only with the exact
required literal (24 for minSdk). Check every flavor override as well.
For check-only requests, report mismatches without rewriting the application.

## Internet permission

Inspect `android_internet`: require an unrestricted `<uses-permission
android:name="android.permission.INTERNET"/>` directly under the main manifest
root in `android/app/src/main/AndroidManifest.xml`. A declaration only in debug or
profile does not pass. Commented entries, entries removed with `tools:node`, and
entries capped by `android:maxSdkVersion` do not satisfy this requirement.
Malformed/unreadable XML is incomplete verification. This source check does not
prove the effective manifest of every flavor or compiled artifact.

