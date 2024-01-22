"""2600 Series Diode Test Example Script.

Description:
    This script is a conversion of a TSP script called DiodeTest_fast.tsp. This script
    is used to test diodes. It uses several functions to perform forward/reverse voltage,
    dynamic impedance, and current leakage tests. It then displays this information to either
    the console, the instrument display, or both

This script was originally created by Keithley Instruments' Applications
Engineering (Al Ivons) on 08 Apr 2005

Converted to Python tm_devices script. DCA 4.12.23
"""
import time

from typing import Dict, Tuple

from tm_devices import DeviceManager
from tm_devices.drivers import SMU2602B

RESOURCE_ID = "192.168.0.1"

# Any value other than "FAST" will default to slow.
SPEED = "FAST"

# The number of diodes to test.
NDIODES = 1

# Test Inspection Limits (based on Keithley P/N PL-118-1)
VF1_LOW = 3.078  # Low inspection limit for vf1
VF1_HIGH = 3.762  # High inspection limit for vf1
VF2_LOW = 3.366  # Low inspection limit for vf2
VF2_HIGH = 4.114  # High inspection limit for vf2
DYNZ_LOW = -26.4  # Low inspection limit for dynz
DYNZ_HIGH = 69.1  # High inspection limit for dynz
IR1_LOW = -2e-5  # Low inspection limit for ir1
IR1_HIGH = 0  # High inspection limit for ir1
IR2_LOW = -20e-5  # Low inspection limit for ir2
IR2_HIGH = 0  # High inspection limit for ir2
VR_LOW = -39.1  # Low inspection limit for vr
VR_HIGH = -28.9  # High inspection limit for vr

# Source and measure settings are based on Keithley P/N PL-118-1
# Variables used to configure source and measure settings for vf1 test
VF1_ISRC_RNG = 0.005
VF1_ISRC_LEV = 0.005
VF1_SRC_DEL = 0 if SPEED == "FAST" else 0.1  # "SLOW" value 0.1 is default
VF1_VCMPL = 10

# Variables used to configure source and measure settings for vf2 test
VF2_ISRC_RNG = 0.02
VF2_ISRC_LEV = 0.02
VF2_SRC_DEL = 0 if SPEED == "FAST" else 0.1  # "SLOW" value 0.1 is default
VF2_VCMPL = 10

# Variables used to configure source and measure settings for ir1 test
IR1_VSRC_RNG = 40
IR1_VSRC_LEV = -20
IR1_SRC_DEL = 0 if SPEED == "FAST" else 0.1  # "SLOW" value 0.1 is default
IR1_ICMPL = 100e-6

# Variables used to configure source and measure settings for ir2 test
IR2_VSRC_RNG = 40
IR2_VSRC_LEV = -25
IR2_SRC_DEL = 0 if SPEED == "FAST" else 0.1  # "SLOW" value 0.1 is default
IR2_ICMPL = 100e-6

# Variables used to configure source and measure settings for vr test
VR_ISRC_RNG = 100e-6
VR_ISRC_LEV = -100e-6
VR_SRC_DEL = 0 if SPEED == "FAST" else 0.1  # "SLOW" value 0.1 is default
VR_VCMPL = 40

# Integration time used for all measurements
# Expressed in terms of powerline cyclesff (PLC)
NPLC = 0.001 if SPEED == "FAST" else 1

# Boolean flag used to select autozero mode (true = auto and false = once)
AZERO_ON = SPEED != "FAST"

# Delay (in seconds) to slow sequence down for viewing when SPEED = "SLOW"
DELAY = 0 if SPEED == "FAST" else 1

# Create dictionaries to store data.
# Tables used to hold test data and pass/fail status for vf1 test
vf1_test_curr: Dict[int, float] = {}
vf1_test_volt: Dict[int, float] = {}
vf1_status: Dict[int, bool] = {}

# Tables used to hold test data and pass/fail status for vf2 test
vf2_test_curr: Dict[int, float] = {}
vf2_test_volt: Dict[int, float] = {}
vf2_status: Dict[int, bool] = {}

# Tables used to hold test data and pass/fail status for dynz test
dynz_data: Dict[int, float] = {}
dynz_status: Dict[int, bool] = {}

# Tables used to hold test data and pass/fail status for ir1 test
ir1_test_volt: Dict[int, float] = {}
ir1_test_curr: Dict[int, float] = {}
ir1_status: Dict[int, bool] = {}

# Tables used to hold test data and pass/fail status for ir2 test
ir2_test_volt: Dict[int, float] = {}
ir2_test_curr: Dict[int, float] = {}
ir2_status: Dict[int, bool] = {}

# Tables used to hold test data and pass/fail status for vr test
vr_test_curr: Dict[int, float] = {}
vr_test_volt: Dict[int, float] = {}
vr_status: Dict[int, bool] = {}

# Table to hold good/bad part status based on cumulative results of all tests
part_status: Dict[int, bool] = {}

# Table used to count parts put into simulated bins of a component handler
bins = [0, 0, 0, 0, 0, 0, 0]  # Initially set all bins to zero


def diode_test(inst: SMU2602B) -> None:
    """This function performs a complete diode test sequence consisting of 6 tests.

    The tests include:
        - 2 Forward Voltage tests (vf1 and vf2)
        - 1 Dynamic Impedance test (dynz)
        - 2 Reverse Leakage Current tests (ir1 and ir2)
        - 1 Reverse Voltage Breakdown test (vr)

    The individual tests are executed in the order they are listed.  Test results are
    inspected against limits and pass/fail status is displayed on the front panel.
    Based on the pass/fail results the part is "binned".  Digital I/O port Bit 1 is set
    high if the diode is good, or Bit 2 is set high if the part is bad.

    Args:
        inst (SMU2602B): The Python driver instance for the instrument used in the test.
    """
    print("Starting Diode Test...")

    # Perform initial setup of 2600 unit.
    inst.commands.reset()
    inst.commands.smu["a"].reset()

    inst.commands.smu["a"].source.func = inst.commands.smu["a"].OUTPUT_DCVOLTS
    inst.commands.smu["a"].source.levelv = 0

    inst.commands.smu["a"].sense = inst.commands.smu["a"].SENSE_LOCAL
    inst.commands.smu["a"].measure.nplc = NPLC

    if AZERO_ON:
        inst.commands.smu["a"].measure.autozero = inst.commands.smu["a"].AUTOZERO_AUTO
    else:
        inst.commands.smu["a"].measure.autozero = inst.commands.smu["a"].AUTOZERO_ONCE

    inst.commands.errorqueue.clear()  # Clear the error queue

    if SPEED == "FAST":
        inst.commands.display.clear()
        inst.commands.display.setcursor(1, 1)  # type: ignore
        inst.commands.display.settext("Test In Progress")
        inst.commands.display.setcursor(2, 1)  # type: ignore
        inst.commands.display.settext(f"Testing {NDIODES} Parts")

    start_time = time.time()

    inst.commands.smu["a"].source.output = inst.commands.smu["a"].OUTPUT_ON

    for index in range(NDIODES):
        # Perform Forward Voltage Test #1 (Vf1)
        vf1_test_volt[index], vf1_test_curr[index] = vfwd_vrev(
            inst, VF1_ISRC_RNG, VF1_ISRC_LEV, VF1_SRC_DEL, VF1_VCMPL
        )
        vf1_status[index] = test_status(vf1_test_volt[index], VF1_LOW, VF1_HIGH)
        display_test_status("Vf1: ", vf1_test_volt[index], "V", vf1_status[index])

        # Perform Forward Voltage Test #2 (Vf2)
        vf2_test_volt[index], vf2_test_curr[index] = vfwd_vrev(
            inst, VF2_ISRC_RNG, VF2_ISRC_LEV, VF2_SRC_DEL, VF2_VCMPL
        )
        vf2_status[index] = test_status(vf2_test_volt[index], VF2_LOW, VF2_HIGH)
        display_test_status("Vf2: ", vf2_test_volt[index], "V", vf2_status[index])

        # Perform Dynamic Impedance Test (DynZ)
        dynz_data[index] = dynz(
            vf1_test_curr[index], vf1_test_volt[index], vf2_test_curr[index], vf2_test_volt[index]
        )
        dynz_status[index] = test_status(dynz_data[index], DYNZ_LOW, DYNZ_HIGH)
        display_test_status("DynZ: ", dynz_data[index], "Ω", dynz_status[index])

        # Perform Reverse Leakage Current Test #1 (Ir1)
        ir1_test_volt[index], ir1_test_curr[index] = i_leakage(
            inst, IR1_VSRC_RNG, IR1_VSRC_LEV, IR1_SRC_DEL, IR1_ICMPL
        )
        ir1_status[index] = test_status(ir1_test_curr[index], IR1_LOW, IR1_HIGH)
        display_test_status("Ir1: ", ir1_test_curr[index], "A", ir1_status[index])

        # Perform Reverse Leakage Current Test #2 (Ir2)
        ir2_test_volt[index], ir2_test_curr[index] = i_leakage(
            inst, IR2_VSRC_RNG, IR2_VSRC_LEV, IR2_SRC_DEL, IR2_ICMPL
        )
        ir2_status[index] = test_status(ir2_test_curr[index], IR2_LOW, IR2_HIGH)
        display_test_status("Ir2: ", ir2_test_curr[index], "A", ir2_status[index])

        # Perform Reverse Voltage Breakdown Test (Vr)
        vr_test_volt[index], vr_test_curr[index] = vfwd_vrev(
            inst, VR_ISRC_RNG, VR_ISRC_LEV, VR_SRC_DEL, VR_VCMPL
        )
        vr_status[index] = test_status(vr_test_volt[index], VR_LOW, VR_HIGH)
        display_test_status("Vr: ", vr_test_volt[index], "V", vr_status[index])

        # Determine cumulative part status
        part_status[index] = get_part_status(
            vf1_status[index],
            vf2_status[index],
            dynz_status[index],
            ir1_status[index],
            ir2_status[index],
            vr_status[index],
        )

        # Bin the part
        bin_part(
            vf1_status[index],
            vf2_status[index],
            dynz_status[index],
            ir1_status[index],
            ir2_status[index],
            vr_status[index],
        )

        time.sleep(DELAY)

    inst.commands.smu["a"].source.output = inst.commands.smu["a"].OUTPUT_OFF

    stop_time = time.time()
    elapsed_time = stop_time - start_time

    print("Diode Test Complete.")
    print("Elapsed time:", f"{elapsed_time:.2f}s")
    display_bins_status()


def vfwd_vrev(
    inst: SMU2602B, irange: float, ilevel: float, srcdelay: float, vcmpl: float
) -> Tuple[float, float]:
    """This function performs a Forward Voltage Test or a Reverse Voltage Breakdown Test.

    Args:
        inst (SMU2602B): The python driver instance corresponding to the intrument under test.
        irange (float): The current range to use for the test.
        ilevel (float): The current level to use for the test.
        srcdelay (float): The delay after the source is set before the measurement is started.
        vcmpl (float): The voltage compliance limit for the test. This is also used to select the
            voltage measurement range.

    Returns:
        a tuple containing the voltage and current measurements as floating point values
    """
    # Configure source and measure settings
    inst.commands.smu["a"].source.func = inst.commands.smu["a"].OUTPUT_DCAMPS
    inst.commands.smu["a"].source.rangei = irange
    inst.commands.smu["a"].source.leveli = ilevel
    inst.commands.smu["a"].source.limitv = vcmpl
    inst.commands.smu["a"].measure.rangev = vcmpl

    # Wait before making measurement
    time.sleep(srcdelay)

    # Measure current and voltage
    response = inst.commands.smu["a"].measure.iv()
    response_split = response.split("\t")
    voltage, current = response_split[0], response_split[1]

    # Set source output to zero
    inst.commands.smu["a"].source.leveli = 0

    return float(voltage), float(current)


def dynz(curr1: float, volt1: float, curr2: float, volt2: float) -> float:
    """This function calculates the Dynamic Impedance test.

    The test is based on two forward voltage or two reverse voltage measurements.

    Args:
        curr1 (float): The test current used for first forward voltage measurement
        volt1 (float): The resulting voltage for first forward voltage measurement
        curr2 (float): The test current used for second forward voltage measurement
        volt2 (float): The resulting voltage for second forward voltage measurement

    Returns:
        The dynamic inpedence calculated using the values provided.
    """
    denominator = curr2 - curr1 if curr2 - curr1 > 0 else 1e-37
    return (volt2 - volt1) / denominator


def i_leakage(
    inst: SMU2602B, vrange: float, vlevel: float, srcdelay: float, icmpl: float
) -> Tuple[float, float]:
    """This function performs a Reverse Leakage Current Test.

    Args:
        inst (SMU2602B): The python driver instance corresponding to the intrument under test.
        vrange (float): The voltage range to use for the test.
        vlevel (float): The voltage level to use for the test.
        srcdelay (float): The delay after the source is set before the measurement is started.
        icmpl (float): The current compliance limit for the test. This is also used to select the
            current measurement range

    Returns:
        A tuple containing the measured voltage and current as floting point values.
    """
    # Configure source and measure settings
    inst.commands.smu["a"].source.func = "smua.OUTPUT_DCVOLTS"
    inst.commands.smu["a"].source.rangev = vrange
    inst.commands.smu["a"].source.levelv = vlevel
    inst.commands.smu["a"].source.limiti = icmpl
    inst.commands.smu["a"].measure.rangei = icmpl

    # Wait before making measurement
    time.sleep(srcdelay)

    # Measure current and voltage
    response = inst.commands.smu["a"].measure.iv()
    response_split = response.split("\t")
    voltage, current = response_split[0], response_split[1]

    # Set source output to 0
    inst.commands.smu["a"].source.levelv = 0

    return float(voltage), float(current)


def test_status(value: float, low: float, high: float) -> bool:
    """This function determines the status of an individual test within the test sequence.

    Args:
        value (float): The result (measurement or calculation) of an individual test
        low (float): The minimum acceptable value for the subject test
        high (float): The maximum acceptable value for the subject test

    Returns:
        A boolean indicating whether the test passed or failed. Pass = True, Fail = False
    """
    if value < low or value > high:
        return False
    return True


def get_part_status(vf1: bool, vf2: bool, dyn_z: bool, ir1: bool, ir2: bool, vr_: bool) -> bool:
    """This function determines the overall status of the part.

    Args:
        vf1 (bool): flag for forward voltage test 1
        vf2 (bool): flag for forward voltage test 2
        dyn_z (bool): flag for dynamic impedence test
        ir1 (bool): flag for current leakage test 1
        ir2 (bool): flag for current leakage test 2
        vr_ (bool): flag for reverse voltage test

    Returns:
        Returns True if all tests pass, otherwise returns False
    """
    return vf1 and vf2 and dyn_z and ir1 and ir2 and vr_


def bin_part(vf1: bool, vf2: bool, dyn_z: bool, ir1: bool, ir2: bool, vr_: bool) -> None:
    """This function increments the list simulating the bins a component handler may use.

    Args:
        vf1 (bool): flag for forward voltage test 1
        vf2 (bool): flag for forward voltage test 2
        dyn_z (bool): flag for dynamic impedence test
        ir1 (bool): flag for current leakage test 1
        ir2 (bool): flag for current leakage test 2
        vr_ (bool): flag for reverse voltage test
    """
    if not vf1:  # If part first failed Forward Voltage Test #1
        bins[1] += 1
    elif not vf2:  # If part first failed Forward Voltage Test #2
        bins[2] += 1
    elif not dyn_z:  # If part first failed Dynamic Impedance Test
        bins[3] += 1
    elif not ir1:  # If part first failed Reverse Leakage Current Test #1
        bins[4] += 1
    elif not ir2:  # If part first failed Reverse Leakage Current Test #2
        bins[5] += 1
    elif not vr_:  # If part first failed Reverse Voltage Breakdown Test
        bins[6] += 1
    else:  # Part passed; does not fail any tests
        bins[0] += 1


def display_test_status(name: str, value: float, unit: str, status: bool) -> None:
    """Displays individual test results to the console.

    Args:
        name (str): A label to display to identify the test. For example: "Vf1: "
        value (float): The result (measurement or calculation) of an individual test
        unit (str): The unit to display with the test value. For example: "V", "A" etc.
        status (bool): The status of the subject test
    """
    status_str = "PASS" if status else "FAIL"
    # Reduce the result to scientific notation with 2 decimal places
    print(name, f"{float(value):.2e}" + unit, status_str)


def display_bins_status() -> None:
    """Used to display the counts for each bin."""
    print("Bin Counts: ")
    display_str = ""
    for index in range(7):
        display_str += str(bins[index]) + " "
    print(display_str)


# Connect to instrument and begin testing
with DeviceManager(verbose=False) as DM:
    smu_driver: SMU2602B = DM.add_smu(RESOURCE_ID)  # pyright: ignore[reportAssignmentType]

    # Save settings in temporary variables so they can be restored after completion.
    s_func = smu_driver.commands.smu["a"].source.func
    s_autorangei = smu_driver.commands.smu["a"].source.autorangei
    s_rangei = smu_driver.commands.smu["a"].source.rangei
    s_leveli = smu_driver.commands.smu["a"].source.leveli
    m_autorangev = smu_driver.commands.smu["a"].measure.autorangev
    m_rangev = smu_driver.commands.smu["a"].measure.rangev

    diode_test(smu_driver)

    # Update the front panel display and restore modified settings.
    smu_driver.commands.smu["a"].source.func = s_func
    smu_driver.commands.smu["a"].source.autorangei = s_autorangei
    smu_driver.commands.smu["a"].source.rangei = s_rangei
    smu_driver.commands.smu["a"].source.leveli = s_leveli
    smu_driver.commands.smu["a"].measure.autorangev = m_autorangev
    smu_driver.commands.smu["a"].measure.rangev = m_rangev
