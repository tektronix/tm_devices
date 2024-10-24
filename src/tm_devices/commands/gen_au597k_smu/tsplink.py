# pylint: disable=line-too-long
# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The tsplink commands module.

These commands are used in the following models:
SMU2606B, SMU2651A, SMU2657A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - tsplink.group
    - tsplink.master
    - tsplink.node
    - tsplink.readbit()
    - tsplink.readport()
    - tsplink.reset()
    - tsplink.state
    - tsplink.trigger[N].assert()
    - tsplink.trigger[N].clear()
    - tsplink.trigger[N].mode
    - tsplink.trigger[N].overrun
    - tsplink.trigger[N].pulsewidth
    - tsplink.trigger[N].release()
    - tsplink.trigger[N].reset()
    - tsplink.trigger[N].stimulus
    - tsplink.trigger[N].wait()
    - tsplink.writebit()
    - tsplink.writeport()
    - tsplink.writeprotect
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING, Union

from ..helpers import (
    BaseTSPCmd,
    DefaultDictPassKeyToFactory,
    NoDeviceProvidedError,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class TsplinkTriggerItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``tsplink.trigger[N]`` command tree.

    Info:
        - ``N``, the trigger line (1 to 3).

    Constants:
        - ``.EVENT_ID``: The number that is used for the trigger events.

    Properties and methods:
        - ``.assert()``: The ``tsplink.trigger[N].assert()`` function.
        - ``.clear()``: The ``tsplink.trigger[N].clear()`` function.
        - ``.mode``: The ``tsplink.trigger[N].mode`` attribute.
        - ``.overrun``: The ``tsplink.trigger[N].overrun`` attribute.
        - ``.pulsewidth``: The ``tsplink.trigger[N].pulsewidth`` attribute.
        - ``.release()``: The ``tsplink.trigger[N].release()`` function.
        - ``.reset()``: The ``tsplink.trigger[N].reset()`` function.
        - ``.stimulus``: The ``tsplink.trigger[N].stimulus`` attribute.
        - ``.wait()``: The ``tsplink.trigger[N].wait()`` function.
    """

    EVENT_ID = "tsplink.trigger[N].EVENT_ID"
    """str: The number that is used for the trigger events."""

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        # pylint: disable=invalid-name
        self.EVENT_ID = self.EVENT_ID.replace(
            "[N]", f"[{self._cmd_syntax.rsplit('[', maxsplit=1)[-1].split(']', maxsplit=1)[0]}]"
        )

    @property
    def mode(self) -> str:
        """Access the ``tsplink.trigger[N].mode`` attribute.

        Description:
            - This attribute defines the trigger operation and detection mode.

        Usage:
            - Accessing this property will send the ``print(tsplink.trigger[N].mode)`` query.
            - Setting this property to a value will send the ``tsplink.trigger[N].mode = value``
              command.

        TSP Syntax:
            ```
            - tsplink.trigger[N].mode = value
            - print(tsplink.trigger[N].mode)
            ```

        Info:
            - ``N``, the trigger line (1 to 3).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".mode"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.mode)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.mode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @mode.setter
    def mode(self, value: Union[str, float]) -> None:
        """Access the ``tsplink.trigger[N].mode`` attribute.

        Description:
            - This attribute defines the trigger operation and detection mode.

        Usage:
            - Accessing this property will send the ``print(tsplink.trigger[N].mode)`` query.
            - Setting this property to a value will send the ``tsplink.trigger[N].mode = value``
              command.

        TSP Syntax:
            ```
            - tsplink.trigger[N].mode = value
            - print(tsplink.trigger[N].mode)
            ```

        Info:
            - ``N``, the trigger line (1 to 3).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".mode", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.mode = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.mode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def overrun(self) -> str:
        """Access the ``tsplink.trigger[N].overrun`` attribute.

        Description:
            - This attribute indicates if the event detector ignored an event while in the detected
              state.

        Usage:
            - Accessing this property will send the ``print(tsplink.trigger[N].overrun)`` query.

        TSP Syntax:
            ```
            - print(tsplink.trigger[N].overrun)
            ```

        Info:
            - ``N``, the trigger line (1 to 3).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".overrun"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.overrun)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.overrun`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def pulsewidth(self) -> str:
        """Access the ``tsplink.trigger[N].pulsewidth`` attribute.

        Description:
            - This attribute sets the length of time that the trigger line is asserted for output
              triggers.

        Usage:
            - Accessing this property will send the ``print(tsplink.trigger[N].pulsewidth)`` query.
            - Setting this property to a value will send the
              ``tsplink.trigger[N].pulsewidth = value`` command.

        TSP Syntax:
            ```
            - tsplink.trigger[N].pulsewidth = value
            - print(tsplink.trigger[N].pulsewidth)
            ```

        Info:
            - ``width``, the pulse width (in seconds).
            - ``N``, the trigger line (1 to 3).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".pulsewidth"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.pulsewidth)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.pulsewidth`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @pulsewidth.setter
    def pulsewidth(self, value: Union[str, float]) -> None:
        """Access the ``tsplink.trigger[N].pulsewidth`` attribute.

        Description:
            - This attribute sets the length of time that the trigger line is asserted for output
              triggers.

        Usage:
            - Accessing this property will send the ``print(tsplink.trigger[N].pulsewidth)`` query.
            - Setting this property to a value will send the
              ``tsplink.trigger[N].pulsewidth = value`` command.

        TSP Syntax:
            ```
            - tsplink.trigger[N].pulsewidth = value
            - print(tsplink.trigger[N].pulsewidth)
            ```

        Info:
            - ``width``, the pulse width (in seconds).
            - ``N``, the trigger line (1 to 3).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".pulsewidth", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.pulsewidth = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.pulsewidth`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def stimulus(self) -> str:
        """Access the ``tsplink.trigger[N].stimulus`` attribute.

        Description:
            - This attribute specifies the event that causes the synchronization line to assert a
              trigger.

        Usage:
            - Accessing this property will send the ``print(tsplink.trigger[N].stimulus)`` query.
            - Setting this property to a value will send the ``tsplink.trigger[N].stimulus = value``
              command.

        TSP Syntax:
            ```
            - tsplink.trigger[N].stimulus = value
            - print(tsplink.trigger[N].stimulus)
            ```

        Info:
            - ``N``, the trigger line (1 to 3).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".stimulus"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.stimulus)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @stimulus.setter
    def stimulus(self, value: Union[str, float]) -> None:
        """Access the ``tsplink.trigger[N].stimulus`` attribute.

        Description:
            - This attribute specifies the event that causes the synchronization line to assert a
              trigger.

        Usage:
            - Accessing this property will send the ``print(tsplink.trigger[N].stimulus)`` query.
            - Setting this property to a value will send the ``tsplink.trigger[N].stimulus = value``
              command.

        TSP Syntax:
            ```
            - tsplink.trigger[N].stimulus = value
            - print(tsplink.trigger[N].stimulus)
            ```

        Info:
            - ``N``, the trigger line (1 to 3).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".stimulus", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.stimulus = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def assert_(self) -> None:
        """Run the ``tsplink.trigger[N].assert()`` function.

        Description:
            - This function simulates the occurrence of the trigger and generates the corresponding
              event ID.

        TSP Syntax:
            ```
            - tsplink.trigger[N].assert()
            ```

        Info:
            - ``N``, the trigger line (1 to 3).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.assert()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.assert()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def clear(self) -> None:
        """Run the ``tsplink.trigger[N].clear()`` function.

        Description:
            - This function clears the event detector for a LAN trigger.

        TSP Syntax:
            ```
            - tsplink.trigger[N].clear()
            ```

        Info:
            - ``N``, the trigger line (1 to 3) to clear.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.clear()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.clear()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def release(self) -> None:
        """Run the ``tsplink.trigger[N].release()`` function.

        Description:
            - This function releases a latched trigger on the given TSP-Link trigger line.

        TSP Syntax:
            ```
            - tsplink.trigger[N].release()
            ```

        Info:
            - ``N``, the trigger line (1 to 3).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.release()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.release()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def reset(self) -> None:
        """Run the ``tsplink.trigger[N].reset()`` function.

        Description:
            - This function resets some of the TSP-Link trigger attributes to their factory
              defaults.

        TSP Syntax:
            ```
            - tsplink.trigger[N].reset()
            ```

        Info:
            - ``N``, the trigger line (1 to 3).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.reset()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.reset()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def wait(self, timeout: float) -> str:
        """Run the ``tsplink.trigger[N].wait()`` function.

        Description:
            - This function waits for a trigger.

        TSP Syntax:
            ```
            - tsplink.trigger[N].wait()
            ```

        Args:
            timeout: The timeout value in seconds.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.wait({timeout}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.wait()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class Tsplink(BaseTSPCmd):
    """The ``tsplink`` command tree.

    Constants:
        - ``.TRIG_BYPASS``: Allows direct control of the line as a digital I/O line.
        - ``.TRIG_EITHER``: Detects rising-edge or falling-edge triggers as input. Asserts a TTL-low
          pulse for output.
        - ``.TRIG_FALLING``: Detects falling-edge triggers as input. Asserts a TTL-low pulse for
          output.
        - ``.TRIG_RISING``: If the programmed state of the line is high, the tsplink.TRIG_RISING
          mode behaves similarly to tsplink.TRIG_RISINGA.
          If the programmed state of the line is low, the tsplink.TRIG_RISING mode behaves similarly to
          tsplink.TRIG_RISINGM.
          Use tsplink.TRIG_RISINGA if the line is in the high output state.
          Use tsplink.TRIG_RISINGM if the line is in the low output state.
        - ``.TRIG_RISINGA``: Detects rising-edge triggers as input. Asserts a TTL-low pulse for
          output.
        - ``.TRIG_RISINGM``: Edge detection as an input is not available. Generates a TTL-high pulse
          as an output trigger.
        - ``.TRIG_SYNCHRONOUS``: Detects the falling-edge input triggers and automatically latches
          and drives the trigger line low. Asserts a TTL-low pulse as an output trigger.
        - ``.TRIG_SYNCHRONOUSA``: Detects the falling-edge input triggers and automatically latches
          and drives the trigger line low.
        - ``.TRIG_SYNCHRONOUSM``: Detects rising-edge triggers as an input. Asserts a TTL-low pulse
          for output.

    Properties and methods:
        - ``.group``: The ``tsplink.group`` attribute.
        - ``.master``: The ``tsplink.master`` attribute.
        - ``.node``: The ``tsplink.node`` attribute.
        - ``.readbit()``: The ``tsplink.readbit()`` function.
        - ``.readport()``: The ``tsplink.readport()`` function.
        - ``.reset()``: The ``tsplink.reset()`` function.
        - ``.state``: The ``tsplink.state`` attribute.
        - ``.trigger``: The ``tsplink.trigger[N]`` command tree.
        - ``.writebit()``: The ``tsplink.writebit()`` function.
        - ``.writeport()``: The ``tsplink.writeport()`` function.
        - ``.writeprotect``: The ``tsplink.writeprotect`` attribute.
    """  # noqa: E501

    TRIG_BYPASS = "tsplink.TRIG_BYPASS"
    """str: Allows direct control of the line as a digital I/O line."""
    TRIG_EITHER = "tsplink.TRIG_EITHER"
    """str: Detects rising-edge or falling-edge triggers as input. Asserts a TTL-low pulse for output."""  # noqa: E501
    TRIG_FALLING = "tsplink.TRIG_FALLING"
    """str: Detects falling-edge triggers as input. Asserts a TTL-low pulse for output."""
    TRIG_RISING = "tsplink.TRIG_RISING"
    """str: If the programmed state of the line is high, the tsplink.TRIG_RISING mode behaves similarly to tsplink.TRIG_RISINGA.
If the programmed state of the line is low, the tsplink.TRIG_RISING mode behaves similarly to tsplink.TRIG_RISINGM.
Use tsplink.TRIG_RISINGA if the line is in the high output state.
Use tsplink.TRIG_RISINGM if the line is in the low output state."""  # noqa: E501
    TRIG_RISINGA = "tsplink.TRIG_RISINGA"
    """str: Detects rising-edge triggers as input. Asserts a TTL-low pulse for output."""
    TRIG_RISINGM = "tsplink.TRIG_RISINGM"
    """str: Edge detection as an input is not available. Generates a TTL-high pulse as an output trigger."""  # noqa: E501
    TRIG_SYNCHRONOUS = "tsplink.TRIG_SYNCHRONOUS"
    """str: Detects the falling-edge input triggers and automatically latches and drives the trigger line low. Asserts a TTL-low pulse as an output trigger."""  # noqa: E501
    TRIG_SYNCHRONOUSA = "tsplink.TRIG_SYNCHRONOUSA"
    """str: Detects the falling-edge input triggers and automatically latches and drives the trigger line low."""  # noqa: E501
    TRIG_SYNCHRONOUSM = "tsplink.TRIG_SYNCHRONOUSM"
    """str: Detects rising-edge triggers as an input. Asserts a TTL-low pulse for output."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "tsplink") -> None:
        super().__init__(device, cmd_syntax)
        self._trigger: Dict[int, TsplinkTriggerItem] = DefaultDictPassKeyToFactory(
            lambda x: TsplinkTriggerItem(device, f"{self._cmd_syntax}.trigger[{x}]")
        )

    @property
    def group(self) -> str:
        """Access the ``tsplink.group`` attribute.

        Description:
            - This attribute contains the group number of a TSP-Link node.

        Usage:
            - Accessing this property will send the ``print(tsplink.group)`` query.
            - Setting this property to a value will send the ``tsplink.group = value`` command.

        TSP Syntax:
            ```
            - tsplink.group = value
            - print(tsplink.group)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".group"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.group)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.group`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @group.setter
    def group(self, value: Union[str, float]) -> None:
        """Access the ``tsplink.group`` attribute.

        Description:
            - This attribute contains the group number of a TSP-Link node.

        Usage:
            - Accessing this property will send the ``print(tsplink.group)`` query.
            - Setting this property to a value will send the ``tsplink.group = value`` command.

        TSP Syntax:
            ```
            - tsplink.group = value
            - print(tsplink.group)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".group", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.group = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.group`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def master(self) -> str:
        """Access the ``tsplink.master`` attribute.

        Description:
            - This attribute reads the node number assigned to the master node.

        Usage:
            - Accessing this property will send the ``print(tsplink.master)`` query.

        TSP Syntax:
            ```
            - print(tsplink.master)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".master"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.master)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.master`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def node(self) -> str:
        """Access the ``tsplink.node`` attribute.

        Description:
            - This attribute defines the node number.

        Usage:
            - Accessing this property will send the ``print(tsplink.node)`` query.
            - Setting this property to a value will send the ``tsplink.node = value`` command.

        TSP Syntax:
            ```
            - tsplink.node = value
            - print(tsplink.node)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".node"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.node)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.node`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @node.setter
    def node(self, value: Union[str, float]) -> None:
        """Access the ``tsplink.node`` attribute.

        Description:
            - This attribute defines the node number.

        Usage:
            - Accessing this property will send the ``print(tsplink.node)`` query.
            - Setting this property to a value will send the ``tsplink.node = value`` command.

        TSP Syntax:
            ```
            - tsplink.node = value
            - print(tsplink.node)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".node", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.node = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.node`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def state(self) -> str:
        """Access the ``tsplink.state`` attribute.

        Description:
            - This attribute describes the TSP-Link online state.

        Usage:
            - Accessing this property will send the ``print(tsplink.state)`` query.

        TSP Syntax:
            ```
            - print(tsplink.state)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".state"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.state)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.state`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def trigger(self) -> Dict[int, TsplinkTriggerItem]:
        """Return the ``tsplink.trigger[N]`` command tree.

        Info:
            - ``N``, the trigger line (1 to 3).

        Constants:
            - ``.EVENT_ID``: The number that is used for the trigger events.

        Sub-properties and sub-methods:
            - ``.assert()``: The ``tsplink.trigger[N].assert()`` function.
            - ``.clear()``: The ``tsplink.trigger[N].clear()`` function.
            - ``.mode``: The ``tsplink.trigger[N].mode`` attribute.
            - ``.overrun``: The ``tsplink.trigger[N].overrun`` attribute.
            - ``.pulsewidth``: The ``tsplink.trigger[N].pulsewidth`` attribute.
            - ``.release()``: The ``tsplink.trigger[N].release()`` function.
            - ``.reset()``: The ``tsplink.trigger[N].reset()`` function.
            - ``.stimulus``: The ``tsplink.trigger[N].stimulus`` attribute.
            - ``.wait()``: The ``tsplink.trigger[N].wait()`` function.
        """
        return self._trigger

    @property
    def writeprotect(self) -> str:
        """Access the ``tsplink.writeprotect`` attribute.

        Description:
            - This attribute contains the write-protect mask that protects bits from changes by the
              tsplink.writebit() and tsplink.writeport() functions.

        Usage:
            - Accessing this property will send the ``print(tsplink.writeprotect)`` query.
            - Setting this property to a value will send the ``tsplink.writeprotect = value``
              command.

        TSP Syntax:
            ```
            - tsplink.writeprotect = value
            - print(tsplink.writeprotect)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".writeprotect"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.writeprotect)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.writeprotect`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @writeprotect.setter
    def writeprotect(self, value: Union[str, float]) -> None:
        """Access the ``tsplink.writeprotect`` attribute.

        Description:
            - This attribute contains the write-protect mask that protects bits from changes by the
              tsplink.writebit() and tsplink.writeport() functions.

        Usage:
            - Accessing this property will send the ``print(tsplink.writeprotect)`` query.
            - Setting this property to a value will send the ``tsplink.writeprotect = value``
              command.

        TSP Syntax:
            ```
            - tsplink.writeprotect = value
            - print(tsplink.writeprotect)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".writeprotect", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.writeprotect = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.writeprotect`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def readbit(self, n: int) -> str:
        """Run the ``tsplink.readbit()`` function.

        Description:
            - This function reads the state of a TSP-Link synchronization line.

        TSP Syntax:
            ```
            - tsplink.readbit()
            ```

        Args:
            n: The trigger line (1 to 3).

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.readbit({n}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.readbit()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def readport(self) -> str:
        """Run the ``tsplink.readport()`` function.

        Description:
            - This function reads the TSP-Link trigger lines as a digital I/O port.

        TSP Syntax:
            ```
            - tsplink.readport()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.readport())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.readport()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def reset(self, expected_nodes: Optional[int] = None) -> str:
        """Run the ``tsplink.reset()`` function.

        Description:
            - This function initializes (resets) all nodes (instruments) in the TSP-Link system.

        TSP Syntax:
            ```
            - tsplink.reset()
            ```

        Args:
            expected_nodes (optional): The number of nodes expected on the system (1 to 64).

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (expected_nodes,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.reset({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.reset()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def writebit(self, n: int, data: int) -> None:
        """Run the ``tsplink.writebit()`` function.

        Description:
            - This function sets a TSP-Link trigger line high or low.

        TSP Syntax:
            ```
            - tsplink.writebit()
            ```

        Args:
            n: The trigger line (1 to 3).
            data: The value to write to the bit.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.writebit({n}, {data})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.writebit()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def writeport(self, data: int) -> None:
        """Run the ``tsplink.writeport()`` function.

        Description:
            - This function writes to all TSP-Link synchronization lines.

        TSP Syntax:
            ```
            - tsplink.writeport()
            ```

        Args:
            data: Value to write to the port (0 to 7).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.writeport({data})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.writeport()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
