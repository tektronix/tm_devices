"""DMM7510 device driver module."""

from tm_devices.commands import DMM7510Mixin
from tm_devices.drivers.digital_multimeters.dmm75xx.dmm75xx import DMM75xx


class DMM7510(DMM7510Mixin, DMM75xx):
    """DMM7510 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
