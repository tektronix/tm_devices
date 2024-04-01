"""Model 2460 Pulse Train Example Script.

Description:
    This example shows how to generate a current pulse train. In particular,
    this code generates 10 pulses with a magnitude of 6 A and a pulse width
    of 1 ms. The pulse period is 4 ms and the load that is used is 1 ohm.

Converted to Python tm_devices script. DCA 4.7.23
"""

import time

from tm_devices import DeviceManager
from tm_devices.drivers import SMU2460

RESOURCE_ID = "192.168.0.1"

# CONSTANTS
BIAS_LEVEL = 0
PULSE_LEVEL = 6
BIAS_WIDTH = 3e-3
PULSE_WIDTH = 1e-3
PERIOD = BIAS_WIDTH + PULSE_WIDTH
POINTS = 10
LIMIT = 7

with DeviceManager(verbose=True) as dm:
    inst: SMU2460 = dm.add_smu(RESOURCE_ID)  # pyright: ignore[reportAssignmentType]

    # Set to current source and set up source config list
    inst.commands.smu.source.configlist.create("OutputList")
    inst.commands.smu.source.func = inst.commands.smu.FUNC_DC_CURRENT
    inst.commands.smu.source.readback = inst.commands.smu.OFF

    # Set up measure commands
    inst.commands.smu.measure.func = inst.commands.smu.FUNC_DC_VOLTAGE
    inst.commands.smu.measure.nplc = 0.01
    inst.commands.smu.measure.autozero.once()

    inst.commands.smu.terminals = inst.commands.smu.TERMINALS_FRONT
    inst.commands.smu.measure.range = LIMIT
    inst.commands.smu.measure.sense = inst.commands.smu.SENSE_4WIRE

    LINEFREQ = float(inst.commands.localnode.linefreq)
    NPLC = float(inst.commands.smu.measure.nplc)
    MEASURE_DELAY = max(50e-6, PULSE_WIDTH - ((1 / LINEFREQ) * NPLC + 450e-6))

    # Set the source range large enough to fit both the bias and level.
    inst.commands.smu.source.range = max(abs(BIAS_LEVEL), abs(PULSE_LEVEL))
    inst.commands.smu.source.delay = 0
    inst.commands.smu.source.vlimit.level = LIMIT

    # Set to pulselevel (amplitude) and save to list
    inst.commands.smu.source.level = PULSE_LEVEL
    inst.commands.smu.source.configlist.store("OutputList")

    # Set to bisalevel and save to list
    inst.commands.smu.source.level = BIAS_LEVEL
    inst.commands.smu.source.configlist.store("OutputList")

    # Setup Timers
    # Use timer[1] to control the Period of the pulse train
    inst.commands.trigger.timer[1].reset()
    inst.commands.trigger.timer[1].start.generate = "trigger.ON"
    inst.commands.trigger.timer[1].delay = PERIOD
    inst.commands.trigger.timer[1].count = POINTS - 1

    # Use timer[2] to control the Pulse Width of the pulses
    inst.commands.trigger.timer[2].reset()
    inst.commands.trigger.timer[2].start.stimulus = "trigger.EVENT_TIMER1"
    inst.commands.trigger.timer[2].start.generate = "trigger.OFF"
    inst.commands.trigger.timer[2].delay = PULSE_WIDTH
    inst.commands.trigger.timer[2].count = 1
    inst.commands.trigger.timer[2].enable = "trigger.ON"

    # Trigger model setup
    inst.commands.trigger.model.setblock_trigger_block_buffer_clear(1)
    inst.commands.trigger.model.setblock_trigger_block_source_output(2, inst.commands.smu.ON)
    inst.commands.trigger.model.setblock_trigger_block_wait(3, "trigger.EVENT_TIMER1")
    inst.commands.trigger.model.setblock_trigger_block_config_recall(4, "OutputList")
    inst.commands.trigger.model.setblock_trigger_block_delay_constant(
        5,
        MEASURE_DELAY,  # type: ignore[arg-type]
    )
    inst.commands.trigger.model.setblock_trigger_block_measure_digitize(6)
    inst.commands.trigger.model.setblock_trigger_block_wait(7, "trigger.EVENT_TIMER2")
    inst.commands.trigger.model.setblock_trigger_block_config_next(8, "OutputList")
    inst.commands.trigger.model.setblock_trigger_block_branch_counter(9, POINTS, 3)  # type: ignore[arg-type]
    inst.commands.trigger.model.setblock_trigger_block_source_output(10, inst.commands.smu.OFF)

    # Start the trigger model
    inst.commands.buffer_var["defbuffer1"].clear()
    inst.commands.trigger.model.initiate()

    # Set the operation status bit 0 to high when the trigger model is active.
    # See Event Numbers in 2460 reference manual.
    inst.commands.status.operation.setmap(0, 2731, 2732)
    inst.commands.trigger.timer[1].enable = "trigger.ON"

    while True:  # This is needed to wait for the trigger model to complete
        time.sleep(0.5)
        if not int(inst.commands.status.operation.condition):
            break

    buffer_data = inst.get_buffers("defbuffer1")
    voltage = buffer_data["defbuffer1"]

    print("Voltage:")
    for value in voltage:
        print(value)
