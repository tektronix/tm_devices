"""Linear voltage sweep to measure the reverse leakage of a diode."""

import math

from time import sleep
from typing import List, TYPE_CHECKING

from tm_devices import DeviceManager

if TYPE_CHECKING:
    from tm_devices.drivers import SMU2657A


def dioderl_swp(  # noqa: PLR0915
    vstart: float, vstop: float, vstep: float, irange: str, ilimit: float, source_delay: float
) -> None:
    """Linear voltage sweep to measure the reverse leakage of a diode.

    This function uses the trigger model and built-in sweeping function to create a linear
        voltage sweep to measure the reverse leakage of a diode.
    Using this method is useful when there is a need to send or receive external triggers from
        another instrument or device handler.

    Args:
        vstart: The starting voltage of the diode reverse voltage sweep.
        vstop: The stopping voltage of the diode reverse voltage sweep.
        vstep: The step voltage of the diode reverse voltage sweep
            (how much the voltage changes per step).
        irange: current measurement range, set to value or set to "auto" to enable autorange.
        ilimit: The current limit of the voltage source.
        source_delay: The delay between the start of source and the source complete event.
    """
    with DeviceManager() as dev_man:
        smu2657a: SMU2657A = dev_man.add_smu(  # pyright: ignore[reportAssignmentType]
            address="TCPIP::0.0.0.0::inst0::INSTR", alias="my2657a"
        )  # 192.168.0.2
        # Reset and initialize instrument
        smu2657a.reset()
        smu2657a.commands.status.reset()
        smu2657a.commands.errorqueue.clear()

        smua = smu2657a.commands.smu["a"]
        # Configure source function as 2W DCVOLTS

        smua.source.func = smua.OUTPUT_DCVOLTS
        smua.sense = smua.SENSE_LOCAL

        # Define a local variable to store the number of points in the sweep
        # Calculate the number of points in the sweep based on the start and stop values
        l_num_points = math.floor(abs((vstop - vstart) / vstep)) + 1

        # Set up source range
        if abs(vstart) > abs(vstop):
            smua.source.rangev = vstart
        else:
            smua.source.rangev = vstop

        # Set up source delay
        smua.source.delay = source_delay

        # Set up current compliance
        smua.source.limiti = ilimit

        # Set up current measurement range
        if irange == "auto":
            smua.measure.autorangei = smua.AUTORANGE_ON
        else:
            smua.measure.autorangei = smua.AUTORANGE_OFF
            smua.measure.rangei = irange

        # Set the integration time
        smua.measure.nplc = 1

        # Configure the reading buffers
        smu2657a.commands.buffer_var["smua.nvbuffer1"].clear()
        smu2657a.commands.buffer_var["smua.nvbuffer1"].appendmode = 0
        smu2657a.commands.buffer_var["smua.nvbuffer1"].collecttimestamps = 1
        smu2657a.commands.buffer_var["smua.nvbuffer1"].collectsourcevalues = 0
        smu2657a.commands.buffer_var["smua.nvbuffer1"].fillmode = smua.FILL_ONCE

        smu2657a.commands.buffer_var["smua.nvbuffer2"].clear()
        smu2657a.commands.buffer_var["smua.nvbuffer2"].appendmode = 0
        smu2657a.commands.buffer_var["smua.nvbuffer2"].collecttimestamps = 1
        smu2657a.commands.buffer_var["smua.nvbuffer2"].collectsourcevalues = 0
        smu2657a.commands.buffer_var["smua.nvbuffer2"].fillmode = smua.FILL_ONCE

        # Configure the source lsweep
        smua.trigger.source.linearv(vstart, vstop, l_num_points)
        smua.trigger.source.action = smua.ENABLE
        smua.trigger.source.stimulus = 0

        # Configure measurements during the sweep
        smua.trigger.measure.action = smua.ENABLE
        smua.trigger.measure.stimulus = 0
        smua.trigger.measure.iv(
            "smua.nvbuffer1",
            "smua.nvbuffer2",
        )

        # Configure trigger model parameters
        smua.trigger.count = l_num_points
        smua.trigger.arm.count = 1

        # Turn on the output
        smua.source.output = 1
        # Initiate the sweep and wait until sweep is complete before proceeding to next command
        # Start the trigger model execution
        bit = 8
        smu2657a.commands.smu["a"].trigger.initiate()
        is_sweeping = 9999
        while (is_sweeping and bit) == bit:
            sleep(0.25)
            is_sweeping = float(
                smu2657a.commands.status.operation.instrument.smu["a"].condition.rstrip()
            )
        # Turn off the output
        smua.source.output = 0

        def print_data() -> None:
            t_stamp: List[float] = []
            curr: List[float] = []
            volt: List[float] = []
            rdg_cnt: int
            if not (rdg_cnt := int(float(smu2657a.commands.buffer_var["smua.nvbuffer1"].n))):
                print("No readings in buffer")
            else:
                for cnt in range(1, rdg_cnt + 1):
                    t_stamp.append(
                        float(smu2657a.commands.buffer_var["smua.nvbuffer1"].timestamps[cnt])
                    )
                    curr.append(float(smu2657a.commands.buffer_var["smua.nvbuffer1"].readings[cnt]))
                    volt.append(float(smu2657a.commands.buffer_var["smua.nvbuffer2"].readings[cnt]))
                print("Timestamps\tCurrent\tVoltage")
                for cnt in range(1, rdg_cnt + 1):
                    print(f"{t_stamp[cnt - 1]:.6f}\t{curr[cnt - 1]:+f}\t{volt[cnt - 1]:+f}")

        print_data()


dioderl_swp(0, 100, 11.5, "100e-9", 0.01, 0.05)
