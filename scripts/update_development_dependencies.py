"""Update the development dependencies.

This script will update the development dependencies that are pinned in the pyproject.toml and .pre-
commit-config.yaml files.
"""
import shlex
import subprocess
import sys
import warnings

from pathlib import Path
from typing import List

from yamlfix import fix_files  # pyright: ignore[reportUnknownVariableType]

from pypi_latest_version import get_latest_version

# NOTE: When docformatter is uncommented from this list, be sure to
# remove the 'keep' key from the '[tool.pre-commit-update]' section in ``pyproject.toml``.
DEPENDENCIES_TO_UPDATE = (
    # FUTURE # "docformatter[tomli]",  # can't update due to https://github.com/PyCQA/docformatter/issues/174
    "pylint[spelling]",
    "pyright",
    "ruff",
)


def _run_cmd_in_subprocess(command: str) -> None:
    """Run the given command in a subprocess.

    Args:
        command: The command string to send.
    """
    command = command.replace("\\", "/")
    print(f"\nExecuting command: {command}")
    subprocess.check_call(shlex.split(command))  # noqa: S603


def main() -> None:
    """Run the script to update the development dependencies."""
    script_location = Path(__file__)
    python_executable = sys.executable
    latest_dependency_versions: List[str] = []

    # Get the latest versions for each of the dependencies to update
    for dependency in DEPENDENCIES_TO_UPDATE:
        latest_dep_version = get_latest_version(dependency.split("[", maxsplit=1)[0], "pypi")
        latest_dependency_versions.append(dependency + f"=={latest_dep_version}")

    # Update dependencies in pyproject.toml using poetry
    dependencies = " ".join(f'"{x}"' for x in latest_dependency_versions)
    _run_cmd_in_subprocess(f"{python_executable} -m poetry add --group=dev {dependencies}")

    # Run poetry update
    _run_cmd_in_subprocess(f"{python_executable} -m poetry update")

    # Update pre-commit config file
    _run_cmd_in_subprocess(python_executable.rsplit("python", maxsplit=1)[-0] + "pre-commit-update")

    # Fix the formatting of the pre-commit config file
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        fix_files([f"{script_location.parent.parent}/.pre-commit-config.yaml"])


if __name__ == "__main__":
    main()
