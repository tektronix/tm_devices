"""TSOVu device driver module."""

import pyvisa as visa

from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.pi.scopes.scope import Scope
from tm_devices.helpers import DeviceConfigEntry


@family_base_class
class TSOVu(Scope):
    """TSOVu device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
    ) -> None:
        """Create a TSOVu device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        super().__init__(config_entry, verbose, visa_resource)
        self.write("HEADER OFF", verbose=False)

    ################################################################################################
    # Private Methods
    ################################################################################################
