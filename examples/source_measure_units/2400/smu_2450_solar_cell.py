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

with DeviceManager() as device_manager:
    print(device_manager.get_available_devices())

    inst: SMU2450 = device_manager.add_smu("192.168.4.74", alias="my2450")  # pyright: ignore[reportAssignmentType]

    # Define the number of points in the sweep.
    POINTS = 56

    # Reset the instrument and clear the buffer.
    inst.commands.reset()

    # Set the source and measure functions.
    inst.commands.smu.measure.func = inst.commands.smu.FUNC_DC_CURRENT
    inst.commands.smu.source.func = inst.commands.smu.FUNC_DC_VOLTAGE

    # Measurement settings.
    inst.commands.smu.terminals = inst.commands.smu.TERMINALS_FRONT
    inst.commands.smu.measure.sense = inst.commands.smu.SENSE_4WIRE
    inst.commands.smu.measure.autorange = inst.commands.smu.ON
    inst.commands.smu.measure.nplc = 1

    # Source settings.
    inst.commands.smu.source.highc = inst.commands.smu.OFF
    inst.commands.smu.source.range = 2
    inst.commands.smu.source.readback = inst.commands.smu.ON
    inst.commands.smu.source.ilimit.level = 1
    inst.commands.smu.source.sweeplinear("SolarCell", 0, 0.53, POINTS, 0.1)

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
        sleep(1)

    # Define initial values.
    isc = float(inst.commands.buffer_var["defbuffer1"].readings[1])
    imax = 0  # pylint:disable = invalid-name
    MIN_CURR = 0
    pmax = 0  # pylint:disable = invalid-name
    vmax = 0  # pylint:disable = invalid-name
    voc = 0  # pylint:disable = invalid-name

    for i in range(POINTS):
        current = float(inst.commands.buffer_var["defbuffer1"].readings[i + 1])
        voltage = float(inst.commands.buffer_var["defbuffer1"].sourcevalues[i + 1])
        power = voltage * current
        print("Voltage: ", voltage, "Current: ", current, "Power: ", power)

        if current > imax:
            imax = current
        if power > pmax:
            pmax = power
        if voltage > vmax:
            vmax = voltage

        if abs(current) < abs(MIN_CURR):
            voc = voltage

    imax = abs(imax)
    pmax = abs(pmax)

    print("Pmax: ", pmax, "Imax: ", imax, "Vmax: ", vmax, "Isc: ", isc)
