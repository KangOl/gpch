#!/usr/bin/env python3
from collections import defaultdict
import json
import os
import subprocess
import sys


if sys.stdout.isatty():
    SEVERITY = {1: "\033[1;33mWARNING\033[0m", 2: "\033[0;31mERROR\033[0m"}
else:
    SEVERITY = {1: "WARNING", 2: "ERROR"}


def parse_diff(diff):
    files = defaultdict(list)
    last_file = None
    for line in diff.splitlines():
        if line.startswith("+++"):
            last_file = line[4:].partition("\t")[0]
        elif line.startswith("@@"):
            assert last_file
            if os.path.splitext(last_file)[1] != ".js":
                continue
            hunk = line[3:].partition("@@")[0].partition(" ")[2]
            l, _, c = hunk.partition(",")
            start = int(l)
            end = start + int(c) - 1
            files[last_file].append((start, end))

    return files


def main():
    # TODO take a "-p" option to strip path part. (actually hardcoded to "-p0")
    files = parse_diff(sys.stdin.read())
    if not files:
        return
    prefix = len(os.getcwd()) + 1

    eslint = subprocess.Popen(
        ["eslint", "--format", "json"] + list(files),
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    esout, _ = eslint.communicate()
    if eslint.returncode == 0:
        # Nice! No error.
        return

    rc = 0

    for file_ in json.loads(esout):
        path = file_["filePath"][prefix:]
        for error in file_["messages"]:
            line = int(error["line"])
            if any(line in range(*hunk) for hunk in files[path]):
                severity = SEVERITY.get(error["severity"], error["severity"])
                print(f"{severity} {path}:{line} {error['message']} [{error['ruleId']}]")
                rc = 1

    return rc


if __name__ == "__main__":
    sys.exit(main())
