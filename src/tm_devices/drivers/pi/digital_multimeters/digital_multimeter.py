"""Base Digital Multimeter (DMM) device driver module."""
import inspect

from abc import ABC

from tm_devices.drivers.pi.tsp_device import TSPDevice
from tm_devices.helpers import DeviceTypes


class DigitalMultimeter(TSPDevice, ABC):
    """Base Digital Multimeter (DMM) device driver."""

    _DEVICE_TYPE = DeviceTypes.DMM.value

    ################################################################################################
    # Properties
    ################################################################################################

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _reboot(self) -> None:
        """Perform the actual rebooting code.

        Raises:
            NotImplementedError: Indicates the current driver has not implemented this method.
        """
        # TODO: implement
        raise NotImplementedError(
            f"``.{inspect.currentframe().f_code.co_name}()``"  # pyright: ignore
            f" is not yet implemented for the {self.__class__.__name__} driver"
        )
