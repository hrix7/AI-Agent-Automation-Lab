"""Create a safe, predictable research experiment scaffold."""
from __future__ import annotations
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

FOLDERS = ("inputs", "outputs", "logs", "notes")

def plan(root: Path) -> list[Path]:
    return [root, *(root / name for name in FOLDERS)]

def create(root: Path, dry_run: bool = False) -> list[str]:
    targets = plan(root)
    if root.exists():
        raise FileExistsError(f"Refusing to overwrite existing path: {root}")
    if dry_run:
        return [str(path) for path in targets]
    for path in targets:
        path.mkdir(parents=True, exist_ok=False)
    manifest = {
        "name": root.name,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": "planned",
        "data_policy": "Do not place restricted or identifiable data in version control.",
    }
    (root / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return [str(path) for path in targets]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    print("\n".join(create(Path(args.name), args.dry_run)))
