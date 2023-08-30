"""Base Scope device driver module."""
import inspect

from abc import ABC
from functools import cached_property
from typing import Any, List, Optional, Tuple, Union

from tm_devices.drivers.pi.pi_device import PIDevice
from tm_devices.helpers import DeviceTypes


class Scope(PIDevice, ABC):
    """Base Scope device driver."""

    _DEVICE_TYPE = DeviceTypes.SCOPE.value

    ################################################################################################
    # Abstract Methods
    ################################################################################################
    def single_sequence(self) -> None:
        """Perform a single sequence.

        Raises:
            NotImplementedError: Indicates the current driver has not implemented this method.
        """
        # TODO: implement for all driver subclasses then convert to abstractmethod
        raise NotImplementedError(
            f"``.{inspect.currentframe().f_code.co_name}()``"  # pyright: ignore
            f" is not yet implemented for the {self.__class__.__name__} driver"
        )

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
    def curve_query(
        self,
        channel_num: int,
        wfm_type: str = "TimeDomain",
        output_csv_file: Optional[str] = None,
    ) -> List[Any]:
        """Perform a curve query on a specific channel.

        Args:
            channel_num: The channel number to perform the curve query on.
            wfm_type: The type of waveform to query.
            output_csv_file: An optional file path to a csv file to save the curve query data in.

        Raises:
            NotImplementedError: Indicates the current driver has not implemented this method.
        """
        raise NotImplementedError(
            f"``.{inspect.currentframe().f_code.co_name}()``"  # pyright: ignore
            f" is not yet implemented for the {self.__class__.__name__} driver"
        )

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
            self.verify_values(esr, esr_result_str)
        except AssertionError as exc:
            result &= False
            print(exc)  # the exception already contains the timestamp
        allev_result_str = self.query(":ALLev?")
        try:
            self.verify_values(error_string, allev_result_str)
        except AssertionError as exc:
            result &= False
            print(exc)  # the exception already contains the timestamp

        if not result:
            failure_message = (
                f"expect_esr failed: *ESR? {esr_result_str!r} != {esr!r}, "
                f":ALLev? {allev_result_str!r} != {error_string!r}"
            )
            self.raise_failure(failure_message)

        return result, failure_message

    def get_eventlog_status(self) -> Tuple[bool, str]:
        """Help function for getting the eventlog status.

        Returns:
            Boolean indicating no error, String containing concatenated contents of event log.
        """
        result = not int(self.query("*ESR?").strip())

        returned_errors = self.query(":ALLev?")

        return result, returned_errors
