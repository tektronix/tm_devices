"""Model 2460 Solar Panel Sweep Example Script.

Description:
    This example demonstrates how to generate an I-V sweep on a solar panel.
    In this particular example the voltage is swept from 0V to 20V and the resulting current
    is measured.  The maximum power, maximum current, maximum voltage, short circuit current,
    and open circuit voltage are calculated and displayed in the console.

Converted to Python tm_devices script. DCA 4.7.23
"""
import time

from tm_devices import DeviceManager
from tm_devices.drivers import SMU2460

RESOURCE_ID = "192.168.0.1"

# CONSTANTS
NPLC = 1
SOURCE_RANGE = 20
ILIMIT_LEVEL = 4
START = 0
STOP = 20
POINTS = 115
S_DELAY = 0.05

with DeviceManager(verbose=False) as dm:
    inst: SMU2460 = dm.add_smu(RESOURCE_ID)  # pyright: ignore[reportAssignmentType]

    # Reset the Model 2460 and clear its buffer.
    inst.commands.reset()

    # Set the source and measure functions.
    inst.commands.smu.measure.func = inst.commands.smu.FUNC_DC_CURRENT
    inst.commands.smu.source.func = inst.commands.smu.FUNC_DC_VOLTAGE

    # Configure measurement settings.
    inst.commands.smu.terminals = inst.commands.smu.TERMINALS_FRONT
    inst.commands.smu.measure.sense = inst.commands.smu.SENSE_4WIRE
    inst.commands.smu.measure.autorange = inst.commands.smu.ON
    inst.commands.smu.measure.nplc = NPLC

    # Configure source settings.
    inst.commands.smu.source.highc = inst.commands.smu.OFF
    inst.commands.smu.source.range = SOURCE_RANGE
    inst.commands.smu.source.readback = inst.commands.smu.ON
    inst.commands.smu.source.ilimit.level = ILIMIT_LEVEL
    inst.commands.smu.source.sweeplinear("SolarCell", START, STOP, POINTS, S_DELAY)

    # Set the operation status bit 0 to high when the trigger model is active.
    # See Event Numbers in 2460 reference manual.
    inst.commands.status.operation.setmap(0, 2731, 2732)
    inst.commands.trigger.model.initiate()

    while True:  # This is needed to wait for the trigger model to complete
        time.sleep(0.5)
        if not int(inst.commands.status.operation.condition):
            break

    # Get the data from the buffers:
    buffer_data = inst.get_buffers("defbuffer1.sourcevalues", "defbuffer1")
    voltage = buffer_data["defbuffer1.sourcevalues"]
    current = buffer_data["defbuffer1"]

    # Define the initial values.
    isc = current[0]
    min_curr = current[0]
    imax = current[0]
    voc = voltage[0]
    vmax = voltage[0]
    pmax = voltage[0] * current[0]

    # Calculate values and print data.
    print("Voltage:", "Current:", "Power:")
    for idx, _ in enumerate(voltage):
        print(voltage[idx], current[idx], voltage[idx] * current[idx])

        if voltage[idx] * current[idx] < pmax:
            pmax = voltage[idx] * current[idx]
            imax = current[idx]
            vmax = voltage[idx]

        if abs(current[idx]) < abs(min_curr):
            voc = voltage[idx]

    pmax = abs(pmax)
    imax = abs(imax)
    print(f"PMAX: {pmax} W", f"IMAX: {imax} A", f"VMAX: {vmax} V", f"ISC: {isc} A", f"VOC: {voc} V")
