"""A mixin class that contains common methods for checking the PI device for SYSTEM:ERROR."""

from abc import ABC
from typing import List, Tuple, Union

from tm_devices.driver_mixins.device_control.pi_control import PIControl
from tm_devices.helpers import print_with_timestamp, raise_failure, verify_values


class CommonPISystemErrorCheckMixin(PIControl, ABC):
    """A mixin class that contains common methods for checking the PI device for SYSTEM:ERROR.

    !!! note
        This class also inherits from the
        [`PIControl`][tm_devices.driver_mixins.device_control.pi_control.PIControl] mixin and
        therefore provides access to the PI control methods.
    """

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
            verify_values(self._name_and_alias, esr, esr_result_str)
        except AssertionError as exc:
            result &= False
            print(exc)  # the exception already contains the timestamp

        # return the errors if any
        returned_errors = ""
        error = ""
        while error != no_error:
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
        result = int(self.query("*ESR?").strip())

        # return the errors if any
        returned_errors: List[str] = []
        error = ""
        while error != '0,"No error"':
            error = self.query("SYSTEM:ERROR?")
            returned_errors.append(error)

        return result, tuple(returned_errors)
