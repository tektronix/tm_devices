# pyright: reportPrivateUsage=none
"""Verify that all device drivers and connection types can be used."""

import contextlib
import sys

from collections import Counter
from pathlib import Path
from typing import Generator, List, Optional

import pytest

from mock_server import PORT
from tm_devices import DeviceManager
from tm_devices.helpers import ConnectionTypes, SupportedModels

# A list of entries containing: (device_type, address, port, connection_type, device_driver)
SIMULATED_DEVICE_LIST = (
    ("AFG", "AFG3051-HOSTNAME", None, None, None),
    ("AFG", "AFG3022B-HOSTNAME", None, None, None),
    ("AFG", "AFG3252C-HOSTNAME", 10001, "SOCKET", None),
    ("AFG", "AFG31021-HOSTNAME", None, None, None),
    ("AWG", "AWG5200OPT50-HOSTNAME", None, None, None),
    ("AWG", "AWG5012-HOSTNAME", None, None, None),
    ("AWG", "AWG5002B-HOSTNAME", None, None, None),
    ("AWG", "AWG5012C-HOSTNAME", None, None, None),
    ("AWG", "AWG7051OPT01-HOSTNAME", None, None, None),
    ("AWG", "AWG7062BOPT02-HOSTNAME", None, None, None),
    ("AWG", "AWG7082COPT01-HOSTNAME", None, None, None),
    ("AWG", "AWG70001AOPT150-HOSTNAME", None, None, None),
    ("AWG", "AWG70002BOPT208-HOSTNAME", None, None, None),
    ("SCOPE", "MSO22-HOSTNAME", None, None, None),
    ("SCOPE", "MSO56-SERIAL1", None, "USB", None),
    ("SCOPE", "MSO44-HOSTNAME", None, None, None),
    ("SCOPE", "MSO44B-HOSTNAME", None, None, None),
    ("SCOPE", "MSO58B-HOSTNAME", None, None, None),
    ("SCOPE", "MSO58LP-HOSTNAME", None, None, None),
    ("SCOPE", "LPD64-HOSTNAME", None, None, None),
    ("SCOPE", "MSO64-HOSTNAME", None, None, None),
    ("SCOPE", "MSO68B-HOSTNAME", None, None, None),
    ("SCOPE", "DPO70K-HOSTNAME", None, None, None),
    ("SCOPE", "DPO70KDX-HOSTNAME", None, None, None),
    ("SCOPE", "DPO70KSX-HOSTNAME", None, None, None),
    ("SCOPE", "TSOVU-HOSTNAME", None, None, None),
    ("SCOPE", "TEKSCOPEPC-HOSTNAME", None, None, None),
    ("SCOPE", "MSO2K-HOSTNAME", None, None, None),
    ("SCOPE", "MSO2KB-HOSTNAME", None, None, None),
    ("SCOPE", "DPO2K-HOSTNAME", None, None, None),
    ("SCOPE", "DPO2KB-HOSTNAME", None, None, None),
    ("SCOPE", "MDO3-HOSTNAME", None, None, None),
    ("SCOPE", "MDO4K-HOSTNAME", None, None, None),
    ("SCOPE", "MDO4KB-HOSTNAME", None, None, None),
    ("SCOPE", "MDO4KC-HOSTNAME", None, None, None),
    ("SCOPE", "MSO4K-HOSTNAME", None, None, None),
    ("SCOPE", "MSO4KB-HOSTNAME", None, None, None),
    ("SCOPE", "DPO4K-HOSTNAME", None, None, None),
    ("SCOPE", "DPO4KB-HOSTNAME", None, None, None),
    ("SCOPE", "192.168.0.101", None, None, None),
    ("SCOPE", "127.0.0.1", None, None, None),
    ("SCOPE", "MSO70KDX-HOSTNAME", None, None, None),
    ("SMU", "SMU-HOSTNAME", None, None, None),  # smu2612b
    ("SMU", "SMU2450-HOSTNAME", None, None, None),
    ("SMU", "SMU2460-HOSTNAME", None, None, None),
    ("SMU", "SMU2461-HOSTNAME", None, None, None),
    ("SMU", "SMU2470-HOSTNAME", None, None, None),
    ("SMU", "SMU2601B-HOSTNAME", None, None, None),
    ("SMU", "SMU2601B-PULSE-HOSTNAME", None, None, None),
    ("SMU", "SMU2602B-HOSTNAME", None, None, None),
    ("SMU", "SMU2604B-HOSTNAME", None, None, None),
    ("SMU", "SMU2606B-HOSTNAME", None, None, None),
    ("SMU", "SMU2611B-HOSTNAME", None, None, None),
    ("SMU", "1", None, "SERIAL", None),  # smu2614b
    ("SMU", "SMU2634B-HOSTNAME", None, None, None),
    ("SMU", "SMU2635B-HOSTNAME", None, None, None),
    ("SMU", "1", None, "GPIB", None),  # smu2636b
    ("SMU", "SMU2651A-HOSTNAME", None, None, None),
    ("SMU", "SMU2657A-HOSTNAME", None, None, None),
    ("PSU", "PSU-HOSTNAME", None, None, None),
    ("PSU", "PSU2220-HOSTNAME", None, None, None),
    ("DMM", "DMM6500-HOSTNAME", None, None, None),
    ("DMM", "DMM7510-HOSTNAME", None, None, None),
    ("DMM", "DMM7512-HOSTNAME", None, None, None),
    ("SMU", "SMU2601A-HOSTNAME", None, None, None),
    ("SMU", "SMU2602A-HOSTNAME", None, None, None),
    ("SMU", "SMU2604A-HOSTNAME", None, None, None),
    ("SMU", "SMU2611A-HOSTNAME", None, None, None),
    ("SMU", "SMU2612A-HOSTNAME", None, None, None),
    ("SMU", "SMU2614A-HOSTNAME", None, None, None),
    ("SMU", "SMU2634A-HOSTNAME", None, None, None),
    ("SMU", "SMU2635A-HOSTNAME", None, None, None),
    ("SMU", "SMU2636A-HOSTNAME", None, None, None),
    ("SMU", "SMU6430-HOSTNAME", None, None, None),
    ("SMU", "SMU6514-HOSTNAME", None, None, None),
    ("SMU", "SMU6517B-HOSTNAME", None, None, None),
    ("SMU", "SMU2400-HOSTNAME", None, None, None),
    ("SMU", "SMU2401-HOSTNAME", None, None, None),
    ("SMU", "SMU2410-HOSTNAME", None, None, None),
    ("SS", "SS3706A-HOSTNAME", None, None, None),
    ("PSU", "PSU2200-HOSTNAME", None, None, None),
    ("PSU", "PSU2231-HOSTNAME", None, None, None),
    ("PSU", "PSU2231A-HOSTNAME", None, None, None),
    ("PSU", "PSU2280-HOSTNAME", None, None, None),
    ("PSU", "PSU2281-HOSTNAME", None, None, None),
    ("MT", "127.0.0.1", PORT, "REST_API", "TMT4"),
    ("DAQ", "DAQ6510-HOSTNAME", None, None, None),
    ("SCOPE", "DPO5K-HOSTNAME", None, None, None),
    ("SCOPE", "DPO5KB-HOSTNAME", None, None, None),
    ("SCOPE", "DPO7K-HOSTNAME", None, None, None),
    ("SCOPE", "DPO7KC-HOSTNAME", None, None, None),
    ("SCOPE", "DPO70KC-HOSTNAME", None, None, None),
    ("SCOPE", "DPO70KD-HOSTNAME", None, None, None),
    ("SCOPE", "DSA70K-HOSTNAME", None, None, None),
    ("SCOPE", "DSA70KC-HOSTNAME", None, None, None),
    ("SCOPE", "DSA70KD-HOSTNAME", None, None, None),
    ("SCOPE", "MSO5K-HOSTNAME", None, None, None),
    ("SCOPE", "MSO5KB-HOSTNAME", None, None, None),
    ("SCOPE", "MSO70KC-HOSTNAME", None, None, None),
)

# Global variables for this test module
created_connections_list: List[str] = []
created_models_list: List[str] = []
drivers_with_auto_generated_commands: List[str] = []


@pytest.fixture(autouse=True, scope="module")
def _reset_dm(device_manager: DeviceManager) -> Generator[None, None, None]:  # pyright: ignore[reportUnusedFunction]
    """Reset the device_manager settings before and after running the tests in this module.

    Args:
        device_manager: The device manager fixture.
    """
    device_manager.remove_all_devices()
    yield
    device_manager.remove_all_devices()


# noinspection PyUnusedLocal
@pytest.mark.order(1)
@pytest.mark.parametrize(
    ("dev_type", "address", "port", "connection_type", "device_driver"), SIMULATED_DEVICE_LIST
)
def test_device_driver(
    device_manager: DeviceManager,
    dev_type: str,
    address: str,
    port: Optional[int],
    connection_type: Optional[str],
    device_driver: Optional[str],
    mock_http_server: None,  # noqa: ARG001
) -> None:
    """Verify all device drivers can be used.

    Args:
        device_manager: The Device Manager object.
        dev_type: The device type.
        address: The device address.
        port: The device port.
        connection_type: The device connection type.
        device_driver: The device driver.
        mock_http_server: The mock http server.
    """
    device = device_manager._add_device(  # noqa: SLF001
        dev_type,
        address,
        port=port,
        connection_type=connection_type,
        device_driver=device_driver,
    )
    device.cleanup()
    assert not device.has_errors()
    created_models_list.append(device.__class__.__name__)
    created_connections_list.append(device.connection_type)
    with contextlib.suppress(NotImplementedError):
        if device.commands != NotImplemented:
            drivers_with_auto_generated_commands.append(device.__class__.__name__)


@pytest.mark.order(2)
@pytest.mark.depends(on=["test_device_driver"])
def test_all_device_drivers() -> None:
    """Verify all device drivers can be created and all connection types are tested."""
    # Create a list of all supported models and connections
    supported_connections_list: List[str] = sorted(
        x.value for x in ConnectionTypes if not str(x.value).startswith(("_", "MOCK"))
    )
    supported_models_list: List[str] = sorted(x.value for x in SupportedModels)

    created_models_list.sort()
    sorted_created_connections_list = sorted(set(created_connections_list))

    # Verify all supported models
    models_without_testing = set(supported_models_list) - set(created_models_list)
    created_counts = Counter(created_models_list)
    assert all(count == 1 for _, count in created_counts.items()), (
        f"Some drivers were instantiated more than once: {created_counts.most_common(1)[0]}"
    )
    assert created_models_list == supported_models_list, (
        f"Some models are not tested: {models_without_testing=}"
    )

    # Verify all supported connections
    connections_without_testing = set(supported_connections_list) - set(
        sorted_created_connections_list
    )
    assert sorted_created_connections_list == supported_connections_list, (
        f"Some connections are not tested: {connections_without_testing=}"
    )

    print(f"\nVerified all {len(SIMULATED_DEVICE_LIST)} device drivers")  # noqa: T201
    print(  # noqa: T201
        f"{len(drivers_with_auto_generated_commands)} device drivers have auto-generated commands"
    )


@pytest.mark.order(3)
@pytest.mark.depends(on=["test_device_driver"])
def test_visa_device_command_logging() -> None:
    """Test the VISA command log file contents."""
    generated_file = (
        Path(__file__).parent / f"logs/unit_test_py{sys.version_info.major}{sys.version_info.minor}"
        f"_visa_commands_SMU2410-HOSTNAME.log"
    )
    assert generated_file.exists(), f"File not found: {generated_file}"
    assert (
        generated_file.read_text()
        == """*CLS
*RST
*OPC?
*ESR?
SYSTEM:ERROR?
*ESR?
SYSTEM:ERROR?
"""
    )
