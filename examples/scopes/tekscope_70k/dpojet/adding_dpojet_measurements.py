"""An example of adding dpojet measurements and plots."""
from tm_devices import DeviceManager
from tm_devices.drivers import MSO70KDX
from tm_devices.helpers import PYVISA_PY_BACKEND

with DeviceManager(verbose=True) as device_manager:
    # Enable resetting the devices when connecting and closing
    device_manager.setup_cleanup_enabled = True
    device_manager.teardown_cleanup_enabled = True

    # Use the PyVISA-py backend
    device_manager.visa_library = PYVISA_PY_BACKEND

    # Creating one 7K/70K/SX Scope driver object by providing ip address.
    scope: MSO70KDX = device_manager.add_scope("127.0.0.1")  # pyright: ignore[reportAssignmentType]

    # Starting DPOJET
    scope.commands.dpojet.activate.write()
    scope.commands.dpojet.version.query()

    # CLear all measurements
    scope.commands.dpojet.clearallmeas.write()

    # Add a few DPOJET measurements
    scope.commands.dpojet.addmeas.write("Period")
    scope.commands.dpojet.addmeas.write("Pduty")
    scope.commands.dpojet.addmeas.write("RiseTime")
    scope.commands.dpojet.addmeas.write("acrms")

    # Add a few DPOJET plots for the measurements
    scope.commands.dpojet.addplot.write("spectrum, MEAS1")
    scope.commands.dpojet.addplot.write("dataarray, MEAS2")
    scope.commands.dpojet.addplot.write("TimeTrend, MEAS3")
    scope.commands.dpojet.addplot.write("histogram, MEAS4")

    # Start a measurement
    scope.commands.dpojet.state.write("single")

    # Get the measurement values for the current acquisition data
    scope.commands.dpojet.meas[1].results.currentacq.max.query()
    scope.commands.dpojet.meas[1].results.currentacq.population.query()

    # Save all plots
    scope.commands.dpojet.saveallplots.write()

    # Save the report
    scope.commands.dpojet.report.savewaveforms.write("1")
    scope.commands.dpojet.report.write("EXECUTE")
