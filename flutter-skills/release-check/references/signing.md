# Android signing and repository

Inspect `signing` and `signing_repository` findings. Require populated storeFile,
storePassword, keyAlias and keyPassword in key.properties, an existing keystore,
successful keytool store/alias/private-key checks, and release signing using that
key rather than debug signing. Keep `--gradle` and artifact checks from audit.md.

Resolve relative storeFile paths using the actual app Gradle expression:
`file(...)` is relative to android/app/, `rootProject.file(...)` to android/;
absolute paths stay absolute. The script recognizes common properties indexing,
getProperty and Kotlin `?.let { file(it) }` forms. Dynamic, missing or ambiguous
wiring gives `WARN` and requires manual verification; never assume android/app/
when the base cannot be determined. Properties are parsed as simple key=value;
custom loaders/escaped Java properties need manual verification.

Both the keystore and key.properties must be stored inside the Git repository,
tracked in its index and not match effective ignore rules, including nested
.gitignore files. Even force-added ignored files fail. External files and symlinks
fail. The script checks the index, not commit or push status; do not describe this
as proof that a remote clone contains the files. Missing Git or failed Git commands
are incomplete checks; no repository or untracked/ignored files are failures.

This is the user's required repository policy. Check-only requests do not authorize
git add, commits, uploads, changing ignore rules or regenerating keys. For authorized
fixes, preserve the existing signing identity. Never print passwords, file contents
or raw signing tool output, and keep signing files out of packaged app assets.
