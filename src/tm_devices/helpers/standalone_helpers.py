"""Module containing helpers for the `tm_devices` package that only use standard library imports."""

import ipaddress
import re

from typing import Final

####################################################################################################
# Private Constants
####################################################################################################
_HOSTNAME_REGEX = re.compile(
    r"^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*"
    r"([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$"
)

####################################################################################################
# Public Constants
####################################################################################################
PYVISA_PY_BACKEND: Final[str] = "@py"
"""Constant string which indicates to use the pure Python PyVISA-py backend when creating VISA connections."""  # noqa: E501

SYSTEM_DEFAULT_VISA_BACKEND: Final[str] = ""
"""Constant string which indicates to use the current system's default VISA backend when creating VISA connections."""  # noqa: E501

PACKAGE_NAME: Final[str] = "tm_devices"
"""Constant string with the name of this package."""

VISA_RESOURCE_EXPRESSION_REGEX: "Final[re.Pattern[str]]" = re.compile(  # pylint: disable=unsubscriptable-object,useless-suppression
    r"^(\w+)(?:::0X\w+)?::([-.\w]+)(?:::(\w+))?(?:::INST0?)?::(INSTR?|SOCKET)$"
)
"""A regex pattern used to capture pieces of VISA resource expressions."""


####################################################################################################
# Public Functions
####################################################################################################
def validate_address(address: str) -> bool:
    """Validate an IP address or hostname.

    Args:
        address: The address to validate.

    Returns:
        A boolean, if False, the address was an IP address. If True, the address was a hostname.

    Raises:
        ValueError: Indicating the address was not a valid IP address or hostname.
    """
    is_hostname = False
    try:
        _ = ipaddress.ip_address(address)
    except ValueError as error:
        if not _HOSTNAME_REGEX.match(address):
            msg = f"{address=} is not a valid IP address or hostname."
            raise ValueError(msg) from error
        is_hostname = True

    return is_hostname
