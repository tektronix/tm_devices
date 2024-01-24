"""Set up an environment to use to contribute to this package.

This script will run through the commands listed in the CONTRIBUTING.md file.
"""
from __future__ import annotations

import argparse
import glob
import os
import platform
import shlex
import shutil
import subprocess
import sys

from pathlib import Path
from typing import Dict, List, Optional, Union

RUNNING_ON_LINUX = platform.system().upper() != "WINDOWS"


def parse_arguments() -> argparse.Namespace:
    """Parse the command line arguments.

    Returns:
        The parsed Namespace.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--reset",
        action="store_true",
        dest="reset",
        help="Specify if the virtual environment should be completely reset",
    )

    return parser.parse_args()


def running_in_virtualenv() -> bool:
    """Check if the current script is being executed in a virtual environment.

    Returns:
        Boolean indicating if the script is running in a virtualenv
    """
    return sys.prefix != sys.base_prefix


def create_virtual_environment(
    virtual_env_dir: Union[str, os.PathLike[str]], reset_env: bool
) -> None:
    """Create a virtual environment.

    Args:
        virtual_env_dir: The directory where the virtual environment should be created
        reset_env: Indicate if the virtual environment should be completely reset
    """
    virtual_env_dir = Path(virtual_env_dir)
    added_newline = False
    if (
        reset_env
        and virtual_env_dir.exists()
        and not sys.prefix.startswith(str(virtual_env_dir.resolve()))
        and not running_in_virtualenv()
    ):
        if not added_newline:
            added_newline = True
            print("")
        print(f"Removing virtualenv located at '{virtual_env_dir}'")
        shutil.rmtree(virtual_env_dir)
    if not virtual_env_dir.exists() and not running_in_virtualenv():
        if not added_newline:
            print("")
        print(f"Creating virtualenv located at '{virtual_env_dir}'")
        _run_cmd_in_subprocess(f"{sys.executable} -m venv {virtual_env_dir}")


def _run_cmd_in_subprocess(command: str, env_dict: Optional[Dict[str, str]] = None) -> None:
    """Run the given command in a subprocess.

    Args:
        command: The command string to send.
        env_dict: A mapping of environment variables to use in the subprocess.
    """
    command = command.replace("\\", "/")
    if RUNNING_ON_LINUX:
        command_to_send: Union[str, List[str]] = shlex.split(command)
    else:
        command_to_send = command
    print(f"\nExecuting command: {command}")
    subprocess.check_call(command_to_send, env=env_dict)  # noqa: S603


def main() -> None:
    """Set up the environment to allow development.

    Raises:
        SystemExit: Indicates that the setup failed for some reason.
    """
    starting_dir = os.getcwd()
    try:
        args = parse_arguments()
        if running_in_virtualenv():
            raise IndexError
        if not sys.version_info >= (3, 8):
            msg = (
                "Unable to set up the environment. "
                "Please use a Python version greater than or equal to 3.8."
            )
            raise SystemExit(msg)
        # Windows systems require the 64 bit python
        if platform.system().lower() == "windows" and sys.maxsize <= 2**32:
            msg = "Unable to set up the environment. Please use a 64-bit Python version."
            raise SystemExit(msg)
        # Create the virtual environment
        virtual_env_dir = os.path.sep.join([starting_dir, ".venv"])
        create_virtual_environment(virtual_env_dir, args.reset)
        os.environ["VIRTUAL_ENV"] = virtual_env_dir

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
            f"{python_executable} -m pre_commit install",
            f"{python_executable} -m tox -vve tests",
        )
        for command in commands_to_send:
            _run_cmd_in_subprocess(command)
    except IndexError:
        msg = (
            "Unable to set up the environment. Please run this script from a "
            "standard Python installation, not a virtual environment."
        )
        raise SystemExit(msg)  # noqa: TRY200,B904
    finally:
        os.chdir(starting_dir)


if __name__ == "__main__":
    main()
