"""2400 Series Current Sweep Example Script.

Description:
    The TSP code in this example sets the Model 2450
    to the source voltage function and measure current function.
    The voltage source is set to 1 V and the source
    limit is set to 460 mA. The voltage, current, and
    relative timestamp values are returned. Measurements
    are made until the voltage reaches the set level. During the
    test, these measurements are shown on the USER swipe screen at
    the bottom of the screen.
"""

from time import sleep

from tm_devices import DeviceManager
from tm_devices.drivers import SMU2450

with DeviceManager() as device_manager:
    print(device_manager.get_available_devices())

    inst: SMU2450 = device_manager.add_smu("192.168.4.74", alias="my2450")  # pyright: ignore[reportAssignmentType]

    # Clear the buffer.
    inst.commands.buffer_var["defbuffer1"].clear()

    # Source settings.
    inst.commands.smu.source.func = inst.commands.smu.FUNC_DC_VOLTAGE
    inst.commands.smu.source.offmode = inst.commands.smu.OFFMODE_HIGHZ
    inst.commands.smu.source.level = 1
    inst.commands.smu.source.range = 2
    inst.commands.smu.source.readback = inst.commands.smu.ON
    inst.commands.smu.source.ilimit.level = 460e-3

    # Measurement settings.
    inst.commands.smu.measure.func = inst.commands.smu.FUNC_DC_CURRENT
    inst.commands.smu.measure.range = 460e-3
    inst.commands.smu.measure.sense = inst.commands.smu.SENSE_4WIRE

    # Set the voltage limit for the battery to stop discharging.
    VOLTLIMIT = 1.0

    # Set the variable for the number of iterations.
    iteration = 1  # pylint:disable = invalid-name

    # Turn on the source output.
    inst.commands.smu.source.output = inst.commands.smu.ON

    # Change the display to the USER swipe screen.
    inst.commands.display.changescreen(inst.commands.display.SCREEN_USER_SWIPE)

    # Keep acquiring readings until the measured voltage reaches the voltage limit.
    while True:
        # Make a reading and get the current, voltage, and relative timestamp.
        curr = float(inst.commands.smu.measure.read("defbuffer1"))
        volt = float(inst.commands.buffer_var["defbuffer1"].sourcevalues[iteration])
        time = float(inst.commands.buffer_var["defbuffer1"].relativetimestamps[iteration])
        hours = time / 3600.00

        # Display the information on the front panel.
        inst.commands.display.settext("display.TEXT1", f"string.format('Voltage = %.4fV', {volt}")
        inst.commands.display.settext(
            "display.TEXT2", f"string.format('Current = %.2fA, Time = %.2fHrs', {curr}, {hours}"
        )

        if volt <= VOLTLIMIT:
            break  # Exit the loop if it has reached the limit

        iteration += 1
        sleep(10)

    # Turn the output off when the voltage limit is reached.
    inst.commands.smu.source.output = inst.commands.smu.OFF

    # Save the measurements to the USB flash drive.
    FileNumber = int(inst.commands.file.open("/usb1/TestData.csv", inst.commands.file.MODE_WRITE))
    inst.commands.file.write(FileNumber, "Current,Voltage,Seconds\n")

    # Print the measured values in a four-column format.
    print("\nIteration:\tCurrent:\tVoltage:\tTime:\n")
    readings = int(inst.commands.buffer_var["defbuffer1"].n)
    for i in range(readings):
        reading = inst.commands.buffer_var["defbuffer1"].readings[i]
        source_value = inst.commands.buffer_var["defbuffer1"].sourcevalues[i]
        timestamp = float(
            inst.commands.buffer_var["defbuffer1"].relativetimestamps.get[i]  # type: ignore
        )
        print(i, reading, source_value, timestamp)

        inst.commands.file.write(
            FileNumber, f"string.format('%g,%g, %g\r\n', {reading}, {source_value}, {timestamp}"
        )

    # Close the .csv file.
    inst.commands.file.close(FileNumber)
