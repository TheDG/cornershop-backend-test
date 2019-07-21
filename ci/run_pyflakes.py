"""Python script that runs Pyflakes on all files."""

import subprocess
import sys

from utils import collect_sources


def ignore(path):
    """ Ignore hidden and test files """
    parts = path.splitall()
    if any(x.startswith(".") for x in parts):
        return True
    if 'test' in parts:
        return True
    return False


def run_pyflakes():
    """ Command to run Pyflke on all collected files """
    cmd = ["pyflakes"]
    cmd.extend(collect_sources(ignore_func=ignore))
    return subprocess.call(cmd)


if __name__ == "__main__":
    sys.exit(run_pyflakes())
