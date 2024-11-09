"""Tests for the logging functionality."""

import contextlib
import logging

from typing import Generator, TYPE_CHECKING

import pytest

from tm_devices import DeviceManager, PACKAGE_NAME

if TYPE_CHECKING:
    from tm_devices.drivers import MSO2


@pytest.fixture(name="remove_log_file_handler")
def _remove_log_file_handler(device_manager: DeviceManager) -> Generator[None, None, None]:  # pyright: ignore[reportUnusedFunction]
    """Remove the file handler from the logger."""
    device_manager.remove_all_devices()
    logger = logging.getLogger(PACKAGE_NAME)
    file_handler = None
    with contextlib.suppress(StopIteration):
        file_handler = next(
            handler for handler in logger.handlers if isinstance(handler, logging.FileHandler)
        )
        logger.removeHandler(file_handler)
    yield
    if file_handler is not None:
        logger.addHandler(file_handler)
    device_manager.remove_all_devices()


def test_visa_command_logging_edge_cases(
    device_manager: DeviceManager,
    remove_log_file_handler: None,  # noqa: ARG001
) -> None:
    """Test VISA command logging edge cases."""
    scope: MSO2 = device_manager.add_scope("MSO22-HOSTNAME")
    assert scope.model == "MSO22"
