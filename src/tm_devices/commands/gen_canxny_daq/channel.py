# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The channel commands module.

These commands are used in the following models:
DAQ6510

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - channel.close()
    - channel.getclose()
    - channel.getcommonside()
    - channel.getcount()
    - channel.getcountinterval()
    - channel.getdelay()
    - channel.getdmm()
    - channel.getlabel()
    - channel.getmatch()
    - channel.getmatchtype()
    - channel.getmode()
    - channel.getstate()
    - channel.gettype()
    - channel.getwidth()
    - channel.multiple.close()
    - channel.multiple.open()
    - channel.open()
    - channel.read()
    - channel.setcommonside()
    - channel.setcountinterval()
    - channel.setdelay()
    - channel.setdmm()
    - channel.setlabel()
    - channel.setmatch()
    - channel.setmatchtype()
    - channel.setmode()
    - channel.setwidth()
    - channel.write()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class ChannelMultiple(BaseTSPCmd):
    """The ``channel.multiple`` command tree.

    Properties and methods:
        - ``.close()``: The ``channel.multiple.close()`` function.
        - ``.open()``: The ``channel.multiple.open()`` function.
    """

    def close(self, channel_list: str) -> None:
        """Run the ``channel.multiple.close()`` function.

        Description:
            - This function closes the listed channels without affecting any other channels.

        TSP Syntax:
            ```
            - channel.multiple.close()
            ```

        Args:
            channel_list: The list of channels to close.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.close("{channel_list}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.close()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def open(self, channel_list: str) -> None:
        """Run the ``channel.multiple.open()`` function.

        Description:
            - This function opens the channels in the channel list without affecting any others.

        TSP Syntax:
            ```
            - channel.multiple.open()
            ```

        Args:
            channel_list: A list of the channels to open.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.open("{channel_list}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.open()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


#  pylint: disable=too-many-public-methods
class Channel(BaseTSPCmd):
    """The ``channel`` command tree.

    Constants:
        - ``.COUNT_INTERVAL_10M``: The storage of channel relay closure count is set to 10 minutes.
        - ``.COUNT_INTERVAL_15M``: The storage of channel relay closure count is set to 15 minutes.
        - ``.COUNT_INTERVAL_1M``: The storage of channel relay closure count is set to 1 minute.
        - ``.COUNT_INTERVAL_24H``: The storage of channel relay closure count is set to 24 hours.
        - ``.COUNT_INTERVAL_30M``: The storage of channel relay closure count is set to 30 minutes.
        - ``.COUNT_INTERVAL_5M``: The storage of channel relay closure count is set to 5 minutes.
        - ``.COUNT_INTERVAL_60M``: The storage of channel relay closure count is set to 60 minutes.
        - ``.IND_CLOSED``: Channel is closed.
        - ``.IND_MATCH``: Digital I/O or totalizer channel value is matched.
        - ``.IND_OVERFLOW``: Totalizer channel has overflowed.
        - ``.MATCH_ANY``: For an any match, a match is when the match value equals the channel-read
          value.
        - ``.MATCH_EXACT``: The state match indicator only becomes true when the match value equals
          the channel-read value.
        - ``.MATCH_NONE``: When none is set, matching is disabled.
        - ``.MATCH_UNCHANGED``: For an unchanged match, the value should be the same as the
          original. If not, a match is declared.
        - ``.MODE_FALLING_EDGE``: For totalizer channels, select falling edge.
        - ``.MODE_FALLING_EDGE_READ_RESET``: For totalizer channels, select falling edge, then reset
          the count on read.
        - ``.MODE_INPUT``: Set digital channel to input.
        - ``.MODE_OUTPUT``: Set digital channel to output.
        - ``.MODE_RISING_EDGE``: For totalizer channels, select rising edge.
        - ``.MODE_RISING_EDGE_READ_RESET``: For totalizer channels, select rising edge, then reset
          the count on read.
        - ``.TYPE_BACKPLANE``: Backplane.
        - ``.TYPE_DAC``: DAC channel.
        - ``.TYPE_DIGITAL``: Digital channel.
        - ``.TYPE_POLE``: Pole channel.
        - ``.TYPE_RADIO``: Radio channel.
        - ``.TYPE_SWITCH``: Switch channel.
        - ``.TYPE_TOTALIZER``: Totalizer channel.

    Properties and methods:
        - ``.close()``: The ``channel.close()`` function.
        - ``.getclose()``: The ``channel.getclose()`` function.
        - ``.getcommonside()``: The ``channel.getcommonside()`` function.
        - ``.getcount()``: The ``channel.getcount()`` function.
        - ``.getcountinterval()``: The ``channel.getcountinterval()`` function.
        - ``.getdelay()``: The ``channel.getdelay()`` function.
        - ``.getdmm()``: The ``channel.getdmm()`` function.
        - ``.getlabel()``: The ``channel.getlabel()`` function.
        - ``.getmatch()``: The ``channel.getmatch()`` function.
        - ``.getmatchtype()``: The ``channel.getmatchtype()`` function.
        - ``.getmode()``: The ``channel.getmode()`` function.
        - ``.getstate()``: The ``channel.getstate()`` function.
        - ``.gettype()``: The ``channel.gettype()`` function.
        - ``.getwidth()``: The ``channel.getwidth()`` function.
        - ``.multiple``: The ``channel.multiple`` command tree.
        - ``.open()``: The ``channel.open()`` function.
        - ``.read()``: The ``channel.read()`` function.
        - ``.setcommonside()``: The ``channel.setcommonside()`` function.
        - ``.setcountinterval()``: The ``channel.setcountinterval()`` function.
        - ``.setdelay()``: The ``channel.setdelay()`` function.
        - ``.setdmm()``: The ``channel.setdmm()`` function.
        - ``.setlabel()``: The ``channel.setlabel()`` function.
        - ``.setmatch()``: The ``channel.setmatch()`` function.
        - ``.setmatchtype()``: The ``channel.setmatchtype()`` function.
        - ``.setmode()``: The ``channel.setmode()`` function.
        - ``.setwidth()``: The ``channel.setwidth()`` function.
        - ``.write()``: The ``channel.write()`` function.
    """

    COUNT_INTERVAL_10M = "channel.COUNT_INTERVAL_10M"
    """str: The storage of channel relay closure count is set to 10 minutes."""
    COUNT_INTERVAL_15M = "channel.COUNT_INTERVAL_15M"
    """str: The storage of channel relay closure count is set to 15 minutes."""
    COUNT_INTERVAL_1M = "channel.COUNT_INTERVAL_1M"
    """str: The storage of channel relay closure count is set to 1 minute."""
    COUNT_INTERVAL_24H = "channel.COUNT_INTERVAL_24H"
    """str: The storage of channel relay closure count is set to 24 hours."""
    COUNT_INTERVAL_30M = "channel.COUNT_INTERVAL_30M"
    """str: The storage of channel relay closure count is set to 30 minutes."""
    COUNT_INTERVAL_5M = "channel.COUNT_INTERVAL_5M"
    """str: The storage of channel relay closure count is set to 5 minutes."""
    COUNT_INTERVAL_60M = "channel.COUNT_INTERVAL_60M"
    """str: The storage of channel relay closure count is set to 60 minutes."""
    IND_CLOSED = "channel.IND_CLOSED"
    """str: Channel is closed."""
    IND_MATCH = "channel.IND_MATCH"
    """str: Digital I/O or totalizer channel value is matched."""
    IND_OVERFLOW = "channel.IND_OVERFLOW"
    """str: Totalizer channel has overflowed."""
    MATCH_ANY = "channel.MATCH_ANY"
    """str: For an any match, a match is when the match value equals the channel-read value."""
    MATCH_EXACT = "channel.MATCH_EXACT"
    """str: The state match indicator only becomes true when the match value equals the channel-read value."""  # noqa: E501
    MATCH_NONE = "channel.MATCH_NONE"
    """str: When none is set, matching is disabled."""
    MATCH_UNCHANGED = "channel.MATCH_UNCHANGED"
    """str: For an unchanged match, the value should be the same as the original. If not, a match is declared."""  # noqa: E501
    MODE_FALLING_EDGE = "channel.MODE_FALLING_EDGE"
    """str: For totalizer channels, select falling edge."""
    MODE_FALLING_EDGE_READ_RESET = "channel.MODE_FALLING_EDGE_READ_RESET"
    """str: For totalizer channels, select falling edge, then reset the count on read."""
    MODE_INPUT = "channel.MODE_INPUT"
    """str: Set digital channel to input."""
    MODE_OUTPUT = "channel.MODE_OUTPUT"
    """str: Set digital channel to output."""
    MODE_RISING_EDGE = "channel.MODE_RISING_EDGE"
    """str: For totalizer channels, select rising edge."""
    MODE_RISING_EDGE_READ_RESET = "channel.MODE_RISING_EDGE_READ_RESET"
    """str: For totalizer channels, select rising edge, then reset the count on read."""
    TYPE_BACKPLANE = "channel.TYPE_BACKPLANE"
    """str: Backplane."""
    TYPE_DAC = "channel.TYPE_DAC"
    """str: DAC channel."""
    TYPE_DIGITAL = "channel.TYPE_DIGITAL"
    """str: Digital channel."""
    TYPE_POLE = "channel.TYPE_POLE"
    """str: Pole channel."""
    TYPE_RADIO = "channel.TYPE_RADIO"
    """str: Radio channel."""
    TYPE_SWITCH = "channel.TYPE_SWITCH"
    """str: Switch channel."""
    TYPE_TOTALIZER = "channel.TYPE_TOTALIZER"
    """str: Totalizer channel."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "channel") -> None:
        super().__init__(device, cmd_syntax)
        self._multiple = ChannelMultiple(device, f"{self._cmd_syntax}.multiple")

    @property
    def multiple(self) -> ChannelMultiple:
        """Return the ``channel.multiple`` command tree.

        Sub-properties and sub-methods:
            - ``.close()``: The ``channel.multiple.close()`` function.
            - ``.open()``: The ``channel.multiple.open()`` function.
        """
        return self._multiple

    def close(self, channel_list: str) -> None:
        """Run the ``channel.close()`` function.

        Description:
            - This function closes the channels and channel pairs that are specified by the channel
              list parameter.

        TSP Syntax:
            ```
            - channel.close()
            ```

        Args:
            channel_list: A string that lists the channels and channel pairs to close.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.close("{channel_list}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.close()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getclose(self, channel_list: Optional[str] = None) -> str:
        """Run the ``channel.getclose()`` function.

        Description:
            - This function queries for the closed channels indicated by the channel list parameter.

        TSP Syntax:
            ```
            - channel.getclose()
            ```

        Args:
            channel_list (optional): A string that lists the channels to be queried (including
                allslots, slot1, or slot2 to get information on all channels in both slots or a
                specific slot); returns all slots if nothing is specified.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (f'"{channel_list}"' if channel_list is not None else None,)
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.getclose({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getclose()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getcommonside(self, slot: str) -> str:
        """Run the ``channel.getcommonside()`` function.

        Description:
            - This function lists the commonside setting for the specified slot.

        TSP Syntax:
            ```
            - channel.getcommonside()
            ```

        Args:
            slot: A string that lists the slot number; can be allslots, slot1, or slot2.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.getcommonside("{slot}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getcommonside()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getcount(self, channel_list: str) -> str:
        """Run the ``channel.getcount()`` function.

        Description:
            - This function returns the number of times the relays have been closed for the
              specified channels.

        TSP Syntax:
            ```
            - channel.getcount()
            ```

        Args:
            channel_list: A string listing the items to query, which can include.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.getcount("{channel_list}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getcount()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getcountinterval(self) -> str:
        """Run the ``channel.getcountinterval()`` function.

        Description:
            - This function returns the interval that is presently set for storage of channel relay
              closure counts.

        TSP Syntax:
            ```
            - channel.getcountinterval()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.getcountinterval())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getcountinterval()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getdelay(self, channel_list: str) -> str:
        """Run the ``channel.getdelay()`` function.

        Description:
            - This function queries for the additional delay time for the specified channels.

        TSP Syntax:
            ```
            - channel.getdelay()
            ```

        Args:
            channel_list: A string listing the channels to query for their delay times; slot1,
                slot2, or allslots allowed.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.getdelay("{channel_list}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getdelay()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getdmm(self, channel_list: str, setting: str) -> str:
        """Run the ``channel.getdmm()`` function.

        Description:
            - This function returns the setting for a channel DMM attribute.

        TSP Syntax:
            ```
            - channel.getdmm()
            ```

        Args:
            channel_list: List of channels to get from the DMM.
            setting: The DMM function or the parameter values to return for the selected channels.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.getdmm("{channel_list}", {setting}))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getdmm()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getlabel(self, channel_number: str) -> str:
        """Run the ``channel.getlabel()`` function.

        Description:
            - This function returns the label associated with the specified channel.

        TSP Syntax:
            ```
            - channel.getlabel()
            ```

        Args:
            channel_number: A string that lists the channel to query for the associated label.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.getlabel("{channel_number}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getlabel()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getmatch(self, channel_list: str) -> str:
        """Run the ``channel.getmatch()`` function.

        Description:
            - This function gets the match value on a channel.

        TSP Syntax:
            ```
            - channel.getmatch()
            ```

        Args:
            channel_list: String specifying digital I/O or totalizer channels to query, using normal
                channel list syntax.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.getmatch("{channel_list}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getmatch()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getmatchtype(self, channel_list: str) -> str:
        """Run the ``channel.getmatchtype()`` function.

        Description:
            - This function returns the match type for digital I/O and totalizer channels.

        TSP Syntax:
            ```
            - channel.getmatchtype()
            ```

        Args:
            channel_list: String specifying the digital I/O or totalizer channels to query, using
                normal channel list syntax.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.getmatchtype("{channel_list}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getmatchtype()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getmode(self, channel_list: str) -> str:
        """Run the ``channel.getmode()`` function.

        Description:
            - This function returns the present mode of digital and totalizer channels.

        TSP Syntax:
            ```
            - channel.getmode()
            ```

        Args:
            channel_list: String that specifies the channels to query, using normal channel list
                syntax.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.getmode("{channel_list}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getmode()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getstate(self, channel_list: Optional[str] = None) -> str:
        """Run the ``channel.getstate()`` function.

        Description:
            - This function returns the state indicators of the channels in the instrument.

        TSP Syntax:
            ```
            - channel.getstate()
            ```

        Args:
            channel_list (optional): String specifying the channels to query; use normal channel
                list syntax; if no channels are defined, all slots are returned.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (f'"{channel_list}"' if channel_list is not None else None,)
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.getstate({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getstate()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def gettype(self, channel_list: str) -> str:
        """Run the ``channel.gettype()`` function.

        Description:
            - This function returns the type associated with a channel.

        TSP Syntax:
            ```
            - channel.gettype()
            ```

        Args:
            channel_list: String specifying the channels to query, using normal channelList syntax.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.gettype("{channel_list}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.gettype()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getwidth(self, channel_number: int) -> str:
        """Run the ``channel.getwidth()`` function.

        Description:
            - This function gets the width used by the channel.

        TSP Syntax:
            ```
            - channel.getwidth()
            ```

        Args:
            channel_number: The first channel number of the channels to be combined.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.getwidth("{channel_number}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getwidth()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def open(self, channel_list: str) -> None:
        """Run the ``channel.open()`` function.

        Description:
            - This command opens the specified channels and channel pairs.

        TSP Syntax:
            ```
            - channel.open()
            ```

        Args:
            channel_list: String listing the channels to open; allslots, slot1, and slot2 available,
                which open all channels on all slots, all channels on slot 1, or all channels on
                slot 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.open("{channel_list}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.open()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def read(self, channel_list: str, reading_buffer: Optional[str] = None) -> str:
        """Run the ``channel.read()`` function.

        Description:
            - This function reads a value from a totalizer, DAC, or digital I/O channel.

        TSP Syntax:
            ```
            - channel.read()
            ```

        Args:
            channel_list: String that specifies a list of channels, using channel list notation.
            reading_buffer (optional): Reading buffer in which to store read values.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{channel_list}"',
                    reading_buffer,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.read({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.read()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setcommonside(self, slot: str, state: str) -> None:
        """Run the ``channel.setcommonside()`` function.

        Description:
            - This function sets up the specified slot to have a common side path.

        TSP Syntax:
            ```
            - channel.setcommonside()
            ```

        Args:
            slot: A string that lists the slot number; can be allslots, slot1, or slot2.
            state: channel.ON or channel.OFF.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.setcommonside("{slot}", {state})'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setcommonside()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setcountinterval(self, interval: str) -> None:
        """Run the ``channel.setcountinterval()`` function.

        Description:
            - This function determines how often the instrument stores the channel relay closure
              count.

        TSP Syntax:
            ```
            - channel.setcountinterval()
            ```

        Args:
            interval: The count update interval.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setcountinterval({interval})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setcountinterval()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setdelay(self, channel_list: str, delay: float) -> None:
        """Run the ``channel.setdelay()`` function.

        Description:
            - This function sets additional delay time for specified channels.

        TSP Syntax:
            ```
            - channel.setdelay()
            ```

        Args:
            channel_list: A string listing the channels for which to add delay time.
            delay: Delay time for the selected channels; minimum is 0 seconds.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.setdelay("{channel_list}", {delay})'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setdelay()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setdmm(self, channel_list: str, setting: str, value: str) -> None:
        """Run the ``channel.setdmm()`` function.

        Description:
            - This function configures the DMM for a channel or group of channels.

        TSP Syntax:
            ```
            - channel.setdmm()
            ```

        Args:
            channel_list: List of channels for which to set the DMM.
            setting: The DMM function or the parameter for the function to be applied to the
                channelList; refer to Details and the tables following the examples.
            value: The function or attribute value.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.setdmm("{channel_list}", {setting}, {value})'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setdmm()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setlabel(self, channel_number: str, labelname: str) -> None:
        """Run the ``channel.setlabel()`` function.

        Description:
            - This function sets the label associated with a channel.

        TSP Syntax:
            ```
            - channel.setlabel()
            ```

        Args:
            channel_number: A string that lists the channel for which to set the label.
            labelname: A string that contains the label for the channel in channelNumber, up to 19
                characters.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.setlabel("{channel_number}", "{labelname}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setlabel()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setmatch(self, channel_list: str, match_value: str, mask: Optional[str] = None) -> None:
        """Run the ``channel.setmatch()`` function.

        Description:
            - This function sets the match value on a digital input or totalizer channel.

        TSP Syntax:
            ```
            - channel.setmatch()
            ```

        Args:
            channel_list: String that specifies the channels to query, using normal channel list
                syntax.
            match_value: Channel value to compare on the specified channel.
            mask (optional): Value to specify the bits used to mask matchValue.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{channel_list}"',
                    match_value,
                    mask,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setmatch({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setmatch()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setmatchtype(self, channel_list: str, type_: str) -> None:
        """Run the ``channel.setmatchtype()`` function.

        Description:
            - This function sets the match type on a digital I/O or totalizer channel.

        TSP Syntax:
            ```
            - channel.setmatchtype()
            ```

        Args:
            channel_list: String specifying the channels to set, using normal channel list syntax.
            type_: A value for setting the match operation used on this specific channel.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.setmatchtype("{channel_list}", {type_})'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setmatchtype()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setmode(self, channel_list: str, mode: str) -> None:
        """Run the ``channel.setmode()`` function.

        Description:
            - This function sets the mode of operation of a channel.

        TSP Syntax:
            ```
            - channel.setmode()
            ```

        Args:
            channel_list: String specifying the channels to set, using normal channel list syntax.
            mode: The mode of operation for a channel; for digital channels, the options are.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.setmode("{channel_list}", {mode})'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setmode()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setwidth(self, channel_number: int, width: int) -> None:
        """Run the ``channel.setwidth()`` function.

        Description:
            - This function allows you to control multiple digital I/O channels as one channel.

        TSP Syntax:
            ```
            - channel.setwidth()
            ```

        Args:
            channel_number: The first channel number of the channels to be combined.
            width: The number of channels to combine.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.setwidth("{channel_number}", {width})'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setwidth()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def write(self, channel_list: str, value: str) -> None:
        """Run the ``channel.write()`` function.

        Description:
            - This function writes a value to a channel.

        TSP Syntax:
            ```
            - channel.write()
            ```

        Args:
            channel_list: The channels to set, using standard channel naming.
            value: The value to be written to the channel (must be decimal value).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.write("{channel_list}", {value})'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.write()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
