# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The trigger commands module.

These commands are used in the following models:
SMU2601B, SMU2602B, SMU2604B, SMU2606B, SMU2611B, SMU2612B, SMU2614B, SMU2634B, SMU2635B, SMU2636B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - trigger.blender[N].clear()
    - trigger.blender[N].orenable
    - trigger.blender[N].overrun
    - trigger.blender[N].reset()
    - trigger.blender[N].stimulus[M]
    - trigger.blender[N].wait()
    - trigger.clear()
    - trigger.generator[N].assert()
    - trigger.timer[N].clear()
    - trigger.timer[N].count
    - trigger.timer[N].delay
    - trigger.timer[N].delaylist
    - trigger.timer[N].overrun
    - trigger.timer[N].passthrough
    - trigger.timer[N].reset()
    - trigger.timer[N].stimulus
    - trigger.timer[N].wait()
    - trigger.wait()
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING, Union

from ..helpers import (
    BaseTSPCmd,
    DefaultDictDeviceCommunication,
    DefaultDictPassKeyToFactory,
    NoDeviceProvidedError,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class TriggerTimerItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``trigger.timer[N]`` command tree.

    Info:
        - ``N``, the trigger timer number (1 to 8).

    Constants:
        - ``.EVENT_ID``: The trigger timer event number.

    Properties and methods:
        - ``.clear()``: The ``trigger.timer[N].clear()`` function.
        - ``.count``: The ``trigger.timer[N].count`` attribute.
        - ``.delay``: The ``trigger.timer[N].delay`` attribute.
        - ``.delaylist``: The ``trigger.timer[N].delaylist`` attribute.
        - ``.overrun``: The ``trigger.timer[N].overrun`` attribute.
        - ``.passthrough``: The ``trigger.timer[N].passthrough`` attribute.
        - ``.reset()``: The ``trigger.timer[N].reset()`` function.
        - ``.stimulus``: The ``trigger.timer[N].stimulus`` attribute.
        - ``.wait()``: The ``trigger.timer[N].wait()`` function.
    """

    EVENT_ID = "trigger.timer[N].EVENT_ID"
    """str: The trigger timer event number."""

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        # pylint: disable=invalid-name
        self.EVENT_ID = self.EVENT_ID.replace(
            "[N]", f"[{self._cmd_syntax.rsplit('[', maxsplit=1)[-1].split(']', maxsplit=1)[0]}]"
        )

    @property
    def count(self) -> str:
        """Access the ``trigger.timer[N].count`` attribute.

        Description:
            - This attribute sets the number of events to generate each time the timer generates a
              trigger event.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].count)`` query.
            - Setting this property to a value will send the ``trigger.timer[N].count = value``
              command.

        TSP Syntax:
            ```
            - trigger.timer[N].count = value
            - print(trigger.timer[N].count)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".count"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.count)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.count`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @count.setter
    def count(self, value: Union[str, float]) -> None:
        """Access the ``trigger.timer[N].count`` attribute.

        Description:
            - This attribute sets the number of events to generate each time the timer generates a
              trigger event.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].count)`` query.
            - Setting this property to a value will send the ``trigger.timer[N].count = value``
              command.

        TSP Syntax:
            ```
            - trigger.timer[N].count = value
            - print(trigger.timer[N].count)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".count", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.count = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.count`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def delay(self) -> str:
        """Access the ``trigger.timer[N].delay`` attribute.

        Description:
            - This attribute sets and reads the timer delay.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].delay)`` query.
            - Setting this property to a value will send the ``trigger.timer[N].delay = value``
              command.

        TSP Syntax:
            ```
            - trigger.timer[N].delay = value
            - print(trigger.timer[N].delay)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".delay"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.delay)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.delay`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @delay.setter
    def delay(self, value: Union[str, float]) -> None:
        """Access the ``trigger.timer[N].delay`` attribute.

        Description:
            - This attribute sets and reads the timer delay.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].delay)`` query.
            - Setting this property to a value will send the ``trigger.timer[N].delay = value``
              command.

        TSP Syntax:
            ```
            - trigger.timer[N].delay = value
            - print(trigger.timer[N].delay)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".delay", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.delay = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.delay`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def delaylist(self) -> str:
        """Access the ``trigger.timer[N].delaylist`` attribute.

        Description:
            - This attribute sets an array of timer intervals.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].delaylist)`` query.
            - Setting this property to a value will send the ``trigger.timer[N].delaylist = value``
              command.

        TSP Syntax:
            ```
            - trigger.timer[N].delaylist = value
            - print(trigger.timer[N].delaylist)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".delaylist"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.delaylist)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.delaylist`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @delaylist.setter
    def delaylist(self, value: Union[str, float]) -> None:
        """Access the ``trigger.timer[N].delaylist`` attribute.

        Description:
            - This attribute sets an array of timer intervals.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].delaylist)`` query.
            - Setting this property to a value will send the ``trigger.timer[N].delaylist = value``
              command.

        TSP Syntax:
            ```
            - trigger.timer[N].delaylist = value
            - print(trigger.timer[N].delaylist)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".delaylist", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.delaylist = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.delaylist`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def overrun(self) -> str:
        """Access the ``trigger.timer[N].overrun`` attribute.

        Description:
            - This attribute indicates if an event was ignored because of the event detector state.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].overrun)`` query.

        TSP Syntax:
            ```
            - print(trigger.timer[N].overrun)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 8).

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
    def passthrough(self) -> str:
        """Access the ``trigger.timer[N].passthrough`` attribute.

        Description:
            - This attribute enables or disables the timer trigger pass-through mode.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].passthrough)`` query.
            - Setting this property to a value will send the
              ``trigger.timer[N].passthrough = value`` command.

        TSP Syntax:
            ```
            - trigger.timer[N].passthrough = value
            - print(trigger.timer[N].passthrough)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".passthrough"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.passthrough)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.passthrough`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @passthrough.setter
    def passthrough(self, value: Union[str, float]) -> None:
        """Access the ``trigger.timer[N].passthrough`` attribute.

        Description:
            - This attribute enables or disables the timer trigger pass-through mode.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].passthrough)`` query.
            - Setting this property to a value will send the
              ``trigger.timer[N].passthrough = value`` command.

        TSP Syntax:
            ```
            - trigger.timer[N].passthrough = value
            - print(trigger.timer[N].passthrough)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".passthrough", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.passthrough = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.passthrough`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def stimulus(self) -> str:
        """Access the ``trigger.timer[N].stimulus`` attribute.

        Description:
            - This attribute specifies which event starts the timer.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].stimulus)`` query.
            - Setting this property to a value will send the ``trigger.timer[N].stimulus = value``
              command.

        TSP Syntax:
            ```
            - trigger.timer[N].stimulus = value
            - print(trigger.timer[N].stimulus)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 8).

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
        """Access the ``trigger.timer[N].stimulus`` attribute.

        Description:
            - This attribute specifies which event starts the timer.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].stimulus)`` query.
            - Setting this property to a value will send the ``trigger.timer[N].stimulus = value``
              command.

        TSP Syntax:
            ```
            - trigger.timer[N].stimulus = value
            - print(trigger.timer[N].stimulus)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 8).

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

    def clear(self) -> None:
        """Run the ``trigger.timer[N].clear()`` function.

        Description:
            - This function clears the timer event detector and overrun indicator for the specified
              trigger timer number.

        TSP Syntax:
            ```
            - trigger.timer[N].clear()
            ```

        Info:
            - ``N``, the trigger timer number (1 to 8).

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

    def reset(self) -> None:
        """Run the ``trigger.timer[N].reset()`` function.

        Description:
            - This function resets some of the trigger timer settings to their factory defaults.

        TSP Syntax:
            ```
            - trigger.timer[N].reset()
            ```

        Info:
            - ``N``, the trigger timer number (1 to 8).

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
        """Run the ``trigger.timer[N].wait()`` function.

        Description:
            - This function waits for a trigger.

        TSP Syntax:
            ```
            - trigger.timer[N].wait()
            ```

        Args:
            timeout: Maximum amount of time in seconds to wait for the trigger.

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


class TriggerGeneratorItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``trigger.generator[N]`` command tree.

    Info:
        - ``N``, the generator number (1 or 2).

    Constants:
        - ``.EVENT_ID``: The trigger event generated by the trigger event generator.

    Properties and methods:
        - ``.assert()``: The ``trigger.generator[N].assert()`` function.
    """

    EVENT_ID = "trigger.generator[N].EVENT_ID"
    """str: The trigger event generated by the trigger event generator."""

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        # pylint: disable=invalid-name
        self.EVENT_ID = self.EVENT_ID.replace(
            "[N]", f"[{self._cmd_syntax.rsplit('[', maxsplit=1)[-1].split(']', maxsplit=1)[0]}]"
        )

    def assert_(self) -> None:
        """Run the ``trigger.generator[N].assert()`` function.

        Description:
            - This function generates a trigger event.

        TSP Syntax:
            ```
            - trigger.generator[N].assert()
            ```

        Info:
            - ``N``, the generator number (1 or 2).

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


class TriggerBlenderItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``trigger.blender[N]`` command tree.

    Info:
        - ``N``, the blender number (up to six).

    Constants:
        - ``.EVENT_ID``: The trigger blender event number.

    Properties and methods:
        - ``.clear()``: The ``trigger.blender[N].clear()`` function.
        - ``.orenable``: The ``trigger.blender[N].orenable`` attribute.
        - ``.overrun``: The ``trigger.blender[N].overrun`` attribute.
        - ``.reset()``: The ``trigger.blender[N].reset()`` function.
        - ``.stimulus``: The ``trigger.blender[N].stimulus[M]`` attribute.
        - ``.wait()``: The ``trigger.blender[N].wait()`` function.
    """

    EVENT_ID = "trigger.blender[N].EVENT_ID"
    """str: The trigger blender event number."""

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        # pylint: disable=invalid-name
        self.EVENT_ID = self.EVENT_ID.replace(
            "[N]", f"[{self._cmd_syntax.rsplit('[', maxsplit=1)[-1].split(']', maxsplit=1)[0]}]"
        )
        self._stimulus: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.stimulus[{{key}}]",
            write_syntax=f"{self._cmd_syntax}.stimulus[{{key}}] = ",
            query_syntax=f"print({self._cmd_syntax}.stimulus[{{key}}])",
            device=self._device,
        )

    @property
    def orenable(self) -> str:
        """Access the ``trigger.blender[N].orenable`` attribute.

        Description:
            - This attribute selects whether the blender performs OR operations or AND operations.

        Usage:
            - Accessing this property will send the ``print(trigger.blender[N].orenable)`` query.
            - Setting this property to a value will send the ``trigger.blender[N].orenable = value``
              command.

        TSP Syntax:
            ```
            - trigger.blender[N].orenable = value
            - print(trigger.blender[N].orenable)
            ```

        Info:
            - ``N``, the blender number (up to six).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".orenable"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.orenable)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.orenable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @orenable.setter
    def orenable(self, value: Union[str, float]) -> None:
        """Access the ``trigger.blender[N].orenable`` attribute.

        Description:
            - This attribute selects whether the blender performs OR operations or AND operations.

        Usage:
            - Accessing this property will send the ``print(trigger.blender[N].orenable)`` query.
            - Setting this property to a value will send the ``trigger.blender[N].orenable = value``
              command.

        TSP Syntax:
            ```
            - trigger.blender[N].orenable = value
            - print(trigger.blender[N].orenable)
            ```

        Info:
            - ``N``, the blender number (up to six).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".orenable", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.orenable = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.orenable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def overrun(self) -> str:
        """Access the ``trigger.blender[N].overrun`` attribute.

        Description:
            - This attribute indicates whether or not an event was ignored because of the event
              detector state.

        Usage:
            - Accessing this property will send the ``print(trigger.blender[N].overrun)`` query.

        TSP Syntax:
            ```
            - print(trigger.blender[N].overrun)
            ```

        Info:
            - ``N``, the blender number (up to six).

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
    def stimulus(self) -> Dict[int, Union[str, float]]:
        """Access the ``trigger.blender[N].stimulus[M]`` attribute.

        Description:
            - This attribute specifies the events that trigger the blender.

        Usage:
            - Accessing an item from this property will send the
              ``print(trigger.blender[N].stimulus[M])`` query.
            - Setting an item from this property to a value will send the
              ``trigger.blender[N].stimulus[M] = value`` command.

        TSP Syntax:
            ```
            - trigger.blender[N].stimulus[M] = value
            - print(trigger.blender[N].stimulus[M])
            ```

        Info:
            - ``N``, the an integer representing the trigger event blender (up to six).
            - ``M``, the an integer representing the stimulus index (1 to 4).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._stimulus

    def clear(self) -> None:
        """Run the ``trigger.blender[N].clear()`` function.

        Description:
            - This function clears the blender event detector and resets the overrun indicator of
              blender N.

        TSP Syntax:
            ```
            - trigger.blender[N].clear()
            ```

        Info:
            - ``N``, the blender number (up to six).

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

    def reset(self) -> None:
        """Run the ``trigger.blender[N].reset()`` function.

        Description:
            - This function resets some of the trigger blender settings to their factory defaults.

        TSP Syntax:
            ```
            - trigger.blender[N].reset()
            ```

        Info:
            - ``N``, the trigger event blender (up to six).

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
        """Run the ``trigger.blender[N].wait()`` function.

        Description:
            - This function waits for a blender trigger event to occur.

        TSP Syntax:
            ```
            - trigger.blender[N].wait()
            ```

        Args:
            timeout: Maximum amount of time in seconds to wait for the trigger blender event.

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


class Trigger(BaseTSPCmd):
    """The ``trigger`` command tree.

    Constants:
        - ``.EVENT_ID``: The command interface trigger event number.

    Properties and methods:
        - ``.blender``: The ``trigger.blender[N]`` command tree.
        - ``.clear()``: The ``trigger.clear()`` function.
        - ``.generator``: The ``trigger.generator[N]`` command tree.
        - ``.timer``: The ``trigger.timer[N]`` command tree.
        - ``.wait()``: The ``trigger.wait()`` function.
    """

    EVENT_ID = "trigger.EVENT_ID"
    """str: The command interface trigger event number."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "trigger") -> None:
        super().__init__(device, cmd_syntax)
        self._blender: Dict[int, TriggerBlenderItem] = DefaultDictPassKeyToFactory(
            lambda x: TriggerBlenderItem(device, f"{self._cmd_syntax}.blender[{x}]")
        )
        self._generator: Dict[int, TriggerGeneratorItem] = DefaultDictPassKeyToFactory(
            lambda x: TriggerGeneratorItem(device, f"{self._cmd_syntax}.generator[{x}]")
        )
        self._timer: Dict[int, TriggerTimerItem] = DefaultDictPassKeyToFactory(
            lambda x: TriggerTimerItem(device, f"{self._cmd_syntax}.timer[{x}]")
        )

    @property
    def blender(self) -> Dict[int, TriggerBlenderItem]:
        """Return the ``trigger.blender[N]`` command tree.

        Info:
            - ``N``, the blender number (up to six).

        Constants:
            - ``.EVENT_ID``: The trigger blender event number.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``trigger.blender[N].clear()`` function.
            - ``.orenable``: The ``trigger.blender[N].orenable`` attribute.
            - ``.overrun``: The ``trigger.blender[N].overrun`` attribute.
            - ``.reset()``: The ``trigger.blender[N].reset()`` function.
            - ``.stimulus``: The ``trigger.blender[N].stimulus[M]`` attribute.
            - ``.wait()``: The ``trigger.blender[N].wait()`` function.
        """
        return self._blender

    @property
    def generator(self) -> Dict[int, TriggerGeneratorItem]:
        """Return the ``trigger.generator[N]`` command tree.

        Info:
            - ``N``, the generator number (1 or 2).

        Constants:
            - ``.EVENT_ID``: The trigger event generated by the trigger event generator.

        Sub-properties and sub-methods:
            - ``.assert()``: The ``trigger.generator[N].assert()`` function.
        """
        return self._generator

    @property
    def timer(self) -> Dict[int, TriggerTimerItem]:
        """Return the ``trigger.timer[N]`` command tree.

        Info:
            - ``N``, the trigger timer number (1 to 8).

        Constants:
            - ``.EVENT_ID``: The trigger timer event number.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``trigger.timer[N].clear()`` function.
            - ``.count``: The ``trigger.timer[N].count`` attribute.
            - ``.delay``: The ``trigger.timer[N].delay`` attribute.
            - ``.delaylist``: The ``trigger.timer[N].delaylist`` attribute.
            - ``.overrun``: The ``trigger.timer[N].overrun`` attribute.
            - ``.passthrough``: The ``trigger.timer[N].passthrough`` attribute.
            - ``.reset()``: The ``trigger.timer[N].reset()`` function.
            - ``.stimulus``: The ``trigger.timer[N].stimulus`` attribute.
            - ``.wait()``: The ``trigger.timer[N].wait()`` function.
        """
        return self._timer

    def clear(self) -> None:
        """Run the ``trigger.clear()`` function.

        Description:
            - This function clears the command interface trigger event detector.

        TSP Syntax:
            ```
            - trigger.clear()
            ```

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

    def wait(self, timeout: float) -> str:
        """Run the ``trigger.wait()`` function.

        Description:
            - This function waits for a command interface trigger event.

        TSP Syntax:
            ```
            - trigger.wait()
            ```

        Args:
            timeout: Maximum amount of time in seconds to wait for the trigger.

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
