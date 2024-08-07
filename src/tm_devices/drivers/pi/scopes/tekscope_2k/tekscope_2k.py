"""Base TekScope2k scope device driver module."""

import warnings

from abc import ABC
from typing import Any, List, Optional

from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.pi.scopes.scope import Scope

# noinspection PyPep8Naming
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


@family_base_class
class TekScope2k(Scope, ABC):
    """Base TekScope2k scope device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        return int(self.model[6])

    ################################################################################################
    # Public Methods
    ################################################################################################

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
        self.set_and_check("SELECT:" f"{channel_str}", 1)

    def turn_channel_off(
        self,
        channel_str: str,
    ) -> None:
        """Disables the display of a specific channel.

        Args:
            channel_str: The channel number to turn off.
        """
        self.set_and_check("SELECT:" f"{channel_str}", 0)

    ################################################################################################
    # Private Methods
    ################################################################################################
