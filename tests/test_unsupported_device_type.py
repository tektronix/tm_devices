# pyright: reportPrivateUsage=none
"""Test the usage of unsupported device types."""

from pathlib import Path
from typing import Tuple, Union

import pytest

from tm_devices import DeviceManager
from tm_devices.driver_mixins.device_control.pi_control import PIControl
from tm_devices.drivers.device import Device
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


class CustomUnsupportedDeviceUnitTestOnly(PIControl, Device):
    """A custom device that is not one of the officially supported devices for unit tests."""

    _DEVICE_TYPE = "CustomDeviceType"

    @cached_property
    def total_channels(self) -> int:  # noqa: D102  # pylint: disable=no-self-use
        return 4

    def expect_esr(self, esr: Union[int, str], error_string: str = "") -> Tuple[bool, str]:  # noqa: D102,ARG002
        return True, ""


def test_unsupported_device_type_class(device_manager: DeviceManager) -> None:
    """Test using the DeviceManager to connect to an unsupported device type."""
    try:
        device_manager.remove_all_devices()
        assert device_manager.devices == {}
        # Add the custom driver to the DM
        device_manager._external_device_drivers = {  # noqa: SLF001
            "UNSUPPORTED": CustomUnsupportedDeviceUnitTestOnly
        }

        with pytest.warns(
            UserWarning,
            match="An unsupported device type is being added to the DeviceManager. "
            "Not all functionality will be available in the device driver. "
            "Please consider contributing to tm_devices to implement official support for "
            "this device type.",
        ), pytest.warns(
            UserWarning, match='The "UNSUPPORTED" model is not supported by tm_devices'
        ):
            unsupported_device: CustomUnsupportedDeviceUnitTestOnly = (
                device_manager.add_unsupported_device(
                    "UNSUPPORTED-DEVICE-TYPE", alias="MY-UNSUPPORTED-DEVICE"
                )
            )

        assert len(device_manager.devices) == 1
        assert unsupported_device.total_channels == 4
        assert unsupported_device.serial == "000000"
        assert unsupported_device.__class__ == CustomUnsupportedDeviceUnitTestOnly

        # Remove the device
        device_manager.remove_all_devices()
        assert device_manager.devices == {}

        # Load in the device from a config file
        with pytest.warns(
            UserWarning,
            match="An unsupported device type is being added to the DeviceManager. "
            "Not all functionality will be available in the device driver. "
            "Please consider contributing to tm_devices to implement official support for "
            "this device type.",
        ), pytest.warns(
            UserWarning, match='The "UNSUPPORTED" model is not supported by tm_devices'
        ):
            device_manager.load_config_file(
                Path(__file__).parent / "samples/unsupported_device_type_config.yaml"
            )
        assert len(device_manager.devices) == 1
        assert unsupported_device.total_channels == 4
        assert unsupported_device.serial == "000000"
        assert unsupported_device.__class__ == CustomUnsupportedDeviceUnitTestOnly

        # Remove the device
        device_manager.remove_all_devices()
        assert device_manager.devices == {}
    finally:
        device_manager._external_device_drivers = None  # noqa: SLF001
