"""Module containing helpers for the tm_devices package."""
import contextlib
import datetime
import os
import platform
import re
import shlex
import socket
import subprocess  # nosec
import time
import warnings

from enum import EnumMeta
from typing import Any, Dict, Optional, Tuple, Type

from check4updates import check_and_prompt  # type: ignore
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

    from gpib_ctypes import make_default_gpib  # type: ignore
    from pyvisa import util as pyvisa_util
    from pyvisa.resources import MessageBasedResource

    make_default_gpib()

####################################################################################################
# Private Constants
####################################################################################################
_VISA_SYSTEM_DETAILS: Dict[str, Any] = pyvisa_util.get_system_details()
_KEITHLEY_2_CHAR_MODEL_LOOKUP = {
    "24": "SMU",
    "26": "SMU",
    "22": "PSU",
    "75": "DMM",
    "64": "SMU",
    "65": "SMU",
    "37": "SS",
}


####################################################################################################
# Public Functions
####################################################################################################
def check_for_update(package_name: str = PACKAGE_NAME) -> None:
    """Check for an update for the provided package.

    Args:
        package_name: Check for an update for the provided package.
    """
    starting_dir = os.getcwd()
    try:
        # Check for package updates, set the interval to zero to always check.
        with contextlib.redirect_stdout(None), contextlib.redirect_stderr(None):
            result = check_and_prompt(
                package_name, remind_delay=0, online_check_interval=0, mock_user_input="2"
            )
        if result.installed_version != result.pypi_version:
            print(
                f"\n\n\033[91mVersion {result.pypi_version} of "
                f"{package_name} is available on PyPI.\n"
                f"Version {result.installed_version} of "
                f"{package_name} is currently installed.\n\n"
                f"To upgrade {package_name} run the following command: "
                f"python -m pip install -U {package_name}\n\n\033[0m"
            )
    except FileNotFoundError:
        print(
            f"\n\n\033[91m{package_name} is not installed, "
            f"unable to check for updates.\n\n\033[0m"
        )
    except IndexError:
        print(
            f"\n\n\033[91m{package_name} is not available on PyPI, "
            f"unable to check for updates.\n\n\033[0m"
        )
    finally:
        # Reset the current working directory, the third-party package call changes it.
        os.chdir(starting_dir)


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
        visa_object: MessageBasedResource = visa.ResourceManager(  # type: ignore
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
    except Exception as error_1:  # noqa: BLE001
        if not retry_connection:
            message = f"Unable to establish a VISA connection to {resource_expression}"
            raise ConnectionError(message) from error_1
        time.sleep(60)  # wait 60 seconds and try again
        try:
            # noinspection PyTypeChecker
            visa_object: MessageBasedResource = visa.ResourceManager(  # type: ignore
                visa_library
            ).open_resource(resource_expression)
        # The broad except is because pyvisa_py can throw a base exception in the tcpip.py file
        except Exception as error_2:  # noqa: BLE001
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
        - The connection type, e.g. TCPIP.
        - The address of the device, an IP address, hostname, or
          string in the format ``model-serial``.

    Args:
        input_str: The string to check for a VISA resource expression.

    Returns:
        A tuple with the connection information parts.
    """
    retval: Optional[Tuple[str, str]] = None
    if input_str.upper().startswith("ASRL"):
        retval = ("SERIAL", input_str[4:].split("::", 1)[0])
    elif (match := VISA_RESOURCE_EXPRESSION_REGEX.search(input_str.upper())) is not None:
        match_groups_list = list(filter(None, match.groups()))
        for unneeded_part in ("INST", "INST0"):
            if unneeded_part in match_groups_list:
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
        retval = (match_groups_list[0].rstrip("0"), "-".join(match_groups_list[1:]).lstrip("0X"))
    return retval


# pylint: disable=too-many-branches
def get_model_series(model: str) -> str:  # noqa: PLR0912,C901,PLR0915
    """Get the series string from the full model number.

    Args:
        model: The full model string (ex. MSO58, LPD64).

    Returns:
        The model series string (ex. MSO5, LPD6).
    """
    valid_model_endings = {"A", "B", "C", "D", "LP"}
    model = model.strip().upper()
    model_parts = model.split("-")
    if len(model_parts) == 2:  # noqa: PLR2004
        model = model_parts[0]
    elif len(model_parts) == 3:  # noqa: PLR2004
        model = "MODEL" + model_parts[0]

    # find the model postscript if it exists and format it correctly
    model_postscript = ""
    if len(model_parts) > 1:
        for count, part in enumerate(model_parts):
            # avoid first model part as a postscript will likely never be in the beginning
            if count and len(part) > 1 and all(x.isalpha() for x in part):
                model_postscript = part.capitalize()

    if model.replace("MODEL", "").strip() in {x.upper() for x in SupportedModels.list_values()}:
        # These are special models that don't have differences between the
        # full model number and the model series.
        model_beginning = SupportedModels[model.replace("MODEL", "").strip()].value
        model_end = ""
    else:
        # Get any characters at the end of the model, e.g. 'B', 'LP', 'C'
        model_beginning = ""
        model_end = ""
        if re.search("[0-9]", model):  # if the model contains numbers
            model_end = re.split(r"\d+", model)[-1]  # split on the occurence of each number
        if len(model_end) == 1 and model_end not in valid_model_endings:
            model_end = ""
        model_beginning = ""
        if model_numbers := re.findall(r"\d+", model):
            model_number = int(model_numbers[0])
            if model.startswith("MODEL") or all(x.isdigit() for x in model.rstrip(model_end)):
                model_beginning_idx = model.find(model_numbers[0])
                model_beginning = model[model_beginning_idx:]
                if model_beginning[-1].isalpha():
                    model_beginning = model_beginning[:-1]
                # Convert the model into more specific driver names
                with contextlib.suppress(KeyError):
                    model_beginning = (
                        _KEITHLEY_2_CHAR_MODEL_LOOKUP[model_beginning[:2]] + model_beginning
                    )

                # This block of code can be enabled in the future if specific models need
                # to be combined, e.g. SMU2601B -> SMU2600B
                # Check if this is a specific, unique model series or if it needs to be a
                # more generic driver.
                # RELIC # if not model_postscript and (
                # RELIC #     any(
                # RELIC #         model_beginning.startswith(x)
                # RELIC #         for x in _MODEL_BEGINNINGS_TO_COMBINE
                # RELIC #     )
                # RELIC #     and model_beginning not in _SPECIFIC_DRIVER_SET
                # RELIC # ):
                # RELIC #     # Models without a postscript or which are not part of a
                # RELIC #     # specific driver need to use a more generic driver.
                # RELIC #     model_beginning = model_beginning[:-2] + "00"
            elif model.startswith("AWG52"):
                model_beginning += model[:-1] + "0"
            elif model_number >= 10_000:  # noqa: PLR2004
                if model.startswith("AFG"):
                    model_beginning += model[:5] + "K"
                else:
                    model_beginning += model[:4] + "0K"
            elif 1_000 <= model_number < 10_000:  # noqa: PLR2004
                model_beginning += model[:4] + "K"
            else:
                model_beginning += model[:4]
        elif len(model_parts) >= 2:  # noqa: PLR2004
            model_beginning = model.capitalize()
            model_beginning += model_parts[1]
        else:
            model_beginning = model_parts[0]

    model_series = model_beginning + model_end + model_postscript

    if model_series not in SupportedModels.list_values():
        warnings.warn(
            f'The "{model_series}" model series is not supported by {PACKAGE_NAME}', stacklevel=2
        )

    return model_series


def get_timestamp_string() -> str:
    """Return a string containing the current timestamp."""
    return str(datetime.datetime.now())[:-3]


def get_version(version_string: str) -> Version:
    """Get a Version object from a string.

    Args:
        version_string: The string containing the version to create.

    Returns:
        The Version object.
    """
    version_parts = version_string.split(".")
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
            raise
    return version


def get_visa_backend(visa_lib_path: str) -> str:
    """Create a human-readable VISA backend name based on the currently used VISA library path.

    Args:
        visa_lib_path: The path to the currently used VISA library.

    Returns:
        A string indicating the current VISA backend.
    """
    visa_name = ""

    system_visa_info = _VISA_SYSTEM_DETAILS
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
