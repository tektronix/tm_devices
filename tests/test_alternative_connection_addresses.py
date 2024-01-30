# pyright: reportPrivateUsage=none
"""Tests for various methods of connecting to devices."""
from typing import Optional, Tuple

import pytest

from tm_devices import DeviceManager


# NOTE: The entries in this should be a subset of the entries in the unit test named
#       ``test_helpers.test_detect_visa_resource_expression``.
@pytest.mark.parametrize(
    ("address", "device_type", "connection", "expected_info"),
    [
        (
            "TCPIP::MSO56-HOSTNAME::INSTR",
            "SCOPE",
            None,
            ("TCPIP", "MSO5", "MSO56", "SERIAL1"),
        ),
        (
            "MSO56-HOSTNAME",
            "SCOPE",
            "TCPIP",
            ("TCPIP", "MSO5", "MSO56", "SERIAL1"),
        ),
        (
            "MSO56-SERIAL1",
            "SCOPE",
            "USB",
            ("USB", "MSO5", "MSO56", "SERIAL1"),
        ),
        (
            "USB0::0x0699::0x0522::SERIAL1::INSTR",
            "SCOPE",
            None,
            ("USB", "MSO5", "MSO56", "SERIAL1"),
        ),
        (
            "USB0::0x0699::0x0522::200201::INSTR",
            "SCOPE",
            None,
            ("USB", "MSO5B", "MSO58B", "200201"),
        ),
        (
            "SMU2450-HOSTNAME",
            "SMU",
            None,
            ("TCPIP", "SMU2450", "Model 2450", "01419964"),
        ),
        (
            "127.0.0.9",
            "SMU",
            None,
            ("TCPIP", "SMU2450", "Model 2450", "01419964"),
        ),
        (
            "Model 2450-01419964",
            "SMU",
            "USB",
            ("USB", "SMU2450", "Model 2450", "01419964"),
        ),
        (
            "2450-01419964",
            "SMU",
            "USB",
            ("USB", "SMU2450", "Model 2450", "01419964"),
        ),
        (
            "USB0::0x05E6::0x2450::01419964::INSTR",
            "SMU",
            None,
            ("USB", "SMU2450", "Model 2450", "01419964"),
        ),
        (
            "USB::0x05E6::0x2450::01419964::INSTR",
            "SMU",
            None,
            ("USB", "SMU2450", "Model 2450", "01419964"),
        ),
        (
            "TCPIP0::SMU2450-HOSTNAME::INSTR",
            "SMU",
            None,
            ("TCPIP", "SMU2450", "Model 2450", "01419964"),
        ),
        (
            "TCPIP::SMU2450-HOSTNAME::INSTR",
            "SMU",
            None,
            ("TCPIP", "SMU2450", "Model 2450", "01419964"),
        ),
        (
            "TCPIP0::127.0.0.9::inst0::INSTR",
            "SMU",
            None,
            ("TCPIP", "SMU2450", "Model 2450", "01419964"),
        ),
        (
            "TCPIP::127.0.0.9::inst0::INSTR",
            "SMU",
            None,
            ("TCPIP", "SMU2450", "Model 2450", "01419964"),
        ),
        (
            "ASRL1::INSTR",
            "SMU",
            None,
            ("SERIAL", "SMU2614B", "Model 2614B", "4498311"),
        ),
        (
            "TCPIP::AFG3KC-HOSTNAME::10001::SOCKET",
            "AFG",
            None,
            ("SOCKET", "AFG3KC", "AFG3252C", "SERIAL1"),
        ),
    ],
)
def test_alternative_connection_methods(
    device_manager: DeviceManager,
    address: str,
    device_type: str,
    connection: Optional[str],
    expected_info: Tuple[str, str, str, str],
) -> None:
    """Verify various non-standard connection addresses work properly.

    Args:
        device_manager: The DeviceManager object.
        address: The address of the device.
        device_type: The type of device to create.
        connection: The connection type of the device.
        expected_info: The expected information of the device.
    """
    device_manager.remove_all_devices()
    device = device_manager._add_device(  # noqa: SLF001
        device_type, address, connection_type=connection
    )
    assert device.device_type == device_type
    assert (device.connection_type, device.series, device.model, device.serial) == expected_info
