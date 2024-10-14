"""A mixin class that contains common methods for checking the TSP device for errors."""

from abc import ABC
from typing import Tuple, Union

from tm_devices.driver_mixins.device_control.tsp_control import TSPControl
from tm_devices.helpers import print_with_timestamp, raise_failure, verify_values


class CommonTSPErrorCheckMethods(TSPControl, ABC):
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
            error_string = '0,"No events to report - queue empty"'

        # Verify that an allev reply is specified
        if not error_string:
            raise AssertionError("No error string was provided.")  # noqa: TRY003,EM101

        result = True
        esr_result_str = self.query("print(status.standard.event)")
        try:
            verify_values(self._name_and_alias, esr, esr_result_str)
        except AssertionError as exc:
            result &= False
            print(exc)  # the exception already contains the timestamp
        _, allev_result_str = self.get_eventlog_status()

        if allev_result_str != error_string:
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

    def get_eventlog_status(self) -> Tuple[bool, str]:
        """Help function for getting the eventlog status.

        Returns:
            Boolean indicating no error, String containing concatenated contents of event log.
        """
        result_allev = False
        allev_result_str = '0,"No events to report - queue empty"'

        # instrument returns exponential numbers so converting to float before int
        if not (err_count := int(float(self.query("print(errorqueue.count)")))):
            result_allev = True
        else:
            allev_result_list = [self.query("print(errorqueue.next())") for _ in range(err_count)]
            allev_result_str = ",".join(allev_result_list)
        return result_allev, allev_result_str
