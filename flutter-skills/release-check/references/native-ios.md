# Native iOS release checks

Use this route for an iOS app built directly with Xcode. Resolve the project or workspace, target, scheme, bundle ID and release artifact. Mark the Flutter script N/A for this target and perform the native checks below. Do not treat an inapplicable Flutter check as a native verdict.

- Inspect effective release settings and the compiled package. Verify bundle ID, version/build, display name and applicable locale metadata, device families/orientations, permission text and intended capabilities. Confirm launcher icon in the compiled package and on a real simulator or device Home Screen. Check loading and onboarding if required by the project.
- Check packaging for test bundles, known debug flags, demo fixtures and unintended files. Verify normal clean startup. Report the limits of marker scans. Do not disclose private keys, certificate material or credentials.
- Distinguish Simulator app, device archive and exported IPA. Verify device signing, provisioning, team and entitlements where applicable using the built package and Xcode signing evidence. Report unsigned archives, missing provisioning or untested install explicitly. A successful simulator launch covers the simulator only.
- Apply [user journeys and evidence](acceptance.md) to the actual release build. Check the supported device families and orientations. Record physical-only checks such as sensors, locked/background behavior or real system delivery separately. An unavailable device or permission is a concrete coverage gap.

Summarize source, built artifact, runtime and distribution coverage. State the exact checked path and build identity. Preserve separate statuses for packaging and product acceptance.
