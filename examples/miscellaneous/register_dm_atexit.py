"""An example showing how to register the DeviceManager to close on program exit."""

import atexit

from tm_devices import DeviceManager

# Create the device manager
dm = DeviceManager()

# Set up the device manager to be automatically closed when the program terminates
atexit.register(dm.close)

# Add a device
scope = dm.add_scope("192.168.1.102")

# Use the device
print(scope)

# The device manager will automatically close as the script exits, no code required.
