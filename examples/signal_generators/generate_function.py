"""An example showing how to generate a function using an AFG and AWG."""

from tm_devices import DeviceManager
from tm_devices.drivers import AFG3K

with DeviceManager(verbose=True) as dm:
    # Create a connection to the AFG and indicate that it is an AFG3K for type hinting
    afg3k: AFG3K = dm.add_afg("192.168.0.1")  # pyright: ignore[reportAssignmentType]

    # Generate a RAMP waveform on SOURCE1 of the AFG3K with the provided properties.
    afg3k.generate_function(
        function=afg3k.source_device_constants.functions.RAMP,
        channel="SOURCE1",
        frequency=10e6,
        amplitude=0.5,
        offset=0,
        symmetry=50.0,
    )
