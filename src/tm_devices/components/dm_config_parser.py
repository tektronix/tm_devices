"""Config parser module."""

from __future__ import annotations

import contextlib
import dataclasses
import os
import pathlib

from types import MappingProxyType
from typing import (
    Any,
    cast,
    Dict,
    get_type_hints,
    List,
    Mapping,
    Optional,
    Protocol,
    runtime_checkable,
    Tuple,
    Type,
    Union,
)

import tomli
import tomli_w
import yaml

from tm_devices.helpers import (
    AliasDict,
    ConfigFileType,
    ConnectionTypes,
    DeviceConfigEntry,
    DeviceTypes,
    DMConfigOptions,
    SerialConfig,
)
from tm_devices.helpers.constants_and_dataclasses import (
    CONFIG_CLASS_STR_PREFIX_MAPPING,
)


@runtime_checkable
@dataclasses.dataclass
class _DataclassProtocol(Protocol):
    """A Protocol class to allow for type hinting things that accept generic dataclasses."""


class DMConfigParser:
    """Class to parse a configuration file for device connections and runtime options."""

    DEVICES_ENV_VARIABLE = "TM_DEVICES"
    """The name of the environment variable which can contain a list of device configurations.

    Multiple devices are separated by "~~~", each device contains a comma-separated list of device
    parameters to use when connecting to the device. See the [configuration
    documentation][environment-variable] for the device configuration environment variable syntax.
    """
    OPTIONS_ENV_VARIABLE = "TM_OPTIONS"
    """The name of the environment variable which can contain a comma-separated list of options.

    See the [configuration documentation][environment-variable] for the options environment variable
    syntax.
    """
    CONFIG_FILE_PATH_ENV_VARIABLE = "TM_DEVICES_CONFIG"
    """The name of the environment variable to check for a custom config file path.

    This environment variable is checked to see if there is a user-provided path to a custom config
    file that contains a list of devices and hostnames/IP addresses.
    """
    DEFAULT_CONFIG_FILE_PATH = "./tm_devices.yaml"
    """The default location for the config file.

    If present, the file should contain a list of devices and hostnames/IP addresses. See the
    [configuration documentation][config-file] for the config file syntax.
    """
    FileType = ConfigFileType
    """A convenience enumeration listing the valid config file types."""

    _CONFIG_NESTED_DICT_MAPPING: Mapping[
        Union[Type[_DataclassProtocol], Type[SerialConfig]], str
    ] = MappingProxyType({SerialConfig: "serial_config"})

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(self) -> None:
        """Initialize the DMConfigParser and read the configuration."""
        # Create a count of the number of each type of device created
        self.__dev_count: Dict[str, int] = dict.fromkeys(DeviceTypes.list_values(), 0)

        self.__devices: Dict[str, DeviceConfigEntry] = AliasDict()
        self.__options = DMConfigOptions()

        # Check if the environment variables exists
        if self.DEVICES_ENV_VARIABLE in os.environ or self.OPTIONS_ENV_VARIABLE in os.environ:
            devices_list = self.__parse_env_devices()
            self.update_options(self.__parse_env_options())

            self.__pre_process_env_devices(devices_list)
            self.__add_from_device_list(devices_list)
        else:
            # Errors can be ignored, no default file was found
            with contextlib.suppress(FileNotFoundError):
                self.load_config_file()

    def __str__(self) -> str:
        """Return string representation of instance as environment variables."""
        return (
            f"{self.OPTIONS_ENV_VARIABLE}={self.__options}\n"
            f"{self.DEVICES_ENV_VARIABLE}="
            f"{'~~~'.join(['', *map(str, self.__devices.values()), ''])}"
        )

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def defined_config_file_path(self) -> str:
        """Filepath of the config file.

        Prioritizes the path contained in the environment variable defined by
        [`DMConfigParser.CONFIG_FILE_PATH_ENV_VARIABLE`][tm_devices.components.DMConfigParser.CONFIG_FILE_PATH_ENV_VARIABLE]
        with a fallback to the default path defined by
        [`DMConfigParser.DEFAULT_CONFIG_FILE_PATH`][tm_devices.components.DMConfigParser.DEFAULT_CONFIG_FILE_PATH].
        """
        return os.getenv(
            self.CONFIG_FILE_PATH_ENV_VARIABLE,
            self.DEFAULT_CONFIG_FILE_PATH,
        )

    @property
    def devices(self) -> Mapping[str, DeviceConfigEntry]:
        """Return the device dict as a read-only object."""
        return MappingProxyType(self.__devices)

    @property
    def options(self) -> DMConfigOptions:
        """Return the config options."""
        return self.__options

    ################################################################################################
    # Public Methods
    ################################################################################################
    def add_device(  # noqa: PLR0913  # pylint: disable=too-many-locals
        self,
        *,
        device_type: Union[DeviceTypes, str],
        address: str,
        connection_type: Union[ConnectionTypes, str] = ConnectionTypes.TCPIP,
        alias: Optional[str] = None,
        lan_port: Optional[int] = None,
        lan_device_name: Optional[str] = None,
        serial_config: Optional[SerialConfig] = None,
        device_driver: Optional[str] = None,
        gpib_board_number: Optional[int] = None,
    ) -> Tuple[str, DeviceConfigEntry]:
        """Add a new device configuration entry.

        Args:
            device_type: The specific device type defined in the config entry.
            address: The address used to connect to the device:
                TCPIP: IP address or the hostname.
                SOCKET: IP address or the hostname (must define `lan_port` field).
                REST_API: IP address or the hostname (must define `lan_port` field).
                SERIAL/ASRL: serial COM port number.
                USB: use expression format f"{model}-{serial_number}" (ex: "MSO24-ABC0123").
            connection_type: The specific type of connection defined in the config entry.
            alias: An optional key/name used to retrieve this device from the DeviceManager.
            lan_port: The port number to connect on, used for SOCKET/REST_API connections.
            lan_device_name: The LAN device name to connect on, only used for TCPIP connections.
                The default is 'inst0'.
            serial_config: A dataclass for holding serial connection info.
            device_driver: A string indicating the specific Python device driver to use.
            gpib_board_number: The GPIB board number (also referred to as a controller), only used
                for GPIB connections. The default is 0.

        Returns:
            Tuple of the config entry name and the new DeviceConfigEntry

        Raises:
            ValueError: invalid config options, trouble creating (or a duplicate) device entry.
        """
        device_type = cast("DeviceTypes", device_type)
        connection_type = cast("ConnectionTypes", connection_type)
        # device and connection type conversion to enum from string is handled on initialization
        new_entry = DeviceConfigEntry(
            device_type=device_type,
            address=address,
            connection_type=connection_type,
            alias=alias,
            lan_port=lan_port,
            lan_device_name=lan_device_name,
            serial_config=serial_config,
            device_driver=device_driver,
            gpib_board_number=gpib_board_number,
        )
        # Currently, USB connections when using the PyVISA-py backend are not supported.
        if self.__options.standalone and new_entry.connection_type in {
            ConnectionTypes.USB,
            ConnectionTypes.GPIB,
        }:
            message = (
                f"{new_entry.connection_type.value} connections using PyVISA-py (standalone) "
                f"are not supported.\n{new_entry}"
            )
            raise ValueError(message)

        # Validate the connection is unique
        for dev_entry in self.__devices.values():
            new_entry_potential_hostname = new_entry.address.split(".")[0]
            dev_entry_potential_hostname = dev_entry.address.split(".")[0]
            if (new_entry.get_address_expression() == dev_entry.get_address_expression()) or (
                new_entry_potential_hostname == dev_entry_potential_hostname
                and not (
                    new_entry_potential_hostname.isdigit() or dev_entry_potential_hostname.isdigit()
                )
            ):
                message = (
                    f"Found duplicate addresses in the "
                    f'configuration for "{new_entry.get_address_expression()}":'
                    f"\n\t    Entry 1: {dev_entry}\n\tNew Entry 2: {new_entry}"
                )
                raise ValueError(message)

        # increment count
        self.__dev_count[new_entry.device_type.value] += 1
        device_number = self.__dev_count[new_entry.device_type.value]
        new_entry_name = f"{new_entry.device_type.value} {device_number}"
        # store the new entry
        self.__devices[new_entry_name] = new_entry
        if new_entry.alias:
            self.__devices[new_entry.alias] = new_entry
        return new_entry_name, new_entry

    def load_config_file(
        self, config_file_path: Optional[Union[str, os.PathLike[str]]] = None
    ) -> None:
        """Load in the config file located at the given path.

        This method will update any changed options and add any newly defined devices.

        Args:
            config_file_path: The path to the config file to load.
        """
        # Grabs path from environment variable with fallback to the default path
        file_path = config_file_path if config_file_path else self.defined_config_file_path
        # Automatically handles toml and yaml
        options, devices_list = self.__parse_config_file(file_path)
        self.__add_from_device_list(devices_list)
        self.update_options(options)

    def remove_device(self, device_name: str) -> None:
        """Remove a device from the configuration.

        Args:
            device_name: The name of the device to remove from the internal dictionary.
        """
        del self.__devices[device_name]

    def to_config_file_text(self, file_type: ConfigFileType = ConfigFileType.YAML) -> str:
        """Return string representation of instance as config file contents.

        Args:
            file_type: The type of file to create, yaml or toml.
        """
        # order of dict matters to match auto-formatted toml and yaml
        if file_type == self.FileType.TOML:
            retval = tomli_w.dumps(
                {
                    "devices": [dev.to_dict(ignore_none=True) for dev in self.devices.values()],
                    "options": self.options.to_dict(ignore_none=True),
                }
            )
        else:
            retval = yaml.dump(
                {
                    "options": self.options.to_dict(ignore_none=True),
                    "devices": [dev.to_dict(ignore_none=True) for dev in self.devices.values()],
                }
            )
            # add document header
            retval = "---\n" + retval
            # add extra spacing under devices section
            devs_idx = retval.find("devices:") + 8
            opts_idx = retval.find("options:") - 1
            retval = retval.replace(
                retval[devs_idx:opts_idx], retval[devs_idx:opts_idx].replace("\n", "\n  ")
            )
        return retval

    def update_options(self, new_options: DMConfigOptions) -> None:
        """Update the current configuration options.

        This ensures that any time new options are loaded in only explicitly defined options will be
        updated.

        Args:
            new_options: The new options to merge with the current options.
        """
        self.__options = dataclasses.replace(
            self.__options,
            **new_options.to_dict(ignore_none=True),
        )

    def write_config_to_file(
        self, config_file_path: Optional[Union[str, os.PathLike[str]]] = None
    ) -> str:
        """Write the current configuration to a config file.

        This method will overwrite any existing config file with the current devices and options. If
        no custom path is provided, it will write to the file defined by
        [`DMConfigParser.defined_config_file_path`][tm_devices.components.DMConfigParser.defined_config_file_path].

        Args:
            config_file_path: The path to the config file. If ends in ".toml" will create toml file.

        Returns:
            Path to the written file.
        """
        if config_file_path is None:
            config_file_path = self.defined_config_file_path

        config_path_obj = pathlib.Path(config_file_path)

        file_type = (
            DMConfigParser.FileType.TOML
            if config_path_obj.as_posix().lower().endswith(".toml")
            else DMConfigParser.FileType.YAML
        )
        config_path_obj.write_text(self.to_config_file_text(file_type=file_type), encoding="utf-8")

        return config_path_obj.as_posix()

    ################################################################################################
    # Private Methods
    ################################################################################################
    def __add_from_device_list(self, devices_list: List[Dict[str, Any]]) -> None:
        """Add devices from a list to the current config.

        Args:
            devices_list: The list of devices to add to the current config.
        """
        for entry in devices_list:
            # Instantiate nested classes from fields that store kwargs-style dictionaries
            for to_class, entry_key in self._CONFIG_NESTED_DICT_MAPPING.items():
                if config_dict := entry.get(entry_key):
                    # noinspection PyArgumentList
                    entry[entry_key] = to_class(**config_dict)
            self.add_device(**entry)

    def __parse_env_options(self) -> DMConfigOptions:
        """Extract the options flags from the env variable TM_OPTIONS.

        Returns:
            Dataclass of config options/flags.

        Raises:
            KeyError: Indicates unrecognized option name.
        """
        options_dict = {
            arg.strip().split("=", maxsplit=1)[0]: bool(arg)
            if "=" not in arg
            else arg.split("=", maxsplit=1)[-1]
            for arg in os.getenv(self.OPTIONS_ENV_VARIABLE, "").split(",")
            if arg
        }
        valid_config_options = {option.upper() for option in get_type_hints(DMConfigOptions)}
        if valid_config_options.issuperset(options_dict):
            options = {
                arg_name.lower(): int(options_dict[arg_name])
                if isinstance(options_dict[arg_name], str) and options_dict[arg_name].isdigit()  # pyright: ignore[reportUnknownMemberType,reportAttributeAccessIssue]
                else options_dict[arg_name]
                for arg_name in options_dict
            }
            return DMConfigOptions(**options)  # pyright: ignore[reportArgumentType]
        msg = (
            f"Invalid configuration options found: {list(set(options_dict) - valid_config_options)}"
        )
        raise KeyError(msg)

    def __parse_env_devices(self) -> List[Dict[str, Any]]:
        """Extract list of device configuration dictionaries from the env variable TM_DEVICES.

        Returns:
            List of device entry dictionaries.

        Raises:
            ValueError: invalid string formatting cannot be parsed.
        """
        devices_str_list = [
            arg.strip() for arg in os.getenv(self.DEVICES_ENV_VARIABLE, "").split("~~~") if arg
        ]
        retval: List[Dict[str, Any]] = []
        msg: List[str] = []
        for dev_entry in devices_str_list:
            temp_dict: Dict[str, Any] = {}
            for dev_arg in dev_entry.split(","):
                try:
                    dev_key, dev_val = dev_arg.split("=", 1)
                    temp_dict[dev_key] = dev_val
                except ValueError:  # noqa: PERF203
                    msg.append(
                        f'Expected device defined like "device_type=SCOPE,address=1.2.3.4,...",\n'
                        f'cannot parse "{dev_entry}"'
                    )
            retval.append(temp_dict)
        if msg:
            raise ValueError("\n".join(msg))
        return retval

    @staticmethod
    def __parse_config_file(
        config_file_path: Union[str, os.PathLike[str]],
    ) -> Tuple[DMConfigOptions, List[Dict[str, Any]]]:
        """Parse config file for the options flags and list of device configuration dictionaries.

        Args:
            config_file_path: The path to the config file to load.

        Returns:
            Tuple with dataclass of config options/flags and list of device entry dictionaries.

        Raises:
            FileNotFoundError: if the defined config file does not exist.
            KeyError: Indicates unrecognized option name.
        """
        config_path = pathlib.Path(config_file_path)  # normalize the path
        if not config_path.is_file():
            raise FileNotFoundError(config_path)
        # read in data
        with config_path.open(encoding="utf-8") as config_file:
            if config_path.suffix == ".toml":
                data = tomli.loads(config_file.read())
            else:  # ["yaml", "yml"]
                data = yaml.safe_load(config_file)
        # return data with some pre-processing
        options_mapping = data.get("options", {})
        try:
            options = DMConfigOptions(**options_mapping)
        except TypeError:
            options_list = list(options_mapping)
            valid_options = set(get_type_hints(DMConfigOptions))
            msg = f"Invalid configuration options found: {list(set(options_list) - valid_options)}"
            raise KeyError(msg)  # noqa: B904
        devices_list = data.get("devices", [])
        return options, devices_list

    def __pre_process_env_devices(self, devices_list: List[Dict[str, Any]]) -> None:
        """Modify device entries in place to make env data mimic toml/yaml parser output format."""
        for entry in devices_list:
            # Bundle any prefixed pairs into a nested kwarg-style dict.
            for to_class, prefix in CONFIG_CLASS_STR_PREFIX_MAPPING.items():
                config_dict: Dict[str, str]
                if config_dict := {
                    key.replace(prefix, ""): entry.pop(key)
                    for key in list(entry.keys())
                    if key.startswith(prefix)
                    and (key not in self._CONFIG_NESTED_DICT_MAPPING.values())
                }:
                    # assign the dict to the correct key via the class the prefix represented
                    entry[self._CONFIG_NESTED_DICT_MAPPING[to_class]] = config_dict
