"""This script will check for unreleased entries in the CHANGELOG.md file.

It will exit with a non-zero exit code if there are no unreleased entries.

It will also copy the necessary files into the template directory to properly render the CHANGELOG
and Release Notes.
"""

import pathlib
import re
import shutil

CHANGELOG_FILEPATH = pathlib.Path(__file__).parent.parent / "CHANGELOG.md"
TEMPLATE_CHANGELOG_FILEPATH = (
    pathlib.Path(__file__).parent.parent
    / "python_semantic_release_templates"
    / ".previous_changelog_for_template.md"
)
TEMPLATE_RELEASE_NOTES_FILEPATH = (
    pathlib.Path(__file__).parent.parent
    / "python_semantic_release_templates"
    / ".previous_release_notes_for_template.md"
)


def main() -> None:
    """Check for entries in the Unreleased section of the CHANGELOG.md file.

    Raises:
        SystemExit: Indicates no new entries were found.
    """
    release_notes_content = ""
    found_entries = False
    with CHANGELOG_FILEPATH.open(mode="r", encoding="utf-8") as changelog_file:
        tracking_unreleased = False
        tracking_entries = False
        for line in changelog_file:
            if line.startswith("___"):
                tracking_unreleased = False
                tracking_entries = False
            if tracking_unreleased:
                release_notes_content += line
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
            if tracking_entries and not found_entries:
                found_entries = bool(re.match(r"^- \w+", line))

    if not found_entries:
        msg = f"No unreleased entries were found in {CHANGELOG_FILEPATH}."
        raise SystemExit(msg)

    # Copy the files to the correct location
    shutil.copy(CHANGELOG_FILEPATH, TEMPLATE_CHANGELOG_FILEPATH)
    with TEMPLATE_RELEASE_NOTES_FILEPATH.open("w", encoding="utf-8") as template_release_notes:
        template_release_notes.write(release_notes_content.strip() + "\n")


if __name__ == "__main__":
    main()
