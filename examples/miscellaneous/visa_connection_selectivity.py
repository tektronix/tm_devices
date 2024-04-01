"""An example script to choose visa from different visa resources."""

from tm_devices import DeviceManager
from tm_devices.helpers import PYVISA_PY_BACKEND, SYSTEM_DEFAULT_VISA_BACKEND

with DeviceManager(verbose=True) as device_manager:
    # Explicitly specify to use the system VISA backend, this is the default,
    # **this code is not required** to use the system default.
    device_manager.visa_library = SYSTEM_DEFAULT_VISA_BACKEND
    # The above code can also be replaced by:
    device_manager.visa_library = "@ivi"

    # To use the PyVISA-py backend
    device_manager.visa_library = PYVISA_PY_BACKEND
    # The above code can also be replaced by:
    device_manager.visa_library = "@py"

    scope = device_manager.add_scope("127.0.0.1")
    print(scope)  # This prints basic information of the connected scope.
