# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The channel commands module.

These commands are used in the following models:
DMM6500

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - channel.close()
    - channel.getclose()
    - channel.getcount()
    - channel.getdelay()
    - channel.getdmm()
    - channel.getlabel()
    - channel.getstate()
    - channel.gettype()
    - channel.multiple.close()
    - channel.multiple.open()
    - channel.open()
    - channel.setdelay()
    - channel.setdmm()
    - channel.setlabel()
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


class Channel(BaseTSPCmd):
    """The ``channel`` command tree.

    Properties and methods:
        - ``.close()``: The ``channel.close()`` function.
        - ``.getclose()``: The ``channel.getclose()`` function.
        - ``.getcount()``: The ``channel.getcount()`` function.
        - ``.getdelay()``: The ``channel.getdelay()`` function.
        - ``.getdmm()``: The ``channel.getdmm()`` function.
        - ``.getlabel()``: The ``channel.getlabel()`` function.
        - ``.getstate()``: The ``channel.getstate()`` function.
        - ``.gettype()``: The ``channel.gettype()`` function.
        - ``.multiple``: The ``channel.multiple`` command tree.
        - ``.open()``: The ``channel.open()`` function.
        - ``.setdelay()``: The ``channel.setdelay()`` function.
        - ``.setdmm()``: The ``channel.setdmm()`` function.
        - ``.setlabel()``: The ``channel.setlabel()`` function.
    """

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
            channel_list (optional): A string representing the channels and channel patterns that
                will be queried.

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

    def getcount(self, channel_list: Optional[str] = None) -> str:
        """Run the ``channel.getcount()`` function.

        Description:
            - This function returns the number of times the relays have been closed for the
              specified channels.

        TSP Syntax:
            ```
            - channel.getcount()
            ```

        Args:
            channel_list (optional): A string listing the items to query, which can include.

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
                f"print({self._cmd_syntax}.getcount({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getcount()`` function."  # noqa: E501
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
                list syntax; if no channels are defined, all slots are returnedall channels are
                returned.

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
                slot 2allslots and slot1 are available; both open all channels.

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
