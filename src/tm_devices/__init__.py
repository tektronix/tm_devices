"""Test & Measurement Device Management.

Provides access to commonly imported items from the `tm_devices` package.

Examples:
    >>> from tm_devices import DeviceManager
    >>> with DeviceManager() as dm:
    ...     print(dm.is_open)
    2... - Opening DeviceManager
    True
    2... - DeviceManager Closed
"""

from importlib.metadata import version

from tm_devices.device_manager import DeviceManager, print_available_visa_devices
from tm_devices.helpers.constants_and_dataclasses import (
    PACKAGE_NAME,
    PYVISA_PY_BACKEND,
    SYSTEM_DEFAULT_VISA_BACKEND,
)
from tm_devices.helpers.enums import SupportedModels
from tm_devices.helpers.functions import register_additional_usbtmc_mapping
from tm_devices.helpers.logging import configure_logging, LoggingLevels

# Read version from installed package.
__version__ = version(PACKAGE_NAME)


__all__ = [
    "PYVISA_PY_BACKEND",
    "SYSTEM_DEFAULT_VISA_BACKEND",
    "DeviceManager",
    "LoggingLevels",
    "SupportedModels",
    "configure_logging",
    "print_available_visa_devices",
    "register_additional_usbtmc_mapping",
]
