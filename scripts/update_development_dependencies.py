"""Update the development dependencies.

This script will update the development dependencies that are pinned in the pyproject.toml and .pre-
commit-config.yaml files.
"""

import argparse
import contextlib
import shlex
import subprocess
import sys
import warnings

from pathlib import Path
from typing import List

from yamlfix import fix_files  # pyright: ignore[reportUnknownVariableType]

from pypi_latest_version import get_latest_version

DEPENDENCIES_TO_UPDATE = {
    "dev": (
        "docformatter[tomli]",
        "pylint",
        "pyright",
        "ruff",
    ),
    "tests": ("ruff",),
}


def parse_arguments() -> argparse.Namespace:
    """Parse the command line arguments.

    Returns:
        The parsed Namespace.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--no-install",
        action="store_true",
        dest="no_install",
        help="Indicate if packages should not be installed via poetry (Primarily used in CI).",
    )

    return parser.parse_args()


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
    python_script_location = Path(python_executable).parent
    repository_root_directory = script_location.parent.parent

    args = parse_arguments()
    lock_only = args.no_install

    # Remove the dependencies from poetry to avoid issues if they are in multiple groups
    for group, dependencies_list in DEPENDENCIES_TO_UPDATE.items():
        dependencies = " ".join(f'"{x.split("[", maxsplit=1)[0]}"' for x in dependencies_list)
        _run_cmd_in_subprocess(
            f'"{python_executable}" -m poetry remove --lock --group={group} {dependencies}'
        )

    # Get the latest versions for each of the dependencies to update
    for group, dependencies_list in DEPENDENCIES_TO_UPDATE.items():
        latest_dependency_versions: List[str] = []
        for dependency in dependencies_list:
            latest_dep_version = get_latest_version(dependency.split("[", maxsplit=1)[0], "pypi")
            latest_dependency_versions.append(dependency + f"=={latest_dep_version}")

        # Update dependencies in pyproject.toml using poetry
        dependencies = " ".join(f'"{x}"' for x in latest_dependency_versions)
        poetry_add_cmd = f'"{python_executable}" -m poetry add --group={group} {dependencies}'
        if lock_only:
            poetry_add_cmd += " --lock"
        _run_cmd_in_subprocess(poetry_add_cmd)

    # Run poetry update
    poetry_update_cmd = f'"{python_executable}" -m poetry update'
    if lock_only:
        poetry_update_cmd += " --lock"
    _run_cmd_in_subprocess(poetry_update_cmd)

    # Update pre-commit config file
    _run_cmd_in_subprocess(f'"{python_script_location}/pre-commit-update"')

    # Fix the formatting of the pre-commit config file
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        fix_files([f"{repository_root_directory}/.pre-commit-config.yaml"])

    # Fix the formatting of the pyproject.toml file
    _run_cmd_in_subprocess(
        f'"{python_script_location}/toml-sort" "{repository_root_directory}/pyproject.toml"'
    )

    # Update the docs and tests dependency files
    for group in ("docs", "tests"):
        _run_cmd_in_subprocess(
            f'"{python_executable}" -m poetry export --only {group} '
            f"--without-hashes --output {group}/requirements.txt"
        )
    # Sort the requirements files (ignore failures due to changed files
    with contextlib.suppress(subprocess.CalledProcessError):
        _run_cmd_in_subprocess(
            f'"{python_executable}" -m pre_commit run --all requirements-txt-fixer'
        )


if __name__ == "__main__":
    main()
