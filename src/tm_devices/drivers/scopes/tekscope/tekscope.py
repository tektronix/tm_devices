# pylint: disable=too-many-lines
"""Base TekScope scope device driver module."""

from __future__ import annotations

import logging
import math
import os
import time
import warnings

from abc import ABC
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Any, cast, Dict, List, Literal, Optional, Tuple, Type, TYPE_CHECKING, Union

import pyvisa as visa

from tm_devices.driver_mixins.abstract_device_functionality import (
    BaseAFGSourceChannel,
    BusMixin,
    ChannelControlMixin,
    HistogramMixin,
    LicensedMixin,
    MathMixin,
    MeasurementsMixin,
    PlotMixin,
    PowerMixin,
    ReferenceMixin,
    ScreenCaptureMixin,
    SearchMixin,
    USBDrivesMixin,
)
from tm_devices.driver_mixins.abstract_device_functionality.signal_generator_mixin import (
    ExtendedSourceDeviceConstants,
    ParameterBounds,
    SignalGeneratorMixin,
    SourceDeviceConstants,
)
from tm_devices.driver_mixins.device_control import PIControl
from tm_devices.driver_mixins.shared_implementations._tektronix_pi_scope_mixin import (
    _TektronixPIScopeMixin,  # pyright: ignore[reportPrivateUsage]
)
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.scopes.scope import Scope
from tm_devices.helpers import DeviceConfigEntry, LoadImpedanceAFG, raise_error
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813
from tm_devices.helpers.enums import (
    SignalGeneratorFunctionsIAFG,
    SignalGeneratorOutputPathsBase,
)

if TYPE_CHECKING:
    from tm_devices.commands import (
        LPD6Commands,
        MSO2Commands,
        MSO4Commands,
        MSO5BCommands,
        MSO5Commands,
        MSO5LPCommands,
        MSO6BCommands,
        MSO6Commands,
    )

_logger: logging.Logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class TekScopeSourceDeviceConstants(SourceDeviceConstants):
    """Class to hold source device constants."""

    functions: Type[SignalGeneratorFunctionsIAFG] = SignalGeneratorFunctionsIAFG


@dataclass(frozen=True)
class TekProbeData:
    """Immutable information for ``TekScope.channel["<ch_name>"].probe`` data."""

    probetype: Literal["ANALOG", "DIGITAL"] = "ANALOG"
    probe_id_sernumber: str = "N/A"
    probe_id_type: str = "1X"


# NOTE: This is no longer considered a family_base_class due to the
# differences between the physical scope hardware devices and the TekScopePC device.
class AbstractTekScope(  # pylint: disable=too-many-public-methods
    _TektronixPIScopeMixin,
    PIControl,
    Scope,
    BusMixin,
    HistogramMixin,
    LicensedMixin,
    MathMixin,
    MeasurementsMixin,
    ReferenceMixin,
    SearchMixin,
    PlotMixin,
    PowerMixin,
    USBDrivesMixin,
    ChannelControlMixin,
    ScreenCaptureMixin,
    ABC,
):
    """Base TekScope scope device driver.

    This class contains shared functionality between physical TekScope devices and TekScopePC.
    """

    # re-edit so it reflects the actual Internal AFG
    _DEVICE_CONSTANTS = TekScopeSourceDeviceConstants(
        memory_page_size=2,
        memory_max_record_length=16200000,
        memory_min_record_length=1,
    )

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
        """Create a TekScope device.

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

        self._num_dig_bits_in_ch: int = 8

    ################################################################################################
    # Properties
    ################################################################################################

    @cached_property
    def channel(self) -> "MappingProxyType[str, TekScopeChannel]":
        """Mapping of channel names to any detectable properties, attributes, and settings."""
        # TODO: overwrite in MSO2 driver, would remove need for try-except
        #   https://github.com/tektronix/tm_devices/issues/324
        channel_map: Dict[str, TekScopeChannel] = {}

        with self.temporary_verbose(False) and self.temporary_visa_timeout(
            500
            if not bool(os.environ.get("TM_DEVICES_UNIT_TESTS_RUNNING"))
            else self.default_visa_timeout
        ):
            # Set scope PI to be verbose
            old_pi_verbosity = self.query(":VERBose?")
            self.set_and_check(":VERBose", 1)

            # CH1, CH2, ..., CH<n>[, DCH<n>]
            for channel in self.all_channel_names_list:
                try:
                    # Channels that support the PROBETYPE query are dynamically assigned
                    probetype = cast(
                        "Literal['ANALOG', 'DIGITAL']", self.query(f"{channel}:PROBETYPE?")
                    )
                    probe_id_sernumber = self.query(
                        f"{channel}:PROBE:ID:SERNUMBER?", remove_quotes=True
                    )
                    probe_id_type = self.query(f"{channel}:PROBE:ID:TYPE?", remove_quotes=True)
                    probe = TekProbeData(
                        probetype=probetype,
                        probe_id_sernumber=probe_id_sernumber,
                        probe_id_type=probe_id_type,
                    )
                except visa.errors.Error:
                    # handle digital exclusive channels
                    if channel.startswith("DCH"):
                        probetype: Literal["ANALOG", "DIGITAL"] = "DIGITAL"
                        probe_id_type = "N/A"
                    else:
                        probetype: Literal["ANALOG", "DIGITAL"] = "ANALOG"
                        probe_id_type = "1X"
                    probe = TekProbeData(probetype=probetype, probe_id_type=probe_id_type)
                # verify probetype string is reliably one of ANALOG or DIGITAL
                if probe.probetype not in ("ANALOG", "DIGITAL"):  # pragma: no cover
                    msg = f"{channel}:PROBETYPE? was not ANALOG or DIGITAL, got {probe.probetype}"
                    raise AssertionError(msg)
                # create the probe dataclass
                channel_map[channel] = TekScopeChannel(name=channel, probe=probe)

            # Set scope PI verbosity back to previous value
            self.set_and_check(":VERBose", old_pi_verbosity)
        return MappingProxyType(channel_map)

    @cached_property
    def commands(
        self,
    ) -> Union[
        LPD6Commands,
        MSO2Commands,
        MSO4Commands,
        MSO5Commands,
        MSO5BCommands,
        MSO5LPCommands,
        MSO6Commands,
        MSO6BCommands,
    ]:
        """Return the device commands."""
        return super().commands  # pragma: no cover

    @cached_property
    def hostname(self) -> str:
        """Return the hostname of the device or an empty string if unable to fetch that."""
        return self.query(":ETHERNET:NAME?", verbose=False, remove_quotes=True)

    @cached_property
    def license_list(self) -> Tuple[str, ...]:
        """Return the list of license AppIDs installed on the scope."""
        license_list = self.query(
            ":LICENSE:APPID?", verbose=False, remove_quotes=True, allow_empty=True
        ).split(",")
        return tuple(filter(None, license_list))

    @property
    def num_dig_bits_in_ch(self) -> int:
        """Return the number of digital bits expected in a digital channel."""
        # TODO: should be part of self.channel
        #  https://github.com/tektronix/tm_devices/issues/329
        return self._num_dig_bits_in_ch

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        try:
            return int(self.model[4])
        except ValueError:
            return 0

    @cached_property
    def usb_drives(self) -> Tuple[str, ...]:
        """Return a list of all connected USB drives."""
        # Find all USB drives connected to the device
        usb_drives: List[str] = []
        # These drive letter hosts are hard coded to the front and back usb ports.
        available_hosts = ["E:", "F:", "G:", "H:", "I:", "J:", "K:"]
        with self.temporary_verbose(False):
            original_dir = self.query(":FILESystem:CWD?")
            for working_dir in available_hosts:
                self.write(f':FILESystem:CWD "{working_dir}"')
                if self.query(":FILESystem:CWD?", remove_quotes=True).strip() == working_dir:
                    usb_drives.append(working_dir)
            # Clear any errors from checking for USB drives
            self.ieee_cmds.cls()
            # Set the directory back to where it was originally
            self.write(f":FILESystem:CWD {original_dir}")
        return tuple(usb_drives)

    @property
    def valid_image_extensions(self) -> Tuple[str, ...]:
        """Return a tuple of valid image extensions for this device.

        The extensions will be in the format '.ext', where 'ext' is the lowercase extension,
        e.g. (".png", ".jpg").

        Returns:
            Tuple[str, ...]: A tuple of valid, lowercase image extensions for this device.
        """
        return ".png", ".bmp", ".jpg", ".jpeg"

    ################################################################################################
    # Public Methods
    ################################################################################################
    def add_new_measurement(
        self, meas_name: str, meas_type: str, meas_source: Optional[str] = None
    ) -> None:
        """Add a new measurement with the given name, type, and source.

        Args:
            meas_name: The name of the new measurement.
            meas_type: The type of the new measurement.
            meas_source: The source of the new measurement.
                If None, the currently selected waveform (or first available valid source)
                will be used as the source.
        """
        meas_num = int("".join(char for char in meas_name if char.isdigit()))
        self.add_measurement(meas_num)

        self.set_and_check(f"MEASURE:{meas_name}:TYPE", meas_type)
        if meas_source:
            self.set_and_check(f"MEASURE:{meas_name}:SOURCE", meas_source)

    def add_new_plot(self, plot_name: str, plot_type: str) -> None:
        """Add a new plot with the given name, and type.

        Args:
            plot_name: The name of the new plot.
            plot_type: The type of the new plot.
        """
        plot_num = int("".join(char for char in plot_name if char.isdigit()))
        self.add_plot(plot_num)
        self.set_and_check(f":PLOT:{plot_name}:TYPE", plot_type)

    def add_new_bus(self, bus_name: str, bus_type: str) -> None:
        """Add a new bus with the given name, and type.

        Args:
            bus_name: The name of the new bus.
            bus_type: The type of the new bus.
        """
        bus_num = int("".join(char for char in bus_name if char.isdigit()))
        self.add_bus(bus_num)
        self.set_and_check(f":BUS:{bus_name}:TYPE", bus_type)

    def add_new_math(self, math_name: str, math_expression: str) -> None:
        """Add a new math with the given expression.

        Args:
            math_name: The name of the math.
            math_expression: The math expression.
        """
        math_num = int("".join(char for char in math_name if char.isdigit()))
        self.add_math(math_num)
        self.set_and_check(f":MATH:{math_name}:DEFINE", f'"{math_expression}"')

    # pylint: disable=too-many-branches
    def curve_query(  # noqa: PLR0912,C901
        self,
        channel_num: int,
        wfm_type: str = "TimeDomain",
        output_csv_file: Optional[Union[str, os.PathLike[str]]] = None,
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
        available_sources = self.query(":DATA:SOURCE:AVAIL?")
        source_list = available_sources.strip().split(",")
        found = False

        for source in source_list:
            # Analog
            if wfm_type == "TimeDomain":
                if source == f"CH{channel_num}":
                    self.set_and_check("DATA:SOURCE", f"CH{channel_num}")
                    found = True
                elif source == f"CH{channel_num}_D0":  # Digital
                    self.set_and_check("DATA:SOURCE", f"CH{channel_num}_D0")
                    found = True
            elif wfm_type == "IQ":
                # SV Baseband IQ
                if source == f"CH{channel_num}_SV_BASEBAND_IQ":
                    self.set_and_check("DATA:SOURCE", f"CH{channel_num}_SV_BASEBAND_IQ")
                    found = True
            elif wfm_type == "Spectrum":
                # SV Normal
                if source == f"CH{channel_num}_SV_NORMAL":
                    self.set_and_check("DATA:SOURCE", f"CH{channel_num}_SV_NORMAL")
                    found = True
            elif wfm_type == "FreqVsTime":
                # SV Freq Vs Time
                if source == f"CH{channel_num}_FREQ_VS_TIME":
                    self.set_and_check("DATA:SOURCE", f"CH{channel_num}_FREQ_VS_TIME")
                    found = True
            elif wfm_type == "MagVsTime":
                # SV Mag Vs Time
                if source == f"CH{channel_num}_MAG_VS_TIME":
                    self.set_and_check("DATA:SOURCE", f"CH{channel_num}_MAG_VS_TIME")
                    found = True
            else:
                msg = f"{wfm_type} is an invalid waveform type!"
                raise AssertionError(msg)
            if found:
                break  # break out of loop
        if not found:
            warnings.warn(f"source not available for curve query: CH{channel_num}", stacklevel=2)
            _logger.warning("source not available for curve query: CH%d", channel_num)
            return []

        self.set_and_check(":DATA:ENC", "ASCII")
        wfm_str = self.query(":CURVE?")
        frames = wfm_str.splitlines()[0].split(";")
        wfm_data: List[Union[List[int], List[float]]] = []
        if wfm_type == "TimeDomain":
            for frame in frames:
                wfm_data.append([int(b) for b in frame.split(",")])  # noqa: PERF401
        else:
            for frame in frames:
                wfm_data.append([float(b) for b in frame.split(",")])  # noqa: PERF401

        if output_csv_file:
            with Path(output_csv_file).open("w", encoding="UTF-8") as csv_file:
                for frame in frames:
                    csv_file.write(frame)
                    csv_file.write(",")

        if len(wfm_data) == 1:
            return wfm_data[0]  # return single frame

        return wfm_data  # return list of frames

    def recall_reference(self, reference_path: str, ref_number: Union[int, str]) -> None:
        """Recall a reference waveform file.

        Args:
            reference_path: The path to the reference waveform file.
            ref_number: The REF number to recall the waveform to.
        """
        if not reference_path.startswith('"'):
            reference_path = '"' + reference_path
        if not reference_path.endswith('"'):
            reference_path += '"'
        self.write(f"RECALL:WAVEFORM {reference_path}, REF{ref_number}", opc=True)

    def recall_session(self, session_path: str) -> None:
        """Recall a session file.

        Args:
            session_path: The path to the session file.
        """
        if not session_path.startswith('"'):
            session_path = '"' + session_path
        if not session_path.endswith('"'):
            session_path += '"'
        self.write(f":RECALL:SESSION {session_path}", opc=True)

    def save_waveform_to_reference(self, waveform: str, reference: str) -> None:
        """Save the specified waveform to a reference.

        This uses a workaround by saving the waveform to a file and then recalling that file
        to a reference because the PI command ``:SAVE:WAVEFORM CH1,REF1`` is not available
        currently.  If it gets added later this function should be updated.
        Recalling a file to a ref turns on ref, so :REF:ADDNEW is not needed.

        Args:
            waveform: The name of the waveform to save, e.g. CH1, MATH1, etc.
            reference: The name of the target reference, e.g. REF1.
        """
        self.write(f':SAVE:WAVEFORM {waveform},"{reference}.wfm"', opc=True)
        self.write(f':RECALL:WAVEFORM "{reference}.wfm",{reference}', opc=True)

    def single_sequence(self) -> None:
        """Perform a single sequence."""
        self.commands.acquire.stopafter.write("SEQUENCE", verify=True)
        self.commands.acquire.state.write(1)
        self._ieee_cmds.opc()

    def turn_channel_off(self, channel_str: str) -> None:
        """Turn off the specified channel.

        Args:
            channel_str: The name of the channel to turn off.
        """
        self._set_channel_display_state(channel_str, False)

    def turn_channel_on(self, channel_str: str) -> None:
        """Turn on the specified channel.

        Args:
            channel_str: The name of the channel to turn on.
        """
        self._set_channel_display_state(channel_str, True)

    ################################################################################################
    # Public Methods (PI Library)
    ################################################################################################
    def add_bus(self, bus_num: int) -> None:
        """Add a new bus.

        Args:
            bus_num: The number of the bus to add.
        """
        self._add_or_delete_dynamic_item("BUS", bus_num)

    def add_histogram(self, hist_num: int) -> None:
        """Add a new histogram.

        Args:
            hist_num: The number of the histogram to add.
        """
        self._add_or_delete_dynamic_item("HISTOGRAM", hist_num)

    def add_math(self, math_num: int) -> None:
        """Add a new math.

        Args:
            math_num: The number of the math to add.
        """
        self._add_or_delete_dynamic_item("MATH", math_num)

    def add_measurement(self, measurement_num: int) -> None:
        """Add a new measurement.

        Args:
            measurement_num: The number of the measurement to add.
        """
        self._add_or_delete_dynamic_item("MEASUREMENT", measurement_num)

    def add_measurement_table(self, meas_table_num: int) -> None:
        """Add a new measurement table.

        Args:
            meas_table_num: The number of the measurement table to add.
        """
        self._add_or_delete_dynamic_item("MEASTABLE", meas_table_num)

    def add_plot(self, plot_num: int) -> None:
        """Add a new plot.

        Args:
            plot_num: The number of the plot to add.
        """
        self._add_or_delete_dynamic_item("PLOT", plot_num)

    def add_power(self, power_meas_num: int) -> None:
        """Add a new power measurement.

        Args:
            power_meas_num: The number of the power measurement to add.
        """
        self._add_or_delete_dynamic_item("POWER", power_meas_num)

    def add_ref(self, ref_num: int) -> None:
        """Add a new ref.

        Args:
            ref_num: The number of the ref to add.
        """
        self._add_or_delete_dynamic_item("REF", ref_num)

    def add_search(self, search_num: int) -> None:
        """Add a new search.

        Args:
            search_num: The number of the search to add.
        """
        self._add_or_delete_dynamic_item("SEARCH", search_num)

    def delete_bus(self, bus_num: int) -> None:
        """Delete a bus.

        Args:
            bus_num: The number of the bus to delete.
        """
        self._add_or_delete_dynamic_item("BUS", bus_num, delete_item=True)

    def delete_histogram(self, hist_num: int) -> None:
        """Delete a histogram.

        Args:
            hist_num: The number of the histogram to delete.
        """
        self._add_or_delete_dynamic_item("HISTOGRAM", hist_num, delete_item=True)

    def delete_math(self, math_num: int) -> None:
        """Delete a math.

        Args:
            math_num: The number of the math to delete.
        """
        self._add_or_delete_dynamic_item("MATH", math_num, delete_item=True)

    def delete_measurement(self, measurement_num: int) -> None:
        """Delete a measurement.

        Args:
            measurement_num: The number of the measurement to delete.
        """
        self._add_or_delete_dynamic_item("MEASUREMENT", measurement_num, delete_item=True)

    def delete_measurement_table(self, measurement_table_num: int) -> None:
        """Delete a measurement table.

        Args:
            measurement_table_num: The number of the measurement table to delete.
        """
        self._add_or_delete_dynamic_item("MEASTABLE", measurement_table_num, delete_item=True)

    def delete_plot(self, plot_num: int) -> None:
        """Delete a plot.

        Args:
            plot_num: The number of the plot to delete.
        """
        self._add_or_delete_dynamic_item("PLOT", plot_num, delete_item=True)

    def delete_power(self, power_num: int) -> None:
        """Delete a power.

        Args:
            power_num: The number of the power to delete.
        """
        self._add_or_delete_dynamic_item("POWER", power_num, delete_item=True)

    def delete_ref(self, ref_num: int) -> None:
        """Delete a ref.

        Args:
            ref_num: The number of the ref to delete.
        """
        self._add_or_delete_dynamic_item("REF", ref_num, delete_item=True)

    def delete_search(self, search_num: int) -> None:
        """Delete a search.

        Args:
            search_num: The number of the search to delete.
        """
        self._add_or_delete_dynamic_item("SEARCH", search_num, delete_item=True)

    ################################################################################################
    # Private Methods/Properties
    ################################################################################################
    def _add_or_delete_dynamic_item(
        self,
        item_type: str,
        item_num: int,
        *,
        delete_item: bool = False,
    ) -> None:
        """Add a new dynamic item.

        Args:
            item_type: The type of item to create, e.g. MATH, REF, SEARCH, MEAS.
            item_num: The number of the item to add.
            delete_item: Boolean indicating the item should be deleted instead of added.
        """
        # This dict maps the input strings to the item name that will be used to create the item
        valid_items = {
            "BUS": "B",
            "HISTOGRAM": "HIST",
            "MATH": "MATH",
            "MEASTABLE": "TABLE",
            "MEASUREMENT": "MEAS",
            "PLOT": "PLOT",
            "POWER": "POWER",
            "REF": "REF",
            "SEARCH": "SEARCH",
        }
        if item_type not in valid_items:
            msg = f"{item_type} is not a valid item, valid items: {valid_items.items()}"
            raise AssertionError(msg)

        item_name = f"{valid_items[item_type]}{item_num}"
        if delete_item:
            self.write(f':{item_type}:DELete "{item_name}"')
        else:
            self.write(f':{item_type}:ADDNew "{item_name}"')

        # Get the list of items
        item_list = self.query(f":{item_type}:LIST?", remove_quotes=True).strip().split(",")

        if delete_item:
            if item_name in item_list:
                raise_error(
                    self.name_and_alias,
                    f"Failed to delete {item_name}\n"
                    f':{item_type}:LIST? returned "{",".join(item_list)}"',
                )
        elif item_name not in item_list:
            raise_error(
                self.name_and_alias,
                f'Failed to add {item_name}\n:{item_type}:LIST? returned "{",".join(item_list)}"',
            )

    def _ensure_directory_exists_on_device(self, filepath: Path) -> None:
        """Ensure that the directory of the filepath exists on the device, creating it if necessary.

        Args:
            filepath: The filepath to check.
        """
        with self.temporary_verbose(False):
            original_dir = self.query(":FILESystem:CWD?")
            # Remove the current working directory from the front of the input filepath
            try:
                relative_filepath = Path(filepath.relative_to(original_dir.replace('"', "")))
            except ValueError:
                # The input filepath is already a relative path
                relative_filepath = filepath
            changed_dir = False
            try:
                for path_part in relative_filepath.parents:  # pragma: no cover
                    if path_part.is_file() or path_part.suffix or not path_part.name:
                        break
                    path_part_string = path_part.as_posix()
                    if path_part_string not in {
                        x.split(";")[0]
                        for x in self.query(
                            ":FILESystem:LDIR?", remove_quotes=True, allow_empty=True
                        ).split(",")
                    }:
                        self.write(f':FILESystem:MKDir "{path_part_string}"')
                    changed_dir = True
                    self.write(f':FILESystem:CWD "./{path_part_string}"')
            finally:
                if changed_dir:
                    self.write(f":FILESystem:CWD {original_dir}")

    def _save_screenshot(
        self,
        filename: Path,
        *,
        colors: Optional[str],
        view_type: Optional[str],  # noqa: ARG002
        local_folder: Path,
        device_folder: Path,
        keep_device_file: bool = False,
    ) -> None:
        """Capture a screenshot from the device and save it locally.

        Args:
            filename: The name of the file to save the screenshot as.
            colors: The color scheme to use for the screenshot.
            view_type: The type of view to capture. (Not used in any TekScope drivers)
            local_folder: The local folder to save the screenshot in. Defaults to "./".
            device_folder: The folder on the device to save the screenshot in. Defaults to "./".
            keep_device_file: Whether to keep the file on the device after downloading it.
                Defaults to False.
        """
        if colors:
            self.set_and_check("SAVE:IMAGE:COMPOSITION", colors)
        else:
            self.set_and_check("SAVE:IMAGE:COMPOSITION", "NORMAL")
        device_filepath = device_folder / filename
        device_filepath_string = (
            f'"{"./" if not device_filepath.drive else ""}{device_filepath.as_posix()}"'
        )
        self._ensure_directory_exists_on_device(device_filepath)
        self.write(f"SAVE:IMAGE {device_filepath_string}", opc=True)
        self.write(f"FILESYSTEM:READFILE {device_filepath_string}")
        data = self.read_raw()
        (local_folder / filename).write_bytes(data)
        if not keep_device_file:
            self.write(f"FILESYSTEM:DELETE {device_filepath_string}", opc=True)
            time.sleep(0.2)  # wait to ensure the file is deleted

    def _reboot(self) -> None:
        """Reboot the device."""
        self.write(":SCOPEAPP REBOOT")

    @staticmethod
    def _get_driver_specific_multipliers() -> float:
        """Return a value to multiply the original Tekscope IAFG frequency by."""
        return 1.0

    def _set_channel_display_state(
        self, channel_str: str, state: bool, turn_on_group: bool = True
    ) -> None:
        """Turn channel on or off.

        In the case of digital channels connected to CH1, by default CH1_D0 - D7 are turned on.
        if turn_on_group is False, then only the selected channel is turned on, say CH1_D5.

        Args:
            channel_str: The name of the channel to turn ON/OFF, e.g. 'CH1' or 'CH1_D0'
            state: The state to turn the channel to, True for ON and False for OFF.
            turn_on_group: A boolean indicating if the entire digital group should be turned on.
        """
        if (
            self.channel[
                (channel_str_base := channel_str.split("_", maxsplit=1)[0])
            ].probe.probetype
            == "DIGITAL"
            and turn_on_group
        ):
            channel_str = channel_str_base + "_DALL"
        self.set_and_check(f":DISPLAY:WAVEVIEW:{channel_str}:STATE", int(state))


@family_base_class
class TekScope(
    SignalGeneratorMixin[SignalGeneratorFunctionsIAFG, TekScopeSourceDeviceConstants],
    AbstractTekScope,
    ABC,
):
    """A physical TekScope device.

    Physical TekScope devices all come with an Internal AFG.
    """

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def source_device_constants(self) -> TekScopeSourceDeviceConstants:
        """The constants defining what functions and memory sizes are allowed for the device."""
        return self._DEVICE_CONSTANTS

    @cached_property
    def internal_afg(self) -> "InternalAFGChannel":
        """The scope's internal AFG."""
        return InternalAFGChannel(self)

    ################################################################################################
    # Public Methods
    ################################################################################################
    def generate_function(  # noqa: PLR0913
        self,
        frequency: float,
        function: SignalGeneratorFunctionsIAFG,
        amplitude: float,
        offset: float,
        channel: str = "all",
        output_signal_path: Optional[SignalGeneratorOutputPathsBase] = None,
        termination: Literal["FIFTY", "HIGHZ"] = "FIFTY",
        duty_cycle: float = 50.0,
        polarity: Literal["NORMAL", "INVERTED"] = "NORMAL",
        symmetry: float = 50.0,
    ) -> None:
        """Generate a predefined waveform given the following parameters.

        Args:
            frequency: The frequency of the waveform to generate.
            function: The function to generate.
            amplitude: The amplitude of the signal to generate.
            offset: The offset of the signal to generate.
            channel: Unused in this class.
            output_signal_path: Unused in this class.
            termination: The impedance to set the channel to.
            duty_cycle: The duty cycle to set the signal to.
            polarity: Unused in this class.
            symmetry: The symmetry to set the signal to, only applicable to certain functions.
        """
        del polarity, channel, output_signal_path  # these aren't used
        self._validate_generated_function(function)
        # Turn off the Internal AFG
        self.internal_afg.set_state(0)
        self.internal_afg.set_function_properties(
            frequency=frequency,
            function=function,
            amplitude=amplitude,
            offset=offset,
            burst_count=0,
            termination=termination,
            duty_cycle=duty_cycle,
            symmetry=symmetry,
        )
        # Turn on the Internal AFG
        self.internal_afg.set_state(1)
        # Don't check for errors as any measurement with low amplitude will generate an error

    def setup_burst(  # noqa: PLR0913
        self,
        frequency: float,
        function: SignalGeneratorFunctionsIAFG,
        amplitude: float,
        offset: float,
        burst_count: int,
        channel: str = "all",
        output_signal_path: Optional[SignalGeneratorOutputPathsBase] = None,
        termination: Literal["FIFTY", "HIGHZ"] = "FIFTY",
        duty_cycle: float = 50.0,
        polarity: Literal["NORMAL", "INVERTED"] = "NORMAL",
        symmetry: float = 50.0,
    ) -> None:
        """Set up the Internal AFG for sending a burst of waveforms given the following parameters.

        Args:
            frequency: The frequency of the waveform to generate.
            function: The function to generate.
            amplitude: The amplitude of the signal to generate.
            offset: The offset of the signal to generate.
            burst_count: The number of wavelengths to be generated.
            channel: Unused in this class.
            output_signal_path: Unused in this class.
            termination: The impedance to set the channel to.
            duty_cycle: The duty cycle to set the signal to.
            polarity: Unused in this class.
            symmetry: The symmetry to set the signal to, only applicable to certain functions.
        """
        del polarity, channel, output_signal_path  # these aren't used
        self._validate_generated_function(function)
        self.internal_afg.set_function_properties(
            frequency=frequency,
            function=function,
            amplitude=amplitude,
            offset=offset,
            burst_count=burst_count,
            termination=termination,
            duty_cycle=duty_cycle,
            symmetry=symmetry,
        )

    def generate_burst(self) -> None:
        """Generate a burst of waveforms by forcing trigger."""
        self.internal_afg.trigger_burst()
        # Don't check for errors as any measurement with low amplitude will generate an error

    # pylint: disable=too-many-locals
    def get_waveform_constraints(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        function: Optional[SignalGeneratorFunctionsIAFG] = None,
        waveform_length: Optional[int] = None,
        frequency: Optional[float] = None,
        output_signal_path: Optional[SignalGeneratorOutputPathsBase] = None,
        load_impedance: LoadImpedanceAFG = LoadImpedanceAFG.HIGHZ,
    ) -> ExtendedSourceDeviceConstants:
        """Get the constraints that restrict the waveform to certain parameter ranges.

        Args:
            function: The function that needs to be generated.
            waveform_length: Unused in this class.
            frequency: The frequency of the waveform that needs to be generated.
            output_signal_path: Unused in this class.
            load_impedance: The suggested impedance on the source.

        Returns:
            A Named Tuple containing a set of parameters and their restricted bounds.
        """
        del output_signal_path, waveform_length

        if not function:
            msg = "IAFGs must have a function defined."
            raise ValueError(msg)

        base_frequency_low = 100.0e-3
        base_frequency_high = 50.0e6 * self._get_driver_specific_multipliers()

        load_impedance_multiplier = 1.0 if load_impedance == LoadImpedanceAFG.HIGHZ else 0.5

        base_amplitude_low = 20.0e-3
        base_amplitude_high = 5.0

        square_duty_cycle_range = ParameterBounds(lower=10.0, upper=90.0)
        pulse_width_range = None
        # handle logic to constrain limits of duty cycle and pulse width range due to frequency
        if frequency is not None:
            max_duty = 90.0
            min_duty = 10.0
            max_square_pulse_freq = base_frequency_high / 2
            # limit to valid range for calcs, otherwise values are outside valid ranges
            calc_freq = max((base_amplitude_high, min((max_square_pulse_freq, frequency))))
            # above 10MHz (or 20MHz), then SQUARE duty cycle and PULSE width ranges get coerced
            if frequency > (duty_cycle_coercion_start_freq := base_frequency_high / 5):
                # 15 percent change over the difference between max frequency and start of coercion
                coercion_slope = 15.0 / (max_square_pulse_freq - duty_cycle_coercion_start_freq)
                max_duty = 90.0 - (coercion_slope * (calc_freq - duty_cycle_coercion_start_freq))
                min_duty = 10.0 + (coercion_slope * (calc_freq - duty_cycle_coercion_start_freq))
                # one decimal place of accuracy as percentage,
                # and uses floor/ceil on the max/min to stay in valid zone
                square_duty_cycle_range = ParameterBounds(
                    lower=math.ceil(min_duty * 10) / 10, upper=math.floor(max_duty * 10) / 10
                )
            # NOTE: There is an edge case where the IAFG period doesn't exactly equal 1/frequency
            #  this can cause the pulse width max and min to be outside valid range by tiny bit,
            #  workaround is to query actual period time and set frequency=1/<actual_period>
            # limited to 0.1ns resolution regardless of frequency
            # also uses floor/ceil to stay in valid zone
            pulse_width_range = ParameterBounds(
                lower=math.ceil(min_duty / 100 * 1e10 / calc_freq) / 1e10,
                upper=math.floor(max_duty / 100 * 1e10 / calc_freq) / 1e10,
            )
        amplitude_multiplier = 1

        if function in {SignalGeneratorFunctionsIAFG.SIN}:
            frequency_multiplier = 1
        elif function in {
            SignalGeneratorFunctionsIAFG.SQUARE,
            SignalGeneratorFunctionsIAFG.PULSE,
            SignalGeneratorFunctionsIAFG.ARBITRARY,
        }:
            frequency_multiplier = 0.5
        elif function in {SignalGeneratorFunctionsIAFG.SINC}:
            frequency_multiplier = 0.04
            amplitude_multiplier = 0.6
        elif function in {
            SignalGeneratorFunctionsIAFG.RAMP,
            SignalGeneratorFunctionsIAFG.CARDIAC,
        }:
            frequency_multiplier = 0.01
        else:
            frequency_multiplier = 0.1
            amplitude_multiplier = 0.5 if function != SignalGeneratorFunctionsIAFG.LORENTZ else 0.48

        frequency_range = ParameterBounds(
            lower=base_frequency_low, upper=base_frequency_high * frequency_multiplier
        )
        amplitude_range = ParameterBounds(
            lower=base_amplitude_low * load_impedance_multiplier,
            upper=base_amplitude_high * amplitude_multiplier * load_impedance_multiplier,
        )
        offset_range = ParameterBounds(
            lower=-2.5 * load_impedance_multiplier, upper=2.5 * load_impedance_multiplier
        )
        # RAMP symmetry range never changes with frequency
        ramp_symmetry_range = ParameterBounds(lower=0.0, upper=100.0)
        sample_rate_range = ParameterBounds(lower=250.0e6, upper=250.0e6)
        return ExtendedSourceDeviceConstants(
            amplitude_range=amplitude_range,
            frequency_range=frequency_range,
            offset_range=offset_range,
            sample_rate_range=sample_rate_range,
            square_duty_cycle_range=square_duty_cycle_range,
            pulse_width_range=pulse_width_range,
            ramp_symmetry_range=ramp_symmetry_range,
        )


@dataclass
class TekScopeChannel:
    """Scope channel information."""

    name: str
    """Name of the channel."""
    probe: TekProbeData
    """Details about channel setup and any connected probe."""
    termination: Optional[Literal[50, 250_000, 1_000_000]] = None
    """Defines impedance at channel port."""


class InternalAFGChannel(BaseAFGSourceChannel):
    """Internal AFG channel driver."""

    def __init__(self, tekscope: TekScope) -> None:
        """Create an Internal AFG channel.

        Args:
            tekscope: A TekScope.
        """
        super().__init__(pi_control=tekscope, channel_name="AFG")
        self._tekscope = tekscope

    def __getattribute__(self, item: Any) -> Any:
        """Get a class attribute.

        Args:
            item: The attribute to access.
        """
        obj: TekScope = super().__getattribute__("_tekscope")
        if obj.has_license("AFG"):
            return super().__getattribute__(item)
        msg = "No AFG License, the class instance attributes are not accessible."
        raise AttributeError(msg)

    def set_function_properties(  # noqa: PLR0913  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        frequency: float,
        function: SignalGeneratorFunctionsIAFG,
        amplitude: float,
        offset: float,
        burst_count: int = 0,
        termination: Literal["FIFTY", "HIGHZ"] = "FIFTY",
        duty_cycle: float = 50.0,
        polarity: Literal["NORMAL", "INVERTED"] = "NORMAL",
        symmetry: float = 50.0,
    ) -> None:
        """Set the given parameters on the internal AFG.

        Args:
            frequency: The frequency of the waveform to generate.
            function: The waveform shape to generate.
            amplitude: The amplitude of the signal to generate.
            offset: The offset of the signal to generate.
            burst_count: The number of wavelengths to be generated.
            termination: The impedance this device's ``channel`` expects to see at the received end.
            duty_cycle: The duty cycle percentage within [10.0, 90.0].
            polarity: Unused in this class.
            symmetry: The symmetry to set the signal to, only applicable to certain functions.
        """
        del polarity
        if burst_count > 0:
            self.setup_burst_waveform(burst_count)
        # Generate the waveform from the Internal AFG
        # Frequency
        self.set_frequency(frequency)
        # Function
        self.set_function(function)
        # Duty Cycle
        if function == SignalGeneratorFunctionsIAFG.SQUARE:
            self.set_square_duty_cycle(duty_cycle)
        # Symmetry
        if function == SignalGeneratorFunctionsIAFG.RAMP:
            self.set_ramp_symmetry(symmetry)
        # Termination impedance
        self.set_impedance(termination)
        # Amplitude, needs to be after termination so that the amplitude is properly adjusted
        self.set_amplitude(amplitude)
        # Offset, needs to be after termination so that the offset is properly adjusted
        self.set_offset(offset)

    def set_amplitude(self, value: float, absolute_tolerance: float = 0) -> None:
        """Set the amplitude on the internal AFG.

        Args:
            value: The amplitude value to set.
            absolute_tolerance: The acceptable difference between two floating point values.
        """
        self._tekscope.set_if_needed(
            f"{self.name}:AMPLITUDE",
            value,
            tolerance=absolute_tolerance,
        )

    def set_burst_count(self, value: int) -> None:
        """Set the number of wavelengths to be generated when the internal AFG is set to burst.

        Args:
            value: The number of wavelengths to be generated within [1, 1000000].
        """
        self._tekscope.set_if_needed(f"{self.name}:BURST:CCOUNT", f"{value}")

    def set_frequency(self, value: float, absolute_tolerance: float = 0) -> None:
        """Set the frequency on the internal AFG.

        Args:
            value: The frequency value to set.
            absolute_tolerance: The acceptable difference between two floating point values.
        """
        self._tekscope.set_if_needed(
            f"{self.name}:FREQUENCY",
            value,
            tolerance=absolute_tolerance,
        )

    def set_function(self, value: SignalGeneratorFunctionsIAFG) -> None:  # pyright: ignore[reportIncompatibleMethodOverride]
        """Set the function to output on the internal AFG.

        Args:
            value: The name of the function to output.
        """
        self._tekscope.set_if_needed(f"{self.name}:FUNCTION", str(value.value))

    def set_impedance(self, value: Literal["FIFTY", "HIGHZ"]) -> None:
        """Set the output load impedance on the internal AFG.

        Args:
            value: The impedance value to set (Options: "FIFTY", "HIGHZ").
        """
        self._tekscope.set_if_needed(f"{self.name}:OUTPUT:LOAD:IMPEDANCE", value)

    def set_offset(self, value: float, absolute_tolerance: float = 0) -> None:
        """Set the offset on the internal AFG.

        Args:
            value: The offset value to set.
            absolute_tolerance: The acceptable difference between two floating point values.
        """
        self._tekscope.set_if_needed(
            f"{self.name}:OFFSET",
            value,
            tolerance=absolute_tolerance,
        )

    def set_output_mode(self, value: Literal["OFF", "CONTINUOUS", "BURST"]) -> None:
        """Set the output mode on the internal AFG.

        Args:
            value: The output mode to set (Options: "OFF", "CONTINUOUS", "BURST").
        """
        self._tekscope.set_if_needed(f"{self.name}:OUTPUT:MODE", value)

    def set_ramp_symmetry(self, value: float) -> None:
        """Set the symmetry of the ramp waveform on the internal AFG.

        Args:
            value: The symmetry percentage within [0, 100].
        """
        self._tekscope.set_if_needed(f"{self.name}:RAMP:SYMMETRY", value)

    def set_state(self, value: int) -> None:
        """Set the output state to ON/OFF (1/0) on the internal AFG.

        Args:
            value: The output state.
        """
        if value not in [0, 1]:
            error_message = "Output state value must be 1 (ON) or 0 (OFF)."
            raise ValueError(error_message)
        self._tekscope.set_if_needed(f"{self.name}:OUTPUT:STATE", value)

    def set_square_duty_cycle(self, value: float) -> None:
        """Set the duty cycle of the square waveform on the internal AFG.

        Args:
            value: The duty cycle percentage within [10.0, 90.0].
        """
        self._tekscope.set_if_needed(f"{self.name}:SQUARE:DUTY", value)

    def setup_burst_waveform(self, burst_count: int) -> None:
        """Prepare the internal AFG for a burst waveform.

        Args:
            burst_count: The number of wavelengths to be generated.
        """
        # set to external as to not burst every millisecond
        self.set_output_mode("BURST")
        self.set_burst_count(burst_count)

    def trigger_burst(self) -> None:
        """Trigger a burst on the internal AFG."""
        self._tekscope.write(f"{self.name}:BURST:TRIGGER")
