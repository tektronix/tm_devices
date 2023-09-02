"""Test for the documentation."""
import os
import shlex
import shutil
import sys

from importlib.util import find_spec
from typing import Generator, List

import pytest

from sphinx.cmd.build import build_main

import tm_devices

from conftest import PROJECT_ROOT_DIR


def create_sphinx_build_cmd(build_type: str) -> List[str]:
    """Create the sphinx-build command to send via subprocess.

    Args:
        build_type: The type of sphinx build to perform.

    Returns:
        The sphinx build command.
    """
    os.environ["SPHINXPROJ"] = tm_devices.__name__
    source_dir = "."
    build_dir = "_build"
    num_processors = os.getenv("SPHINX_PROC_COUNT", "auto")
    return shlex.split(
        f'-b {build_type} "{source_dir}" "{build_dir}" -W --keep-going -j {num_processors}'
    )


@pytest.fixture(scope="module", autouse=True)
def _use_docs_directory() -> Generator[None, None, None]:  # pyright: ignore [reportUnusedFunction]
    """Use a custom docs directory for these tests."""
    os.chdir(PROJECT_ROOT_DIR)
    build_dir = f".docs_{sys.version_info.major}{sys.version_info.minor}"
    starting_directory = os.getcwd()
    shutil.rmtree(build_dir, ignore_errors=True)
    shutil.copytree("docs", build_dir, ignore=shutil.ignore_patterns("_*"))
    shutil.copytree("docs/_static", build_dir + "/_static")
    shutil.copytree("docs/_templates", build_dir + "/_templates")
    try:
        os.chdir(build_dir)
        yield
    finally:
        os.chdir(starting_directory)


# TODO: make these tests always skip unless called with a specific marker
@pytest.mark.docs
@pytest.mark.slow
@pytest.mark.skipif(find_spec("sphinx") is None, reason="The sphinx module is not installed.")
class TestDocs:  # pylint: disable=no-self-use
    """A collection of documentation tests."""

    @pytest.mark.order(1)
    def test_docs_html(self) -> None:
        """Test creating html documentation."""
        build_main(create_sphinx_build_cmd("html"))

    @pytest.mark.xfail(reason="tm_devices GitHub links don't work currently")
    @pytest.mark.order(2)
    def test_docs_linkcheck(self) -> None:
        """Run the linkcheck test for the documentation."""
        build_main(create_sphinx_build_cmd("linkcheck"))

    @pytest.mark.order(3)
    def test_docs_coverage(self) -> None:
        """Run the coverage test for the documentation."""
        build_main(create_sphinx_build_cmd("coverage"))

    @pytest.mark.order(4)
    def test_docs_doctest(self) -> None:
        """Run the doctest test for the documentation."""
        build_main(create_sphinx_build_cmd("doctest"))
