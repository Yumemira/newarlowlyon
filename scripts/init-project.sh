#!/usr/bin/env bash

set -euo pipefail

workspace_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
projects_root="$workspace_root/projects"

if [[ $# -gt 1 ]]; then
  echo "Usage: $0 [project-directory-or-name]" >&2
  echo "Example: $0 my_flutter_app" >&2
  exit 2
fi

project_arg="${1:-.}"
if [[ "$project_arg" = /* ]]; then
  project_dir="$project_arg"
elif [[ "$project_arg" = "." ]]; then
  project_dir="$PWD"
else
  project_dir="$projects_root/$project_arg"
fi

project_dir="$(cd "$project_dir" 2>/dev/null && pwd)" || {
  echo "Project directory does not exist: $project_arg" >&2
  exit 1
}

case "$project_dir/" in
  "$projects_root/"*) ;;
  *)
    echo "Project must be inside $projects_root" >&2
    exit 1
    ;;
esac

if [[ ! -f "$project_dir/pubspec.yaml" ]]; then
  echo "Warning: no pubspec.yaml found; continuing with generic Spec Kit setup." >&2
fi

command -v specify >/dev/null 2>&1 || {
  echo "The 'specify' CLI is not available on PATH." >&2
  exit 1
}

(
  cd "$project_dir"
  specify init --here --force --non-interactive \
    --integration codex \
    --integration-options='--skills' \
    --script sh
)

# Project-specific skills are copied from the workspace toolkit into the project.
# The project remains self-contained after it is moved or opened independently.
for skill_dir in "$workspace_root/.agents/skills/flutter-dart" \
                 "$workspace_root/.agents/skills/create-todo" \
                 "$workspace_root/.agents/skills/rescrinit"; do
  if [[ -d "$skill_dir" ]]; then
    mkdir -p "$project_dir/.agents/skills"
    rm -rf "$project_dir/.agents/skills/$(basename "$skill_dir")"
    cp -R "$skill_dir" "$project_dir/.agents/skills/"
  fi
done

if [[ ! -f "$project_dir/AGENTS.md" && -f "$workspace_root/templates/project/AGENTS.md" ]]; then
  cp "$workspace_root/templates/project/AGENTS.md" "$project_dir/AGENTS.md"
fi

echo "Project-local Spec Kit setup is ready: $project_dir"
echo "Spec Kit state: $project_dir/.specify"
echo "Codex skills:   $project_dir/.agents/skills"
