"""Test the PSUs."""

from typing import TYPE_CHECKING

from packaging.version import Version

from tm_devices import DeviceManager

if TYPE_CHECKING:
    from tm_devices.drivers import PSU2230


def test_psu(device_manager: DeviceManager) -> None:
    """Test the PSU driver.

    Args:
        device_manager: The DeviceManager object.
    """
    psu: PSU2230 = device_manager.add_psu("psu-hostname", alias="psu-device")
    assert id(device_manager.get_psu(number_or_alias="psu-device")) == id(psu)
    assert id(device_manager.get_psu(number_or_alias=psu.device_number)) == id(psu)

    assert psu.manufacturer == "Keithley instruments"
    assert psu.model == "2230G-30-6"
    assert psu.serial == "0123456789AF"
    assert psu.sw_version == Version("1.04")
    assert psu.fpga_version == Version("1.06")
    assert psu.total_channels == 3

    assert psu.expect_esr(0)[0]
    assert psu.get_eventlog_status() == (True, '0,"No error"')
