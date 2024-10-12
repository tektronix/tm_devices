# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The trigger commands module.

These commands are used in the following models:
DAQ6510

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
    - trigger.continuous
    - trigger.digin[N].clear()
    - trigger.digin[N].edge
    - trigger.digin[N].overrun
    - trigger.digin[N].wait()
    - trigger.digout[N].assert()
    - trigger.digout[N].logic
    - trigger.digout[N].pulsewidth
    - trigger.digout[N].release()
    - trigger.digout[N].stimulus
    - trigger.ext.reset()
    - trigger.extin.clear()
    - trigger.extin.edge
    - trigger.extin.overrun
    - trigger.extin.wait()
    - trigger.extout.assert()
    - trigger.extout.logic
    - trigger.extout.stimulus
    - trigger.lanin[N].clear()
    - trigger.lanin[N].edge
    - trigger.lanin[N].overrun
    - trigger.lanin[N].wait()
    - trigger.lanout[N].assert()
    - trigger.lanout[N].connect()
    - trigger.lanout[N].connected
    - trigger.lanout[N].disconnect()
    - trigger.lanout[N].ipaddress
    - trigger.lanout[N].logic
    - trigger.lanout[N].protocol
    - trigger.lanout[N].stimulus
    - trigger.model.abort()
    - trigger.model.getblocklist()
    - trigger.model.getbranchcount()
    - trigger.model.initiate()
    - trigger.model.load() - ConfigList
    - trigger.model.load() - DurationLoop
    - trigger.model.load() - Empty
    - trigger.model.load() - LogicTrigger
    - trigger.model.load() - LoopUntilEvent
    - trigger.model.load() - SimpleLoop
    - trigger.model.pause()
    - trigger.model.resume()
    - trigger.model.setblock() - trigger.BLOCK_BRANCH_ALWAYS
    - trigger.model.setblock() - trigger.BLOCK_BRANCH_COUNTER
    - trigger.model.setblock() - trigger.BLOCK_BRANCH_DELTA
    - trigger.model.setblock() - trigger.BLOCK_BRANCH_LIMIT_CONSTANT
    - trigger.model.setblock() - trigger.BLOCK_BRANCH_LIMIT_DYNAMIC
    - trigger.model.setblock() - trigger.BLOCK_BRANCH_ONCE
    - trigger.model.setblock() - trigger.BLOCK_BRANCH_ONCE_EXCLUDED
    - trigger.model.setblock() - trigger.BLOCK_BRANCH_ON_EVENT
    - trigger.model.setblock() - trigger.BLOCK_BUFFER_CLEAR
    - trigger.model.setblock() - trigger.BLOCK_CONFIG_NEXT
    - trigger.model.setblock() - trigger.BLOCK_CONFIG_PREV
    - trigger.model.setblock() - trigger.BLOCK_CONFIG_RECALL
    - trigger.model.setblock() - trigger.BLOCK_DELAY_CONSTANT
    - trigger.model.setblock() - trigger.BLOCK_DELAY_DYNAMIC
    - trigger.model.setblock() - trigger.BLOCK_DIGITAL_IO
    - trigger.model.setblock() - trigger.BLOCK_LOG_EVENT
    - trigger.model.setblock() - trigger.BLOCK_MEASURE_DIGITIZE
    - trigger.model.setblock() - trigger.BLOCK_NOP
    - trigger.model.setblock() - trigger.BLOCK_NOTIFY
    - trigger.model.setblock() - trigger.BLOCK_RESET_BRANCH_COUNT
    - trigger.model.setblock() - trigger.BLOCK_WAIT
    - trigger.model.state()
    - trigger.timer[N].clear()
    - trigger.timer[N].count
    - trigger.timer[N].delay
    - trigger.timer[N].delaylist
    - trigger.timer[N].enable
    - trigger.timer[N].reset()
    - trigger.timer[N].start.fractionalseconds
    - trigger.timer[N].start.generate
    - trigger.timer[N].start.overrun
    - trigger.timer[N].start.seconds
    - trigger.timer[N].start.stimulus
    - trigger.timer[N].wait()
    - trigger.tsplinkin[N].clear()
    - trigger.tsplinkin[N].edge
    - trigger.tsplinkin[N].overrun
    - trigger.tsplinkin[N].wait()
    - trigger.tsplinkout[N].assert()
    - trigger.tsplinkout[N].logic
    - trigger.tsplinkout[N].pulsewidth
    - trigger.tsplinkout[N].release()
    - trigger.tsplinkout[N].stimulus
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


class TriggerTsplinkoutItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``trigger.tsplinkout[N]`` command tree.

    Info:
        - ``N``, the trigger line (1 to 3).

    Properties and methods:
        - ``.assert()``: The ``trigger.tsplinkout[N].assert()`` function.
        - ``.logic``: The ``trigger.tsplinkout[N].logic`` attribute.
        - ``.pulsewidth``: The ``trigger.tsplinkout[N].pulsewidth`` attribute.
        - ``.release()``: The ``trigger.tsplinkout[N].release()`` function.
        - ``.stimulus``: The ``trigger.tsplinkout[N].stimulus`` attribute.
    """

    @property
    def logic(self) -> str:
        """Access the ``trigger.tsplinkout[N].logic`` attribute.

        Description:
            - This attribute defines the trigger output with output logic for a trigger line.

        Usage:
            - Accessing this property will send the ``print(trigger.tsplinkout[N].logic)`` query.
            - Setting this property to a value will send the ``trigger.tsplinkout[N].logic = value``
              command.

        TSP Syntax:
            ```
            - trigger.tsplinkout[N].logic = value
            - print(trigger.tsplinkout[N].logic)
            ```

        Info:
            - ``N``, the trigger line (1 to 3).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".logic"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.logic)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.logic`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @logic.setter
    def logic(self, value: Union[str, float]) -> None:
        """Access the ``trigger.tsplinkout[N].logic`` attribute.

        Description:
            - This attribute defines the trigger output with output logic for a trigger line.

        Usage:
            - Accessing this property will send the ``print(trigger.tsplinkout[N].logic)`` query.
            - Setting this property to a value will send the ``trigger.tsplinkout[N].logic = value``
              command.

        TSP Syntax:
            ```
            - trigger.tsplinkout[N].logic = value
            - print(trigger.tsplinkout[N].logic)
            ```

        Info:
            - ``N``, the trigger line (1 to 3).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".logic", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.logic = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.logic`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def pulsewidth(self) -> str:
        """Access the ``trigger.tsplinkout[N].pulsewidth`` attribute.

        Description:
            - This attribute sets the length of time that the trigger line is asserted for output
              triggers.

        Usage:
            - Accessing this property will send the ``print(trigger.tsplinkout[N].pulsewidth)``
              query.
            - Setting this property to a value will send the
              ``trigger.tsplinkout[N].pulsewidth = value`` command.

        TSP Syntax:
            ```
            - trigger.tsplinkout[N].pulsewidth = value
            - print(trigger.tsplinkout[N].pulsewidth)
            ```

        Info:
            - ``width``, the pulse width (0.0 to 100 ks).
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
        """Access the ``trigger.tsplinkout[N].pulsewidth`` attribute.

        Description:
            - This attribute sets the length of time that the trigger line is asserted for output
              triggers.

        Usage:
            - Accessing this property will send the ``print(trigger.tsplinkout[N].pulsewidth)``
              query.
            - Setting this property to a value will send the
              ``trigger.tsplinkout[N].pulsewidth = value`` command.

        TSP Syntax:
            ```
            - trigger.tsplinkout[N].pulsewidth = value
            - print(trigger.tsplinkout[N].pulsewidth)
            ```

        Info:
            - ``width``, the pulse width (0.0 to 100 ks).
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
        """Access the ``trigger.tsplinkout[N].stimulus`` attribute.

        Description:
            - This attribute specifies the event that causes the synchronization line to assert a
              trigger.

        Usage:
            - Accessing this property will send the ``print(trigger.tsplinkout[N].stimulus)`` query.
            - Setting this property to a value will send the
              ``trigger.tsplinkout[N].stimulus = value`` command.

        TSP Syntax:
            ```
            - trigger.tsplinkout[N].stimulus = value
            - print(trigger.tsplinkout[N].stimulus)
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
        """Access the ``trigger.tsplinkout[N].stimulus`` attribute.

        Description:
            - This attribute specifies the event that causes the synchronization line to assert a
              trigger.

        Usage:
            - Accessing this property will send the ``print(trigger.tsplinkout[N].stimulus)`` query.
            - Setting this property to a value will send the
              ``trigger.tsplinkout[N].stimulus = value`` command.

        TSP Syntax:
            ```
            - trigger.tsplinkout[N].stimulus = value
            - print(trigger.tsplinkout[N].stimulus)
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
        """Run the ``trigger.tsplinkout[N].assert()`` function.

        Description:
            - This function simulates the occurrence of the trigger and generates the corresponding
              trigger event.

        TSP Syntax:
            ```
            - trigger.tsplinkout[N].assert()
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

    def release(self) -> None:
        """Run the ``trigger.tsplinkout[N].release()`` function.

        Description:
            - This function releases a latched trigger on the given TSP-Link trigger line.

        TSP Syntax:
            ```
            - trigger.tsplinkout[N].release()
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


class TriggerTsplinkinItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``trigger.tsplinkin[N]`` command tree.

    Info:
        - ``N``, the trigger line (1 to 3) to clear.

    Properties and methods:
        - ``.clear()``: The ``trigger.tsplinkin[N].clear()`` function.
        - ``.edge``: The ``trigger.tsplinkin[N].edge`` attribute.
        - ``.overrun``: The ``trigger.tsplinkin[N].overrun`` attribute.
        - ``.wait()``: The ``trigger.tsplinkin[N].wait()`` function.
    """

    @property
    def edge(self) -> str:
        """Access the ``trigger.tsplinkin[N].edge`` attribute.

        Description:
            - This attribute indicates which trigger edge controls the trigger event detector for a
              trigger line.

        Usage:
            - Accessing this property will send the ``print(trigger.tsplinkin[N].edge)`` query.
            - Setting this property to a value will send the ``trigger.tsplinkin[N].edge = value``
              command.

        TSP Syntax:
            ```
            - trigger.tsplinkin[N].edge = value
            - print(trigger.tsplinkin[N].edge)
            ```

        Info:
            - ``N``, the trigger line (1 to 3).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".edge"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.edge)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.edge`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @edge.setter
    def edge(self, value: Union[str, float]) -> None:
        """Access the ``trigger.tsplinkin[N].edge`` attribute.

        Description:
            - This attribute indicates which trigger edge controls the trigger event detector for a
              trigger line.

        Usage:
            - Accessing this property will send the ``print(trigger.tsplinkin[N].edge)`` query.
            - Setting this property to a value will send the ``trigger.tsplinkin[N].edge = value``
              command.

        TSP Syntax:
            ```
            - trigger.tsplinkin[N].edge = value
            - print(trigger.tsplinkin[N].edge)
            ```

        Info:
            - ``N``, the trigger line (1 to 3).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".edge", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.edge = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.edge`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def overrun(self) -> str:
        """Access the ``trigger.tsplinkin[N].overrun`` attribute.

        Description:
            - This attribute indicates if the event detector ignored an event while in the detected
              state.

        Usage:
            - Accessing this property will send the ``print(trigger.tsplinkin[N].overrun)`` query.

        TSP Syntax:
            ```
            - print(trigger.tsplinkin[N].overrun)
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

    def clear(self) -> None:
        """Run the ``trigger.tsplinkin[N].clear()`` function.

        Description:
            - This function clears the event detector for a LAN trigger.

        TSP Syntax:
            ```
            - trigger.tsplinkin[N].clear()
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

    def wait(self, timeout: float) -> str:
        """Run the ``trigger.tsplinkin[N].wait()`` function.

        Description:
            - This function waits for a trigger.

        TSP Syntax:
            ```
            - trigger.tsplinkin[N].wait()
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


class TriggerTimerItemStart(BaseTSPCmd):
    """The ``trigger.timer[N].start`` command tree.

    Info:
        - ``N``, the trigger timer number (1 to 4).

    Properties and methods:
        - ``.fractionalseconds``: The ``trigger.timer[N].start.fractionalseconds`` attribute.
        - ``.generate``: The ``trigger.timer[N].start.generate`` attribute.
        - ``.overrun``: The ``trigger.timer[N].start.overrun`` attribute.
        - ``.seconds``: The ``trigger.timer[N].start.seconds`` attribute.
        - ``.stimulus``: The ``trigger.timer[N].start.stimulus`` attribute.
    """

    @property
    def fractionalseconds(self) -> str:
        """Access the ``trigger.timer[N].start.fractionalseconds`` attribute.

        Description:
            - This attribute configures the fractional seconds of an alarm or a time in the future
              when the timer will start.

        Usage:
            - Accessing this property will send the
              ``print(trigger.timer[N].start.fractionalseconds)`` query.
            - Setting this property to a value will send the
              ``trigger.timer[N].start.fractionalseconds = value`` command.

        TSP Syntax:
            ```
            - trigger.timer[N].start.fractionalseconds = value
            - print(trigger.timer[N].start.fractionalseconds)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 4).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".fractionalseconds"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.fractionalseconds)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.fractionalseconds`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @fractionalseconds.setter
    def fractionalseconds(self, value: Union[str, float]) -> None:
        """Access the ``trigger.timer[N].start.fractionalseconds`` attribute.

        Description:
            - This attribute configures the fractional seconds of an alarm or a time in the future
              when the timer will start.

        Usage:
            - Accessing this property will send the
              ``print(trigger.timer[N].start.fractionalseconds)`` query.
            - Setting this property to a value will send the
              ``trigger.timer[N].start.fractionalseconds = value`` command.

        TSP Syntax:
            ```
            - trigger.timer[N].start.fractionalseconds = value
            - print(trigger.timer[N].start.fractionalseconds)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 4).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".fractionalseconds", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.fractionalseconds = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.fractionalseconds`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def generate(self) -> str:
        """Access the ``trigger.timer[N].start.generate`` attribute.

        Description:
            - This attribute specifies when timer events are generated.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].start.generate)``
              query.
            - Setting this property to a value will send the
              ``trigger.timer[N].start.generate = value`` command.

        TSP Syntax:
            ```
            - trigger.timer[N].start.generate = value
            - print(trigger.timer[N].start.generate)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 4).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".generate"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.generate)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.generate`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @generate.setter
    def generate(self, value: Union[str, float]) -> None:
        """Access the ``trigger.timer[N].start.generate`` attribute.

        Description:
            - This attribute specifies when timer events are generated.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].start.generate)``
              query.
            - Setting this property to a value will send the
              ``trigger.timer[N].start.generate = value`` command.

        TSP Syntax:
            ```
            - trigger.timer[N].start.generate = value
            - print(trigger.timer[N].start.generate)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 4).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".generate", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.generate = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.generate`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def overrun(self) -> str:
        """Access the ``trigger.timer[N].start.overrun`` attribute.

        Description:
            - This attribute indicates if an event was ignored because of the event detector state.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].start.overrun)`` query.

        TSP Syntax:
            ```
            - print(trigger.timer[N].start.overrun)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 4).

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
    def seconds(self) -> str:
        """Access the ``trigger.timer[N].start.seconds`` attribute.

        Description:
            - This attribute configures the seconds of an alarm or a time in the future when the
              timer will start.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].start.seconds)`` query.
            - Setting this property to a value will send the
              ``trigger.timer[N].start.seconds = value`` command.

        TSP Syntax:
            ```
            - trigger.timer[N].start.seconds = value
            - print(trigger.timer[N].start.seconds)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 4).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".seconds"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.seconds)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.seconds`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @seconds.setter
    def seconds(self, value: Union[str, float]) -> None:
        """Access the ``trigger.timer[N].start.seconds`` attribute.

        Description:
            - This attribute configures the seconds of an alarm or a time in the future when the
              timer will start.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].start.seconds)`` query.
            - Setting this property to a value will send the
              ``trigger.timer[N].start.seconds = value`` command.

        TSP Syntax:
            ```
            - trigger.timer[N].start.seconds = value
            - print(trigger.timer[N].start.seconds)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 4).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".seconds", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.seconds = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.seconds`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def stimulus(self) -> str:
        """Access the ``trigger.timer[N].start.stimulus`` attribute.

        Description:
            - This attribute describes the event that starts the trigger timer.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].start.stimulus)``
              query.
            - Setting this property to a value will send the
              ``trigger.timer[N].start.stimulus = value`` command.

        TSP Syntax:
            ```
            - trigger.timer[N].start.stimulus = value
            - print(trigger.timer[N].start.stimulus)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 4).

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
        """Access the ``trigger.timer[N].start.stimulus`` attribute.

        Description:
            - This attribute describes the event that starts the trigger timer.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].start.stimulus)``
              query.
            - Setting this property to a value will send the
              ``trigger.timer[N].start.stimulus = value`` command.

        TSP Syntax:
            ```
            - trigger.timer[N].start.stimulus = value
            - print(trigger.timer[N].start.stimulus)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 4).

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


class TriggerTimerItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``trigger.timer[N]`` command tree.

    Info:
        - ``N``, the trigger timer number (1 to 4).

    Properties and methods:
        - ``.clear()``: The ``trigger.timer[N].clear()`` function.
        - ``.count``: The ``trigger.timer[N].count`` attribute.
        - ``.delay``: The ``trigger.timer[N].delay`` attribute.
        - ``.delaylist``: The ``trigger.timer[N].delaylist`` attribute.
        - ``.enable``: The ``trigger.timer[N].enable`` attribute.
        - ``.reset()``: The ``trigger.timer[N].reset()`` function.
        - ``.start``: The ``trigger.timer[N].start`` command tree.
        - ``.wait()``: The ``trigger.timer[N].wait()`` function.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._start = TriggerTimerItemStart(device, f"{self._cmd_syntax}.start")

    @property
    def count(self) -> str:
        """Access the ``trigger.timer[N].count`` attribute.

        Description:
            - This attribute sets the number of events to generate each time the timer generates a
              trigger event or is enabled as a timer or alarm.

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
            - ``N``, the trigger timer number (1 to 4).

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
              trigger event or is enabled as a timer or alarm.

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
            - ``N``, the trigger timer number (1 to 4).

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
            - ``N``, the trigger timer number (1 to 4).

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
            - ``N``, the trigger timer number (1 to 4).

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
            - ``N``, the trigger timer number (1 to 4).

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
            - ``N``, the trigger timer number (1 to 4).

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
    def enable(self) -> str:
        """Access the ``trigger.timer[N].enable`` attribute.

        Description:
            - This attribute enables the trigger timer.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].enable)`` query.
            - Setting this property to a value will send the ``trigger.timer[N].enable = value``
              command.

        TSP Syntax:
            ```
            - trigger.timer[N].enable = value
            - print(trigger.timer[N].enable)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 4).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enable"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enable)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enable.setter
    def enable(self, value: Union[str, float]) -> None:
        """Access the ``trigger.timer[N].enable`` attribute.

        Description:
            - This attribute enables the trigger timer.

        Usage:
            - Accessing this property will send the ``print(trigger.timer[N].enable)`` query.
            - Setting this property to a value will send the ``trigger.timer[N].enable = value``
              command.

        TSP Syntax:
            ```
            - trigger.timer[N].enable = value
            - print(trigger.timer[N].enable)
            ```

        Info:
            - ``N``, the trigger timer number (1 to 4).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enable", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enable = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def start(self) -> TriggerTimerItemStart:
        """Return the ``trigger.timer[N].start`` command tree.

        Info:
            - ``N``, the trigger timer number (1 to 4).

        Sub-properties and sub-methods:
            - ``.fractionalseconds``: The ``trigger.timer[N].start.fractionalseconds`` attribute.
            - ``.generate``: The ``trigger.timer[N].start.generate`` attribute.
            - ``.overrun``: The ``trigger.timer[N].start.overrun`` attribute.
            - ``.seconds``: The ``trigger.timer[N].start.seconds`` attribute.
            - ``.stimulus``: The ``trigger.timer[N].start.stimulus`` attribute.
        """
        return self._start

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
            - ``N``, the trigger timer number (1 to 4).

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
            - This function resets trigger timer settings to their default values.

        TSP Syntax:
            ```
            - trigger.timer[N].reset()
            ```

        Info:
            - ``N``, the trigger timer number (1 to 4).

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


#  pylint: disable=too-many-public-methods
class TriggerModel(BaseTSPCmd):
    """The ``trigger.model`` command tree.

    Properties and methods:
        - ``.abort()``: The ``trigger.model.abort()`` function.
        - ``.getblocklist()``: The ``trigger.model.getblocklist()`` function.
        - ``.getbranchcount()``: The ``trigger.model.getbranchcount()`` function.
        - ``.initiate()``: The ``trigger.model.initiate()`` function.
        - ``.load_config_list()``: The ``trigger.model.load() - ConfigList`` function.
        - ``.load_duration_loop()``: The ``trigger.model.load() - DurationLoop`` function.
        - ``.load_empty()``: The ``trigger.model.load() - Empty`` function.
        - ``.load_logic_trigger()``: The ``trigger.model.load() - LogicTrigger`` function.
        - ``.load_loop_until_event()``: The ``trigger.model.load() - LoopUntilEvent`` function.
        - ``.load_simple_loop()``: The ``trigger.model.load() - SimpleLoop`` function.
        - ``.pause()``: The ``trigger.model.pause()`` function.
        - ``.resume()``: The ``trigger.model.resume()`` function.
        - ``.setblock_trigger_block_branch_always()``: The
          ``trigger.model.setblock() - trigger.BLOCK_BRANCH_ALWAYS`` function.
        - ``.setblock_trigger_block_branch_counter()``: The
          ``trigger.model.setblock() - trigger.BLOCK_BRANCH_COUNTER`` function.
        - ``.setblock_trigger_block_branch_delta()``: The
          ``trigger.model.setblock() - trigger.BLOCK_BRANCH_DELTA`` function.
        - ``.setblock_trigger_block_branch_limit_constant()``: The
          ``trigger.model.setblock() - trigger.BLOCK_BRANCH_LIMIT_CONSTANT`` function.
        - ``.setblock_trigger_block_branch_limit_dynamic()``: The
          ``trigger.model.setblock() - trigger.BLOCK_BRANCH_LIMIT_DYNAMIC`` function.
        - ``.setblock_trigger_block_branch_once()``: The
          ``trigger.model.setblock() - trigger.BLOCK_BRANCH_ONCE`` function.
        - ``.setblock_trigger_block_branch_once_excluded()``: The
          ``trigger.model.setblock() - trigger.BLOCK_BRANCH_ONCE_EXCLUDED`` function.
        - ``.setblock_trigger_block_branch_on_event()``: The
          ``trigger.model.setblock() - trigger.BLOCK_BRANCH_ON_EVENT`` function.
        - ``.setblock_trigger_block_buffer_clear()``: The
          ``trigger.model.setblock() - trigger.BLOCK_BUFFER_CLEAR`` function.
        - ``.setblock_trigger_block_config_next()``: The
          ``trigger.model.setblock() - trigger.BLOCK_CONFIG_NEXT`` function.
        - ``.setblock_trigger_block_config_prev()``: The
          ``trigger.model.setblock() - trigger.BLOCK_CONFIG_PREV`` function.
        - ``.setblock_trigger_block_config_recall()``: The
          ``trigger.model.setblock() - trigger.BLOCK_CONFIG_RECALL`` function.
        - ``.setblock_trigger_block_delay_constant()``: The
          ``trigger.model.setblock() - trigger.BLOCK_DELAY_CONSTANT`` function.
        - ``.setblock_trigger_block_delay_dynamic()``: The
          ``trigger.model.setblock() - trigger.BLOCK_DELAY_DYNAMIC`` function.
        - ``.setblock_trigger_block_digital_io()``: The
          ``trigger.model.setblock() - trigger.BLOCK_DIGITAL_IO`` function.
        - ``.setblock_trigger_block_log_event()``: The
          ``trigger.model.setblock() - trigger.BLOCK_LOG_EVENT`` function.
        - ``.setblock_trigger_block_measure_digitize()``: The
          ``trigger.model.setblock() - trigger.BLOCK_MEASURE_DIGITIZE`` function.
        - ``.setblock_trigger_block_nop()``: The ``trigger.model.setblock() - trigger.BLOCK_NOP``
          function.
        - ``.setblock_trigger_block_notify()``: The
          ``trigger.model.setblock() - trigger.BLOCK_NOTIFY`` function.
        - ``.setblock_trigger_block_reset_branch_count()``: The
          ``trigger.model.setblock() - trigger.BLOCK_RESET_BRANCH_COUNT`` function.
        - ``.setblock_trigger_block_wait()``: The ``trigger.model.setblock() - trigger.BLOCK_WAIT``
          function.
        - ``.state()``: The ``trigger.model.state()`` function.
    """

    def abort(self) -> None:
        """Run the ``trigger.model.abort()`` function.

        Description:
            - This function stops all trigger model commands and scans on the instrument.

        TSP Syntax:
            ```
            - trigger.model.abort()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.abort()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.abort()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getblocklist(self) -> str:
        """Run the ``trigger.model.getblocklist()`` function.

        Description:
            - This function returns the settings for all trigger model blocks.

        TSP Syntax:
            ```
            - trigger.model.getblocklist()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.getblocklist())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getblocklist()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getbranchcount(self, block_number: int) -> str:
        """Run the ``trigger.model.getbranchcount()`` function.

        Description:
            - This function returns the count value of the trigger model counter block.

        TSP Syntax:
            ```
            - trigger.model.getbranchcount()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.getbranchcount({block_number}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getbranchcount()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def initiate(self) -> None:
        """Run the ``trigger.model.initiate()`` function.

        Description:
            - This function starts the trigger model or scan.

        TSP Syntax:
            ```
            - trigger.model.initiate()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.initiate()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.initiate()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def load_config_list(
        self,
        measure_config_list: str,
        delay: Optional[float] = None,
        buffer_name: Optional[str] = None,
    ) -> None:
        """Run the ``trigger.model.load() - ConfigList`` function.

        Description:
            - This function loads a trigger-model template configuration that uses a measure
              configuration list.

        TSP Syntax:
            ```
            - trigger.model.load()
            ```

        Args:
            measure_config_list: A string that contains the name of the measurement configuration
                list to use.
            delay (optional): The delay time before each measurement (167 ns to 10 ks); default is 0
                for no delay.
            buffer_name (optional): The name of the reading buffer, which may be a default buffer
                (defbuffer1 or defbuffer2) or a user-defined buffer; defaults to defbuffer1.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    '"ConfigList"',
                    f'"{measure_config_list}"',
                    delay,
                    buffer_name,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.load({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.load()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def load_duration_loop(
        self, duration: float, delay: Optional[float] = None, buffer_name: Optional[str] = None
    ) -> None:
        """Run the ``trigger.model.load() - DurationLoop`` function.

        Description:
            - This function loads a trigger-model template configuration that makes continuous
              measurements for a specified amount of time.

        TSP Syntax:
            ```
            - trigger.model.load()
            ```

        Args:
            duration: The amount of time for which to make measurements (500 ns to 100 ks).
            delay (optional): The delay time before each measurement (167 ns to 10 ks); default is 0
                for no delay.
            buffer_name (optional): The name of the reading buffer, which may be a default buffer
                (defbuffer1 or defbuffer2) or a user-defined buffer; defaults to defbuffer1.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    '"DurationLoop"',
                    duration,
                    delay,
                    buffer_name,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.load({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.load()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def load_empty(self) -> None:
        """Run the ``trigger.model.load() - Empty`` function.

        Description:
            - This function clears the trigger model.

        TSP Syntax:
            ```
            - trigger.model.load()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.load()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.load()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def load_logic_trigger(
        self,
        dig_in_line: int,
        dig_out_line: int,
        count: int,
        clear: str,
        delay: Optional[float] = None,
        buffer_name: Optional[str] = None,
    ) -> None:
        """Run the ``trigger.model.load() - LogicTrigger`` function.

        Description:
            - This function loads a trigger-model template configuration that sets up a logic
              trigger through the digital or external I/O.

        TSP Syntax:
            ```
            - trigger.model.load()
            ```

        Args:
            dig_in_line: The digital input line (1 to 6) or external input line (7); also, the event
                that the trigger model will wait on in block 1.
            dig_out_line: The digital output line (1 to 6) or external input line (7).
            count: The number of measurements the instrument will make.
            clear: To clear previously detected trigger events when entering the wait block.
            delay (optional): The delay time before each measurement (167 ns to 10 ks); default is 0
                for no delay.
            buffer_name (optional): The name of the reading buffer, which may be a default buffer
                (defbuffer1 or defbuffer2) or a user-defined buffer; defaults to defbuffer1.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    '"LogicTrigger"',
                    dig_in_line,
                    dig_out_line,
                    count,
                    clear,
                    delay,
                    buffer_name,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.load({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.load()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def load_loop_until_event(
        self,
        trigger_event: str,
        position: int,
        clear: str,
        delay: Optional[float] = None,
        buffer_name: Optional[str] = None,
    ) -> None:
        """Run the ``trigger.model.load() - LoopUntilEvent`` function.

        Description:
            - This function loads a trigger-model template configuration that makes continuous
              measurements until the specified event occurs.

        TSP Syntax:
            ```
            - trigger.model.load()
            ```

        Args:
            trigger_event: The event that ends infinite triggering or readings set to occur before
                the trigger; see Details.
            position: The number of readings to make in relation to the size of the reading buffer;
                enter as a percentage (0% to 100%).
            clear: To clear previously detected trigger events when entering the wait block
                (default).
            delay (optional): The delay time before each measurement (167 ns to 10 ks); default is 0
                for no delay.
            buffer_name (optional): The name of the reading buffer, which may be a default buffer
                (defbuffer1 or defbuffer2) or a user-defined buffer; defaults to defbuffer1.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    '"LoopUntilEvent"',
                    trigger_event,
                    position,
                    clear,
                    delay,
                    buffer_name,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.load({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.load()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def load_simple_loop(
        self, count: int, delay: Optional[float] = None, buffer_name: Optional[str] = None
    ) -> None:
        """Run the ``trigger.model.load() - SimpleLoop`` function.

        Description:
            - This function loads a trigger-model template configuration that makes a specific
              number of measurements.

        TSP Syntax:
            ```
            - trigger.model.load()
            ```

        Args:
            count: The number of measurements the instrument will make.
            delay (optional): The delay time before each measurement (167 ns to 10 ks); default is 0
                for no delay.
            buffer_name (optional): Indicates the reading buffer to use; the default buffers
                (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is
                specified, defbuffer1 is used.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    '"SimpleLoop"',
                    count,
                    delay,
                    buffer_name,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.load({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.load()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def pause(self) -> None:
        """Run the ``trigger.model.pause()`` function.

        Description:
            - This function pauses a running scan or trigger model.

        TSP Syntax:
            ```
            - trigger.model.pause()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.pause()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.pause()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def resume(self) -> None:
        """Run the ``trigger.model.resume()`` function.

        Description:
            - This function continues a paused scan or trigger model.

        TSP Syntax:
            ```
            - trigger.model.resume()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.resume()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.resume()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_branch_always(self, block_number: int, branch_to_block: str) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_BRANCH_ALWAYS`` function.

        Description:
            - This function defines a trigger model block that always goes to a specific block.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            branch_to_block: The block number to execute when the trigger model reaches the Branch
                Always block.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({block_number}, "
                f"trigger.BLOCK_BRANCH_ALWAYS, "
                f"{branch_to_block})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_branch_counter(
        self, block_number: int, target_count: int, branch_to_block: str
    ) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_BRANCH_COUNTER`` function.

        Description:
            - This function defines a trigger model block that branches to a specified block a
              specified number of times.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            target_count: The number of times to repeat.
            branch_to_block: The block number of the trigger model block to execute when the counter
                is less than the targetCount value.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({block_number}, "
                f"trigger.BLOCK_BRANCH_COUNTER, "
                f"{target_count}, "
                f"{branch_to_block})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_branch_delta(
        self,
        block_number: int,
        target_difference: str,
        branch_to_block: str,
        measure_block: Optional[float] = None,
    ) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_BRANCH_DELTA`` function.

        Description:
            - This function defines a trigger model block that goes to a specified block if the
              difference of two measurements meets preset criteria.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            target_difference: The value against which the block compares the difference between the
                measurements.
            branch_to_block: The block number of the trigger model block to execute when the
                difference between the measurements is less than or equal to the targetDifference.
            measure_block (optional): The block number of the measure/digitize block that makes the
                measurements to be compared; if this is 0 or undefined, the trigger model uses the
                previous measure/digitize block.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    block_number,
                    "trigger.BLOCK_BRANCH_DELTA",
                    target_difference,
                    branch_to_block,
                    measure_block,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_branch_limit_constant(
        self,
        block_number: int,
        limit_type: float,
        limit_a: float,
        limit_b: float,
        branch_to_block: str,
        measure_block: Optional[float] = None,
    ) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_BRANCH_LIMIT_CONSTANT`` function.

        Description:
            - This function defines a trigger model block that goes to a specified block if a
              measurement meets preset criteria.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            limit_type: The type of limit, which can be one of the following types.
            limit_a: The lower limit that the measurement is tested against; if limitType is set to.
            limit_b: The upper limit that the measurement is tested against; if limitType is set to.
            branch_to_block: The block number of the trigger model block to execute when the
                measurement meets the defined criteria.
            measure_block (optional): The block number of the measure/digitize block that makes the
                measurements to be compared; if this is 0 or undefined, the trigger model uses the
                previous measure/digitize block.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    block_number,
                    "trigger.BLOCK_BRANCH_LIMIT_CONSTANT",
                    limit_type,
                    limit_a,
                    limit_b,
                    branch_to_block,
                    measure_block,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_branch_limit_dynamic(
        self,
        block_number: int,
        limit_type: float,
        limit_number: float,
        branch_to_block: str,
        measure_block: Optional[float] = None,
    ) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_BRANCH_LIMIT_DYNAMIC`` function.

        Description:
            - This function defines a trigger model block that goes to a specified block in the
              trigger model if a measurement meets user-defined criteria.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            limit_type: The type of limit, which can be one of the following types.
            limit_number: The limit number (1 or 2).
            branch_to_block: The block number of the trigger model block to execute when the
                measurement meets the criteria set in the configuration list.
            measure_block (optional): The block number of the measure/digitize block that makes the
                measurements to be compared; if this is 0 or undefined, the trigger model uses the
                previous measure/digitize block.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    block_number,
                    "trigger.BLOCK_BRANCH_LIMIT_DYNAMIC",
                    limit_type,
                    limit_number,
                    branch_to_block,
                    measure_block,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_branch_once(self, block_number: int, branch_to_block: str) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_BRANCH_ONCE`` function.

        Description:
            - This function causes the trigger model to branch to a specified building block the
              first time it is encountered in the trigger model.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            branch_to_block: The block number of the trigger model block to execute when the trigger
                model first encounters this block.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({block_number}, "
                f"trigger.BLOCK_BRANCH_ONCE, "
                f"{branch_to_block})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_branch_once_excluded(
        self, block_number: int, branch_to_block: str
    ) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_BRANCH_ONCE_EXCLUDED`` function.

        Description:
            - This function defines a trigger model block that causes the trigger model to go to a
              specified building block every time the trigger model encounters it, except for the
              first time.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            branch_to_block: The block number of the trigger model block to execute when the trigger
                model encounters this block after the first encounter.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({block_number}, "
                f"trigger.BLOCK_BRANCH_ONCE_EXCLUDED, "
                f"{branch_to_block})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_branch_on_event(
        self, block_number: int, event: str, branch_to_block: str
    ) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_BRANCH_ON_EVENT`` function.

        Description:
            - This function branches to a specified block when a specified trigger event occurs.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            event: The event that must occur before the trigger model branches the specified block.
            branch_to_block: The block number of the trigger model block to execute when the
                specified event occurs.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({block_number}, "
                f"trigger.BLOCK_BRANCH_ON_EVENT, "
                f"{event}, "
                f"{branch_to_block})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_buffer_clear(
        self, block_number: int, buffer_name: Optional[str] = None
    ) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_BUFFER_CLEAR`` function.

        Description:
            - This function defines a trigger model block that clears the reading buffer.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            buffer_name (optional): The name of the buffer, which must be an existing buffer; if no
                buffer is defined, defbuffer1 is used.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    block_number,
                    "trigger.BLOCK_BUFFER_CLEAR",
                    buffer_name,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_config_next(
        self, block_number: int, configuration_list: str
    ) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_CONFIG_NEXT`` function.

        Description:
            - This function recalls the settings at the next index of a configuration list.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            configuration_list: A string that defines the configuration list to recall.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({block_number}, "
                f"trigger.BLOCK_CONFIG_NEXT, "
                f'"{configuration_list}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_config_prev(
        self, block_number: int, configuration_list: str
    ) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_CONFIG_PREV`` function.

        Description:
            - This function defines a trigger model block that recalls the settings stored at the
              previous index in a configuration list.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            configuration_list: A string that defines the configuration list to recall.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({block_number}, "
                f"trigger.BLOCK_CONFIG_PREV, "
                f'"{configuration_list}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_config_recall(
        self, block_number: int, configuration_list: str, index: Optional[int] = None
    ) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_CONFIG_RECALL`` function.

        Description:
            - This function recalls the system settings that are stored in a configuration list.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            configuration_list: A string that defines the configuration list to recall.
            index (optional): The index in the configuration list to recall; default is 1.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    block_number,
                    "trigger.BLOCK_CONFIG_RECALL",
                    f'"{configuration_list}"',
                    index,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_delay_constant(self, block_number: int, time: str) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_DELAY_CONSTANT`` function.

        Description:
            - This function adds a constant delay to the execution of a trigger model.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            time: The amount of time to delay in seconds (167 ns to 10 ks, or 0 for no delay).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({block_number}, trigger.BLOCK_DELAY_CONSTANT, {time})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_delay_dynamic(self, block_number: int, n: int) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_DELAY_DYNAMIC`` function.

        Description:
            - This function adds a user delay to the execution of the trigger model.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            n: The number of the user delay, 1 to 5, set by dmm.measure.userdelay[N] or
                dmm.digitize.userdelay[N].

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({block_number}, trigger.BLOCK_DELAY_DYNAMIC, {n})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_digital_io(
        self, block_number: int, bit_pattern: int, bit_mask: int
    ) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_DIGITAL_IO`` function.

        Description:
            - <img id='f14261' src='notesmall_lr.png' class='linkedepsandpngtemplate' alt='VARIABLE
              - NOTE' height='17' width='41' vspace='0' hspace='0' align='bottom' border='0'>This
              command requires a communications accessory card to be installed in the instrument.
              Accessory cards include the KTTI-GPIB, KTTI-TSP, and KTTI-RS232.This function defines
              a trigger model block that sets the lines on the digital I/O port high or low.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            bit_pattern: Sets the value that specifies the output line bit pattern (0 to 63).
            bit_mask: Specifies the bit mask; if omitted, all lines are driven (0 to 63).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({block_number}, "
                f"trigger.BLOCK_DIGITAL_IO, "
                f"{bit_pattern}, "
                f"{bit_mask})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_log_event(
        self, block_number: int, event_number: int, message: str
    ) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_LOG_EVENT`` function.

        Description:
            - This function allows you to log an event in the event log when the trigger model is
              running.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            event_number: The event number.
            message: A string up to 31 characters.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({block_number}, "
                f"trigger.BLOCK_LOG_EVENT, "
                f"{event_number}, "
                f'"{message}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_measure_digitize(
        self, block_number: int, buffer_name: Optional[str] = None, count: Optional[int] = None
    ) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_MEASURE_DIGITIZE`` function.

        Description:
            - This function defines a trigger block that makes or digitizes a measurement.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            buffer_name (optional): The name of the buffer, which must be an existing buffer; if no
                buffer is defined, defbuffer1 is used.
            count (optional): The number of measure or digitize readings to make before moving to
                the next block in the trigger model; set to.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    block_number,
                    "trigger.BLOCK_MEASURE_DIGITIZE",
                    buffer_name,
                    count,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_nop(self, block_number: int) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_NOP`` function.

        Description:
            - This function creates a placeholder that performs no action in the trigger model;
              available only using remote commands.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({block_number})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_notify(self, block_number: int, n: str) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_NOTIFY`` function.

        Description:
            - This function defines a trigger model block that generates a trigger event and
              immediately continues to the next block.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            n: The identification number of the notification; 1 to 8.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({block_number}, trigger.BLOCK_NOTIFY, {n})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_reset_branch_count(self, block_number: int, counter: str) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_RESET_BRANCH_COUNT`` function.

        Description:
            - This function creates a block in the trigger model that resets a branch counter to 0.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            counter: The block number of the counter that is to be reset.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({block_number}, "
                f"trigger.BLOCK_RESET_BRANCH_COUNT, "
                f"{counter})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setblock_trigger_block_wait(
        self,
        block_number: int,
        event: str,
        clear: Optional[str] = None,
        logic: Optional[str] = None,
        event_2: Optional[str] = None,
        event_3: Optional[str] = None,
    ) -> None:
        """Run the ``trigger.model.setblock() - trigger.BLOCK_WAIT`` function.

        Description:
            - This function defines a trigger model block that waits for an event before allowing
              the trigger model to continue.

        TSP Syntax:
            ```
            - trigger.model.setblock()
            ```

        Args:
            block_number: The sequence of the block in the trigger model.
            event: The event that must occur before the trigger block allows trigger execution to
                continue (see Details).
            clear (optional): To clear previously detected trigger events when entering the wait
                block.
            logic (optional): If each event must occur before the trigger model continues.
            event_2 (optional): The event that must occur before the trigger block allows trigger
                execution to continue (see Details).
            event_3 (optional): The event that must occur before the trigger block allows trigger
                execution to continue (see Details).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    block_number,
                    "trigger.BLOCK_WAIT",
                    event,
                    clear,
                    logic,
                    event_2,
                    event_3,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setblock({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def state(self) -> str:
        """Run the ``trigger.model.state()`` function.

        Description:
            - This function returns the present state of the trigger model.

        TSP Syntax:
            ```
            - trigger.model.state()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.state())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.state()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class TriggerLanoutItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``trigger.lanout[N]`` command tree.

    Info:
        - ``N``, the LAN event number (1 to 8).

    Properties and methods:
        - ``.assert()``: The ``trigger.lanout[N].assert()`` function.
        - ``.connect()``: The ``trigger.lanout[N].connect()`` function.
        - ``.connected``: The ``trigger.lanout[N].connected`` attribute.
        - ``.disconnect()``: The ``trigger.lanout[N].disconnect()`` function.
        - ``.ipaddress``: The ``trigger.lanout[N].ipaddress`` attribute.
        - ``.logic``: The ``trigger.lanout[N].logic`` attribute.
        - ``.protocol``: The ``trigger.lanout[N].protocol`` attribute.
        - ``.stimulus``: The ``trigger.lanout[N].stimulus`` attribute.
    """

    @property
    def connected(self) -> str:
        """Access the ``trigger.lanout[N].connected`` attribute.

        Description:
            - This attribute contains the LAN event connection state.

        Usage:
            - Accessing this property will send the ``print(trigger.lanout[N].connected)`` query.

        TSP Syntax:
            ```
            - print(trigger.lanout[N].connected)
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".connected"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.connected)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.connected`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ipaddress(self) -> str:
        """Access the ``trigger.lanout[N].ipaddress`` attribute.

        Description:
            - This attribute specifies the address (in dotted-decimal format) of UDP or TCP
              listeners.

        Usage:
            - Accessing this property will send the ``print(trigger.lanout[N].ipaddress)`` query.
            - Setting this property to a value will send the ``trigger.lanout[N].ipaddress = value``
              command.

        TSP Syntax:
            ```
            - trigger.lanout[N].ipaddress = value
            - print(trigger.lanout[N].ipaddress)
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ipaddress"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ipaddress)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ipaddress`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ipaddress.setter
    def ipaddress(self, value: Union[str, float]) -> None:
        """Access the ``trigger.lanout[N].ipaddress`` attribute.

        Description:
            - This attribute specifies the address (in dotted-decimal format) of UDP or TCP
              listeners.

        Usage:
            - Accessing this property will send the ``print(trigger.lanout[N].ipaddress)`` query.
            - Setting this property to a value will send the ``trigger.lanout[N].ipaddress = value``
              command.

        TSP Syntax:
            ```
            - trigger.lanout[N].ipaddress = value
            - print(trigger.lanout[N].ipaddress)
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ipaddress", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ipaddress = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ipaddress`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def logic(self) -> str:
        """Access the ``trigger.lanout[N].logic`` attribute.

        Description:
            - This attribute sets the logic on which the trigger event detector and the output
              trigger generator operate on the given trigger line.

        Usage:
            - Accessing this property will send the ``print(trigger.lanout[N].logic)`` query.
            - Setting this property to a value will send the ``trigger.lanout[N].logic = value``
              command.

        TSP Syntax:
            ```
            - trigger.lanout[N].logic = value
            - print(trigger.lanout[N].logic)
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".logic"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.logic)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.logic`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @logic.setter
    def logic(self, value: Union[str, float]) -> None:
        """Access the ``trigger.lanout[N].logic`` attribute.

        Description:
            - This attribute sets the logic on which the trigger event detector and the output
              trigger generator operate on the given trigger line.

        Usage:
            - Accessing this property will send the ``print(trigger.lanout[N].logic)`` query.
            - Setting this property to a value will send the ``trigger.lanout[N].logic = value``
              command.

        TSP Syntax:
            ```
            - trigger.lanout[N].logic = value
            - print(trigger.lanout[N].logic)
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".logic", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.logic = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.logic`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def protocol(self) -> str:
        """Access the ``trigger.lanout[N].protocol`` attribute.

        Description:
            - This attribute sets the LAN protocol to use for sending trigger messages.

        Usage:
            - Accessing this property will send the ``print(trigger.lanout[N].protocol)`` query.
            - Setting this property to a value will send the ``trigger.lanout[N].protocol = value``
              command.

        TSP Syntax:
            ```
            - trigger.lanout[N].protocol = value
            - print(trigger.lanout[N].protocol)
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".protocol"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.protocol)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.protocol`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @protocol.setter
    def protocol(self, value: Union[str, float]) -> None:
        """Access the ``trigger.lanout[N].protocol`` attribute.

        Description:
            - This attribute sets the LAN protocol to use for sending trigger messages.

        Usage:
            - Accessing this property will send the ``print(trigger.lanout[N].protocol)`` query.
            - Setting this property to a value will send the ``trigger.lanout[N].protocol = value``
              command.

        TSP Syntax:
            ```
            - trigger.lanout[N].protocol = value
            - print(trigger.lanout[N].protocol)
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".protocol", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.protocol = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.protocol`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def stimulus(self) -> str:
        """Access the ``trigger.lanout[N].stimulus`` attribute.

        Description:
            - This attribute specifies events that cause this trigger to assert.

        Usage:
            - Accessing this property will send the ``print(trigger.lanout[N].stimulus)`` query.
            - Setting this property to a value will send the ``trigger.lanout[N].stimulus = value``
              command.

        TSP Syntax:
            ```
            - trigger.lanout[N].stimulus = value
            - print(trigger.lanout[N].stimulus)
            ```

        Info:
            - ``N``, a number specifying the trigger packet over the LAN for which to set or query
              the trigger source (1 to 8).

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
        """Access the ``trigger.lanout[N].stimulus`` attribute.

        Description:
            - This attribute specifies events that cause this trigger to assert.

        Usage:
            - Accessing this property will send the ``print(trigger.lanout[N].stimulus)`` query.
            - Setting this property to a value will send the ``trigger.lanout[N].stimulus = value``
              command.

        TSP Syntax:
            ```
            - trigger.lanout[N].stimulus = value
            - print(trigger.lanout[N].stimulus)
            ```

        Info:
            - ``N``, a number specifying the trigger packet over the LAN for which to set or query
              the trigger source (1 to 8).

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
        """Run the ``trigger.lanout[N].assert()`` function.

        Description:
            - This function simulates the occurrence of the trigger and generates the corresponding
              event.

        TSP Syntax:
            ```
            - trigger.lanout[N].assert()
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

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

    def connect(self) -> None:
        """Run the ``trigger.lanout[N].connect()`` function.

        Description:
            - This function prepares the event generator for outgoing trigger events.

        TSP Syntax:
            ```
            - trigger.lanout[N].connect()
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.connect()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.connect()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def disconnect(self) -> None:
        """Run the ``trigger.lanout[N].disconnect()`` function.

        Description:
            - This function disconnects the LAN trigger event generator.

        TSP Syntax:
            ```
            - trigger.lanout[N].disconnect()
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.disconnect()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.disconnect()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class TriggerLaninItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``trigger.lanin[N]`` command tree.

    Info:
        - ``N``, the LAN event number (1 to 8) to clear.

    Properties and methods:
        - ``.clear()``: The ``trigger.lanin[N].clear()`` function.
        - ``.edge``: The ``trigger.lanin[N].edge`` attribute.
        - ``.overrun``: The ``trigger.lanin[N].overrun`` attribute.
        - ``.wait()``: The ``trigger.lanin[N].wait()`` function.
    """

    @property
    def edge(self) -> str:
        """Access the ``trigger.lanin[N].edge`` attribute.

        Description:
            - This attribute sets the trigger operation and detection mode of the specified LAN
              event.

        Usage:
            - Accessing this property will send the ``print(trigger.lanin[N].edge)`` query.
            - Setting this property to a value will send the ``trigger.lanin[N].edge = value``
              command.

        TSP Syntax:
            ```
            - trigger.lanin[N].edge = value
            - print(trigger.lanin[N].edge)
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".edge"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.edge)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.edge`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @edge.setter
    def edge(self, value: Union[str, float]) -> None:
        """Access the ``trigger.lanin[N].edge`` attribute.

        Description:
            - This attribute sets the trigger operation and detection mode of the specified LAN
              event.

        Usage:
            - Accessing this property will send the ``print(trigger.lanin[N].edge)`` query.
            - Setting this property to a value will send the ``trigger.lanin[N].edge = value``
              command.

        TSP Syntax:
            ```
            - trigger.lanin[N].edge = value
            - print(trigger.lanin[N].edge)
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".edge", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.edge = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.edge`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def overrun(self) -> str:
        """Access the ``trigger.lanin[N].overrun`` attribute.

        Description:
            - This attribute contains the overrun status of the LAN event detector.

        Usage:
            - Accessing this property will send the ``print(trigger.lanin[N].overrun)`` query.

        TSP Syntax:
            ```
            - print(trigger.lanin[N].overrun)
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

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

    def clear(self) -> None:
        """Run the ``trigger.lanin[N].clear()`` function.

        Description:
            - This function clears the event detector for a LAN trigger.

        TSP Syntax:
            ```
            - trigger.lanin[N].clear()
            ```

        Info:
            - ``N``, the LAN event number (1 to 8) to clear.

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
        """Run the ``trigger.lanin[N].wait()`` function.

        Description:
            - This function waits for an input trigger.

        TSP Syntax:
            ```
            - trigger.lanin[N].wait()
            ```

        Args:
            timeout: Maximum amount of time in seconds to wait for the trigger event.

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


class TriggerExtout(BaseTSPCmd):
    """The ``trigger.extout`` command tree.

    Properties and methods:
        - ``.assert()``: The ``trigger.extout.assert()`` function.
        - ``.logic``: The ``trigger.extout.logic`` attribute.
        - ``.stimulus``: The ``trigger.extout.stimulus`` attribute.
    """

    @property
    def logic(self) -> str:
        """Access the ``trigger.extout.logic`` attribute.

        Description:
            - This attribute sets the output logic of the trigger event generator to positive or
              negative for the EXTERNAL TRIGGER OUT line.

        Usage:
            - Accessing this property will send the ``print(trigger.extout.logic)`` query.
            - Setting this property to a value will send the ``trigger.extout.logic = value``
              command.

        TSP Syntax:
            ```
            - trigger.extout.logic = value
            - print(trigger.extout.logic)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".logic"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.logic)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.logic`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @logic.setter
    def logic(self, value: Union[str, float]) -> None:
        """Access the ``trigger.extout.logic`` attribute.

        Description:
            - This attribute sets the output logic of the trigger event generator to positive or
              negative for the EXTERNAL TRIGGER OUT line.

        Usage:
            - Accessing this property will send the ``print(trigger.extout.logic)`` query.
            - Setting this property to a value will send the ``trigger.extout.logic = value``
              command.

        TSP Syntax:
            ```
            - trigger.extout.logic = value
            - print(trigger.extout.logic)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".logic", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.logic = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.logic`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def stimulus(self) -> str:
        """Access the ``trigger.extout.stimulus`` attribute.

        Description:
            - This attribute selects the event that causes a trigger to be asserted on the EXTERNAL
              TRIGGER OUT line.

        Usage:
            - Accessing this property will send the ``print(trigger.extout.stimulus)`` query.
            - Setting this property to a value will send the ``trigger.extout.stimulus = value``
              command.

        TSP Syntax:
            ```
            - trigger.extout.stimulus = value
            - print(trigger.extout.stimulus)
            ```

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
        """Access the ``trigger.extout.stimulus`` attribute.

        Description:
            - This attribute selects the event that causes a trigger to be asserted on the EXTERNAL
              TRIGGER OUT line.

        Usage:
            - Accessing this property will send the ``print(trigger.extout.stimulus)`` query.
            - Setting this property to a value will send the ``trigger.extout.stimulus = value``
              command.

        TSP Syntax:
            ```
            - trigger.extout.stimulus = value
            - print(trigger.extout.stimulus)
            ```

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
        """Run the ``trigger.extout.assert()`` function.

        Description:
            - This function asserts a trigger on the EXTERNAL TRIGGER OUT line.

        TSP Syntax:
            ```
            - trigger.extout.assert()
            ```

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


class TriggerExtin(BaseTSPCmd):
    """The ``trigger.extin`` command tree.

    Properties and methods:
        - ``.clear()``: The ``trigger.extin.clear()`` function.
        - ``.edge``: The ``trigger.extin.edge`` attribute.
        - ``.overrun``: The ``trigger.extin.overrun`` attribute.
        - ``.wait()``: The ``trigger.extin.wait()`` function.
    """

    @property
    def edge(self) -> str:
        """Access the ``trigger.extin.edge`` attribute.

        Description:
            - This attribute sets the type of edge that is detected as an input on the EXTERNAL
              TRIGGER IN trigger line.

        Usage:
            - Accessing this property will send the ``print(trigger.extin.edge)`` query.
            - Setting this property to a value will send the ``trigger.extin.edge = value`` command.

        TSP Syntax:
            ```
            - trigger.extin.edge = value
            - print(trigger.extin.edge)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".edge"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.edge)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.edge`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @edge.setter
    def edge(self, value: Union[str, float]) -> None:
        """Access the ``trigger.extin.edge`` attribute.

        Description:
            - This attribute sets the type of edge that is detected as an input on the EXTERNAL
              TRIGGER IN trigger line.

        Usage:
            - Accessing this property will send the ``print(trigger.extin.edge)`` query.
            - Setting this property to a value will send the ``trigger.extin.edge = value`` command.

        TSP Syntax:
            ```
            - trigger.extin.edge = value
            - print(trigger.extin.edge)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".edge", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.edge = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.edge`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def overrun(self) -> str:
        """Access the ``trigger.extin.overrun`` attribute.

        Description:
            - This attribute returns the event detector overrun status.

        Usage:
            - Accessing this property will send the ``print(trigger.extin.overrun)`` query.

        TSP Syntax:
            ```
            - print(trigger.extin.overrun)
            ```

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

    def clear(self) -> None:
        """Run the ``trigger.extin.clear()`` function.

        Description:
            - This function clears the trigger event on the EXTERNAL TRIGGER IN line.

        TSP Syntax:
            ```
            - trigger.extin.clear()
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
        """Run the ``trigger.extin.wait()`` function.

        Description:
            - This function waits for a trigger.

        TSP Syntax:
            ```
            - trigger.extin.wait()
            ```

        Args:
            timeout: Timeout in seconds.

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


class TriggerExt(BaseTSPCmd):
    """The ``trigger.ext`` command tree.

    Properties and methods:
        - ``.reset()``: The ``trigger.ext.reset()`` function.
    """

    def reset(self) -> None:
        """Run the ``trigger.ext.reset()`` function.

        Description:
            - This function resets the edge, logic, and stimulus values for the EXTERNAL TRIGGER IN
              and EXTERNAL TRIGGER OUT lines to their default values.

        TSP Syntax:
            ```
            - trigger.ext.reset()
            ```

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


class TriggerDigoutItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``trigger.digout[N]`` command tree.

    Info:
        - ``N``, the digital I/O trigger line (1 to 6).

    Properties and methods:
        - ``.assert()``: The ``trigger.digout[N].assert()`` function.
        - ``.logic``: The ``trigger.digout[N].logic`` attribute.
        - ``.pulsewidth``: The ``trigger.digout[N].pulsewidth`` attribute.
        - ``.release()``: The ``trigger.digout[N].release()`` function.
        - ``.stimulus``: The ``trigger.digout[N].stimulus`` attribute.
    """

    @property
    def logic(self) -> str:
        """Access the ``trigger.digout[N].logic`` attribute.

        Description:
            - This attribute sets the output logic of the trigger event generator to positive or
              negative for the specified line.

        Usage:
            - Accessing this property will send the ``print(trigger.digout[N].logic)`` query.
            - Setting this property to a value will send the ``trigger.digout[N].logic = value``
              command.

        TSP Syntax:
            ```
            - trigger.digout[N].logic = value
            - print(trigger.digout[N].logic)
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".logic"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.logic)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.logic`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @logic.setter
    def logic(self, value: Union[str, float]) -> None:
        """Access the ``trigger.digout[N].logic`` attribute.

        Description:
            - This attribute sets the output logic of the trigger event generator to positive or
              negative for the specified line.

        Usage:
            - Accessing this property will send the ``print(trigger.digout[N].logic)`` query.
            - Setting this property to a value will send the ``trigger.digout[N].logic = value``
              command.

        TSP Syntax:
            ```
            - trigger.digout[N].logic = value
            - print(trigger.digout[N].logic)
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".logic", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.logic = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.logic`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def pulsewidth(self) -> str:
        """Access the ``trigger.digout[N].pulsewidth`` attribute.

        Description:
            - <img id='f14261' src='notesmall_lr.png' class='linkedepsandpngtemplate' alt='VARIABLE
              - NOTE' height='17' width='41' vspace='0' hspace='0' align='bottom' border='0'>This
              command requires a communications accessory card to be installed in the instrument.
              Accessory cards include the KTTI-GPIB, KTTI-TSP, and KTTI-RS232.This attribute
              describes the length of time that the trigger line is asserted for output triggers.

        Usage:
            - Accessing this property will send the ``print(trigger.digout[N].pulsewidth)`` query.
            - Setting this property to a value will send the
              ``trigger.digout[N].pulsewidth = value`` command.

        TSP Syntax:
            ```
            - trigger.digout[N].pulsewidth = value
            - print(trigger.digout[N].pulsewidth)
            ```

        Info:
            - ``width``, the pulse width (0 to 100 ks).
            - ``N``, the digital I/O trigger line (1 to 6).

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
        """Access the ``trigger.digout[N].pulsewidth`` attribute.

        Description:
            - <img id='f14261' src='notesmall_lr.png' class='linkedepsandpngtemplate' alt='VARIABLE
              - NOTE' height='17' width='41' vspace='0' hspace='0' align='bottom' border='0'>This
              command requires a communications accessory card to be installed in the instrument.
              Accessory cards include the KTTI-GPIB, KTTI-TSP, and KTTI-RS232.This attribute
              describes the length of time that the trigger line is asserted for output triggers.

        Usage:
            - Accessing this property will send the ``print(trigger.digout[N].pulsewidth)`` query.
            - Setting this property to a value will send the
              ``trigger.digout[N].pulsewidth = value`` command.

        TSP Syntax:
            ```
            - trigger.digout[N].pulsewidth = value
            - print(trigger.digout[N].pulsewidth)
            ```

        Info:
            - ``width``, the pulse width (0 to 100 ks).
            - ``N``, the digital I/O trigger line (1 to 6).

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
        """Access the ``trigger.digout[N].stimulus`` attribute.

        Description:
            - This attribute selects the event that causes a trigger to be asserted on the digital
              output line.

        Usage:
            - Accessing this property will send the ``print(trigger.digout[N].stimulus)`` query.
            - Setting this property to a value will send the ``trigger.digout[N].stimulus = value``
              command.

        TSP Syntax:
            ```
            - trigger.digout[N].stimulus = value
            - print(trigger.digout[N].stimulus)
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 6).

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
        """Access the ``trigger.digout[N].stimulus`` attribute.

        Description:
            - This attribute selects the event that causes a trigger to be asserted on the digital
              output line.

        Usage:
            - Accessing this property will send the ``print(trigger.digout[N].stimulus)`` query.
            - Setting this property to a value will send the ``trigger.digout[N].stimulus = value``
              command.

        TSP Syntax:
            ```
            - trigger.digout[N].stimulus = value
            - print(trigger.digout[N].stimulus)
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 6).

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
        """Run the ``trigger.digout[N].assert()`` function.

        Description:
            - This function asserts a trigger pulse on one of the digital I/O lines.

        TSP Syntax:
            ```
            - trigger.digout[N].assert()
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 6).

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

    def release(self) -> None:
        """Run the ``trigger.digout[N].release()`` function.

        Description:
            - This function releases an indefinite length or latched trigger.

        TSP Syntax:
            ```
            - trigger.digout[N].release()
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 6).

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


class TriggerDiginItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``trigger.digin[N]`` command tree.

    Info:
        - ``N``, the digital I/O trigger line (1 to 6).

    Properties and methods:
        - ``.clear()``: The ``trigger.digin[N].clear()`` function.
        - ``.edge``: The ``trigger.digin[N].edge`` attribute.
        - ``.overrun``: The ``trigger.digin[N].overrun`` attribute.
        - ``.wait()``: The ``trigger.digin[N].wait()`` function.
    """

    @property
    def edge(self) -> str:
        """Access the ``trigger.digin[N].edge`` attribute.

        Description:
            - This attribute sets the edge used by the trigger event detector on the given trigger
              line.

        Usage:
            - Accessing this property will send the ``print(trigger.digin[N].edge)`` query.
            - Setting this property to a value will send the ``trigger.digin[N].edge = value``
              command.

        TSP Syntax:
            ```
            - trigger.digin[N].edge = value
            - print(trigger.digin[N].edge)
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".edge"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.edge)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.edge`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @edge.setter
    def edge(self, value: Union[str, float]) -> None:
        """Access the ``trigger.digin[N].edge`` attribute.

        Description:
            - This attribute sets the edge used by the trigger event detector on the given trigger
              line.

        Usage:
            - Accessing this property will send the ``print(trigger.digin[N].edge)`` query.
            - Setting this property to a value will send the ``trigger.digin[N].edge = value``
              command.

        TSP Syntax:
            ```
            - trigger.digin[N].edge = value
            - print(trigger.digin[N].edge)
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".edge", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.edge = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.edge`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def overrun(self) -> str:
        """Access the ``trigger.digin[N].overrun`` attribute.

        Description:
            - This attribute returns the event detector overrun status.

        Usage:
            - Accessing this property will send the ``print(trigger.digin[N].overrun)`` query.

        TSP Syntax:
            ```
            - print(trigger.digin[N].overrun)
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 6).

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

    def clear(self) -> None:
        """Run the ``trigger.digin[N].clear()`` function.

        Description:
            - <img id='f14261' src='notesmall_lr.png' class='linkedepsandpngtemplate' alt='VARIABLE
              - NOTE' height='17' width='41' vspace='0' hspace='0' align='bottom' border='0'>This
              command requires a communications accessory card to be installed in the instrument.
              Accessory cards include the KTTI-GPIB, KTTI-TSP, and KTTI-RS232.This function clears
              the trigger event on a digital input line.

        TSP Syntax:
            ```
            - trigger.digin[N].clear()
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 6).

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
        """Run the ``trigger.digin[N].wait()`` function.

        Description:
            - This function waits for a trigger.

        TSP Syntax:
            ```
            - trigger.digin[N].wait()
            ```

        Args:
            timeout: Timeout in seconds.

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


class TriggerBlenderItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``trigger.blender[N]`` command tree.

    Info:
        - ``N``, the blender number (up to two).

    Properties and methods:
        - ``.clear()``: The ``trigger.blender[N].clear()`` function.
        - ``.orenable``: The ``trigger.blender[N].orenable`` attribute.
        - ``.overrun``: The ``trigger.blender[N].overrun`` attribute.
        - ``.reset()``: The ``trigger.blender[N].reset()`` function.
        - ``.stimulus``: The ``trigger.blender[N].stimulus[M]`` attribute.
        - ``.wait()``: The ``trigger.blender[N].wait()`` function.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
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
            - ``N``, the blender number (up to two).

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
            - ``N``, the blender number (up to two).

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
            - ``N``, the blender number (up to two).

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
            - ``N``, the an integer that represents the trigger event blender (up to two).
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
            - ``N``, the blender number (up to two).

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
            - ``N``, the trigger event blender (up to two).

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


#  pylint: disable=too-many-instance-attributes
class Trigger(BaseTSPCmd):
    """The ``trigger`` command tree.

    Constants:
        - ``.BLOCK_BRANCH_ALWAYS``: Defines a trigger model block that always goes to a specific
          block.
        - ``.BLOCK_BRANCH_COUNTER``: Defines a trigger model block that branches to a specified
          block a specified number of times.
        - ``.BLOCK_BRANCH_DELTA``: Defines a trigger model block that goes to a specified block if
          the difference of two measurements meets preset criteria.
        - ``.BLOCK_BRANCH_LIMIT_CONSTANT``: Defines a trigger model block that goes to a specified
          block if a measurement meets preset criteria.
        - ``.BLOCK_BRANCH_LIMIT_DYNAMIC``: Defines a trigger model block that goes to a specified
          block in the trigger model if a measurement meets user-defined criteria.
        - ``.BLOCK_BRANCH_ONCE``: Causes the trigger model to branch to a specified building block
          the first time it is encountered in the trigger model.
        - ``.BLOCK_BRANCH_ONCE_EXCLUDED``: Causes the trigger model to go to a specified building
          block every time the trigger model encounters it, except for the first time.
        - ``.BLOCK_BRANCH_ON_EVENT``: Branches to a specified block when a specified trigger event
          occurs.
        - ``.BLOCK_BUFFER_CLEAR``: Defines a trigger model block that clears the reading buffer.
        - ``.BLOCK_CONFIG_NEXT``: Recalls the settings at the next index of a configuration list.
        - ``.BLOCK_CONFIG_PREV``: Recalls the settings stored at the previous  index of a
          configuration list.
        - ``.BLOCK_DELAY_CONSTANT``: Adds a constant delay to the execution of a trigger model.
        - ``.BLOCK_DELAY_DYNAMIC``: Adds a user delay to the execution of the trigger model.
        - ``.BLOCK_DIGITAL_IO``: Defines a trigger model block that sets the lines on the digital
          I/O port high or low.
        - ``.BLOCK_LOG_EVENT``: Allows you to log an event in the event log when the trigger model
          is running.
        - ``.BLOCK_MEASURE``: Deprecated; use trigger.BLOCK_MEASURE_DIGITIZE instead.
        - ``.BLOCK_MEASURE_DIGITIZE``: defines a trigger block that makes or digitizes a
          measurement.
        - ``.BLOCK_NOP``: Creates a placeholder that performs no action in the trigger model.
        - ``.BLOCK_NOTIFY``: Defines a trigger-model block that generates a trigger event and
          immediately continues to the next block.
        - ``.BLOCK_RESET_BRANCH_COUNT``: Creates a block in the trigger model that resets a branch
          counter to 0.
        - ``.BLOCK_WAIT``: Defines a trigger model block that waits for an event before allowing the
          trigger model to continue.
        - ``.CLEAR_ENTER``: Clear previously detected trigger events when entering the wait block.
        - ``.CLEAR_NEVER``: Immediately act on any previously detected triggers and not clear them
          (default).
        - ``.CONT_AUTO``: Start continuous measurements after boot.
        - ``.CONT_OFF``: Do not start continuous measurements after boot.
        - ``.CONT_RESTART``: Place the instrument into local control and start continuous
          measurements after boot.
        - ``.COUNT_AUTO``: Use most recent count value.
        - ``.COUNT_INFINITE``: Infinite (run continuously until stopped).
        - ``.COUNT_STOP``: Stop infinite to stop the block.
        - ``.EDGE_EITHER``: Sets the selected trigger line to detect either rising-edge or
          falling-edge triggers as input when the line is configured as an input or open drain.
        - ``.EDGE_FALLING``: Sets the selected trigger line to detect falling-edge triggers as input
          when the line is configured as an input or open drain.
        - ``.EDGE_RISING``: Sets the selected trigger line to detect rising-edge triggers as input
          when the line is configured as an input or open drain.
        - ``.EVENT_ANALOGTRIGGER``: Analog trigger.
        - ``.EVENT_BLENDERN``: Trigger event blender N (1 to 2), which combines trigger events.
        - ``.EVENT_COMMAND``: A command interface trigger.
        - ``.EVENT_DIGION``: Line edge (either rising, falling, or either based on the configuration
          of the line) detected on digital input line N (1 to 6).
        - ``.EVENT_DISPLAY``: Front-panel TRIGGER key press.
        - ``.EVENT_EXTERNAL``: External in trigger.
        - ``.EVENT_LANN``: Appropriate LXI trigger packet is received on LAN trigger object N (1 to
          8).
        - ``.EVENT_NONE``: No trigger event.
        - ``.EVENT_NOTIFYN``: Notify trigger block N (1 to 3) generates a trigger event when the
          trigger model executes it.
        - ``.EVENT_SCAN_ALARM_LIMIT``: Limit value for scan reached (returns trigger.EVENT_NOTIFY3).
        - ``.EVENT_SCAN_CHANNEL_READY``: Channel closed (returns trigger.EVENT_NOTIFY6).
        - ``.EVENT_SCAN_COMPLETE``: Scan completed (returns trigger.EVENT_NOTIFY8).
        - ``.EVENT_SCAN_MEASURE_COMPLETE``: Measure completed (returns trigger.EVENT_NOTIFY7).
        - ``.EVENT_TIMER1``: Trigger timer 1 expired.
        - ``.EVENT_TIMER2``: Trigger timer 2 expired.
        - ``.EVENT_TIMER3``: Trigger timer 3 expired.
        - ``.EVENT_TIMER4``: Trigger timer 4 expired.
        - ``.EVENT_TIMERN``: Trigger timer N (1 to 4) expired.
        - ``.EVENT_TSPLINKN``: Line edge detected on TSP-Link synchronization line N (1 to 3).
        - ``.LIMIT_ABOVE``: The measurement is above the value set by limit B; limit A must be set,
          but is ignored when this type is selected.
        - ``.LIMIT_BELOW``: The measurement is below the value set by limit A; limit B must be set,
          but is ignored when this type is selected.
        - ``.LIMIT_INSIDE``: The measurement is inside the values set by limits A and B; limit A
          must be the low value and Limit B must be the high value.
        - ``.LIMIT_OUTSIDE``: The measurement is outside the values set by limits A and B; limit A
          must be the low value and Limit B must be the high value.
        - ``.LOGIC_NEGATIVE``: Asserts a TTL-low pulse for the output logic of the trigger event
          generator for the specified line.
        - ``.LOGIC_POSITIVE``: Asserts a TTL-high pulse for the output logic of the trigger event
          generator for the specified line.
        - ``.LOG_ERROR1``: Log error event 1 in the event log when trigger model execution reaches
          this block.
        - ``.LOG_ERROR2``: Log error event 2 in the event log when trigger model execution reaches
          this block.
        - ``.LOG_ERROR3``: Log error event 3 in the event log when trigger model execution reaches
          this block.
        - ``.LOG_ERROR4``: Log error event 4 in the event log when trigger model execution reaches
          this block.
        - ``.LOG_INFO1``: Log information event 1 in the event log when trigger model execution
          reaches this block.
        - ``.LOG_INFO2``: Log information event 2 in the event log when trigger model execution
          reaches this block.
        - ``.LOG_INFO3``: Log information event 3 in the event log when trigger model execution
          reaches this block.
        - ``.LOG_INFO4``: Log information event 4 in the event log when trigger model execution
          reaches this block.
        - ``.LOG_WARN1``: Log warning event 1 in the event log when trigger model execution reaches
          this block.
        - ``.LOG_WARN2``: Log warning event 2 in the event log when trigger model execution reaches
          this block.
        - ``.LOG_WARN3``: Log warning event 3 in the event log when trigger model execution reaches
          this block.
        - ``.LOG_WARN4``: Log warning event 4 in the event log when trigger model execution reaches
          this block.
        - ``.LOG_WARN_ABORT``: Abort the trigger model immediately and post a warning event log
          message.
        - ``.OFF``: Disable the trigger timer.
        - ``.ON``: Enable the trigger timer.
        - ``.SCAN_ALARM_LIMIT``: Scan alarm limit exceeded.
        - ``.STATE_ABORTED``: The trigger model is stopped.
        - ``.STATE_ABORTING``: The trigger model is stopping.
        - ``.STATE_BUILDING``: Blocks have been added.
        - ``.STATE_EMPTY``: The trigger model is selected, but no blocks are defined.
        - ``.STATE_FAILED``: The trigger model is stopped because of an error.
        - ``.STATE_IDLE``: The trigger model is stopped.
        - ``.STATE_RUNNING``: The trigger model is running.
        - ``.STATE_WAITING``: The trigger model has been in the same wait block for more than 100
          ms.
        - ``.WAIT_AND``: Each event must occur before the trigger model continues.
        - ``.WAIT_OR``: At least one of the events must occur before the trigger model continues.

    Properties and methods:
        - ``.blender``: The ``trigger.blender[N]`` command tree.
        - ``.clear()``: The ``trigger.clear()`` function.
        - ``.continuous``: The ``trigger.continuous`` attribute.
        - ``.digin``: The ``trigger.digin[N]`` command tree.
        - ``.digout``: The ``trigger.digout[N]`` command tree.
        - ``.ext``: The ``trigger.ext`` command tree.
        - ``.extin``: The ``trigger.extin`` command tree.
        - ``.extout``: The ``trigger.extout`` command tree.
        - ``.lanin``: The ``trigger.lanin[N]`` command tree.
        - ``.lanout``: The ``trigger.lanout[N]`` command tree.
        - ``.model``: The ``trigger.model`` command tree.
        - ``.timer``: The ``trigger.timer[N]`` command tree.
        - ``.tsplinkin``: The ``trigger.tsplinkin[N]`` command tree.
        - ``.tsplinkout``: The ``trigger.tsplinkout[N]`` command tree.
        - ``.wait()``: The ``trigger.wait()`` function.
    """

    BLOCK_BRANCH_ALWAYS = "trigger.BLOCK_BRANCH_ALWAYS"
    """str: Defines a trigger model block that always goes to a specific block."""
    BLOCK_BRANCH_COUNTER = "trigger.BLOCK_BRANCH_COUNTER"
    """str: Defines a trigger model block that branches to a specified block a specified number of times."""  # noqa: E501
    BLOCK_BRANCH_DELTA = "trigger.BLOCK_BRANCH_DELTA"
    """str: Defines a trigger model block that goes to a specified block if the difference of two measurements meets preset criteria."""  # noqa: E501
    BLOCK_BRANCH_LIMIT_CONSTANT = "trigger.BLOCK_BRANCH_LIMIT_CONSTANT"
    """str: Defines a trigger model block that goes to a specified block if a measurement meets preset criteria."""  # noqa: E501
    BLOCK_BRANCH_LIMIT_DYNAMIC = "trigger.BLOCK_BRANCH_LIMIT_DYNAMIC"
    """str: Defines a trigger model block that goes to a specified block in the trigger model if a measurement meets user-defined criteria."""  # noqa: E501
    BLOCK_BRANCH_ONCE = "trigger.BLOCK_BRANCH_ONCE"
    """str: Causes the trigger model to branch to a specified building block the first time it is encountered in the trigger model."""  # noqa: E501
    BLOCK_BRANCH_ONCE_EXCLUDED = "trigger.BLOCK_BRANCH_ONCE_EXCLUDED"
    """str: Causes the trigger model to go to a specified building block every time the trigger model encounters it, except for the first time."""  # noqa: E501
    BLOCK_BRANCH_ON_EVENT = "trigger.BLOCK_BRANCH_ON_EVENT"
    """str: Branches to a specified block when a specified trigger event occurs."""
    BLOCK_BUFFER_CLEAR = "trigger.BLOCK_BUFFER_CLEAR"
    """str: Defines a trigger model block that clears the reading buffer."""
    BLOCK_CONFIG_NEXT = "trigger.BLOCK_CONFIG_NEXT"
    """str: Recalls the settings at the next index of a configuration list."""
    BLOCK_CONFIG_PREV = "trigger.BLOCK_CONFIG_PREV"
    """str: Recalls the settings stored at the previous  index of a configuration list."""
    BLOCK_DELAY_CONSTANT = "trigger.BLOCK_DELAY_CONSTANT"
    """str: Adds a constant delay to the execution of a trigger model."""
    BLOCK_DELAY_DYNAMIC = "trigger.BLOCK_DELAY_DYNAMIC"
    """str: Adds a user delay to the execution of the trigger model."""
    BLOCK_DIGITAL_IO = "trigger.BLOCK_DIGITAL_IO"
    """str: Defines a trigger model block that sets the lines on the digital I/O port high or low."""  # noqa: E501
    BLOCK_LOG_EVENT = "trigger.BLOCK_LOG_EVENT"
    """str: Allows you to log an event in the event log when the trigger model is running."""
    BLOCK_MEASURE = "trigger.BLOCK_MEASURE"
    """str: Deprecated; use trigger.BLOCK_MEASURE_DIGITIZE instead."""
    BLOCK_MEASURE_DIGITIZE = "trigger.BLOCK_MEASURE_DIGITIZE"
    """str: defines a trigger block that makes or digitizes a measurement."""
    BLOCK_NOP = "trigger.BLOCK_NOP"
    """str: Creates a placeholder that performs no action in the trigger model."""
    BLOCK_NOTIFY = "trigger.BLOCK_NOTIFY"
    """str: Defines a trigger-model block that generates a trigger event and immediately continues to the next block."""  # noqa: E501
    BLOCK_RESET_BRANCH_COUNT = "trigger.BLOCK_RESET_BRANCH_COUNT"
    """str: Creates a block in the trigger model that resets a branch counter to 0."""
    BLOCK_WAIT = "trigger.BLOCK_WAIT"
    """str: Defines a trigger model block that waits for an event before allowing the trigger model to continue."""  # noqa: E501
    CLEAR_ENTER = "trigger.CLEAR_ENTER"
    """str: Clear previously detected trigger events when entering the wait block."""
    CLEAR_NEVER = "trigger.CLEAR_NEVER"
    """str: Immediately act on any previously detected triggers and not clear them (default)."""
    CONT_AUTO = "trigger.CONT_AUTO"
    """str: Start continuous measurements after boot."""
    CONT_OFF = "trigger.CONT_OFF"
    """str: Do not start continuous measurements after boot."""
    CONT_RESTART = "trigger.CONT_RESTART"
    """str: Place the instrument into local control and start continuous measurements after boot."""
    COUNT_AUTO = "trigger.COUNT_AUTO"
    """str: Use most recent count value."""
    COUNT_INFINITE = "trigger.COUNT_INFINITE"
    """str: Infinite (run continuously until stopped)."""
    COUNT_STOP = "trigger.COUNT_STOP"
    """str: Stop infinite to stop the block."""
    EDGE_EITHER = "trigger.EDGE_EITHER"
    """str: Sets the selected trigger line to detect either rising-edge or falling-edge triggers as input when the line is configured as an input or open drain."""  # noqa: E501
    EDGE_FALLING = "trigger.EDGE_FALLING"
    """str: Sets the selected trigger line to detect falling-edge triggers as input when the line is configured as an input or open drain."""  # noqa: E501
    EDGE_RISING = "trigger.EDGE_RISING"
    """str: Sets the selected trigger line to detect rising-edge triggers as input when the line is configured as an input or open drain."""  # noqa: E501
    EVENT_ANALOGTRIGGER = "trigger.EVENT_ANALOGTRIGGER"
    """str: Analog trigger."""
    EVENT_BLENDERN = "trigger.EVENT_BLENDERN"
    """str: Trigger event blender N (1 to 2), which combines trigger events."""
    EVENT_COMMAND = "trigger.EVENT_COMMAND"
    """str: A command interface trigger."""
    EVENT_DIGION = "trigger.EVENT_DIGION"
    """str: Line edge (either rising, falling, or either based on the configuration of the line) detected on digital input line N (1 to 6)."""  # noqa: E501
    EVENT_DISPLAY = "trigger.EVENT_DISPLAY"
    """str: Front-panel TRIGGER key press."""
    EVENT_EXTERNAL = "trigger.EVENT_EXTERNAL"
    """str: External in trigger."""
    EVENT_LANN = "trigger.EVENT_LANN"
    """str: Appropriate LXI trigger packet is received on LAN trigger object N (1 to 8)."""
    EVENT_NONE = "trigger.EVENT_NONE"
    """str: No trigger event."""
    EVENT_NOTIFYN = "trigger.EVENT_NOTIFYN"
    """str: Notify trigger block N (1 to 3) generates a trigger event when the trigger model executes it."""  # noqa: E501
    EVENT_SCAN_ALARM_LIMIT = "trigger.EVENT_SCAN_ALARM_LIMIT"
    """str: Limit value for scan reached (returns trigger.EVENT_NOTIFY3)."""
    EVENT_SCAN_CHANNEL_READY = "trigger.EVENT_SCAN_CHANNEL_READY"
    """str: Channel closed (returns trigger.EVENT_NOTIFY6)."""
    EVENT_SCAN_COMPLETE = "trigger.EVENT_SCAN_COMPLETE"
    """str: Scan completed (returns trigger.EVENT_NOTIFY8)."""
    EVENT_SCAN_MEASURE_COMPLETE = "trigger.EVENT_SCAN_MEASURE_COMPLETE"
    """str: Measure completed (returns trigger.EVENT_NOTIFY7)."""
    EVENT_TIMER1 = "trigger.EVENT_TIMER1"
    """str: Trigger timer 1 expired."""
    EVENT_TIMER2 = "trigger.EVENT_TIMER2"
    """str: Trigger timer 2 expired."""
    EVENT_TIMER3 = "trigger.EVENT_TIMER3"
    """str: Trigger timer 3 expired."""
    EVENT_TIMER4 = "trigger.EVENT_TIMER4"
    """str: Trigger timer 4 expired."""
    EVENT_TIMERN = "trigger.EVENT_TIMERN"
    """str: Trigger timer N (1 to 4) expired."""
    EVENT_TSPLINKN = "trigger.EVENT_TSPLINKN"
    """str: Line edge detected on TSP-Link synchronization line N (1 to 3)."""
    LIMIT_ABOVE = "trigger.LIMIT_ABOVE"
    """str: The measurement is above the value set by limit B; limit A must be set, but is ignored when this type is selected."""  # noqa: E501
    LIMIT_BELOW = "trigger.LIMIT_BELOW"
    """str: The measurement is below the value set by limit A; limit B must be set, but is ignored when this type is selected."""  # noqa: E501
    LIMIT_INSIDE = "trigger.LIMIT_INSIDE"
    """str: The measurement is inside the values set by limits A and B; limit A must be the low value and Limit B must be the high value."""  # noqa: E501
    LIMIT_OUTSIDE = "trigger.LIMIT_OUTSIDE"
    """str: The measurement is outside the values set by limits A and B; limit A must be the low value and Limit B must be the high value."""  # noqa: E501
    LOGIC_NEGATIVE = "trigger.LOGIC_NEGATIVE"
    """str: Asserts a TTL-low pulse for the output logic of the trigger event generator for the specified line."""  # noqa: E501
    LOGIC_POSITIVE = "trigger.LOGIC_POSITIVE"
    """str: Asserts a TTL-high pulse for the output logic of the trigger event generator for the specified line."""  # noqa: E501
    LOG_ERROR1 = "trigger.LOG_ERROR1"
    """str: Log error event 1 in the event log when trigger model execution reaches this block."""
    LOG_ERROR2 = "trigger.LOG_ERROR2"
    """str: Log error event 2 in the event log when trigger model execution reaches this block."""
    LOG_ERROR3 = "trigger.LOG_ERROR3"
    """str: Log error event 3 in the event log when trigger model execution reaches this block."""
    LOG_ERROR4 = "trigger.LOG_ERROR4"
    """str: Log error event 4 in the event log when trigger model execution reaches this block."""
    LOG_INFO1 = "trigger.LOG_INFO1"
    """str: Log information event 1 in the event log when trigger model execution reaches this block."""  # noqa: E501
    LOG_INFO2 = "trigger.LOG_INFO2"
    """str: Log information event 2 in the event log when trigger model execution reaches this block."""  # noqa: E501
    LOG_INFO3 = "trigger.LOG_INFO3"
    """str: Log information event 3 in the event log when trigger model execution reaches this block."""  # noqa: E501
    LOG_INFO4 = "trigger.LOG_INFO4"
    """str: Log information event 4 in the event log when trigger model execution reaches this block."""  # noqa: E501
    LOG_WARN1 = "trigger.LOG_WARN1"
    """str: Log warning event 1 in the event log when trigger model execution reaches this block."""
    LOG_WARN2 = "trigger.LOG_WARN2"
    """str: Log warning event 2 in the event log when trigger model execution reaches this block."""
    LOG_WARN3 = "trigger.LOG_WARN3"
    """str: Log warning event 3 in the event log when trigger model execution reaches this block."""
    LOG_WARN4 = "trigger.LOG_WARN4"
    """str: Log warning event 4 in the event log when trigger model execution reaches this block."""
    LOG_WARN_ABORT = "trigger.LOG_WARN_ABORT"
    """str: Abort the trigger model immediately and post a warning event log message."""
    OFF = "trigger.OFF"
    """str: Disable the trigger timer."""
    ON = "trigger.ON"
    """str: Enable the trigger timer."""
    SCAN_ALARM_LIMIT = "trigger.SCAN_ALARM_LIMIT"
    """str: Scan alarm limit exceeded."""
    STATE_ABORTED = "trigger.STATE_ABORTED"
    """str: The trigger model is stopped."""
    STATE_ABORTING = "trigger.STATE_ABORTING"
    """str: The trigger model is stopping."""
    STATE_BUILDING = "trigger.STATE_BUILDING"
    """str: Blocks have been added."""
    STATE_EMPTY = "trigger.STATE_EMPTY"
    """str: The trigger model is selected, but no blocks are defined."""
    STATE_FAILED = "trigger.STATE_FAILED"
    """str: The trigger model is stopped because of an error."""
    STATE_IDLE = "trigger.STATE_IDLE"
    """str: The trigger model is stopped."""
    STATE_RUNNING = "trigger.STATE_RUNNING"
    """str: The trigger model is running."""
    STATE_WAITING = "trigger.STATE_WAITING"
    """str: The trigger model has been in the same wait block for more than 100 ms."""
    WAIT_AND = "trigger.WAIT_AND"
    """str: Each event must occur before the trigger model continues."""
    WAIT_OR = "trigger.WAIT_OR"
    """str: At least one of the events must occur before the trigger model continues."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "trigger") -> None:
        super().__init__(device, cmd_syntax)
        self._blender: Dict[int, TriggerBlenderItem] = DefaultDictPassKeyToFactory(
            lambda x: TriggerBlenderItem(device, f"{self._cmd_syntax}.blender[{x}]")
        )
        self._digin: Dict[int, TriggerDiginItem] = DefaultDictPassKeyToFactory(
            lambda x: TriggerDiginItem(device, f"{self._cmd_syntax}.digin[{x}]")
        )
        self._digout: Dict[int, TriggerDigoutItem] = DefaultDictPassKeyToFactory(
            lambda x: TriggerDigoutItem(device, f"{self._cmd_syntax}.digout[{x}]")
        )
        self._ext = TriggerExt(device, f"{self._cmd_syntax}.ext")
        self._extin = TriggerExtin(device, f"{self._cmd_syntax}.extin")
        self._extout = TriggerExtout(device, f"{self._cmd_syntax}.extout")
        self._lanin: Dict[int, TriggerLaninItem] = DefaultDictPassKeyToFactory(
            lambda x: TriggerLaninItem(device, f"{self._cmd_syntax}.lanin[{x}]")
        )
        self._lanout: Dict[int, TriggerLanoutItem] = DefaultDictPassKeyToFactory(
            lambda x: TriggerLanoutItem(device, f"{self._cmd_syntax}.lanout[{x}]")
        )
        self._model = TriggerModel(device, f"{self._cmd_syntax}.model")
        self._timer: Dict[int, TriggerTimerItem] = DefaultDictPassKeyToFactory(
            lambda x: TriggerTimerItem(device, f"{self._cmd_syntax}.timer[{x}]")
        )
        self._tsplinkin: Dict[int, TriggerTsplinkinItem] = DefaultDictPassKeyToFactory(
            lambda x: TriggerTsplinkinItem(device, f"{self._cmd_syntax}.tsplinkin[{x}]")
        )
        self._tsplinkout: Dict[int, TriggerTsplinkoutItem] = DefaultDictPassKeyToFactory(
            lambda x: TriggerTsplinkoutItem(device, f"{self._cmd_syntax}.tsplinkout[{x}]")
        )

    @property
    def blender(self) -> Dict[int, TriggerBlenderItem]:
        """Return the ``trigger.blender[N]`` command tree.

        Info:
            - ``N``, the blender number (up to two).

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
    def continuous(self) -> str:
        """Access the ``trigger.continuous`` attribute.

        Description:
            - This attribute determines the trigger mode setting after bootup.

        Usage:
            - Accessing this property will send the ``print(trigger.continuous)`` query.
            - Setting this property to a value will send the ``trigger.continuous = value`` command.

        TSP Syntax:
            ```
            - trigger.continuous = value
            - print(trigger.continuous)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".continuous"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.continuous)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.continuous`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @continuous.setter
    def continuous(self, value: Union[str, float]) -> None:
        """Access the ``trigger.continuous`` attribute.

        Description:
            - This attribute determines the trigger mode setting after bootup.

        Usage:
            - Accessing this property will send the ``print(trigger.continuous)`` query.
            - Setting this property to a value will send the ``trigger.continuous = value`` command.

        TSP Syntax:
            ```
            - trigger.continuous = value
            - print(trigger.continuous)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".continuous", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.continuous = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.continuous`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def digin(self) -> Dict[int, TriggerDiginItem]:
        """Return the ``trigger.digin[N]`` command tree.

        Info:
            - ``N``, the digital I/O trigger line (1 to 6).

        Sub-properties and sub-methods:
            - ``.clear()``: The ``trigger.digin[N].clear()`` function.
            - ``.edge``: The ``trigger.digin[N].edge`` attribute.
            - ``.overrun``: The ``trigger.digin[N].overrun`` attribute.
            - ``.wait()``: The ``trigger.digin[N].wait()`` function.
        """
        return self._digin

    @property
    def digout(self) -> Dict[int, TriggerDigoutItem]:
        """Return the ``trigger.digout[N]`` command tree.

        Info:
            - ``N``, the digital I/O trigger line (1 to 6).

        Sub-properties and sub-methods:
            - ``.assert()``: The ``trigger.digout[N].assert()`` function.
            - ``.logic``: The ``trigger.digout[N].logic`` attribute.
            - ``.pulsewidth``: The ``trigger.digout[N].pulsewidth`` attribute.
            - ``.release()``: The ``trigger.digout[N].release()`` function.
            - ``.stimulus``: The ``trigger.digout[N].stimulus`` attribute.
        """
        return self._digout

    @property
    def ext(self) -> TriggerExt:
        """Return the ``trigger.ext`` command tree.

        Sub-properties and sub-methods:
            - ``.reset()``: The ``trigger.ext.reset()`` function.
        """
        return self._ext

    @property
    def extin(self) -> TriggerExtin:
        """Return the ``trigger.extin`` command tree.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``trigger.extin.clear()`` function.
            - ``.edge``: The ``trigger.extin.edge`` attribute.
            - ``.overrun``: The ``trigger.extin.overrun`` attribute.
            - ``.wait()``: The ``trigger.extin.wait()`` function.
        """
        return self._extin

    @property
    def extout(self) -> TriggerExtout:
        """Return the ``trigger.extout`` command tree.

        Sub-properties and sub-methods:
            - ``.assert()``: The ``trigger.extout.assert()`` function.
            - ``.logic``: The ``trigger.extout.logic`` attribute.
            - ``.stimulus``: The ``trigger.extout.stimulus`` attribute.
        """
        return self._extout

    @property
    def lanin(self) -> Dict[int, TriggerLaninItem]:
        """Return the ``trigger.lanin[N]`` command tree.

        Info:
            - ``N``, the LAN event number (1 to 8) to clear.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``trigger.lanin[N].clear()`` function.
            - ``.edge``: The ``trigger.lanin[N].edge`` attribute.
            - ``.overrun``: The ``trigger.lanin[N].overrun`` attribute.
            - ``.wait()``: The ``trigger.lanin[N].wait()`` function.
        """
        return self._lanin

    @property
    def lanout(self) -> Dict[int, TriggerLanoutItem]:
        """Return the ``trigger.lanout[N]`` command tree.

        Info:
            - ``N``, the LAN event number (1 to 8).

        Sub-properties and sub-methods:
            - ``.assert()``: The ``trigger.lanout[N].assert()`` function.
            - ``.connect()``: The ``trigger.lanout[N].connect()`` function.
            - ``.connected``: The ``trigger.lanout[N].connected`` attribute.
            - ``.disconnect()``: The ``trigger.lanout[N].disconnect()`` function.
            - ``.ipaddress``: The ``trigger.lanout[N].ipaddress`` attribute.
            - ``.logic``: The ``trigger.lanout[N].logic`` attribute.
            - ``.protocol``: The ``trigger.lanout[N].protocol`` attribute.
            - ``.stimulus``: The ``trigger.lanout[N].stimulus`` attribute.
        """
        return self._lanout

    @property
    def model(self) -> TriggerModel:
        """Return the ``trigger.model`` command tree.

        Sub-properties and sub-methods:
            - ``.abort()``: The ``trigger.model.abort()`` function.
            - ``.getblocklist()``: The ``trigger.model.getblocklist()`` function.
            - ``.getbranchcount()``: The ``trigger.model.getbranchcount()`` function.
            - ``.initiate()``: The ``trigger.model.initiate()`` function.
            - ``.load_config_list()``: The ``trigger.model.load() - ConfigList`` function.
            - ``.load_duration_loop()``: The ``trigger.model.load() - DurationLoop`` function.
            - ``.load_empty()``: The ``trigger.model.load() - Empty`` function.
            - ``.load_logic_trigger()``: The ``trigger.model.load() - LogicTrigger`` function.
            - ``.load_loop_until_event()``: The ``trigger.model.load() - LoopUntilEvent`` function.
            - ``.load_simple_loop()``: The ``trigger.model.load() - SimpleLoop`` function.
            - ``.pause()``: The ``trigger.model.pause()`` function.
            - ``.resume()``: The ``trigger.model.resume()`` function.
            - ``.setblock_trigger_block_branch_always()``: The
              ``trigger.model.setblock() - trigger.BLOCK_BRANCH_ALWAYS`` function.
            - ``.setblock_trigger_block_branch_counter()``: The
              ``trigger.model.setblock() - trigger.BLOCK_BRANCH_COUNTER`` function.
            - ``.setblock_trigger_block_branch_delta()``: The
              ``trigger.model.setblock() - trigger.BLOCK_BRANCH_DELTA`` function.
            - ``.setblock_trigger_block_branch_limit_constant()``: The
              ``trigger.model.setblock() - trigger.BLOCK_BRANCH_LIMIT_CONSTANT`` function.
            - ``.setblock_trigger_block_branch_limit_dynamic()``: The
              ``trigger.model.setblock() - trigger.BLOCK_BRANCH_LIMIT_DYNAMIC`` function.
            - ``.setblock_trigger_block_branch_once()``: The
              ``trigger.model.setblock() - trigger.BLOCK_BRANCH_ONCE`` function.
            - ``.setblock_trigger_block_branch_once_excluded()``: The
              ``trigger.model.setblock() - trigger.BLOCK_BRANCH_ONCE_EXCLUDED`` function.
            - ``.setblock_trigger_block_branch_on_event()``: The
              ``trigger.model.setblock() - trigger.BLOCK_BRANCH_ON_EVENT`` function.
            - ``.setblock_trigger_block_buffer_clear()``: The
              ``trigger.model.setblock() - trigger.BLOCK_BUFFER_CLEAR`` function.
            - ``.setblock_trigger_block_config_next()``: The
              ``trigger.model.setblock() - trigger.BLOCK_CONFIG_NEXT`` function.
            - ``.setblock_trigger_block_config_prev()``: The
              ``trigger.model.setblock() - trigger.BLOCK_CONFIG_PREV`` function.
            - ``.setblock_trigger_block_config_recall()``: The
              ``trigger.model.setblock() - trigger.BLOCK_CONFIG_RECALL`` function.
            - ``.setblock_trigger_block_delay_constant()``: The
              ``trigger.model.setblock() - trigger.BLOCK_DELAY_CONSTANT`` function.
            - ``.setblock_trigger_block_delay_dynamic()``: The
              ``trigger.model.setblock() - trigger.BLOCK_DELAY_DYNAMIC`` function.
            - ``.setblock_trigger_block_digital_io()``: The
              ``trigger.model.setblock() - trigger.BLOCK_DIGITAL_IO`` function.
            - ``.setblock_trigger_block_log_event()``: The
              ``trigger.model.setblock() - trigger.BLOCK_LOG_EVENT`` function.
            - ``.setblock_trigger_block_measure_digitize()``: The
              ``trigger.model.setblock() - trigger.BLOCK_MEASURE_DIGITIZE`` function.
            - ``.setblock_trigger_block_nop()``: The
              ``trigger.model.setblock() - trigger.BLOCK_NOP`` function.
            - ``.setblock_trigger_block_notify()``: The
              ``trigger.model.setblock() - trigger.BLOCK_NOTIFY`` function.
            - ``.setblock_trigger_block_reset_branch_count()``: The
              ``trigger.model.setblock() - trigger.BLOCK_RESET_BRANCH_COUNT`` function.
            - ``.setblock_trigger_block_wait()``: The
              ``trigger.model.setblock() - trigger.BLOCK_WAIT`` function.
            - ``.state()``: The ``trigger.model.state()`` function.
        """
        return self._model

    @property
    def timer(self) -> Dict[int, TriggerTimerItem]:
        """Return the ``trigger.timer[N]`` command tree.

        Info:
            - ``N``, the trigger timer number (1 to 4).

        Sub-properties and sub-methods:
            - ``.clear()``: The ``trigger.timer[N].clear()`` function.
            - ``.count``: The ``trigger.timer[N].count`` attribute.
            - ``.delay``: The ``trigger.timer[N].delay`` attribute.
            - ``.delaylist``: The ``trigger.timer[N].delaylist`` attribute.
            - ``.enable``: The ``trigger.timer[N].enable`` attribute.
            - ``.reset()``: The ``trigger.timer[N].reset()`` function.
            - ``.start``: The ``trigger.timer[N].start`` command tree.
            - ``.wait()``: The ``trigger.timer[N].wait()`` function.
        """
        return self._timer

    @property
    def tsplinkin(self) -> Dict[int, TriggerTsplinkinItem]:
        """Return the ``trigger.tsplinkin[N]`` command tree.

        Info:
            - ``N``, the trigger line (1 to 3) to clear.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``trigger.tsplinkin[N].clear()`` function.
            - ``.edge``: The ``trigger.tsplinkin[N].edge`` attribute.
            - ``.overrun``: The ``trigger.tsplinkin[N].overrun`` attribute.
            - ``.wait()``: The ``trigger.tsplinkin[N].wait()`` function.
        """
        return self._tsplinkin

    @property
    def tsplinkout(self) -> Dict[int, TriggerTsplinkoutItem]:
        """Return the ``trigger.tsplinkout[N]`` command tree.

        Info:
            - ``N``, the trigger line (1 to 3).

        Sub-properties and sub-methods:
            - ``.assert()``: The ``trigger.tsplinkout[N].assert()`` function.
            - ``.logic``: The ``trigger.tsplinkout[N].logic`` attribute.
            - ``.pulsewidth``: The ``trigger.tsplinkout[N].pulsewidth`` attribute.
            - ``.release()``: The ``trigger.tsplinkout[N].release()`` function.
            - ``.stimulus``: The ``trigger.tsplinkout[N].stimulus`` attribute.
        """
        return self._tsplinkout

    def clear(self) -> None:
        """Run the ``trigger.clear()`` function.

        Description:
            - This function clears any pending command triggers.

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
            - This function waits for a trigger event.

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
