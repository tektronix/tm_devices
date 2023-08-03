"""This is an example to do a single DMM Measurement.

This Example does same DMM Readings with no switching
DMM needs to be configured once then a specified number of
readings are taken after being triggered


This will have two setups

Each setup will be doing DCV, 1 NPLC and 10 V range

Single_Measure_1()
Single 3706, no switch cards, reading VIA Analog Backplane, Single reading

Single_Measure_2()
Single 3706, no switch cards, reading VIA Analog Backplane, 5 readings


To Run:
1) Load TSP file to 3706 Memory
    - Select the .tsp file of interest
    - Press the run arrow in Test Script Builder Main Menu

2) Run Program
    - At TSP> prompt in the Instrument Control Panel, type Single_Measure_1() or Single_Measure_2()

Required equipment:
3706 System Switch and Multimeter

Rev: 1-EEB
    1.1-Update Function Names-EEB
"""

from tm_devices import DeviceManager
from tm_devices.drivers import SS3706A

with DeviceManager() as dev_man:
    ss3706a: SS3706A = dev_man.add_ss(
        address="TCPIP::0.0.0.0::inst0::INSTR", alias="my3706a"
    )  # 192.168.0.2

    def single_measure_1() -> None:
        """Single measure with no buffer."""
        ss3706a.reset()  # Reset
        ss3706a.commands.dmm.func = "dmm.DC_VOLTS"  # Set measurement function
        ss3706a.commands.dmm.nplc = 1  # Set NPLC
        ss3706a.commands.dmm.range = 100  # Set Range
        print(ss3706a.commands.dmm.measure())  # Take dmm measure and print reading

    def single_measure_2() -> None:
        """Single measure with buffer."""
        ss3706a.reset()  # Reset
        buffer_name = "reading_buffer"
        ss3706a.write(f"{buffer_name}=dmm.makebuffer(10)")  # configure reading buffer
        ss3706a.commands.dmm.func = "dmm.DC_VOLTS"  # Set measurement function
        ss3706a.commands.dmm.nplc = 1  # set nplc
        ss3706a.commands.dmm.range = 10  # set range
        ss3706a.commands.dmm.measurecount = 5  # set measure count
        ss3706a.commands.dmm.measure(buffer_name)  # trigger measure and store reading in buffer
        buf = ss3706a.commands.printbuffer(1, 5, buffer_name)  # print buffer/retrieve data
        data = [
            float(i) for i in buf.split(",")
        ]  # convert returned data string to a list of floats
        print(data)

        ss3706a.write(f"{buffer_name} = nil")

    # Function Copy and Paste
    single_measure_1()
