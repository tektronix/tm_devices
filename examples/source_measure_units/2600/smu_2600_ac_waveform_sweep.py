"""2600 Series AC Waveform Example Script.

Description:
    This example demonstrates how to output an AC Waveform with the Series 2600B
    System SourceMeter instruments. This example script shows how to configure
    the Series 2600B trigger model to output a waveform with consistent timing.
    At the conclusion of the sweeps the data is returned to the console in a
    format that is compatible for use in Microsoft Excel.

Equipment Needed:
    1x Series 2600B SourceMeter instrument

Converted to Python tm_devices script. DCA 4.12.23
"""

import math

from tm_devices import DeviceManager
from tm_devices.drivers import SMU2602B

RESOURCE_ID = "192.168.0.1"

# TEST PARAMETERS:
VRMS = 12
VPP = VRMS * 2**0.5
NUM_CYCLES = 2
FREQUENCY = 60
LIMIT_I = 100e-3
NPLC = 0.001
PTS_PER_CYCLE = int(7200 / FREQUENCY)  # This value MUST be an integer!
NUM_DATA_PTS = PTS_PER_CYCLE * NUM_CYCLES  # This value MUST be an integer!


def waveform_sweep(inst: SMU2602B) -> None:
    """Performs an AC Waveform Sweep on the Instrument.

    Note:
        RMS voltage is smaller than peak voltage.  RMS voltage must be set low
        enough that peak voltage fits within the maximum voltage source range
        of the SourceMeter instrument. Maximum frequency is approximately 1000 Hz
        depending on the quality of sine wave desired.

    Args:
        inst (SMU2602B): The instance of the python driver sending commands to the instrument.
    """
    # Aliases for more readability
    commands = inst.commands
    smua = inst.commands.smu["a"]

    # Configure SMU ranges
    smua.reset()
    smua.source.settling = smua.SETTLE_FAST_POLARITY
    smua.source.autorangev = smua.AUTORANGE_OFF
    smua.source.autorangei = smua.AUTORANGE_OFF
    smua.source.rangev = VPP
    smua.source.limiti = LIMIT_I

    smua.measure.autorangev = smua.AUTORANGE_OFF
    smua.measure.autorangei = smua.AUTORANGE_OFF
    smua.measure.autozero = smua.AUTOZERO_OFF
    smua.measure.rangei = LIMIT_I
    smua.measure.nplc = NPLC

    # Prepare reading buffers
    commands.buffer_var["smua.nvbuffer1"].clear()
    commands.buffer_var["smua.nvbuffer1"].collecttimestamps = 1
    commands.buffer_var["smua.nvbuffer2"].clear()
    commands.buffer_var["smua.nvbuffer2"].collecttimestamps = 1

    # Configure trigger Model
    # Timer 1 controls the time between source points
    commands.trigger.timer[1].delay = 1 / 7200
    commands.trigger.timer[1].passthrough = "true"
    commands.trigger.timer[1].stimulus = smua.trigger.ARMED_EVENT_ID
    commands.trigger.timer[1].count = NUM_DATA_PTS - 1

    # Create the source values list.
    inst.write("src_values = {}")
    for index in range(1, NUM_DATA_PTS + 1):
        value = VPP * math.sin(index * 2 * math.pi / PTS_PER_CYCLE)
        inst.write(f"src_values[{index}] = {value:.2e}")
    inst.write("smua.trigger.source.listv(src_values)")

    # Configure the SMU trigger model
    smua.trigger.source.limiti = LIMIT_I
    smua.trigger.measure.action = smua.ENABLE
    smua.trigger.measure.iv("smua.nvbuffer1", "smua.nvbuffer2")
    smua.trigger.endpulse.action = smua.SOURCE_HOLD
    smua.trigger.endsweep.action = smua.SOURCE_IDLE
    smua.trigger.count = NUM_DATA_PTS
    smua.trigger.arm.stimulus = 0
    smua.trigger.source.stimulus = commands.trigger.timer[1].EVENT_ID
    smua.trigger.measure.stimulus = 0
    smua.trigger.endpulse.stimulus = 0
    smua.trigger.source.action = smua.ENABLE

    # Begin the test
    smua.source.output = smua.OUTPUT_ON
    smua.trigger.initiate()

    # Wait for operation to complete
    inst.query("waitcomplete() print(1)")

    smua.source.output = smua.OUTPUT_OFF

    print("Timestamps", "Voltage", "Current", sep="\t")
    inst.print_buffers("smua.nvbuffer1.timestamps", "smua.nvbuffer2", "smua.nvbuffer1")


# RUN TEST
with DeviceManager(verbose=False) as DM:
    inst_driver: SMU2602B = DM.add_smu(RESOURCE_ID)  # pyright: ignore[reportAssignmentType]
    waveform_sweep(inst_driver)
