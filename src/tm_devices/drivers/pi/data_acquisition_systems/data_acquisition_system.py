"""Base Data Acquisition (DAQ) device driver module."""
import inspect

from abc import ABC

from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.pi.tsp_device import TSPDevice
from tm_devices.helpers import DeviceTypes


@family_base_class
class DataAcquisitionSystem(TSPDevice, ABC):
    """Base Data Acquisition (DAQ) device driver."""

    _DEVICE_TYPE = DeviceTypes.DAQ.value

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
