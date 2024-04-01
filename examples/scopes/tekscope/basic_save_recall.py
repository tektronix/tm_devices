"""An example of saving and recalling a waveform and session file."""

from tm_devices import DeviceManager
from tm_devices.drivers import MSO6B

with DeviceManager(verbose=True) as dm:
    # Get a scope
    scope: MSO6B = dm.add_scope("192.168.1.177")  # pyright: ignore[reportAssignmentType]

    # Send some commands
    scope.add_new_math("MATH1", "CH1")  # add MATH1 to CH1
    scope.turn_channel_on("CH2")  # turn on channel 2
    scope.set_and_check(":HORIZONTAL:SCALE", 100e-9)  # adjust horizontal scale

    # save the session as example.tss
    scope.commands.save.session.write("example.tss")
    # save the waveform on CH1 as example.wfm
    scope.commands.save.waveform.write('CH1,"example.wfm"')

    scope.reset()  # reset the scope

    scope.recall_session("example.tss")  # recall the saved session example.tss
    scope.recall_reference("example.wfm", 1)  # recall example.wfm as REF1
