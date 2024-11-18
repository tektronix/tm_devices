"""TSOVu device driver module."""

import pyvisa as visa

from tm_devices.driver_mixins.device_control import PIControl
from tm_devices.driver_mixins.shared_implementations._tektronix_pi_scope_mixin import (
    _TektronixPIScopeMixin,  # pyright: ignore[reportPrivateUsage]
)
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.scopes.scope import Scope
from tm_devices.helpers import DeviceConfigEntry
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


@family_base_class
class TSOVu(_TektronixPIScopeMixin, PIControl, Scope):
    """TSOVu device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
        default_visa_timeout: int,
    ) -> None:
        """Create a TSOVu device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed. If True,
                communication printouts will be logged with a level of INFO. If False,
                communication printouts will be logged with a level of DEBUG.
            visa_resource: The VISA resource object.
            default_visa_timeout: The default VISA timeout value in milliseconds.
        """
        super().__init__(config_entry, verbose, visa_resource, default_visa_timeout)
        self.write("HEADER OFF", verbose=False)

    ################################################################################################
    # Properties
    ################################################################################################
    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels."""
        return 0

    ################################################################################################
    # Private Methods
    ################################################################################################
