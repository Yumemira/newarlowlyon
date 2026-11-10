# Localization

## Mandatory translation languages

Every application must provide complete translations into **all and only** these
six languages:

1. English (`en`)
2. German (`de`)
3. Spanish (`es`)
4. French (`fr`)
5. Italian (`it`)
6. Vietnamese (`vi`)

Verify that the effective supported locales and language selector expose exactly
this language set, and inspect the localization resources for complete coverage
of user-facing strings, including loading and onboarding. Locale region/script
variants do not replace a required language or permit an additional language.
An enabled locale without its translations, missing keys, or fallback to another
language for untranslated text does not satisfy the requirement.

Report any missing language, additional supported language, or incomplete
translation as `FAIL`, naming the affected languages and files. If coverage cannot
be verified, report it as incomplete rather than `PASS`. Report this check
separately from the script's JSON counts and exit code unless the script explicitly
implements it. For check-only requests, report violations without modifying the
application.

