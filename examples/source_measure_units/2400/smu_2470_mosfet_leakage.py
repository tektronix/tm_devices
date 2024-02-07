"""The following script performs a MOSFET leakage measurement.

It does this by sourcing 600 V and measuring the resulting leakage current. The Duration Loop
trigger model template applies the voltage for 60 seconds and makes measurements at 200 ms
intervals.
"""
from typing import List

from tm_devices import DeviceManager
from tm_devices.drivers import SMU2470

with DeviceManager(verbose=False) as device_manager:
    smu2470: SMU2470 = device_manager.add_smu("TCPIP::0.0.0.0::inst0::INSTR", alias="my2470")  # pyright: ignore[reportAssignmentType]

    # Reset the instrument, which also clears the buffer.
    smu2470.commands.reset()
    # Set up the source function.
    smu2470.commands.smu.source.func = smu2470.commands.smu.FUNC_DC_VOLTAGE
    smu2470.commands.smu.source.ilimit.level = 10e-3
    smu2470.commands.smu.source.level = 600
    # Set up measure function.
    smu2470.commands.smu.measure.func = smu2470.commands.smu.FUNC_DC_CURRENT
    smu2470.commands.smu.terminals = smu2470.commands.smu.TERMINALS_REAR
    smu2470.commands.smu.measure.autorange = smu2470.commands.smu.ON
    smu2470.commands.smu.measure.nplc = 1
    # Turn on the output and initiate readings.
    smu2470.commands.trigger.model.load_duration_loop(60, 0.2)

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
    n = range(1, int(defbuffer1.n))
    tmst: List[float] = []
    curr: List[float] = []
    # Parse index and data into three columns.
    for cnt in n:
        tmst.append(float(defbuffer1.relativetimestamps[cnt]))
        curr.append(float(defbuffer1.readings[cnt]))
    print("Rdg #\tTime (s)\tCurrent (A)")
    for cnt in n:
        print(f"{cnt}\t{tmst[cnt-1]:.6f}\t{curr[cnt-1]:+e}")
