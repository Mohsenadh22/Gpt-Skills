"""Verify every vendored source file against its pinned provenance manifest."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def verify() -> list[dict]:
    manifest = json.loads((ROOT / "sources.lock.json").read_text(encoding="utf-8"))
    skills = manifest["skills"]
    if len(skills) != 18:
        raise ValueError(f"Expected 18 skills, found {len(skills)}")
    names = set()
    count = 0
    for skill in skills:
        if not re.fullmatch(r"[a-z0-9-]+", skill["name"]):
            raise ValueError(f"Invalid skill name: {skill['name']}")
        if skill["name"] in names:
            raise ValueError(f"Duplicate skill name: {skill['name']}")
        names.add(skill["name"])
        path = (ROOT / skill["path"]).resolve()
        if not path.is_relative_to(ROOT / ".agents" / "skills"):
            raise ValueError(f"Invalid source path: {path}")
        content = (path / "SKILL.md").read_text(encoding="utf-8-sig")
        if not content.startswith("---") or not re.search(r"^description:", content, re.MULTILINE):
            raise ValueError(f"Missing skill frontmatter: {skill['id']}")
        if not re.fullmatch(r"[0-9a-f]{40}", skill["commit"]):
            raise ValueError(f"Invalid upstream commit: {skill['id']}")
        expected = skill["files"]
        actual = {
            p.relative_to(path).as_posix() for p in path.rglob("*")
            if p.is_file() and "__pycache__" not in p.parts
        }
        if actual != set(expected):
            raise ValueError(f"Source file list differs: {skill['id']}")
        for relative, checksum in expected.items():
            file_path = (path / relative).resolve()
            if not file_path.is_relative_to(path) or file_path.is_symlink():
                raise ValueError(f"Unsafe file path: {relative}")
            if hashlib.sha256(file_path.read_bytes()).hexdigest() != checksum:
                raise ValueError(f"Source checksum mismatch: {skill['id']}/{relative}")
            count += 1
        license_path = skill.get("repository_license")
        if license_path and not (ROOT / license_path).is_file():
            raise ValueError(f"Missing source license: {license_path}")
    print(f"Verified {len(skills)} skills and {count} source files.")
    return skills


if __name__ == "__main__":
    verify()
