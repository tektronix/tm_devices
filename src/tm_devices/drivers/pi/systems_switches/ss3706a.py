"""SS3706A device driver module."""
import inspect

from functools import cached_property
from typing import Tuple

import pyvisa as visa

from tm_devices.commands import SS3706AMixin
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.pi.systems_switches.systems_switch import SystemsSwitch
from tm_devices.helpers import DeviceConfigEntry


@family_base_class
class SS3706A(SS3706AMixin, SystemsSwitch):
    """SS3706A device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a SS3706A device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        super().__init__(config_entry, verbose, visa_resource)

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def all_channel_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the channel names."""
        return tuple(f"{x+1}" for x in range(self.total_channels))

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        return 576

    ################################################################################################
    # Public Methods
    ################################################################################################
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
