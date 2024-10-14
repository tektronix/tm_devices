"""A mixin class that contains common methods for checking the TSP device for errors."""

from abc import ABC
from typing import Tuple, Union

from tm_devices.driver_mixins.device_control.tsp_control import TSPControl
from tm_devices.helpers import print_with_timestamp, raise_failure, verify_values


class CommonTSPErrorCheckMixin(TSPControl, ABC):
    """A mixin class that contains common methods for checking the TSP device for errors.

    !!! note
        This class also inherits from the
        [`TSPControl`][tm_devices.driver_mixins.device_control.tsp_control.TSPControl] mixin and
        therefore provides access to the TSP control methods.
    """

    ################################################################################################
    # Public Methods
    ################################################################################################
    def expect_esr(self, esr: Union[int, str], error_string: str = "") -> Tuple[bool, str]:
        r"""Check for the expected number of errors and output string.

        Sends the equivalent of ``*ESR?`` and system error queries.

        Args:
            esr: Expected ``*ESR?`` value.
            error_string: Expected error buffer string.
                Multiple errors should be separated by a \n character.

        Returns:
            Boolean indicating if the check passed or failed and a string with the results.
        """
        failure_message = ""
        if not int(esr):
            # TODO: nfelt14: Update this default error string
            error_string = ""

        # Verify that an allev reply is specified when expecting an error
        if int(esr) and not error_string:
            raise AssertionError("No error string was provided.")  # noqa: TRY003,EM101

        result = True
        esr_result_str = self.query("print(status.standard.event)")
        try:
            verify_values(self._name_and_alias, esr, esr_result_str)
        except AssertionError as exc:
            result &= False
            print(exc)  # the exception already contains the timestamp
        _, allev_result_tuple = self._get_errors()
        if (allev_result_str := ",".join(allev_result_tuple)) != error_string:
            result &= False
            print_with_timestamp(
                f"FAILURE: ({self._name_and_alias}) : Incorrect eventlog status returned:\n"
                f"  exp: {error_string!r}\n  act: {allev_result_str!r}"
            )

        if not result:
            failure_message = (
                f"expect_esr failed: "
                f"print(status.standard.event) {esr_result_str!r} != {esr!r}, "
                f"eventlog {allev_result_str!r} != {error_string!r}"
            )
            raise_failure(self._name_and_alias, failure_message)

        return result, failure_message

    def _get_errors(self) -> Tuple[int, Tuple[str, ...]]:
        """Get the current errors from the device.

        !!! note
            This method will clear out the error queue after reading the current errors.

        Returns:
            A tuple containing the current error code alongside a tuple of the current error
            messages.
        """
        # instrument returns exponential numbers so converting to float before int
        err_count = int(float(self.query("print(errorqueue.count)")))
        error_message_list = []
        if err_count:
            error_message_list = [self.query("print(errorqueue.next())") for _ in range(err_count)]
        return err_count, tuple(filter(None, error_message_list))
