"""2600 Series BJT Slow Example Script.

Description:
    This program performs a sequence of standard transistor tests for model 2N3904.

Required equipment:
    1 Keithley 2602 System Sourcemeter(c)
    1 Keithley 8101-04-TRX Test Fixture
    2 Keithley 2600-DEMO-TRX cables

Converted to Python tm_devices script. DCA 4.11.23
"""

import time

from typing import Dict, Tuple

from tm_devices import DeviceManager
from tm_devices.drivers import SMU2602B

RESOURCE_ID = "192.168.0.1"
NUM_PARTS = 1
DELAY = 0.01
NPLC = 0.001
NPLC2 = 0.05
AZERO = 0
VCEO_LIMIT = 40
SRC_COLLECTOR = 10e-3
LIMIT_VCESAT = 0.2
SRC_BASE = 1e-3
LIMIT_VBESAT = 1.1
VCE_SOURCE = 1
HIGH_IB = 10e-7
LOW_IB = 1e-9
HFE1_LIMIT = 40
TARGET_IC = 100e-6

# dicts to store the data for each part, and its overall status
vceo_data: Dict[int, float] = {}
vce_sat_data: Dict[int, float] = {}
vbe_sat_data: Dict[int, float] = {}
beta1_data: Dict[int, float] = {}
status_data: Dict[int, bool] = {}
bins = [0, 0, 0, 0, 0]


def bjt_slow(inst: SMU2602B) -> None:
    """This function will loop repeatedly to test a certain amount of BJTs for functionality.

    The constant NUM_PARTS corresponds to the number of BJTs to test. Each will undergo four tests:
    VCEO, VCEsat, VBEsat, and HFE1. Once finished, the results will be printed to the console.

    Args:
        inst (SMU2602B): The python driver instance for the instrument used in testing.

    Note:
        Each part will be binned according to its test results. The bins are as follows:
            Bin 0: Passed All Tests
            Bin 1: Failed VCEO
            Bin 2: Failed VCEsat
            Bin 3: Failed VBEsat
            Bin 4: Failed HFE1
    """
    for index in range(NUM_PARTS):
        setup(inst)

        vceo_status = vceo(inst, index)
        vce_sat_status, vbe_sat_status = vbe_vce_sat(inst, index)
        hfe_status = hfe1(inst, index)

        if not vceo_status:
            bins[1] += 1
        elif not vce_sat_status:
            bins[2] += 1
        elif not vbe_sat_status:
            bins[3] += 1
        elif not hfe_status:
            bins[4] += 1
        else:
            bins[1] += 1

        status_data[index] = vceo_status and vce_sat_status and vbe_sat_status and hfe_status

        # Reset intrument to
        inst.commands.smu["b"].source.func = inst.commands.smu["b"].OUTPUT_DCVOLTS
        inst.commands.smu["b"].source.levelv = 0

        inst.commands.smu["a"].source.func = inst.commands.smu["a"].OUTPUT_DCVOLTS
        inst.commands.smu["a"].source.levelv = 0

        inst.commands.smu["b"].measure.autozero = inst.commands.smu["b"].AUTOZERO_AUTO
        inst.commands.smu["b"].measure.nplc = NPLC
        inst.commands.smu["b"].measure.v()
        inst.commands.smu["b"].measure.i()

        inst.commands.smu["a"].measure.autozero = inst.commands.smu["a"].AUTOZERO_AUTO
        inst.commands.smu["a"].measure.nplc = NPLC
        inst.commands.smu["a"].measure.v()
        inst.commands.smu["a"].measure.i()

        inst.commands.smu["a"].source.output = inst.commands.smu["a"].OUTPUT_OFF
        inst.commands.smu["b"].source.output = inst.commands.smu["b"].OUTPUT_OFF

    display_results()


def setup(inst: SMU2602B) -> None:
    """This function sends the commands to setup the instrument before the tests begin.

    Args:
        inst (SMU2602B): The python driver instance for the instrument used in testing.
    """
    inst.commands.digio.writeport(0)

    inst.commands.smu["a"].reset()
    inst.commands.smu["b"].reset()

    # Setup SMUB - Base
    inst.commands.smu["b"].source.func = inst.commands.smu["b"].OUTPUT_DCVOLTS
    inst.commands.smu["b"].measure.autozero = AZERO
    inst.commands.smu["b"].measure.autorangei = inst.commands.smu["b"].AUTORANGE_OFF
    inst.commands.smu["b"].measure.autorangev = inst.commands.smu["b"].AUTORANGE_OFF
    inst.commands.smu["b"].source.autorangei = inst.commands.smu["b"].AUTORANGE_OFF
    inst.commands.smu["b"].source.autorangev = inst.commands.smu["b"].AUTORANGE_OFF

    inst.commands.smu["b"].source.rangei = 0.01
    inst.commands.smu["b"].source.levelv = 0
    inst.commands.smu["b"].source.output = inst.commands.smu["b"].OUTPUT_ON

    # Setup SMUA - Collector
    inst.commands.smu["a"].source.func = inst.commands.smu["a"].OUTPUT_DCVOLTS
    inst.commands.smu["a"].measure.autozero = inst.commands.smu["a"].AUTOZERO_AUTO
    inst.commands.smu["a"].measure.nplc = NPLC
    inst.commands.smu["a"].measure.v()
    inst.commands.smu["a"].measure.i()
    inst.commands.smu["a"].measure.autozero = AZERO

    inst.commands.smu["a"].measure.autorangei = 0
    inst.commands.smu["a"].measure.autorangev = 0
    inst.commands.smu["a"].source.autorangei = 0
    inst.commands.smu["a"].source.autorangev = 0

    inst.commands.smu["a"].source.rangev = 40
    inst.commands.smu["a"].source.levelv = 0
    inst.commands.smu["a"].source.output = inst.commands.smu["b"].OUTPUT_ON


def vceo(inst: SMU2602B, index: int) -> bool:
    """This function will run the VCEO test on the transistor.

    Args:
        inst (SMU2602B): The python driver instance for the instrument used in testing.
        index (int): The number of the transistor under test.

    Returns:
        bool: Returns the status of the VCEO test. Pass = True, Fail = False.
    """
    inst.commands.smu["a"].measure.nplc = NPLC
    inst.commands.smu["b"].measure.nplc = NPLC

    inst.commands.smu["b"].source.func = inst.commands.smu["b"].OUTPUT_DCAMPS
    inst.commands.smu["b"].source.rangev = VCEO_LIMIT
    inst.commands.smu["b"].source.limitv = VCEO_LIMIT
    inst.commands.smu["b"].source.leveli = 0
    inst.commands.smu["b"].source.rangei = 100e-9
    inst.commands.smu["b"].measure.rangev = VCEO_LIMIT
    time.sleep(DELAY)

    inst.commands.smu["a"].source.func = inst.commands.smu["a"].OUTPUT_DCAMPS
    inst.commands.smu["a"].source.rangev = VCEO_LIMIT
    inst.commands.smu["a"].source.limitv = VCEO_LIMIT
    inst.commands.smu["a"].source.rangei = 0.01
    inst.commands.smu["a"].source.leveli = 0.01
    inst.commands.smu["a"].measure.rangev = VCEO_LIMIT
    time.sleep(DELAY)

    vceo_data[index] = float(inst.commands.smu["a"].measure.v())

    status = vceo_data[index] > 0.75 * VCEO_LIMIT

    display_status(index, "VCEO", status)
    return status


def vbe_vce_sat(inst: SMU2602B, index: int) -> Tuple[bool, bool]:
    """This function will run the VCEsat and VBEsat tests on the transistor.

    Args:
        inst (SMU2602B): The python driver instance for the instrument used in testing.
        index (int): The number of the transistor under test.

    Returns:
        tuple: Returns a tuple containing two booleans, the first for the status of the VBEsat
        test, and the second for the status of the VCEsat test. Pass = True, Fail = False
    """
    inst.commands.smu["a"].measure.rangev = 1
    inst.commands.smu["a"].source.rangei = SRC_COLLECTOR
    inst.commands.smu["a"].source.leveli = SRC_COLLECTOR

    inst.commands.smu["b"].measure.rangev = 1
    inst.commands.smu["b"].source.rangei = SRC_BASE
    inst.commands.smu["b"].source.leveli = SRC_BASE
    time.sleep(DELAY)

    vce_sat_data[index] = float(inst.commands.smu["a"].measure.v())
    vbe_sat_data[index] = float(inst.commands.smu["b"].measure.i())

    vce_sat_status = vce_sat_data[index] < LIMIT_VCESAT
    vbe_sat_status = vbe_sat_data[index] < LIMIT_VBESAT

    display_status(index, "VCEsat", vce_sat_status)
    display_status(index, "VBEsat", vbe_sat_status)
    return vce_sat_status, vbe_sat_status


def hfe1(inst: SMU2602B, index: int) -> bool:
    """This function will run the HFE1 test on the transistor.

    Args:
        inst (SMU2602B): The python driver instance for the instrument used in testing.
        index (int): The number of the transistor under test.

    Returns:
        bool: Returns the status of the HFE1 test. Pass = True, Fail = False
    """
    # these are used to modify these values without overwriting between tests
    high_ib_tmp = HIGH_IB
    low_ib_tmp = LOW_IB

    inst.commands.smu["a"].measure.nplc = NPLC2
    inst.commands.smu["b"].measure.nplc = NPLC2

    inst.commands.smu["a"].source.func = inst.commands.smu["a"].OUTPUT_DCVOLTS
    inst.commands.smu["a"].source.limiti = 5 * TARGET_IC
    inst.commands.smu["a"].source.rangev = 6
    inst.commands.smu["a"].measure.rangei = 10e-3

    inst.commands.smu["b"].source.func = inst.commands.smu["b"].OUTPUT_DCVOLTS
    inst.commands.smu["b"].measure.rangei = 100e-6
    inst.commands.smu["b"].source.limiti = HIGH_IB
    inst.commands.smu["b"].source.rangev = 6
    inst.commands.smu["b"].source.limitv = 6
    inst.commands.smu["b"].measure.rangev = 6

    inst.commands.smu["a"].source.levelv = VCE_SOURCE
    inst.commands.smu["b"].source.leveli = 0
    inst.commands.smu["a"].source.output = inst.commands.smu["a"].OUTPUT_ON

    time.sleep(DELAY)

    # Search for the right base current
    index = 0
    max_loops = 10
    while True:
        index += 1
        ib_value = (high_ib_tmp + low_ib_tmp) / 2 + low_ib_tmp
        inst.commands.smu["b"].source.leveli = ib_value
        time.sleep(0.01)

        if ic_meas := float(inst.commands.smu["a"].measure.i()) > TARGET_IC:
            high_ib_tmp = ib_value
        else:
            low_ib_tmp = ib_value

        if index > max_loops or abs(ic_meas - TARGET_IC) < (0.05 * TARGET_IC):
            break

    beta1_data[index] = ic_meas / ib_value

    status = beta1_data[index] > HFE1_LIMIT

    display_status(index, "HFE1", status)
    return status


def display_status(test_number: int, test_name: str, status: bool) -> None:
    """This function prints the status of the transistor under test to the console.

    Args:
        test_number (int): The number of the transistor under test
        test_name (str): The name of the test as a string.
        status (bool): The status of the transistor.
    """
    status_str = "Pass" if status else "Fail"
    print(f"PART {test_number} {test_name}: {status_str}")


def display_results(sep: str = "\t") -> None:
    """This function will iterate through each of the data arrays and print their data to console.

    Args:
        sep (str, optional): Controls the separator of the output table. Defaults to tab.
    """
    print("")
    print("BJT Slow Complete. Results: ")
    print("VCEO", "VCEsat", "VBEsat", "BETA1", "STATUS", sep=sep)
    for index in range(NUM_PARTS):
        status_str = "Pass" if status_data[index] else "Fail"
        print(
            f"{vceo_data[index]:.2e}",
            f"{vce_sat_data[index]:.2e}",
            f"{vbe_sat_data[index]:.2e}",
            f"{beta1_data[index]:.2e}",
            status_str,
            sep=sep,
        )


# Connect to instrument and begin testing.
with DeviceManager(verbose=False) as DM:
    smu_driver: SMU2602B = DM.add_smu(RESOURCE_ID)  # pyright: ignore[reportAssignmentType]

    bjt_slow(smu_driver)
