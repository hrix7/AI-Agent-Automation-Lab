"""Create the verification manifest I use for research and automation outputs."""
from __future__ import annotations
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()

def build_manifest(root: Path) -> dict:
    if not root.is_dir():
        raise NotADirectoryError(root)
    files = []
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        files.append({"path": path.relative_to(root).as_posix(),
                      "bytes": path.stat().st_size, "sha256": sha256(path)})
    return {"root": root.name, "created_at": datetime.now(timezone.utc).isoformat(),
            "file_count": len(files), "files": files}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("folder")
    parser.add_argument("--output")
    args = parser.parse_args()
    manifest = json.dumps(build_manifest(Path(args.folder)), indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(manifest, encoding="utf-8")
    else:
        print(manifest, end="")
