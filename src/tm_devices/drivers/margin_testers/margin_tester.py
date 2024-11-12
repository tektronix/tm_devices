"""Base Margin Tester device driver module."""

from __future__ import annotations

import os
import time

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Mapping, MutableMapping, Tuple, TYPE_CHECKING, Union

from requests.structures import CaseInsensitiveDict

from tm_devices.driver_mixins.device_control import RESTAPIControl
from tm_devices.drivers.device import Device, family_base_class
from tm_devices.helpers import DeviceConfigEntry, DeviceTypes
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

if TYPE_CHECKING:
    from packaging.version import Version


@family_base_class
class MarginTester(Device, RESTAPIControl, ABC):
    """Base Margin Tester device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(self, config_entry: DeviceConfigEntry, verbose: bool) -> None:
        """Create a TMT4 device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed. If True,
                communication printouts will be logged with a level of INFO. If False,
                communication printouts will be logged with a level of DEBUG.
        """
        super().__init__(config_entry, verbose)

        self._auth_token_file_path: Path = Path()

    ################################################################################################
    # Abstract Cached Properties
    ################################################################################################
    @cached_property
    @abstractmethod
    def adapter(self) -> str:
        """Return the device's connected adapter."""

    @cached_property
    @abstractmethod
    def fpga_version(self) -> Version:
        """Return the fpga version of the device."""

    @cached_property
    @abstractmethod
    def fw_version(self) -> Version:
        """Return the firmware version of the device."""

    @cached_property
    @abstractmethod
    def supported_technologies(self) -> Tuple[str, ...]:
        """Return the device's supported technologies."""

    ################################################################################################
    # Abstract Methods
    ################################################################################################
    @abstractmethod
    def request_about_info(self, verbose: bool = True) -> Dict[str, Any]:
        """Make a get request to 'about' and 'version' endpoints and return device information.

        Args:
            verbose: A boolean indicating if verbose output should be printed.
        """

    @abstractmethod
    def wait_till_unlocked(self, timeout: int = 30) -> None:
        """Wait until the device becomes unlocked.

        Args:
            timeout: The timeout to wait for an unlocked device in seconds.

        Raises:
            TimeoutError: If the device does not unlock within the timeout.
        """

    ################################################################################################
    # Properties
    ################################################################################################
    @cached_property
    def device_type(self) -> str:
        """Return a string representing the device type."""
        return DeviceTypes.MT.value

    @property
    def auth_token_file_path(self) -> str:
        """Return the path to the file containing the auth token."""
        return self._auth_token_file_path.as_posix()

    @auth_token_file_path.setter
    def auth_token_file_path(self, value: Union[str, os.PathLike[str]]) -> None:
        """Set the path to the file containing the auth token."""
        self._auth_token_file_path = Path(value)

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _close(self) -> None:
        """Close this device and all its used resources and components."""
        # This currently isn't needed for Margin Tester devices.
        self._is_open = False

    def _generate_headers(self) -> Mapping[str, str]:
        """Generate headers using a user provided auth token file.

        Returns:
            The header dictionary.

        Raises:
            AssertionError: Indicates that no auth token file is available.
        """
        if not (
            self._auth_token_file_path
            and self._auth_token_file_path.exists()
            and self._auth_token_file_path.is_file()
        ):
            msg = (
                "No auth token file set! Please set the ``.auth_token_file_path`` attribute "
                "to point to a file with an authorization token."
            )
            raise AssertionError(msg)
        headers: MutableMapping[str, str] = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        token = self._auth_token_file_path.read_text(encoding="utf-8").replace("\n", "")
        headers["Authorization"] = f"Bearer {token}"
        return headers

    def _get_errors(self) -> Tuple[int, Tuple[str, ...]]:
        """Get the current errors from the device.

        !!! note
            This method will clear out the error queue after reading the current errors.

        Returns:
            A tuple containing the current error code alongside a tuple of the current error
                messages.
        """
        return 0, ()

    def _open(self) -> bool:
        """Open necessary resources and components."""
        # Simply wait for the network connection, that indicates the device is open.
        time.sleep(15)
        self._is_open = self.wait_for_network_connection(
            120,
            accept_immediate_connection=bool(os.environ.get("TM_DEVICES_UNIT_TESTS_RUNNING")),
        )
        self._is_open &= self.wait_for_api_connection(
            120,
            accept_immediate_connection=True,
        )
        return self._is_open
