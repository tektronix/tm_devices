"""A mixin class that contains common methods for checking the PI device for SYSTEM:ERROR."""

from abc import ABC
from typing import List, Tuple

from tm_devices.driver_mixins.device_control._abstract_device_visa_write_query_control import (
    _AbstractDeviceVISAWriteQueryControl,  # pyright: ignore[reportPrivateUsage]
)


class CommonPISystemErrorCheckMixin(_AbstractDeviceVISAWriteQueryControl, ABC):
    """A mixin class that contains common methods for checking the PI device for SYSTEM:ERROR.

    !!! important
        Any class that inherits this mixin must also inherit the
        [`PIControl`][tm_devices.driver_mixins.device_control.PIControl] mixin in order
        to have access to the methods required by this class.
    """

    @property
    def _no_error_string(self) -> str:
        """A string containing the expected error message when no error is present."""
        return '0,"No error"'

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
        while error != self._no_error_string:
            error = self.query("SYSTEM:ERROR?")
            returned_errors.append(error)

        return result, tuple(returned_errors)
