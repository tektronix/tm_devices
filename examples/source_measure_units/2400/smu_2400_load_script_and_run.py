"""2400 Series Current Sweep Example Script.

Description:
    This example shows how a user can send a TSP script file from their PC
    to their 2400 Interactive SourceMeter then call its embedded function(s),
    possibly acquiring measurement data. The TSP script file which accompanies
    this code includes a function that performs a 4-wire (or 4-point)
    resistivity measurement on semiconductor wafer material. The application
    note on which the script is based can be found at:
    https://www.tek.com/en/documents/application-note/resistivity-measurements-using-model-2450-sourcemeter-smu-instrument-and-f

    A copy of the TSP script file can be obtained at:
    https://github.com/tektronix/keithley/tree/main/Application_Specific/Resistivity_of_Materials/Measuring_Resistivity_with_a_4-Point_Probe/Load_and_Execute_with_Python
"""

import pathlib

from tm_devices import DeviceManager
from tm_devices.drivers import SMU2450

# Main code starts here with instantiation of the device manager and the SMU instrument connection.
devmgr = DeviceManager(verbose=True)
smu2400: SMU2450 = devmgr.add_smu("192.168.0.1", alias="my2450")  # pyright: ignore[reportAssignmentType]
smu2400.enable_verification = False

# Capture the path to the script file and load it to working memory.
print(pathlib.Path.cwd())
fileandpath = f"{pathlib.Path.cwd()}\\KEI2400_TTI_Driver\\simple_resistivity_measure.tsp"
smu2400.load_script(fileandpath, script_name="resistivityscript", run_script=True)

# Call the resistivity measurement function on the instrument with the desired current,
# then print the result to the console.
I_LEVEL = 100e-3
RESISTIVITY_VALUE = float(smu2400.query(f"print(resistivity_4point({I_LEVEL}))"))
print(f"Resistivity = {RESISTIVITY_VALUE:0.4e} Ω/Square")

devmgr.close()
