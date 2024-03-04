"""Create a post-release version for test.pypi.org."""

import argparse

from poetry.core.constraints.version import Version


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
        help="Provide the current, latest version of the package",
    )

    return parser.parse_args()


def main() -> None:
    """Create and print a post-release version string for test.pypi.org."""
    args = parse_arguments()
    version: Version = args.version

    new_post_release_num = 1
    if version.post:
        new_post_release_num += version.post.number

    print(f"{'.'.join(str(x) for x in version.parts)}.post{new_post_release_num}")


if __name__ == "__main__":
    main()
