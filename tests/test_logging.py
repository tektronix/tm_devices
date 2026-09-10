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
    from types import TracebackType

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


def _capture_exception_info(
    exception: BaseException,
) -> "tuple[type[BaseException], BaseException, TracebackType]":
    """Raise and catch an exception in order to give it a real traceback.

    Args:
        exception: The exception instance to raise.

    Returns:
        The exception info tuple to pass into the package's exception handler.
    """
    captured_traceback = None
    try:
        raise exception  # noqa: TRY301
    except BaseException as error:  # noqa: BLE001
        captured_traceback = error.__traceback__
    assert captured_traceback is not None
    return type(exception), exception, captured_traceback


@pytest.fixture(name="original_excepthook_calls")
def _original_excepthook_calls(  # pyright: ignore[reportUnusedFunction]
    monkeypatch: pytest.MonkeyPatch,
) -> Generator[list[tuple[object, ...]], None, None]:
    """Record the calls made to the original excepthook by the package's exception handler."""
    recorded_calls: list[tuple[object, ...]] = []

    def _record_call(*args: object) -> None:
        recorded_calls.append(args)

    monkeypatch.setattr(tm_devices_logging, "_ORIGINAL_SYS_EXCEPTHOOK", _record_call)
    yield recorded_calls
    # The exception handler logs through temporary loggers which keep a permanent reference to the
    # package's handlers, remove them so that the logging state is left the way it was found.
    for handler_type_name in ("FileHandler", "StreamHandler"):
        temp_logger = logging.getLogger(f"{tm_devices_logging.__name__}_{handler_type_name}_only")
        for handler in temp_logger.handlers.copy():
            temp_logger.removeHandler(handler)


def test_exception_handler_with_string_message(
    original_excepthook_calls: list[tuple[object, ...]],
) -> None:
    """Verify the exception handler rewrites string messages to point at the logfile."""
    # The "See the logfile at" text asserted below is only produced when a file handler exists.
    assert any(
        isinstance(handler, logging.FileHandler)
        for handler in logging.getLogger(PACKAGE_NAME).handlers
    )
    exception_info = _capture_exception_info(ValueError("something went wrong", 42))
    tm_devices_logging.__exception_handler(*exception_info)  # noqa: SLF001  # pyright: ignore[reportPrivateUsage]
    exception = exception_info[1]
    assert original_excepthook_calls == [exception_info]
    assert exception.args[0].startswith("something went wrong")
    assert "See the logfile at" in exception.args[0]
    assert exception.args[1] == 42
    assert exception.__cause__ is None


def test_exception_handler_with_non_string_first_argument(
    original_excepthook_calls: list[tuple[object, ...]],
) -> None:
    """Verify the exception handler tolerates exceptions with a non-string first argument."""
    exception_info = _capture_exception_info(ConnectionResetError(10054, "forcibly closed"))
    tm_devices_logging.__exception_handler(*exception_info)  # noqa: SLF001  # pyright: ignore[reportPrivateUsage]
    exception = exception_info[1]
    assert original_excepthook_calls == [exception_info]
    # The arguments of an OSError must be left alone, its message is built from other attributes.
    assert exception.args == (10054, "forcibly closed")
    assert str(exception) == "[Errno 10054] forcibly closed"
    # The logfile location is attached as a note instead, which requires Python 3.11 or newer.
    if sys.version_info >= (3, 11):
        assert len(exception.__notes__) == 1
        assert exception.__notes__[0].startswith("See the logfile at")


def test_exception_handler_with_no_arguments(
    original_excepthook_calls: list[tuple[object, ...]],
) -> None:
    """Verify the exception handler falls back to the class name for an argument-less exception."""
    exception_info = _capture_exception_info(RuntimeError())
    tm_devices_logging.__exception_handler(*exception_info)  # noqa: SLF001  # pyright: ignore[reportPrivateUsage]
    exception = exception_info[1]
    assert original_excepthook_calls == [exception_info]
    assert exception.args == ()


def test_exception_handler_when_logging_fails(
    original_excepthook_calls: list[tuple[object, ...]],
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Verify a failure while logging cannot stop the original excepthook from being called."""

    def _raise_error(*_args: object, **_kwargs: object) -> str:
        msg = "the logging handlers are already closed"
        raise RuntimeError(msg)

    monkeypatch.setattr(
        tm_devices_logging, "__log_message_to_console_and_traceback_to_file", _raise_error
    )
    exception_info = _capture_exception_info(ValueError("something went wrong"))
    exception_info[1].__cause__ = KeyError("the original cause")
    tm_devices_logging.__exception_handler(*exception_info)  # noqa: SLF001  # pyright: ignore[reportPrivateUsage]
    exception = exception_info[1]
    assert original_excepthook_calls == [exception_info]
    assert exception.args == ("something went wrong",)
    # Without a logfile entry to point at, the full chained traceback is worth keeping.
    assert exception.__cause__ is not None
    assert "the logging handlers are already closed" in capsys.readouterr().err


def test_exception_handler_when_logging_raises_base_exception(
    original_excepthook_calls: list[tuple[object, ...]],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Verify a BaseException while logging still reports the original exception first."""

    def _raise_error(*_args: object, **_kwargs: object) -> str:
        raise KeyboardInterrupt

    monkeypatch.setattr(
        tm_devices_logging, "__log_message_to_console_and_traceback_to_file", _raise_error
    )
    exception_info = _capture_exception_info(ValueError("something went wrong"))
    with pytest.raises(KeyboardInterrupt):
        tm_devices_logging.__exception_handler(*exception_info)  # noqa: SLF001  # pyright: ignore[reportPrivateUsage]
    assert original_excepthook_calls == [exception_info]


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
    temp_excepthook = sys.excepthook
    yield
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
