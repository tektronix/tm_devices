# pyright: reportPrivateUsage=none
"""Test the AFGs."""
from unittest import mock

import pytest
import pyvisa as visa

from packaging.version import Version

from tm_devices import DeviceManager
from tm_devices.drivers.pi.signal_sources.afgs.afg import AFGSourceDeviceConstants
from tm_devices.helpers.constants_and_dataclasses import UNIT_TEST_TIMEOUT


def test_afg3kc(device_manager: DeviceManager) -> None:
    """Test the AFG3KC driver.

    Args:
        device_manager: The DeviceManager object.
    """
    afg3kc = device_manager.add_afg(
        "afg3kc-hostname", alias="afg3kc", connection_type="SOCKET", port=10001
    )
    assert id(device_manager.get_afg(number_or_alias="afg3kc")) == id(afg3kc)
    assert id(device_manager.get_afg(number_or_alias=1)) == id(afg3kc)
    assert afg3kc.visa_timeout == UNIT_TEST_TIMEOUT
    assert afg3kc.default_visa_timeout == UNIT_TEST_TIMEOUT
    assert afg3kc.resource_expression == "TCPIP0::AFG3KC-HOSTNAME::10001::SOCKET"
    assert afg3kc.total_channels == 2
    assert afg3kc.idn_string == "TEKTRONIX,AFG3252C,SERIAL1,SCPI:99.0 FV:3.2.3"
    assert afg3kc.sw_version == Version("3.2.3")
    assert afg3kc.all_channel_names_list == ("SOURCE1", "SOURCE2")
    assert afg3kc.source_device_constants == AFGSourceDeviceConstants(
        memory_page_size=2,
        memory_max_record_length=128 * 1024,
        memory_min_record_length=2,
    )
    assert afg3kc.check_visa_connection()
    afg3kc.write("*OPC?")
    assert afg3kc.read() == "1"
    assert afg3kc.opt_string == "0"
    assert afg3kc.query("SYSTEM:ERROR?") == '0,"No error"'
    assert afg3kc.query("SYSTEM:ERROR?", remove_quotes=True) == "0,No error"
    assert afg3kc.expect_esr(0)[0]
    with mock.patch("pyvisa.highlevel.VisaLibraryBase.clear", mock.MagicMock(return_value=None)):
        assert afg3kc.query_expect_timeout("INVALID?", timeout_ms=1) == ""
    with mock.patch(
        "pyvisa.resources.messagebased.MessageBasedResource.query",
        mock.MagicMock(side_effect=visa.errors.Error("custom error")),
    ), pytest.raises(visa.errors.Error):
        assert afg3kc.query_expect_timeout("INVALID?", timeout_ms=1) == ""
    assert afg3kc.expect_esr(32, '1, Command error\n0,"No error"')[0]
    with pytest.raises(AssertionError):
        afg3kc.expect_esr(32, '1, Command error\n0,"No error"')

    afg3kc.generate_waveform(25e6, afg3kc.source_device_constants.functions.PULSE, 1.0, 0.0, "all")
    afg3kc.generate_waveform(
        25e6,
        afg3kc.source_device_constants.functions.SIN,
        1.0,
        0.0,
        "SOURCE1",
        burst=1,
        termination="HIGHZ",
    )
    afg3kc.generate_waveform(
        25e6,
        afg3kc.source_device_constants.functions.RAMP,
        1.0,
        0.0,
        "SOURCE1",
        burst=1,
        termination="FIFTY",
    )
    afg3kc.generate_waveform(
        25e6,
        afg3kc.source_device_constants.functions.DC,
        1.0,
        0.0,
        "SOURCE1",
        termination="HIGHZ",
    )
    afg3kc.generate_waveform(
        25e6,
        afg3kc.source_device_constants.functions.PULSE,
        1.0,
        0.0,
        "SOURCE1",
        termination="FIFTY",
    )
    assert afg3kc.expect_esr(0)[0]
    assert afg3kc.get_eventlog_status() == (True, '0,"No error"')

    with pytest.raises(AssertionError, match="No error string was provided"):
        afg3kc.expect_esr(1)

    with pytest.raises(AssertionError, match="Invalid channel name 'ch', valid items: "):
        afg3kc._validate_channels("ch")  # noqa: SLF001

    with pytest.raises(AssertionError, match="Invalid channel name '99', valid items: "):
        afg3kc._validate_channels("99")  # noqa: SLF001

    with pytest.raises(
        TypeError,
        match="Generate Waveform does not accept functions as non Enums. "
        "Please use 'source_device_constants.functions'.",
    ):
        afg3kc.generate_waveform(
            25e6,
            afg3kc.source_device_constants.functions.PULSE.value,  # pyright: ignore[reportArgumentType]
            1.0,
            0.0,
            "all",
        )


def test_afg31k(device_manager: DeviceManager, capsys: pytest.CaptureFixture[str]) -> None:
    """Test the AFG31K driver.

    Args:
        device_manager: The DeviceManager object.
        capsys: The pytest capture fixture.
    """
    afg31k = device_manager.add_afg("afg31k-hostname")

    _ = capsys.readouterr().out  # throw away stdout

    # Check hostname
    assert afg31k.hostname == "AFG31K-HOSTNAME"

    # simulate a reboot
    afg31k.reboot()

    stdout = capsys.readouterr().out
    assert "SYSTem:RESTart" in stdout

    assert not afg31k.has_errors()
