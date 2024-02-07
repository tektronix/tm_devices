"""This script creates a pulsed voltage sweep and porduces a trigger on an I/O pin when finished.

You can use this trigger to notify other instruments that the 2461 completed its pulse sweep.

The Model 2461 voltage source outputs a pulse sweep from 1V to 5V in 101 steps as the Model 2461
ammeter measures the resulting current through the DUT. The application is set up to make 10ms
pulses with 90ms of off time; 45ms before each pulse and 45ms after each pulse Once the measurements
are made, the output is turned off.

The Model 2461's pulse commands are utilized to generate the config lists used by the trigger model
for pulsing, but the trigger model is replaced with one that produces the output trigger. The
function pulse_delay_cal is used to compute the length of the constant delay block used to set the
width of each pulse in the sweep. The computation is normally done by the instrument when the pulse
commands build the trigger model, but the script must do it because the strandard trigger model is
being erased and replaced for this example. The current and voltage readings are printed to the
Instrument Console. You can copy and paste these readings into a spreadsheet for further analysis.
"""

# Press the green button in the gutter to run the script.
from time import sleep
from typing import List

from tm_devices import DeviceManager
from tm_devices.drivers import SMU2461


# Function to calculate the pulse width delay block's time
def pulse_delay_calc(pulse_width: str) -> float:
    """Calculates the pulse delay.

    Args:
        pulse_width : The time the pulse is high
    """
    # Gather status information from the the SMU
    nplc = float(smu2461.commands.smu.measure.nplc)
    line_freq = int(smu2461.commands.localnode.linefreq)
    sreadback = smu2461.commands.smu.source.readback
    auto_zero = smu2461.commands.smu.measure.autozero.enable
    filter_enable = smu2461.commands.smu.measure.filter.enable
    filter_type = smu2461.commands.smu.measure.filter.type
    filter_count = int(smu2461.commands.smu.measure.filter.count)
    reading_count: int = 1

    if (
        filter_enable == smu2461.commands.smu.ON
        and filter_type == smu2461.commands.smu.FILTER_REPEAT_AVG
    ):
        reading_count = (
            reading_count + filter_count - 1
        )  # Account for the number of repeat filter readings
    else:
        filter_count = 1

    if auto_zero == smu2461.commands.smu.ON and sreadback == smu2461.commands.smu.OFF:
        reading_count *= 3  # The SMU takes 3 readings if autozero is on
    elif auto_zero == smu2461.commands.smu.ON and sreadback == smu2461.commands.smu.ON:
        reading_count *= 4  # The SMU takes 4 readings if autozero and source readback are on
    elif auto_zero == smu2461.commands.smu.OFF and sreadback == smu2461.commands.smu.ON:
        reading_count *= 2  # The SMU takes 2 readings if source readback is on

    # The delays in the meas_time calculation come from:
    # 200us for reading post processing EVERY reading
    # repeat average filtering shaves 50us off of this time for every set of readings
    meas_time = (
        (1 / line_freq) * nplc * reading_count + 200e-6 * reading_count - filter_count * 50e-6
    )

    # Calculate the(not quite finalized) final_delay by subtracting
    # calculated measure time and 80us of pulse output block overhead
    final_delay = float(pulse_width) - meas_time - 80e-6

    if sreadback == smu2461.commands.smu.ON:
        final_delay -= (
            0.41e-3 * filter_count
        )  # Source readback takes an extra 410us for every set of readings

    if auto_zero == smu2461.commands.smu.ON:
        final_delay -= (
            1.28e-3 * filter_count
        )  # Autozero takes an extra 1.28ms for every set of readings

    if final_delay > 0:
        return final_delay  # Pass the final delay as an output
    print("Measure time too long!")  # The measure time exceeds the desired pulse width
    return 0


with DeviceManager() as device_manager:
    print(device_manager.get_available_devices())

    smu2461: SMU2461 = device_manager.add_smu(  # pyright: ignore[reportAssignmentType]
        "TCPIP::0.0.0.0::inst0::INSTR", alias="my2461"
    )  # 192.168.0.2

    # Reset the instrument
    smu2461.commands.reset()
    smu2461.commands.smu.source.func = smu2461.commands.smu.FUNC_DC_VOLTAGE
    smu2461.commands.smu.source.range = 7
    smu2461.commands.smu.measure.func = smu2461.commands.smu.FUNC_DC_CURRENT
    smu2461.commands.smu.measure.sense = smu2461.commands.smu.SENSE_2WIRE
    smu2461.commands.smu.measure.autorange = smu2461.commands.smu.ON
    # The instrument will select a best fixed range to fit the pulses

    smu2461.commands.smu.source.readback = smu2461.commands.smu.ON
    smu2461.commands.smu.measure.autozero.enable = smu2461.commands.smu.OFF
    smu2461.commands.smu.measure.nplc = 0.01
    # NPLC can be increased to improve measurement accuracy.
    # However, it has to remain small enough to fit the measurement
    # within the width of the settled part of the pulse.

    # Set up the pulse parameters
    CONFIG_LIST_NAME = "myPulseSweep"
    BIAS_LEVEL = "0"  # Bias level between pulses
    START = 1  # Sweep start point
    STOP = 5  # Sweep end point
    POINTS = 101  # 101 points in the sweep
    PULSE_WIDTH = "10e-3"  # Pulse width
    MEASURE_ENABLE = smu2461.commands.smu.ON  # Enables measurements on each pulse
    BUFFER_NAME = "defbuffer1"  # Buffer to save results
    PULSE_DELAY = 45e-3  # Delay before each pulse
    OFF_TIME = "45e-3"  # Off time after each pulse
    COUNT = 1  # Number of times to repeat the pulse sweep
    X_BIAS_LIMIT = "1e-3"  # Current limit between pulses
    X_PULSE_LIMIT = "100e-3"  # Current limit during pulses
    FAIL_ABORT = smu2461.commands.smu.OFF  # Abort pulse sweep if current limit is hit
    DUAL = smu2461.commands.smu.OFF  # Only sweep from 1V to 5V, but not back down again

    # 2461 Pulse Command
    smu2461.commands.smu.source.pulsesweeplinear(
        CONFIG_LIST_NAME,
        BIAS_LEVEL,
        START,
        STOP,
        POINTS,
        str(PULSE_WIDTH),
        MEASURE_ENABLE,
        BUFFER_NAME,
        PULSE_DELAY,
        OFF_TIME,
        COUNT,
        X_BIAS_LIMIT,
        X_PULSE_LIMIT,
        FAIL_ABORT,
        DUAL,
    )
    # Configure tsplink triggering

    smu2461.commands.digio.line[1].mode = smu2461.commands.digio.MODE_TRIGGER_OUT
    smu2461.commands.trigger.digout[1].logic = "trigger.LOGIC_NEGATIVE"
    smu2461.commands.trigger.digout[1].stimulus = smu2461.commands.trigger.EVENT_NOTIFYN[:-1] + "1"

    # Configure the trigger model
    smu2461.commands.trigger.model.load_empty()
    smu2461.commands.trigger.model.setblock_trigger_block_buffer_clear(1, BUFFER_NAME)
    smu2461.commands.trigger.model.setblock_trigger_block_config_recall(
        2, "MeasmyPulseSweep", 1, CONFIG_LIST_NAME, 1
    )
    smu2461.commands.trigger.model.setblock_trigger_block_source_output(3, smu2461.commands.smu.ON)
    smu2461.commands.trigger.model.setblock_trigger_block_branch_always(4, "6")
    smu2461.commands.trigger.model.setblock_trigger_block_config_next(5, CONFIG_LIST_NAME)
    smu2461.commands.trigger.model.setblock_trigger_block_delay_constant(6, str(PULSE_DELAY))
    smu2461.commands.trigger.model.setblock_trigger_block_source_output(7, smu2461.commands.smu.ON)
    smu2461.commands.trigger.model.setblock_trigger_block_delay_constant(
        8, str(pulse_delay_calc(PULSE_WIDTH))
    )
    smu2461.commands.trigger.model.setblock_trigger_block_measure_digitize(9, BUFFER_NAME)
    smu2461.commands.trigger.model.setblock_trigger_block_source_pulse_output(
        10, smu2461.commands.smu.OFF
    )
    smu2461.commands.trigger.model.setblock_trigger_block_delay_constant(11, OFF_TIME)
    smu2461.commands.trigger.model.setblock_trigger_block_branch_counter(12, POINTS, "5")
    smu2461.commands.trigger.model.setblock_trigger_block_source_output(
        13, smu2461.commands.smu.OFF
    )
    smu2461.commands.trigger.model.setblock_trigger_block_notify(
        14, smu2461.commands.trigger.EVENT_NOTIFYN[:-1] + "1"
    )

    # Set bit 8 when event 2731 occurs
    # Clear bit 8 when event 2732 occurs
    # (See Operation Event Register section of manual for more info)
    BIT = 8
    smu2461.commands.status.operation.setmap(BIT, 2731, 2732)
    is_sweeping = True  # pylint: disable=invalid-name
    wait = 1  # pylint: disable=invalid-name
    smu2461.commands.trigger.model.initiate()
    # Wait for the measurements to complete. waitcomplete()
    _ = smu2461.commands.status.operation.condition  # throw away first read of status byte

    while is_sweeping:
        sleep(wait := wait * 1.1)
        operation_condition_register = int(smu2461.commands.status.operation.condition.rstrip())
        is_sweeping = operation_condition_register == 2**BIT

    defbuffer1 = smu2461.commands.buffer_var["defbuffer1"]
    RDG_CNT = int(float(defbuffer1.n))
    curr: List[float] = []
    volt: List[float] = []
    # Print Results
    if not RDG_CNT:
        print("Buffer is empty\n")
    else:
        for cnt in range(1, RDG_CNT + 1):
            curr.append(float(defbuffer1.sourcevalues[cnt]))
            volt.append(float(defbuffer1.readings[cnt]))
        print("Rdg\tCurrent\t\tVoltage")
        for cnt in range(1, RDG_CNT + 1):
            print(f"{cnt}\t{curr[cnt-1]:+e}\t{volt[cnt-1]:+e}")
