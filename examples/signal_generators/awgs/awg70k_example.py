"""An example script for AWG70K compiling sine waveform, name the waveform and play it."""

from tm_devices import DeviceManager
from tm_devices.drivers import AWG70KB
from tm_devices.helpers import PYVISA_PY_BACKEND

with DeviceManager(verbose=True) as device_manager:
    # Disable resetting the devices when connecting and closing
    device_manager.setup_cleanup_enabled = False
    device_manager.teardown_cleanup_enabled = False

    # Use the PyVISA-py backend
    device_manager.visa_library = PYVISA_PY_BACKEND

    # Creating Scope driver object by providing ip address.
    scope: AWG70KB = device_manager.add_awg("127.0.0.1")

    # Sets the Basic Waveform editor plug-in waveform type.
    scope.commands.bwaveform.function.write("SINE")
    # Sets the peak-to-peak Amplitude value for the waveform created by the Basic Waveform
    # editor plug-in.
    scope.commands.bwaveform.amplitude.write(250.0e-3)
    # Sets the Sample Rate for the waveform created by the Basic Waveform editor plug-in.
    scope.commands.bwaveform.srate.write(2.0e9)
    # Sets the name of the Basic Waveform editor plug-in compiled waveform.
    scope.commands.bwaveform.compile.name.write("Basic_Wfm_sine")
    # Enabled the state of the Basic Waveform editor to either immediately play the waveform
    # after compile or just compile
    scope.commands.bwaveform.compile.play.write("ON")
