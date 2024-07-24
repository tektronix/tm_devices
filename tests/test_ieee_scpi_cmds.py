"""Test the IEEE 488.2 SCPI commands."""

import pytest

from tm_devices import DeviceManager


def test_ieee_scpi_cmds(device_manager: DeviceManager) -> None:
    """Test the IEEE 488.2 SCPI commands."""
    device_manager.remove_all_devices()
    device = device_manager.add_afg("afg3252c-hostname")
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
