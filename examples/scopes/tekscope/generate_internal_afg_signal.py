"""An example showing how to generate a signal using the scope's internal AFG."""

from tm_devices import DeviceManager
from tm_devices.drivers import MSO5

with DeviceManager(verbose=True) as dm:
    # Create a connection to the scope and indicate that it is a MSO5 scope for type hinting
    scope: MSO5 = dm.add_scope("192.168.1.102")  # pyright: ignore[reportAssignmentType]

    # Generate the signal using individual PI commands.
    scope.commands.afg.frequency.write(10e6)  # set frequency
    scope.commands.afg.offset.write(0.2)  # set offset
    scope.commands.afg.square.duty.write(50)  # set duty cycle
    scope.commands.afg.function.write("SQUARE")  # set function
    scope.commands.afg.output.load.impedance.write("FIFTY")  # set load impedance
    scope.commands.ch[1].scale.write(0.5, verify=True)  # set and check vertical scale on CH1
    scope.commands.afg.output.state.write(1)  # turn on the Internal AFG output
    scope.commands.esr.query()  # check for any errors

    scope.commands.acquire.stopafter.write("SEQUENCE")  # perform a single sequence

    # Generate the same signal using a single method call.
    scope.generate_function(
        frequency=10e6,
        offset=0.2,
        amplitude=0.5,
        duty_cycle=50,
        function=scope.source_device_constants.functions.SQUARE,
        termination="FIFTY",
    )
    scope.commands.ch[1].scale.write(0.5, verify=True)  # set and check vertical scale on CH1
    scope.commands.acquire.stopafter.write("SEQUENCE")  # perform a single sequence
