"""Test for the documentation."""
import os
import shlex
import shutil
import subprocess
import sys

from importlib.util import find_spec
from typing import Generator

import pytest

from conftest import PROJECT_ROOT_DIR


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


@pytest.mark.docs
@pytest.mark.slow
@pytest.mark.skipif(find_spec("sphinx") is None, reason="The sphinx module is not installed.")
class TestDocs:  # pylint: disable=no-self-use
    """A collection of documentation tests."""

    @pytest.mark.order(1)
    def test_docs_html(self) -> None:
        """Test creating html documentation."""
        subprocess.check_call(shlex.split("make html"))  # noqa: S603

    @pytest.mark.order(2)
    def test_docs_linkcheck(self) -> None:
        """Run the linkcheck test for the documentation."""
        subprocess.check_call(shlex.split("make linkcheck"))  # noqa: S603

    @pytest.mark.order(3)
    def test_docs_coverage(self) -> None:
        """Run the coverage test for the documentation."""
        subprocess.check_call(shlex.split("make coverage"))  # noqa: S603

    @pytest.mark.order(4)
    def test_docs_doctest(self) -> None:
        """Run the doctest test for the documentation."""
        subprocess.check_call(shlex.split("make doctest"))  # noqa: S603
