"""An example of using devices which are defined via environment variables.

These environment variables are settable outside Python code, usually they are set in the shell used
to execute the Python script.
"""

import os

from tm_devices import DeviceManager

# Indicate to use the PyVISA-py backend rather than any installed VISA backends.
os.environ["TM_OPTIONS"] = "STANDALONE"
# Define some devices.
os.environ["TM_DEVICES"] = (
    "device_type=SCOPE,address=<IP or hostname>"  # Define a scope
    "~~~device_type=AFG,address=<IP or hostname>"  # Define an AFG
    "~~~device_type=SMU,address=<IP or hostname>"  # Define a SMU
)

# Create Tektronix Devices

with DeviceManager(verbose=True) as dm:
    # Scope
    scope = dm.get_scope(1)
    print(scope.query("IDN?"))

    # Set horizontal scale and verify success
    scope.set_and_check(":HORIZONTAL:SCALE", 400e-9)
    scope.expect_esr(0)

    # AFG
    afg = dm.get_afg(1)
    print(afg.idn_string)

    # Turn on AFG and verify success
    afg.set_and_check(":OUTPUT1:STATE", "1")

    # SMU
    smu = dm.get_smu(1)

    # Get device information
    print(smu.query("print(localnode.model)"))
    print(smu.query("print(localnode.serialno)"))
    print(smu.query("print(localnode.version)"))
