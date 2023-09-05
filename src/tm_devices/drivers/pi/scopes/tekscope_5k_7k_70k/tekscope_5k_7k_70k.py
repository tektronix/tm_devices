"""Base TekScope5k7k70k scope device driver module."""
from abc import ABC
from functools import cached_property

import pyvisa as visa

from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.pi.scopes.scope import Scope
from tm_devices.helpers import DeviceConfigEntry


@family_base_class
class TekScope5k7k70k(Scope, ABC):
    """Base TekScope5k7k70k scope device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a TekScope5k7k70k device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        super().__init__(config_entry, verbose, visa_resource)
        self.write("HEADER OFF", verbose=False)
        # Extract the numeric part as string from the model number
        digits = "".join(char for char in self.model if char.isdigit())
        # Last digit represents the channel number.
        self._total_channels: int = int(digits[-1])
        # Check for models starting with MSO, as these models only offer digital channels.
        if self.model.startswith("MSO"):
            self._num_dig_bits_in_ch: int = 16
        else:
            self._num_dig_bits_in_ch = 0

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def num_dig_bits_in_ch(self) -> int:
        """Return the number of digital bits expected in a digital channel."""
        # TODO: should be part of self.channel
        return self._num_dig_bits_in_ch

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        return self._total_channels

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _reboot(self) -> None:
        """Perform the actual rebooting code."""
        # TODO: implement
        raise NotImplementedError(
            f"``.reboot()`` is not yet implemented for the {self.__class__.__name__} driver"
        )
