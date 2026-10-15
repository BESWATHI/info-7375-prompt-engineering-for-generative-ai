"""Assembles scenes.py = iso_kit.py + iso_originals_25.py + code/scenes_body.py (Gate A copies only scenes.py)."""
from pathlib import Path
R = Path(__file__).resolve().parents[1]
K = R.parents[1] / "brutalist.art/skills/make/show-tell/templates"
parts = [(K / "iso_kit.py").read_text(), (K / "iso_originals_25.py").read_text(), (R / "code/scenes_body.py").read_text()]
(R / "scenes.py").write_text("\n\n".join(parts))
print("scenes.py:", sum(p.count("\n") for p in parts), "lines")
