"""Set up an environment to use to contribute to this package.

This script will run through the commands listed in the CONTRIBUTING.md file.
"""

from __future__ import annotations

import glob
import os
import platform
import shlex
import subprocess
import sys

from pathlib import Path

RUNNING_ON_LINUX = platform.system().upper() != "WINDOWS"
RUNNING_IN_VIRTUALENV = sys.prefix != sys.base_prefix


def create_virtual_environment(virtual_env_dir: str | os.PathLike[str]) -> None:
    """Create a virtual environment.

    Args:
        virtual_env_dir: The directory where the virtual environment should be created
    """
    print(f"\nCreating virtualenv located at '{virtual_env_dir}'")
    _run_cmd_in_subprocess(f"{sys.executable} -m venv {virtual_env_dir} --clear")


def _run_cmd_in_subprocess(command: str) -> None:
    """Run the given command in a subprocess.

    Args:
        command: The command string to send.
    """
    command = command.replace("\\", "/")
    print(f"\nExecuting command: {command}")
    subprocess.check_call(shlex.split(command))  # noqa: S603


def main() -> None:
    """Set up the environment to allow development.

    Raises:
        SystemExit: Indicates that the setup failed for some reason.
    """
    starting_dir = Path.cwd()
    try:
        if RUNNING_IN_VIRTUALENV:
            raise IndexError
        # This requires contributors to use newer versions of Python even
        # though the package supports older versions.
        if sys.version_info < (3, 9):
            msg = (
                "Unable to set up the environment. "
                "Please use a Python version greater than 3.8 for "
                "local development on this package."
            )
            raise SystemExit(msg)
        # Windows systems require the 64 bit python
        if platform.system().lower() == "windows" and sys.maxsize <= 2**32:
            msg = "Unable to set up the environment. Please use a 64-bit Python version."
            raise SystemExit(msg)
        # Create the virtual environment
        virtual_env_dir = starting_dir / ".venv"
        create_virtual_environment(virtual_env_dir)
        os.environ["VIRTUAL_ENV"] = virtual_env_dir.as_posix()

        # Delete the previous poetry lock file
        lock_file = Path(starting_dir) / "poetry.lock"
        if lock_file.exists():
            lock_file.unlink()

        # Find the python executable from the new virtual environment
        files = list(
            filter(
                lambda x: "site-packages" not in x and "pythonw" not in x,
                glob.iglob(
                    f"{virtual_env_dir}/{'bin' if RUNNING_ON_LINUX else 'Scripts'}/**/python*",
                    recursive=True,
                ),
            )
        )
        python_executable = files[0]
        commands_to_send = (
            f"{python_executable} -m pip install -U pip wheel poetry",
            f"{python_executable} -m poetry install",
            f"{python_executable} -m nodeenv --python-virtualenv --clean-src",
            f"{python_executable} -m pre_commit install --install-hooks",
            f"{python_executable} -m tox -e tests",
        )
        for command in commands_to_send:
            _run_cmd_in_subprocess(command)
    except IndexError:
        msg = (
            "Unable to set up the environment. Please run this script from a "
            "standard Python installation, not a virtual environment."
        )
        raise SystemExit(msg)  # noqa: B904
    finally:
        os.chdir(starting_dir)


if __name__ == "__main__":
    main()
