"""Helpers for logging."""

import importlib.metadata
import logging
import sys
import time

from pathlib import Path
from typing import Optional

import colorlog
import pyvisa

from tzlocal import get_localzone  # pyright: ignore[reportUnknownVariableType]

from tm_devices.helpers.constants_and_dataclasses import PACKAGE_NAME
from tm_devices.helpers.enums import LoggingLevels

_logger_initialized = False


class _CustomFormatter(logging.Formatter):  # pragma: no cover
    def format(self, record: logging.LogRecord) -> str:
        # Add the package name to the log record
        record.package_name = record.name.split(".", maxsplit=1)[0]
        # Call the original format method
        return super().format(record)


def configure_logging(
    *,
    console_logging_level: LoggingLevels = LoggingLevels.INFO,
    file_logging_level: LoggingLevels = LoggingLevels.DEBUG,
    log_file_directory: Optional[Path] = None,
    log_file_name: Optional[str] = None,
    colored_output: bool = True,
    include_pyvisa_logs: bool = True,
) -> logging.Logger:  # pragma: no cover
    """Configure the logging for this package.

    Args:
        console_logging_level: The logging level to set for the console. Defaults to INFO. Set to
            [`LoggingLevels.NONE`][tm_devices.helpers.enums.LoggingLevels.NONE] to disable all
            console logging/printouts except for certain warnings and exceptions.
        file_logging_level: The logging level to set for the file. Defaults to DEBUG. Set to
            [`LoggingLevels.NONE`][tm_devices.helpers.enums.LoggingLevels.NONE] to disable logging
            to a file entirely.
        log_file_directory: The directory to save the log file to. Defaults to "./logs" in the
            current working directory.
        log_file_name: The name of the log file to save the logs to. Defaults to a timestamped name.
        colored_output: Whether to use colored output from the `colorlog` package for the console.
            Defaults to True.
        include_pyvisa_logs: Whether to include logs from the `pyvisa` package in the log file. The
            logging level will match the `file_logging_level`. Defaults to True.

    Returns:
        The base logger for the package, this base logger can also be accessed using
        `logging.getLogger(tm_devices.PACKAGE_NAME)`.
    """
    global _logger_initialized  # noqa: PLW0603

    _logger: logging.Logger = logging.getLogger(PACKAGE_NAME)
    if _logger_initialized:
        # If the logger was previously initialized, just return it
        return _logger
    # Set the logger level to the lowest level, the handlers will filter out specific levels
    # based on user configuration
    _logger.setLevel(logging.DEBUG)
    _logger.addHandler(logging.NullHandler())
    # The logger/module name is not included in the message, since formatting the messages to
    # be aligned would cause the width of the message prefix to be almost 100 characters before
    # the message is even added to the line.
    logging_file_format_string = "[%(asctime)s] [%(package_name)10s] [%(levelname)8s] %(message)s"
    logging_console_format_string = "%(asctime)s - %(message)s"
    if not log_file_directory:
        log_file_directory = Path("./logs")
    if not log_file_name:
        log_file_name = f"{PACKAGE_NAME}_{time.strftime('%m-%d-%Y_%H-%M-%S', time.localtime())}.log"
    log_filepath = log_file_directory / log_file_name

    # TODO: logging: look into rotating log files
    if file_logging_level != LoggingLevels.NONE:
        # Set up logger for tm_devices
        log_filepath.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_filepath, mode="w", encoding="utf-8")
        file_formatter = _CustomFormatter(logging_file_format_string)
        file_formatter.default_msec_format = "%s.%06d"  # Use 6 digits of precision for milliseconds

        file_handler.setLevel(getattr(logging, file_logging_level.value))
        file_handler.setFormatter(file_formatter)
        _logger.addHandler(file_handler)

        if include_pyvisa_logs:
            # Hook into pyvisa's logging to save it into the same file
            pyvisa.logger.setLevel(getattr(logging, file_logging_level.value))
            pyvisa.logger.addHandler(file_handler)

    # Log a few things to just the file
    _logger.debug("timezone==%s", get_localzone())  # pyright: ignore[reportUnknownArgumentType]
    _logger.debug("%s==%s", PACKAGE_NAME, importlib.metadata.version(PACKAGE_NAME))

    if console_logging_level != LoggingLevels.NONE:
        if colored_output:
            console_handler = colorlog.StreamHandler(stream=sys.stdout)
            console_formatter = colorlog.ColoredFormatter(
                "%(log_color)s" + logging_console_format_string,
                log_colors=colorlog.default_log_colors,
            )
        else:
            console_handler = logging.StreamHandler(stream=sys.stdout)
            console_formatter = logging.Formatter(logging_console_format_string)
        console_formatter.default_msec_format = (
            "%s.%06d"  # Use 6 digits of precision for milliseconds
        )

        console_handler.setLevel(getattr(logging, console_logging_level.value))
        console_handler.setFormatter(console_formatter)
        _logger.addHandler(console_handler)

    _logger_initialized = True
    return _logger
