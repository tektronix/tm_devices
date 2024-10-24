# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The buffer commands module.

These commands are used in the following models:
SMU2460, SMU2461

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - buffer.clearstats()
    - buffer.delete()
    - buffer.getstats()
    - buffer.make()
    - buffer.save()
    - buffer.saveappend()
    - buffer.write.format()
    - buffer.write.reading()
    ```
"""

from typing import Any, Dict, Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class BufferWrite(BaseTSPCmd):
    """The ``buffer.write`` command tree.

    Properties and methods:
        - ``.format()``: The ``buffer.write.format()`` function.
        - ``.reading()``: The ``buffer.write.reading()`` function.
    """

    def format(
        self,
        buffer_var: str,
        units: str,
        display_digits: int,
        extra_units: Optional[str] = None,
        extra_digits: Optional[int] = None,
    ) -> None:
        """Run the ``buffer.write.format()`` function.

        Description:
            - This function sets the units and number of digits of the readings that are written
              into the reading buffer.

        TSP Syntax:
            ```
            - buffer.write.format()
            ```

        Args:
            buffer_var: The name of the buffer.
            units: The units for the first measurement in the buffer index.
            display_digits: The number of digits to use for the first measurement.
            extra_units (optional): The units for the second measurement in the buffer index; the
                selections are the same as units (only valid for buffer style WRITABLE_FULL); if not
                specified, uses the value for units.
            extra_digits (optional): The number of digits to use for the second measurement; the
                selections are the same as displayDigits (only valid for buffer style
                WRITABLE_FULL); if not specified, uses the value for displayDigits.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    buffer_var,
                    units,
                    display_digits,
                    extra_units,
                    extra_digits,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.format({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.format()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def reading(
        self,
        buffer_var: str,
        reading_value: str,
        extra_value: Optional[str] = None,
        seconds: Optional[str] = None,
        fractional_seconds: Optional[str] = None,
        status: Optional[str] = None,
    ) -> None:
        """Run the ``buffer.write.reading()`` function.

        Description:
            - This function allows you to write readings into the reading buffer.

        TSP Syntax:
            ```
            - buffer.write.reading()
            ```

        Args:
            buffer_var: The name of the buffer.
            reading_value: The first value that is recorded in the buffer index.
            extra_value (optional): A second value that is recorded in the buffer index (only valid
                for buffer style WRITABLE_FULL).
            seconds (optional): An integer that represents the seconds.
            fractional_seconds (optional): The portion of the time that represents the fractional
                seconds.
            status (optional): Additional information about the reading; see Details.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    buffer_var,
                    reading_value,
                    extra_value,
                    seconds,
                    fractional_seconds,
                    status,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.reading({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.reading()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class Buffer(BaseTSPCmd):
    """The ``buffer`` command tree.

    Constants:
        - ``.COL_ALL``: Save all data from the specified reading buffer.
        - ``.COL_BRIEF``: Save reading and relative time data from the specified reading buffer.
        - ``.COL_DISPLAY_DIGITS``: Save display digits from the specified reading buffer.
        - ``.COL_EXTRA``: Relative time and additional values if they exist (such as the sense
          voltage from a dc voltage ratio measurement).
        - ``.COL_EXTRA_RANGE``: Save sxtra value range digits from the specified reading buffer.
        - ``.COL_EXTRA_UNIT``: Save extra value units from the specified reading buffer.
        - ``.COL_EXTRA_VALUE``: Save extra values from the specified reading buffer.
        - ``.COL_INDEX``: Save index into buffer from the specified reading buffer.
        - ``.COL_LIMITS``: The status of all limits.
        - ``.COL_MATH``: Math enabled (F is math is not enabled; T if math is enabled) and relative
          time.
        - ``.COL_ORIGIN``: Save origin status from the specified reading buffer.
        - ``.COL_QUESTIONABLE``: Save questionable status from the specified reading buffer.
        - ``.COL_RANGE_DIGITS``: Save range digits from the specified reading buffer.
        - ``.COL_READING``: Save the measurement reading from the specified reading buffer.
        - ``.COL_STANDARD``: Save the relative time, reading, channel, and source value from the
          specified reading buffer.
        - ``.COL_START``: Save the status of the start group from the specified reading buffer.
        - ``.COL_STATUS``: Save the status information associated with the measurement from the
          specified reading buffer.
        - ``.COL_TERMINAL``: Save the terminal status from the specified reading buffer.
        - ``.COL_TIMESTAMP_READING``: Save the timestamp reading from the specified reading buffer.
        - ``.COL_TIME_ABSOLUTE``: Save the time when the data point was measured as an absolute from
          the specified reading buffer.
        - ``.COL_TIME_PARTS``: Save absolute time in multiple columns from the specified reading
          buffer.
        - ``.COL_TIME_RAW``: Save absolute time in seconds from the specified reading buffer.
        - ``.COL_TIME_RELATIVE``: Save the relative time when the data point was measured in seconds
          from the specified reading buffer.
        - ``.COL_UNIT``: Save the reading and the unit of measure from the specified reading buffer.
        - ``.DIGITS_3_5``: The number of digits to use for the  first measurement.
        - ``.DIGITS_4_5``: The number of digits to use for the  first measurement.
        - ``.DIGITS_5_5``: The number of digits to use for the  first measurement.
        - ``.DIGITS_6_5``: The number of digits to use for the  first measurement.
        - ``.DIGITS_7_5``: The number of digits to use for the  first measurement.
        - ``.DIGITS_8_5``: The number of digits to use for the  first measurement.
        - ``.EXPR_ADD``: Add the present and previous measurements.
        - ``.EXPR_AVERAGE``: Average the present and previous measurements.
        - ``.EXPR_DIVIDE``: Divide the present reading by the previous reading.
        - ``.EXPR_EXPONENT``: Exponent (10^present reading).
        - ``.EXPR_LOG10``: Log10 (log10(present reading)).
        - ``.EXPR_MULTIPLY``: Multiply the present and previous measurements.
        - ``.EXPR_NONE``: Remove the math expression.
        - ``.EXPR_POLY``: Polynomial where r is present reading and c is constant.
        - ``.EXPR_POWER``: Present reading raised to power of defined constant.
        - ``.EXPR_RATE``: Rate of change (present reading - previous reading)/(timestamp of present
          reading - timestamp of previous reading).
        - ``.EXPR_RECIPROCAL``: Reciprocal (1/present reading).
        - ``.EXPR_SQROOT``: Square root of the present reading.
        - ``.EXPR_SUBTRACT``: Present reading - previous reading.
        - ``.FILL_CONTINUOUS``: Fill the buffer continuously.
        - ``.FILL_ONCE``: Fill the buffer, then stop.
        - ``.OFF``: Do not log information events.
        - ``.ON``: Log information events.
        - ``.SAVE_FORMAT_TIME``: Include dates, times, and fractional seconds in the buffer.
        - ``.SAVE_RAW_TIME``: Include seconds and fractional seconds in the buffer.
        - ``.SAVE_RELATIVE_TIME``: Include relative timestamps in the buffer.
        - ``.SAVE_TIMESTAMP_TIME``: Include timestamps in the buffer.
        - ``.STAT_LIMIT``: Source function level was limited.
        - ``.STAT_LIMIT1_HIGH``: Reading is above high limit 1.
        - ``.STAT_LIMIT1_LOW``: Reading is below low limit 1.
        - ``.STAT_LIMIT2_HIGH``: Reading is above high limit 2.
        - ``.STAT_LIMIT2_LOW``: Reading is below low limit 2.
        - ``.STAT_ORIGIN``: A/D converter from which reading originated; for most instruments, this
          will always be 0 (main). For digitizing instruments, can be 2 (digitize).
        - ``.STAT_OUTPUT``: Output was on.
        - ``.STAT_OVER_TEMP``: Overtemperature condition was active.
        - ``.STAT_PROTECTION``: Overvoltage protection was active.
        - ``.STAT_QUESTIONABLE``: Measure status questionable.
        - ``.STAT_READBACK``: Measured source value was read.
        - ``.STAT_REL``: Relative offset.
        - ``.STAT_SCAN``: Scan.
        - ``.STAT_SENSE``: Four-wire sense was used.
        - ``.STAT_START_GROUP``: First reading in a group.
        - ``.STAT_TERMINAL``: Measure terminal, front is 1, rear is 0.
        - ``.STYLE_COMPACT``: Store readings with reduced accuracy (6.5 digits) with no formatting
          information, 1 μs accurate timestamp.
        - ``.STYLE_FULL``: Store the same information with full accuracy with formatting, plus
          additional information.
        - ``.STYLE_STANDARD``: Store readings with full accuracy with formatting.
        - ``.STYLE_WRITABLE``: Store external reading buffer data.
        - ``.STYLE_WRITABLE_FULL``: Store external reading buffer data with two reading values.
        - ``.UNIT_AMP``: Set units of measure to dc current.
        - ``.UNIT_AMP_AC``: Set units of measure to ac current.
        - ``.UNIT_CELSIUS``: Set units of measure to Celsius.
        - ``.UNIT_CUSTOM1``: Custom unit 1 (defined by buffer.unit()).
        - ``.UNIT_CUSTOM2``: Custom unit 2 (defined by buffer.unit()).
        - ``.UNIT_CUSTOM3``: Custom unit 3 (defined by buffer.unit()).
        - ``.UNIT_DAC``: Set units of measure to DAC (voltage).
        - ``.UNIT_DBM``: Set units of measure to decibel-milliwatts.
        - ``.UNIT_DECIBEL``: Set units of measure to decibels.
        - ``.UNIT_DIO``: Set units of measure to digital I/O.
        - ``.UNIT_FAHRENHEIT``: Set units of measure to Fahrenheit.
        - ``.UNIT_FARAD``: Set units of measure to capacitance.
        - ``.UNIT_HERTZ``: Set units of measure to frequency.
        - ``.UNIT_KELVIN``: Set units of measure to Kelvin.
        - ``.UNIT_NONE``: Set units of measure to no units.
        - ``.UNIT_OHM``: Set units of measure to ohms.
        - ``.UNIT_PERCENT``: Set units of measure to percent.
        - ``.UNIT_RATIO``: Set units of measure to dc voltage ratio.
        - ``.UNIT_RECIPROCAL``: Set units of measure to reciprocal.
        - ``.UNIT_SECOND``: Set units of measure to period.
        - ``.UNIT_TOT``: Set units of measure to totalizer.
        - ``.UNIT_VOLT``: Set units of measure to dc voltage.
        - ``.UNIT_VOLT_AC``: Set units of measure to ac voltage.
        - ``.UNIT_WATT``: Set units of measure to watts.
        - ``.UNIT_X``: Set units of measure to buffer.UNIT_X.

    Properties and methods:
        - ``.clearstats()``: The ``buffer.clearstats()`` function.
        - ``.delete()``: The ``buffer.delete()`` function.
        - ``.getstats()``: The ``buffer.getstats()`` function.
        - ``.make()``: The ``buffer.make()`` function.
        - ``.save()``: The ``buffer.save()`` function.
        - ``.saveappend()``: The ``buffer.saveappend()`` function.
        - ``.write``: The ``buffer.write`` command tree.
    """

    COL_ALL = "buffer.COL_ALL"
    """str: Save all data from the specified reading buffer."""
    COL_BRIEF = "buffer.COL_BRIEF"
    """str: Save reading and relative time data from the specified reading buffer."""
    COL_DISPLAY_DIGITS = "buffer.COL_DISPLAY_DIGITS"
    """str: Save display digits from the specified reading buffer."""
    COL_EXTRA = "buffer.COL_EXTRA"
    """str: Relative time and additional values if they exist (such as the sense voltage from a dc voltage ratio measurement)."""  # noqa: E501
    COL_EXTRA_RANGE = "buffer.COL_EXTRA_RANGE"
    """str: Save sxtra value range digits from the specified reading buffer."""
    COL_EXTRA_UNIT = "buffer.COL_EXTRA_UNIT"
    """str: Save extra value units from the specified reading buffer."""
    COL_EXTRA_VALUE = "buffer.COL_EXTRA_VALUE"
    """str: Save extra values from the specified reading buffer."""
    COL_INDEX = "buffer.COL_INDEX"
    """str: Save index into buffer from the specified reading buffer."""
    COL_LIMITS = "buffer.COL_LIMITS"
    """str: The status of all limits."""
    COL_MATH = "buffer.COL_MATH"
    """str: Math enabled (F is math is not enabled; T if math is enabled) and relative time."""
    COL_ORIGIN = "buffer.COL_ORIGIN"
    """str: Save origin status from the specified reading buffer."""
    COL_QUESTIONABLE = "buffer.COL_QUESTIONABLE"
    """str: Save questionable status from the specified reading buffer."""
    COL_RANGE_DIGITS = "buffer.COL_RANGE_DIGITS"
    """str: Save range digits from the specified reading buffer."""
    COL_READING = "buffer.COL_READING"
    """str: Save the measurement reading from the specified reading buffer."""
    COL_STANDARD = "buffer.COL_STANDARD"
    """str: Save the relative time, reading, channel, and source value from the specified reading buffer."""  # noqa: E501
    COL_START = "buffer.COL_START"
    """str: Save the status of the start group from the specified reading buffer."""
    COL_STATUS = "buffer.COL_STATUS"
    """str: Save the status information associated with the measurement from the specified reading buffer."""  # noqa: E501
    COL_TERMINAL = "buffer.COL_TERMINAL"
    """str: Save the terminal status from the specified reading buffer."""
    COL_TIMESTAMP_READING = "buffer.COL_TIMESTAMP_READING"
    """str: Save the timestamp reading from the specified reading buffer."""
    COL_TIME_ABSOLUTE = "buffer.COL_TIME_ABSOLUTE"
    """str: Save the time when the data point was measured as an absolute from the specified reading buffer."""  # noqa: E501
    COL_TIME_PARTS = "buffer.COL_TIME_PARTS"
    """str: Save absolute time in multiple columns from the specified reading buffer."""
    COL_TIME_RAW = "buffer.COL_TIME_RAW"
    """str: Save absolute time in seconds from the specified reading buffer."""
    COL_TIME_RELATIVE = "buffer.COL_TIME_RELATIVE"
    """str: Save the relative time when the data point was measured in seconds from the specified reading buffer."""  # noqa: E501
    COL_UNIT = "buffer.COL_UNIT"
    """str: Save the reading and the unit of measure from the specified reading buffer."""
    DIGITS_3_5 = "buffer.DIGITS_3_5"
    """str: The number of digits to use for the  first measurement."""
    DIGITS_4_5 = "buffer.DIGITS_4_5"
    """str: The number of digits to use for the  first measurement."""
    DIGITS_5_5 = "buffer.DIGITS_5_5"
    """str: The number of digits to use for the  first measurement."""
    DIGITS_6_5 = "buffer.DIGITS_6_5"
    """str: The number of digits to use for the  first measurement."""
    DIGITS_7_5 = "buffer.DIGITS_7_5"
    """str: The number of digits to use for the  first measurement."""
    DIGITS_8_5 = "buffer.DIGITS_8_5"
    """str: The number of digits to use for the  first measurement."""
    EXPR_ADD = "buffer.EXPR_ADD"
    """str: Add the present and previous measurements."""
    EXPR_AVERAGE = "buffer.EXPR_AVERAGE"
    """str: Average the present and previous measurements."""
    EXPR_DIVIDE = "buffer.EXPR_DIVIDE"
    """str: Divide the present reading by the previous reading."""
    EXPR_EXPONENT = "buffer.EXPR_EXPONENT"
    """str: Exponent (10^present reading)."""
    EXPR_LOG10 = "buffer.EXPR_LOG10"
    """str: Log10 (log10(present reading))."""
    EXPR_MULTIPLY = "buffer.EXPR_MULTIPLY"
    """str: Multiply the present and previous measurements."""
    EXPR_NONE = "buffer.EXPR_NONE"
    """str: Remove the math expression."""
    EXPR_POLY = "buffer.EXPR_POLY"
    """str: Polynomial where r is present reading and c is constant."""
    EXPR_POWER = "buffer.EXPR_POWER"
    """str: Present reading raised to power of defined constant."""
    EXPR_RATE = "buffer.EXPR_RATE"
    """str: Rate of change (present reading - previous reading)/(timestamp of present reading - timestamp of previous reading)."""  # noqa: E501
    EXPR_RECIPROCAL = "buffer.EXPR_RECIPROCAL"
    """str: Reciprocal (1/present reading)."""
    EXPR_SQROOT = "buffer.EXPR_SQROOT"
    """str: Square root of the present reading."""
    EXPR_SUBTRACT = "buffer.EXPR_SUBTRACT"
    """str: Present reading - previous reading."""
    FILL_CONTINUOUS = "buffer.FILL_CONTINUOUS"
    """str: Fill the buffer continuously."""
    FILL_ONCE = "buffer.FILL_ONCE"
    """str: Fill the buffer, then stop."""
    OFF = "buffer.OFF"
    """str: Do not log information events."""
    ON = "buffer.ON"
    """str: Log information events."""
    SAVE_FORMAT_TIME = "buffer.SAVE_FORMAT_TIME"
    """str: Include dates, times, and fractional seconds in the buffer."""
    SAVE_RAW_TIME = "buffer.SAVE_RAW_TIME"
    """str: Include seconds and fractional seconds in the buffer."""
    SAVE_RELATIVE_TIME = "buffer.SAVE_RELATIVE_TIME"
    """str: Include relative timestamps in the buffer."""
    SAVE_TIMESTAMP_TIME = "buffer.SAVE_TIMESTAMP_TIME"
    """str: Include timestamps in the buffer."""
    STAT_LIMIT = "buffer.STAT_LIMIT"
    """str: Source function level was limited."""
    STAT_LIMIT1_HIGH = "buffer.STAT_LIMIT1_HIGH"
    """str: Reading is above high limit 1."""
    STAT_LIMIT1_LOW = "buffer.STAT_LIMIT1_LOW"
    """str: Reading is below low limit 1."""
    STAT_LIMIT2_HIGH = "buffer.STAT_LIMIT2_HIGH"
    """str: Reading is above high limit 2."""
    STAT_LIMIT2_LOW = "buffer.STAT_LIMIT2_LOW"
    """str: Reading is below low limit 2."""
    STAT_ORIGIN = "buffer.STAT_ORIGIN"
    """str: A/D converter from which reading originated; for most instruments, this will always be 0 (main). For digitizing instruments, can be 2 (digitize)."""  # noqa: E501
    STAT_OUTPUT = "buffer.STAT_OUTPUT"
    """str: Output was on."""
    STAT_OVER_TEMP = "buffer.STAT_OVER_TEMP"
    """str: Overtemperature condition was active."""
    STAT_PROTECTION = "buffer.STAT_PROTECTION"
    """str: Overvoltage protection was active."""
    STAT_QUESTIONABLE = "buffer.STAT_QUESTIONABLE"
    """str: Measure status questionable."""
    STAT_READBACK = "buffer.STAT_READBACK"
    """str: Measured source value was read."""
    STAT_REL = "buffer.STAT_REL"
    """str: Relative offset."""
    STAT_SCAN = "buffer.STAT_SCAN"
    """str: Scan."""
    STAT_SENSE = "buffer.STAT_SENSE"
    """str: Four-wire sense was used."""
    STAT_START_GROUP = "buffer.STAT_START_GROUP"
    """str: First reading in a group."""
    STAT_TERMINAL = "buffer.STAT_TERMINAL"
    """str: Measure terminal, front is 1, rear is 0."""
    STYLE_COMPACT = "buffer.STYLE_COMPACT"
    """str: Store readings with reduced accuracy (6.5 digits) with no formatting information, 1 μs accurate timestamp."""  # noqa: E501
    STYLE_FULL = "buffer.STYLE_FULL"
    """str: Store the same information with full accuracy with formatting, plus additional information."""  # noqa: E501
    STYLE_STANDARD = "buffer.STYLE_STANDARD"
    """str: Store readings with full accuracy with formatting."""
    STYLE_WRITABLE = "buffer.STYLE_WRITABLE"
    """str: Store external reading buffer data."""
    STYLE_WRITABLE_FULL = "buffer.STYLE_WRITABLE_FULL"
    """str: Store external reading buffer data with two reading values."""
    UNIT_AMP = "buffer.UNIT_AMP"
    """str: Set units of measure to dc current."""
    UNIT_AMP_AC = "buffer.UNIT_AMP_AC"
    """str: Set units of measure to ac current."""
    UNIT_CELSIUS = "buffer.UNIT_CELSIUS"
    """str: Set units of measure to Celsius."""
    UNIT_CUSTOM1 = "buffer.UNIT_CUSTOM1"
    """str: Custom unit 1 (defined by buffer.unit())."""
    UNIT_CUSTOM2 = "buffer.UNIT_CUSTOM2"
    """str: Custom unit 2 (defined by buffer.unit())."""
    UNIT_CUSTOM3 = "buffer.UNIT_CUSTOM3"
    """str: Custom unit 3 (defined by buffer.unit())."""
    UNIT_DAC = "buffer.UNIT_DAC"
    """str: Set units of measure to DAC (voltage)."""
    UNIT_DBM = "buffer.UNIT_DBM"
    """str: Set units of measure to decibel-milliwatts."""
    UNIT_DECIBEL = "buffer.UNIT_DECIBEL"
    """str: Set units of measure to decibels."""
    UNIT_DIO = "buffer.UNIT_DIO"
    """str: Set units of measure to digital I/O."""
    UNIT_FAHRENHEIT = "buffer.UNIT_FAHRENHEIT"
    """str: Set units of measure to Fahrenheit."""
    UNIT_FARAD = "buffer.UNIT_FARAD"
    """str: Set units of measure to capacitance."""
    UNIT_HERTZ = "buffer.UNIT_HERTZ"
    """str: Set units of measure to frequency."""
    UNIT_KELVIN = "buffer.UNIT_KELVIN"
    """str: Set units of measure to Kelvin."""
    UNIT_NONE = "buffer.UNIT_NONE"
    """str: Set units of measure to no units."""
    UNIT_OHM = "buffer.UNIT_OHM"
    """str: Set units of measure to ohms."""
    UNIT_PERCENT = "buffer.UNIT_PERCENT"
    """str: Set units of measure to percent."""
    UNIT_RATIO = "buffer.UNIT_RATIO"
    """str: Set units of measure to dc voltage ratio."""
    UNIT_RECIPROCAL = "buffer.UNIT_RECIPROCAL"
    """str: Set units of measure to reciprocal."""
    UNIT_SECOND = "buffer.UNIT_SECOND"
    """str: Set units of measure to period."""
    UNIT_TOT = "buffer.UNIT_TOT"
    """str: Set units of measure to totalizer."""
    UNIT_VOLT = "buffer.UNIT_VOLT"
    """str: Set units of measure to dc voltage."""
    UNIT_VOLT_AC = "buffer.UNIT_VOLT_AC"
    """str: Set units of measure to ac voltage."""
    UNIT_WATT = "buffer.UNIT_WATT"
    """str: Set units of measure to watts."""
    UNIT_X = "buffer.UNIT_X"
    """str: Set units of measure to buffer.UNIT_X."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "buffer") -> None:
        super().__init__(device, cmd_syntax)
        self._write = BufferWrite(device, f"{self._cmd_syntax}.write")

    @property
    def write(self) -> BufferWrite:
        """Return the ``buffer.write`` command tree.

        Sub-properties and sub-methods:
            - ``.format()``: The ``buffer.write.format()`` function.
            - ``.reading()``: The ``buffer.write.reading()`` function.
        """
        return self._write

    def clearstats(self, buffer_var: Optional[str] = None) -> None:
        """Run the ``buffer.clearstats()`` function.

        Description:
            - This function clears the statistical information associated with the specified buffer.

        TSP Syntax:
            ```
            - buffer.clearstats()
            ```

        Args:
            buffer_var (optional): The name of the reading buffer, which may be a default buffer
                (defbuffer1 or defbuffer2) or a user-defined buffer; defaults to defbuffer1 if not
                specified.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (buffer_var,) if x is not None)
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.clearstats({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.clearstats()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def delete(self, buffer_name: str) -> None:
        """Run the ``buffer.delete()`` function.

        Description:
            - This function deletes a user-defined reading buffer.

        TSP Syntax:
            ```
            - buffer.delete()
            ```

        Args:
            buffer_name: The name of a user-defined reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.delete({buffer_name})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.delete()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getstats(
        self,
        buffer_var: Optional[str] = None,
        rel_start_time: Optional[str] = None,
        rel_end_time: Optional[str] = None,
    ) -> Dict[Any, Any]:
        """Run the ``buffer.getstats()`` function.

        Description:
            - This function returns statistics from a specified reading buffer.

        TSP Syntax:
            ```
            - buffer.getstats()
            ```

        Args:
            buffer_var (optional): The name of the reading buffer, which may be a default buffer
                (defbuffer1 or defbuffer2) or a user-defined buffer; if no buffer is specified, this
                parameter defaults to defbuffer1.
            rel_start_time (optional): The start time in seconds relative to the start time of the
                data in the buffer.
            rel_end_time (optional): The end time in seconds relative to the start time of the data
                in the buffer.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    buffer_var,
                    rel_start_time,
                    rel_end_time,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"tempvar = {self._cmd_syntax}.getstats({function_args})"
            )
            retval = self._get_tsp_table_dict("tempvar")
            self._device.write("tempvar = nil")  # type: ignore[union-attr]
            return retval  # noqa: TRY300
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getstats()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def make(self, buffer_size: int, style: Optional[str] = None) -> str:
        """Run the ``buffer.make()`` function.

        Description:
            - This function creates a user-defined reading buffer.

        TSP Syntax:
            ```
            - buffer.make()
            ```

        Args:
            buffer_size: The maximum number of readings that can be stored in bufferVar; minimum is
                10; 0 to maximize buffer size (see Details).
            style (optional): The type of reading buffer to create.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    buffer_size,
                    style,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.make({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.make()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def save(
        self,
        buffer_var: str,
        file_name: str,
        what: Optional[str] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
    ) -> None:
        """Run the ``buffer.save()`` function.

        Description:
            - This function saves data from the specified reading buffer to a USB flash drive.

        TSP Syntax:
            ```
            - buffer.save()
            ```

        Args:
            buffer_var: The name of the reading buffer, which may be a default buffer (defbuffer1 or
                defbuffer2) or a user-defined buffer.
            file_name: A string that indicates the name of the file on the USB flash drive in which
                to save the reading buffer.
            what (optional): Defines which information is saved in the file on the USB flash drive.
            start (optional): Defines the starting point in the buffer to start saving data.
            end (optional): Defines the ending point in the buffer to stop saving data.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    buffer_var,
                    f'"{file_name}"',
                    what,
                    start,
                    end,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.save({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.save()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def saveappend(
        self,
        buffer_var: str,
        file_name: str,
        time_format: Optional[str] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
    ) -> None:
        """Run the ``buffer.saveappend()`` function.

        Description:
            - This function appends data from the reading buffer to a file on the USB flash drive.

        TSP Syntax:
            ```
            - buffer.saveappend()
            ```

        Args:
            buffer_var: Indicates the reading buffer to use; the default buffers (defbuffer1 or
                defbuffer2) or the name of a user-defined buffer; if no buffer is specified,
                defbuffer1 is used.
            file_name: A string that indicates the name of the file on the USB flash drive in which
                to save the reading buffer.
            time_format (optional): Indicates how date and time information from the buffer is saved
                in the file on the USB flash drive; the options are.
            start (optional): Defines the starting point in the buffer to start saving data.
            end (optional): Defines the ending point in the buffer to stop saving data.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    buffer_var,
                    f'"{file_name}"',
                    time_format,
                    start,
                    end,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.saveappend({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.saveappend()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
