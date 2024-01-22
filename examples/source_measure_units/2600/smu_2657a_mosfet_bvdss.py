"""SMU 2657A Example Script: MOSFET Drain-Source Breakdown Voltage Test.

Description:
    This test uses the SMU 2657A to force a current from the MOSFET's drain to its source. The SMU
    will measure the resulting voltage with the FET channel turned off. A second instrument applies
    the gate to source voltage to ensure that the gate is turned off.

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
GATE_LIMITI = 0.01
DRAIN_I = 0.001
DRAIN_LIMITV = 30
NPLC = 1
MEAS_DELAY = 0.01

with DeviceManager(verbose=False) as DM:
    # Replace the SMU2636B class with the instrument you are using for this test.
    smu2657a: SMU2657A = DM.add_smu(SMU1_ID)  # pyright: ignore[reportAssignmentType]
    smu26xx: SMU2636B = DM.add_smu(SMU2_ID)  # pyright: ignore[reportAssignmentType]

    smua1 = smu2657a.commands.smu["a"]
    smua2 = smu26xx.commands.smu["a"]

    smu2657a.commands.reset()
    smu26xx.commands.reset()

    # Configure the Gate SMU
    smua2.source.func = smua2.OUTPUT_DCVOLTS
    smua2.source.levelv = GATE_V
    smua2.source.limiti = GATE_LIMITI

    # Configure the Drain SMU
    smua1.source.func = smua1.OUTPUT_DCAMPS
    smua1.source.rangei = DRAIN_I
    smua1.source.leveli = DRAIN_I
    smua1.source.limitv = DRAIN_LIMITV
    smua1.measure.rangev = DRAIN_LIMITV
    smua1.measure.nplc = NPLC
    smua1.measure.delay = MEAS_DELAY

    # Run the test
    smua2.source.output = 1
    smua1.source.output = 1

    print("Test Current:", "Measured Voltage:", sep="\t")
    print(str(smua1.measure.iv()))

    smua1.source.output = 0
    smua2.source.output = 0
