# pyright: reportPrivateUsage=none
"""Test generic PIDevice functionality."""

from unittest import mock

import pytest
import pyvisa as visa

from tm_devices import DeviceManager


def test_pi_device(  # noqa: PLR0915
    device_manager: DeviceManager, capsys: pytest.CaptureFixture[str]
) -> None:
    """Test generic PIDevice functionality.

    Args:
        device_manager: The DeviceManager object.
        capsys: The captured stdout and stderr.
    """
    scope = device_manager.add_scope("MSO22-HOSTNAME")
    assert scope._open()  # noqa: SLF001
    assert scope.query_binary("CURVE?") == [0.0]
    assert "Query Binary Values >>  " in capsys.readouterr().out
    assert scope.query_binary("CURVE?", verbose=False) == [0.0]
    assert "Query Binary Values >>  " not in capsys.readouterr().out
    assert scope.query_raw_binary("CURVE?") == b"#14\x00\x00\x00\x00\n"
    assert "Query Raw Binary >>  " in capsys.readouterr().out
    assert scope.query_raw_binary("CURVE?", verbose=False) == b"#14\x00\x00\x00\x00\n"
    assert "Query Raw Binary >>  " not in capsys.readouterr().out
    scope.factory_reset()
    assert "Write >>  'FACTORY'" in capsys.readouterr().out
    with pytest.raises(AssertionError) as error:
        scope.query_response("*OPC?", 2, custom_message_prefix="Custom prefix")
    assert "Custom prefix, query_response failed for query: *OPC?" in str(error)
    assert scope.query_response_not("*OPC?", "2", custom_message_prefix="Custom prefix") == (
        True,
        "1",
    )
    assert scope.query_response("*OPC?", "1") == (True, "1")
    with pytest.raises(AssertionError):
        scope.query_response_not("*OPC?", "1")
    assert scope.query_less_than("*OPC?", 1, percentage=True, allow_equal=True)
    with pytest.raises(AssertionError):
        scope.query_less_than("*OPC?", 1)

    scope.write_raw(b"FACTORY", verbose=False)
    assert "Write Raw >>  " not in capsys.readouterr().out
    with mock.patch(
        "pyvisa.resources.messagebased.MessageBasedResource.write_raw",
        mock.MagicMock(side_effect=visa.VisaIOError(123)),
    ), pytest.raises(visa.Error):
        scope.write_raw(b"INVALID")
    with pytest.raises(visa.Error):
        scope.query_binary("INVALID?")
    with pytest.raises(SystemError):
        scope.query_binary("EMPTYBIN?")
    with pytest.raises(visa.Error):
        scope.query_raw_binary("INVALID?")
    with pytest.raises(SystemError):
        scope.query_raw_binary("EMPTY?")
    with mock.patch(
        "pyvisa.resources.messagebased.MessageBasedResource.write",
        mock.MagicMock(side_effect=visa.VisaIOError(123)),
    ), pytest.raises(visa.Error):
        scope.write("INVALID")
    with mock.patch(
        "pyvisa.resources.resource.Resource.wait_on_event",
        mock.MagicMock(return_value=object()),
    ):
        assert scope.wait_for_srq_event(1)
    with mock.patch(
        "pyvisa.resources.messagebased.MessageBasedResource.read",
        mock.MagicMock(return_value="2"),
    ), pytest.raises(SystemError):
        scope.write("FACTORY", opc=True)
    # from OPC return which was previously mocked and unable to be read
    assert scope.read() == "1"

    assert scope.wait_for_visa_connection(0.1, sleep_seconds=0, accept_immediate_connection=True)
    stdout = capsys.readouterr().out
    assert f"Attempting to establish a VISA connection with {scope.resource_expression}" in stdout
    assert f"Successfully established a VISA connection with {scope.resource_expression} " in stdout
    assert scope.wait_for_visa_connection(
        0.1, sleep_seconds=1, accept_immediate_connection=True, verbose=False
    )
    stdout = capsys.readouterr().out
    assert "Attempting to establish a VISA connection with " not in stdout
    assert "Successfully established a VISA connection with " not in stdout
    with pytest.raises(AssertionError):
        scope.wait_for_visa_connection(0.1, sleep_seconds=0, accept_immediate_connection=False)
    with mock.patch("pyvisa.ResourceManager", mock.MagicMock(side_effect=visa.Error())):
        assert not scope.wait_for_visa_connection(
            0.05, sleep_seconds=0, accept_immediate_connection=True
        )
        assert "Unable to establish a VISA connection with " in capsys.readouterr().out

    # Test a temporary VISA timeout
    old_timeout = scope.visa_timeout
    old_verbose = scope.verbose
    with scope.temporary_visa_timeout(6000):
        stdout = capsys.readouterr().out
        assert scope.visa_timeout != old_timeout
        assert scope.visa_timeout == 6000
        assert "VISA timeout set to: 6000ms" in stdout
        # test a temporary verbose OFF
        with scope.temporary_verbose(False):
            assert scope.verbose != old_verbose
            # do something that would normally cause a printout
            scope.visa_timeout = 5000
            stdout = capsys.readouterr().out
            assert stdout == ""
            assert scope.visa_timeout == 5000
    stdout = capsys.readouterr().out
    assert f"VISA timeout set to: {old_timeout}ms" in stdout
    assert scope.visa_timeout == old_timeout

    # Test closing a device that is powered off
    with mock.patch(
        "pyvisa.resources.resource.Resource.close",
        mock.MagicMock(side_effect=visa.VisaIOError(123)),
    ), pytest.warns(Warning):
        scope._close()  # noqa: SLF001
        assert scope._visa_resource is None  # noqa: SLF001
        assert not scope._is_open  # noqa: SLF001

    # Re-open the device for device manager teardown
    with mock.patch.dict("os.environ", {"TM_DEVICES_UNIT_TESTS_REBOOT_ALLOW": "true"}, clear=True):
        assert scope._open()  # noqa: SLF001

    # Ensure VERBose is off
    scope.set_and_check(":VERBose", 0)
    # Expect set not needed since verbose is already off.
    assert scope.set_if_needed(":VERBose", 0) == (False, "0")
    # Expect set needed
    assert scope.set_if_needed(":VERBose", 1) == (True, "1")
    # Set VERBose back to off
    scope.set_and_check(":VERBose", "0")

    scope.set_and_check(":DISPLAY:WAVEVIEW:CH1:STATE", 1)
    scope.poll_query(1, ":DISPLAY:WAVEVIEW:CH1:STATE?", 1.0, sleep_time=0)
    # Display waveview state is set to 1, but we are wanting 0.
    with pytest.raises(AssertionError):
        scope.poll_query(2, ":DISPLAY:WAVEVIEW:CH1:STATE?", 0, sleep_time=0)
    # Set display waveview state to a maximum bound value.
    scope.set_and_check(":DISPLAY:WAVEVIEW:CH1:STATE", 9.9e37)
    with pytest.raises(AssertionError):
        # Pass in the maximum bound value as invalid values.
        scope.poll_query(
            1, ":DISPLAY:WAVEVIEW:CH1:STATE?", 9.9e37, sleep_time=0, invalid_values=[9.9e37]
        )
