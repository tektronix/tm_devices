"""The following script makes insulation resistance measurements.

It does this by sourcing 300 V and measuring the resistance. The Simple Loop trigger model template
is used to make 10 measurements at 100 ms intervals.
"""
from typing import List

from tm_devices import DeviceManager
from tm_devices.drivers import SMU2470

with DeviceManager(verbose=False) as device_manager:
    smu2470: SMU2470 = device_manager.add_smu(  # pyright: ignore[reportAssignmentType]
        "TCPIP::0.0.0.0::inst0::INSTR", alias="my2470"
    )  # 192.168.0.2

    # Reset the instrument
    smu2470.commands.reset()
    # Set up the source function.
    smu2470.commands.smu.source.func = smu2470.commands.smu.FUNC_DC_VOLTAGE
    smu2470.commands.smu.source.ilimit.level = 1e-3
    smu2470.commands.smu.source.level = 300
    # Set up the measure function
    smu2470.commands.smu.measure.func = smu2470.commands.smu.FUNC_DC_CURRENT
    smu2470.commands.smu.measure.unit = smu2470.commands.smu.UNIT_OHM
    smu2470.commands.smu.terminals = smu2470.commands.smu.TERMINALS_REAR
    smu2470.commands.smu.measure.autorange = smu2470.commands.smu.ON
    smu2470.commands.smu.measure.nplc = 1
    # Turn on the source output and take readings.
    smu2470.commands.trigger.model.load_simple_loop(10, 0.1)
    smu2470.commands.smu.source.output = smu2470.commands.smu.ON

    # Set bit 8 when event 2731 occurs
    # Clear bit 8 when event 2732 occurs
    # (See Operation Event Register section of manual for more info)
    BIT = 8
    smu2470.commands.status.operation.setmap(BIT, 2731, 2732)
    is_sweeping = True  # pylint: disable=invalid-name

    smu2470.commands.trigger.model.initiate()
    # Wait for the measurements to complete. waitcomplete()
    _ = smu2470.commands.status.operation.condition  # throw away first read of status byte

    while is_sweeping:
        operation_condition_register = int(smu2470.commands.status.operation.condition.rstrip())
        is_sweeping = operation_condition_register == 2**BIT
    # Turn off the output.
    smu2470.commands.smu.source.output = smu2470.commands.smu.OFF

    defbuffer1 = smu2470.commands.buffer_var["defbuffer1"]
    num = range(1, int(defbuffer1.n))
    tmst: List[float] = []
    res: List[float] = []
    # Parse index and the data into three columns.
    for cnt in num:
        tmst.append(float(defbuffer1.relativetimestamps[cnt]))
        res.append(float(defbuffer1.readings[cnt]))
    print("Rdg #\tTime (s)\tResistance (Ohm)")
    for cnt in num:
        print(f"{cnt}\t{tmst[cnt-1]:f}\t{res[cnt-1]:+e}")
