"""2400 Series Current Sweep Example Script.

Description:
    This sequence of TSP commands makes 100 low-resistance measurements
    by sourcing current and measuring resistance.

    In this example, the source current magnitude and limit voltage
    are set automatically. It uses remote commands to change the
    front-panel display to show the GRAPH swipe screen. This allows
    you to view numeric data at the top of the screen and graphic
    data at the bottom of the screen.

    After the code executes, the data is displayed in console.
"""

from time import sleep

from tm_devices import DeviceManager
from tm_devices.drivers import SMU2450

with DeviceManager() as device_manager:
    print(device_manager.get_available_devices())

    inst: SMU2450 = device_manager.add_smu("192.168.4.74", alias="my2450")  # pyright: ignore[reportGeneralTypeIssues]

    # Configure the Simple Loop trigger model template to make 100 readings.
    inst.commands.trigger.model.load_simple_loop(100)

    # Change the view on the front panel to the GRAPH swipe screen.
    inst.commands.display.changescreen(inst.commands.display.SCREEN_GRAPH_SWIPE)

    # Set to measure resistance, use 4-wire sense, and offset compensation.
    inst.commands.smu.measure.func = inst.commands.smu.FUNC_RESISTANCE
    inst.commands.smu.measure.sense = inst.commands.smu.SENSE_4WIRE
    inst.commands.smu.measure.offsetcompensation = inst.commands.smu.ON

    # Set bit 8 when event 2731 occurs
    # Clear bit 8 when event 2732 occurs
    # (See Operation Event Register section of manual for more info)
    BIT = 8
    inst.commands.status.operation.setmap(BIT, 2731, 2732)

    # Run trigger model and wait for it to complete
    inst.commands.trigger.model.initiate()

    is_sweeping = inst.commands.status.operation.condition
    while is_sweeping:
        operation_condition_register = int(inst.commands.status.operation.condition.rstrip())
        is_sweeping = operation_condition_register == 2**BIT
        sleep(0.1)

    # Turn off output
    inst.commands.smu.source.output = inst.commands.smu.OFF

    # Read the resistance and time values from defbuffer1.
    print("Resistance:\tTime:")

    # Print the data back to the Console in tabular format
    timestamp_data = []
    buffer1_data = []
    print("Time\tResistance")
    READING_COUNT = int(float(inst.commands.buffer_var["defbuffer1"].n))
    for x in range(1, READING_COUNT + 1):
        # Resistance readings are in defbuffer1.
        timestamp_data.append(  # type:ignore
            inst.commands.buffer_var["defbuffer1"].timestamps[x]
        )
        buffer1_data.append(inst.commands.buffer_var["defbuffer1"].readings[x])  # type:ignore

        print(f"{timestamp_data[x-1]}, {buffer1_data[x-1]}")
