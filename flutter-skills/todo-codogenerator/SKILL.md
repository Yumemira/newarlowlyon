---
name: todo-codogenerator
description: Convert a user's feature or refactoring plan into a compile-ready, TODO-only source-code scaffold. Use when the user invokes $todo-codogenerator, selects TODO-codogenerator from the slash-command skill list, or asks to prepare project structure, classes, interfaces, method signatures, and integration markers without implementing behavior.
---

# TODO Codogenerator

Turn the user's implementation plan into structure inside the codebase. Create the smallest useful set of files, types, members, and `TODO` markers while deliberately leaving business behavior unimplemented.

## Workflow

1. Read the full request after the invocation as the scaffold specification.
2. Inspect applicable repository instructions, build layout, module ownership, nearby implementations, naming conventions, and current working-tree changes.
3. Follow every repository-mandated planning or governance workflow. Treat the requested deliverable as a planning scaffold, not permission to bypass local rules.
4. Resolve only uncertainty that would materially change ownership, public contracts, persistence, security, or file layout. Otherwise make a conservative assumption and state it.
5. Design the minimal file and symbol map needed to make the intended implementation obvious.
6. Create or edit the scaffold with patch-based file edits. Preserve unrelated user changes.
7. Run the repository-approved compile or packaging check that does not execute tests. If local instructions forbid or omit verification, perform syntax-oriented inspection instead.
8. Report the affected files, the planned responsibility of each, verification performed, and that runtime behavior remains intentionally unfinished.

## Scaffold Rules

- Do not implement business logic, algorithms, persistence, networking, event effects, or user-visible behavior.
- Create only structural elements needed by the plan: packages, classes, records, interfaces, enums, constructors, fields, method signatures, configuration shapes, and safe integration markers.
- Put a concrete `// TODO:` inside every unfinished class or method. Describe the implementation action, relevant contract, and important edge cases; avoid vague comments such as `// TODO: implement`.
- Follow the repository's language rules for identifiers and comments. If none exist, write identifiers in English and `TODO` text in the user's language.
- Keep source files syntactically valid. For a method that cannot compile with a comment-only body, add the `// TODO:` and then the smallest fail-fast placeholder allowed by the language, such as `throw new UnsupportedOperationException("TODO")` in Java. Never return fake success, `null`, or fabricated data merely to compile.
- Prefer interfaces or abstract contracts when they accurately represent the design; do not distort the architecture just to avoid a placeholder body.
- Record inputs, outputs, failure behavior, threading or lifecycle constraints, validation, configuration, and integration dependencies in the nearest relevant `TODO` comments.
- Use ordered TODO identifiers such as `TODO(S1)`, `TODO(S2)` only when dependencies or implementation order matter. Keep identifiers consistent across files.
- Do not register, enable, schedule, expose, or call an unfinished component at runtime. Add a TODO at the future integration point instead.
- Do not add migrations, secrets, live credentials, generated binaries, or runtime data.
- Do not create passing empty tests. Add test-case TODOs only when explicitly requested or required by repository rules, and ensure they cannot be mistaken for completed coverage.
- Do not replace existing working code with placeholders unless the user explicitly asks for that exact refactor scaffold.

## TODO Quality

Make each marker implementable without rediscovering the design. Prefer:

```java
// TODO(S2): Resolve the player's configured locale from the immutable profile snapshot.
// Fall back to the server default when the profile has no locale; do not perform file I/O here.
throw new UnsupportedOperationException("TODO(S2)");
```

Avoid:

```java
// TODO: add code
return null;
```

## Completion Boundary

Stop when the architectural scaffold is present, TODOs are specific and internally consistent, and the permitted compile/package check succeeds. Do not continue from scaffolding into implementation unless the user gives a separate explicit instruction.
