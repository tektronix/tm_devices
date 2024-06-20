# pyright: reportPrivateUsage=none
"""Verify that all device drivers and connection types can be used."""

from collections import Counter
from typing import List

from mock_server import PORT
from tm_devices import DeviceManager
from tm_devices.helpers import ConnectionTypes, SupportedModels


# pylint: disable=too-many-locals
def test_all_device_drivers(
    device_manager: DeviceManager,
    mock_http_server: None,  # noqa: ARG001
) -> None:
    """Verify all device drivers can be used.

    Args:
        device_manager: The Device Manager object.
        mock_http_server: The mock http server.
    """
    # A list of entries containing: (device_type, address, port, connection_type, device_driver)
    simulated_device_list = (
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
        ("SCOPE", "TEKSCOPESW-HOSTNAME", None, None, None),
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

    # Remove all previous devices.
    device_manager.remove_all_devices()

    try:
        # Create a list of all supported models and connections
        supported_connections_list: List[str] = sorted(
            x.value for x in ConnectionTypes if not str(x.value).startswith(("_", "MOCK"))
        )
        created_connections_list: List[str] = []
        supported_models_list: List[str] = sorted(x.value for x in SupportedModels)
        created_models_list: List[str] = []
        drivers_with_auto_generated_commands: List[str] = []

        # Add devices to the Device Manager and add the models to the list of created models
        for dev_type, address, port, connection_type, device_driver in simulated_device_list:
            device = device_manager._add_device(  # noqa: SLF001
                dev_type,
                address,
                port=port,
                connection_type=connection_type,
                device_driver=device_driver,
            )
            device.cleanup()
            assert not device.has_errors()
            assert device.commands is not None
            assert device.command_argument_constants is not None
            created_models_list.append(device.__class__.__name__)
            created_connections_list.append(device.connection_type)
            if device.commands != NotImplemented:
                drivers_with_auto_generated_commands.append(device.__class__.__name__)

        created_models_list.sort()
        created_connections_list = sorted(set(created_connections_list))

        # Verify all supported models
        models_without_testing = set(supported_models_list) - set(created_models_list)
        created_counts = Counter(created_models_list)
        assert all(
            count == 1 for _, count in created_counts.items()
        ), f"Some drivers were instantiated more than once: {created_counts.most_common(1)[0]}"
        assert (
            created_models_list == supported_models_list
        ), f"Some models are not tested: {models_without_testing=}"

        # Verify all supported connections
        connections_without_testing = set(supported_connections_list) - set(
            created_connections_list
        )
        assert (
            created_connections_list == supported_connections_list
        ), f"Some connections are not tested: {connections_without_testing=}"
    finally:
        # Remove all devices after testing.
        device_manager.remove_all_devices()

    print(f"\nVerified all {len(simulated_device_list)} device drivers")
    print(
        f"{len(drivers_with_auto_generated_commands)} device drivers have auto-generated commands"
    )
