"""Test & Measurement Device Management.

Provides access to commonly imported items from the tm_devices package.

Examples:
    >>> from tm_devices import DeviceManager
    >>> with DeviceManager() as dm:  # doctest: +SKIP
    ...     print(dm.is_open)
    2023-09-21 01:50:16.031 - Opening DeviceManager
    True
    2023-09-21 01:50:16.031 - DeviceManager Closed
"""
from importlib.metadata import version

from tm_devices.device_manager import DeviceManager, print_available_visa_devices
from tm_devices.helpers.constants_and_dataclasses import (
    PACKAGE_NAME,
    PYVISA_PY_BACKEND,
    SYSTEM_DEFAULT_VISA_BACKEND,
)
from tm_devices.helpers.enums import SupportedModels

# Read version from installed package.
__version__ = version(PACKAGE_NAME)

__all__ = [
    "DeviceManager",
    "print_available_visa_devices",
    "PYVISA_PY_BACKEND",
    "SupportedModels",
    "SYSTEM_DEFAULT_VISA_BACKEND",
]
