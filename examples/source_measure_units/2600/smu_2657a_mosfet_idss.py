"""SMU 2657A Example Script: MOSFET Drain to Source Leakage Current Measurement Sweep.

Description:
    This function uses the Model 2657A to sweep the voltage across the drain up to the drain-source
    breakdown voltage and measure the drain current. A second SMU instrument is used to bias the
    gate. For enhancement-mode power MOSFETs, a typical gate bias is 0 V.

Required Equipment:
    1x SMU 2657A
    1x SMU 2600 Series
    1x MOSFET (adjust test parameters to match MOSFET spec)
    1x Model 8010 High Power Device Test Fixture or a Model 2657A-PM-200 Protection Module
    Appropriate cabling to connect the SMUs to the test fixture

Note:
    This test uses high voltage! Ensure your test setup is correct and proper safety measures
    have been taken.

Converted to Python tm_devices script. DCA 6.6.23
"""
from tm_devices import DeviceManager
from tm_devices.drivers import SMU2636B, SMU2657A

SMU1_ID = "192.168.0.1"
SMU2_ID = "192.168.0.2"

GATE_V = 0
GATE_LIMITI = 0.001
DRAIN_V = 0
DRAIN_LIMITI = 500e-6
MEAS_RANGE = 100e-9
MEAS_DELAY = 0.05
NPLC = 1

START_V = 1
STOP_V = 1760
NUM_STEPS = 500
STEP_V = (STOP_V - START_V) / (NUM_STEPS - 1)


with DeviceManager() as DM:
    # Replace the SMU2636B class with the instrument you are using for this test.
    smu2657a: SMU2657A = DM.add_smu(SMU1_ID)  # pyright: ignore[reportAssignmentType]
    smu26xx: SMU2636B = DM.add_smu(SMU2_ID)  # pyright: ignore[reportAssignmentType]

    smua1 = smu2657a.commands.smu["a"]
    smua2 = smu26xx.commands.smu["a"]
    nvbuffer1 = smu2657a.commands.buffer_var["smua.nvbuffer1"]
    nvbuffer2 = smu2657a.commands.buffer_var["smua.nvbuffer2"]

    smu2657a.commands.reset()
    smu26xx.commands.reset()

    # Configure the reading buffers
    nvbuffer1.clear()
    nvbuffer1.appendmode = 1
    nvbuffer1.collecttimestamps = 1

    nvbuffer2.clear()
    nvbuffer2.appendmode = 1
    nvbuffer2.collecttimestamps = 1

    # Configure the Gate SMU
    smua2.source.func = smua2.OUTPUT_DCVOLTS
    smua2.source.levelv = GATE_V
    smua2.source.limiti = GATE_LIMITI

    # Configure the Drain SMU
    smua1.source.func = smua1.OUTPUT_DCVOLTS
    smua1.source.levelv = DRAIN_V
    smua1.source.limiti = DRAIN_LIMITI
    smua1.source.rangev = max(START_V, STOP_V)
    smua1.measure.rangei = MEAS_RANGE
    smua1.measure.delay = MEAS_DELAY
    smua1.measure.nplc = NPLC

    # Run the test
    smua1.source.output = 1
    smua2.source.output = 1

    for i in range(NUM_STEPS):
        smua1.source.levelv = START_V + STEP_V * i
        smua1.measure.iv("smua.nvbuffer1", "smua.nvbuffer2")

        if smua1.source.compliance == "true":
            break

    smua1.source.levelv = 0
    smua2.source.levelv = 0
    smua1.source.output = 0
    smua2.source.output = 0

    print("Results: (Timestamp, Voltage, Current)")
    smu2657a.print_buffers(
        "smua.nvbuffer1.timestamps", "smua.nvbuffer2.readings", "smua.nvbuffer1.readings"
    )
