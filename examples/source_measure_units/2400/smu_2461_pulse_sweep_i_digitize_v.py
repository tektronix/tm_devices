"""This Model 2461 example shows you how to set up a pulsed current sweep.

It starts at -10mA and stop at 10mA The Model 2461 current source creates 201 pulses and is
constantly taking digitizer readings at a rate of 500,000 samples per second. The application is set
up to make 500us pulses with 500us of off time after each pulse.

The Model 2461's pulse commands are used to generate the trigger model necessary for pulsing. All of
the source and measure settings are configured before the pulse command
(smu.source.pulsesweeplinear) is sent to the instrument. The pulse command accepts a lot of
arguments so the the arguments are stored in variables to make them easier to read.
"""

from typing import cast, List

from tm_devices import DeviceManager
from tm_devices.drivers import SMU2461

with DeviceManager() as device_manager:
    print(device_manager.get_available_devices())

    smu2461: SMU2461 = cast(
        SMU2461, device_manager.add_smu("TCPIP::0.0.0.0::inst0::INSTR", alias="my2461")
    )  # 192.168.0.2

    # Reset the instrument
    smu2461.commands.reset()

    # Source settings
    smu2461.commands.smu.source.func = smu2461.commands.smu.FUNC_DC_CURRENT
    smu2461.commands.smu.source.range = 10e-3
    smu2461.commands.smu.source.readback = smu2461.commands.smu.ON

    # Digitize settings
    smu2461.commands.smu.digitize.func = (
        "smu.FUNC_DIGITIZE_VOLTAGE"  # smu2461.commands.smu.FUNC_DIGITIZE_VOLTAGE
    )
    smu2461.commands.smu.digitize.sense = smu2461.commands.smu.SENSE_4WIRE
    smu2461.commands.smu.digitize.range = 20
    smu2461.commands.smu.digitize.samplerate = 500000
    smu2461.commands.buffer_var["defbuffer1"].capacity = 1000000

    # Pulse command parameters
    CONFIG_LIST_NAME = "myPulseSweep"
    BIAS_LEVEL = "0"  # Bias level between pulses
    START = -10e-3  # Sweep start point
    STOP = 10e-3  # Sweep end point
    POINTS = 201  # 201 points in the sweep
    PULSE_WIDTH = "500e-6"  # Pulse width
    MeasureEnable = smu2461.commands.smu.ON  # Enables digitized measurements
    BUFFER_NAME = "defbuffer1"  # Buffer to save results
    PULSE_DELAY = 0  # Delay before each pulse
    OFF_TIME = "500e-6"  # Off time after each pulse
    COUNT = 1  # Number of times to repeat the pulse sweep
    X_BIAS_LIMIT = "2"  # Voltage limit between pulses
    X_PULSE_LIMIT = "20"  # Voltage limit during pulses
    fail_abort = smu2461.commands.smu.ON  # Abort pulse sweep if voltage limit is hit
    dual = smu2461.commands.smu.OFF  # Only sweep from -10ma to 10ma, but not back down again

    # Pulse command
    smu2461.commands.smu.source.pulsesweeplinear(
        CONFIG_LIST_NAME,
        BIAS_LEVEL,
        START,
        STOP,
        POINTS,
        PULSE_WIDTH,
        MeasureEnable,
        BUFFER_NAME,
        PULSE_DELAY,
        OFF_TIME,
        COUNT,
        X_BIAS_LIMIT,
        X_PULSE_LIMIT,
        fail_abort,
        dual,
    )

    # Set bit 8 when event 2731 occurs
    # Clear bit 8 when event 2732 occurs
    # (See Operation Event Register section of manual for more info)
    BIT = 8
    smu2461.commands.status.operation.setmap(BIT, 2731, 2732)
    is_sweeping = True  # pylint: disable=invalid-name

    # Run trigger model and wait for it to complete
    smu2461.commands.trigger.model.initiate()
    # waitcomplete
    _ = smu2461.commands.status.operation.condition  # throw away first read of status byte

    while is_sweeping:
        operation_condition_register = int(smu2461.commands.status.operation.condition.rstrip())
        is_sweeping = operation_condition_register == 2**BIT

    num: List[int] = []
    curr: List[float] = []
    volt: List[float] = []
    rdg_cnt: int
    if not (rdg_cnt := int(float(smu2461.commands.buffer_var["defbuffer1"].n))):
        print("No readings in buffer")
    else:
        for cnt in range(1, rdg_cnt + 1):
            num.append(cnt)
            curr.append(float(smu2461.commands.buffer_var["defbuffer1"].readings[cnt]))
            volt.append(float(smu2461.commands.buffer_var["defbuffer1"].readings[cnt]))
        print("Meas #\tCurrent\tVoltage")
        for cnt in range(1, rdg_cnt + 1):
            print(f"{num[cnt - 1]}\t{curr[cnt - 1]:+f}\t{volt[cnt - 1]:+f}")
