"""Module containing constants and dataclasses for the tm_devices package."""
import re

from dataclasses import dataclass
from types import MappingProxyType
from typing import Final, List, Mapping, Optional, Protocol, runtime_checkable

import pyvisa as visa

from tm_devices.helpers.dataclass_mixins import (
    AsDictionaryMixin,
    AsDictionaryUseEnumNameUseCustEnumStrValueMixin,
)
from tm_devices.helpers.enums import ConnectionTypes, DeviceTypes, SupportedModels
from tm_devices.helpers.standalone_functions import validate_address


@runtime_checkable
@dataclass
class DataclassProtocol(Protocol):
    """A Protocol class to allow for type hinting things that accept generic dataclasses."""


@dataclass
class USBTMCConfiguration:
    """Dataclass for holding USBTMC configuration information.

    Each instance of the dataclass holds a Vendor ID and a Model ID to allow easier creation of
    USBTMC VISA resource expressions.
    """

    vendor_id: str
    """str: The hexadecimal Vendor ID used to create the USBTMC resource expression."""
    model_id: str
    """str: The hexadecimal Model ID used to create the USBTMC resource expression."""


class _ConfigEntryEnvStrMixin(AsDictionaryMixin):
    """Implements __str__ dunder method to format configuration information as an env variable.

    Handles nested classes through a prefix mapping stored in CONFIG_CLASS_STR_PREFIX_MAPPING.
    Changes to the mapping need to be reversible in the dm_config_parser which needs to bundle
    prefixed values under their own dictionary (to mimic the return type from the toml/yaml config
    files -> ``Dict[str, Union[str, int, Dict[str,...]]]``).

    So make sure to also modify DMConfigParser's _CONFIG_NESTED_DICT_MAPPING class property.
    """

    def __str__(self) -> str:
        """Return a single line of comma separated, key-value pairs for an environment variable."""
        ret_list: List[str] = []
        for key, val in self.to_dict(ignore_none=True).items():
            # must pull class type from actual value, not the to_dict()'s representation
            if (
                prefix := CONFIG_CLASS_STR_PREFIX_MAPPING.get(type(getattr(self, key)))
            ) is not None:
                if any(val.values()):
                    # still need to ignore the None values
                    str_pair = ",".join(
                        f"{prefix}{key2}={val2}" for key2, val2 in val.items() if val2 is not None
                    )
                else:
                    continue  # pragma: no cover
            else:
                str_pair = f"{key}={val}"
            ret_list.append(str_pair)
        return ",".join(ret_list)


@dataclass
class SerialConfig(AsDictionaryUseEnumNameUseCustEnumStrValueMixin, _ConfigEntryEnvStrMixin):
    """Serial configuration properties for connecting to a device over SERIAL (ASRL).

    Notes:
        - baud_rate: The baud rate controls the communication frequency.
            e.g. 9600
        - data_bits: The number of data bits in each character.
            One of [5, 6, 7, 8].
        - flow_control: Control for pausing/resuming data stream between slower devices.
            One of ``SerialConfig.FlowControl.[none|xon_xoff|dtr_dsr|rts_cts]``.
        - parity: Parity controls checksum bit (added to each data character) behavior.
            One of ``SerialConfig.Parity.[none|odd|even|mark|space]``.
        - stop_bits: Number of bits to use to indicate end of a character.
            One of ``SerialConfig.StopBits.[one|one_and_a_half|two]``.
        - end_input: Character(s) to indicate the end of a message transmission.
            One of ``SerialConfig.Termination.[termination_break|termination_char|last_bit|none]``.
    """

    FlowControl = visa.resources.serial.constants.ControlFlow
    """visa.resources.serial.constants.ControlFlow: Control flow for a serial device."""
    Parity = visa.resources.serial.constants.Parity
    """visa.resources.serial.constants.Parity: Parity type to use with every frame transmitted and received on a serial session.

    Used only for SERIAL (ASRL) resources.
    """  # noqa: E501
    StopBits = visa.resources.serial.constants.StopBits
    """visa.resources.serial.constants.StopBits: The number of stop bits that indicate the end of a frame on a serial resource.

    Used only for SERIAL (ASRL) resources.
    """  # noqa: E501
    Termination = visa.resources.serial.constants.SerialTermination
    """visa.resources.serial.constants.SerialTermination: The available methods for terminating a serial transfer."""  # noqa: E501
    baud_rate: Optional[int] = None
    """Optional[int]: The baud rate controls the communication frequency."""
    data_bits: Optional[int] = None
    """Optional[int]: The number of data bits in each character.

    One of ``[5, 6, 7, 8]``.
    """
    flow_control: Optional[FlowControl] = None
    """Optional[FlowControl]: Control for pausing/resuming data stream between slower devices.

    One of ``SerialConfig.FlowControl.[none|xon_xoff|dtr_dsr|rts_cts]``."""
    parity: Optional[Parity] = None
    """Optional[Parity]: Parity adds a checksum bit to each data character.
     Checksum bit enables the target device to determine whether the data was received correctly.

    One of ``SerialConfig.Parity.[none|odd|even|mark|space]``.
    """
    stop_bits: Optional[StopBits] = None
    """Optional[StopBits]: Number of bits to use to indicate end of a character.

    One of ``SerialConfig.StopBits.[one|one_and_a_half|two]``.
    """
    end_input: Optional[Termination] = None
    """Optional[Termination]: Character(s) to indicate the end of a message transmission.

    One of ``SerialConfig.Termination.[termination_break|termination_char|last_bit|none]``.
    """

    def __post_init__(self) -> None:
        """Convert from string to expected type and translate enum string names into the values."""
        if isinstance(self.baud_rate, str):
            self.baud_rate = int(self.baud_rate)
        if isinstance(self.data_bits, str):
            self.data_bits = int(self.data_bits)
        if isinstance(self.flow_control, str):
            self.flow_control = getattr(self.FlowControl, self.flow_control)
        if isinstance(self.parity, str):
            self.parity = getattr(self.Parity, self.parity)
        if isinstance(self.stop_bits, str):
            self.stop_bits = getattr(self.StopBits, self.stop_bits)
        if isinstance(self.end_input, str):
            self.end_input = getattr(self.Termination, self.end_input)


@dataclass(frozen=True)
class DeviceConfigEntry(AsDictionaryUseEnumNameUseCustEnumStrValueMixin, _ConfigEntryEnvStrMixin):
    """Dataclass for holding configuration information for a single device."""

    device_type: DeviceTypes
    """tm_devices.helpers.DeviceTypes: The specific device type defined in the config entry."""
    address: str
    """str: The address used to connect to the device.

    Notes:
        - TCPIP: IP address or the hostname.
        - SOCKET: IP address or the hostname (must define `lan_port` field).
        - REST_API: IP address or the hostname (must define `lan_port` field).
        - SERIAL/ASRL: serial COM port number.
        - USB: use expression format f"{model}-{serial_number}" (ex: "MSO24-ABC0123").
    """
    connection_type: ConnectionTypes = ConnectionTypes.TCPIP
    """tm_devices.helpers.ConnectionTypes: The specific type of connection defined in the config entry."""  # noqa: E501
    alias: Optional[str] = None
    """Optional[str]: An optional key/name used to retrieve this devices from the DeviceManager."""
    lan_port: Optional[int] = None
    """Optional[int]: The port number to connect on, used for SOCKET/REST_API connections."""
    serial_config: Optional[SerialConfig] = None
    """Optional[SerialConfig]: Serial configuration properties for connecting to a device over SERIAL (ASRL)."""  # noqa: E501
    device_driver: Optional[str] = None
    """Optional[str]: The name of the Python driver to use for the device (required for connection_type=REST_API, ignored otherwise)"""  # noqa: E501

    # pylint: disable=too-many-branches
    def __post_init__(self) -> None:  # noqa: PLR0912,C901
        """Validate data after creation.

        Raises:
            TypeError: Indicates a bad enum type.
            ValueError: Indicates a bad input value.
        """
        # manually handle type conversion from parsing from config file
        # (this is the correct way to edit the frozen data)
        if self.lan_port is not None and isinstance(self.lan_port, str):
            object.__setattr__(self, "lan_port", int(self.lan_port))
        if not isinstance(self.address, str):  # pyright: ignore
            object.__setattr__(self, "address", str(self.address))

        # Validate the connection and interface types
        try:
            # device and connections are inside this try clause to raise a TypeError on bad values.
            # Convert them from strings (parsed from config/env) to appropriate enum value.
            if not isinstance(self.device_type, DeviceTypes):  # pyright: ignore
                object.__setattr__(self, "device_type", DeviceTypes(self.device_type))
            if not isinstance(self.connection_type, ConnectionTypes):  # pyright: ignore
                object.__setattr__(self, "connection_type", ConnectionTypes(self.connection_type))

            # While a SerialConfig is not frozen, if not created here then it cannot be added later.
            # A serial_config must be created if the connection_type is SERIAL (ASRL).
            if self.connection_type == ConnectionTypes.SERIAL and self.serial_config is None:
                object.__setattr__(self, "serial_config", SerialConfig())

            if self.device_type not in VALID_DEVICE_CONNECTION_TYPES:
                msg = (
                    f"{self.device_type.name} is not a valid device type. Valid device types: "
                    f"{VALID_DEVICE_CONNECTION_TYPES}"
                )
                raise TypeError(msg)
            if self.connection_type not in VALID_DEVICE_CONNECTION_TYPES[self.device_type]:
                msg = (
                    f"{self.connection_type.name} is not a valid "
                    f"{self.device_type} connection type. Valid connection types: "
                    f"{[x.name for x in VALID_DEVICE_CONNECTION_TYPES[self.device_type]]}"
                )
                raise TypeError(msg)
        except ValueError as error:
            # this is from an invalid enum name
            raise TypeError(*error.args)  # noqa: TRY200,B904

        # Check if a specific device driver is needed to be specified
        if self.connection_type == ConnectionTypes.REST_API and self.device_driver is None:
            msg = (
                f'Device configuration entry "{self}" specified a '
                f"REST_API connection without providing the Python device driver name to use."
            )
            raise ValueError(msg)

        if self.connection_type == ConnectionTypes.SOCKET and self.lan_port is None:
            msg = (
                f'Device configuration entry "{self}" specified a '
                f"socket connection without a port number."
            )
            raise ValueError(msg)

        # validate address
        try:
            if self.connection_type in [
                ConnectionTypes.TCPIP,
                ConnectionTypes.SOCKET,
                ConnectionTypes.REST_API,
            ]:
                validate_address(self.address)
            elif (  # pylint: disable=too-many-boolean-expressions
                (self.connection_type == ConnectionTypes.USB and "-" not in self.address)
                or (self.connection_type == ConnectionTypes.SERIAL and not self.address.isdigit())
                or (
                    self.connection_type == ConnectionTypes.GPIB
                    and not (self.address.isdigit() and 1 <= int(self.address) <= MAX_GPIB_ADDRESS)
                )
            ):
                raise ValueError
        except ValueError as exc:
            msg = f"""Found invalid value of `address={self.address}`
        Must provide an valid address format for the `connection_type={self.connection_type.value}':
            TCPIP: IP address or the hostname.
            SOCKET: IP address or the hostname (must define `lan_port` field).
            REST_API: IP address or the hostname (must define `lan_port` field).
            SERIAL/ASRL: serial COM port number.
            GPIB: address number (1 <= n <= 30).
            USB: use expression format "<model>-<serial_number>" (ex: "MSO24-ABC0123").
                """
            raise ValueError(msg) from exc

        # Validate serial config
        if self.serial_config is not None:
            # make sure serial attributes with integer input are in valid range
            if (
                self.serial_config.baud_rate is not None
                and self.serial_config.baud_rate not in VALID_SERIAL_BAUD
            ):
                msg = (
                    f"Unexpected baud rate of {self.serial_config.baud_rate}, "
                    f"must be in {sorted(VALID_SERIAL_BAUD)}"
                )
                raise ValueError(msg)
            if (
                self.serial_config.data_bits is not None
                and self.serial_config.data_bits not in VALID_SERIAL_DATA_BITS
            ):
                msg = (
                    f"Unexpected data bits of {self.serial_config.data_bits}, "
                    f"must be in {sorted(VALID_SERIAL_DATA_BITS)}"
                )
                raise ValueError(msg)

    def get_address_expression(self) -> str:
        """Return an address expression.

        This is not the resource expression, it is used to help catch duplicate addresses.
        """
        return (
            self.connection_type.value + " " + self.address + ""
            if self.lan_port is None
            else f":{self.lan_port}"
        )

    def get_visa_resource_expression(self) -> str:
        """Construct the VISA resource expression for the device.

        Example visa expressions:

            - TCPIP0::MSO58-3000260::instr0::INSTR
            - USB0::0x0699::0x0522::3000260::INSTR
            - TCPIP0::192.168.0.1::4000::SOCKET
            - ASRL3::INSTR  (serial on COM port 3)

        Returns:
            A string containing the VISA resource expression.

        Raises:
            NotImplementedError: Indicates that the USBTMC lookup dictionary needs to be
                updated to support the current device.
            ValueError: Indicates that the connection type specified in the config is not valid.
        """
        # If USBTMC for the address check if connected
        if self.connection_type == ConnectionTypes.USB:
            full_model, serial = self.address.split("-", 1)
            # local import here to avoid circular imports
            # pylint: disable=import-outside-toplevel,cyclic-import
            from tm_devices.helpers.functions import get_model_series

            model_series = get_model_series(full_model)
            try:
                usbtmc_config = USB_MODEL_ID_LOOKUP[model_series]

                # This commented out block of code can help deal with devices where the specific
                # model number is the USBTMC model_id but the Python driver is shared between
                # multiple model numbers. It is currently not needed, if this is needed in the
                # future this code block can be uncommented.
                # RELIC # if usbtmc_config.model_id == _USBTMC_UNKNOWN_MODEL:
                # RELIC #     usbtmc_config = USBTMCConfiguration(
                # RELIC #         vendor_id=usbtmc_config.vendor_id,
                # RELIC #         model_id="0x" + (full_model.split(" ", maxsplit=1)[-1])[:4],
                # RELIC #     )

                resource_expr = (
                    f"USB0::{usbtmc_config.vendor_id}::{usbtmc_config.model_id}::{serial}::0::INSTR"
                )
            except KeyError as exc:
                msg = (
                    f"USBTMC model ID has not been configured for the "
                    f"{model_series} model series\nconfig = {self}"
                )
                raise NotImplementedError(msg) from exc
        elif self.connection_type == ConnectionTypes.SOCKET:
            resource_expr = f"TCPIP0::{self.address}::{self.lan_port}::SOCKET"
        elif self.connection_type == ConnectionTypes.TCPIP:
            resource_expr = f"TCPIP0::{self.address}::inst0::INSTR"
        elif self.connection_type == ConnectionTypes.GPIB:
            resource_expr = f"GPIB0::{self.address}::INSTR"
        elif self.connection_type == ConnectionTypes.SERIAL:
            resource_expr = f"ASRL{self.address}::INSTR"
        elif self.connection_type == ConnectionTypes.MOCK:  # pragma: no cover
            resource_expr = f"MOCK0::{self.address}::INSTR"
        else:
            msg = (
                f"{self.connection_type.value} is not a valid connection "
                f"type for a VISA resource."
            )
            raise ValueError(msg)
        return resource_expr


@dataclass
class DMConfigOptions(AsDictionaryMixin):
    """Device Management Configuration options."""

    standalone: Optional[bool] = None
    """Optional[bool]: An option indicating to use PyVISA-py's pure Python VISA backend."""
    setup_cleanup: Optional[bool] = None
    """Optional[bool]: An option indicating to run a device's ``cleanup()`` method when opening the connection."""  # noqa: E501
    teardown_cleanup: Optional[bool] = None
    """Optional[bool]: An option indicating to run a device's ``cleanup()`` method when closing the connection."""  # noqa: E501
    verbose_mode: Optional[bool] = None
    """Optional[bool]: A verbosity flag to turn on more printouts to stdout."""
    verbose_visa: Optional[bool] = None
    """Optional[bool]: A verbosity flag to enable extremely verbose VISA logging to stdout."""
    retry_visa_connection: Optional[bool] = None
    """Optional[bool]: A flag to enable retrying the first VISA connection attempt."""

    def __str__(self) -> str:
        """Complete config entry line for an environment variable."""
        return ",".join(
            [
                opt_key.upper()
                for opt_key, opt_val in self.to_dict(ignore_none=True).items()
                if opt_val
            ]
        )


###############################################################################
#                                CONSTANTS
###############################################################################
# don't include this in the __init__
MAX_GPIB_ADDRESS = 30
# don't include this in the __init__
CONFIG_CLASS_STR_PREFIX_MAPPING: Final = MappingProxyType({SerialConfig: "serial_"})
# don't include this in the __init__
VALID_SERIAL_BAUD: Final = frozenset(
    [
        300,
        600,
        1200,
        2400,
        4800,
        9600,
        14400,
        19200,
        28800,
        31250,
        38400,
        57600,
        115200,
    ]
)
# don't include this in the __init__
VALID_SERIAL_DATA_BITS: Final = frozenset([5, 6, 7, 8])

PYVISA_PY_BACKEND: Final = "@py"
"""str: Constant string which indicates to use the pure Python PyVISA-py backend when creating VISA connections."""  # noqa: E501

SYSTEM_DEFAULT_VISA_BACKEND: Final = ""
"""str: Constant string which indicates to use the current system's default VISA backend when creating VISA connections."""  # noqa: E501

PACKAGE_NAME: Final = "tm_devices"
"""str: Constant string with the name of this package."""

VISA_RESOURCE_EXPRESSION_REGEX: Final = re.compile(
    r"^(\w+)(?:::0X\w+)?::([-.\w]+)(?:::(\w+))?(?:::INST0?)?::INSTR?$"
)
"""re.Pattern[str]: A regex pattern used to capture pieces of VISA resource expressions."""

UNIT_TEST_TIMEOUT: Final = 50
"""int: The VISA timeout value to use during unit tests, in milliseconds."""

VALID_DEVICE_CONNECTION_TYPES: Final = MappingProxyType(
    {
        DeviceTypes.AFG: (
            ConnectionTypes.TCPIP,
            ConnectionTypes.USB,
            ConnectionTypes.SOCKET,
            ConnectionTypes.SERIAL,
            ConnectionTypes.GPIB,
        ),
        DeviceTypes.AWG: (
            ConnectionTypes.TCPIP,
            ConnectionTypes.USB,
            ConnectionTypes.SOCKET,
            ConnectionTypes.SERIAL,
            ConnectionTypes.GPIB,
        ),
        DeviceTypes.DAQ: (
            ConnectionTypes.TCPIP,
            ConnectionTypes.USB,
            ConnectionTypes.GPIB,
            ConnectionTypes.SERIAL,
        ),
        DeviceTypes.DMM: (
            ConnectionTypes.TCPIP,
            ConnectionTypes.USB,
            ConnectionTypes.SOCKET,
            ConnectionTypes.SERIAL,
            ConnectionTypes.GPIB,
        ),
        DeviceTypes.MT: (ConnectionTypes.REST_API,),
        DeviceTypes.PSU: (
            ConnectionTypes.TCPIP,
            ConnectionTypes.USB,
            ConnectionTypes.SOCKET,
            ConnectionTypes.SERIAL,
            ConnectionTypes.GPIB,
        ),
        DeviceTypes.SCOPE: (
            ConnectionTypes.TCPIP,
            ConnectionTypes.USB,
            ConnectionTypes.SOCKET,
            ConnectionTypes.SERIAL,
            ConnectionTypes.GPIB,
            ConnectionTypes.MOCK,
        ),
        DeviceTypes.SMU: (
            ConnectionTypes.TCPIP,
            ConnectionTypes.USB,
            ConnectionTypes.SOCKET,
            ConnectionTypes.SERIAL,
            ConnectionTypes.GPIB,
        ),
        DeviceTypes.SS: (
            ConnectionTypes.TCPIP,
            ConnectionTypes.USB,
            ConnectionTypes.SOCKET,
            ConnectionTypes.GPIB,
        ),
    }
)
"""Dict[tm_devices.helpers.DeviceTypes, Tuple[tm_devices.helpers.ConnectionTypes, ...]]: Mapping of each device type to its supported connection types.

Any additions to this class need to be added to the :py:obj:`~tm_devices.helpers.enums.DeviceTypes`
enum as well.
"""  # noqa: E501

# USBTMC configuration defines
_TEKTRONIX_USBTMC_VENDOR_ID: Final = "0x0699"
_KEITHLEY_USBTMC_VENDOR_ID: Final = "0x05E6"
USB_MODEL_ID_LOOKUP: Final[Mapping[str, USBTMCConfiguration]] = MappingProxyType(
    {
        SupportedModels.MDO3K.value: USBTMCConfiguration(
            vendor_id=_TEKTRONIX_USBTMC_VENDOR_ID, model_id="0x0408"
        ),
        SupportedModels.MSO2.value: USBTMCConfiguration(
            vendor_id=_TEKTRONIX_USBTMC_VENDOR_ID, model_id="0x0105"
        ),
        SupportedModels.MSO4.value: USBTMCConfiguration(
            vendor_id=_TEKTRONIX_USBTMC_VENDOR_ID, model_id="0x0527"
        ),
        SupportedModels.MSO5.value: USBTMCConfiguration(
            vendor_id=_TEKTRONIX_USBTMC_VENDOR_ID, model_id="0x0522"
        ),
        SupportedModels.MSO5B.value: USBTMCConfiguration(
            vendor_id=_TEKTRONIX_USBTMC_VENDOR_ID, model_id="0x0522"
        ),
        SupportedModels.MSO5LP.value: USBTMCConfiguration(
            vendor_id=_TEKTRONIX_USBTMC_VENDOR_ID, model_id="0x0529"
        ),
        SupportedModels.MSO6.value: USBTMCConfiguration(
            vendor_id=_TEKTRONIX_USBTMC_VENDOR_ID, model_id="0x0528"
        ),
        SupportedModels.MSO6B.value: USBTMCConfiguration(
            vendor_id=_TEKTRONIX_USBTMC_VENDOR_ID, model_id="0x0530"
        ),
        SupportedModels.LPD6.value: USBTMCConfiguration(
            vendor_id=_TEKTRONIX_USBTMC_VENDOR_ID, model_id="0x052F"
        ),
        SupportedModels.AFG3K.value: USBTMCConfiguration(
            vendor_id=_TEKTRONIX_USBTMC_VENDOR_ID, model_id="0x0345"
        ),
        SupportedModels.SMU2450.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2450"
        ),
        SupportedModels.SMU2460.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2460"
        ),
        SupportedModels.SMU2461.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2461"
        ),
        SupportedModels.SMU2470.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2470"
        ),
        SupportedModels.SMU2601A.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2601"
        ),
        SupportedModels.SMU2602A.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2602"
        ),
        SupportedModels.SMU2604A.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2604"
        ),
        SupportedModels.SMU2611A.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2611"
        ),
        SupportedModels.SMU2612A.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2612"
        ),
        SupportedModels.SMU2614A.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2614"
        ),
        SupportedModels.SMU2634A.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2634"
        ),
        SupportedModels.SMU2635A.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2635"
        ),
        SupportedModels.SMU2636A.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2636"
        ),
        SupportedModels.SMU2601B.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2601"
        ),
        SupportedModels.SMU2602B.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2602"
        ),
        SupportedModels.SMU2604B.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2604"
        ),
        SupportedModels.SMU2606B.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2606"
        ),
        SupportedModels.SMU2611B.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2611"
        ),
        SupportedModels.SMU2612B.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2612"
        ),
        SupportedModels.SMU2614B.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2614"
        ),
        SupportedModels.SMU2634B.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2634"
        ),
        SupportedModels.SMU2635B.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2635"
        ),
        SupportedModels.SMU2636B.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2636"
        ),
        SupportedModels.PSU2200.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2200"
        ),
        SupportedModels.PSU2220.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2220"
        ),
        SupportedModels.PSU2230.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2230"
        ),
        SupportedModels.PSU2231.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2231"
        ),
        SupportedModels.PSU2231A.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2231"
        ),
        SupportedModels.PSU2280.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2280"
        ),
        SupportedModels.PSU2281.value: USBTMCConfiguration(
            vendor_id=_KEITHLEY_USBTMC_VENDOR_ID, model_id="0x2281"
        ),
        SupportedModels.AWG5200.value: USBTMCConfiguration(
            vendor_id=_TEKTRONIX_USBTMC_VENDOR_ID, model_id="0x0503"
        ),
        SupportedModels.AWG70KA.value: USBTMCConfiguration(
            vendor_id=_TEKTRONIX_USBTMC_VENDOR_ID, model_id="0x0503"
        ),
        SupportedModels.AWG70KB.value: USBTMCConfiguration(
            vendor_id=_TEKTRONIX_USBTMC_VENDOR_ID, model_id="0x0503"
        ),
    }
)
"""Dict[str, tm_devices.helpers.USBTMCConfiguration]: Mapping of model USBTMC info."""
