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


def _record(response: object, **extra: object) -> logging.LogRecord:
    """Build a log record shaped like the ones the query methods emit.

    Args:
        response: The response to log as the record's second argument.
        extra: Any additional attributes to set on the record.

    Returns:
        The constructed log record.
    """
    record = logging.LogRecord(
        PACKAGE_NAME,
        logging.DEBUG,
        __file__,
        0,
        "Response from %r >>  %r",
        ("*IDN?", response),
        None,
    )
    for key, value in extra.items():
        setattr(record, key, value)
    return record


@pytest.mark.parametrize(
    ("response", "max_characters", "expected"),
    [
        # An unset override with no global limit configured logs the full repr
        (b"hello world", tm_devices_logging.UNSET, "Response from '*IDN?' >>  b'hello world'"),
        # An explicit None disables truncation
        (b"hello world", None, "Response from '*IDN?' >>  b'hello world'"),
        # A limit longer than the response does not truncate
        ("hi", 100, "Response from '*IDN?' >>  'hi'"),
        # A limit shorter than the response truncates and appends the marker
        (
            b"hello world",
            5,
            "Response from '*IDN?' >>  b'hello'"
            + tm_devices_logging.RESPONSE_LOG_TRUNCATION_MARKER,
        ),
        # A limit of zero suppresses the contents of every argument on the record
        (
            b"hello world",
            0,
            f"Response from ''{tm_devices_logging.RESPONSE_LOG_TRUNCATION_MARKER} >>  "
            f"b''{tm_devices_logging.RESPONSE_LOG_TRUNCATION_MARKER}",
        ),
    ],
)
def test_response_truncation_filter(
    response: object, max_characters: int | None | tm_devices_logging.UnsetType, expected: str
) -> None:
    """Test that the filter truncates oversized response arguments.

    Args:
        response: The response to log.
        max_characters: The per-call override to apply.
        expected: The expected formatted message.
    """
    record = _record(response, **tm_devices_logging.response_log_extra(max_characters))
    assert tm_devices_logging.ResponseTruncationFilter().filter(record)
    assert record.getMessage() == expected


def test_response_truncation_filter_applies_to_all_records(
    reset_package_logger: None,  # noqa: ARG001
) -> None:
    """Test that the global limit truncates records which never opt in to truncation."""
    configure_logging(
        log_console_level=LoggingLevels.NONE,
        log_file_level=LoggingLevels.NONE,
        log_response_max_characters=8,
    )
    log_filter = tm_devices_logging.ResponseTruncationFilter()
    # A record with no per-call override still gets truncated by the global limit
    record = _record("abcdefghij")
    assert log_filter.filter(record)
    assert record.getMessage() == (
        "Response from '*IDN?' >>  'abcdefgh'" + tm_devices_logging.RESPONSE_LOG_TRUNCATION_MARKER
    )
    # An arbitrary logging call which never opted in is truncated too
    other = logging.LogRecord(PACKAGE_NAME, logging.DEBUG, __file__, 0, "%s", ("abcdefghij",), None)
    assert log_filter.filter(other)
    assert other.getMessage() == ("abcdefgh" + tm_devices_logging.RESPONSE_LOG_TRUNCATION_MARKER)
    # Records logged with a mapping argument are handled as well
    mapping = logging.LogRecord(
        PACKAGE_NAME, logging.DEBUG, __file__, 0, "%(value)s", ({"value": "abcdefghij"},), None
    )
    assert log_filter.filter(mapping)
    assert mapping.getMessage() == ("abcdefgh" + tm_devices_logging.RESPONSE_LOG_TRUNCATION_MARKER)


def test_configure_logging_response_max_characters(reset_package_logger: None) -> None:  # noqa: ARG001
    """Test that the log_response_max_characters config option is stored globally."""
    # Truncation is disabled by default
    assert tm_devices_logging.get_log_response_max_characters() is None
    configure_logging(
        log_console_level=LoggingLevels.NONE,
        log_file_level=LoggingLevels.NONE,
        log_response_max_characters=4,
    )
    assert tm_devices_logging.get_log_response_max_characters() == 4


def test_response_log_extra() -> None:
    """Test the mapping built for overriding the truncation limit of a single logging call."""
    # An unset override produces an empty mapping, so the global value applies
    assert not tm_devices_logging.response_log_extra()
    assert not tm_devices_logging.response_log_extra(tm_devices_logging.UNSET)
    # An explicit value is passed through under the documented record attribute
    assert tm_devices_logging.response_log_extra(None) == {
        tm_devices_logging.LOG_RECORD_MAX_CHARACTERS_ATTR: None
    }
    assert tm_devices_logging.response_log_extra(10) == {
        tm_devices_logging.LOG_RECORD_MAX_CHARACTERS_ATTR: 10
    }


def test_unset_sentinel_repr() -> None:
    """Test that the sentinel renders readably in the generated API documentation."""
    assert repr(tm_devices_logging.UNSET) == "UNSET"


def test_response_truncation_filter_keeps_small_arguments() -> None:
    """Test that arguments within the limit are passed through untouched."""
    record = logging.LogRecord(
        PACKAGE_NAME, logging.DEBUG, __file__, 0, "%r %r", (12345, "ok"), None
    )
    setattr(record, tm_devices_logging.LOG_RECORD_MAX_CHARACTERS_ATTR, 100)
    assert tm_devices_logging.ResponseTruncationFilter().filter(record)
    assert record.args == (12345, "ok")
    assert record.getMessage() == "12345 'ok'"
