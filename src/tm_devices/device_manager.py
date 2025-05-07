# pylint: disable=too-many-lines
"""Device manager module."""

from __future__ import annotations

import contextlib
import inspect
import json
import logging
import os
import pathlib
import socket
import warnings

from types import FrameType, MappingProxyType, TracebackType
from typing import cast, Dict, Mapping, Optional, Tuple, Type, TYPE_CHECKING, Union

from typing_extensions import TypeVar

from tm_devices.components import DMConfigParser
from tm_devices.drivers._device_driver_mapping import (
    _DEVICE_DRIVER_MODEL_STR_MAPPING,  # pyright: ignore[reportPrivateUsage]
)
from tm_devices.drivers.afgs.afg import AFG
from tm_devices.drivers.awgs.awg import AWG
from tm_devices.drivers.data_acquisition_systems.data_acquisition_system import (
    DataAcquisitionSystem,
)
from tm_devices.drivers.device import Device
from tm_devices.drivers.digital_multimeters.digital_multimeter import DigitalMultimeter
from tm_devices.drivers.margin_testers.margin_tester import MarginTester
from tm_devices.drivers.power_supplies.power_supply import PowerSupplyUnit
from tm_devices.drivers.scopes.scope import Scope
from tm_devices.drivers.source_measure_units.source_measure_unit import SourceMeasureUnit
from tm_devices.drivers.systems_switches.systems_switch import SystemsSwitch
from tm_devices.helpers import (
    AliasDict,
    check_for_update,
    configure_logging,
    ConnectionTypes,
    create_visa_connection,
    detect_visa_resource_expression,
    DeviceConfigEntry,
    DeviceTypes,
    DMConfigOptions,
    get_model_series,
    PACKAGE_NAME,
    PYVISA_PY_BACKEND,
    SerialConfig,
    Singleton,
)

with warnings.catch_warnings():
    warnings.simplefilter("ignore", UserWarning)
    import pyvisa as visa

    from pyvisa_py.protocols.rpc import RPCError  # pyright: ignore[reportMissingTypeStubs]


if TYPE_CHECKING:
    from pyvisa.resources import MessageBasedResource
    from typing_extensions import Self

    # noinspection PyUnresolvedReferences
    from tm_devices.driver_mixins.device_control.pi_control import PIControl

####################################################################################################
# Type Aliases
####################################################################################################
AFGAlias = TypeVar("AFGAlias", bound=AFG, default=AFG)
"""An alias to a specific Arbitrary Function Generator Python driver."""
AWGAlias = TypeVar("AWGAlias", bound=AWG, default=AWG)
"""An alias to a specific Arbitrary Waveform Generator Python driver."""
DataAcquisitionSystemAlias = TypeVar(
    "DataAcquisitionSystemAlias", bound=DataAcquisitionSystem, default=DataAcquisitionSystem
)
"""An alias to a specific Data Acquisition System Python driver."""
DigitalMultimeterAlias = TypeVar(
    "DigitalMultimeterAlias", bound=DigitalMultimeter, default=DigitalMultimeter
)
"""An alias to a specific Digital Multimeter Python driver."""
ScopeAlias = TypeVar("ScopeAlias", bound=Scope, default=Scope)
"""An alias to a specific Scope driver."""
MarginTesterAlias = TypeVar("MarginTesterAlias", bound=MarginTester, default=MarginTester)
"""An alias to a specific Margin Tester Python driver."""
PowerSupplyUnitAlias = TypeVar(
    "PowerSupplyUnitAlias", bound=PowerSupplyUnit, default=PowerSupplyUnit
)
"""An alias to a specific Power Supply Unit Python driver."""
SourceMeasureUnitAlias = TypeVar(
    "SourceMeasureUnitAlias", bound=SourceMeasureUnit, default=SourceMeasureUnit
)
"""An alias to a specific Source Measure Unit Python driver."""
SystemsSwitchAlias = TypeVar("SystemsSwitchAlias", bound=SystemsSwitch, default=SystemsSwitch)
"""An alias to a specific Systems Switch Python driver."""
UnsupportedDeviceAlias = TypeVar("UnsupportedDeviceAlias", bound=Device, default=Device)
"""An alias to a custom device driver for an unsupported device type."""

_logger: logging.Logger = logging.getLogger(__name__)


####################################################################################################
# DeviceManager class
####################################################################################################
# pylint: disable=too-many-public-methods,too-many-instance-attributes
class DeviceManager(metaclass=Singleton):
    """The manager for all devices.

    Once instantiated, this class creates and manages connections to all devices.

    This class is a singleton, meaning only one instance can ever be created. Any subsequent
    instantiation attempts will return a pointer to the original instance.
    """

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        verbose: bool = True,
        config_options: Optional[DMConfigOptions] = None,
        external_device_drivers: Optional[Mapping[str, Type[Device]]] = None,
    ) -> None:
        """Create the instance of the DeviceManager.

        Args:
            verbose: A boolean indicating if verbose output should be printed. This flag cascades
                down to all connected devices. Setting it to False **will not** remove all printouts
                to stdout. To remove all console output, use
                [`configure_logging()`][tm_devices.configure_logging] before instantiating the
                DeviceManager.
            config_options: An optional set of configuration options to use
                (updates the current configuration options).
            external_device_drivers: An optional dict for passing in additional device drivers.
        """
        self._suppress_protection = False
        # Set up the DeviceManager
        self.__is_open = False
        self.__verbose_visa = False
        self.__devices: Dict[str, Device] = AliasDict()
        self._external_device_drivers = external_device_drivers
        # initialize for __set_options()
        self.__verbose: bool = NotImplemented
        self.__teardown_cleanup_enabled: bool = NotImplemented
        self.__setup_cleanup_enabled: bool = NotImplemented
        self.__disable_command_verification: bool = NotImplemented
        self.__visa_library: str = NotImplemented
        self.__default_visa_timeout: int = NotImplemented

        # Create the config
        self.__config = DMConfigParser()
        if config_options is not None:
            self.__config.update_options(config_options)
        if self.__config.options.check_for_updates:  # pragma: no cover
            check_for_update()
        # actually populate the options
        self.__set_options(verbose)

        # Pass in the options from the config file or environment variable to the logger
        logging_options = {
            key: value
            for key, value in self.__config.options.to_dict(ignore_none=True).items()
            if key.startswith("log_")
        }
        configure_logging(**logging_options)

        self.open()

    def __del__(self) -> None:
        """Delete the instance of the DeviceManger."""
        if self.__is_open:
            self.close()

    def __enter__(self) -> Self:
        """Provide access to the DeviceManager class instance.

        This and the __exit__ method allow this class to be used as a Context Manager.
        """
        if not self.__is_open:
            self.open()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        """Handle exiting the context by closing down the DeviceManager.

        This and the __enter__ method allow this class to be used as a Context Manager.
        """
        if self.__is_open:
            self.close()

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def default_visa_timeout(self) -> int:
        """Return the default VISA timeout value."""
        return self.__default_visa_timeout

    @default_visa_timeout.setter
    def default_visa_timeout(self, value: int) -> None:
        """Set the default VISA timeout value."""
        self.__config.options.default_visa_timeout = value
        self.__default_visa_timeout = value

    @property
    def devices(self) -> Mapping[str, Device]:
        """Return the dictionary of devices."""
        return MappingProxyType(self.__devices)

    @property
    def disable_command_verification(self) -> bool:
        """Indicate if command verification is disabled for all devices."""
        return self.__disable_command_verification

    @disable_command_verification.setter
    def disable_command_verification(self, value: bool) -> None:
        """Set the property which will disable (or enable) command verification for all devices."""
        self.__protect_access()
        self.__config.options.disable_command_verification = value
        self.__disable_command_verification = value
        for device in self.__devices.values():
            device.enable_verification = not value

    @property
    def is_open(self) -> bool:
        """Indicate if the DeviceManager has closed all device connections."""
        return self.__is_open

    @property
    def teardown_cleanup_enabled(self) -> bool:
        """Indicate if cleanup at teardown is enabled for devices."""
        return self.__teardown_cleanup_enabled

    @teardown_cleanup_enabled.setter
    def teardown_cleanup_enabled(self, value: bool) -> None:
        """Set the property which can enable cleanup on teardown of devices."""
        self.__config.options.teardown_cleanup = value
        self.__teardown_cleanup_enabled = value

    @property
    def setup_cleanup_enabled(self) -> bool:
        """Indicate if cleanup at setup is enabled for devices."""
        return self.__setup_cleanup_enabled

    @setup_cleanup_enabled.setter
    def setup_cleanup_enabled(self, value: bool) -> None:
        """Set the property which can enable cleanup on setup of devices."""
        self.__config.options.setup_cleanup = value
        self.__setup_cleanup_enabled = value

    @property
    def verbose(self) -> bool:
        """Return the verbosity setting of the DeviceManager."""
        return self.__verbose

    @verbose.setter
    def verbose(self, value: bool) -> None:
        """Set the verbosity of the DeviceManager."""
        self.__config.options.verbose_mode = value
        self.__verbose = value

    @property
    def verbose_visa(self) -> bool:
        """Return the VISA verbosity setting of the DeviceManager."""
        return self.__verbose_visa

    @verbose_visa.setter
    def verbose_visa(self, value: bool) -> None:
        """Set the VISA verbosity setting of the DeviceManager."""
        if value:
            visa.log_to_screen()
        else:
            for handler in visa.logger.handlers.copy():
                if "DEBUG" in str(handler) and (
                    isinstance(handler, logging.StreamHandler)
                    and not isinstance(handler, logging.FileHandler)
                ):
                    visa.logger.removeHandler(handler)  # pyright: ignore[reportUnknownArgumentType]
        self.__config.options.verbose_visa = value
        self.__verbose_visa = value

    @property
    def visa_library(self) -> str:
        """Return the currently selected VISA library."""
        return self.__visa_library

    @visa_library.setter
    def visa_library(self, value: str) -> None:
        """Set the VISA library to use when creating new device connections."""
        self.__config.options.standalone = value == PYVISA_PY_BACKEND
        self.__visa_library = value

    ################################################################################################
    # Public Methods
    ################################################################################################
    def add_afg(
        self,
        address: str,
        *,
        alias: Optional[str] = None,
        connection_type: Optional[str] = None,
        port: Optional[int] = None,
        serial_config: Optional[SerialConfig] = None,
        gpib_board_number: Optional[int] = None,
    ) -> AFGAlias:
        """Add an Arbitrary Function Generator to the DeviceManager.

        Args:
            address: The address of the AFG, either an IP address or hostname. If the connection
                     type is ``"USB"`` then the address must be specified as ``"<model>-<serial>"``.
            alias: An optional alias to use to refer to the AFG. If no alias is provided,
                   the device type and number can be used to access the AFG instead.
            connection_type: The type of connection to use for VISA, defaults to TCPIP, not needed
                when the address is a visa resource expression since the connection type is parsed
                from the address string.
            port: The port to use when creating a socket connection.
            serial_config: Serial connection settings, only needed when connection_type="SERIAL".
            gpib_board_number: The GPIB board number (also referred to as a controller) to be used
                when making a GPIB connection (defaults to 0).

        Returns:
            The Arbitrary Function Generator device driver.
        """
        self.__protect_access()
        return cast(
            "AFGAlias",
            self._add_device(
                device_type=DeviceTypes.AFG.value,
                address=address,
                alias=alias,
                connection_type=connection_type,
                port=port,
                serial_config=serial_config,
                gpib_board_number=gpib_board_number,
            ),
        )

    def add_awg(
        self,
        address: str,
        *,
        alias: Optional[str] = None,
        connection_type: Optional[str] = None,
        port: Optional[int] = None,
        serial_config: Optional[SerialConfig] = None,
        gpib_board_number: Optional[int] = None,
    ) -> AWGAlias:
        """Add an Arbitrary Waveform Generator to the DeviceManager.

        Args:
            address: The address of the AWG, either an IP address or hostname. If the connection
                     type is ``"USB"`` then the address must be specified as ``"<model>-<serial>"``.
            alias: An optional alias to use to refer to the AWG. If no alias is provided,
                   the device type and number can be used to access the AWG instead.
            connection_type: The type of connection to use for VISA, defaults to TCPIP, not needed
                when the address is a visa resource expression since the connection type is parsed
                from the address string.
            port: The port to use when creating a socket connection.
            serial_config: Serial connection settings, only needed when connection_type="SERIAL".
            gpib_board_number: The GPIB board number (also referred to as a controller) to be used
                when making a GPIB connection (defaults to 0).

        Returns:
            The Arbitrary Waveform Generator device driver.
        """
        self.__protect_access()
        return cast(
            "AWGAlias",
            self._add_device(
                device_type=DeviceTypes.AWG.value,
                address=address,
                alias=alias,
                connection_type=connection_type,
                port=port,
                serial_config=serial_config,
                gpib_board_number=gpib_board_number,
            ),
        )

    def add_daq(
        self,
        address: str,
        *,
        alias: Optional[str] = None,
        connection_type: Optional[str] = None,
        port: Optional[int] = None,
        serial_config: Optional[SerialConfig] = None,
        gpib_board_number: Optional[int] = None,
    ) -> DataAcquisitionSystemAlias:
        """Add a Data Acquisition System to the DeviceManager.

        Args:
            address: The address of the DAQ, either an IP address or hostname. If the connection
                     type is ``"USB"`` then the address must be specified as ``"<model>-<serial>"``.
            alias: An optional alias to use to refer to the DAQ. If no alias is provided,
                   the device type and number can be used to access the DAQ instead.
            connection_type: The type of connection to use for VISA, defaults to TCPIP, not needed
                when the address is a visa resource expression since the connection type is parsed
                from the address string.
            port: The port to use when creating a socket connection.
            serial_config: Serial connection settings, only needed when connection_type="SERIAL".
            gpib_board_number: The GPIB board number (also referred to as a controller) to be used
                when making a GPIB connection (defaults to 0).

        Returns:
            The Data Acquisition System device driver.
        """
        self.__protect_access()
        return cast(
            "DataAcquisitionSystemAlias",
            self._add_device(
                device_type=DeviceTypes.DAQ.value,
                address=address,
                alias=alias,
                connection_type=connection_type,
                port=port,
                serial_config=serial_config,
                gpib_board_number=gpib_board_number,
            ),
        )

    def add_dmm(
        self,
        address: str,
        *,
        alias: Optional[str] = None,
        connection_type: Optional[str] = None,
        port: Optional[int] = None,
        serial_config: Optional[SerialConfig] = None,
        gpib_board_number: Optional[int] = None,
    ) -> DigitalMultimeterAlias:
        """Add a Digital Multimeter to the DeviceManager.

        Args:
            address: The address of the DMM, either an IP address or hostname. If the connection
                     type is ``"USB"`` then the address must be specified as ``"<model>-<serial>"``.
            alias: An optional alias to use to refer to the DMM. If no alias is provided,
                   the device type and number can be used to access the AWG instead.
            connection_type: The type of connection to use for VISA, defaults to TCPIP, not needed
                when the address is a visa resource expression since the connection type is parsed
                from the address string.
            port: The port to use when creating a socket connection.
            serial_config: Serial connection settings, only needed when connection_type="SERIAL".
            gpib_board_number: The GPIB board number (also referred to as a controller) to be used
                when making a GPIB connection (defaults to 0).

        Returns:
            The Digital Multimeter device driver.
        """
        self.__protect_access()
        return cast(
            "DigitalMultimeterAlias",
            self._add_device(
                device_type=DeviceTypes.DMM.value,
                address=address,
                alias=alias,
                connection_type=connection_type,
                port=port,
                serial_config=serial_config,
                gpib_board_number=gpib_board_number,
            ),
        )

    def add_mt(
        self,
        address: str,
        device_driver: str,
        *,
        alias: Optional[str] = None,
        port: Optional[int] = None,
    ) -> MarginTesterAlias:
        """Add a Margin Tester to the DeviceManager.

        Args:
            address: The address of the Margin Tester, either an IP address or hostname.
            device_driver: A string indicating the specific Python device driver to use.
            alias: An optional alias to use to refer to the Margin Tester. If no alias is provided,
                   the device type and number can be used to access the Margin Tester instead.
            port: The port to use when creating the connection.

        Returns:
            The Margin Tester device driver.
        """
        self.__protect_access()
        return cast(
            "MarginTesterAlias",
            self._add_device(
                device_type=DeviceTypes.MT.value,
                address=address,
                device_driver=device_driver,
                alias=alias,
                connection_type=ConnectionTypes.REST_API.value,
                port=port,
            ),
        )

    def add_psu(
        self,
        address: str,
        *,
        alias: Optional[str] = None,
        connection_type: Optional[str] = None,
        port: Optional[int] = None,
        serial_config: Optional[SerialConfig] = None,
        gpib_board_number: Optional[int] = None,
    ) -> PowerSupplyUnitAlias:
        """Add a Power Supply Unit to the DeviceManager.

        Args:
            address: The address of the PSU, either an IP address or hostname. If the connection
                     type is ``"USB"`` then the address must be specified as ``"<model>-<serial>"``.
            alias: An optional alias to use to refer to the PSU. If no alias is provided,
                   the device type and number can be used to access the PSU instead.
            connection_type: The type of connection to use for VISA, defaults to TCPIP, not needed
                when the address is a visa resource expression since the connection type is parsed
                from the address string.
            port: The port to use when creating a socket connection.
            serial_config: Serial connection settings, only needed when connection_type="SERIAL".
            gpib_board_number: The GPIB board number (also referred to as a controller) to be used
                when making a GPIB connection (defaults to 0).

        Returns:
            The Power Supply Unit device driver.
        """
        self.__protect_access()
        return cast(
            "PowerSupplyUnitAlias",
            self._add_device(
                device_type=DeviceTypes.PSU.value,
                address=address,
                alias=alias,
                connection_type=connection_type,
                port=port,
                serial_config=serial_config,
                gpib_board_number=gpib_board_number,
            ),
        )

    def add_scope(
        self,
        address: str,
        *,
        alias: Optional[str] = None,
        connection_type: Optional[str] = None,
        port: Optional[int] = None,
        serial_config: Optional[SerialConfig] = None,
        gpib_board_number: Optional[int] = None,
    ) -> ScopeAlias:
        """Add a scope to the DeviceManager.

        Args:
            address: The address of the scope, either an IP address or hostname. If the connection
                     type is ``"USB"`` then the address must be specified as ``"<model>-<serial>"``.
            alias: An optional alias to use to refer to the scope. If no alias is provided,
                   the device type and number can be used to access the scope instead.
            connection_type: The type of connection to use for VISA, defaults to TCPIP, not needed
                when the address is a visa resource expression since the connection type is parsed
                from the address string.
            port: The port to use when creating a socket connection.
            serial_config: Serial connection settings, only needed when connection_type="SERIAL".
            gpib_board_number: The GPIB board number (also referred to as a controller) to be used
                when making a GPIB connection (defaults to 0).

        Returns:
            The scope device driver.
        """
        self.__protect_access()
        return cast(
            "ScopeAlias",
            self._add_device(
                device_type=DeviceTypes.SCOPE.value,
                address=address,
                alias=alias,
                connection_type=connection_type,
                port=port,
                serial_config=serial_config,
                gpib_board_number=gpib_board_number,
            ),
        )

    def add_smu(
        self,
        address: str,
        *,
        alias: Optional[str] = None,
        connection_type: Optional[str] = None,
        port: Optional[int] = None,
        serial_config: Optional[SerialConfig] = None,
        gpib_board_number: Optional[int] = None,
    ) -> SourceMeasureUnitAlias:
        """Add a Source Measure Unit to the DeviceManager.

        Args:
            address: The address of the device, either an IP address or hostname. If the connection
                     type is ``"USB"`` then the address must be specified as ``"<model>-<serial>"``.
            alias: An optional alias to use to refer to the SMU. If no alias is provided,
                   the device type and number can be used to access the SMU instead.
            connection_type: The type of connection to use for VISA, defaults to TCPIP, not needed
                when the address is a visa resource expression since the connection type is parsed
                from the address string.
            port: The port to use when creating a socket connection.
            serial_config: Serial connection settings, only needed when connection_type="SERIAL".
            gpib_board_number: The GPIB board number (also referred to as a controller) to be used
                when making a GPIB connection (defaults to 0).

        Returns:
            The Source Measure Unit device driver.
        """
        self.__protect_access()
        return cast(
            "SourceMeasureUnitAlias",
            self._add_device(
                device_type=DeviceTypes.SMU.value,
                address=address,
                alias=alias,
                connection_type=connection_type,
                port=port,
                serial_config=serial_config,
                gpib_board_number=gpib_board_number,
            ),
        )

    def add_ss(
        self,
        address: str,
        *,
        alias: Optional[str] = None,
        connection_type: Optional[str] = None,
        port: Optional[int] = None,
        gpib_board_number: Optional[int] = None,
    ) -> SystemsSwitchAlias:
        """Add a Systems Switch to the DeviceManager.

        Args:
            address: The address of the device, either an IP address or hostname. If the connection
                     type is ``"USB"`` then the address must be specified as ``"<model>-<serial>"``.
            alias: An optional alias to use to refer to the Systems Switch. If no alias is provided,
                   the device type and number can be used to access the Systems Switch instead.
            connection_type: The type of connection to use for VISA, defaults to TCPIP, not needed
                when the address is a visa resource expression since the connection type is parsed
                from the address string.
            port: The port to use when creating a socket connection.
            gpib_board_number: The GPIB board number (also referred to as a controller) to be used
                when making a GPIB connection (defaults to 0).

        Returns:
            The Systems Switch device driver.
        """
        self.__protect_access()
        return cast(
            "SystemsSwitchAlias",
            self._add_device(
                device_type=DeviceTypes.SS.value,
                address=address,
                alias=alias,
                connection_type=connection_type,
                port=port,
                gpib_board_number=gpib_board_number,
            ),
        )

    def add_unsupported_device(
        self,
        address: str,
        *,
        alias: Optional[str] = None,
        connection_type: Optional[str] = None,
        port: Optional[int] = None,
        gpib_board_number: Optional[int] = None,
    ) -> UnsupportedDeviceAlias:
        """Add a custom device to the DeviceManager that is not an officially supported device type.

        !!! warning
            This should not be used unless absolutely necessary.

        Args:
            address: The address of the device, either an IP address or hostname. If the connection
                     type is ``"USB"`` then the address must be specified as ``"<model>-<serial>"``.
            alias: An optional alias to use to refer to the device. If no alias is provided,
                   the device type and number can be used to access the device instead.
            connection_type: The type of connection to use for VISA, defaults to TCPIP, not needed
                when the address is a visa resource expression since the connection type is parsed
                from the address string.
            port: The port to use when creating a socket connection.
            gpib_board_number: The GPIB board number (also referred to as a controller) to be used
                when making a GPIB connection (defaults to 0).

        Returns:
            The custom device driver.
        """
        self.__protect_access()
        return cast(
            "UnsupportedDeviceAlias",
            self._add_device(
                device_type=DeviceTypes.UNSUPPORTED.value,
                address=address,
                alias=alias,
                connection_type=connection_type,
                port=port,
                gpib_board_number=gpib_board_number,
            ),
        )

    def cleanup_all_devices(self) -> None:
        """Cleanup and reset all devices."""
        self.__protect_access()
        for device_name, device_object in self.__devices.items():
            try:
                device_object.cleanup(verbose=bool(self.__config.options.verbose_mode))
            except (visa.errors.Error, socket.error, RPCError, AttributeError):  # noqa: PERF203
                _logger.warning("Device cleanup of %s failed. Retrying...", device_name)
                device_object.cleanup()

    def close(self) -> None:
        """Close the DeviceManager."""
        self.__protect_access()
        if self.__devices:
            _logger.info("Closing Connections to Devices")
            if self.__teardown_cleanup_enabled:
                self.cleanup_all_devices()
            for device_object in list(self.__devices.values()):
                device_object.close()
        self.__is_open = False
        _logger.info("%s Closed", self.__class__.__name__)

    def disable_device_command_checking(self) -> None:
        """Set the `.enable_verification` attribute of each device to `False`.

        This can have the effect of speeding up automation scripts by no longer checking each
        command after it is sent via the `.set_and_check()` method.
        """
        deprecation_msg = (
            "``DeviceManager.disable_device_command_checking()`` is deprecated. "
            "Use the ``DeviceManager.disable_command_verification`` property instead."
        )
        _logger.warning(deprecation_msg)
        warnings.warn(deprecation_msg, DeprecationWarning, stacklevel=2)
        self.disable_command_verification = True

    def get_available_devices(
        self, search: str = "", configured: bool = True, local: bool = True
    ) -> Dict[str, Tuple[str, ...]]:
        """Get tuples of local and configured devices, optionally narrowed by a search.

        Args:
            search: Simple case-insensitive search criteria for available devices.
            configured: Whether to include configured devices.
            local: Whether to include local devices.

        Returns:
            A dictionary of found devices.

        Raises:
            AssertionError: Local resources can't be queried with the VISA ResourceManager.
                May need to configure the VISA backend.
        """
        self.__protect_access()
        found_devices: Dict[str, Tuple[str, ...]] = {}
        if configured:
            found_devices["configured"] = tuple(
                str(device_config) for device_config in self.__config.devices.values()
            )
        if local:
            try:
                resource_manager = visa.ResourceManager(self.__visa_library)
                found_devices["local"] = resource_manager.list_resources()
            except visa.Error as exc:
                msg = (
                    "Unable to query local resources, ensure you have a suitable "
                    "VISA backend properly installed (NI-VISA is recommended) or "
                    "specify STANDALONE in your config file."
                )
                raise AssertionError(msg) from exc
        if search:
            if configured:
                found_devices["configured"] = tuple(
                    x for x in found_devices["configured"] if search.upper() in x.upper()
                )
            if local:
                found_devices["local"] = tuple(
                    x for x in found_devices["local"] if search.upper() in x.upper()
                )

        return found_devices

    def get_afg(self, number_or_alias: Union[int, str]) -> AFGAlias:
        """Get the Arbitrary Function Generator Python driver for the given AFG number or alias.

        Integers are treated as a device number, strings are treated as an alias.

        Args:
            number_or_alias: The number or alias of the AFG to get.

        Returns:
            The Arbitrary Function Generator device driver.
        """
        self.__protect_access()
        if isinstance(number_or_alias, int):
            return cast(
                "AFGAlias",
                self.get_device(device_type=DeviceTypes.AFG.value, device_number=number_or_alias),
            )
        return cast(
            "AFGAlias", self.get_device(device_type=DeviceTypes.AFG.value, alias=number_or_alias)
        )

    def get_awg(self, number_or_alias: Union[int, str]) -> AWGAlias:
        """Get the Arbitrary Waveform Generator Python driver for the given AWG number or alias.

        Integers are treated as a device number, strings are treated as an alias.

        Args:
            number_or_alias: The number or alias of the AWG to get.

        Returns:
            The Arbitrary Waveform Generator device driver.
        """
        self.__protect_access()
        if isinstance(number_or_alias, int):
            return cast(
                "AWGAlias",
                self.get_device(device_type=DeviceTypes.AWG.value, device_number=number_or_alias),
            )
        return cast(
            "AWGAlias", self.get_device(device_type=DeviceTypes.AWG.value, alias=number_or_alias)
        )

    def get_daq(self, number_or_alias: Union[int, str]) -> DataAcquisitionSystemAlias:
        """Get the Data Acquisition System Python driver for the given DAQ number or alias.

        Integers are treated as a device number, strings are treated as an alias.

        Args:
            number_or_alias: The number or alias of the DAQ to get.

        Returns:
            The Data Acquisition System device driver.
        """
        self.__protect_access()
        if isinstance(number_or_alias, int):
            return cast(
                "DataAcquisitionSystemAlias",
                self.get_device(device_type=DeviceTypes.DAQ.value, device_number=number_or_alias),
            )
        return cast(
            "DataAcquisitionSystemAlias",
            self.get_device(device_type=DeviceTypes.DAQ.value, alias=number_or_alias),
        )

    def get_dmm(self, number_or_alias: Union[int, str]) -> DigitalMultimeterAlias:
        """Get the Digital Multimeter Python driver for the given DMM number or alias.

        Integers are treated as a device number, strings are treated as an alias.

        Args:
            number_or_alias: The number or alias of the DMM to get.

        Returns:
            The Digital Multimeter device driver.
        """
        self.__protect_access()
        if isinstance(number_or_alias, int):
            return cast(
                "DigitalMultimeterAlias",
                self.get_device(device_type=DeviceTypes.DMM.value, device_number=number_or_alias),
            )
        return cast(
            "DigitalMultimeterAlias",
            self.get_device(device_type=DeviceTypes.DMM.value, alias=number_or_alias),
        )

    def get_device(
        self,
        *,
        device_type: Optional[str] = None,
        device_number: Optional[Union[int, str]] = None,
        alias: Optional[str] = None,
    ) -> Device:
        """Get the driver for the given device.

        Either `device_type` and `device_number` or `alias` must be provided when using this method.

        Args:
            device_type: The type of the device to get.
            device_number: The number of the device to get.
            alias: The alias of the device to get.

        Returns:
            The device driver.

        Raises:
            LookupError: The device was not found in the device driver dictionary.
            ValueError: Indicates that both the type/number and alias parameter were left empty.
            TypeError: Indicates that the fetched device type does not match the specified type.
        """
        if not ((device_type and device_number) or alias):
            message = "Either a name or alias must be specified when fetching a device."
            raise ValueError(message)

        device_name = alias.upper() if alias else f"{device_type} {device_number}".upper()
        try:
            device = self.__devices[device_name]
        except KeyError as error:
            message = f"{device_name} was not found in the device driver dictionary."
            raise LookupError(message) from error
        # double check that the device is the correct type
        if (
            device_type is not None
            and device.device_type != device_type.upper()
            and device.config_entry.device_type != DeviceTypes.UNSUPPORTED
        ):
            message = (
                f'A device of type "{device_type}" was specified to be accessed, '
                f'but the accessed device type is actually of type "{device.device_type}".'
            )
            raise TypeError(message)

        return device

    def get_mt(self, number_or_alias: Union[int, str]) -> MarginTesterAlias:
        """Get the Margin Tester Python driver for the given Margin Tester number or alias.

        Integers are treated as a device number, strings are treated as an alias.

        Args:
            number_or_alias: The number or alias of the Margin Tester to get.

        Returns:
            The Margin Tester device driver.
        """
        self.__protect_access()
        if isinstance(number_or_alias, int):
            return cast(
                "MarginTesterAlias",
                self.get_device(device_type=DeviceTypes.MT.value, device_number=number_or_alias),
            )
        return cast(
            "MarginTesterAlias",
            self.get_device(device_type=DeviceTypes.MT.value, alias=number_or_alias),
        )

    def get_psu(self, number_or_alias: Union[int, str]) -> PowerSupplyUnitAlias:
        """Get the Power Supply Unit Python driver for the given PSU number or alias.

        Integers are treated as a device number, strings are treated as an alias.

        Args:
            number_or_alias: The number or alias of the PSU to get.

        Returns:
            The Power Supply Unit device driver.
        """
        self.__protect_access()
        if isinstance(number_or_alias, int):
            return cast(
                "PowerSupplyUnitAlias",
                self.get_device(device_type=DeviceTypes.PSU.value, device_number=number_or_alias),
            )
        return cast(
            "PowerSupplyUnitAlias",
            self.get_device(device_type=DeviceTypes.PSU.value, alias=number_or_alias),
        )

    def get_scope(self, number_or_alias: Union[int, str]) -> ScopeAlias:
        """Get the scope driver for the given scope number or alias.

        Integers are treated as a device number, strings are treated as an alias.

        Args:
            number_or_alias: The number or alias of the scope to get.

        Returns:
            The scope device driver.
        """
        self.__protect_access()
        if isinstance(number_or_alias, int):
            return cast(
                "ScopeAlias",
                self.get_device(device_type=DeviceTypes.SCOPE.value, device_number=number_or_alias),
            )
        return cast(
            "ScopeAlias",
            self.get_device(device_type=DeviceTypes.SCOPE.value, alias=number_or_alias),
        )

    def get_smu(self, number_or_alias: Union[int, str]) -> SourceMeasureUnitAlias:
        """Get the Source Measure Unit Python driver for the given SMU number or alias.

        Integers are treated as a device number, strings are treated as an alias.

        Args:
            number_or_alias: The number or alias of the SMU to get.

        Returns:
            The Source Measure Unit device driver.
        """
        self.__protect_access()
        if isinstance(number_or_alias, int):
            return cast(
                "SourceMeasureUnitAlias",
                self.get_device(device_type=DeviceTypes.SMU.value, device_number=number_or_alias),
            )
        return cast(
            "SourceMeasureUnitAlias",
            self.get_device(device_type=DeviceTypes.SMU.value, alias=number_or_alias),
        )

    def get_ss(self, number_or_alias: Union[int, str]) -> SystemsSwitchAlias:
        """Get the Systems Switch Python driver for the given Systems Switch number or alias.

        Integers are treated as a device number, strings are treated as an alias.

        Args:
            number_or_alias: The number or alias of the Systems Switch to get.

        Returns:
            The Systems Switch device driver.
        """
        self.__protect_access()
        if isinstance(number_or_alias, int):
            return cast(
                "SystemsSwitchAlias",
                self.get_device(device_type=DeviceTypes.SS.value, device_number=number_or_alias),
            )
        return cast(
            "SystemsSwitchAlias",
            self.get_device(device_type=DeviceTypes.SS.value, alias=number_or_alias),
        )

    def load_config_file(self, config_file_path: Union[str, os.PathLike[str]]) -> None:
        """Load in the config file located at the given path.

        This method will update the current configuration options with any newly defined options and
        add any newly defined devices.

        Args:
            config_file_path: The path to the config file to load.
        """
        _logger.info("Loading Configuration from %s", pathlib.Path(config_file_path).resolve())
        self.__config.load_config_file(config_file_path)
        self.__set_options(self.__verbose)
        if len(self.__config.devices) != len(self.__devices):
            _logger.info("Opening Connections to Devices")
            for device_name, device_config in self.__config.devices.items():
                if device_name not in self.__devices:
                    self.__create_device(device_name, device_config, 3)

    def open(self) -> bool:
        """Reopen all devices if the DeviceManager has been previously closed.

        Returns:
            A boolean indicating if the DeviceManager was opened.
        """
        self._suppress_protection = True
        if self.__is_open:
            msg = (
                f"The .open() method should only be used if the "
                f"{self.__class__.__name__} has already been closed."
            )
            raise AssertionError(msg)
        _logger.info("Opening %s", self.__class__.__name__)
        # Create the devices
        if self.__config.devices:
            _logger.info("Opening Connections to Devices")
        for device_name, device_config in self.__config.devices.items():
            self.__create_device(device_name, device_config, 3)
        self.__is_open = True
        self._suppress_protection = False

        return self.__is_open

    def remove_all_devices(self) -> None:
        """Remove all devices from the DeviceManager."""
        self.__protect_access()
        for device in list(self.__devices.values()):
            self.remove_device(device_type=device.device_type, device_number=device.device_number)

    def remove_device(
        self,
        *,
        device_type: Optional[str] = None,
        device_number: Optional[Union[int, str]] = None,
        alias: Optional[str] = None,
    ) -> None:
        """Remove a device from the DeviceManager.

        Either `device_type` and `device_number` or `alias` must be provided when using this method.

        Args:
            device_type: The type of the device to remove, e.g. 'SCOPE'.
            device_number: The number of the device to remove, e.g. '1'.
            alias: A device alias.
        """
        self.__protect_access()
        # Get the device
        if alias:
            device = self.get_device(alias=alias)
        else:
            device = self.get_device(device_type=device_type, device_number=device_number)
        # cannot depend on device.name here in case of mismatched device_type and device.device_type
        device_name = f"{device.config_entry.device_type.value} {device.device_number}"
        # Close the device
        device.close()
        # Remove the device from the dictionary
        del self.__devices[device_name]
        # Remove the device from the config
        self.__config.remove_device(device_name)

    def write_current_configuration_to_config_file(
        self,
        config_file_path: Optional[Union[str, os.PathLike[str]]] = None,
    ) -> None:
        """Write a config file located at the current working directory (or custom path).

        This method will overwrite any existing config file with the current devices and options.
        This method also respects the ``TM_DEVICES_CONFIG`` environment variable.

        Args:
            config_file_path: The path to the config file. If ends in ".toml" will create toml file.
        """
        _logger.info("Writing Configuration to file")
        new_file_path = pathlib.Path(self.__config.write_config_to_file(config_file_path)).resolve()
        _logger.info("Wrote Configuration to %s", new_file_path)

    def get_current_configuration_as_environment_variable_strings(self) -> str:
        """Return the current configuration represented as environment variables."""
        return str(self.__config)

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _add_device(  # noqa: PLR0913
        self,
        device_type: str,
        address: str,
        *,
        alias: Optional[str] = None,
        connection_type: Optional[str] = None,
        port: Optional[int] = None,
        serial_config: Optional[SerialConfig] = None,
        device_driver: Optional[str] = None,
        gpib_board_number: Optional[int] = None,
    ) -> Device:
        """Add a device to the DeviceManager.

        Args:
            device_type: The type of device to add, e.g. 'SCOPE', 'AFG', etc.
            address: The address of the device, either an IP address or hostname. If the connection
                     type is ``"USB"`` then the address must be specified as ``"<model>-<serial>"``.
            alias: An optional alias to use to refer to the device. If no alias is provided,
                   the device type and number can be used to access the device instead.
            connection_type: The type of connection to use for VISA, defaults to TCPIP, not needed
                when the address is a visa resource expression since the connection type is parsed
                from the address string.
            port: The port to use when creating a socket connection.
            serial_config: Serial connection settings, only needed when connection_type="SERIAL".
            device_driver: A string indicating the specific Python device driver to use.
            gpib_board_number: The GPIB board number (also referred to as a controller) to be used
                when making a GPIB connection (defaults to 0).

        Returns:
            The created device.
        """
        if (visa_resource_parts := detect_visa_resource_expression(address)) is not None:
            connection_type = visa_resource_parts[0]
            address = visa_resource_parts[1]
            if (
                connection_type == ConnectionTypes.SOCKET.value
                and len(address_parts := address.split(":", maxsplit=1)) > 1
            ):
                address = address_parts[0]
                port = int(address_parts[1])
            if connection_type.startswith(ConnectionTypes.GPIB.value):
                with contextlib.suppress(ValueError):
                    gpib_board_number = int("".join(filter(lambda x: x.isdigit(), connection_type)))
                connection_type = ConnectionTypes.GPIB.value

        # Device Manager uses all caps for key mappings to device drivers and aliases
        config_dict: dict[str, Optional[Union[str, int, SerialConfig]]] = {
            "device_type": device_type.upper(),
            "address": address.upper(),
        }
        if alias:
            config_dict["alias"] = alias.upper()
        if connection_type:
            config_dict["connection_type"] = connection_type.upper()
        if port:
            config_dict["lan_port"] = port
        if serial_config:
            config_dict["serial_config"] = serial_config
        if device_driver:
            config_dict["device_driver"] = device_driver
        if gpib_board_number:
            config_dict["gpib_board_number"] = gpib_board_number
        new_device_name, new_device_config = self.__config.add_device(**config_dict)  # pyright: ignore[reportArgumentType]

        return self.__create_device(new_device_name, new_device_config, 4)

    @staticmethod
    def __clear_visa_output_buffer_and_get_idn(visa_resource: MessageBasedResource) -> str:
        """Clear out the VISA buffer of a device and return the ``*IDN?`` response.

        Args:
            visa_resource: The VISA resource object.

        Returns:
            The response from the ``*IDN?`` query.

        Raises:
            SystemError: Indicates that the buffer was unable to be cleared.
        """
        # use a try-except block to avoid any errors caused by Visa instruments that may not
        # respond correctly to the read_stb or clear functions.
        try:
            if 16 & visa_resource.read_stb():
                # 16 is the MAV bit (Message Available) from the Status Byte register
                # MAV flag is only one bit and turns off after a single response is
                # successfully read, even if there is more in the buffer.
                msg = (
                    f"\nThe device `{visa_resource.resource_info.resource_name}` had data "
                    "sitting in the VISA Output Buffer on first connection. "
                    "\nDetected data in the buffer via the Status Byte register. "
                    "\nThe device_clear() will be called so VISA I/O buffers get flushed."
                )
                warnings.warn(msg, stacklevel=1)
                _logger.warning(msg)
            # always flush the VISA I/O Buffers on the device to clean up any stale data.
            # (note: the Events are kept in different buffers, so *ESR? is not impacted)
            visa_resource.clear()
        except visa.VisaIOError as e:
            msg = (
                f"A VISA IO error occurred when attempting to read the status byte or clear the "
                f"output buffer of the resource `{visa_resource.resource_info.resource_name}`.\n"
                f"Error: {e}"
            )
            warnings.warn(msg, stacklevel=1)
            _logger.warning(msg)
        visa_resource.write("*IDN?")
        idn_response = ""
        error_msg = None
        old_timeout = visa_resource.timeout
        # 2 second timeout to read should be good
        visa_resource.timeout = 2000
        try:
            msg_string = visa_resource.read().strip()
            # IDN should be a 4 fields separated by 3 commas, also double check string is consistent
            assert msg_string.count(",") == 3  # noqa: S101,PLR2004
            assert msg_string == visa_resource.query("*IDN?").strip()  # noqa: S101
            idn_response = msg_string
        except (UnicodeDecodeError, AssertionError):
            # Unreadable or mismatched response means something is really wrong.
            error_msg = (
                f"Unable to read *IDN? response.\n\t"
                f"The device `{visa_resource.resource_info.resource_name}` likely has data sitting "
                f"in the VISA Output Buffer that survived device_clear()."
            )
        except visa.VisaIOError as error:
            # A timeout means something has gone terribly wrong.
            error_msg = (
                f"{error!s}\n\t"
                "Unable to read data after 2s.\n\t\n\t"
                "Please reboot or read/clear the VISA output buffer on your device and try again."
            )
        if error_msg is not None:
            visa_resource.close()
            raise SystemError(error_msg)
        visa_resource.timeout = old_timeout
        return idn_response

    def __create_device(
        self,
        device_config_name: str,
        device_config: DeviceConfigEntry,
        warning_stacklevel: int,
    ) -> Device:
        """Create a new device driver and add it to the device dictionary.

        Args:
            device_config_name: The name returned when creating the device_config.
            device_config: The dataclass holding the device configuration information.
            warning_stacklevel: The stacklevel of the warning to raise for unsupported device types.

        Returns:
            The created device driver.

        Raises:
            TypeError: Indicates that the created device type does not match the specified type.
            LookupError: Indicates something went wrong when creating the device.
            SystemError: Indicates something went wrong when creating the device.
            AssertionError: Indicates something went wrong when creating the device.
        """
        if self._external_device_drivers is not None:
            device_drivers: Mapping[str, Type[Device]] = MappingProxyType(
                {**self._external_device_drivers, **_DEVICE_DRIVER_MODEL_STR_MAPPING}
            )
        else:
            device_drivers = _DEVICE_DRIVER_MODEL_STR_MAPPING

        alias_string = f' "{device_config.alias}"' if device_config.alias else ""
        if device_config.device_type == DeviceTypes.UNSUPPORTED:
            msg = (
                f"An unsupported device type is being added to the {self.__class__.__name__}. "
                f"Not all functionality will be available in the device driver. "
                f"Please consider contributing to {PACKAGE_NAME} to implement official "
                f"support for this device type."
            )
            warnings.warn(msg, stacklevel=warning_stacklevel)
            _logger.warning(msg)
        _logger.info("Creating Connection to %s%s", device_config_name, alias_string)
        new_device: Device
        if device_config.connection_type == ConnectionTypes.REST_API:
            device_driver_class = device_drivers[str(device_config.device_driver)]
            new_device = device_driver_class(device_config, self.__verbose)
        else:
            # Create VISA connection and determine proper device driver
            try:
                visa_resource = create_visa_connection(
                    device_config,
                    self.__visa_library,
                    retry_connection=bool(self.__config.options.retry_visa_connection),
                )
                new_device = self.__select_visa_device_driver(
                    visa_resource, device_config, device_drivers
                )
            except (LookupError, SystemError, AssertionError, NotImplementedError, ConnectionError):
                # Catch errors here and remove the device to allow future connections to happen.
                self.__config.remove_device(device_config_name)
                # Simply re-raise the exception, it will have plenty of information on the error.
                raise

        # hardcode the device number from the config entry key name
        new_device._device_number = int(  # noqa: SLF001  # pyright: ignore [reportPrivateUsage]
            device_config_name.rsplit(" ", 1)[1]
        )
        # Reset cached properties by deleting them
        # noinspection PyPropertyAccess
        del new_device.name
        # noinspection PyPropertyAccess
        del new_device.alias
        # noinspection PyPropertyAccess
        del new_device.name_and_alias

        if device_config_name in self.__devices:
            del self.__devices[device_config_name]
        self.__devices[device_config_name] = new_device
        if device_config.alias:
            self.__devices[device_config.alias] = new_device
        if new_device.config_entry.device_type == DeviceTypes.UNSUPPORTED:
            # Add an alias to the AliasDict which contains the device_type that the custom device
            # driver defines, which may be different from the device type defined in the config,
            # which is "UNSUPPORTED". This allows the device to be removed from the config and
            # DeviceManager when necessary.
            self.__devices[f"{new_device.device_type} {new_device.device_number}".upper()] = (
                new_device
            )

        # double check created device is correct type
        if (
            new_device.device_type != new_device.config_entry.device_type.value
            and new_device.config_entry.device_type != DeviceTypes.UNSUPPORTED
        ):
            self.remove_device(
                alias=new_device.config_entry.alias,
                device_type=new_device.config_entry.device_type.value,
                device_number=new_device.device_number,
            )
            msg = (
                f'A device of type "{new_device.config_entry.device_type.value}" was specified to '
                f"be created, but the created device type is actually of type "
                f'"{new_device.device_type}".'
            )
            raise TypeError(msg)

        # Clean up devices if the option is enabled.
        if self.__setup_cleanup_enabled:
            new_device.cleanup(verbose=bool(self.__config.options.verbose_mode))

        return new_device

    def __protect_access(self) -> None:
        """Check if the method should be allowed to be used.

        Raises:
            AttributeError: Indicates that the calling method should not have been used.
        """
        if not self.__is_open and not self._suppress_protection:
            previous_frame = cast("FrameType", inspect.currentframe().f_back.f_back)  # pyright: ignore[reportOptionalMemberAccess]
            message = (
                f"The {self.__class__.__name__} is closed, please use the .open() "
                f"method before continuing to use the {self.__class__.__name__}.\n"
            )
            with contextlib.suppress(AttributeError):
                message += (
                    f"Called from {previous_frame.f_code.co_filename}:{previous_frame.f_lineno}\n"
                )
            raise AttributeError(message)

    def __select_visa_device_driver(
        self,
        visa_resource: MessageBasedResource,
        device_config: DeviceConfigEntry,
        device_drivers: Mapping[str, Type[Device]],
    ) -> Device:
        """Select the correct VISA device driver based on the ``*IDN?`` response.

        Be sure to handle removing the device from the config on a SystemError.

        Args:
            visa_resource: The VISA resource object.
            device_config: The device configuration object.
            device_drivers: The mapping of model series strings to device drivers.

        Returns:
            The new device driver.

        Raises:
            SystemError: Indicating the correct driver was unable to be determined.
        """
        idn_response = self.__clear_visa_output_buffer_and_get_idn(visa_resource)
        model_series = ""
        try:
            model_series = get_model_series(idn_response.split(",")[1])
            device_driver = cast("Type[PIControl]", device_drivers[model_series])
            new_device = device_driver(
                device_config,
                self.__verbose,
                visa_resource,
                self.__default_visa_timeout,
            )
        except (KeyError, IndexError) as error:
            visa_resource.close()
            message = "Unable to determine which device driver to use."
            if model_series:
                message += f' The parsed model series is "{model_series}".'
            message += f" *IDN? returned {idn_response!r}"
            raise SystemError(message) from error

        return cast("Device", new_device)

    def __set_options(self, verbose: bool) -> None:
        """Set the options for the DeviceManager.

        Args:
            verbose: A boolean indicating if verbose output should be printed.
        """
        self.__verbose = self.__config.options.verbose_mode = verbose or bool(
            self.__config.options.verbose_mode
        )
        self.__teardown_cleanup_enabled = bool(self.__config.options.teardown_cleanup)
        self.__setup_cleanup_enabled = bool(self.__config.options.setup_cleanup)
        self.__disable_command_verification = bool(
            self.__config.options.disable_command_verification
        )
        self.__default_visa_timeout = (
            5000
            if self.__config.options.default_visa_timeout is None
            else self.__config.options.default_visa_timeout
        )
        # Configure the VISA library
        if self.__config.options.standalone:
            self.__visa_library = PYVISA_PY_BACKEND
        elif self.__visa_library is NotImplemented:
            # Check for an environment variable, primarily used for enabling
            # validation of example code on simulated instruments.
            if visa_library := os.getenv("TM_DEVICES_VISA_LIBRARY"):
                self.__visa_library = visa_library
            else:
                self.__visa_library = ""
        self.verbose_visa = bool(self.__config.options.verbose_visa)


def print_available_visa_devices() -> None:  # pragma: no cover
    """Print all available VISA devices to the console."""
    with contextlib.redirect_stdout(None), contextlib.redirect_stderr(None), DeviceManager() as dm:
        available_devices = dm.get_available_devices()
    print(json.dumps(available_devices["local"], indent=2))  # noqa: T201
