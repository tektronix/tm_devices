"""An example of creating and reading from a dynamic buffer."""

from tm_devices import DeviceManager
from tm_devices.drivers import SMU2601B

with DeviceManager() as device_manager:
    # Create a SMU and type hint it as a 2601B
    smu: SMU2601B = device_manager.add_smu("192.168.0.1")  # pyright: ignore[reportAssignmentType]

    # Create a buffer
    BUFFER_NAME = "mybuffer"
    smu.write(f"{BUFFER_NAME} = smua.makebuffer(100)")
    smu.commands.buffer_var[BUFFER_NAME].clear()
    smu.commands.buffer_var[BUFFER_NAME].collectsourcevalues = 1  # Enable source value storage
    smu.commands.buffer_var[BUFFER_NAME].appendmode = 1  # Enable buffer append mode
    capacity = smu.commands.buffer_var[BUFFER_NAME].capacity  # Get the buffer capacity
