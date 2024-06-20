"""Check the behavior of the DeviceManager __dell__ method.

This is a test that should be run in isolation from the standard test suite. The standard test suite
runs this script via a subprocess to avoid interactions with the test of the tests.
"""

from contextlib import redirect_stdout
from io import StringIO
from unittest import mock

import pyvisa.constants

from conftest import mock_gethostbyaddr, mock_gethostbyname, SIMULATED_VISA_LIB
from tm_devices import DeviceManager, PYVISA_PY_BACKEND
from tm_devices.helpers import DMConfigOptions


@mock.patch("socket.gethostbyname", mock.MagicMock(side_effect=mock_gethostbyname))
@mock.patch("socket.gethostbyaddr", mock.MagicMock(side_effect=mock_gethostbyaddr))
@mock.patch(
    "pyvisa.resources.messagebased.MessageBasedResource.read_stb", mock.MagicMock(return_value=0)
)
@mock.patch(
    "pyvisa.resources.messagebased.MessageBasedResource.clear",
    mock.MagicMock(return_value=pyvisa.constants.StatusCode.success),
)
def verify_deleting_device_manager() -> None:
    """Test the behavior of deleting the DeviceManager instance."""
    # Test the __del__ method is run correctly
    with mock.patch.dict("os.environ", {"TM_OPTIONS": "STANDALONE,TEARDOWN_CLEANUP"}):
        dev_manager = DeviceManager(
            verbose=True, config_options=DMConfigOptions(setup_cleanup=True, teardown_cleanup=False)
        )
    assert dev_manager.visa_library == PYVISA_PY_BACKEND
    assert dev_manager.verbose
    assert not dev_manager.verbose_visa
    assert not dev_manager.teardown_cleanup_enabled
    assert dev_manager.setup_cleanup_enabled
    # Switch to the simulated visa library
    dev_manager.visa_library = SIMULATED_VISA_LIB
    # Set up the device manager with a single device
    assert not dev_manager.devices
    dev_manager.add_afg("afg3252c-hostname")
    assert len(dev_manager.devices) == 1
    # Delete the device manager
    stdout_buffer = StringIO()
    with redirect_stdout(stdout_buffer):
        del dev_manager

    stdout = stdout_buffer.getvalue()
    print(stdout)
    assert "Closing Connections to Devices" in stdout
    assert "Closing Connection to AFG 1" in stdout
    assert "DeviceManager Closed" in stdout

    # Test the .close() method closes and the __del__ method skips
    dev_manager = DeviceManager(verbose=True)
    dev_manager.visa_library = SIMULATED_VISA_LIB
    # Set up the device manager with a single device
    assert not dev_manager.devices
    dev_manager.add_afg("afg3252c-hostname")
    dev_manager.close()
    assert len(dev_manager.devices) == 1
    # Delete the device manager
    stdout_buffer = StringIO()
    with redirect_stdout(stdout_buffer):
        del dev_manager

    stdout = stdout_buffer.getvalue()
    print(stdout)
    assert stdout == ""

    # Test that the closing happens when the python interpreter exits
    with mock.patch.dict("os.environ", {"TM_DEVICES_VISA_LIBRARY": "custom_lib"}):
        dev_manager = DeviceManager(verbose=True)
    assert dev_manager.visa_library == "custom_lib"
    dev_manager.visa_library = SIMULATED_VISA_LIB
    # Set up the device manager with a single device
    assert not dev_manager.devices
    dev_manager.add_afg("afg3252c-hostname")


if __name__ == "__main__":
    verify_deleting_device_manager()
