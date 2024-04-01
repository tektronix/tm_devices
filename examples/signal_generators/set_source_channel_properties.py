"""An example showing the use of an AWG source channel."""

from tm_devices import DeviceManager
from tm_devices.drivers import AWG5K

with DeviceManager(verbose=True) as dm:
    # Create a connection to the scope and indicate that it is an AWG5K for type hinting.
    awg5k: AWG5K = dm.add_awg("192.168.0.1")  # pyright: ignore[reportAssignmentType]

    # Set the offset to 0.5 on SOURCE1 of the AWG5K
    awg5k.source_channel["SOURCE1"].set_offset(0.5)

    # Set the amplitude to 0.2 on SOURCE1 of the AWG5K
    awg5k.source_channel["SOURCE1"].set_amplitude(0.2)

    # Turn on SOURCE1 of the AWG5K
    awg5k.source_channel["SOURCE1"].set_state(1)
