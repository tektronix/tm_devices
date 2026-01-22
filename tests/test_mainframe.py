"""Test the MFs."""

from typing import TYPE_CHECKING
from unittest import mock

import pytest
import pyvisa as visa

from tm_devices import DeviceManager

if TYPE_CHECKING:
    from tm_devices.drivers import MP5103


@pytest.mark.parametrize(
    ("slot", "expected_exception", "match_msg"),
    [
        # Test valid slot
        (3, None, None),
        # Test invalid slot number (low)
        (0, ValueError, r"Slot number 0 is out of range. It must be between 1 and 3."),
        # Test invalid slot number (high)
        (4, ValueError, r"Slot number 4 is out of range. It must be between 1 and 3."),
        # Test invalid module
        (
            2,
            ValueError,
            r"Error encountered while accessing module commands object: TBD Module "
            r"in slot 2 is an invalid module.",
        ),
        # Test slot with a non-integer type
        (
            "2",
            TypeError,
            r"2 of type str is not a valid slot number. A valid slot number must be an integer.",
        ),
        # Test unsupported module.
        (
            1,
            TypeError,
            r"No supported PSU module found in slot 1. The supported PSU modules are: MPSU50-2ST.",
        ),
    ],
)
def test_mainframe_psu_exception(
    device_manager: DeviceManager,
    slot: int,
    expected_exception: type[BaseException] | None,
    match_msg: str,
) -> None:
    """Test the MP5103 driver for PSU modules."""
    device_manager.remove_all_devices()
    mainframe: MP5103 = device_manager.add_mf(
        "TCPIP::MP5103-HOSTNAME::10002::SOCKET", alias="mainframe-device"
    )

    # Common mainframe checks
    assert id(device_manager.get_mf(number_or_alias="mainframe-device")) == id(mainframe)
    assert id(device_manager.get_mf(number_or_alias=mainframe.device_number)) == id(mainframe)

    assert mainframe.manufacturer == "TEKTRONIX"
    assert mainframe.model == "MP5103"
    assert mainframe.serial == "0"
    assert mainframe.total_slots == 3

    expected_slot_names = tuple(str(x) for x in range(1, mainframe.total_slots + 1))
    assert mainframe.all_slot_names_list == expected_slot_names

    # Event log checks
    assert mainframe.expect_esr(0)
    assert mainframe.get_errors() == (0, ())

    with mock.patch("pyvisa.highlevel.VisaLibraryBase.clear", mock.MagicMock(return_value=None)):
        assert mainframe.query_expect_timeout("INVALID?", timeout_ms=1) == ""
    with (
        mock.patch(
            "pyvisa.resources.messagebased.MessageBasedResource.query",
            mock.MagicMock(side_effect=visa.errors.Error("custom error")),
        ),
        pytest.raises(visa.errors.Error),
    ):
        mainframe.query_expect_timeout("INVALID?", timeout_ms=1)
    assert mainframe.expect_esr(32, ("Command error", "No Error"))

    expected_ch_names = tuple(str(x) for x in range(1, mainframe.total_channels + 1))
    assert mainframe.all_channel_names_list == expected_ch_names

    # Slot-specific PSU checks
    if expected_exception:
        with pytest.raises(expected_exception, match=match_msg):
            mainframe.get_module_commands_psu(slot)
    else:
        psu_commands = mainframe.get_module_commands_psu(slot)
        assert psu_commands.model == "MPSU50-2ST"
        assert mainframe.total_channels == 2


def test_tsp_buffer_cleanup(
    device_manager: DeviceManager, caplog: pytest.LogCaptureFixture
) -> None:
    """Test TSP buffer creation and cleanup for PSU modules."""
    mainframe: MP5103 = device_manager.add_mf(
        "TCPIP::MP5103-HOSTNAME::10002::SOCKET", alias="mainframe-device"
    )

    mainframe.commands.slot[3].psu[1].makebuffer("10", buffer_name="buff_name")
    mainframe.cleanup()
    assert any("buff_name = nil" in rec.message for rec in caplog.records)


@pytest.mark.parametrize(
    ("slot", "expected_exception", "match_msg"),
    [
        # Test valid slot
        (
            3,
            TypeError,
            r"No supported SMU module found in slot 3. The supported SMU modules are: MSMU60-2",
        ),
        # Test invalid slot number (low)
        (0, ValueError, r"Slot number 0 is out of range. It must be between 1 and 3."),
        # Test invalid slot number (high)
        (4, ValueError, r"Slot number 4 is out of range. It must be between 1 and 3."),
        # Test invalid module
        (
            2,
            ValueError,
            r"Error encountered while accessing module commands object: TBD Module "
            r"in slot 2 is an invalid module.",
        ),
        # Test slot with a non-integer type
        (
            "2",
            TypeError,
            r"2 of type str is not a valid slot number. A valid slot number must be an integer.",
        ),
        # Test unsupported module.
        (
            1,
            TypeError,
            r"No supported SMU module found in slot 1. The supported SMU modules are: MSMU60-2",
        ),
    ],
)
def test_mainframe_smu_exception(
    device_manager: DeviceManager,
    slot: int,
    expected_exception: type[BaseException] | None,
    match_msg: str,
) -> None:
    """Test the MP5103 driver for PSU modules."""
    device_manager.remove_all_devices()
    mainframe: MP5103 = device_manager.add_mf(
        "TCPIP::MP5103-HOSTNAME::10002::SOCKET", alias="mainframe-device"
    )
    if expected_exception:
        with pytest.raises(expected_exception, match=match_msg):
            mainframe.get_module_commands_smu(slot)
    else:
        smu_commands = mainframe.get_module_commands_smu(slot)
        assert smu_commands.model == "MSMU60-2"
        assert mainframe.total_channels == 2
