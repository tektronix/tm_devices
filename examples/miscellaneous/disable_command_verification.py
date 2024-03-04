"""An example showing how to disable the verification portion of the ``.set_and_check()`` method."""

from tm_devices import DeviceManager
from tm_devices.drivers import MSO5, SMU2601B

with DeviceManager(verbose=True) as dm:
    # Add some devices
    scope: MSO5 = dm.add_scope("192.168.0.1")  # pyright: ignore[reportAssignmentType]
    smu: SMU2601B = dm.add_smu("192.168.0.2")  # pyright: ignore[reportAssignmentType]

    #
    # Set some values and use verification to verify they were set properly.
    #
    # using set_and_check
    scope.set_and_check(":HORIZONTAL:SCALE", 100e-9)
    # using force_verify on the auto-generated commands
    scope.commands.horizontal.scale.write(200e-9, verify=True)
    # using the command verification context manager on the auto-generated commands
    with scope.command_verification():
        scope.commands.horizontal.scale.write(50e-9)
    # using set_and_check
    smu.set_and_check("beeper.enable", 1)
    # using the command verification context manager on the auto-generated commands
    with smu.command_verification():
        smu.commands.beeper.enable = 0

    #
    # Disable command verification.
    #
    # Disable just for the scope
    scope.enable_verification = False
    # Disable command verification for all devices
    dm.disable_device_command_checking()

    #
    # Set some values, but now **no verification** will happen in any of these method calls.
    #
    # using set_and_check
    scope.set_and_check(":HORIZONTAL:SCALE", 100e-9)
    # using force_verify on the auto-generated commands
    scope.commands.horizontal.scale.write(200e-9, verify=True)
    # using the command verification context manager on the auto-generated commands
    with scope.command_verification():
        scope.commands.horizontal.scale.write(50e-9)
    # using set_and_check
    smu.set_and_check("beeper.enable", 1)
    # using the command verification context manager on the auto-generated commands
    with smu.command_verification():
        smu.commands.beeper.enable = 0
