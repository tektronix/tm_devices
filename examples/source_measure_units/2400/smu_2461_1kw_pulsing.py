"""This script creates pulses on the model 2461.

This script creates pulses on the model 2461.
"""

from time import sleep

from tm_devices import DeviceManager
from tm_devices.drivers import SMU2461

with DeviceManager() as device_manager:
    print(device_manager.get_available_devices())

    smu2461: SMU2461 = device_manager.add_smu("TCPIP::0.0.0.0::inst0::INSTR", alias="my2461")  # pyright: ignore[reportAssignmentType]

    # Reset the instrument
    smu2461.commands.reset()
    # Set up the pulse parameters (user-specified).
    CONFIG_LIST_NAME = "myPulses"
    BIAS_LEVEL = "0"
    PULSE_LEVEL = "10"
    PULSE_WIDTH = "1e-3"
    COUNT = 1
    MEASURE_ENABLE = smu2461.commands.smu.ON
    BUFFER_NAME = "defbuffer1"
    DELAY = 1e-3
    OFFTIME = "99e-3"
    X_BIAS_LIMIT = "2"
    X_PULSE_LIMIT = "21"
    FAIL_ABORT = smu2461.commands.smu.OFF
    # Set the source to output current.
    smu2461.commands.smu.source.func = smu2461.commands.smu.FUNC_DC_CURRENT
    smu2461.commands.smu.source.readback = smu2461.commands.smu.ON
    # Set up the measure functions.
    smu2461.commands.smu.digitize.func = "smu.FUNC_DIGITIZE_VOLTAGE"
    smu2461.commands.smu.digitize.sense = smu2461.commands.smu.SENSE_4WIRE
    smu2461.commands.smu.digitize.range = 20
    smu2461.commands.smu.digitize.samplerate = 500000
    smu2461.commands.buffer_var["defbuffer1"].capacity = 1000000
    # Send the pulse train command to set up the trigger model and config lists.
    smu2461.commands.smu.source.pulsetrain(
        CONFIG_LIST_NAME,
        BIAS_LEVEL,
        PULSE_LEVEL,
        PULSE_WIDTH,
        COUNT,
        MEASURE_ENABLE,
        BUFFER_NAME,
        DELAY,
        OFFTIME,
        X_BIAS_LIMIT,
        X_PULSE_LIMIT,
        FAIL_ABORT,
    )

    # Set bit 8 when event 2731 occurs
    # Clear bit 8 when event 2732 occurs
    # (See Operation Event Register section of manual for more info)
    BIT = 8
    smu2461.commands.status.operation.setmap(BIT, 2731, 2732)
    is_sweeping = True  # pylint: disable=invalid-name
    wait = 0.2  # pylint: disable=invalid-name
    smu2461.commands.trigger.model.initiate()
    # Wait for the measurements to complete. waitcomplete()
    _ = smu2461.commands.status.operation.condition  # throw away first read of status byte

    while is_sweeping:
        sleep(wait := wait * 1.1)
        operation_condition_register = int(smu2461.commands.status.operation.condition.rstrip())
        is_sweeping = operation_condition_register == 2**BIT
