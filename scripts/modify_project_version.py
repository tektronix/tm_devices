"""This script modifies the current project version in the pyproject.toml file."""
import argparse
import os.path
import pathlib

import tomli
import tomli_w

from poetry.core.constraints.version import Version

PYPROJECT_FILE = pathlib.Path(f"{os.path.dirname(__file__)}/../pyproject.toml")


def parse_arguments() -> argparse.Namespace:
    """Parse the command line arguments.

    Returns:
        The parsed Namespace.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version",
        required=True,
        type=Version.parse,
        action="store",
        dest="version",
        help="Provide the version to write to the pyproject.toml file",
    )

    return parser.parse_args()


def main() -> None:
    """Modify the project version."""
    args = parse_arguments()
    new_version: Version = args.version

    # Read in the current data
    with open(PYPROJECT_FILE, "rb") as file_handle:
        pyproject_data = tomli.load(file_handle)

    # Modify the version value
    pyproject_data["tool"]["poetry"]["version"] = new_version.to_string()

    # Write back the data to the file
    with open(PYPROJECT_FILE, "wb") as file_handle:
        tomli_w.dump(pyproject_data, file_handle)


if __name__ == "__main__":
    main()
