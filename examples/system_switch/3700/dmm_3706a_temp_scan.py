"""This Example does a Thermocouple Scan.

Temp_Scan will be doing K T/C Scan

Temp_Scan
Using 3706 with switching card with a CJC on the STP in Slot 1 (3720,3721)

To Run:

From Test Script Builder

1) Load TSP file to 3706 Memory
    - Select the .tsp file of interest
    - Press the run arrow in Test Script Builder Main Menu

2) Run Program
    - At the TSP> prompt in the Instrument Control Panel, type Temp_Scan()

Required equipment:
3706 System Switch and Multimeter
Multiplexer Switch Card with CJC on STP.


Rev: 1-EEB
    1.1-Update Function Names-EEB
"""

from tm_devices import DeviceManager
from tm_devices.drivers import SS3706A

with DeviceManager() as dev_man:
    ss3706a: SS3706A = dev_man.add_ss(
        address="TCPIP::0.0.0.0::inst0::INSTR", alias="my3706a"
    )  # 192.168.0.2

    def temp_scan() -> None:  # create function called Setup_1()
        """Thermocouple scan."""
        ss3706a.reset()  # reset instrument
        buffer_name = "reading_buffer"
        ss3706a.write(f"{buffer_name}=dmm.makebuffer(1000)")
        ss3706a.commands.dmm.func = "dmm.TEMPERATURE"  # set function to Temperature
        ss3706a.commands.dmm.nplc = 1  # set NPLC
        ss3706a.commands.dmm.transducer = "dmm.TEMP_THERMOCOUPLE"  # set sensor to T/C
        ss3706a.commands.dmm.refjunction = (
            "dmm.REF_JUNCTION_INTERNAL"  # set Reference Junction to internal
        )
        ss3706a.commands.dmm.thermocouple = "dmm.THERMOCOUPLE_K"  # set T/C to K
        ss3706a.write("dmm.units = dmm.UNITS_FAHRENHEIT")  # set units to F
        ss3706a.write('dmm.configure.set("mytemp")')  # save DMM setting to mytemp
        ss3706a.commands.dmm.setconfig(
            "4001:4005,4017:4021", "mytemp"
        )  # assign mytemp setting to channels
        ss3706a.commands.scan.create('"4001:4005,4017:4021"')  # create scan list
        ss3706a.commands.scan.execute(buffer_name)  # execute scan and save readings to buffer
        buf = ss3706a.commands.printbuffer(1, 10, buffer_name)  # print buffer/retrieve data
        data = [
            float(i) for i in buf.split(",")
        ]  # convert returned data string to a list of floats
        print(data)

        ss3706a.write(
            f"{buffer_name} = nil"
        )  # It's important to release memory when done with it on 3706

    temp_scan()
