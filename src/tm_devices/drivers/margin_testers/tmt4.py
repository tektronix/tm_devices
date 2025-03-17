"""TMT4 series device driver module."""

import time

from types import MappingProxyType
from typing import Any, cast, Dict, Mapping, Optional, Tuple

from packaging.version import Version

from tm_devices.drivers.margin_testers.margin_tester import MarginTester
from tm_devices.helpers import DeviceConfigEntry
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


class TMT4(MarginTester):
    """TMT4 series device driver."""

    API_VERSIONS: Mapping[int, str] = MappingProxyType({1: "/api"})
    """A mapping of supported API version numbers with the corresponding API URL."""

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

        Notes:
            The default port is 5000, but device could be configured for any specific port.
        """
        super().__init__(config_entry, verbose)

        # The URL to use for REST API requests
        # noinspection HttpUrlsUsage
        self._base_url = f"http://{self.ip_address}:{self.port}"
        self.set_api_version(1)

        # Make get request to about and version endpoints
        self._about_info = self.request_about_info(verbose=False)

    ################################################################################################
    # Properties
    ################################################################################################
    @cached_property
    def adapter(self) -> str:
        """Return the device's connected adapter."""
        return self._about_info["adapter"]

    @cached_property
    def fpga_version(self) -> Version:
        """Return the fpga version of the device."""
        # This key can return strings indicating a reboot is needed instead of Versions.
        try:
            return Version(self._about_info["fpga_version"])
        except ValueError:
            return Version("0")

    @cached_property
    def fw_version(self) -> Version:
        """Return the firmware version of the device."""
        # This key can (also) return strings indicating a reboot is needed instead of Versions.
        try:
            return Version(self._about_info["fw_version"])
        except ValueError:
            return Version("0")

    @cached_property
    def manufacturer(self) -> str:
        """Return the manufacturer of the device."""
        return self._about_info["manufacturer"]

    @cached_property
    def model(self) -> str:
        """Return the full model of the device."""
        return self._about_info["model"]

    @property
    def port(self) -> Optional[int]:
        """Return the configured device port, defaults to 5000."""
        return super().port or 5000

    @cached_property
    def serial(self) -> str:
        """Return the serial number of the device."""
        return self._about_info["serialNumber"]

    @cached_property
    def supported_technologies(self) -> Tuple[str, ...]:
        """Return the device's supported technologies."""
        return tuple(self._about_info["supportedTechnologies"].split(","))

    @cached_property
    def sw_version(self) -> Version:
        """Return the software version of the device."""
        return Version(self._about_info["sw_version"])

    ################################################################################################
    # Public Methods
    ################################################################################################
    def request_about_info(self, verbose: bool = True) -> Dict[str, Any]:
        """Make a get request to the 'about' endpoint and return the device information.

        Args:
            verbose: A boolean indicating if verbose output should be printed.

        Returns:
            A Dictionary with information about the Margin device.
        """
        # Make get request to about and version endpoints
        with self.temporary_verbose(verbose):
            _, res_json, _, _ = self.get("/device/about")
            res_json = cast("Dict[str, Any]", res_json)
            _, res_json2, _, _ = self.get("/device/version")
            res_json2 = cast("Dict[str, Any]", res_json2)
            res_json.update(res_json2)
        return res_json

    def wait_till_unlocked(self, timeout: int = 120) -> None:
        """Wait until the device becomes unlocked.

        Args:
            timeout: The timeout to wait for an unlocked device in seconds.

        Raises:
            TimeoutError: If the device does not unlock within the timeout.
        """
        start = time.time()
        while time.time() < start + timeout:
            _, res_json, _, _ = self.get("/device/status", allow_errors=True)
            if res_json["usage"] == "NOT LOCKED":  # pyright: ignore[reportArgumentType,reportCallIssue]
                return
            time.sleep(1)
        msg = f"waited more than {timeout} seconds for {self.name} to unlock"
        raise TimeoutError(msg)

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _check_api_connection(self) -> bool:
        """Make any call to the API to check if there is a connection.

        Returns:
            A boolean indicating if the call was successful.
        """
        with self.temporary_verbose(False):
            # allow_errors is set to True since this is just checking if the API is reachable
            return self.get("/device/about", allow_errors=True)[0]

    def _cleanup(self) -> None:
        """Perform the cleanup defined for the device."""
