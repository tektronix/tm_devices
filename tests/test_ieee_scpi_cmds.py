"""Test the IEEE 488.2 SCPI commands."""

import pytest

from tm_devices import DeviceManager
from tm_devices.drivers.afgs.afg import AFG

_DEVICE_ALIAS = "TESTING_AFG_IEEE"


@pytest.fixture(name="device")
def _device(device_manager: DeviceManager) -> AFG:  # pyright: ignore[reportUnusedFunction]
    """Reset the device after each test."""
    afg = device_manager.add_afg("afg3252c-hostname", alias=_DEVICE_ALIAS)
    afg.ieee_cmds.ese(0)
    afg.ieee_cmds.sre(0)
    afg.ieee_cmds.psc(True)
    return afg


def test_ieee_scpi_cmds(device: AFG) -> None:
    """Test the IEEE 488.2 SCPI commands."""
    assert device.ieee_cmds.esr() == "0"
    assert device.ieee_cmds.tst() == "1"
    assert device.ieee_cmds.stb() == "4"
    assert device.ieee_cmds.opt() == "0"
    assert device.ieee_cmds.lrn() == "*RST;"
    assert device.ieee_cmds.ese() == "0"
    device.ieee_cmds.ese(255)
    with pytest.raises(
        ValueError, match="value=256 is not a valid value. The value must be between 0 and 255."
    ):
        device.ieee_cmds.ese(256)
    assert device.ieee_cmds.sre() == "0"
    device.ieee_cmds.sre(255)
    with pytest.raises(
        ValueError, match="value=256 is not a valid value. The value must be between 0 and 255."
    ):
        device.ieee_cmds.sre(256)
    assert device.ieee_cmds.opc(write=True) == ""
    device.ieee_cmds.wai()
    assert device.ieee_cmds.psc() == "1"
    assert device.ieee_cmds.psc(False) == "0"
