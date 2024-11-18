"""A mixin class that contains common methods for checking the TSP device for errors."""

from abc import ABC
from typing import Tuple

from tm_devices.driver_mixins.device_control._abstract_device_visa_write_query_control import (
    _AbstractDeviceVISAWriteQueryControl,  # pyright: ignore[reportPrivateUsage]
)


class CommonTSPErrorCheckMixin(_AbstractDeviceVISAWriteQueryControl, ABC):
    """A mixin class that contains common methods for checking the TSP device for errors.

    !!! important
        Any class that inherits this mixin must also inherit the
        [`TSPControl`][tm_devices.driver_mixins.device_control.TSPControl] mixin in
        order to have access to the methods required by this class.
    """

    def _get_errors(self) -> Tuple[int, Tuple[str, ...]]:
        """Get the current errors from the device.

        !!! note
            This method will clear out the error queue after reading the current errors.

        Returns:
            A tuple containing the current error code alongside a tuple of the current error
                messages.
        """
        # instrument returns exponential numbers so converting to float before int
        error_code = int(float(self.query("print(status.standard.event)")))
        err_count = int(float(self.query("print(errorqueue.count)")))
        error_message_list = []
        if err_count:
            error_message_list = [self.query("print(errorqueue.next())") for _ in range(err_count)]
        return error_code, tuple(filter(None, error_message_list))
