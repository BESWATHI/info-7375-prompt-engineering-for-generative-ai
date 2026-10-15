#!/usr/bin/env bash
# Assemble scenes.py = show-tell iso_kit + approved original props + this film's scenes.
# Gate A copies only scenes.py, so the kit is pasted in, never imported (show-tell SKILL.md).
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
KIT="${ART_HOME:-$HERE/../../Brutalist}/skills/make/show-tell/templates"
cat "$KIT/iso_kit.py" "$KIT/iso_originals_25.py" "$HERE/scenes_body.py" > "$HERE/scenes.py"
echo "scenes.py: $(grep -c '^class B' "$HERE/scenes.py") scenes"
