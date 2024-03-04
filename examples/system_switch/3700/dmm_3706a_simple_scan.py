"""This Example does some DMM Readings with scanning.

DMM needs to be configured once then a specified number of readings
 are taken.

Each setup will be doing DCV, 1 NPLC and 10 V range

DMM_Simple_Scan()
Using 3706 with switching card in slot 4

To Run:
1) Load TSP file to 3706 Memory
    - Select the .tsp file of interest
    - Press the run arrow in Test Script Builder Main Menu

2) Run Program
    - At the TSP> prompt in the Instrument Control Panel, type DMM_Simple_Scan()

Required equipment:
3706 System Switch and Multimeter
Multiplexer Switch Card

Rev: 1-EEB
    1.1-Updated Function Names-EEB
"""

from tm_devices import DeviceManager
from tm_devices.drivers import SS3706A

with DeviceManager() as dev_man:
    ss3706a: SS3706A = dev_man.add_ss(
        address="TCPIP::0.0.0.0::inst0::INSTR", alias="my3706a"
    )  # 192.168.0.2

    def dmm_simple_scan() -> None:  # Sets up 10 channel scan by saving configurations to channels
        """Simple scan with configuration."""
        ss3706a.reset()  # Reset
        buffer_name = "reading_buffer"
        ss3706a.commands.dmm.func = "dmm.DC_VOLTS"  # Set measurement function
        ss3706a.commands.dmm.nplc = 1  # Set NPLC
        ss3706a.commands.dmm.range = 10  # Set Range
        ss3706a.write('dmm.configure.set("mydcvolts")')  # Save Configuration
        ss3706a.commands.dmm.setconfig("4001:4010", "mydcvolts")  # Assign configuration to channels
        ss3706a.commands.scan.create('"4001:4010"')  # create scan
        ss3706a.commands.scan.scancount = 1  # Set Scan Count
        ss3706a.write(f"{buffer_name}=dmm.makebuffer(1000)")  # Configure Buffer
        ss3706a.commands.scan.execute(buffer_name)  # Execute Scan and save to buffer
        buf = ss3706a.commands.printbuffer(1, 10, buffer_name)  # print buffer/retrieve data
        data = [
            float(i) for i in buf.split(",")
        ]  # convert returned data string to a list of floats
        print(data)

        ss3706a.write(
            f"{buffer_name} = nil"
        )  # It's important to release memory when done with it on 3706a

    dmm_simple_scan()
