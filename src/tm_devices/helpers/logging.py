# pyright: reportUnnecessaryTypeIgnoreComment=none
"""Helpers for logging."""

from __future__ import annotations

import importlib.metadata
import inspect
import logging
import sys
import time
import traceback

from datetime import datetime
from pathlib import Path
from typing import Literal, Optional, Tuple, Type, TYPE_CHECKING, TypeVar, Union

import colorlog
import pyvisa

from tzlocal import (
    get_localzone,  # pyright: ignore[reportUnknownVariableType]
)

from tm_devices.helpers.enums import CustomStrEnum

if TYPE_CHECKING:
    import os

    from types import TracebackType

_logger_initialized = False


_T = TypeVar("_T", bound=logging.Handler)
__MULTILINE_MESSAGE_LEADING_WHITESPACE = " " * 29
_ORIGINAL_SYS_EXCEPTHOOK = sys.__excepthook__


class _CustomFormatterWithMicroseconds(logging.Formatter):  # pragma: no cover
    """A formatter that includes microsecond precision in the timestamp."""

    converter = datetime.fromtimestamp  # pyright: ignore[reportAssignmentType]

    def formatTime(self, record: logging.LogRecord, datefmt: str | None = None) -> str:  # noqa: N802
        ct: datetime = self.converter(record.created)  # pyright: ignore[reportAssignmentType]
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            t = ct.strftime("%Y-%m-%d %H:%M:%S")
            # Use microseconds in the time format for 6 digits of precision
            s = f"{t:s}.{ct.microsecond:06d}"
        return s


class _CustomFormatterWithColorAndMicroseconds(
    colorlog.ColoredFormatter, _CustomFormatterWithMicroseconds
):  # pragma: no cover
    """A formatter that includes color and microsecond precision in the timestamp."""


class _CustomFormatterWithPackageNameAndMicroseconds(
    _CustomFormatterWithMicroseconds
):  # pragma: no cover
    """A formatter that includes the package name and microsecond precision in the timestamp."""

    def format(self, record: logging.LogRecord) -> str:
        # Add the package name to the log record
        record.package_name = record.name.split(".", maxsplit=1)[0]
        # Call the original format method
        return super().format(record)


class LoggingLevels(CustomStrEnum):
    """A class holding the valid logging levels supported."""

    DEBUG = "DEBUG"
    """An enum member representing the DEBUG logging level."""
    INFO = "INFO"
    """An enum member representing the INFO logging level."""
    WARNING = "WARNING"
    """An enum member representing the WARNING logging level."""
    ERROR = "ERROR"
    """An enum member representing the ERROR logging level."""
    CRITICAL = "CRITICAL"
    """An enum member representing the CRITICAL logging level."""
    NONE = "NONE"
    """An enum member indicating no logging messages should be captured."""


def configure_logging(  # pylint: disable=too-many-locals
    *,
    log_console_level: Union[str, LoggingLevels] = LoggingLevels.INFO,
    log_file_level: Union[str, LoggingLevels] = LoggingLevels.DEBUG,
    log_file_directory: Optional[Union[str, os.PathLike[str], Path]] = None,
    log_file_name: Optional[str] = None,
    log_colored_output: bool = False,
    log_pyvisa_messages: bool = False,
    log_uncaught_exceptions: bool = True,
) -> logging.Logger:
    """Configure the logging for this package.

    !!! note
        After this function is called once, if it is called again, it will not perform any
        additional configuration. It will simply return the base logger for the package. This means
        that if logging is configured explicitly in Python code, then any configuration options set
        in the config file or environment variables will be ignored.

    !!! important
        This function will overwrite the [`sys.excepthook`][sys.excepthook] function in order to
        log uncaught exceptions if logging to a log file is enabled. The custom hook function
        used by this package will call [`sys.__excepthook__`][sys.__excepthook__] after the custom
        code is run, so exceptions and tracebacks will still get printed to the console. If you
        have a custom exception hook function you need to use, you will need to overwrite the
        [`sys.excepthook`][sys.excepthook] function after this package's logging is configured.
        To opt out of this behavior and keep Python's default exception handling
        (which means exceptions will not be logged to the log file), set the
        `log_uncaught_exceptions` parameter to `False`.

    Args:
        log_console_level: The logging level to set for the console. Defaults to INFO. Set to
            [`LoggingLevels.NONE`][tm_devices.helpers.logging.LoggingLevels.NONE] to disable all
            console logging/printouts except for certain warnings and exceptions.
        log_file_level: The logging level to set for the file. Defaults to DEBUG. Set to
            [`LoggingLevels.NONE`][tm_devices.helpers.logging.LoggingLevels.NONE] to disable logging
            to a file entirely.
        log_file_directory: The directory to save log files to. Defaults to "./logs" in the
            current working directory.
        log_file_name: The name of the log file to save the logs to. Defaults to a timestamped name
            with the .log extension.
        log_colored_output: Whether to use colored output from the `colorlog` package for the
            console. Defaults to False.
        log_pyvisa_messages: Whether to include logs from the `pyvisa` package in the log file. The
            logging level used for these additional log entries will match
            `log_file_level`. Defaults to False.
        log_uncaught_exceptions: Whether to log uncaught exceptions to the log file with full
            tracebacks and reduce the traceback size of exceptions in the console. Defaults to True.
            Setting the `log_file_level` parameter to
            [`LoggingLevels.NONE`][tm_devices.helpers.logging.LoggingLevels.NONE] will disable
            this feature regardless of the value of `log_uncaught_exceptions`.

    Returns:
        The base logger for the package, this base logger can also be accessed using
            `logging.getLogger(tm_devices.PACKAGE_NAME)`.
    """
    from tm_devices.helpers.constants_and_dataclasses import (  # pylint: disable=import-outside-toplevel
        PACKAGE_NAME,
    )

    global _logger_initialized  # noqa: PLW0603

    _logger: logging.Logger = logging.getLogger(PACKAGE_NAME)
    if _logger_initialized:
        # If the logger was previously initialized, just return it
        return _logger
    # Convert object types into enum values
    log_console_level = LoggingLevels(log_console_level)
    log_file_level = LoggingLevels(log_file_level)
    # Set the logger level to the lowest level, the handlers will filter out specific levels
    # based on user configuration
    _logger.setLevel(logging.DEBUG)
    _logger.addHandler(logging.NullHandler())
    # The logger/module name is not included in the message, since formatting the messages to
    # be aligned would cause the width of the message prefix to be almost 100 characters before
    # the message is even added to the line.
    logging_file_format_string = "[%(asctime)s] [%(package_name)10s] [%(levelname)8s] %(message)s"
    logging_console_format_string = "%(asctime)s - %(message)s"
    if not log_file_directory:  # pragma: no cover
        log_file_directory = Path("./logs")
    if not log_file_name:  # pragma: no cover
        log_file_name = f"{PACKAGE_NAME}_{time.strftime('%m-%d-%Y_%H-%M-%S', time.localtime())}.log"
    log_filepath = Path(log_file_directory) / log_file_name

    if log_file_level != LoggingLevels.NONE:
        # Set up logger for tm_devices
        log_filepath.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_filepath, mode="w", encoding="utf-8")
        file_formatter = _CustomFormatterWithPackageNameAndMicroseconds(logging_file_format_string)

        file_handler.setLevel(getattr(logging, log_file_level.value))
        file_handler.setFormatter(file_formatter)
        _logger.addHandler(file_handler)

        if log_pyvisa_messages:
            # Hook into pyvisa's logging to save it into the same file
            pyvisa.logger.setLevel(getattr(logging, log_file_level.value))
            pyvisa.logger.addHandler(file_handler)

    # Log a few things to just the file
    _logger.debug("timezone==%s", get_localzone())  # pyright: ignore[reportUnknownArgumentType,reportUnnecessaryTypeIgnoreComment]
    _logger.debug("%s==%s", PACKAGE_NAME, importlib.metadata.version(PACKAGE_NAME))

    if log_console_level != LoggingLevels.NONE:
        if log_colored_output:
            console_handler = colorlog.StreamHandler(stream=sys.stdout)
            console_formatter = _CustomFormatterWithColorAndMicroseconds(
                "%(log_color)s" + logging_console_format_string,
                log_colors=colorlog.default_log_colors,
            )
        else:
            console_handler = logging.StreamHandler(stream=sys.stdout)
            console_formatter = _CustomFormatterWithMicroseconds(logging_console_format_string)

        console_handler.setLevel(getattr(logging, log_console_level.value))
        console_handler.setFormatter(console_formatter)
        _logger.addHandler(console_handler)

    if log_uncaught_exceptions and log_file_level != LoggingLevels.NONE:
        sys.excepthook = __exception_handler
    _logger_initialized = True
    return _logger


def __exception_handler(
    exc_type: Type[BaseException], exc_value: BaseException, exc_traceback: TracebackType
) -> None:  # pragma: no cover
    """Log uncaught exceptions."""
    from tm_devices.helpers.constants_and_dataclasses import (  # pylint: disable=import-outside-toplevel
        PACKAGE_NAME,
    )

    additional_message_for_file = (
        f"\n\nAn uncaught exception occurred. If the exception was explicitly raised by "
        f"the {PACKAGE_NAME} package, look for the most recent previous ERROR log entry "
        f"above to see the specific timestamp of the exception. Otherwise, use the "
        f"traceback to debug the issue."
    )
    updated_message = __log_message_to_console_and_traceback_to_file(
        exc_value.args[0] if exc_value.args else exc_value.__class__.__name__,
        message_for_console="UNCAUGHT EXCEPTION!!!",
        additional_message_for_file=additional_message_for_file,
        exc_info=(exc_type, exc_value, exc_traceback),
    )

    # Remove the original cause if it exists to make the traceback in the console shorter.
    exc_value.__cause__ = None
    # Update the message to include the log file location where the complete traceback is located.
    if exc_value.args:
        exc_value.args = (updated_message,) + exc_value.args[1:]
    _ORIGINAL_SYS_EXCEPTHOOK(exc_type, exc_value, exc_traceback)


def __log_to_specific_handler_type_only(
    handler_type: Type[_T],
    message: str,
    logging_level_str: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL", "EXCEPTION"],
    *,
    exc_info: Optional[Tuple[Type[BaseException], BaseException, TracebackType]] = None,
) -> Optional[_T]:  # pragma: no cover
    """Log a message to handlers of a specific type only.

    This should only be used when absolutely necessary, usually during custom error handling.

    Args:
        handler_type: The type of handler to log the message to.
        message: The message to log.
        logging_level_str: The logging level to log the message at.
        exc_info: The exception information to log. Defaults to None.

    Returns:
        A pointer to the handler that it logged the message to.
    """
    handler_used: Optional[_T] = None
    exception_info: Optional[
        Union[
            Tuple[Type[BaseException], BaseException, TracebackType],
            str,
        ]
    ] = None
    if exc_info:
        exception_info = exc_info
    elif logging_level_str == "EXCEPTION" and sys.exc_info() == (None, None, None):
        exception_info = "Traceback:\n" + "".join(
            traceback.format_stack(inspect.currentframe().f_back.f_back.f_back)  # pyright: ignore[reportOptionalMemberAccess]
        )
    try:
        log_level = getattr(logging, logging_level_str)
    except AttributeError:
        # This is from the EXCEPTION case, so we need to handle it differently
        log_level = logging.CRITICAL
    if handler_type.__name__ == "StreamHandler":
        message = f"\n{__MULTILINE_MESSAGE_LEADING_WHITESPACE}".join(message.splitlines())
    _logger = configure_logging()
    for handler in _logger.handlers:
        if handler.__class__.__name__ == handler_type.__name__ and isinstance(
            handler, handler_type
        ):
            if not handler_used:
                handler_used = handler
            temp_logger = logging.getLogger(f"{__name__}_{handler_type.__name__}_only")
            temp_logger.addHandler(handler)
            temp_logger.setLevel(log_level)
            temp_logger.propagate = False
            if isinstance(exception_info, str):
                temp_logger.log(log_level, "%s%s", message, exception_info)
            elif exc_info:
                temp_logger.log(log_level, message, exc_info=exc_info)
            else:
                temp_logger.log(log_level, message, exc_info=logging_level_str == "EXCEPTION")

    return handler_used


def __log_message_to_console_and_traceback_to_file(
    message: str,
    *,
    message_for_console: Optional[str] = None,
    additional_message_for_file: str = "",
    exc_info: Optional[Tuple[Type[BaseException], BaseException, TracebackType]] = None,
) -> str:  # pyright: ignore[reportUnusedFunction]  # pragma: no cover
    """Log a message to the console and the current traceback to the log file.

    This should only be used when absolutely necessary, usually during custom error handling.

    Args:
        message: The primary message to log.
        message_for_console: The message to log to the console. Defaults to None. Overrides the
            `message` parameter if present.
        additional_message_for_file: An additional message to log to the file. Defaults to None
        exc_info: The exception information to log. Defaults to None.

    Returns:
        The message that was logged, with additional text appended indicating the
            complete traceback is located in the log file.
    """
    file_handler = __log_to_specific_handler_type_only(
        logging.FileHandler,
        message.split("\n")[0] + additional_message_for_file + "\n\n",
        "EXCEPTION",
        exc_info=exc_info,
    )
    __log_to_specific_handler_type_only(
        logging.StreamHandler, message_for_console or message, "CRITICAL"
    )
    if file_handler:
        message += (
            f"\n\nSee the logfile at '{file_handler.baseFilename}' for the complete traceback."
        )
    else:
        message += (
            "No logfile was created, so the complete traceback is not available. "
            "To ensure the complete traceback is available, please update the logging "
            "configuration to include a logfile."
        )
    return message
