# pylint: disable=too-many-lines
"""Device manager module."""
from __future__ import annotations

import contextlib
import inspect
import json
import os
import pathlib
import socket
import warnings

from types import FrameType, MappingProxyType, TracebackType
from typing import cast, Dict, Mapping, Optional, Tuple, Type, TYPE_CHECKING, Union

from tm_devices.components import DMConfigParser
from tm_devices.drivers import (
    AFG3K,
    AFG3KB,
    AFG3KC,
    AFG31K,
    AWG5K,
    AWG5KB,
    AWG5KC,
    AWG7K,
    AWG7KB,
    AWG7KC,
    AWG70KA,
    AWG70KB,
    AWG5200,
    DAQ6510,
    DMM6500,
    DMM7510,
    DMM7512,
    DPO2K,
    DPO2KB,
    DPO4K,
    DPO4KB,
    DPO5K,
    DPO5KB,
    DPO7K,
    DPO7KC,
    DPO70K,
    DPO70KC,
    DPO70KD,
    DPO70KDX,
    DPO70KSX,
    DSA70K,
    DSA70KC,
    DSA70KD,
    LPD6,
    MDO3,
    MDO3K,
    MDO4K,
    MDO4KB,
    MDO4KC,
    MSO2,
    MSO2K,
    MSO2KB,
    MSO4,
    MSO4K,
    MSO4KB,
    MSO5,
    MSO5B,
    MSO5K,
    MSO5KB,
    MSO5LP,
    MSO6,
    MSO6B,
    MSO70K,
    MSO70KC,
    MSO70KDX,
    PSU2200,
    PSU2220,
    PSU2230,
    PSU2231,
    PSU2231A,
    PSU2280,
    PSU2281,
    SMU2400,
    SMU2401,
    SMU2410,
    SMU2450,
    SMU2460,
    SMU2461,
    SMU2470,
    SMU2601A,
    SMU2601B,
    SMU2601BPulse,
    SMU2602A,
    SMU2602B,
    SMU2604A,
    SMU2604B,
    SMU2606B,
    SMU2611A,
    SMU2611B,
    SMU2612A,
    SMU2612B,
    SMU2614A,
    SMU2614B,
    SMU2634A,
    SMU2634B,
    SMU2635A,
    SMU2635B,
    SMU2636A,
    SMU2636B,
    SMU2651A,
    SMU2657A,
    SMU6430,
    SMU6514,
    SMU6517B,
    SS3706A,
    TekScopeSW,
    TMT4,
    TSOVu,
)
from tm_devices.drivers.api.rest_api.rest_api_device import RESTAPIDevice
from tm_devices.drivers.pi.pi_device import PIDevice
from tm_devices.helpers import (
    AliasDict,
    check_for_update,
    ConnectionTypes,
    create_visa_connection,
    detect_visa_resource_expression,
    DeviceConfigEntry,
    DeviceTypes,
    DMConfigOptions,
    get_model_series,
    print_with_timestamp,
    PYVISA_PY_BACKEND,
    SerialConfig,
    Singleton,
)

with warnings.catch_warnings():
    warnings.simplefilter("ignore", UserWarning)
    import pyvisa as visa

    from pyvisa_py.protocols.rpc import RPCError  # type: ignore

# noinspection PyUnresolvedReferences  # pylint: disable=unused-import,wrong-import-order
from traceback_with_variables import activate_by_import  # noqa: F401  # type: ignore

if TYPE_CHECKING:
    from pyvisa.resources import MessageBasedResource
    from typing_extensions import Self, TypeAlias

    from tm_devices.drivers.device import Device

####################################################################################################
# Type Aliases
####################################################################################################
# TODO: this is temporary until python3.12 which will support TypeVar with defaults
AFGAlias: TypeAlias = Union[AFG3K, AFG3KB, AFG3KC, AFG31K]
AWGAlias: TypeAlias = Union[AWG5K, AWG5KB, AWG5KC, AWG7K, AWG7KB, AWG7KC, AWG5200, AWG70KA, AWG70KB]
DataAcquisitionSystemAlias: TypeAlias = Union[DAQ6510]  # pyright: ignore
DigitalMultimeterAlias: TypeAlias = Union[DMM6500, DMM7510, DMM7512]
ScopeAlias: TypeAlias = Union[
    DPO5K,
    DPO5KB,
    DPO7K,
    DPO7KC,
    DPO70K,
    DPO70KC,
    DPO70KD,
    DPO70KDX,
    DPO70KSX,
    DSA70K,
    DSA70KC,
    DSA70KD,
    LPD6,
    MSO5,
    MSO6,
    MSO4,
    MSO2,
    MSO6B,
    MSO5B,
    MSO5LP,
    TekScopeSW,
    TSOVu,
    MSO2K,
    MSO2KB,
    DPO2K,
    DPO2KB,
    MDO3,
    MDO3K,
    MDO4K,
    MDO4KB,
    MDO4KC,
    MSO4K,
    MSO4KB,
    DPO4K,
    DPO4KB,
    MSO5K,
    MSO5KB,
    MSO70K,
    MSO70KC,
    MSO70KDX,
]
MarginTesterAlias: TypeAlias = Union[TMT4]  # pyright: ignore
PowerSupplyUnitAlias: TypeAlias = Union[
    PSU2200,
    PSU2220,
    PSU2230,
    PSU2231,
    PSU2231A,
    PSU2280,
    PSU2281,
]
SourceMeasureUnitAlias: TypeAlias = Union[
    SMU2400,
    SMU2401,
    SMU2410,
    SMU2450,
    SMU2460,
    SMU2461,
    SMU2470,
    SMU2601B,
    SMU2601BPulse,
    SMU2602B,
    SMU2604B,
    SMU2606B,
    SMU2611B,
    SMU2612B,
    SMU2614B,
    SMU2634B,
    SMU2635B,
    SMU2636B,
    SMU2651A,
    SMU2657A,
    SMU2601A,
    SMU2602A,
    SMU2604A,
    SMU2611A,
    SMU2612A,
    SMU2614A,
    SMU2634A,
    SMU2635A,
    SMU2636A,
    SMU6430,
    SMU6514,
    SMU6517B,
]
SystemsSwitchAlias: TypeAlias = Union[SS3706A]  # pyright: ignore


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
            verbose: A boolean indicating if verbose output should be printed.
            config_options: An optional set of configuration options to use
                (updates the current configuration options).
            external_device_drivers: An optional dict for passing in additional device drivers.
        """
        check_for_update()
        self._suppress_protection = False
        # Set up the DeviceManager
        self.__is_open = False
        self.__verbose_visa = False
        self.__devices: Dict[str, Union[PIDevice, RESTAPIDevice]] = AliasDict()
        self._external_device_drivers = external_device_drivers
        self.__config = DMConfigParser()
        if config_options is not None:
            self.__config.update_options(config_options)

        # initialize for __set_options
        self.__verbose: bool = NotImplemented
        self.__teardown_cleanup_enabled: bool = NotImplemented
        self.__setup_cleanup_enabled: bool = NotImplemented
        self.__visa_library: str = NotImplemented
        # actually populate the options
        self.__set_options(verbose)

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
    def devices(self) -> Mapping[str, Union[RESTAPIDevice, PIDevice]]:
        """Return the dictionary of devices."""
        return MappingProxyType(self.__devices)

    @property
    def is_open(self) -> bool:
        """Return a boolean indicating if the DeviceManager has closed all device connections."""
        return self.__is_open

    @property
    def teardown_cleanup_enabled(self) -> bool:
        """Return a boolean indicating if cleanup at teardown is enabled for devices."""
        return self.__teardown_cleanup_enabled

    @teardown_cleanup_enabled.setter
    def teardown_cleanup_enabled(self, value: bool) -> None:
        """Set the property which can enable cleanup on teardown of devices."""
        self.__config.options.teardown_cleanup = value
        self.__teardown_cleanup_enabled = value

    @property
    def setup_cleanup_enabled(self) -> bool:
        """Return a boolean indicating if cleanup at setup is enabled for devices."""
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
                if "DEBUG" in str(handler):
                    visa.logger.removeHandler(handler)
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
    ) -> AFGAlias:
        """Add an AFG to the DeviceManager.

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

        Returns:
            The AFG device driver.
        """
        self.__protect_access()
        return cast(
            AFGAlias,
            self._add_device(
                device_type=DeviceTypes.AFG.value,
                address=address,
                alias=alias,
                connection_type=connection_type,
                port=port,
                serial_config=serial_config,
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
    ) -> AWGAlias:
        """Add an AWG to the DeviceManager.

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

        Returns:
            The AWG device driver.
        """
        self.__protect_access()
        return cast(
            AWGAlias,
            self._add_device(
                device_type=DeviceTypes.AWG.value,
                address=address,
                alias=alias,
                connection_type=connection_type,
                port=port,
                serial_config=serial_config,
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
    ) -> DataAcquisitionSystemAlias:
        """Add a DAQ to the DeviceManager.

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

        Returns:
            The DAQ device driver.
        """
        self.__protect_access()
        return cast(
            DataAcquisitionSystemAlias,
            self._add_device(
                device_type=DeviceTypes.DAQ.value,
                address=address,
                alias=alias,
                connection_type=connection_type,
                port=port,
                serial_config=serial_config,
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
    ) -> DigitalMultimeterAlias:
        """Add a DMM to the DeviceManager.

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

        Returns:
            The DMM device driver.
        """
        self.__protect_access()
        return cast(
            DigitalMultimeterAlias,
            self._add_device(
                device_type=DeviceTypes.DMM.value,
                address=address,
                alias=alias,
                connection_type=connection_type,
                port=port,
                serial_config=serial_config,
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
            MarginTesterAlias,
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
    ) -> PowerSupplyUnitAlias:
        """Add a PSU to the DeviceManager.

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

        Returns:
            The PSU device driver.
        """
        self.__protect_access()
        return cast(
            PowerSupplyUnitAlias,
            self._add_device(
                device_type=DeviceTypes.PSU.value,
                address=address,
                alias=alias,
                connection_type=connection_type,
                port=port,
                serial_config=serial_config,
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

        Returns:
            The scope device driver.
        """
        self.__protect_access()
        return cast(
            ScopeAlias,
            self._add_device(
                device_type=DeviceTypes.SCOPE.value,
                address=address,
                alias=alias,
                connection_type=connection_type,
                port=port,
                serial_config=serial_config,
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
    ) -> SourceMeasureUnitAlias:
        """Add a SMU to the DeviceManager.

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

        Returns:
            The SMU device driver.
        """
        self.__protect_access()
        return cast(
            SourceMeasureUnitAlias,
            self._add_device(
                device_type=DeviceTypes.SMU.value,
                address=address,
                alias=alias,
                connection_type=connection_type,
                port=port,
                serial_config=serial_config,
            ),
        )

    def add_ss(
        self,
        address: str,
        *,
        alias: Optional[str] = None,
        connection_type: Optional[str] = None,
        port: Optional[int] = None,
    ) -> SystemsSwitchAlias:
        """Add a SS to the DeviceManager.

        Args:
            address: The address of the device, either an IP address or hostname. If the connection
                     type is ``"USB"`` then the address must be specified as ``"<model>-<serial>"``.
            alias: An optional alias to use to refer to the SS. If no alias is provided,
                   the device type and number can be used to access the SS instead.
            connection_type: The type of connection to use for VISA, defaults to TCPIP, not needed
            when the address is a visa resource expression since the connection type is parsed from
            the address string.
            port: The port to use when creating a socket connection.

        Returns:
            The SS device driver.
        """
        self.__protect_access()
        return cast(
            SystemsSwitchAlias,
            self._add_device(
                device_type=DeviceTypes.SS.value,
                address=address,
                alias=alias,
                connection_type=connection_type,
                port=port,
            ),
        )

    def cleanup_all_devices(self) -> None:
        """Cleanup and reset all devices."""
        self.__protect_access()
        for device_name, device_object in self.__devices.items():
            try:
                device_object.cleanup(verbose=False or bool(self.__config.options.verbose_mode))
            except (visa.errors.Error, socket.error, RPCError, AttributeError):  # noqa: PERF203
                print(f"Device cleanup of {device_name} failed. Retrying...")
                device_object.cleanup()

    def close(self) -> None:
        """Close the DeviceManager."""
        self.__protect_access()
        print("")
        if self.__devices:
            print_with_timestamp("Closing Connections to Devices")
            if self.__teardown_cleanup_enabled:
                self.cleanup_all_devices()
            for device_object in list(self.__devices.values()):
                device_object.close()
        self.__is_open = False
        print_with_timestamp(f"{self.__class__.__name__} Closed")

    def disable_device_command_checking(self) -> None:
        """Set the `.enable_verification` attribute of each device to `False`.

        This has the effect of speeding up automation scripts that no longer require checking each
        command after it is sent.
        """
        self.__protect_access()
        for device in self.__devices.values():
            device.enable_verification = False

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
        """Get the AFG driver for the given AFG number or alias.

        Integers are treated as a device number, strings are treated as an alias.

        Args:
            number_or_alias: The number or alias of the AFG to get.

        Returns:
            The AFG device driver.
        """
        self.__protect_access()
        if isinstance(number_or_alias, int):
            return cast(
                AFGAlias,
                self.get_device(device_type=DeviceTypes.AFG.value, device_number=number_or_alias),
            )
        return cast(
            AFGAlias, self.get_device(device_type=DeviceTypes.AFG.value, alias=number_or_alias)
        )

    def get_awg(self, number_or_alias: Union[int, str]) -> AWGAlias:
        """Get the AWG driver for the given AWG number or alias.

        Integers are treated as a device number, strings are treated as an alias.

        Args:
            number_or_alias: The number or alias of the AWG to get.

        Returns:
            The AWG device driver.
        """
        self.__protect_access()
        if isinstance(number_or_alias, int):
            return cast(
                AWGAlias,
                self.get_device(device_type=DeviceTypes.AWG.value, device_number=number_or_alias),
            )
        return cast(
            AWGAlias, self.get_device(device_type=DeviceTypes.AWG.value, alias=number_or_alias)
        )

    def get_daq(self, number_or_alias: Union[int, str]) -> DataAcquisitionSystemAlias:
        """Get the DAQ driver for the given scope number or alias.

        Integers are treated as a device number, strings are treated as an alias.

        Args:
            number_or_alias: The number or alias of the scope to get.

        Returns:
            The scope device driver.
        """
        self.__protect_access()
        if isinstance(number_or_alias, int):
            return cast(
                DataAcquisitionSystemAlias,
                self.get_device(device_type=DeviceTypes.DAQ.value, device_number=number_or_alias),
            )
        return cast(
            DataAcquisitionSystemAlias,
            self.get_device(device_type=DeviceTypes.DAQ.value, alias=number_or_alias),
        )

    def get_dmm(self, number_or_alias: Union[int, str]) -> DigitalMultimeterAlias:
        """Get the DMM driver for the given DMM number or alias.

        Integers are treated as a device number, strings are treated as an alias.

        Args:
            number_or_alias: The number or alias of the DMM to get.

        Returns:
            The DMM device driver.
        """
        self.__protect_access()
        if isinstance(number_or_alias, int):
            return cast(
                DigitalMultimeterAlias,
                self.get_device(device_type=DeviceTypes.DMM.value, device_number=number_or_alias),
            )
        return cast(
            DigitalMultimeterAlias,
            self.get_device(device_type=DeviceTypes.DMM.value, alias=number_or_alias),
        )

    def get_device(
        self,
        *,
        device_type: Optional[str] = None,
        device_number: Optional[Union[int, str]] = None,
        alias: Optional[str] = None,
    ) -> Union[RESTAPIDevice, PIDevice]:
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
        if device_type is not None and device.device_type != device_type.upper():
            message = (
                f'A device of type "{device_type}" was specified to be accessed, '
                f'but the accessed device type is actually of type "{device.device_type}".'
            )
            raise TypeError(message)

        return device

    def get_mt(self, number_or_alias: Union[int, str]) -> MarginTesterAlias:
        """Get the Margin Tester driver for the given Margin Tester number or alias.

        Integers are treated as a device number, strings are treated as an alias.

        Args:
            number_or_alias: The number or alias of the Margin Tester to get.

        Returns:
            The Margin Tester device driver.
        """
        self.__protect_access()
        if isinstance(number_or_alias, int):
            return cast(
                MarginTesterAlias,
                self.get_device(device_type=DeviceTypes.MT.value, device_number=number_or_alias),
            )
        return cast(
            MarginTesterAlias,
            self.get_device(device_type=DeviceTypes.MT.value, alias=number_or_alias),
        )

    def get_psu(self, number_or_alias: Union[int, str]) -> PowerSupplyUnitAlias:
        """Get the PSU driver for the given PSU number or alias.

        Integers are treated as a device number, strings are treated as an alias.

        Args:
            number_or_alias: The number or alias of the PSU to get.

        Returns:
            The PSU device driver.
        """
        self.__protect_access()
        if isinstance(number_or_alias, int):
            return cast(
                PowerSupplyUnitAlias,
                self.get_device(device_type=DeviceTypes.PSU.value, device_number=number_or_alias),
            )
        return cast(
            PowerSupplyUnitAlias,
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
                ScopeAlias,
                self.get_device(device_type=DeviceTypes.SCOPE.value, device_number=number_or_alias),
            )
        return cast(
            ScopeAlias, self.get_device(device_type=DeviceTypes.SCOPE.value, alias=number_or_alias)
        )

    def get_smu(self, number_or_alias: Union[int, str]) -> SourceMeasureUnitAlias:
        """Get the SMU driver for the given SMU number or alias.

        Integers are treated as a device number, strings are treated as an alias.

        Args:
            number_or_alias: The number or alias of the SMU to get.

        Returns:
            The SMU device driver.
        """
        self.__protect_access()
        if isinstance(number_or_alias, int):
            return cast(
                SourceMeasureUnitAlias,
                self.get_device(device_type=DeviceTypes.SMU.value, device_number=number_or_alias),
            )
        return cast(
            SourceMeasureUnitAlias,
            self.get_device(device_type=DeviceTypes.SMU.value, alias=number_or_alias),
        )

    def get_ss(self, number_or_alias: Union[int, str]) -> SystemsSwitchAlias:
        """Get the SS driver for the given SS number or alias.

        Integers are treated as a device number, strings are treated as an alias.

        Args:
            number_or_alias: The number or alias of the SS to get.

        Returns:
            The SS device driver.
        """
        self.__protect_access()
        if isinstance(number_or_alias, int):
            return cast(
                SystemsSwitchAlias,
                self.get_device(device_type=DeviceTypes.SS.value, device_number=number_or_alias),
            )
        return cast(
            SystemsSwitchAlias,
            self.get_device(device_type=DeviceTypes.SS.value, alias=number_or_alias),
        )

    def load_config_file(self, config_file_path: Union[str, os.PathLike[str]]) -> None:
        """Load in the config file located at the given path.

        This method will update the current configuration options with any newly defined options and
        add any newly defined devices.

        Args:
            config_file_path: The path to the config file to load.
        """
        print_with_timestamp(
            f"Loading Configuration from {pathlib.Path(config_file_path).resolve()}"
        )
        self.__config.load_config_file(config_file_path)
        self.__set_options(self.__verbose)
        if len(self.__config.devices) != len(self.__devices):
            print_with_timestamp("Opening Connections to Devices")
            for device_name, device_config in self.__config.devices.items():
                if device_name not in self.__devices:
                    self.__create_device(device_name, device_config)

    def open(self) -> bool:  # noqa: A003
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
        print_with_timestamp(f"Opening {self.__class__.__name__}")
        # Create the devices
        if self.__config.devices:
            print_with_timestamp("Opening Connections to Devices")
        for device_name, device_config in self.__config.devices.items():
            self.__create_device(device_name, device_config)
        if self.__setup_cleanup_enabled:
            self.cleanup_all_devices()
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
        print_with_timestamp("Writing Configuration to file")
        new_file_path = pathlib.Path(self.__config.write_config_to_file(config_file_path)).resolve()
        print_with_timestamp(f"Wrote Configuration to {new_file_path}")

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
    ) -> Union[RESTAPIDevice, PIDevice]:
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

        Returns:
            The created device.
        """
        if (visa_resource_parts := detect_visa_resource_expression(address)) is not None:
            connection_type = visa_resource_parts[0]
            address = visa_resource_parts[1]

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
        new_device_name, new_device_config = self.__config.add_device(**config_dict)  # type: ignore

        return self.__create_device(new_device_name, new_device_config)

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
        if 16 & visa_resource.read_stb():
            # 16 is the MAV bit (Message Available) from the Status Byte register
            # MAV flag is only one bit and turns off after a single response is successfully read,
            # even if there's more in the buffer
            warnings.warn(
                f"\nThe device `{visa_resource.resource_info.resource_name}` had data "
                "sitting in the VISA Output Buffer on first connection. "
                "\nDetected data in the buffer via the Status Byte register. "
                "\nThe device_clear() will be called so VISA I/O buffers get flushed.",
                stacklevel=1,
            )
        # always flush the VISA I/O Buffers on the device to clean up any stale data.
        # (note: the Events are kept in different buffers, so *ESR? is not impacted)
        visa_resource.clear()
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
        self, device_config_name: str, device_config: DeviceConfigEntry
    ) -> Union[RESTAPIDevice, PIDevice]:
        """Create a new device driver and add it to the device dictionary.

        Args:
            device_config_name: The name returned when creating the device_config.
            device_config: The dataclass holding the device configuration information.

        Returns:
            The created device driver.

        Raises:
            TypeError: Indicates that the created device type does not match the specified type.
            LookupError: Indicates something went wrong when creating the device.
            SystemError: Indicates something went wrong when creating the device.
            AssertionError: Indicates something went wrong when creating the device.
        """
        # pylint: disable=import-outside-toplevel
        from tm_devices.drivers import DEVICE_DRIVER_MODEL_MAPPING

        if self._external_device_drivers is not None:
            device_drivers: Mapping[str, Type[Device]] = MappingProxyType(
                {**self._external_device_drivers, **DEVICE_DRIVER_MODEL_MAPPING}
            )
        else:
            device_drivers = DEVICE_DRIVER_MODEL_MAPPING

        alias_string = f' "{device_config.alias}"' if device_config.alias else ""
        print_with_timestamp(f"Creating Connection to {device_config_name}{alias_string}")
        new_device: Union[RESTAPIDevice, PIDevice]
        if device_config.connection_type == ConnectionTypes.REST_API:
            device_driver_class = device_drivers[str(device_config.device_driver)]
            new_device = cast(RESTAPIDevice, device_driver_class(device_config, self.__verbose))
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

        if device_config_name in self.__devices:
            del self.__devices[device_config_name]
        self.__devices[device_config_name] = new_device
        if device_config.alias:
            self.__devices[device_config.alias] = new_device

        # double check created device is correct type
        if new_device.device_type != new_device.config_entry.device_type.value:
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
            new_device.cleanup(verbose=False or bool(self.__config.options.verbose_mode))

        return new_device

    def __protect_access(self) -> None:
        """Check if the method should be allowed to be used.

        Raises:
            AttributeError: Indicates that the calling method should not have been used.
        """
        if not self.__is_open and not self._suppress_protection:
            previous_frame = cast(FrameType, inspect.currentframe().f_back.f_back)  # type: ignore
            message = (
                f"The {self.__class__.__name__} is closed, please use the .open() "
                f"method before continuing to use the {self.__class__.__name__}.\n"
            )
            with contextlib.suppress(AttributeError):
                message += (
                    f"Called from {previous_frame.f_code.co_filename}:"
                    f"{previous_frame.f_lineno}\n"
                )
            raise AttributeError(message)

    def __select_visa_device_driver(
        self,
        visa_resource: MessageBasedResource,
        device_config: DeviceConfigEntry,
        device_drivers: Mapping[str, Type[Device]],
    ) -> PIDevice:
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
            device_driver = cast(Type[PIDevice], device_drivers[model_series])
            new_device = device_driver(device_config, self.__verbose, visa_resource)
        except (KeyError, IndexError) as error:
            visa_resource.close()
            message = "Unable to determine which device driver to use."
            if model_series:
                message += f' The parsed model series is "{model_series}".'
            message += f" *IDN? returned {idn_response!r}"
            raise SystemError(message) from error

        return new_device

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
    print(json.dumps(available_devices["local"], indent=2))
