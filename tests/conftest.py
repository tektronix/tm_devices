"""Pytest configuration file."""
import os
import socket

from pathlib import Path
from typing import Generator, List, Tuple
from unittest import mock

import pytest
import pyvisa.constants

from mock_server import mocker_server, PORT
from tm_devices import DeviceManager
from tm_devices.components import DMConfigParser
from tm_devices.helpers import validate_address

os.environ["TM_DEVICES_UNIT_TESTS_RUNNING"] = "true"
# Make sure to not use any local config files
os.environ[DMConfigParser.CONFIG_FILE_PATH_ENV_VARIABLE] = ""

PROJECT_ROOT_DIR = Path(__file__).parent.parent
SIMULATED_VISA_LIB = str(Path(__file__).parent / "sim_devices/devices.yaml@sim")


def mock_gethostbyname(address: str) -> str:
    """Mock the socket.gethostbyname function."""
    try:
        is_hostname = validate_address(address)
        if not is_hostname:  # pylint: disable=consider-using-assignment-expr
            return address
        raise ValueError
    except ValueError as error:
        raise socket.herror from error


def mock_gethostbyaddr(address: str) -> Tuple[str, List[str], List[str]]:
    """Mock the socket.gethostbyaddr function."""
    try:
        is_hostname = validate_address(address)
        if is_hostname:  # pylint: disable=consider-using-assignment-expr
            return address, [], []
        raise ValueError
    except ValueError as error:
        raise socket.herror from error


@pytest.fixture(autouse=True, scope="session")
def bypass_time_sleep() -> Generator[mock.MagicMock, None, None]:
    """Bypass the `time.sleep()` method during unit tests."""
    with mock.patch("time.sleep", mock.MagicMock(return_value=None)) as _fixture:
        yield _fixture


@pytest.fixture(autouse=True)
def _auto_add_newline_to_test_start() -> (  # pyright: ignore [reportUnusedFunction]
    Generator[None, None, None]
):
    """Automatically add a newline at the start of each test."""
    print(f"\n{'#' * 90}\nExecuting {os.environ['PYTEST_CURRENT_TEST'].split(' ')[0]}\n")
    yield
    print(f"\n\nFinished {os.environ['PYTEST_CURRENT_TEST'].split(' ')[0]}\n{'#' * 90}")


@pytest.fixture(name="device_manager", scope="session")
def fixture_device_manager() -> Generator[DeviceManager, None, None]:
    """Create and yield a DeviceManager instance.

    Yields:
        The DeviceManager instance.
    """
    print("")
    with mock.patch(
        "socket.gethostbyname", mock.MagicMock(side_effect=mock_gethostbyname)
    ), mock.patch(
        "socket.gethostbyaddr",
        mock.MagicMock(side_effect=mock_gethostbyaddr),
    ), mock.patch(
        "pyvisa.resources.messagebased.MessageBasedResource.read_stb",
        mock.MagicMock(return_value=0),
    ), mock.patch(
        "pyvisa.resources.messagebased.MessageBasedResource.clear",
        mock.MagicMock(return_value=pyvisa.constants.StatusCode.success),
    ), DeviceManager(verbose=True) as dev_manager:
        dev_manager.visa_library = SIMULATED_VISA_LIB
        yield dev_manager


@pytest.fixture(name="mock_http_server", scope="session")
def _fixture_mock_http_server() -> (  # pyright: ignore [reportUnusedFunction]
    Generator[None, None, None]
):
    """Create a mock HTTP server.

    Yields:
        The HTTP server instance.
    """
    with mocker_server.run("127.0.0.1", PORT):  # pyright: ignore[reportUnknownMemberType]
        yield
