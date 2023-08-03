"""Base Power Supply Unit (PSU) device driver module.

PSUs include PI devices.
"""
from abc import ABC
from typing import Tuple, Union

from tm_devices.drivers.pi.pi_device import PIDevice
from tm_devices.drivers.pi.signal_sources.signal_source import SignalSource
from tm_devices.helpers import DeviceTypes


class PowerSupplyUnit(PIDevice, ABC):
    """Base Power Supply Unit (PSU) device driver."""

    _DEVICE_TYPE = DeviceTypes.PSU.value

    ################################################################################################
    # Public Methods
    ################################################################################################
    def expect_esr(self, esr: Union[int, str], error_string: str = "") -> Tuple[bool, str]:
        r"""Check for the expected number of errors and output string.

        Sends the ``*ESR?`` and SYSTEM:ERROR? queries.

        Args:
            esr: Expected ``*ESR?`` value
            error_string: Expected error buffer string.
                Multiple errors should be separated by a \n character

        Returns:
            Boolean indicating if the check passed or failed and a string with the results.
        """
        return SignalSource.expect_esr(self, esr, error_string)  # type: ignore

    def get_eventlog_status(self) -> Tuple[bool, str]:
        """Help function for getting the eventlog status.

        Returns:
            Boolean indicating no error, String containing concatenated contents of event log.
        """
        return SignalSource.get_eventlog_status(self)  # type: ignore
