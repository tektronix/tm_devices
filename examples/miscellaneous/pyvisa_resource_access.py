"""Directly access the PyVISA resource object."""

from tm_devices import DeviceManager

with DeviceManager() as device_manager:
    # Create the scope object.
    scope = device_manager.add_scope("192.168.0.1")

    # Access the PyVISA resource object directly,
    # `scope.visa_resource` returns a MessageBasedResource object from PyVISA.
    scope.visa_resource.read_bytes(1024)
