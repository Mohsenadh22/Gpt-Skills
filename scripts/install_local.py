"""Install this reviewed collection without overwriting existing local skills."""

from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
import shutil

from verify_collection import ROOT, verify


def identical(destination: Path, files: dict[str, str]) -> bool:
    actual = {
        p.relative_to(destination).as_posix() for p in destination.rglob("*")
        if p.is_file() and "__pycache__" not in p.parts
    }
    if actual != set(files):
        return False
    return all(hashlib.sha256((destination / p).read_bytes()).hexdigest() == digest
               for p, digest in files.items())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, help="Override the user skills directory")
    parser.add_argument("--dry-run", action="store_true", help="Verify and show the plan without copying")
    args = parser.parse_args()
    destination = args.dest or Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "skills"
    destination = destination.expanduser().resolve()
    skills = verify()
    plan = []
    for skill in skills:
        target = destination / skill["name"]
        if target.exists():
            if not target.is_dir() or not identical(target, skill["files"]):
                raise SystemExit(f"Existing skill differs and was preserved: {target}")
            print(f"Already installed: {skill['name']}")
        else:
            plan.append((ROOT / skill["path"], target))
    if args.dry_run:
        for _, target in plan:
            print(f"Would install: {target}")
        print(f"Ready to install {len(plan)} skills. No files changed.")
        return
    destination.mkdir(parents=True, exist_ok=True)
    for source, target in plan:
        shutil.copytree(source, target)
        print(f"Installed: {target}")
    print(f"Installed {len(plan)} skills. They are available on the next Codex turn.")


if __name__ == "__main__":
    main()
