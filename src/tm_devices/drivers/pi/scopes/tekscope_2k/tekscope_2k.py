"""Base TekScope2k scope device driver module."""
from abc import ABC

from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.pi.scopes.scope import Scope


@family_base_class
class TekScope2k(Scope, ABC):
    """Base TekScope2k scope device driver."""

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
    def _reboot(self) -> None:
        """Perform the actual rebooting code."""
        # TODO: implement
        raise NotImplementedError(
            f"``.reboot()`` is not yet implemented for the {self.__class__.__name__} driver"
        )
