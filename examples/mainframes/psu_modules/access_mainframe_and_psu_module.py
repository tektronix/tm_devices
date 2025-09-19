"""Add a mainframe to the Device Manager and access a PSU module through the mainframe."""

from typing import cast, TYPE_CHECKING

from tm_devices import DeviceManager
from tm_devices.drivers import MP5103

if TYPE_CHECKING:
    from tm_devices.commands import MPSU50_2STCommands

with DeviceManager(verbose=True) as device_manager:
    # Add a mainframe to the device manager and access its commands.
    mainframe: MP5103 = device_manager.add_mf("192.168.0.1")

    # Some examples demonstrating the usage of mainframe level commands.
    mf_model = mainframe.commands.localnode.model
    value = mainframe.commands.eventlog.count

    # Get access to the psu module command object available in third slot of the mainframe.
    modular_psu = cast("MPSU50_2STCommands", mainframe.get_module_commands_psu(slot=3))
    # Some examples demonstrating the usage of module level commands.
    # Get the psu model and version
    psu_model = modular_psu.model
    psu_version = modular_psu.version
    modular_psu.firmware.verify()

    # Some examples demonstrating the usage of channel level commands.
    # Set the measurement aperture in seconds
    modular_psu.psu[1].measure.count = 5
    # Enable the source output
    modular_psu.psu[2].source.output = 1
    # Set the offset value used for voltage measurements
    rel_value = modular_psu.psu[1].measure.rel.levelv
    # Create a reference to the default buffer
    my_buffer = modular_psu.psu[1].defbuffer1
    # Read the value in the specified reading buffer
    # Measure the voltage on channel 1 of the PSU
    voltage_value = modular_psu.psu[1].measure.v()
