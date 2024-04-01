"""2400 Series Current Sweep Example Script.

Description:
    In this application, a linear voltage sweep is
    configured to output voltage from 0 V to 0.53 V in
    56 steps. The instrument measures the resulting
    current from the solar cell during the sweep.
"""

from time import sleep

from tm_devices import DeviceManager
from tm_devices.drivers import SMU2450

with DeviceManager(verbose=False) as device_manager:
    inst: SMU2450 = device_manager.add_smu("192.168.1.4", alias="my2450")  # pyright: ignore[reportAssignmentType]

    # Reset the instrument, which also clears the buffer.
    inst.commands.reset()

    # Set up the source function.
    inst.commands.smu.source.func = inst.commands.smu.FUNC_DC_VOLTAGE
    inst.commands.smu.source.ilimit.level = 10e-3
    inst.commands.smu.source.level = 20
    inst.commands.smu.source.delay = 0.2

    # Set up measure function.
    inst.commands.smu.measure.func = inst.commands.smu.FUNC_DC_CURRENT
    inst.commands.smu.terminals = inst.commands.smu.TERMINALS_REAR
    inst.commands.smu.measure.autorange = inst.commands.smu.ON
    inst.commands.smu.measure.nplc = 1
    inst.commands.smu.source.highc = inst.commands.smu.OFF

    # Turn on the output and initiate readings.
    inst.commands.smu.source.output = inst.commands.smu.ON
    inst.commands.trigger.model.load_duration_loop(60)

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

    # Discharge the capacitor to 0 V and turn off the output.
    inst.commands.smu.source.level = 0
    sleep(2)
    inst.commands.smu.source.output = inst.commands.smu.OFF

    # Parse index and data into three columns.
    timestamp_data = []
    buffer1_data = []
    print("Rdg #", "Time (s)", "Current (A)")
    READING_COUNT = int(float(inst.commands.buffer_var["defbuffer1"].n))
    for x in range(1, READING_COUNT + 1):
        # Voltage readings are in defbuffer1.
        timestamp_data.append(  # pyright: ignore[reportUnknownMemberType]
            inst.commands.buffer_var["defbuffer1"].relativetimestamps[x]
        )
        buffer1_data.append(inst.commands.buffer_var["defbuffer1"].readings[x])  # pyright: ignore[reportUnknownMemberType]

        print(f"{x}, {timestamp_data[x-1]}, {buffer1_data[x-1]}")
