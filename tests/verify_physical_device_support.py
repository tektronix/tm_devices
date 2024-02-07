"""A script verifying support for any number of real, physical devices.

Any devices that need to be verified must be defined in a file called "verify_devices.yaml", located
in the same folder as this module. See the configuration documentation for details on the file
format.
"""
import os

from pathlib import Path

from tm_devices import DeviceManager

if __name__ == "__main__":
    os.environ["TM_DEVICES_CONFIG"] = f"{Path(__file__).parent}/verify_devices.yaml"

    with DeviceManager(verbose=False) as device_manager:
        device_manager.setup_cleanup_enabled = False
        device_manager.teardown_cleanup_enabled = False
        for device in device_manager.devices.values():
            print(device)
            device.cleanup()
            assert not device.has_errors()
