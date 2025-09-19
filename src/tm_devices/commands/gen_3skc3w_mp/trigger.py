# pyright: reportConstantRedefinition=none
"""The trigger commands module.

These commands are used in the following models:
MP5103

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - trigger.clear()
    - trigger.detector[N].clear()
    - trigger.detector[N].overrun
    - trigger.detector[N].stimulus
    - trigger.detector[N].wait
    - trigger.generator[N].assert()
    - trigger.timer[N].clear()
    - trigger.timer[N].count
    - trigger.timer[N].delay
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
    DefaultDictPassKeyToFactory,
    NoDeviceProvidedError,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class TriggerTimerItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``trigger.timer[N]`` command tree.

    Info:
        - ``N``, the trigger trimer number: 1 to 8.

    Constants:
        - ``.EVENT_ID``: The trigger timer event number.

    Properties and methods:
        - ``.clear()``: The ``trigger.timer[N].clear()`` function.
        - ``.count``: The ``trigger.timer[N].count`` attribute.
        - ``.delay``: The ``trigger.timer[N].delay`` attribute.
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
            - ``N``, the trigger timer number: 1 to 8.

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
            - ``N``, the trigger timer number: 1 to 8.

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
            - ``N``, the trigger timer number: 1 to 8.

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
            - ``N``, the trigger timer number: 1 to 8.

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
    def overrun(self) -> str:
        """Access the ``trigger.timer[N].overrun`` attribute.

        Description:
            - This attribute indicates if an event was ignored because of the event detector state.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].overrun)`` query.
            - Setting this property to a value will send the ``trigger.timer[N].overrun = value``
              command.

        TSP Syntax:
            ```
            - trigger.timer[N].overrun = value
            - print(trigger.timer[N].overrun)
            ```

        Info:
            - ``N``, the trigger timer number: 1 to 8.

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

    @overrun.setter
    def overrun(self, value: Union[str, float]) -> None:
        """Access the ``trigger.timer[N].overrun`` attribute.

        Description:
            - This attribute indicates if an event was ignored because of the event detector state.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].overrun)`` query.
            - Setting this property to a value will send the ``trigger.timer[N].overrun = value``
              command.

        TSP Syntax:
            ```
            - trigger.timer[N].overrun = value
            - print(trigger.timer[N].overrun)
            ```

        Info:
            - ``N``, the trigger timer number: 1 to 8.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".overrun", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.overrun = {value}"
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
            - ``N``, the trigger timer number: 1 to 8.

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
            - ``N``, the trigger timer number: 1 to 8.

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
            - ``N``, the trigger timer number: 1 to 8.

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
            - ``N``, the trigger timer number: 1 to 8.

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
            - ``N``, the trigger timer number: 1 to 8.

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
            - ``N``, the trigger timer number: 1 to 8.

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
        - ``N``, the generator number: 1 to 8.

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
            - ``N``, the generator number: 1 to 8.

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


class TriggerDetectorItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``trigger.detector[N]`` command tree.

    Info:
        - ``N``, the detector number: 1 to 8.

    Properties and methods:
        - ``.clear()``: The ``trigger.detector[N].clear()`` function.
        - ``.overrun``: The ``trigger.detector[N].overrun`` attribute.
        - ``.stimulus``: The ``trigger.detector[N].stimulus`` attribute.
        - ``.wait``: The ``trigger.detector[N].wait`` function.
    """

    @property
    def overrun(self) -> str:
        """Access the ``trigger.detector[N].overrun`` attribute.

        Description:
            - This attribute indicates if an event was ignored because of the event detector state.

        Usage:
            - Accessing this property will send the ``print(trigger.detector[N].overrun)`` query.

        TSP Syntax:
            ```
            - print(trigger.detector[N].overrun)
            ```

        Info:
            - ``N``, the detector number: 1 to 8.

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
    def stimulus(self) -> str:
        """Access the ``trigger.detector[N].stimulus`` attribute.

        Description:
            - This attribute specifies which event triggers the detector.

        Usage:
            - Accessing this property will send the ``print(trigger.detector[N].stimulus)`` query.
            - Setting this property to a value will send the
              ``trigger.detector[N].stimulus = value`` command.

        TSP Syntax:
            ```
            - trigger.detector[N].stimulus = value
            - print(trigger.detector[N].stimulus)
            ```

        Info:
            - ``N``, the detector number: 1 to 8.

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
        """Access the ``trigger.detector[N].stimulus`` attribute.

        Description:
            - This attribute specifies which event triggers the detector.

        Usage:
            - Accessing this property will send the ``print(trigger.detector[N].stimulus)`` query.
            - Setting this property to a value will send the
              ``trigger.detector[N].stimulus = value`` command.

        TSP Syntax:
            ```
            - trigger.detector[N].stimulus = value
            - print(trigger.detector[N].stimulus)
            ```

        Info:
            - ``N``, the detector number: 1 to 8.

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
        """Run the ``trigger.detector[N].clear()`` function.

        Description:
            - This command clears the trigger event detector and the overrun indicator.

        TSP Syntax:
            ```
            - trigger.detector[N].clear()
            ```

        Info:
            - ``N``, the detector number: 1 to 8.

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
        """Run the ``trigger.detector[N].wait`` function.

        Description:
            - This command waits for an event to be detected by the detector.

        TSP Syntax:
            ```
            - trigger.detector[N].wait
            ```

        Args:
            timeout: The maximum amount of time (in seconds) to wait for the trigger.

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
        - ``.EVENT_NONE``: This trigger event ID is never generated. It is used to disconnect
          stimulus inputs.

    Properties and methods:
        - ``.clear()``: The ``trigger.clear()`` function.
        - ``.detector``: The ``trigger.detector[N]`` command tree.
        - ``.generator``: The ``trigger.generator[N]`` command tree.
        - ``.timer``: The ``trigger.timer[N]`` command tree.
        - ``.wait()``: The ``trigger.wait()`` function.
    """

    EVENT_ID = "trigger.EVENT_ID"
    """str: The command interface trigger event number."""
    EVENT_NONE = "trigger.EVENT_NONE"
    """str: This trigger event ID is never generated. It is used to disconnect stimulus inputs."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "trigger") -> None:
        super().__init__(device, cmd_syntax)
        self._detector: Dict[int, TriggerDetectorItem] = DefaultDictPassKeyToFactory(
            lambda x: TriggerDetectorItem(device, f"{self._cmd_syntax}.detector[{x}]")
        )
        self._generator: Dict[int, TriggerGeneratorItem] = DefaultDictPassKeyToFactory(
            lambda x: TriggerGeneratorItem(device, f"{self._cmd_syntax}.generator[{x}]")
        )
        self._timer: Dict[int, TriggerTimerItem] = DefaultDictPassKeyToFactory(
            lambda x: TriggerTimerItem(device, f"{self._cmd_syntax}.timer[{x}]")
        )

    @property
    def detector(self) -> Dict[int, TriggerDetectorItem]:
        """Return the ``trigger.detector[N]`` command tree.

        Info:
            - ``N``, the detector number: 1 to 8.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``trigger.detector[N].clear()`` function.
            - ``.overrun``: The ``trigger.detector[N].overrun`` attribute.
            - ``.stimulus``: The ``trigger.detector[N].stimulus`` attribute.
            - ``.wait``: The ``trigger.detector[N].wait`` function.
        """
        return self._detector

    @property
    def generator(self) -> Dict[int, TriggerGeneratorItem]:
        """Return the ``trigger.generator[N]`` command tree.

        Info:
            - ``N``, the generator number: 1 to 8.

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
            - ``N``, the trigger trimer number: 1 to 8.

        Constants:
            - ``.EVENT_ID``: The trigger timer event number.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``trigger.timer[N].clear()`` function.
            - ``.count``: The ``trigger.timer[N].count`` attribute.
            - ``.delay``: The ``trigger.timer[N].delay`` attribute.
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
