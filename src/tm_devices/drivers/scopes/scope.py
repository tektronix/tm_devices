"""Base Scope device driver module."""

from abc import ABC, abstractmethod
from typing import Tuple, Union

from tm_devices.driver_mixins.device_control.pi_control import PIControl
from tm_devices.drivers.device import Device
from tm_devices.helpers import DeviceTypes, raise_failure, verify_values
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


# TODO: nfelt14: remove PIControl inheritance if possible
class Scope(PIControl, Device, ABC):
    """Base Scope device driver."""

    _DEVICE_TYPE = DeviceTypes.SCOPE.value

    ################################################################################################
    # Abstract Properties
    ################################################################################################
    @cached_property
    @abstractmethod
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""

    ################################################################################################
    # Abstract Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def all_channel_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the channel names."""
        return tuple(f"CH{x+1}" for x in range(self.total_channels))

    @cached_property
    def opt_string(self) -> str:
        r"""Return the string returned from the ``*OPT?`` query when the device was created."""
        return self.ieee_cmds.opt()

    ################################################################################################
    # Public Methods
    ################################################################################################
    def expect_esr(self, esr: Union[int, str], error_string: str = "") -> Tuple[bool, str]:
        r"""Check for the expected number of errors and output string.

        Sends the ``*ESR?`` and ALLEV? queries.

        Args:
            esr: Expected ``*ESR?`` value
            error_string: Expected error buffer string.
                Multiple errors should be separated by a \n character

        Returns:
            Boolean indicating if the check passed or failed and a string with the results.
        """
        failure_message = ""
        if not int(esr):
            error_string = '0,"No events to report - queue empty"'

        # Verify that an allev reply is specified
        if not error_string:
            raise AssertionError("No error string was provided.")  # noqa: TRY003,EM101

        result = True
        esr_result_str = self.ieee_cmds.esr()
        try:
            verify_values(self._name_and_alias, esr, esr_result_str)
        except AssertionError as exc:
            result &= False
            print(exc)  # the exception already contains the timestamp
        allev_result_str = self.query(":ALLev?")
        try:
            verify_values(self._name_and_alias, error_string, allev_result_str)
        except AssertionError as exc:
            result &= False
            print(exc)  # the exception already contains the timestamp

        if not result:
            failure_message = (
                f"expect_esr failed: *ESR? {esr_result_str!r} != {esr!r}, "
                f":ALLev? {allev_result_str!r} != {error_string!r}"
            )
            raise_failure(self._name_and_alias, failure_message)

        return result, failure_message

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _get_errors(self) -> Tuple[int, Tuple[str, ...]]:
        """Get the current errors from the device.

        !!! note
            This method will clear out the error queue after reading the current errors.

        Returns:
            A tuple containing the current error code alongside a tuple of the current error
            messages.
        """
        result = int(self.query("*ESR?").strip())
        allev_list = [
            x + ('"' if not x.endswith('"') else "") for x in self.query(":ALLev?").split('",')
        ]
        returned_errors = tuple(filter(None, allev_list))

        return result, returned_errors
