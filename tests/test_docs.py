"""Test for the documentation."""

import os
import shlex
import subprocess
import sys
import time

from importlib.util import find_spec
from pathlib import Path
from typing import Generator

import pytest

from conftest import PROJECT_ROOT_DIR


@pytest.fixture(name="docs_server")
def fixture_docs_server(site_dir: str) -> Generator[str, None, None]:
    """Serve the documentation site."""
    port = f"8{sys.version_info.major}{sys.version_info.minor}"
    cmd = [sys.executable, "-m", "http.server", port, "--directory", site_dir]
    with subprocess.Popen(  # noqa: S603
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ) as server_process:
        time.sleep(1)  # wait for server to start

        yield f"http://127.0.0.1:{port}/"

        server_process.terminate()  # stop the server
        try:
            server_process.wait(timeout=10)  # Wait up to 10 seconds for the server to terminate
        except subprocess.TimeoutExpired:
            server_process.kill()  # Force kill if it doesn't terminate in time


@pytest.fixture(name="site_dir", scope="session")
def fixture_site_dir(pytestconfig: pytest.Config) -> str:
    """Create the site directory path for testing."""
    site_path = (
        Path(__file__).parent.parent / f".site_{sys.version_info.major}{sys.version_info.minor}/"
    ).resolve()
    if xml_path := pytestconfig.getoption("xmlpath"):
        site_path = (Path(xml_path).parent / ".site_html/").resolve()  # pyright: ignore[reportArgumentType]
    site_path.mkdir(parents=True, exist_ok=True)
    return site_path.as_posix()


@pytest.fixture(scope="module", autouse=True)
def _docs_tests_setup() -> Generator[None, None, None]:  # pyright: ignore [reportUnusedFunction]
    """Setup for docs tests.."""
    starting_directory = os.getcwd()
    try:
        os.chdir(PROJECT_ROOT_DIR)
        yield
    finally:
        os.chdir(starting_directory)


@pytest.mark.docs
@pytest.mark.slow
@pytest.mark.skipif(find_spec("mkdocs") is None, reason="The mkdocs package is not installed.")
class TestDocs:  # pylint: disable=no-self-use
    """A collection of documentation tests."""

    @pytest.mark.order(1)
    def test_docs_html(self, site_dir: str) -> None:
        """Test creating html documentation."""
        subprocess.check_call(shlex.split(f"mkdocs build --verbose --site-dir={site_dir}"))  # noqa: S603

    @pytest.mark.order(2)
    @pytest.mark.depends(on=["test_docs_html"])
    def test_docs_linkcheck(self, docs_server: str) -> None:
        """Run the linkcheck test for the documentation."""
        subprocess.check_call(  # noqa: S603
            shlex.split(f"linkchecker --config=docs/.linkchecker.ini {docs_server}")
        )
