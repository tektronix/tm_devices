"""MSO2KB device driver module."""

import warnings

from typing import Any, List, Optional, Tuple

import pyvisa as visa

from tm_devices.commands import MSO2KBMixin
from tm_devices.drivers.pi.scopes.tekscope_2k.mso2k import MSO2K
from tm_devices.helpers import DeviceConfigEntry

# noinspection PyPep8Naming
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


class MSO2KB(MSO2KBMixin, MSO2K):  # pyright: ignore[reportIncompatibleMethodOverride]
    """MSO2KB device driver."""

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
        """Create a MSO2KB device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
            default_visa_timeout: The default VISA timeout value in milliseconds.
        """
        # NOTE: This method must be defined for the documentation to properly generate
        super().__init__(config_entry, verbose, visa_resource, default_visa_timeout)

    ################################################################################################
    # Properties
    ################################################################################################

    ################################################################################################
    # Public Methods
    ################################################################################################
    @property
    def all_channel_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the channel names.

        Notes:
            Includes the dedicated digital channel ``DCH1`` if ``MSO`` license is present.
        """
        return super().all_channel_names_list

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        return 4

    def curve_query(  # pylint: disable=too-many-locals
        self,
        channel_num: int,
        wfm_type: str = "TimeDomain",
        output_csv_file: Optional[str] = None,
    ) -> List[Any]:
        """Perform a curve query on a specific channel.

        Args:
            channel_num: The channel number to perform the curve query on.
            wfm_type: The type of waveform to query.
            output_csv_file: An optional file path to a csv file to save the curve query data in.

        Returns:
            List of waveform data

        Raises:
            AssertionError: Indicates that an invalid waveform type was passed in to the method.
        """
        available_sources = self.query(":DATA:SOURCE?")
        source_list = available_sources.strip().split(",")
        found = False

        for source in source_list:
            # Analog
            if wfm_type == "TimeDomain":
                if source == f"CH{channel_num}":
                    self.set_and_check("DATA:SOURCE", f"CH{channel_num}")
                    found = True
                elif source == f"D{channel_num}":  # Digital
                    self.set_and_check("DATA:SOURCE", f"D{channel_num}")
                    found = True
            else:
                msg = f"{wfm_type} is an invalid waveform type!"
                raise AssertionError(msg)
            if found:
                break  # break out of loop
        if not found:
            warnings.warn(f"source not available for curve query: CH{channel_num}", stacklevel=2)
            return []

        self.set_and_check(":DATA:ENC", "ASCI")
        wfm_str = self.query(":CURVE?")
        frames = wfm_str.splitlines()[0].split(",")
        wfm_data = [float(frame) for frame in frames]

        ymult = float(self.query("WFMO:YMU?"))
        yoff = float(self.query("WFMO:YOF?"))
        yzero = float(self.query("WFMO:YZE?"))

        data = [((i - yoff) * ymult) + yzero for i in wfm_data]
        wfm_data = [round(i, 3) for i in data]

        if output_csv_file:
            with open(output_csv_file, "w", encoding="UTF-8") as csv_file:
                for frame in wfm_data:
                    csv_file.write(str(frame))
                    csv_file.write(",")

        return wfm_data  # return list of frames

    def turn_channel_on(
        self,
        channel_str: str,
    ) -> None:
        """Enables the display of a specific channel.

        Args:
            channel_str: The channel number to turn on.
        """
        self.write("SELECT:" f"{channel_str}" " ON")

    def turn_channel_off(
        self,
        channel_str: str,
    ) -> None:
        """Disables the display of a specific channel.

        Args:
            channel_str: The channel number to turn off.
        """
        self.write("SELECT:" f"{channel_str}" " OFF")

    ################################################################################################
    # Private Methods
    ################################################################################################
