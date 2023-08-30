"""Base Source device driver module.

Sources include PI devices such as AFGs and AWGs.
"""
from abc import ABC, abstractmethod
from functools import cached_property
from typing import Tuple, Union

from tm_devices.driver_mixins.signal_generator_mixin import SignalGeneratorMixin
from tm_devices.drivers.pi.pi_device import PIDevice
from tm_devices.helpers import print_with_timestamp


class SignalSource(PIDevice, SignalGeneratorMixin, ABC):
    """Base Source device driver."""

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def all_channel_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the channel names."""
        return tuple(f"SOURCE{x+1}" for x in range(self.total_channels))

    @cached_property
    def opt_string(self) -> str:
        r"""Return the string returned from the ``*OPT?`` query when the device was created."""
        return self.ieee_cmds.opt()

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
        failure_message = ""
        no_error = '0,"No error"'
        if not int(esr):
            error_string = no_error

        # Verify that an allev reply is specified
        if not error_string:
            raise AssertionError("No error string was provided.")  # noqa: TRY003,EM101

        result = True
        esr_result_str = self.query("*ESR?")
        try:
            self.verify_values(esr, esr_result_str)
        except AssertionError as exc:
            result &= False
            print(exc)  # the exception already contains the timestamp

        # return the errors if any
        returned_errors = ""
        error = ""
        while error != '0,"No error"':
            error = str(self.query("SYSTEM:ERROR?"))
            returned_errors += error
            if error != no_error:
                returned_errors += "\n"

        if returned_errors != error_string:
            result &= False
            print_with_timestamp(
                f"FAILURE: ({self._name_and_alias}) : Incorrect SYSTEM:ERROR? returned:\n"
                f"  exp: {error_string!r}\n  act: {returned_errors!r}"
            )

        if not result:
            returned_errors = returned_errors.replace("\n", ", ")
            error_string = error_string.replace("\n", ", ")
            failure_message = (
                f"expect_esr failed: *ESR? {esr_result_str!r} != {esr!r}, "
                f"SYSTEM:ERROR? {returned_errors!r} != {error_string!r}"
            )
            self.raise_failure(failure_message)

        return result, failure_message

    def get_eventlog_status(self) -> Tuple[bool, str]:
        """Help function for getting the eventlog status.

        Returns:
            Boolean indicating no error, String containing concatenated contents of event log.
        """
        result = not int(self.query("*ESR?").strip())

        # return the errors if any
        returned_errors = ""
        error = ""
        while error != '0,"No error"':
            error = str(self.query("SYSTEM:ERROR?"))
            returned_errors += error

        return result, returned_errors.rstrip()

    ################################################################################################
    # Private Methods
    ################################################################################################
    @abstractmethod
    def _send_waveform(self, target_file: str) -> None:
        """Send the waveform information to the source as a file in memory.

        Args:
            target_file: The name of the waveform file.
        """
        raise NotImplementedError

    def _validate_channels(self, channel: str) -> Tuple[str, ...]:
        """Create a list of channels to use on the source based on the desired channel number.

        Args:
            channel: The channel name to output the signal from, or 'all'.

        Returns:
            A tuple containing the list of channels to use.
        """
        # Verify the channel given is valid
        if channel not in (valid_channels := ["all", *self.all_channel_names_list]):
            msg = f"Invalid channel name {channel!r}, valid items: {valid_channels}"
            raise AssertionError(msg)

        return self.all_channel_names_list if channel == "all" else (channel,)
