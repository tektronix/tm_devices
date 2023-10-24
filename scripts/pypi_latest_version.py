"""Get the latest version from the index server."""
import argparse
import json

import requests

from poetry.core.constraints.version import Version


def parse_arguments() -> argparse.Namespace:
    """Parse the command line arguments.

    Returns:
        The parsed Namespace.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--package",
        required=True,
        action="store",
        dest="package",
        help="Provide the package to get the latest version for",
    )
    parser.add_argument(
        "--index",
        action="store",
        dest="index",
        choices=["pypi", "test.pypi"],
        default="pypi",
        help="Provide the index to query for the latest version, one of (pypi|test.pypi)",
    )

    return parser.parse_args()


def main() -> None:
    """Get the latest version of the provided package.

    Raises:
        SystemExit: Indicates there were no versions for the package.
    """
    args = parse_arguments()
    package = args.package
    index = args.index

    # This code mirrors code found in src/tm_devices/helpers/functions.py.
    # If this code is updated, the helper function should be updated too.
    url = f"https://{index}.org/pypi/{package}/json"
    try:
        response = requests.get(url, timeout=10)
        releases = json.loads(response.text)["releases"]
        version_list = sorted(releases, key=Version.parse, reverse=True)
        latest_version = version_list[0]
    except (IndexError, json.decoder.JSONDecodeError) as error:
        msg = f"There were no versions found for the {package} package."
        raise SystemExit(msg) from error

    print(latest_version)


if __name__ == "__main__":
    main()
