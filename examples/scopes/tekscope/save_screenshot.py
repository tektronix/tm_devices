"""Save a screenshot on the device and copy it to the local machine/environment."""

from tm_devices import DeviceManager
from tm_devices.drivers import MSO6B

with DeviceManager(verbose=True) as dm:
    # Add a scope
    scope: MSO6B = dm.add_scope("192.168.1.5")

    # Send some commands
    scope.add_new_math("MATH1", "CH1")  # add MATH1 to CH1
    scope.turn_channel_on("CH2")  # turn on channel 2
    scope.set_and_check(":HORIZONTAL:SCALE", 100e-9)  # adjust horizontal scale

    # Save a screenshot as a timestamped file. This will create a screenshot on the device,
    # copy it to the current working directory on the local machine,
    # and then delete the screenshot file from the device.
    scope.save_screenshot()

    # Save a screenshot as "example.png". This will create a screenshot on the device,
    # copy it to the current working directory on the local machine,
    # and then delete the screenshot file from the device.
    scope.save_screenshot("example.png")

    # Save a screenshot as "example.jpg". This will create a screenshot on the device
    # using INVERTED colors in the "./device_folder" folder,
    # copy it to "./images/example.jpg" on the local machine,
    # but this time the screenshot file on the device will not be deleted.
    scope.save_screenshot(
        "example.jpg",
        colors="INVERTED",
        local_folder="./images",
        device_folder="./device_folder",
        keep_device_file=True,
    )
