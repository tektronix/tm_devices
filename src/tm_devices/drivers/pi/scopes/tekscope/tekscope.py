"""Base TekScope scope device driver module."""
import os
import warnings

from abc import ABC
from dataclasses import dataclass
from functools import cached_property
from types import MappingProxyType
from typing import Any, cast, List, Literal, Optional, Tuple, Type, Union

import pyvisa as visa

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
from tm_devices.driver_mixins.analysis_object_mixins import (
    BusMixin,
    HistogramMixin,
    MathMixin,
    MeasurementsMixin,
    PlotMixin,
    PowerMixin,
    ReferenceMixin,
    SearchMixin,
)
from tm_devices.driver_mixins.licensed_mixin import LicensedMixin
from tm_devices.driver_mixins.signal_generator_mixin import (
    SignalGeneratorMixin,
    SourceDeviceConstants,
)
from tm_devices.driver_mixins.usb_drives_mixin import USBDrivesMixin
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.pi.scopes.scope import Scope
from tm_devices.helpers import DeviceConfigEntry, SignalSourceFunctionsIAFG
from tm_devices.helpers.constants_and_dataclasses import UNIT_TEST_TIMEOUT


@dataclass(frozen=True)
class TekScopeSourceDeviceConstants(SourceDeviceConstants):
    """Class to hold source device constants."""

    functions: Type[SignalSourceFunctionsIAFG] = SignalSourceFunctionsIAFG


@dataclass(frozen=True)
class TekProbeData:
    """Immutable information for ``TekScope.channel["<ch_name>"].probe`` data."""

    probetype: Literal["ANALOG", "DIGITAL"] = "ANALOG"
    probe_id_sernumber: str = "N/A"
    probe_id_type: str = "1X"


@dataclass
class TekScopeChannel:
    """Scope channel information."""

    name: str
    """Name of the channel."""
    probe: TekProbeData
    """Details about channel setup and any connected probe."""
    termination: Optional[Literal[50, 250_000, 1_000_000]] = None
    """Defines impedance at channel port."""


# pylint: disable=too-many-public-methods
@family_base_class
class TekScope(
    Scope,
    BusMixin,
    HistogramMixin,
    LicensedMixin,
    MathMixin,
    MeasurementsMixin,
    ReferenceMixin,
    SearchMixin,
    SignalGeneratorMixin,
    PlotMixin,
    PowerMixin,
    USBDrivesMixin,
    ABC,
):
    """Base TekScope scope device driver."""

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
    ) -> None:
        """Create a TekScope device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
        """
        super().__init__(config_entry, verbose, visa_resource)
        self.write("HEADER OFF", verbose=False)

        # TODO: this should be a property of the probe attribute on the channel object
        self._num_dig_bits_in_ch: int = 8

    ################################################################################################
    # Properties
    ################################################################################################
    @cached_property
    def channel(self) -> "MappingProxyType[str, TekScopeChannel]":
        """Mapping of channel names to any detectable properties, attributes, and settings."""
        # TODO: overwrite in MSO2 driver, would remove need for try-except
        channel_map = {}

        with self.temporary_verbose(False) and self.temporary_visa_timeout(
            500 if not bool(os.environ.get("TM_DEVICES_UNIT_TESTS_RUNNING")) else UNIT_TEST_TIMEOUT
        ):
            # Set scope PI to be verbose
            old_pi_verbosity = self.query(":VERBose?")
            self.set_and_check(":VERBose", 1)

            # CH1, CH2, ..., CH<n>[, DCH<n>]
            for channel in self.all_channel_names_list:
                try:
                    # Channels that support the PROBETYPE query are dynamically assigned
                    probetype = cast(
                        Literal["ANALOG", "DIGITAL"], self.query(f"{channel}:PROBETYPE?")
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
        return MappingProxyType(channel_map)  # pyright: ignore[reportUnknownVariableType]

    @property
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
        return self._commands  # pragma: no cover

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
        return self._num_dig_bits_in_ch

    @property
    def source_device_constants(self) -> TekScopeSourceDeviceConstants:
        """Return the device constants."""
        return self._DEVICE_CONSTANTS

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
            # Only going up to I to compensate for network mounts in CI
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
            with open(output_csv_file, "w", encoding="UTF-8") as csv_file:
                for frame in frames:
                    csv_file.write(frame)
                    csv_file.write(",")

        if len(wfm_data) == 1:
            return wfm_data[0]  # return single frame

        return wfm_data  # return list of frames

    def generate_waveform(  # noqa: PLR0913  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        frequency: float,
        function: SignalSourceFunctionsIAFG,
        amplitude: float,
        offset: float,
        channel: str = "all",
        burst: int = 0,
        termination: Literal["FIFTY", "HIGHZ"] = "FIFTY",
        duty_cycle: float = 50.0,
        polarity: Literal["NORMAL", "INVERTED"] = "NORMAL",
        symmetry: float = 50.0,
    ) -> None:
        """Generate a signal given the following parameters.

        Args:
            frequency: The frequency of the waveform to generate.
            function: The function to generate.
            amplitude: The amplitude of the signal to generate.
            offset: The offset of the signal to generate.
            channel: The channel number to output the signal from, or 'all'.
            burst: The number of waveforms to be generated.
            termination: The impedance to set the channel to.
            duty_cycle: The duty cycle to set the signal to.
            polarity: The polarity to set the signal to.
            symmetry: The symmetry to set the signal to, only applicable to certain functions.
        """
        del polarity, channel  # these aren't used
        self._validate_generated_function(function)
        # Turn off the Internal AFG
        self.set_and_check("AFG:OUTPUT:STATE", 0)
        if burst > 0:
            self.set_and_check("AFG:OUTPUT:MODE", "BURST")
            self.set_and_check("AFG:BURST:CCOUNT", f"{burst}")
        # Generate the waveform from the Internal AFG
        # Frequency
        self.set_and_check("AFG:FREQUENCY", frequency)
        # Offset
        self.set_and_check("AFG:OFFSET", offset)
        # Duty Cycle
        self.set_and_check("AFG:SQUARE:DUTY", duty_cycle)
        # Function
        if function == SignalSourceFunctionsIAFG.RAMP:
            self.set_and_check("AFG:RAMP:SYMMETRY", symmetry)
        self.set_and_check("AFG:FUNCTION", function.value)
        # Termination impedance
        self.set_and_check("AFG:OUTPUT:LOAD:IMPEDANCE", termination)
        # Amplitude, needs to be after termination so that the amplitude is properly adjusted
        self.set_and_check("AFG:AMPLITUDE", amplitude)
        # Turn on the Internal AFG
        self.set_and_check("AFG:OUTPUT:STATE", 1)
        if burst > 0:
            self.write("AFG:BURST:TRIGGER")
        # Don't check for errors as any measurement with low amplitude will generate an error

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
                self.raise_error(
                    f"Failed to delete {item_name}\n"
                    f":{item_type}:LIST? returned \"{','.join(item_list)}\""
                )
        elif item_name not in item_list:
            self.raise_error(
                f"Failed to add {item_name}\n"
                f":{item_type}:LIST? returned \"{','.join(item_list)}\""
            )

    def _reboot(self) -> None:
        """Reboot the device."""
        self.write(":SCOPEAPP REBOOT")

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
