"""TekScopePC device driver module."""

import logging
import warnings

from tm_devices.commands import TekScopePCMixin
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.scopes.tekscope.tekscope import AbstractTekScope
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

_logger: logging.Logger = logging.getLogger(__name__)


@family_base_class
class TekScopePC(TekScopePCMixin, AbstractTekScope):  # pyright: ignore[reportIncompatibleVariableOverride]
    """TekScopePC device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        # TekScopePC supports a maximum of 8 channels
        return 8

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _reboot(self) -> None:
        """Reboot the device."""
        msg = (
            f"Rebooting is not supported for the {self.__class__.__name__} driver, "
            f"{self.name_and_alias} will not be rebooted."
        )
        _logger.warning(msg)
        warnings.warn(msg, stacklevel=3)
