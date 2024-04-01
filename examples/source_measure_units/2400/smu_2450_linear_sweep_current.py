"""2400 Series Current Sweep Example Script.

Description:
    This Model 2450 example shows you how to sweep the
    test current and measure the resulting voltage drop on a low
    resistance device.

The Model 2450 current source outputs a sweep from -100 mA to 100 mA in 101 steps as the Model 2450
voltmete measures the resulting voltage drop across the resistor.  This application is set up to
take 101 readings with a 100 ms interval time.  Once the measurements are made, the output is turned
off. The current and voltage readings are printed to the Instrument Console.  You can copy and paste
these readings into a spreadsheet for further analysis and graphing.
"""

from tm_devices import DeviceManager
from tm_devices.drivers import SMU2450

with DeviceManager() as device_manager:
    smu2450: SMU2450 = device_manager.add_smu(  # pyright: ignore[reportAssignmentType]
        "USB0::0x05E6::0x2450::01419969::INSTR", alias="my2450"
    )

    NPLC = 1.0

    # Reset the SMU
    smu2450.commands.reset()
    smu2450.commands.smu.reset()
    smu2450.commands.buffer_var["defbuffer1"].clear()

    # Measure Settings
    smu2450.commands.smu.measure.func = smu2450.commands.smu.FUNC_DC_VOLTAGE
    smu2450.commands.smu.measure.autorange = smu2450.commands.smu.measure.autorange
    smu2450.commands.smu.measure.nplc = NPLC
    smu2450.commands.smu.measure.sense = smu2450.commands.smu.SENSE_4WIRE

    # Source Settings
    smu2450.commands.smu.source.func = smu2450.commands.smu.FUNC_DC_CURRENT
    smu2450.commands.smu.source.vlimit.level = 50
    smu2450.commands.smu.source.delay = 0.1
    smu2450.commands.smu.source.sweeplinear("LowR", 10e-3, 50e-3, 4)  # DUT: 560ohm resistor

    # set bit 8 when event 2731 occurs
    # clear bit 8 when event 2732 occurs
    # (see Operation Event Register section of manual)
    BIT = 8
    smu2450.commands.status.operation.setmap(BIT, 2731, 2732)

    # Run trigger model and wait for it to complete
    smu2450.commands.trigger.model.initiate()
    _ = smu2450.commands.status.operation.condition  # throw away first read of status byte

    is_sweeping = int(smu2450.commands.status.operation.condition.rstrip())
    while is_sweeping:
        operation_condition_register = int(smu2450.commands.status.operation.condition.rstrip())
        is_sweeping = operation_condition_register == 2**BIT

    smu2450.commands.smu.source.output = smu2450.commands.smu.OFF

    # Print the data back to the Console in tabular format
    timestamp_data = []
    buffer1_data = []
    buffer2_data = []
    print("Time\tVoltage\tCurrent")
    READING_COUNT = int(float(smu2450.commands.buffer_var["defbuffer1"].n))
    for x in range(1, READING_COUNT + 1):
        # Voltage readings are in defbuffer1.
        timestamp_data.append(  # pyright: ignore[reportUnknownMemberType]
            smu2450.commands.buffer_var["defbuffer1"].timestamps[x]
        )
        buffer1_data.append(smu2450.commands.buffer_var["defbuffer1"].readings[x])  # pyright: ignore[reportUnknownMemberType]

        print(f"{timestamp_data[x-1]}, {buffer1_data[x-1]}")
