"""Base Test Script Processing (TSP) control class module."""

from __future__ import annotations

from abc import ABC
from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

from tm_devices.driver_mixins.device_control.pi_control import PIControl
from tm_devices.driver_mixins.shared_implementations.ieee488_2_commands import TSPIEEE4882Commands

if TYPE_CHECKING:
    import os


class TSPControl(PIControl, ABC):
    """Base Test Script Processing (TSP) control class.

    !!! important
        Any class that inherits this control Mixin must also inherit a descendant of the
        [`Device`][tm_devices.drivers.device.Device] class in order to have access to the
        attributes required by this class.
    """

    _IEEE_COMMANDS_CLASS = TSPIEEE4882Commands

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def ieee_cmds(self) -> TSPIEEE4882Commands:
        """Return an internal class containing methods for the standard IEEE 488.2 command set."""
        return self._ieee_cmds  # pyright: ignore[reportReturnType]

    ################################################################################################
    # Public Methods
    ################################################################################################
    def export_buffers(self, filepath: str, *args: str, sep: str = ",") -> None:
        """Export one or more of the device's buffers to the given filepath.

        Args:
            filepath: A string representing the path of the file to write to.
            args: The buffer name(s) to export.
            sep: The delimiter used to separate data. Defaults to ",".
        """
        with open(filepath, mode="w", encoding="utf-8") as file:
            buffer_data = self.get_buffers(*args)
            column_length = max(len(x) for x in buffer_data.values())
            file.write(sep.join(buffer_data) + "\n")
            for index in range(column_length):
                file.write(
                    sep.join(
                        [str(ls[index]) if index < len(ls) else "" for ls in buffer_data.values()]
                    )
                    + "\n"
                )

    def get_buffers(self, *args: str) -> Dict[str, List[float]]:
        """Get the contents of one or more buffers on the device.

        Args:
            args: The buffer name(s) to get.

        Returns:
            A dictionary containing each of the buffers name, and the contents of the buffer.
        """
        buffer_attributes = (  # These attributes use bufferVar.n, not bufferVar.attribute.n
            ".dates",
            ".extraformattedvalues",
            ".extravalues",
            ".extravalueunits",
            ".formattedreadings",
            ".fractionalseconds",
            ".measurefunctions",
            ".measureranges",
            ".readings",
            ".relativetimestamps",
            ".seconds",
            ".sourceformattedvalues",
            ".sourcefunctions",
            ".sourceoutputstates",
            ".sourceranges",
            ".sourcestatuses",
            ".sourceunits",
            ".sourcevalues",
            ".statuses",
            ".times",
            ".timestamps",
            ".units",
        )

        buffer_data: Dict[str, List[float]] = {}
        for buffer_name in args:
            buffer_size_name = buffer_name
            for attr_name in buffer_attributes:
                if buffer_name.endswith(attr_name):
                    buffer_size_name = buffer_name.rstrip(attr_name)
                    break
            buffer_str = self.query(f"printbuffer(1, {buffer_size_name}.n, {buffer_name})")
            buffer_data[buffer_name] = [float(x) for x in buffer_str.split(", ") if buffer_str]
        return buffer_data

    def load_script(
        self,
        script_name: str,
        *,
        script_body: str = "",
        file_path: Union[str, os.PathLike[str], None] = None,
        run_script: bool = False,
        to_nv_memory: bool = False,
    ) -> None:
        """Upload a TSP script to the instrument.

        Args:
            script_name: A string indicating what to name the script being loaded on the instrument.
            script_body: TSP content to load on the instrument, overwritten if `file_path` defined.
            file_path: a *.tsp file from the local filesystem to read and use as the `script_body`.
            run_script: Boolean indicating if the script should be run immediately after loading.
            to_nv_memory: Boolean indicating if the script is to be saved to non-volatile memory.
        """
        if file_path is not None:
            # script_body argument is overwritten by file contents
            with open(file_path, encoding="utf-8") as script_tsp:
                script_body = script_tsp.read().strip()

        # Check if the script exists, delete it if it does
        self.write(f"if {script_name} ~= nil then script.delete('{script_name}') end")

        # Load the script
        self.write(f"loadscript {script_name}\n{script_body}\nendscript")

        # Save to Non-Volatile Memory (script definition survives power cycle)
        if to_nv_memory:
            self.write(f"{script_name}.save()")

        if run_script:
            self.run_script(script_name)

    def print_buffers(self, *args: str) -> None:
        """Print one of more of the device's buffers to the console.

        Args:
            args: The buffer name(s) to print.
        """
        buffer_data = self.get_buffers(*args)
        # Get the largest buffer size
        column_length = max(len(x) for x in buffer_data.values())
        column_widths = {  # Get the largest width value of each column
            k: max(len(k), *[len(str(x)) for x in v]) for k, v in buffer_data.items()
        }

        def fix_width(key: str, value: Any) -> str:  # Function to add spaces if needed
            return str(value) + " " * (column_widths[key] - len(str(value)))

        print(*[fix_width(x, x) for x in buffer_data])
        for index in range(column_length):
            print(
                *[fix_width(k, v[index] if index < len(v) else "") for k, v in buffer_data.items()]
            )

    def run_script(self, script_name: str) -> None:
        """Run a TSP script on the instrument.

        Args:
            script_name: String indicating the name to of the script to run.
        """
        self.write(f"{script_name}()")

    def set_and_check(  # noqa: PLR0913
        self,
        command: str,
        value: Union[str, float],
        tolerance: float = 0,
        percentage: bool = False,
        remove_quotes: bool = False,
        custom_message_prefix: str = "",
        *,
        expected_value: Optional[Union[str, float]] = None,
        opc: bool = False,
    ) -> str:
        """Send the given command with the given value and then verify the results.

        Args:
            command: The command to send.
                For example: ``smu.output.level``
            value: The value being set by the command.
                For example: ``10.0``
            tolerance: The acceptable difference between two floating point values.
            percentage: A boolean indicating what kind of tolerance check to perform.
                False means absolute tolerance: +/- tolerance.
                True means percent tolerance: +/- (tolerance / 100) * value.
            remove_quotes: Set this to True to remove all double quotes from the returned value.
            custom_message_prefix: A custom message to be prepended to the failure message.
            expected_value: An optional, alternative value expected to be returned.
            opc: Boolean indicating if ``*OPC?`` should be queried after sending the command.

        Returns:
            The output of the query portion of the method.
        """
        self.write(f"{command} = {value}", opc=opc)
        if self._enable_verification:
            check = self.query("print(" + command + ")", remove_quotes=remove_quotes)
            message_prefix = f"Failed to set {command} to {value}"
            if custom_message_prefix:
                message_prefix = f"{custom_message_prefix}\n{message_prefix}"
            self.verify_values(
                value if expected_value is None else expected_value,
                check,
                tolerance=tolerance,
                percentage=percentage,
                custom_message_prefix=message_prefix,
                log_error=True,
            )
        else:
            check = ""
        return check


################################################################################################
# Private Methods
################################################################################################
