"""SMU Model 2657A Capacitor Leakage Test Example Script.

Description:
    This example demonstrates how to use the Model 2657A High Power System SourceMeter
    instrument to measure the leakage current and calculate the insulation resistance of
    a capacitor.

Required Equipment:
    1x SMU 2657A
    1x Model 8010 High Power Device Test Fixture or similar
    1x High voltage capacitor

Note:
    This test uses high voltage! Ensure your test setup is correct and proper safety measures
    have been taken.

Converted to Python tm_devices script. DCA 5.10.23
"""

from tm_devices import DeviceManager
from tm_devices.drivers import SMU2657A

RESOURCE_ID = "192.168.0.1"

LEVEL_V = 2000
LIMIT_I = 1e-3
MEAS_RANGE = 10e-9
NUM_READINGS = 10
SOAK_TIME = 30
NPLC = 1


def capacitor_leakage(inst: SMU2657A) -> None:
    """Runs the capacitor leakage test using the SMU2657A device.

    Args:
        inst (SMU2657A): The python driver controlling the SMU2657A unit.
    """
    # Set aliases to improve readability
    smua = inst.commands.smu["a"]
    nvbuffer1 = inst.commands.buffer_var["smua.nvbuffer1"]
    nvbuffer2 = inst.commands.buffer_var["smua.nvbuffer2"]

    # Initialize the SMU
    inst.commands.reset()
    inst.commands.errorqueue.clear()
    inst.commands.status.reset()

    # Configure the reading buffers
    nvbuffer1.clear()
    nvbuffer1.appendmode = 0
    nvbuffer1.collecttimestamps = 1
    nvbuffer1.collectsourcevalues = 0

    nvbuffer2.clear()
    nvbuffer2.appendmode = 0
    nvbuffer2.collecttimestamps = 1
    nvbuffer2.collectsourcevalues = 0

    # Configure source function
    smua.source.func = smua.OUTPUT_DCVOLTS
    smua.source.levelv = LEVEL_V
    smua.source.limiti = LIMIT_I

    # Configure measurement parameters
    smua.measure.autozero = smua.AUTOZERO_ONCE
    smua.measure.rangei = MEAS_RANGE
    smua.measure.count = NUM_READINGS
    smua.measure.nplc = NPLC
    smua.measure.delay = SOAK_TIME

    # Run the test
    smua.source.output = smua.OUTPUT_ON
    smua.measure.iv("smua.nvbuffer1", "smua.nvbuffer2")
    inst.query("waitcomplete() print(1)")
    smua.source.levelv = 0
    smua.source.output = smua.OUTPUT_OFF

    # Find the average voltage, average current, and insulation resistance
    current_stats = smua.buffer.getstats("smua.nvbuffer1")
    current_mean = current_stats["mean"]
    voltage_stats = smua.buffer.getstats("smua.nvbuffer2")
    voltage_mean = voltage_stats["mean"]
    resistance = voltage_mean / current_mean

    # Print the buffer data and the calculated values
    print("Buffer Data (Timestamp/Current/Voltage):")
    inst.print_buffers("smua.nvbuffer1.timestamps", "smua.nvbuffer1", "smua.nvbuffer2")
    print()
    print(f"Average Current: {current_mean}")
    print(f"Avergae Voltage: {voltage_mean}")
    print(f"Insulation Resistance: {resistance}")


with DeviceManager() as DM:
    smu_driver: SMU2657A = DM.add_smu(RESOURCE_ID)  # pyright: ignore[reportAssignmentType]
    capacitor_leakage(smu_driver)
