"""Run pylint, single-process on Python 3.15+.

pylint pickles the linter with dill when ``jobs`` is 0 or greater than 1.
dill 0.4.1, still the newest release, reads ``code.co_lnotab``, which Python
3.15 removed. Until a newer dill is released, parallel pylint cannot run there.

TODO: Delete this script and restore the pre-commit pylint hook ``entry`` to
``pylint`` once a dill release newer than 0.4.1 is available.
"""

from __future__ import annotations

import sys

from pylint.lint import Run


def main() -> None:
    """Invoke pylint, forcing one job on Python 3.15 and newer."""
    args = list(sys.argv[1:])
    if sys.version_info >= (3, 15) and not any(
        arg == "--jobs" or arg.startswith("--jobs=") for arg in args
    ):
        args = ["--jobs=1", *args]
    Run(args)


if __name__ == "__main__":
    main()
