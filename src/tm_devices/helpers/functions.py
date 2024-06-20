"""Module containing helpers for the `tm_devices` package."""

import contextlib
import datetime
import importlib.metadata
import json
import platform
import re
import shlex
import socket
import subprocess  # nosec
import time
import warnings

from enum import EnumMeta
from functools import lru_cache
from typing import Any, Dict, Optional, Tuple, Type

import requests

from dateutil.tz import tzlocal
from packaging.version import InvalidVersion, Version

from tm_devices.helpers.constants_and_dataclasses import (
    ConnectionTypes,
    DeviceConfigEntry,
    PACKAGE_NAME,
    PYVISA_PY_BACKEND,
    USB_MODEL_ID_LOOKUP,
    VISA_RESOURCE_EXPRESSION_REGEX,
)
from tm_devices.helpers.enums import CustomStrEnum, SupportedModels
from tm_devices.helpers.standalone_functions import validate_address

with warnings.catch_warnings():
    warnings.simplefilter("ignore", UserWarning)
    import pyvisa as visa

    from gpib_ctypes import make_default_gpib  # pyright: ignore[reportMissingTypeStubs]
    from pyvisa import util as pyvisa_util
    from pyvisa.resources import MessageBasedResource

    make_default_gpib()

####################################################################################################
# Private Constants
####################################################################################################
__SUPPORTED_MODEL_REGEX_STRING = (
    # AFGs
    rf"(?P<{SupportedModels.AFG3K.value}>^AFG3\d\d\d$)"
    rf"|(?P<{SupportedModels.AFG3KB.value}>^AFG3\d\d\dB$)"
    rf"|(?P<{SupportedModels.AFG3KC.value}>^AFG3\d\d\dC$)"
    rf"|(?P<{SupportedModels.AFG31K.value}>^AFG31\d\d\d$)"
    # AWGs
    rf"|(?P<{SupportedModels.AWG5200.value}>^AWG52\d\d$)"
    rf"|(?P<{SupportedModels.AWG5K.value}>^AWG5\d\d\d$)"
    rf"|(?P<{SupportedModels.AWG5KB.value}>^AWG5\d\d\dB$)"
    rf"|(?P<{SupportedModels.AWG5KC.value}>^AWG5\d\d\dC$)"
    rf"|(?P<{SupportedModels.AWG7K.value}>^AWG7\d\d\d$)"
    rf"|(?P<{SupportedModels.AWG7KB.value}>^AWG7\d\d\dB$)"
    rf"|(?P<{SupportedModels.AWG7KC.value}>^AWG7\d\d\dC$)"
    rf"|(?P<{SupportedModels.AWG70KA.value}>^AWG70\d\d\dA?$)"
    rf"|(?P<{SupportedModels.AWG70KB.value}>^AWG70\d\d\dB$)"
    # Scopes
    rf"|(?P<{SupportedModels.DPO5K.value}>^DPO5\d\d\d$)"
    rf"|(?P<{SupportedModels.DPO5KB.value}>^DPO5\d\d\dB$)"
    rf"|(?P<{SupportedModels.DPO7K.value}>^DPO7\d\d\d$)"
    rf"|(?P<{SupportedModels.DPO7KC.value}>^DPO7\d\d\dC$)"
    rf"|(?P<{SupportedModels.DPO70K.value}>^DPO7\d\d\d\d$)"
    rf"|(?P<{SupportedModels.DPO70KC.value}>^DPO7\d\d\d\dC$)"
    rf"|(?P<{SupportedModels.DPO70KD.value}>^DPO7\d\d\d\dD$)"
    rf"|(?P<{SupportedModels.DPO70KDX.value}>^DPO7\d\d\d\dDX$)"
    rf"|(?P<{SupportedModels.DPO70KSX.value}>^DPO7\d\d\d\dSX$)"
    rf"|(?P<{SupportedModels.DSA70K.value}>^DSA7\d\d\d\d$)"
    rf"|(?P<{SupportedModels.DSA70KC.value}>^DSA7\d\d\d\dC$)"
    rf"|(?P<{SupportedModels.DSA70KD.value}>^DSA7\d\d\d\dD$)"
    rf"|(?P<{SupportedModels.LPD6.value}>^LPD6\d$)"
    rf"|(?P<{SupportedModels.MSO2.value}>^MSO2\d$)"
    rf"|(?P<{SupportedModels.MSO4.value}>^MSO4\d$)"
    rf"|(?P<{SupportedModels.MSO4B.value}>^MSO4\dB$)"
    rf"|(?P<{SupportedModels.MSO5.value}>^MSO5\d$)"
    rf"|(?P<{SupportedModels.MSO5B.value}>^MSO5\dB$)"
    rf"|(?P<{SupportedModels.MSO5LP.value}>^MSO5\dLP$)"
    rf"|(?P<{SupportedModels.MSO6.value}>^MSO6\d$)"
    rf"|(?P<{SupportedModels.MSO6B.value}>^MSO6\dB$)"
    rf"|(?P<{SupportedModels.MSO2K.value}>^MSO2\d\d\d$)"
    rf"|(?P<{SupportedModels.MSO2KB.value}>^MSO2\d\d\dB$)"
    rf"|(?P<{SupportedModels.DPO2K.value}>^DPO2\d\d\d$)"
    rf"|(?P<{SupportedModels.DPO2KB.value}>^DPO2\d\d\dB$)"
    rf"|(?P<{SupportedModels.MDO3.value}>^MDO3\d$)"
    rf"|(?P<{SupportedModels.MDO3K.value}>^MDO3\d\d\d$)"
    rf"|(?P<{SupportedModels.MSO4K.value}>^MSO4\d\d\d$)"
    rf"|(?P<{SupportedModels.MSO4KB.value}>^MSO4\d\d\dB$)"
    rf"|(?P<{SupportedModels.MDO4K.value}>^MDO4\d\d\d$)"
    rf"|(?P<{SupportedModels.MDO4KB.value}>^MDO4\d\d\dB$)"
    rf"|(?P<{SupportedModels.MDO4KC.value}>^MDO4\d\d\dC$)"
    rf"|(?P<{SupportedModels.DPO4K.value}>^DPO4\d\d\d$)"
    rf"|(?P<{SupportedModels.DPO4KB.value}>^DPO4\d\d\dB$)"
    rf"|(?P<{SupportedModels.MSO5K.value}>^MSO5\d\d\d$)"
    rf"|(?P<{SupportedModels.MSO5KB.value}>^MSO5\d\d\dB$)"
    rf"|(?P<{SupportedModels.MSO70K.value}>^MSO7\d\d\d\d$)"
    rf"|(?P<{SupportedModels.MSO70KC.value}>^MSO7\d\d\d\dC$)"
    rf"|(?P<{SupportedModels.MSO70KDX.value}>^MSO7\d\d\d\dDX$)"
    rf"|(?P<{SupportedModels.TEKSCOPESW.value}>^TEKSCOPESW$)"
    rf"|(?P<{SupportedModels.TSOVU.value}>^TSOVU$)"
    rf"|(?P<{SupportedModels.TMT4.value}>^TMT4$)"
    # SMUs
    rf"|(?P<{SupportedModels.SMU2400.value}>^2400$)"
    rf"|(?P<{SupportedModels.SMU2401.value}>^2401$)"
    rf"|(?P<{SupportedModels.SMU2410.value}>^2410$)"
    rf"|(?P<{SupportedModels.SMU2450.value}>^2450$)"
    rf"|(?P<{SupportedModels.SMU2460.value}>^2460$)"
    rf"|(?P<{SupportedModels.SMU2461.value}>^2461$)"
    rf"|(?P<{SupportedModels.SMU2470.value}>^2470$)"
    rf"|(?P<{SupportedModels.SMU2601B_PULSE.value}>^2601B-PULSE$)"
    rf"|(?P<{SupportedModels.SMU2601B.value}>^2601B$)"
    rf"|(?P<{SupportedModels.SMU2602B.value}>^2602B$)"
    rf"|(?P<{SupportedModels.SMU2604B.value}>^2604B$)"
    rf"|(?P<{SupportedModels.SMU2606B.value}>^2606B$)"
    rf"|(?P<{SupportedModels.SMU2611B.value}>^2611B$)"
    rf"|(?P<{SupportedModels.SMU2612B.value}>^2612B$)"
    rf"|(?P<{SupportedModels.SMU2614B.value}>^2614B$)"
    rf"|(?P<{SupportedModels.SMU2634B.value}>^2634B$)"
    rf"|(?P<{SupportedModels.SMU2635B.value}>^2635B$)"
    rf"|(?P<{SupportedModels.SMU2636B.value}>^2636B$)"
    rf"|(?P<{SupportedModels.SMU2651A.value}>^2651A$)"
    rf"|(?P<{SupportedModels.SMU2657A.value}>^2657A$)"
    rf"|(?P<{SupportedModels.SMU2601A.value}>^2601A$)"
    rf"|(?P<{SupportedModels.SMU2602A.value}>^2602A$)"
    rf"|(?P<{SupportedModels.SMU2604A.value}>^2604A$)"
    rf"|(?P<{SupportedModels.SMU2611A.value}>^2611A$)"
    rf"|(?P<{SupportedModels.SMU2612A.value}>^2612A$)"
    rf"|(?P<{SupportedModels.SMU2614A.value}>^2614A$)"
    rf"|(?P<{SupportedModels.SMU2634A.value}>^2634A$)"
    rf"|(?P<{SupportedModels.SMU2635A.value}>^2635A$)"
    rf"|(?P<{SupportedModels.SMU2636A.value}>^2636A$)"
    rf"|(?P<{SupportedModels.SMU6430.value}>^6430$)"
    rf"|(?P<{SupportedModels.SMU6514.value}>^6514$)"
    rf"|(?P<{SupportedModels.SMU6517B.value}>^6517B$)"
    # PSUs
    rf"|(?P<{SupportedModels.PSU2200.value}>^2200$)"
    rf"|(?P<{SupportedModels.PSU2220.value}>^2220$)"
    rf"|(?P<{SupportedModels.PSU2230.value}>^2230$)"
    rf"|(?P<{SupportedModels.PSU2231.value}>^2231$)"
    rf"|(?P<{SupportedModels.PSU2231A.value}>^2231A$)"
    rf"|(?P<{SupportedModels.PSU2280.value}>^2280$)"
    rf"|(?P<{SupportedModels.PSU2281.value}>^2281$)"
    # DAQs
    rf"|(?P<{SupportedModels.DAQ6510.value}>^DAQ6510$)"
    # DMMs
    rf"|(?P<{SupportedModels.DMM6500.value}>^DMM6500$)"
    rf"|(?P<{SupportedModels.DMM7510.value}>^DMM7510$)"
    rf"|(?P<{SupportedModels.DMM7512.value}>^DMM7512$)"
    # SSs
    rf"|(?P<{SupportedModels.SS3706A.value}>^3706A$)"
)
# NOTE: This regex would show as having a bunch of errors in the PyCharm IDE due to an
# open bug affecting f-strings in regex: https://youtrack.jetbrains.com/issue/PY-52140.
# For this reason, the regex string itself is stored in a separate, private constant.
_SUPPORTED_MODEL_REGEX_MAPPING = re.compile(__SUPPORTED_MODEL_REGEX_STRING)


####################################################################################################
# Public Functions
####################################################################################################
def check_for_update(package_name: str = PACKAGE_NAME, index_name: str = "pypi") -> None:
    """Check for an update for the provided package.

    Args:
        package_name: Check for an update for the provided package.
        index_name: The name of the index (pypi|test.pypi) to check for the package.
    """
    try:
        # Get the version from the local installation
        installed_version = importlib.metadata.version(package_name)

        # Get the version from the index
        # This code mirrors code found in scripts/pypi_latest_version.py.
        # If this code is updated, the script should be updated too.
        url = f"https://{index_name}.org/pypi/{package_name}/json"
        response = requests.get(url, timeout=10)
        releases = json.loads(response.text)["releases"]
        version_list = sorted(releases, key=Version, reverse=True)
        latest_version = version_list[0]

        if installed_version != latest_version:
            print(
                f"\n\n\033[91mVersion {latest_version} of "
                f"{package_name} is available on {index_name}.org.\n"
                f"Version {installed_version} of "
                f"{package_name} is currently installed.\n\n"
                f"To upgrade {package_name} run the following command: "
                f"python -m pip install -U {package_name}\n\n\033[0m"
            )
    except ModuleNotFoundError:
        print(
            f"\n\n\033[91m{package_name} is not installed, "
            f"unable to check for updates.\n\n\033[0m"
        )
    except (IndexError, ValueError):
        print(
            f"\n\n\033[91m{package_name} is not available on {index_name}.org, "
            f"unable to check for updates.\n\n\033[0m"
        )


def check_network_connection(
    device_name: str, ip_address: str, verbose: bool = True
) -> Tuple[bool, str]:
    """Check the network connection to the device using the external ping command.

    Args:
        device_name: The name of the device.
        ip_address: The ip address of the device.
        verbose: Set this to False in order to disable printouts.

    Returns:
        A boolean indicating if there is a network connection and
        a string with the result of the ping command.
    """
    if verbose:
        print_with_timestamp(f"({device_name}) ping >> {ip_address}")
        print(f"{get_timestamp_string()} - ")
    ping_result = ping_address(ip_address)
    if verbose:
        print_with_timestamp("Response from ping >>")
        for line in ping_result.strip().split("\n"):
            print(f"    {line}")

    return "ttl=" in ping_result.lower(), ping_result


def check_port_connection(
    device_name: str, ip_address: str, port: int, timeout_seconds: int = 5, verbose: bool = True
) -> bool:
    """Check if the given port is open on the device.

    Args:
        device_name: The name of the device.
        ip_address: The ip address.
        port: The port to check.
        timeout_seconds: The number of seconds to use as the socket timeout.
        verbose: Set this to False in order to disable printouts.

    Returns:
        A boolean indicating if the port is open.
    """
    if verbose:
        print_with_timestamp(f"({device_name}) >> checking if port {port} is open on {ip_address}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as temp_socket:
        try:
            temp_socket.settimeout(timeout_seconds)
            temp_socket.connect((ip_address, port))
            temp_socket.shutdown(socket.SHUT_RDWR)
            port_open = True
        except (socket.error, socket.gaierror, socket.herror):
            port_open = False

    if verbose:
        print_with_timestamp(f"Result >> {port_open}")
    return port_open


def check_visa_connection(
    config_entry: DeviceConfigEntry, visa_library: str, device_name: str, verbose: bool = True
) -> bool:
    """Check if a VISA connection can be made to the device.

    Args:
        config_entry: The device listed in the config of the framework to check.
        visa_library: Indicates which visa library to use for the connection.
        device_name: The name of the device.
        verbose: Set this to False in order to disable printouts.

    Returns:
        a boolean indicating if the visa connection was successful
    """
    if verbose:
        print_with_timestamp(
            f"({device_name}) >> checking if a VISA connection can be made to "
            f"{config_entry.get_visa_resource_expression()}"
        )
    try:
        # Create new VISA connection
        temp_resource = create_visa_connection(
            config_entry,
            visa_library=visa_library,
        )
        temp_resource.close()
        visa_connected = True
    except ConnectionError:  # raised by the create_visa_connection() function
        visa_connected = False

    if verbose:
        print_with_timestamp(f"Result >> {visa_connected}")
    return visa_connected


def create_visa_connection(
    device_config_entry: DeviceConfigEntry,
    visa_library: str,
    *,
    retry_connection: bool = False,
) -> MessageBasedResource:
    """Create a VISA resource.

    Args:
        device_config_entry: The device config entry.
        visa_library: A string containing the VISA library to use to create a ResourceManager.
        retry_connection: Boolean indicating if a second connection attempt should be made. If True,
            two attempts are made to establish a VISA connection, with a 60-second delay in between
            each attempt.

    Returns:
        A VISA resource that can be passed into the device driver.

    Raises:
        ConnectionError: The VISA connection couldn't be created to the device.
    """
    # Set up the VISA resource that will be used for communicating with the VISA device
    resource_expression = device_config_entry.get_visa_resource_expression()
    try:
        # noinspection PyTypeChecker
        visa_object: MessageBasedResource = visa.ResourceManager(  # pyright: ignore[reportAssignmentType]
            visa_library
        ).open_resource(resource_expression)
        # Print a warning if PyVISA-py is used when the user didn't specify STANDALONE
        if (
            visa_object.visalib.library_path.path == "py" and visa_library != PYVISA_PY_BACKEND
        ):  # pragma: no cover
            warnings.warn(
                "No VISA installation was detected, defaulting to using "
                "PyVISA-py as the VISA backend.\n\n"
                'Add the "STANDALONE" option to the configuration to silence this warning.',
                stacklevel=4,
            )
    # The broad except is because pyvisa_py can throw a base exception in the tcpip.py file
    except Exception as error_1:
        if not retry_connection:
            message = f"Unable to establish a VISA connection to {resource_expression}"
            raise ConnectionError(message) from error_1
        time.sleep(60)  # wait 60 seconds and try again
        try:
            # noinspection PyTypeChecker
            visa_object: MessageBasedResource = visa.ResourceManager(  # pyright: ignore[reportAssignmentType]
                visa_library
            ).open_resource(resource_expression)
        # The broad except is because pyvisa_py can throw a base exception in the tcpip.py file
        except Exception as error_2:
            message = f"Unable to establish a VISA connection to {resource_expression}\n\n"
            if device_config_entry.connection_type in {
                ConnectionTypes.TCPIP,
                ConnectionTypes.SOCKET,
            }:
                message += (
                    f"This is the current ping output for the device at "
                    f"{device_config_entry.address}:\n{ping_address(device_config_entry.address)}"
                )
            raise ConnectionError(message) from error_2

    return _configure_visa_object(visa_object, device_config_entry, visa_library)


def detect_visa_resource_expression(input_str: str) -> Optional[Tuple[str, str]]:
    """Check if a given string is a VISA resource expression.

    This function will check if a string is a VISA resource expression and pull out the pieces
    needed to make a connection using the DeviceManager.

    The pieces consist of:
        - The connection type, e.g. TCPIP, GPIB<board_number> (e.g. GPIB0).
        - The address of the device, an IP address
          (with port separated by a colon for SOCKET connections), hostname, or
          string in the format ``model-serial``.

    Args:
        input_str: The string to check for a VISA resource expression.

    Returns:
        A tuple with the connection information parts.
    """
    retval: Optional[Tuple[str, str]] = None
    if input_str.upper().startswith("ASRL"):
        retval = (ConnectionTypes.SERIAL.value, input_str[4:].split("::", 1)[0])
    elif (match := VISA_RESOURCE_EXPRESSION_REGEX.search(input_str.upper())) is not None:
        match_groups_list = list(filter(None, match.groups()))
        for unneeded_part in ("INST", "INST0", "INSTR"):
            while unneeded_part in match_groups_list:
                match_groups_list.remove(unneeded_part)
        # Check if the model is in the USB model lookup
        filtered_usb_model_keys = [
            key
            for key, value in USB_MODEL_ID_LOOKUP.items()
            if value.model_id == match_groups_list[1].lower()
        ]
        if filtered_usb_model_keys:
            # SMU and PSU need to be removed from the string to prevent issues
            match_groups_list[1] = filtered_usb_model_keys[0].replace("SMU", "").replace("PSU", "")
        if match_groups_list[-1] == ConnectionTypes.SOCKET.value:
            retval = (match_groups_list[-1], ":".join(match_groups_list[1:3]))
        # If connection_type is GPIB, the board number must be passed back in the returned value
        elif input_str.upper().startswith(ConnectionTypes.GPIB.value.upper()):
            retval = (
                match_groups_list[0],
                "-".join(match_groups_list[1:]).lstrip("0X"),
            )
        else:
            retval = (
                match_groups_list[0].rstrip("0"),
                "-".join(match_groups_list[1:]).lstrip("0X"),
            )
    return retval


def get_model_series(model: str) -> str:
    """Get the series string from the full model number.

    Args:
        model: The full model string (ex. MSO58, LPD64).

    Returns:
        The model series string (ex. MSO5, LPD6).
    """
    model_parts = model.strip().upper().split("-")
    simplified_model = model_parts[0].replace("MODEL", "").strip()

    # Remove "Virtual" from the model string
    simplified_model = simplified_model.replace("VIRTUAL", "")

    # Remove ending characters from the model string that doesn't
    # contribute to determining the correct series.
    valid_model_endings = {"A", "B", "C", "D", "LP"}
    model_end = ""
    if re.search(r"\d", simplified_model):  # if the model contains numbers
        model_end = re.split(r"\d+", simplified_model)[-1]  # split on the occurrence of each number
    if len(model_end) == 1 and model_end not in valid_model_endings:
        simplified_model = simplified_model.rstrip(model_end)

    # Check for any postscripts, e.g. 2601B-Pulse where "Pulse" is the postscript, which are a
    # necessary part of determining the correct series and add them back to the model string
    # to use to determine the series.
    if len(model_parts) > 1:
        for count, part in enumerate(model_parts):
            # avoid first model part as a postscript will likely never be in the beginning
            if count and len(part) > 1 and all(x.isalpha() for x in part):
                simplified_model += f"-{part}"

    # Find the series by checking against the regex mapping
    model_series = ""
    if match := _SUPPORTED_MODEL_REGEX_MAPPING.match(simplified_model):
        match_dict = match.groupdict()
        filtered_dict = dict(filter(lambda item: item[1] is not None, match_dict.items()))
        with contextlib.suppress(StopIteration):
            model_series = next(iter(filtered_dict.keys()))

    # Warn the user if the model is not in the regex mapping or list of supported models,
    # and therefore not officially supported.
    if not model_series:
        if model not in SupportedModels.list_values():
            warnings.warn(f'The "{model}" model is not supported by {PACKAGE_NAME}', stacklevel=2)
        model_series = model
    return model_series


def get_timestamp_string() -> str:
    """Return a string containing the current timestamp."""
    return str(datetime.datetime.now(tz=tzlocal()))[:-3]


def get_version(version_string: str) -> Version:
    """Get a Version object from a string.

    Args:
        version_string: The string containing the version to create.

    Returns:
        The Version object.
    """
    version_parts = version_string.split(".")
    found_alpha = False
    try:
        version = Version(version_string)
    except InvalidVersion:
        if all(x.isalpha() for x in version_parts[-1]) and all(
            y.isdigit() for y in version_parts[:-1]
        ):
            version = Version(
                version_string.replace("." + version_parts[-1], "+" + version_parts[-1])
            )
        else:
            output_str = ""
            for char in version_parts[-1]:
                if char.isalpha() and not found_alpha:
                    output_str += "+" + char
                    found_alpha = True
                else:
                    output_str += char
            version = Version(version_string.replace(version_parts[-1], output_str))
    return version


def get_visa_backend(visa_lib_path: str) -> str:
    """Create a human-readable VISA backend name based on the currently used VISA library path.

    Args:
        visa_lib_path: The path to the currently used VISA library.

    Returns:
        A string indicating the current VISA backend.
    """
    visa_name = ""

    system_visa_info = _get_system_visa_info()
    # noinspection PyTypeChecker
    visa_backends: Dict[str, Any] = system_visa_info["backends"]

    # Figure out which visa is being used
    try:
        if visa_lib_path == "py":
            visa_name = "PyVISA-py"
        else:
            raise KeyError
    except KeyError:
        found_visa = False
        for visa_type in visa_backends:
            for visa_implementation in visa_backends[visa_type]:
                if visa_lib_path in visa_implementation:
                    vendor = visa_backends[visa_type][visa_implementation]["Vendor"]
                    visa_name = "NI-VISA" if "National Instruments" in vendor else f"{vendor} VISA"
                    found_visa = True
                elif visa_lib_path.endswith("yaml") and visa_type == "sim":
                    visa_name = "PyVISA-sim"
                    found_visa = True
            if found_visa:
                break

    return visa_name


def ping_address(address: str, timeout: int = 2) -> str:
    """Ping the given address.

    Args:
        address: The address to ping, either an IP or hostname.
        timeout: The timeout to use, in seconds.

    Returns:
         The response of the ping command.
    """
    ping_command = _create_ping_command(address, timeout)

    try:
        output = subprocess.check_output(shlex.split(ping_command)).decode("utf-8")  # noqa: S603
    except subprocess.CalledProcessError:
        output = ""
    return output.replace("\r\n", "\n")


def print_with_timestamp(message: str, end: str = "\n") -> str:
    """Print and return a string prepended with a timestamp.

    Args:
        message: The message to print.
        end: The end of the line to print.
    """
    message = f"{get_timestamp_string()} - {message}"
    print(message, end=end)
    return message


def sanitize_enum(value: str, enum_class: Type[CustomStrEnum]) -> CustomStrEnum:
    """Sanitize a string value into its enum value.

    Args:
        value: The value to check for.
        enum_class: The Enum class to look in.

    Returns:
        The enum value corresponding to the string value passed in.

    Raises:
        TypeError: Indicates that the value doesn't exist in the enum
    """
    if string_in_enum(value, enum_class):
        sanitized_enum = enum_class[value]
    else:
        msg = (
            f"{value} is not a valid enum of {enum_class.__name__}. "
            f"Valid options are: {enum_class.list_values()}"
        )
        raise TypeError(msg)

    return sanitized_enum


def string_in_enum(value: str, enum_class: EnumMeta) -> bool:
    """Check if a string value exists in an Enum class object.

    Args:
        value: The value to check for.
        enum_class: The Enum class to look in.

    Returns:
        A boolean indicating if the string exists in the Enum.
    """
    try:
        _ = enum_class[value]
    except KeyError:
        return False
    return True


####################################################################################################
# Private Functions
####################################################################################################
def _create_ping_command(address: str, timeout: int = 2) -> str:
    """Create a ping command to ping the given address.

    Args:
        address: The address to ping, either an IP or hostname.
        timeout: The timeout to use, in seconds.

    Returns:
         The response of the ping command.
    """
    validate_address(address)
    # Create the ping command
    if (platform_system := platform.system().lower()) == "windows":
        count_arg = "-n"
        timeout_arg = "-w"
        timeout_val = timeout * 1000  # Windows uses milliseconds
    else:
        count_arg = "-c"
        timeout_arg = "-W" if platform_system == "darwin" else "-w"
        timeout_val = timeout  # Linux/MacOS uses seconds
    return f"ping {address} {count_arg} 1 {timeout_arg} {timeout_val}"


def _configure_visa_object(
    visa_object: MessageBasedResource,
    device_config_entry: DeviceConfigEntry,
    visa_library: str,
) -> MessageBasedResource:
    """Configure settings on the VISA resource object.

    Args:
        visa_object: The VISA resource object to configure.
        device_config_entry: The device config entry.
        visa_library: A string containing the VISA library to use to create a ResourceManager.

    Returns:
        A VISA resource that can be passed into the device driver.
    """
    visa_object.encoding = "utf-8"

    if visa_library.endswith("@sim"):  # pragma: no cover
        visa_object.read_termination = "\n"
        visa_object.write_termination = "\n"

    if isinstance(visa_object, visa.resources.TCPIPSocket):
        # Socket connections seem to need the termination characters specified.
        visa_object.write_termination = "\n"
        visa_object.read_termination = "\n"

        if visa_library != PYVISA_PY_BACKEND:  # pragma: no cover
            visa_object.send_end = True
    elif (
        isinstance(visa_object, visa.resources.SerialInstrument)
        and device_config_entry.serial_config
    ):
        serial_config = device_config_entry.serial_config
        # update serial fields if they were specified, otherwise use the serial visa object defaults
        for name in serial_config.to_dict():
            if (value := getattr(serial_config, name)) is not None:
                setattr(visa_object, name, value)
            else:
                setattr(serial_config, name, getattr(visa_object, name))

    return visa_object


@lru_cache(maxsize=None)
def _get_system_visa_info() -> Dict[str, Any]:
    """Get the VISA information for the current system.

    Returns:
        A dictionary with the VISA info for the system.
    """
    fetch_backend_info = True

    if platform.system().lower() == "darwin":
        try:
            output = subprocess.check_output(shlex.split("csrutil status")).decode(  # noqa: S603
                "utf-8"
            )
        except subprocess.SubprocessError:
            output = ""
        if "System Integrity Protection status: enabled" in output:
            fetch_backend_info = False

    return pyvisa_util.get_system_details(backends=fetch_backend_info)
