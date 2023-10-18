"""This script will check for unreleased entries in the CHANGELOG.md file.

It will exit with a non-zero exit code if there are no unreleased entries.
"""
import pathlib
import re

CHANGELOG_FILENAME = "CHANGELOG.md"


def main() -> None:
    """Check for entries in the Unreleased section of the CHANGELOG.md file.

    Raises:
        SystemExit: Indicates no new entries were found.
    """
    found_entries = False
    with open(
        pathlib.Path(__file__).parent.parent / CHANGELOG_FILENAME, encoding="utf-8"
    ) as changelog_file:
        tracking_unreleased = False
        tracking_entries = False
        for line in changelog_file:
            if line.startswith("___"):
                tracking_unreleased = False
                tracking_entries = False
            if line.startswith("## Unreleased"):
                tracking_unreleased = True
            if tracking_unreleased and line.startswith(
                (
                    "### Added\n",
                    "### Changed\n",
                    "### Deprecated\n",
                    "### Removed\n",
                    "### Fixed\n",
                    "### Security\n",
                )
            ):
                tracking_entries = True
            if tracking_entries:
                found_entries = bool(re.match(r"^- \w+", line))
            if found_entries:
                break

    if not found_entries:
        msg = f"No unreleased entries were found in {CHANGELOG_FILENAME}."
        raise SystemExit(msg)


if __name__ == "__main__":
    main()
