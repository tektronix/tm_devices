"""Pytest configuration file."""

import logging
import os
import socket
import sys

from pathlib import Path
from typing import Generator, List, Tuple
from unittest import mock

import pytest
import pyvisa.constants

from mock_server import mocker_server, PORT
from tm_devices import configure_logging, DeviceManager, LoggingLevels
from tm_devices.components import DMConfigParser
from tm_devices.helpers import DMConfigOptions, validate_address

os.environ["TM_DEVICES_UNIT_TESTS_RUNNING"] = "true"
# Make sure to not use any local config files
os.environ[DMConfigParser.CONFIG_FILE_PATH_ENV_VARIABLE] = ""

PROJECT_ROOT_DIR = Path(__file__).parent.parent
SIMULATED_VISA_LIB = str(Path(__file__).parent / "sim_devices/devices.yaml@sim")
UNIT_TEST_TIMEOUT = 50


####################################################################################################
# Configure the logging for the package that will run during unit tests
class _DynamicStreamHandler(logging.StreamHandler):  # pyright: ignore[reportMissingTypeArgument]
    def emit(self, record: logging.LogRecord) -> None:
        self.stream = sys.stdout
        super().emit(record)


_logger = configure_logging(
    console_logging_level=LoggingLevels.NONE,
    file_logging_level=LoggingLevels.DEBUG,
    log_file_name="unit_test.log",
    log_file_directory=Path(__file__).parent / "logs",
)
_unit_test_console_handler = _DynamicStreamHandler(stream=sys.stdout)
_unit_test_console_handler.setLevel(logging.DEBUG)
_unit_test_console_formatter = logging.Formatter("%(asctime)s - %(message)s")
_unit_test_console_formatter.default_msec_format = (
    "%s.%06d"  # Use 6 digits of precision for milliseconds
)
_unit_test_console_handler.setFormatter(_unit_test_console_formatter)
_logger.addHandler(_unit_test_console_handler)
####################################################################################################


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
    print(f"\n{'#' * 90}\nExecuting {os.environ['PYTEST_CURRENT_TEST'].split(' ')[0]}\n")  # noqa: T201
    yield
    print(f"\n\nFinished {os.environ['PYTEST_CURRENT_TEST'].split(' ')[0]}\n{'#' * 90}")  # noqa: T201


@pytest.fixture(name="device_manager", scope="session")
def fixture_device_manager() -> Generator[DeviceManager, None, None]:
    """Create and yield a DeviceManager instance.

    Yields:
        The DeviceManager instance.
    """
    print()  # noqa: T201
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
    ), DeviceManager(
        verbose=True, config_options=DMConfigOptions(default_visa_timeout=UNIT_TEST_TIMEOUT)
    ) as dev_manager:
        dev_manager.visa_library = SIMULATED_VISA_LIB
        yield dev_manager


@pytest.fixture(name="unit_test_config_file", scope="session")
def fixture_unit_test_config_file(
    tmpdir_factory: pytest.TempdirFactory, device_manager: DeviceManager
) -> Path:
    """Save the unit test configuration file.

    Args:
        tmpdir_factory: The temporary directory path.
        device_manager: The device manager fixture.
    """
    config_file = tmpdir_factory.mktemp("tests") / "unit_test_config.yaml"
    device_manager.write_current_configuration_to_config_file(config_file)
    return Path(config_file)


@pytest.fixture(autouse=True)
def _reset_dm(  # pyright: ignore[reportUnusedFunction]
    device_manager: DeviceManager, unit_test_config_file: Path
) -> Generator[None, None, None]:
    """Reset the device_manager settings after each test.

    Args:
        device_manager: The device manager fixture.
        unit_test_config_file: The unit test configuration file.
    """
    saved_setup_enable = device_manager.setup_cleanup_enabled
    saved_teardown_enable = device_manager.teardown_cleanup_enabled
    yield
    device_manager.setup_cleanup_enabled = saved_setup_enable
    device_manager.teardown_cleanup_enabled = saved_teardown_enable
    device_manager.load_config_file(unit_test_config_file)


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
