# pyright: reportPrivateUsage=none
"""Test the Scopes."""

import os
import subprocess
import sys

from typing import cast
from unittest import mock

import pytest
import pyvisa as visa

from packaging.version import Version

from tm_devices import DeviceManager
from tm_devices.drivers import MSO2, MSO5, MSO5B, MSO6, MSO70KDX, TekScopeSW
from tm_devices.drivers.pi.scopes.tekscope.tekscope import (
    ExtendedSourceDeviceConstants,
    ParameterBounds,
    SignalGeneratorFunctionsIAFG,
    TekProbeData,
    TekScope,
    TekScopeChannel,
)


class TmDevicesUnitTestOnlyCustomMSO5(MSO5):
    """Custom MSO5 class."""

    def custom_mso5_method(self, value: str) -> str:
        """Run a custom method."""
        return f"This is a custom method for the {self.model} device. {value=}"


def test_tekscope(device_manager: DeviceManager) -> None:  # noqa: PLR0915
    """Test the tekscope implementation.

    Args:
        device_manager: The DeviceManager object.
    """
    device_manager.remove_all_devices()
    # Verify hostname can be determined when only the IP is provided
    scope: MSO5 = cast(
        MSO5, device_manager.add_scope("MSO56-SERIAL1", alias="mso56", connection_type="USB")
    )

    # cheeky super() call for coverage of USB connection type on Device's hostname implementation
    assert super(TekScope, scope).hostname == ""
    # clear cached property so that the scope instance will use the proper implementation
    # noinspection PyPropertyAccess
    del scope.hostname

    # Assert 5 series device was added and aliased properly (USB)
    assert scope.hostname == "MSO56"
    assert id(device_manager.get_scope(number_or_alias="mso56")) == id(scope)
    assert id(device_manager.get_scope(number_or_alias=scope.device_number)) == id(scope)
    assert scope.all_channel_names_list == ("CH1", "CH2", "CH3", "CH4", "CH5", "CH6")
    assert scope.usb_drives == ("E:",)
    assert scope.ip_address == ""
    assert scope.opt_string == "0"
    assert scope.channel["CH1"].probe == TekProbeData(
        probetype="ANALOG",
        probe_id_sernumber="N/A",
        probe_id_type="1X",
    )
    assert scope.channel["CH2"].probe == TekProbeData(
        probetype="DIGITAL",
        probe_id_sernumber="C01234",
        probe_id_type="TLP058",
    )
    assert scope.channel["CH3"].probe == TekProbeData(
        probetype="ANALOG",
        probe_id_sernumber="C56789",
        probe_id_type="TPP0500B",
    )

    # Test that invalid PI commands are caught properly
    scope.write("EXAMPLE_COMMAND")
    scope.expect_esr(32, '113,"Undefined header; Command not found; EXAMPLE_COMMAND"')
    # Test that querying the status register clears it
    with pytest.raises(AssertionError):
        scope.expect_esr(32, '113,"Undefined header; Command not found; EXAMPLE_COMMAND"')
    # Assert there are no errors before proceeding with tests
    scope.expect_esr(0, '0,"No events to report - queue empty"')

    # Test that features can be added
    scope.add_new_bus("B1", "I3C")
    scope.add_new_math("MATH1", "LOG(10)")
    scope.add_histogram(1)
    scope.add_new_plot("PLOT1", "TIMETREND")
    scope.add_ref(1)
    scope.add_search(1)
    scope.add_new_measurement("MEAS1", "MAXIMUM", meas_source="REF1")
    scope.add_new_measurement("MEAS1", "MAXIMUM")
    scope.add_measurement_table(1)
    # Power visa commands modified to simulate failure to add
    with pytest.raises(AssertionError):
        scope.add_power(1)
    # Assert there are no errors after testing feature additions
    scope.expect_esr(0, '0,"No events to report - queue empty"')

    # Simulate successful feature deletion by replacing name of item with BLANK
    scope.write(":BUS:ADDNew BLANK")
    scope.write(":HISTOGRAM:ADDNew BLANK")
    scope.write(":MATH:ADDNew BLANK")
    scope.write(":MEAS:ADDNew BLANK")
    scope.write(":TABLE:ADDNew BLANK")
    scope.write(":PLOT:ADDNew BLANK")
    scope.write(":POWER:ADDNew BLANK")
    scope.write(":REF:ADDNew BLANK")
    # Test that features can be deleted
    scope.delete_bus(1)
    scope.delete_histogram(1)
    scope.delete_math(1)
    scope.delete_measurement(1)
    scope.delete_measurement_table(1)
    scope.delete_plot(1)
    scope.delete_power(1)
    scope.delete_ref(1)
    # Search deletion not simulated to simulate deletion error
    with pytest.raises(AssertionError):
        scope.delete_search(1)
    # Assert there are no errors after testing feature deletions
    scope.expect_esr(0, '0,"No events to report - queue empty"')
    assert scope.query("EMPTY:STRING?", allow_empty=True) == ""
    with pytest.raises(SystemError):
        scope.query("EMPTY:STRING?")

    # Test generating waveform functionality
    scope.generate_function(10e3, scope.source_device_constants.functions.SIN, 0.5, 0.0)
    scope.generate_function(
        10e3, scope.source_device_constants.functions.SIN, 0.5, 0.0, termination="HIGHZ"
    )
    scope.setup_burst(10e3, scope.source_device_constants.functions.RAMP, 0.5, 0.0, burst_count=1)
    with pytest.raises(
        TypeError,
        match="Generate Waveform does not accept functions as non Enums. "
        "Please use 'source_device_constants.functions'.",
    ):
        scope.generate_function(
            25e6,
            scope.source_device_constants.functions.PULSE.value,  # pyright: ignore[reportArgumentType]
            1.0,
            0.0,
            "all",
        )
    # Test saving waveform functionality
    scope.save_waveform_to_reference("temp.wfm", "REF1")
    # Assert there are no errors after testing waveform generations and saving
    scope.expect_esr(0, '0,"No events to report - queue empty"')

    # Test curve query write to csv functionality with multi-frame curve
    filepath = f"temp_{sys.version_info.major}{sys.version_info.minor}.csv"
    try:
        curve = scope.curve_query(1, wfm_type="TimeDomain", output_csv_file=filepath)
        with open(filepath, encoding="utf8") as curve_csv:
            # Remove trailing command a format string as list of ints based on commas
            curve_reformatted_from_file = list(map(int, curve_csv.read()[:-1].split(",")))
            # Flatten list of lists returned from multi-frame curve query
            curve_flattened_return_list = [item for child_list in curve for item in child_list]
            # Assert what was saved in file matches what was returned, after formatting is applied
            assert curve_flattened_return_list == curve_reformatted_from_file
    finally:
        os.remove(filepath)
    # Simulate single frame curve
    scope.write(":CURVE 1,0,1,0")
    # Simulate an available source list able to accommodate all waveform types
    scope.write(
        ":DATA:SOURCE:AVAIL "
        "CH1_D0,CH1_SV_BASEBAND_IQ,CH1_SV_NORMAL,CH1_FREQ_VS_TIME,CH1_MAG_VS_TIME"
    )
    # Assert curve_query returns the expected response and handles errors
    assert scope.curve_query(1, wfm_type="TimeDomain") == [1, 0, 1, 0]
    assert scope.curve_query(1, wfm_type="IQ") == [1.0, 0.0, 1.0, 0.0]
    assert scope.curve_query(1, wfm_type="Spectrum") == [1.0, 0.0, 1.0, 0.0]
    assert scope.curve_query(1, wfm_type="FreqVsTime") == [1.0, 0.0, 1.0, 0.0]
    assert scope.curve_query(1, wfm_type="MagVsTime") == [1.0, 0.0, 1.0, 0.0]
    # Test that invalid wave form types are handled
    with pytest.raises(AssertionError):
        scope.curve_query(1, wfm_type="InvalidWFM")
    # Test curve queries when there is no valid data source return empty list
    scope.write(":DATA:SOURCE:AVAIL None")
    with pytest.warns(UserWarning):
        assert scope.curve_query(1, wfm_type="TimeDomain") == []
    # Assert there are no errors after testing curve query
    scope.expect_esr(0, '0,"No events to report - queue empty"')

    # Assert that getting license list returns the correct tuple
    assert scope.license_list == ("LIC5", "LIC4")
    assert scope.has_license("LIC5")
    # Assert that the number of digital bits in channel is 8
    assert scope.num_dig_bits_in_ch == 8

    # Test recalling reference functionality
    scope.recall_reference("temp.wfm", 1)
    scope.recall_reference('"temp.wfm"', 1)
    # Test recalling session functionality
    scope.recall_session("session")
    scope.recall_session('"session"')

    # Test toggle all channels on/off
    scope.turn_all_channels_on()
    scope.turn_all_channels_off()

    # Test that single sequence can be set
    scope.single_sequence()

    # simulate a reboot
    scope.reboot()

    # test some internal assertions
    with pytest.raises(AssertionError, match="none is not a valid item.*"):
        scope._add_or_delete_dynamic_item("none", 1)  # noqa: SLF001

    with pytest.raises(AssertionError, match="No error string was provided"):
        scope.expect_esr(1)

    # Assert no errors after completing testing
    scope.expect_esr(0, '0,"No events to report - queue empty"')
    assert scope.get_eventlog_status() == (True, '0,"No events to report - queue empty"')

    # MSO2 overridden channel names implementation
    mso2_scope: MSO2 = cast(
        MSO2, device_manager.add_scope("MSO22-HOSTNAME", connection_type="TCPIP")
    )
    # Assert 2 series device was added and aliased properly (TCPIP)
    assert mso2_scope.hostname == "MSO22-200201"
    assert id(device_manager.get_scope(number_or_alias=mso2_scope.device_number)) == id(mso2_scope)
    assert mso2_scope.all_channel_names_list == ("CH1", "CH2")
    assert mso2_scope.usb_drives == ("E:",)
    assert mso2_scope.ip_address == ""
    with mock.patch(
        "tm_devices.drivers.pi.scopes.tekscope.mso2.MSO2.license_list",
        property(mock.MagicMock(return_value=("MSO",))),
    ):
        # reset the cache
        # noinspection PyPropertyAccess
        del mso2_scope.total_channels
        assert mso2_scope.all_channel_names_list == ("CH1", "CH2", "DCH1")
        # MSO2 does not support the probe queries, so do it now while analog and digital are covered
        assert mso2_scope.channel["CH1"] == TekScopeChannel(
            name="CH1",
            probe=TekProbeData(probetype="ANALOG", probe_id_sernumber="N/A", probe_id_type="1X"),
        )
        assert mso2_scope.channel["DCH1"] == TekScopeChannel(
            name="DCH1",
            probe=TekProbeData(probetype="DIGITAL", probe_id_sernumber="N/A", probe_id_type="N/A"),
        )


def test_iafg(device_manager: DeviceManager) -> None:
    """Test the IAFG.

    Args:
        device_manager: The DeviceManager object.
    """
    mso64: MSO6 = cast(MSO6, device_manager.add_scope("MSO64-HOSTNAME", alias="mso64"))
    mso64_constraints = mso64.get_waveform_constraints(
        SignalGeneratorFunctionsIAFG.SIN,
        frequency=25.0e6,
    )

    assert mso64_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=20.0e-3, upper=5.0),
        offset_range=ParameterBounds(lower=-2.5, upper=2.5),
        frequency_range=ParameterBounds(lower=100.0e-3, upper=50.0e6),
        sample_rate_range=ParameterBounds(lower=250.0e6, upper=250.0e6),
        square_duty_cycle_range=ParameterBounds(lower=25.0, upper=75.0),
        pulse_width_range=ParameterBounds(lower=1.0e-8, upper=3.0e-8),
        ramp_symmetry_range=ParameterBounds(lower=0.0, upper=100.0),
    )

    mso64_constraints = mso64.get_waveform_constraints(
        SignalGeneratorFunctionsIAFG.SQUARE,
        frequency=5.0e6,
    )

    assert mso64_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=20.0e-3, upper=5.0),
        offset_range=ParameterBounds(lower=-2.5, upper=2.5),
        frequency_range=ParameterBounds(lower=100.0e-3, upper=25.0e6),
        sample_rate_range=ParameterBounds(lower=250.0e6, upper=250.0e6),
        square_duty_cycle_range=ParameterBounds(lower=10.0, upper=90.0),
        pulse_width_range=ParameterBounds(lower=2.0e-08, upper=1.8e-07),
        ramp_symmetry_range=ParameterBounds(lower=0.0, upper=100.0),
    )

    mso64_constraints = mso64.get_waveform_constraints(
        SignalGeneratorFunctionsIAFG.RAMP,
    )

    assert mso64_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=20.0e-3, upper=5.0),
        offset_range=ParameterBounds(lower=-2.5, upper=2.5),
        frequency_range=ParameterBounds(lower=100.0e-3, upper=500.0e3),
        sample_rate_range=ParameterBounds(lower=250.0e6, upper=250.0e6),
        square_duty_cycle_range=ParameterBounds(lower=10.0, upper=90.0),
        pulse_width_range=None,
        ramp_symmetry_range=ParameterBounds(lower=0.0, upper=100.0),
    )

    mso64_constraints = mso64.get_waveform_constraints(
        SignalGeneratorFunctionsIAFG.SINC,
    )

    assert mso64_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=20.0e-3, upper=3.0),
        offset_range=ParameterBounds(lower=-2.5, upper=2.5),
        frequency_range=ParameterBounds(lower=100.0e-3, upper=2.0e6),
        sample_rate_range=ParameterBounds(lower=250.0e6, upper=250.0e6),
        square_duty_cycle_range=ParameterBounds(lower=10.0, upper=90.0),
        pulse_width_range=None,
        ramp_symmetry_range=ParameterBounds(lower=0.0, upper=100.0),
    )

    mso64_constraints = mso64.get_waveform_constraints(
        SignalGeneratorFunctionsIAFG.HAVERSINE,
    )

    assert mso64_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=20.0e-3, upper=2.5),
        offset_range=ParameterBounds(lower=-2.5, upper=2.5),
        frequency_range=ParameterBounds(lower=100.0e-3, upper=5.0e6),
        sample_rate_range=ParameterBounds(lower=250.0e6, upper=250.0e6),
        square_duty_cycle_range=ParameterBounds(lower=10.0, upper=90.0),
        pulse_width_range=None,
        ramp_symmetry_range=ParameterBounds(lower=0.0, upper=100.0),
    )

    mso56b: MSO5 = cast(MSO5B, device_manager.add_scope("MSO58B-HOSTNAME", alias="mso56b"))
    mso56b_constraints = mso56b.get_waveform_constraints(
        SignalGeneratorFunctionsIAFG.SIN,
    )

    assert mso56b_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=20.0e-3, upper=5.0),
        offset_range=ParameterBounds(lower=-2.5, upper=2.5),
        frequency_range=ParameterBounds(lower=100.0e-3, upper=100.0e6),
        sample_rate_range=ParameterBounds(lower=250.0e6, upper=250.0e6),
        square_duty_cycle_range=ParameterBounds(lower=10.0, upper=90.0),
        pulse_width_range=None,
        ramp_symmetry_range=ParameterBounds(lower=0.0, upper=100.0),
    )

    with pytest.raises(ValueError, match="IAFGs must have a waveform defined."):
        mso64.get_waveform_constraints()

    with pytest.raises(ValueError, match=r"Output state value must be 1 \(ON\) or 0 \(OFF\)\."):
        mso64.internal_afg.set_state(-1)


def test_exceptions(device_manager: DeviceManager) -> None:
    """Test visa error handling within tekscope.

    Args:
        device_manager: The DeviceManager object.
    """
    # Test that visa errors are caught appropriately
    scope = device_manager.add_scope("mso22-timeout")
    with pytest.raises(visa.errors.Error):
        scope.turn_channel_on("CH1")
    with pytest.raises(AssertionError):
        scope.expect_esr(0)
    device_manager.remove_all_devices()


def test_tekscope70k(device_manager: DeviceManager, capsys: pytest.CaptureFixture[str]) -> None:
    """Test the tekscope_70k implementation.

    Args:
        device_manager: The DeviceManager object.
        capsys: The captured stdout and stderr.
    """
    scope = device_manager.add_scope("127.0.0.1")
    assert scope.ip_address == "127.0.0.1"
    assert scope.hostname == ""
    # Test some generic device functionality
    assert scope.wait_for_network_connection(
        wait_time=0.05, sleep_seconds=1, accept_immediate_connection=True, verbose=True
    )
    assert (
        f"Successfully established a network connection with {scope.ip_address}"
        in capsys.readouterr().out
    )
    assert scope.wait_for_network_connection(
        wait_time=0.05, sleep_seconds=1, accept_immediate_connection=True, verbose=False
    )
    assert (
        f"Successfully established a network connection with {scope.ip_address}"
        not in capsys.readouterr().out
    )
    with mock.patch(
        "subprocess.check_output", mock.MagicMock(side_effect=subprocess.CalledProcessError(1, ""))
    ):
        assert not scope.wait_for_network_connection(
            wait_time=0.05, sleep_seconds=1, accept_immediate_connection=True, verbose=True
        )
        assert (
            f"Unable to establish a network connection with {scope.ip_address}"
            in capsys.readouterr().out
        )
    with pytest.raises(AssertionError):
        scope.wait_for_network_connection(
            wait_time=0.05, sleep_seconds=1, accept_immediate_connection=False, verbose=False
        )
    scope.expect_esr(0)
    with pytest.raises(SystemError):
        scope.query("EMPTY?")

    with pytest.raises(NotImplementedError) as error:
        scope.reboot()
    assert str(error.value.args[0]) == "``.reboot()`` is not yet implemented for the MSO70K driver"

    # get coverage for different IDN format
    scope_70k: MSO70KDX = cast(
        MSO70KDX, device_manager.add_scope("MSO70KDX-HOSTNAME", alias="mso70k")
    )
    assert scope_70k.sw_version == Version("10.99.1")

    # Assert the total number of analog channels.
    assert scope_70k.total_channels == 4
    # Assert the total number of digital channels.
    assert scope_70k.num_dig_bits_in_ch == 16


def test_long_device_name(device_manager: DeviceManager) -> None:
    """Test a device with a long name.

    Args:
        device_manager: The DeviceManager object.
    """
    # Custom class for testing external device drivers
    try:
        device_manager._external_device_drivers = {  # noqa: SLF001
            "LONGNAMEINSTRUMENT": TmDevicesUnitTestOnlyCustomMSO5
        }

        with pytest.warns(UserWarning):
            scope = device_manager.add_scope("LONGNAMEINSTRUMENT-HOSTNAME")

        assert not scope.total_channels
        assert scope.all_channel_names_list == ()

        # noinspection PyUnresolvedReferences
        assert scope.custom_mso5_method("test-value") == (  # pyright: ignore[reportUnknownMemberType,reportAttributeAccessIssue]
            "This is a custom method for the LONGNAMEINSTRUMENT device. value='test-value'"
        )

    finally:
        device_manager._external_device_drivers = None  # noqa: SLF001


def test_tekscope3k_4k(device_manager: DeviceManager, capsys: pytest.CaptureFixture[str]) -> None:
    """Test the tekscope3k_4k implementation.

    Args:
        device_manager: The DeviceManager object.
        capsys: The captured stdout and stderr.
    """
    scope = device_manager.add_scope("MDO3K-HOSTNAME")
    assert scope.all_channel_names_list == ("CH1", "CH2", "CH3", "CH4")
    assert scope.hostname == "MDO3K-HOSTNAME"

    with mock.patch.dict("os.environ", {"TM_DEVICES_UNIT_TESTS_REBOOT_ALLOW": "true"}, clear=True):
        assert scope.reboot(quiet_period=5)
    stdout = capsys.readouterr().out
    assert "Waiting for 5 seconds" in stdout
    assert "Connection Reestablished with " in stdout

    with mock.patch("pyvisa.ResourceManager", mock.MagicMock(side_effect=visa.Error())):
        assert not scope.reboot()
    with mock.patch.dict("os.environ", {"TM_DEVICES_UNIT_TESTS_REBOOT_ALLOW": "true"}, clear=True):
        assert scope._open()  # noqa: SLF001

    scope2 = device_manager.add_scope("MDO3-HOSTNAME")
    assert scope2.total_channels == 2


def test_tekscopesw(device_manager: DeviceManager) -> None:
    """Test the TekScopeSW implementation.

    Args:
        device_manager: The DeviceManager object.
    """
    scope: TekScopeSW = cast(TekScopeSW, device_manager.add_scope("TEKSCOPESW-HOSTNAME"))
    # Assert TekScopeSW device was added and aliased properly
    assert scope.hostname == "hostname"
    assert id(device_manager.get_scope(number_or_alias=scope.device_number)) == id(scope)
    assert scope.all_channel_names_list == ()
    assert scope.usb_drives == ("E:",)
    assert scope.ip_address == ""
    assert not scope.total_channels
    assert scope.all_channel_names_list == ()
