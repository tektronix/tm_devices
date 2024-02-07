"""2651A Fast ADC Usage Example Script.

Description:
    This script is designed to output pulses and
    capture     both the current and the voltage of the pulse using
    the fast ADC of the Model 2651A High Power System SourceMeter
    instrument.

Equipment Needed:
    1x 2651A High Power System SourceMeter instrument

Converted to Python tm_devices script. DCA 4.12.23
"""
from datetime import datetime

from dateutil.tz import tzlocal

from tm_devices import DeviceManager
from tm_devices.drivers import SMU2651A

TODAY_DATE = datetime.now(tz=tzlocal()).date()
RESOURCE_ID = "192.168.0.1"
V_FILENAME = "CapturePulseV_" + str(TODAY_DATE) + ".csv"
I_FILENAME = "CapturePulseI_" + str(TODAY_DATE) + ".csv"

# TEST CONSTANTS
NUM_PULSES = 5
PULSE_LEVEL = 5
PULSE_WIDTH = 300e-6
PULSE_LIMIT = 50
BIAS_LEVEL = 0
DC_LIMIT = 5
MEASURE_INTERVAL = 1e-6


def capture_pulse_i(inst: SMU2651A) -> None:
    """Uses fast ADC to capture current pulses at 1% duty cycle.

    Args:
        inst (SMU2651A): The python driver for the instrument under test.
    """
    # Aliases for redability
    commands = inst.commands
    smua = inst.commands.smu["a"]

    # Configure the SMU
    commands.reset()
    smua.reset()
    smua.source.func = smua.OUTPUT_DCAMPS
    smua.sense = smua.SENSE_REMOTE
    smua.source.rangei = PULSE_LEVEL
    smua.source.leveli = BIAS_LEVEL
    smua.source.limitv = DC_LIMIT
    smua.measure.autozero = smua.AUTOZERO_ONCE

    # Use a measure range that is as large as the biggest
    # possible pulse
    smua.measure.rangev = PULSE_LIMIT
    smua.measure.rangei = PULSE_LEVEL

    # Select the fast ADC for measurements
    smua.measure.adc = "smua.ADC_FAST"

    # Set the time between measurements.  1us is the smallest
    smua.measure.interval = MEASURE_INTERVAL

    # Set the measure count to be 1.25 times the width of the pulse
    # to ensure we capture the entire pulse plus falling edge.
    smua.measure.count = PULSE_WIDTH / MEASURE_INTERVAL * 1.25

    # Prepare the reading buffers
    commands.buffer_var["smua.nvbuffer1"].clear()
    commands.buffer_var["smua.nvbuffer1"].collecttimestamps = 1
    commands.buffer_var["smua.nvbuffer1"].collectsourcevalues = 0
    commands.buffer_var["smua.nvbuffer2"].clear()
    commands.buffer_var["smua.nvbuffer2"].collecttimestamps = 1
    commands.buffer_var["smua.nvbuffer2"].collectsourcevalues = 0
    # Can't use source values with async measurements

    # # Configure the Pulsed Sweep setup
    # Timer 1 controls the pulse period
    commands.trigger.timer[1].count = NUM_PULSES - 1
    # 1% Duty Cycle
    commands.trigger.timer[1].delay = PULSE_WIDTH / 0.01
    commands.trigger.timer[1].passthrough = "true"
    commands.trigger.timer[1].stimulus = smua.trigger.ARMED_EVENT_ID

    # Timer 2 controls the pulse width
    commands.trigger.timer[2].count = 1
    commands.trigger.timer[2].delay = PULSE_WIDTH - 3e-6
    commands.trigger.timer[2].passthrough = "false"
    commands.trigger.timer[2].stimulus = smua.trigger.SOURCE_COMPLETE_EVENT_ID

    # Configure SMU Trigger Model for Sweep/Pulse Output
    # Pulses will all be the same level so set start and stop to
    # the same value and the number of points in the sweep to 2
    smua.trigger.source.lineari(PULSE_LEVEL, PULSE_LEVEL, 2)
    smua.trigger.source.limitv = PULSE_LIMIT
    smua.trigger.measure.action = smua.ASYNC
    # We want to start the measurements before the source action takes
    # place so we must configure the ADC to operate asynchronously of
    # the rest of the SMU trigger model actions

    # Measure I and V during the pulse
    smua.trigger.measure.iv("smua.nvbuffer1", "smua.nvbuffer2")

    # Return the output to the bias level at the end of the pulse
    smua.trigger.endpulse.action = smua.SOURCE_IDLE
    smua.trigger.endsweep.action = smua.SOURCE_IDLE
    smua.trigger.count = NUM_PULSES
    smua.trigger.arm.stimulus = 0
    smua.trigger.source.stimulus = commands.trigger.timer[1].EVENT_ID
    smua.trigger.measure.stimulus = commands.trigger.timer[1].EVENT_ID
    smua.trigger.endpulse.stimulus = commands.trigger.timer[2].EVENT_ID
    smua.trigger.source.action = smua.ENABLE

    smua.source.output = 1
    smua.trigger.initiate()
    inst.query(
        "waitcomplete() print(1)"
    )  # This is necessary to wait for the trigger model to complete fully

    smua.source.output = 0

    inst.write_buffers(I_FILENAME, "smua.nvbuffer1.timestamps", "smua.nvbuffer2", "smua.nvbuffer1")


def capture_pulse_v(inst: SMU2651A) -> None:
    """Uses fast ADC to capture voltage pulses at 1% duty cycle.

    Args:
        inst (SMU2651A): The python driver for the instrument under test.
    """
    # Aliases for readability
    commands = inst.commands
    smua = inst.commands.smu["a"]

    # Configure the SMU
    commands.reset()
    smua.reset()
    smua.source.func = smua.OUTPUT_DCVOLTS
    smua.sense = smua.SENSE_REMOTE
    smua.source.rangev = PULSE_LEVEL
    smua.source.levelv = BIAS_LEVEL
    smua.source.limiti = DC_LIMIT
    smua.measure.autozero = smua.AUTOZERO_ONCE

    # Use a measure range that is as large as the biggest possible pulse
    smua.measure.rangei = PULSE_LIMIT
    smua.measure.rangev = PULSE_LEVEL

    # Select the fast ADC for measurements
    smua.measure.adc = "smua.ADC_FAST"

    # Set the time between measurements.  1us is the smallest
    smua.measure.interval = MEASURE_INTERVAL

    # Set the measure count to be 1.25 times the width of the pulse
    # to ensure we capture the entire pulse plus falling edge.
    smua.measure.count = PULSE_WIDTH / MEASURE_INTERVAL * 1.25

    # Prepare the reading buffers
    commands.buffer_var["smua.nvbuffer1"].clear()
    commands.buffer_var["smua.nvbuffer1"].collecttimestamps = 1
    commands.buffer_var["smua.nvbuffer1"].collectsourcevalues = 0
    commands.buffer_var["smua.nvbuffer2"].clear()
    commands.buffer_var["smua.nvbuffer2"].collecttimestamps = 1
    commands.buffer_var["smua.nvbuffer2"].collectsourcevalues = 0
    # Can't use source values with async measurements

    # Configure the Pulsed Sweep setup

    # Timer 1 controls the pulse period
    commands.trigger.timer[1].count = NUM_PULSES - 1
    # 1% Duty Cycle
    commands.trigger.timer[1].delay = PULSE_WIDTH / 0.01
    commands.trigger.timer[1].passthrough = "true"
    commands.trigger.timer[1].stimulus = smua.trigger.ARMED_EVENT_ID

    # Timer 2 controls the pulse width
    commands.trigger.timer[2].count = 1
    commands.trigger.timer[2].delay = PULSE_WIDTH - 3e-6
    commands.trigger.timer[2].passthrough = "false"
    commands.trigger.timer[2].stimulus = smua.trigger.SOURCE_COMPLETE_EVENT_ID

    # Configure SMU Trigger Model for Sweep/Pulse Output

    # Pulses will all be the same level so set start and stop to
    # the same value and the number of points in the sweep to 2
    smua.trigger.source.linearv(PULSE_LEVEL, PULSE_LEVEL, 2)
    smua.trigger.source.limiti = PULSE_LIMIT
    smua.trigger.measure.action = smua.ASYNC
    # We want to start the measurements before the source action takes
    # place so we must configure the ADC to operate asynchronously of
    # the rest of the SMU trigger model actions

    # Measure I and V during the pulse
    smua.trigger.measure.iv("smua.nvbuffer1", "smua.nvbuffer2")

    # Return the output to the bias level at the end of the pulse/sweep
    smua.trigger.endpulse.action = smua.SOURCE_IDLE
    smua.trigger.endsweep.action = smua.SOURCE_IDLE
    smua.trigger.count = NUM_PULSES
    smua.trigger.arm.stimulus = 0
    smua.trigger.source.stimulus = commands.trigger.timer[1].EVENT_ID
    smua.trigger.measure.stimulus = commands.trigger.timer[1].EVENT_ID
    smua.trigger.endpulse.stimulus = commands.trigger.timer[2].EVENT_ID
    smua.trigger.source.action = smua.ENABLE

    smua.source.output = 1
    smua.trigger.initiate()
    inst.query(
        "waitcomplete() print(1)"
    )  # This is necessary to wait for the trigger model to complete fully

    smua.source.output = 0

    inst.write_buffers(V_FILENAME, "smua.nvbuffer1.timestamps", "smua.nvbuffer2", "smua.nvbuffer1")


# RUN TEST
with DeviceManager() as DM:
    inst_driver: SMU2651A = DM.add_smu(RESOURCE_ID)  # pyright: ignore[reportAssignmentType]

    capture_pulse_i(inst_driver)
    capture_pulse_v(inst_driver)
