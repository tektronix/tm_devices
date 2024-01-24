"""This script modifies or gets the current project version in the pyproject.toml file."""
import argparse
import pathlib

import tomli
import tomli_w

from poetry.core.constraints.version import Version

PYPROJECT_FILE = pathlib.Path(f"{pathlib.Path(__file__).parent}/../pyproject.toml")


def parse_arguments() -> argparse.Namespace:
    """Parse the command line arguments.

    Returns:
        The parsed Namespace.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--set-version",
        required=False,
        type=Version.parse,
        action="store",
        dest="set_version",
        help="Provide the version to write to the pyproject.toml file",
    )

    return parser.parse_args()


def main() -> None:
    """Modify or get the project version."""
    args = parse_arguments()
    new_version: Version = args.set_version

    # Read in the current data
    with open(PYPROJECT_FILE, "rb") as file_handle:
        pyproject_data = tomli.load(file_handle)

    if new_version:
        # Modify the version value
        pyproject_data["tool"]["poetry"]["version"] = new_version.to_string()

        # Write back the data to the file
        with open(PYPROJECT_FILE, "wb") as file_handle:
            tomli_w.dump(pyproject_data, file_handle)
    else:
        print(pyproject_data["tool"]["poetry"]["version"])


if __name__ == "__main__":
    main()
