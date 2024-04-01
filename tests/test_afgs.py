# pyright: reportPrivateUsage=none
"""Test the AFGs."""

from unittest import mock

import pytest
import pyvisa as visa

from packaging.version import Version

from tm_devices import DeviceManager
from tm_devices.drivers.pi.signal_generators.afgs.afg import (
    AFGSourceDeviceConstants,
    ExtendedSourceDeviceConstants,
    ParameterBounds,
    SignalGeneratorFunctionsAFG,
)
from tm_devices.helpers.constants_and_dataclasses import UNIT_TEST_TIMEOUT


def test_afg3k(device_manager: DeviceManager) -> None:  # noqa: PLR0915  # pylint: disable=too-many-locals
    """Test the AFG3KC driver.

    Args:
        device_manager: The DeviceManager object.
    """
    afg3252c = device_manager.add_afg(
        "afg3252c-hostname", alias="afg3252c", connection_type="SOCKET", port=10001
    )
    assert id(device_manager.get_afg(number_or_alias="afg3252c")) == id(afg3252c)
    assert id(device_manager.get_afg(number_or_alias=1)) == id(afg3252c)
    assert afg3252c.visa_timeout == UNIT_TEST_TIMEOUT
    assert afg3252c.default_visa_timeout == UNIT_TEST_TIMEOUT
    assert afg3252c.resource_expression == "TCPIP0::AFG3252C-HOSTNAME::10001::SOCKET"
    assert afg3252c.total_channels == 2
    assert afg3252c.idn_string == "TEKTRONIX,AFG3252C,SERIAL1,SCPI:99.0 FV:3.2.3"
    assert afg3252c.sw_version == Version("3.2.3")
    assert afg3252c.all_channel_names_list == ("SOURCE1", "SOURCE2")
    assert afg3252c.visa_backend == "PyVISA-sim"
    assert afg3252c.source_device_constants == AFGSourceDeviceConstants(
        memory_page_size=2,
        memory_max_record_length=128 * 1024,
        memory_min_record_length=2,
    )
    assert afg3252c.check_visa_connection()
    afg3252c.write("*OPC?")
    assert afg3252c.read() == "1"
    assert afg3252c.opt_string == "0"
    assert afg3252c.query("SYSTEM:ERROR?") == '0,"No error"'
    assert afg3252c.query("SYSTEM:ERROR?", remove_quotes=True) == "0,No error"
    assert afg3252c.expect_esr(0)[0]
    with mock.patch("pyvisa.highlevel.VisaLibraryBase.clear", mock.MagicMock(return_value=None)):
        assert afg3252c.query_expect_timeout("INVALID?", timeout_ms=1) == ""
    with mock.patch(
        "pyvisa.resources.messagebased.MessageBasedResource.query",
        mock.MagicMock(side_effect=visa.errors.Error("custom error")),
    ), pytest.raises(visa.errors.Error):
        assert afg3252c.query_expect_timeout("INVALID?", timeout_ms=1) == ""
    assert afg3252c.expect_esr(32, '1, Command error\n0,"No error"')[0]
    with pytest.raises(AssertionError):
        afg3252c.expect_esr(32, '1, Command error\n0,"No error"')

    with pytest.raises(AssertionError, match="No error string was provided"):
        afg3252c.expect_esr(1)

    with pytest.raises(AssertionError, match="Invalid channel name 'ch', valid items: "):
        afg3252c._validate_channels("ch")  # noqa: SLF001

    with pytest.raises(AssertionError, match="Invalid channel name '99', valid items: "):
        afg3252c._validate_channels("99")  # noqa: SLF001

    with pytest.raises(
        TypeError,
        match="Generate Waveform does not accept functions as non Enums. "
        "Please use 'source_device_constants.functions'.",
    ):
        afg3252c.generate_function(
            25e6,
            afg3252c.source_device_constants.functions.PULSE.value,  # type: ignore[arg-type]
            1.0,
            0.0,
            "all",
        )

    afg3051 = device_manager.add_afg("afg3051-hostname", alias="afg3051")

    afg3051_constraints = afg3051.get_waveform_constraints(SignalGeneratorFunctionsAFG.RAMP)

    assert afg3051_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=20.0e-3, upper=20.0),
        offset_range=ParameterBounds(lower=-10.0, upper=10.0),
        frequency_range=ParameterBounds(lower=1.0e-6, upper=500.0e3),
        sample_rate_range=ParameterBounds(lower=250.0e6, upper=250.0e6),
        square_duty_cycle_range=None,
        pulse_width_range=None,
        ramp_symmetry_range=None,
    )

    afg3011c = device_manager.add_afg("afg3011c-hostname", alias="afg3011c")

    afg3011c_constraints = afg3011c.get_waveform_constraints(SignalGeneratorFunctionsAFG.SIN)

    assert afg3011c_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=40.0e-3, upper=40.0),
        offset_range=ParameterBounds(lower=-20.0, upper=20.0),
        frequency_range=ParameterBounds(lower=1.0e-6, upper=10.0e6),
        sample_rate_range=ParameterBounds(lower=250.0e6, upper=250.0e6),
        square_duty_cycle_range=None,
        pulse_width_range=None,
        ramp_symmetry_range=None,
    )

    afg3021c = device_manager.add_afg("afg3021c-hostname", alias="afg3021c")

    afg3021c_constraints = afg3021c.get_waveform_constraints(SignalGeneratorFunctionsAFG.SQUARE)

    assert afg3021c_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=20.0e-3, upper=20.0),
        offset_range=ParameterBounds(lower=-10.0, upper=10.0),
        frequency_range=ParameterBounds(lower=1.0e-3, upper=25.0e6),
        sample_rate_range=ParameterBounds(lower=250.0e6, upper=250.0e6),
        square_duty_cycle_range=None,
        pulse_width_range=None,
        ramp_symmetry_range=None,
    )

    afg3052c = device_manager.add_afg("afg3052c-hostname", alias="afg3052c")

    afg3052c_constraints = afg3052c.get_waveform_constraints(SignalGeneratorFunctionsAFG.RAMP)

    assert afg3052c_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=20.0e-3, upper=20.0),
        offset_range=ParameterBounds(lower=-10.0, upper=10.0),
        frequency_range=ParameterBounds(lower=1.0e-6, upper=800.0e3),
        sample_rate_range=ParameterBounds(lower=250.0e6, upper=250.0e6),
        square_duty_cycle_range=None,
        pulse_width_range=None,
        ramp_symmetry_range=None,
    )

    afg3101c = device_manager.add_afg("afg3101c-hostname", alias="afg3101c")

    afg3101c_constraints = afg3101c.get_waveform_constraints(
        SignalGeneratorFunctionsAFG.ARBITRARY, waveform_length=5_000
    )

    assert afg3101c_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=40.0e-3, upper=20.0),
        offset_range=ParameterBounds(lower=-10.0, upper=10.0),
        frequency_range=ParameterBounds(lower=1.0e-3, upper=50.0e6),
        sample_rate_range=ParameterBounds(lower=1.0e9, upper=1.0e9),
        square_duty_cycle_range=None,
        pulse_width_range=None,
        ramp_symmetry_range=None,
    )

    afg3151c = device_manager.add_afg("afg3151c-hostname", alias="afg3151c")

    afg3151c_constraints = afg3151c.get_waveform_constraints(SignalGeneratorFunctionsAFG.LORENTZ)

    assert afg3151c_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=40.0e-3, upper=16.0),
        offset_range=ParameterBounds(lower=-10.0, upper=10.0),
        frequency_range=ParameterBounds(lower=1.0e-6, upper=1.5e6),
        sample_rate_range=ParameterBounds(lower=250.0e6, upper=250.0e6),
        square_duty_cycle_range=None,
        pulse_width_range=None,
        ramp_symmetry_range=None,
    )

    afg3252c_constraints = afg3252c.get_waveform_constraints(SignalGeneratorFunctionsAFG.SIN)

    assert afg3252c_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=100.0e-3, upper=8.0),
        offset_range=ParameterBounds(lower=-5.0, upper=5.0),
        frequency_range=ParameterBounds(lower=1.0e-6, upper=240.0e6),
        sample_rate_range=ParameterBounds(lower=250.0e6, upper=250.0e6),
        square_duty_cycle_range=None,
        pulse_width_range=None,
        ramp_symmetry_range=None,
    )

    with pytest.raises(ValueError, match="AFGs must have a waveform defined."):
        afg3252c.get_waveform_constraints()

    with pytest.raises(ValueError, match=r"Output state value must be 1 \(ON\) or 0 \(OFF\)\."):
        afg3252c.source_channel["SOURCE1"].set_state(-1)

    afg3252c.source_channel["SOURCE1"].set_impedance(1)
    query_value = afg3252c.query("OUTPUT1:IMPEDANCE?")
    assert float(query_value) == 1
    afg3252c.source_channel["SOURCE1"].set_impedance(10e3)
    query_value = afg3252c.query("OUTPUT1:IMPEDANCE?")
    assert float(query_value) == 10e3

    afg3252c.source_channel["SOURCE1"].set_pulse_duty_cycle(0.4)
    query_value = afg3252c.query("SOURCE1:PULSE:DCYCLE?")
    assert float(query_value) == 0.4
    afg3252c.source_channel["SOURCE1"].set_pulse_duty_cycle(99.6)
    query_value = afg3252c.query("SOURCE1:PULSE:DCYCLE?")
    assert float(query_value) == 99.6
    afg3252c.source_channel["SOURCE1"].set_pulse_duty_cycle(75)
    query_value = afg3252c.query("SOURCE1:PULSE:DCYCLE?")
    assert float(query_value) == 75

    afg3252c.source_channel["SOURCE1"].set_ramp_symmetry(0.0)
    query_value = afg3252c.query("SOURCE1:FUNCTION:RAMP:SYMMETRY?")
    assert not float(query_value)
    afg3252c.source_channel["SOURCE1"].set_ramp_symmetry(100.0)
    query_value = afg3252c.query("SOURCE1:FUNCTION:RAMP:SYMMETRY?")
    assert float(query_value) == 100.0
    afg3252c.source_channel["SOURCE1"].set_ramp_symmetry(25.0)
    query_value = afg3252c.query("SOURCE1:FUNCTION:RAMP:SYMMETRY?")
    assert float(query_value) == 25.0

    afg3252c.source_channel["SOURCE1"].set_burst_state(1)
    query_value = afg3252c.query("SOURCE1:BURST:STATE?")
    assert float(query_value) == 1
    error_message = r"Burst state value must be 1 \(ON\) or 0 \(OFF\)\."
    with pytest.raises(ValueError, match=error_message):
        afg3252c.source_channel["SOURCE1"].set_burst_state(5)

    afg3252c.source_channel["SOURCE1"].set_burst_count(10)
    query_value = afg3252c.query("SOURCE1:BURST:NCYCLES?")
    assert float(query_value) == 10


def test_afg31k(device_manager: DeviceManager, capsys: pytest.CaptureFixture[str]) -> None:
    """Test the AFG31K driver.

    Args:
        device_manager: The DeviceManager object.
        capsys: The pytest capture fixture.
    """
    afg31021 = device_manager.add_afg("afg31021-hostname")

    _ = capsys.readouterr().out  # throw away stdout

    # Check hostname
    assert afg31021.hostname == "AFG31021-HOSTNAME"

    # simulate a reboot
    afg31021.reboot()

    stdout = capsys.readouterr().out
    assert "SYSTem:RESTart" in stdout

    assert not afg31021.has_errors()

    afg31021_constraints = afg31021.get_waveform_constraints(
        SignalGeneratorFunctionsAFG.SIN,
        waveform_length=16383,
        frequency=20.0e6,
    )

    assert afg31021_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=2.0e-3, upper=20.0),
        offset_range=ParameterBounds(lower=-10.0, upper=10.0),
        frequency_range=ParameterBounds(lower=1.0e-6, upper=25.0e6),
        sample_rate_range=ParameterBounds(lower=250.0e6, upper=250.0e6),
        square_duty_cycle_range=None,
        pulse_width_range=None,
        ramp_symmetry_range=None,
    )

    afg31051 = device_manager.add_afg("afg31051-hostname")
    afg31051_constraints = afg31051.get_waveform_constraints(
        SignalGeneratorFunctionsAFG.SQUARE,
        waveform_length=16383,
        frequency=70.0e6,
    )

    assert afg31051_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=2.0e-3, upper=16.0),
        offset_range=ParameterBounds(lower=-10.0, upper=10.0),
        frequency_range=ParameterBounds(lower=1.0e-6, upper=40.0e6),
        sample_rate_range=ParameterBounds(lower=1.0e9, upper=1.0e9),
        square_duty_cycle_range=None,
        pulse_width_range=None,
        ramp_symmetry_range=None,
    )

    afg31101 = device_manager.add_afg("afg31101-hostname")
    afg31101_constraints = afg31101.get_waveform_constraints(
        SignalGeneratorFunctionsAFG.RAMP,
        frequency=90.0e6,
    )

    assert afg31101_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=2.0e-3, upper=12.0),
        offset_range=ParameterBounds(lower=-10.0, upper=10.0),
        frequency_range=ParameterBounds(lower=1.0e-6, upper=1.0e6),
        sample_rate_range=ParameterBounds(lower=250.0e6, upper=250.0e6),
        square_duty_cycle_range=None,
        pulse_width_range=None,
        ramp_symmetry_range=None,
    )

    afg31152 = device_manager.add_afg("afg31152-hostname")
    afg31152_constraints = afg31152.get_waveform_constraints(
        SignalGeneratorFunctionsAFG.ARBITRARY,
        waveform_length=16383,
        frequency=0.5e6,
    )

    assert afg31152_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=2.0e-3, upper=10.0),
        offset_range=ParameterBounds(lower=-5.0, upper=5.0),
        frequency_range=ParameterBounds(lower=1.0e-6, upper=75.0e6),
        sample_rate_range=ParameterBounds(lower=2.0e9, upper=2.0e9),
        square_duty_cycle_range=None,
        pulse_width_range=None,
        ramp_symmetry_range=None,
    )

    afg31251 = device_manager.add_afg("afg31251-hostname")
    afg31251_constraints = afg31251.get_waveform_constraints(
        SignalGeneratorFunctionsAFG.SIN,
        frequency=210.0e6,
    )

    assert afg31251_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=2.0e-3, upper=8.0),
        offset_range=ParameterBounds(lower=-5.0, upper=5.0),
        frequency_range=ParameterBounds(lower=1.0e-6, upper=250.0e6),
        sample_rate_range=ParameterBounds(lower=250.0e6, upper=250.0e6),
        square_duty_cycle_range=None,
        pulse_width_range=None,
        ramp_symmetry_range=None,
    )
