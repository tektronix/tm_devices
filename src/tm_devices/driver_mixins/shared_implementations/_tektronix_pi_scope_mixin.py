"""A private mixin for common methods and attributes for Tektronix scopes."""

from abc import ABC
from typing import Tuple

from tm_devices.driver_mixins.device_control._abstract_device_visa_write_query_control import (
    _AbstractDeviceVISAWriteQueryControl,  # pyright: ignore[reportPrivateUsage]
)


class _TektronixPIScopeMixin(_AbstractDeviceVISAWriteQueryControl, ABC):  # pyright: ignore[reportUnusedClass]
    """A private mixin for common methods and attributes for Tektronix scopes.

    !!! important
        Any class that inherits this mixin must also inherit the
        [`PIControl`][tm_devices.driver_mixins.device_control.PIControl] mixin in order
        to have access to the methods required by this class.
    """

    @property
    def _no_error_string(self) -> str:
        """A string containing the expected error message when no error is present."""
        return '0,"No events to report - queue empty"'

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
