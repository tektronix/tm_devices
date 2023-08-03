"""This Example does a scan.

It does this with external trigger to pace an internal measure scan
An external trigger signal will also be generated when channel closed

DMM_Ext_Trigger will run the program

DMM_Ext_Trigger
Using 3706 with switching card with a the STP in Slot 1

To Run:

From Test Script Builder

1) Load TSP file to 3706 Memory
    - Select the .tsp file of interest
    - Press the run arrow in Test Script Builder Main Menu

2) Run Program
    - At the TSP> prompt in the Instrument Control Panel, type DMM_Ext_Trigger(1)
        -Pass the number or scans that you want to run.  In the above example 1 is passed

Required equipment:
3706 System Switch and Multimeter
Multiplexer Switch Card with

Rev: 1-EEB
    1.1-Update Function Names-EEB
"""

from tm_devices import DeviceManager
from tm_devices.drivers import SS3706A

with DeviceManager() as dev_man:
    ss3706a: SS3706A = dev_man.add_ss(
        address="TCPIP::0.0.0.0::inst0::INSTR", alias="my3706a"
    )  # 192.168.0.2

    def dmm_ext_trigger(
        scan_count: int,
    ) -> None:  # Function Name that is used to pass the number of scans
        """adsf.

        Args:
            scan_count : number of scans to be taken
        """
        ss3706a.reset()  # Reset
        buffer_name = "reading_buffer"
        ss3706a.write(f"{buffer_name} = dmm.makebuffer(1000)")
        ss3706a.commands.dmm.func = "dmm.DC_VOLTS"  # Set measurement function
        ss3706a.commands.dmm.nplc = 1  # Set NPLC
        ss3706a.commands.dmm.range = 10  # Set Range
        ss3706a.write('dmm.configure.set("mydcvolts")')  # Save Configuration
        ss3706a.commands.dmm.setconfig("4001:4010", "mydcvolts")  # Assign configuration to channels
        # scan.bypass allows unit to fall through the channel stimulus the first time
        # through the trigger model.  This is useful if you have two unit in external trigger
        # mode, one needs to go first to "prime the pump".
        # by turning bypass off, 3706 will wait for a trigger BEFORE taking the first measurement
        ss3706a.commands.scan.bypass = "scan.OFF"  # Turns scan bypass off, it is on by default
        ss3706a.commands.scan.trigger.channel.stimulus = ss3706a.commands.digio.trigger[
            2
        ].EVENT_ID  # Configure Scan Channel Stimulus to Digital [2]
        ss3706a.commands.digio.trigger[
            2
        ].mode = "display.trigger.EVENT_ID"  # Configure Digital I/O line for falling edge input
        ss3706a.commands.digio.trigger[2].clear()  # Clear Digital line 2
        ss3706a.commands.digio.trigger[
            1  # Configure Digital line[1] to scan channel ready output
        ].stimulus = "scan.trigger.EVENT_MEASURE_COMP"
        ss3706a.commands.digio.trigger[
            1
        ].mode = "display.trigger.EVENT_ID"  # Configure Digital I/O line for falling edge output
        ss3706a.commands.digio.trigger[1].pulsewidth = 0.001  # Configure output width
        ss3706a.commands.scan.create('"4001:4010"')  # Create Scan
        ss3706a.commands.scan.scancount = scan_count  # Pass scan count from function call
        ss3706a.commands.scan.execute(buffer_name)  # Execute Scan
        buf = ss3706a.commands.printbuffer(1, 10, buffer_name)  # print buffer/retrieve data
        data = [
            float(i) for i in buf.split(",")
        ]  # convert returned data string to a list of floats
        print(data)

        ss3706a.write(
            f"{buffer_name} = nil"
        )  # It's important to release memory when done with it on 3706

    dmm_ext_trigger(1)
