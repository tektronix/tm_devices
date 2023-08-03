"""Base Margin Tester device driver module."""
import os
import time

from abc import ABC, abstractmethod
from functools import cached_property
from typing import Any, Dict, Mapping, MutableMapping, Tuple

from packaging.version import Version
from requests.structures import CaseInsensitiveDict

from tm_devices.drivers.api.rest_api.rest_api_device import RESTAPIDevice
from tm_devices.drivers.device import family_base_class
from tm_devices.helpers import DeviceConfigEntry, DeviceTypes


@family_base_class
class MarginTester(RESTAPIDevice, ABC):
    """Base Margin Tester device driver."""

    _DEVICE_TYPE = DeviceTypes.MT.value

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(self, config_entry: DeviceConfigEntry, verbose: bool) -> None:
        """Create a TMT4 device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
        """
        super().__init__(config_entry, verbose)

        self._auth_token_file_path = ""

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
            TimeoutError if device does not unlock within timeout.
        """

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def auth_token_file_path(self) -> str:
        """Return the path to the file containing the auth token."""
        return self._auth_token_file_path

    @auth_token_file_path.setter
    def auth_token_file_path(self, value: str) -> None:
        """Set the path to the file containing the auth token."""
        self._auth_token_file_path = value

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
        if not self._auth_token_file_path:
            msg = (
                "No auth token file set! Please set the ``.auth_token_file_path`` attribute "
                "to point to a file with an authorization token."
            )
            raise AssertionError(msg)
        headers: MutableMapping[str, str] = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        with open(self._auth_token_file_path, encoding="utf-8") as auth_file:
            token = auth_file.read().replace("\n", "")
        headers["Authorization"] = f"Bearer {token}"
        return headers

    def _has_errors(self) -> bool:
        """Check if the device has any errors.

        Returns:
            A boolean indicating if any errors were found in the device.
        """
        # TODO: implement
        return False

    def _open(self) -> bool:
        """Open necessary resources and components."""
        # Simply wait for the network connection, that indicates the device is open.
        time.sleep(15)
        self._is_open = self.wait_for_network_connection(
            120,
            verbose=False,
            accept_immediate_connection=bool(os.environ.get("TM_DEVICES_UNIT_TESTS_RUNNING")),
        )
        self._is_open &= self.wait_for_api_connection(
            120,
            verbose=False,
            accept_immediate_connection=True,
        )
        return self._is_open
