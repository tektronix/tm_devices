"""An example script for connecting and configuring scope for acquisition."""
from tm_devices import DeviceManager
from tm_devices.drivers import MSO6B
from tm_devices.helpers import PYVISA_PY_BACKEND

with DeviceManager(verbose=True) as device_manager:
    # Enable resetting the devices when connecting and closing
    device_manager.setup_cleanup_enabled = True
    device_manager.teardown_cleanup_enabled = True

    # Use the PyVISA-py backend
    device_manager.visa_library = PYVISA_PY_BACKEND

    # Creating Scope driver object by providing ip address.
    scope: MSO6B = device_manager.add_scope("127.0.0.1")  # pyright: ignore[reportAssignmentType]

    # Turn on channel 1
    scope.commands.display.waveview1.ch[1].state.write("ON")

    # Set channel 1 vertical scale to 10mV
    scope.commands.ch[1].scale.write(10e-3)

    # Set horizontal record length to 20000
    scope.commands.horizontal.recordlength.write(20000)

    # Set horizontal position to 100
    scope.commands.horizontal.position.write(10)

    # Set trigger type to Edge
    scope.commands.trigger.a.type.write("EDGE")

    # Acquisition setup
    scope.commands.acquire.state.write("OFF")
    scope.commands.acquire.mode.write("Sample")
    scope.commands.acquire.stopafter.write("Sequence")

    # Adding measurements
    scope.commands.measurement.addmeas.write("AMPLitude")
    scope.commands.measurement.addmeas.write("PK2PK")
    scope.commands.measurement.meas[1].source.write("CH1")
    scope.commands.measurement.meas[2].source.write("CH1")

    # Get the measurement values
    scope.commands.acquire.state.write("ON")

    if int(scope.commands.opc.query()) == 1:
        scope.commands.measurement.meas[1].results.currentacq.mean.query()
        scope.commands.measurement.meas[2].results.currentacq.maximum.query()
