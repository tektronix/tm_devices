"""MSO2 device driver module."""

from types import MappingProxyType

import pyvisa as visa

from tm_devices.commands import MSO2Mixin
from tm_devices.drivers.scopes.tekscope.tekscope import (
    TekProbeData,
    TekScope,
    TekScopeChannel,
)
from tm_devices.helpers import DeviceConfigEntry
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


class MSO2(MSO2Mixin, TekScope):  # pyright: ignore[reportIncompatibleVariableOverride]
    """MSO2 device driver."""

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
        """Create a MSO2 device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed. If True,
                communication printouts will be logged with a level of INFO. If False,
                communication printouts will be logged with a level of DEBUG.
            visa_resource: The VISA resource object.
            default_visa_timeout: The default VISA timeout value in milliseconds.
        """
        super().__init__(config_entry, verbose, visa_resource, default_visa_timeout)
        # MSO2 takes 15-20 seconds for shutdown, needs more time before opening visa connection.
        self._reboot_quiet_period = 20
        # the DCH1 channel has 16 bit lanes
        self._num_dig_bits_in_ch = 16

    ################################################################################################
    # Public Methods
    ################################################################################################
    @property
    def all_channel_names_list(self) -> tuple[str, ...]:
        """Return a tuple containing all the channel names.

        Notes:
            Includes the dedicated digital channel ``DCH1`` if ``MSO`` license is present.
        """
        retval = super().all_channel_names_list
        if self.has_license("MSO"):
            # replace last index CH3 or CH5 with DCH1
            retval = (*retval[:-1], "DCH1")
        return retval

    @cached_property
    def channel(self) -> MappingProxyType[str, TekScopeChannel]:
        """Mapping of channel names to any detectable properties, attributes, and settings.

        MSO2 has no ``PROBETYPE``/``PROBE:ID:*`` PI commands at all (unlike most other
        TekScope families), so this builds the probe data directly from the channel name
        instead of querying the device and relying on ``AbstractTekScope.channel``'s
        VISA-timeout fallback for that.
        """
        return MappingProxyType(
            {
                channel: TekScopeChannel(
                    name=channel,
                    probe=(
                        TekProbeData(probetype="DIGITAL", probe_id_type="N/A")
                        if channel.startswith("DCH")
                        else TekProbeData()
                    ),
                )
                for channel in self.all_channel_names_list
            }
        )

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        retval = super().total_channels
        if self.has_license("MSO"):
            retval += 1
        return retval
