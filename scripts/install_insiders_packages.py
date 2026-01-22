"""Install insiders packages corresponding to currently installed versions of specified packages."""

import importlib.metadata
import logging
import os
import subprocess
import sys

import requests

from packaging.version import parse as parse_version

logging.basicConfig(
    level=getattr(logging, os.getenv("LOGGING_LEVEL", "INFO")),
    format="[%(asctime)s] [%(levelname)8s] %(message)s",
)
logger = logging.getLogger(__name__)

PACKAGE_LIST = {
    "mkdocstrings-python": "https://github.com/pawamoy-insiders/mkdocstrings-python",
    "griffe": "https://github.com/pawamoy-insiders/griffe",
}


def get_github_tags(repo_url_str: str, github_token: str) -> list[str]:
    """Get the tags for a GitHub repository.

    Args:
        repo_url_str: The URL of the GitHub repository.
        github_token: The GitHub token to use for authentication.

    Returns:
        A list of tag names for the repository.
    """
    # Extract the owner and repository name from the URL
    parts = repo_url_str.rstrip("/").split("/")
    owner, repo = parts[-2], parts[-1]

    try:
        response = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/tags",
            headers={"Authorization": f"token {github_token}"},
            timeout=30,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors

        tags = response.json()
        return [tag["name"] for tag in tags]

    except requests.exceptions.RequestException:
        logger.error("Error getting tags for %s", repo_url_str)  # noqa: TRY400
        return []


def get_newest_matching_tag(current_version: str, tags: list[str]) -> str:
    """Find the newest tag that starts with the given current version.

    Args:
        current_version: The current version of the package.
        tags: A list of tag names.

    Returns:
        The newest tag that starts with the current version, or an empty string if none are found.
    """
    # Filter tags that start with the current version
    matching_tags = [tag for tag in tags if tag.startswith(current_version)]

    # Sort matching tags as version numbers in descending order
    matching_tags.sort(key=parse_version, reverse=True)

    return matching_tags[0] if matching_tags else ""


def install_package(package_name: str, repo_url_str: str, tag: str, github_token: str) -> None:
    """Install a package from a GitHub repository using a specific tag.

    Args:
        package_name: The name of the package to install.
        repo_url_str: The HTTPS URL of the GitHub repository.
        tag: The tag to install.
        github_token: The GitHub token to use for authentication.
    """
    # Insert the token into the URL for authentication
    repo_url_str = repo_url_str.replace("https://", f"https://{github_token}@")

    install_url = f"{repo_url_str}.git@{tag}"
    try:
        logger.info("Installing %s from tag %s", package_name, tag)
        subprocess.check_call(  # noqa: S603
            [sys.executable, "-m", "pip", "install", f"git+{install_url}"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        logger.info("Successfully installed %s from tag %s", package_name, tag)
    except subprocess.CalledProcessError:
        logger.error("Failed to install %s from tag %s", package_name, tag)  # noqa: TRY400


def main() -> None:
    """Install insiders packages."""
    if not (github_token := os.environ.get("GITHUB_PAT")):
        logger.info(
            "GITHUB_PAT environment variable is not set, no insiders packages will be installed."
        )
        return
    for package, repo_url in PACKAGE_LIST.items():
        logger.info("Processing %s", package)
        try:
            version = importlib.metadata.version(package)
            logger.info("%s installed version is %s", package, version)
        except importlib.metadata.PackageNotFoundError:
            logger.warning("%s is not installed.", package)
            version = None

        if version and (package_tags := get_github_tags(repo_url, github_token)):
            logger.info("Tags for %s: %s", package, package_tags)

            if newest_tag := get_newest_matching_tag(version, package_tags):
                logger.info(
                    'Newest matching tag for %s version %s is "%s"',
                    package,
                    version,
                    newest_tag,
                )
                install_package(package, repo_url, newest_tag, github_token)
            else:
                logger.info("No matching tags found for %s with version %s", package, version)


if __name__ == "__main__":
    main()
