"""Tests for the logging functionality."""

import contextlib
import logging
import shutil
import sys
import time

from collections.abc import Generator
from pathlib import Path
from typing import TYPE_CHECKING

import colorlog
import pytest
import pyvisa

import tm_devices

from tm_devices import configure_logging, DeviceManager, LoggingLevels, PACKAGE_NAME
from tm_devices.helpers import logging as tm_devices_logging

if TYPE_CHECKING:
    from tm_devices.drivers import MSO2


@pytest.fixture(name="remove_log_file_handler")
def _remove_log_file_handler() -> Generator[None, None, None]:  # pyright: ignore[reportUnusedFunction]
    """Remove the file handler from the logger."""
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


def test_visa_command_logging_edge_cases(
    device_manager: DeviceManager,
    remove_log_file_handler: None,  # noqa: ARG001
) -> None:
    """Test VISA command logging edge cases."""
    scope: MSO2 = device_manager.add_scope("MSO22-HOSTNAME")
    assert scope.model == "MSO22"


def test_logging_singleton() -> None:
    """Verify the singleton behavior of the logging configuration function."""
    package_logger = logging.getLogger(PACKAGE_NAME)
    logger_handlers_copy = package_logger.handlers.copy()
    assert len(logger_handlers_copy) == 3
    logger = configure_logging()
    assert len(logger.handlers) == 3
    assert logger.handlers == logger_handlers_copy


@pytest.fixture(name="reset_package_logger")
def _reset_package_logger() -> Generator[None, None, None]:  # pyright: ignore[reportUnusedFunction]
    """Reset the package logger."""
    logger = logging.getLogger(PACKAGE_NAME)
    handlers_copy = logger.handlers.copy()
    pyvisa_handlers_copy = pyvisa.logger.handlers.copy()
    for handler in handlers_copy:
        logger.removeHandler(handler)
    for handler in pyvisa_handlers_copy:
        pyvisa.logger.removeHandler(handler)
    tm_devices_logging._logger_initialized = False  # noqa: SLF001  # pyright: ignore[reportPrivateUsage]
    tm_devices_logging._configured_logger_name = PACKAGE_NAME  # noqa: SLF001  # pyright: ignore[reportPrivateUsage]
    tm_devices_logging._log_response_max_characters = None  # noqa: SLF001  # pyright: ignore[reportPrivateUsage]
    temp_excepthook = sys.excepthook
    yield
    tm_devices_logging._log_response_max_characters = None  # noqa: SLF001  # pyright: ignore[reportPrivateUsage]
    # Reset the handlers back to what they were
    for handler in logger.handlers.copy():
        logger.removeHandler(handler)
    for handler in handlers_copy:
        logger.addHandler(handler)
    for handler in pyvisa.logger.handlers.copy():
        pyvisa.logger.removeHandler(handler)
    for handler in pyvisa_handlers_copy:
        pyvisa.logger.addHandler(handler)
    sys.excepthook = temp_excepthook


def test_configure_logger_with_base_logger(reset_package_logger: None) -> None:  # noqa: ARG001
    """Test configuring the package logger as a child of an existing logger."""
    base_logger = logging.getLogger("custom_application")
    logger = configure_logging(
        log_console_level=LoggingLevels.NONE,
        log_file_level=LoggingLevels.NONE,
        logger=base_logger,
    )
    assert logger is base_logger.getChild(PACKAGE_NAME)
    assert logger.name == f"custom_application.{PACKAGE_NAME}"
    assert configure_logging() is logger


def test_configure_logger_full(reset_package_logger: None) -> None:  # noqa: ARG001
    """Test the configuration function with all types of logs."""
    log_dir = (
        Path(__file__).parent / f"generated_logs_py{sys.version_info.major}{sys.version_info.minor}"
    )
    log_name = "custom_log.log"
    shutil.rmtree(log_dir, ignore_errors=True)

    time.sleep(1)  # wait to ensure previous tests have disconnected from all devices

    assert not any(isinstance(handler, logging.FileHandler) for handler in pyvisa.logger.handlers)
    assert len(logging.getLogger(PACKAGE_NAME).handlers) == 0  # pylint: disable=use-implicit-booleaness-not-comparison-to-zero
    sys.excepthook = sys.__excepthook__
    logger = configure_logging(
        log_console_level="DEBUG",
        log_file_level="DEBUG",
        log_file_directory=log_dir,
        log_file_name=log_name,
        log_colored_output=False,
        log_pyvisa_messages=True,
        log_uncaught_exceptions=False,
    )
    assert len(logger.handlers) == 3
    assert any(isinstance(handler, logging.FileHandler) for handler in pyvisa.logger.handlers)
    log_contents = (log_dir / log_name).read_text().split("\n")
    assert len(log_contents) == 3
    assert f"] [{PACKAGE_NAME}] [   DEBUG] timezone==" in log_contents[0]
    assert log_contents[1].endswith(
        f"] [{PACKAGE_NAME}] [   DEBUG] {PACKAGE_NAME}=={tm_devices.__version__}"
    )
    assert [type(x) for x in logger.handlers] == [
        logging.NullHandler,
        logging.FileHandler,
        logging.StreamHandler,
    ]
    assert sys.excepthook == sys.__excepthook__  # pylint: disable=comparison-with-callable


def test_configure_logger_no_file(reset_package_logger: None) -> None:  # noqa: ARG001
    """Test the configuration function with no file logging."""
    assert len(logging.getLogger(PACKAGE_NAME).handlers) == 0  # pylint: disable=use-implicit-booleaness-not-comparison-to-zero
    logger = configure_logging(
        log_console_level="DEBUG",
        log_file_level=LoggingLevels.NONE,
        log_colored_output=True,
        log_pyvisa_messages=False,
    )
    assert len(logger.handlers) == 2
    assert [type(x) for x in logger.handlers] == [logging.NullHandler, colorlog.StreamHandler]
    assert isinstance(logger.handlers[1].formatter, colorlog.ColoredFormatter)


@pytest.mark.parametrize(
    ("response", "max_characters", "expected"),
    [
        # No limit (argument and global both None) logs the full repr
        (b"hello world", None, "b'hello world'"),
        # A limit longer than the repr does not truncate
        ("hi", 100, "'hi'"),
        # A limit shorter than the repr truncates and appends the marker
        (b"hello world", 5, "b'hel" + tm_devices_logging.RESPONSE_LOG_TRUNCATION_MARKER),
        # A limit of zero suppresses the response contents entirely
        (b"hello world", 0, tm_devices_logging.RESPONSE_LOG_TRUNCATION_MARKER),
    ],
)
def test_truncate_response_for_logging(
    response: object, max_characters: int | None, expected: str
) -> None:
    """Test the truncation of command responses for logging.

    Args:
        response: The response to format for logging.
        max_characters: The maximum number of characters to keep.
        expected: The expected formatted string.
    """
    assert tm_devices_logging.truncate_response_for_logging(response, max_characters) == expected


def test_configure_logging_response_max_characters(reset_package_logger: None) -> None:  # noqa: ARG001
    """Test that the log_response_max_characters config option is stored and used globally."""
    # Truncation is disabled by default
    assert tm_devices_logging.get_log_response_max_characters() is None
    configure_logging(
        log_console_level=LoggingLevels.NONE,
        log_file_level=LoggingLevels.NONE,
        log_response_max_characters=4,
    )
    # The configured value is retrievable and applied when no per-call length is given
    assert tm_devices_logging.get_log_response_max_characters() == 4
    assert tm_devices_logging.truncate_response_for_logging("abcdefghij") == (
        "'abc" + tm_devices_logging.RESPONSE_LOG_TRUNCATION_MARKER
    )
    # A per-call length overrides the global value
    assert tm_devices_logging.truncate_response_for_logging("abcdefghij", 100) == "'abcdefghij'"
