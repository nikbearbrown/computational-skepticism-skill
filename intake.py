#!/usr/bin/env python3
"""Read-only inventory of one explicitly authorized local project snapshot."""
import argparse
import json
import os
import re
import stat
from collections import deque

SKIP = {".git", ".hg", ".svn", ".ssh", ".aws", "node_modules", ".venv",
        "__pycache__", "pantry", "vendor", "dist", "build"}
SAFE_TYPES = {".md", ".txt", ".rst", ".py", ".js", ".jsx", ".ts", ".tsx", ".json",
              ".yaml", ".yml", ".toml", ".csv", ".go", ".java", ".rb", ".rs",
              ".sql", ".gd", ".html", ".css", ".r", ".kt", ".c", ".cpp", ".h"}
SECRET = re.compile(r"(?i)(^\.env($|\.)|secret|credential|passwd|private[_-]?key|token|^id_(rsa|ed25519)|\.pem$|\.key$)")
DIR_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW


def open_dir(root_fd, rel):
    """Open each component without traversing symlinks."""
    fd = os.dup(root_fd)
    try:
        for part in rel:
            child_fd = os.open(part, DIR_FLAGS, dir_fd=fd)
            os.close(fd)
            fd = child_fd
        return fd
    except BaseException:
        os.close(fd)
        raise


def inventory(target, max_entries, max_bytes):
    # Walk ancestor components without following symlinks either. A path such as
    # /tmp on macOS should be presented in canonical form by the caller.
    absolute = os.path.abspath(target)
    base = os.open("/", DIR_FLAGS)
    reports = []
    skipped = {"excluded": 0, "symlink_or_special": 0, "oversize": 0, "unreadable": 0}
    bucket = {"plan", "evaluation", "data", "code", "documentation", "configuration"}
    seen = 0
    limited = False
    try:
        root = open_dir(base, tuple(absolute.split("/")[1:]) if absolute != "/" else ())
    finally:
        os.close(base)
    try:
        queue = deque([()])
        while queue and not limited:
            rel = queue.popleft()
            try:
                fd = open_dir(root, rel)
            except OSError:
                skipped["unreadable"] += 1
                continue
            try:
                with os.scandir(fd) as entries:
                    for entry in entries:
                        if seen == max_entries:
                            limited = True
                            break
                        seen += 1
                        name = entry.name
                        if name.casefold() in SKIP or SECRET.search(name) or not name.isprintable():
                            skipped["excluded"] += 1
                            continue
                        path = (*rel, name)
                        try:
                            info = entry.stat(follow_symlinks=False)
                        except OSError:
                            skipped["unreadable"] += 1
                            continue
                        if stat.S_ISDIR(info.st_mode):
                            queue.append(path)
                            continue
                        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
                            skipped["symlink_or_special"] += 1
                            continue
                        ext = os.path.splitext(name)[1].lower()
                        if ext not in SAFE_TYPES:
                            skipped["excluded"] += 1
                            continue
                        if info.st_size > max_bytes:
                            skipped["oversize"] += 1
                            continue
                        low = "/".join(path).lower()
                        if re.search(r"(^|[/_.-])(test|eval|benchmark|fixture|tests|evaluation)", low):
                            group = "evaluation"
                        elif re.search(r"(^|[/_.-])(plan|proposal|blueprint|design|roadmap)", low):
                            group = "plan"
                        elif ext == ".csv":
                            group = "data"
                        elif ext in {".json", ".yaml", ".yml", ".toml"}:
                            group = "configuration"
                        elif ext in {".md", ".rst", ".txt"}:
                            group = "documentation"
                        else:
                            group = "code"
                        assert group in bucket
                        reports.append({"path": "/".join(path), "bytes": info.st_size, "candidate_type": group})
            except OSError:
                skipped["unreadable"] += 1
            finally:
                os.close(fd)
    finally:
        os.close(root)
    return {"kind": "intake_only_not_an_audit", "entries_examined": seen, "entry_limit_reached": limited,
            "coverage_incomplete": limited or any(skipped.values()), "skipped": skipped,
            "candidates": sorted(reports, key=lambda x: (x["candidate_type"], x["path"]))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="Canonical path to an authorized local directory")
    parser.add_argument("--max-entries", type=int, default=500)
    parser.add_argument("--max-bytes", type=int, default=262144)
    a = parser.parse_args()
    if not (1 <= a.max_entries <= 10000 and 1 <= a.max_bytes <= 1048576):
        parser.error("limits: entries 1–10000, bytes 1–1048576")
    if "://" in a.target or a.target == "-" or os.path.abspath(a.target) == "/":
        parser.error("provide one authorized local project directory, not a URL or filesystem root")
    try:
        return print(json.dumps(inventory(a.target, a.max_entries, a.max_bytes), ensure_ascii=True, indent=2))
    except OSError as exc:
        parser.exit(2, f"Local directory unavailable or path traverses a symlink: {exc.strerror}\n")


if __name__ == "__main__":
    main()
