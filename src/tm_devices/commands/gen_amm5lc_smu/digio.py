# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The digio commands module.

These commands are used in the following models:
SMU2601B, SMU2602B, SMU2611B, SMU2612B, SMU2635B, SMU2636B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - digio.readbit()
    - digio.readport()
    - digio.trigger[N].assert()
    - digio.trigger[N].clear()
    - digio.trigger[N].mode
    - digio.trigger[N].overrun
    - digio.trigger[N].pulsewidth
    - digio.trigger[N].release()
    - digio.trigger[N].reset()
    - digio.trigger[N].stimulus
    - digio.trigger[N].wait()
    - digio.writebit()
    - digio.writeport()
    - digio.writeprotect
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
    from tm_devices.driver_mixins.device_control.tsp_device import TSPDevice


class DigioTriggerItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``digio.trigger[N]`` command tree.

    Info:
        - ``N``, the digital I/O trigger line (1 to 14).

    Constants:
        - ``.EVENT_ID``: The trigger event generated by the digital I/O line N.

    Properties and methods:
        - ``.assert()``: The ``digio.trigger[N].assert()`` function.
        - ``.clear()``: The ``digio.trigger[N].clear()`` function.
        - ``.mode``: The ``digio.trigger[N].mode`` attribute.
        - ``.overrun``: The ``digio.trigger[N].overrun`` attribute.
        - ``.pulsewidth``: The ``digio.trigger[N].pulsewidth`` attribute.
        - ``.release()``: The ``digio.trigger[N].release()`` function.
        - ``.reset()``: The ``digio.trigger[N].reset()`` function.
        - ``.stimulus``: The ``digio.trigger[N].stimulus`` attribute.
        - ``.wait()``: The ``digio.trigger[N].wait()`` function.
    """

    EVENT_ID = "digio.trigger[N].EVENT_ID"
    """str: The trigger event generated by the digital I/O line N."""

    def __init__(self, device: Optional["TSPDevice"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        # pylint: disable=invalid-name
        self.EVENT_ID = self.EVENT_ID.replace(
            "[N]", f"[{self._cmd_syntax.rsplit('[', maxsplit=1)[-1].split(']', maxsplit=1)[0]}]"
        )

    @property
    def mode(self) -> str:
        """Access the ``digio.trigger[N].mode`` attribute.

        Description:
            - This attribute sets the mode in which the trigger event detector and the output
              trigger generator operate on the given trigger line. This command is not available on
              the 2604B, 2614B, or 2634B.

        Usage:
            - Accessing this property will send the ``print(digio.trigger[N].mode)`` query.
            - Setting this property to a value will send the ``digio.trigger[N].mode = value``
              command.

        TSP Syntax:
            ```
            - digio.trigger[N].mode = value
            - print(digio.trigger[N].mode)
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 14).

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
            msg = f"No TSPDevice object was provided, unable to access the ``{self._cmd_syntax}.mode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @mode.setter
    def mode(self, value: Union[str, float]) -> None:
        """Access the ``digio.trigger[N].mode`` attribute.

        Description:
            - This attribute sets the mode in which the trigger event detector and the output
              trigger generator operate on the given trigger line. This command is not available on
              the 2604B, 2614B, or 2634B.

        Usage:
            - Accessing this property will send the ``print(digio.trigger[N].mode)`` query.
            - Setting this property to a value will send the ``digio.trigger[N].mode = value``
              command.

        TSP Syntax:
            ```
            - digio.trigger[N].mode = value
            - print(digio.trigger[N].mode)
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 14).

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
            msg = f"No TSPDevice object was provided, unable to access the ``{self._cmd_syntax}.mode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def overrun(self) -> str:
        """Access the ``digio.trigger[N].overrun`` attribute.

        Description:
            - This attribute returns the event detector overrun status. This command is not
              available on the 2604B, 2614B, or 2634B.

        Usage:
            - Accessing this property will send the ``print(digio.trigger[N].overrun)`` query.

        TSP Syntax:
            ```
            - print(digio.trigger[N].overrun)
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 14).

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
            msg = f"No TSPDevice object was provided, unable to access the ``{self._cmd_syntax}.overrun`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def pulsewidth(self) -> str:
        """Access the ``digio.trigger[N].pulsewidth`` attribute.

        Description:
            - This attribute describes the length of time that the trigger line is asserted for
              output triggers. This command is not available on the 2604B, 2614B, or 2634B.

        Usage:
            - Accessing this property will send the ``print(digio.trigger[N].pulsewidth)`` query.
            - Setting this property to a value will send the ``digio.trigger[N].pulsewidth = value``
              command.

        TSP Syntax:
            ```
            - digio.trigger[N].pulsewidth = value
            - print(digio.trigger[N].pulsewidth)
            ```

        Info:
            - ``width``, the pulse width (seconds).
            - ``N``, the digital I/O trigger line (1 to 14).

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
            msg = f"No TSPDevice object was provided, unable to access the ``{self._cmd_syntax}.pulsewidth`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @pulsewidth.setter
    def pulsewidth(self, value: Union[str, float]) -> None:
        """Access the ``digio.trigger[N].pulsewidth`` attribute.

        Description:
            - This attribute describes the length of time that the trigger line is asserted for
              output triggers. This command is not available on the 2604B, 2614B, or 2634B.

        Usage:
            - Accessing this property will send the ``print(digio.trigger[N].pulsewidth)`` query.
            - Setting this property to a value will send the ``digio.trigger[N].pulsewidth = value``
              command.

        TSP Syntax:
            ```
            - digio.trigger[N].pulsewidth = value
            - print(digio.trigger[N].pulsewidth)
            ```

        Info:
            - ``width``, the pulse width (seconds).
            - ``N``, the digital I/O trigger line (1 to 14).

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
            msg = f"No TSPDevice object was provided, unable to access the ``{self._cmd_syntax}.pulsewidth`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def stimulus(self) -> str:
        """Access the ``digio.trigger[N].stimulus`` attribute.

        Description:
            - This attribute selects the event that causes a trigger to be asserted on the digital
              output line. This command is not available on the 2604B, 2614B, or 2634B.

        Usage:
            - Accessing this property will send the ``print(digio.trigger[N].stimulus)`` query.
            - Setting this property to a value will send the ``digio.trigger[N].stimulus = value``
              command.

        TSP Syntax:
            ```
            - digio.trigger[N].stimulus = value
            - print(digio.trigger[N].stimulus)
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 14).

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
            msg = f"No TSPDevice object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @stimulus.setter
    def stimulus(self, value: Union[str, float]) -> None:
        """Access the ``digio.trigger[N].stimulus`` attribute.

        Description:
            - This attribute selects the event that causes a trigger to be asserted on the digital
              output line. This command is not available on the 2604B, 2614B, or 2634B.

        Usage:
            - Accessing this property will send the ``print(digio.trigger[N].stimulus)`` query.
            - Setting this property to a value will send the ``digio.trigger[N].stimulus = value``
              command.

        TSP Syntax:
            ```
            - digio.trigger[N].stimulus = value
            - print(digio.trigger[N].stimulus)
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 14).

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
            msg = f"No TSPDevice object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def assert_(self) -> None:
        """Run the ``digio.trigger[N].assert()`` function.

        Description:
            - This function asserts a trigger pulse on one of the digital I/O lines. This command is
              not available on the 2604B, 2614B, or 2634B.

        TSP Syntax:
            ```
            - digio.trigger[N].assert()
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 14).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.assert()"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to run the ``{self._cmd_syntax}.assert()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def clear(self) -> None:
        """Run the ``digio.trigger[N].clear()`` function.

        Description:
            - This function clears the trigger event on a digital I/O line. This command is not
              available on the 2604B, 2614B, or 2634B.

        TSP Syntax:
            ```
            - digio.trigger[N].clear()
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 14).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.clear()"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to run the ``{self._cmd_syntax}.clear()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def release(self) -> None:
        """Run the ``digio.trigger[N].release()`` function.

        Description:
            - This function releases an indefinite length or latched trigger. This command is not
              available on the 2604B, 2614B, or 2634B.

        TSP Syntax:
            ```
            - digio.trigger[N].release()
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 14).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.release()"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to run the ``{self._cmd_syntax}.release()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def reset(self) -> None:
        """Run the ``digio.trigger[N].reset()`` function.

        Description:
            - This function resets trigger values to their factory defaults. This command is not
              available on the 2604B, 2614B, or 2634B.

        TSP Syntax:
            ```
            - digio.trigger[N].reset()
            ```

        Info:
            - ``N``, the digital I/O trigger line (1 to 14).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.reset()"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to run the ``{self._cmd_syntax}.reset()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def wait(self, timeout: float) -> str:
        """Run the ``digio.trigger[N].wait()`` function.

        Description:
            - This function waits for a trigger. This command is not available on the 2604B, 2614B,
              or 2634B.

        TSP Syntax:
            ```
            - digio.trigger[N].wait()
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
            msg = f"No TSPDevice object was provided, unable to run the ``{self._cmd_syntax}.wait()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class Digio(BaseTSPCmd):
    """The ``digio`` command tree.

    Constants:
        - ``.TRIG_BYPASS``: Sets the mode in which the trigger event detector and the output trigger
          generator operate on the specified trigger line to allow direct control of the line.
        - ``.TRIG_EITHER``: Sets the mode in which the trigger event detector and the output trigger
          generator operate on the specified trigger line to detect rising- or falling-edge triggers
          as input and assert a TTL-low pulse for output.
        - ``.TRIG_FALLING``: Sets the mode in which the trigger event detector and the output
          trigger generator operate on the specified trigger line to detect falling-edge triggers as
          input and assert a TTL-low pulse for output.
        - ``.TRIG_RISING``: Sets the mode in which the trigger event detector and the output trigger
          generator operate on the specified trigger line so that if the programmed state of the
          line is high, the digio.TRIG_RISING mode behavior is similar to digio.TRIG_RISINGA. If the
          programmed state of the line is low, the digio.TRIG_RISING mode behavior is similar to
          digio.TRIG_RISINGM. Only use this setting if necessary for compatibility with other
          Keithley Instruments products.
        - ``.TRIG_RISINGA``: Sets the mode in which the trigger event detector and the output
          trigger generator operate on the specified trigger line to detect rising-edge triggers as
          input and assert a TTL-low pulse for output.
        - ``.TRIG_RISINGM``: Sets the mode in which the trigger event detector and the output
          trigger generator operate on the specified trigger line to assert a TTL-high pulse for
          output. Input edge detection is not possible in this mode.
        - ``.TRIG_SYNCHRONOUS``: Sets the mode in which the trigger event detector and the output
          trigger generator operate on the specified trigger line to detect the falling-edge input
          triggers and automatically latch and drive the trigger line low. Asserts a TTL-low pulse
          as an output trigger.
        - ``.TRIG_SYNCHRONOUSA``: Sets the mode in which the trigger event detector and the output
          trigger generator operate on the specified trigger line to detect the falling-edge input
          triggers and automatically latch and drive the trigger line low. Asserting the output
          trigger releases the latched line.
        - ``.TRIG_SYNCHRONOUSM``: Sets the mode in which the trigger event detector and the output
          trigger generator operate on the specified trigger line to detect rising-edge triggers as
          input and assert a TTL-low pulse for output.

    Properties and methods:
        - ``.readbit()``: The ``digio.readbit()`` function.
        - ``.readport()``: The ``digio.readport()`` function.
        - ``.trigger``: The ``digio.trigger[N]`` command tree.
        - ``.writebit()``: The ``digio.writebit()`` function.
        - ``.writeport()``: The ``digio.writeport()`` function.
        - ``.writeprotect``: The ``digio.writeprotect`` attribute.
    """

    TRIG_BYPASS = "digio.TRIG_BYPASS"
    """str: Sets the mode in which the trigger event detector and the output trigger generator operate on the specified trigger line to allow direct control of the line."""  # noqa: E501
    TRIG_EITHER = "digio.TRIG_EITHER"
    """str: Sets the mode in which the trigger event detector and the output trigger generator operate on the specified trigger line to detect rising- or falling-edge triggers as input and assert a TTL-low pulse for output."""  # noqa: E501
    TRIG_FALLING = "digio.TRIG_FALLING"
    """str: Sets the mode in which the trigger event detector and the output trigger generator operate on the specified trigger line to detect falling-edge triggers as input and assert a TTL-low pulse for output."""  # noqa: E501
    TRIG_RISING = "digio.TRIG_RISING"
    """str: Sets the mode in which the trigger event detector and the output trigger generator operate on the specified trigger line so that if the programmed state of the line is high, the digio.TRIG_RISING mode behavior is similar to digio.TRIG_RISINGA. If the programmed state of the line is low, the digio.TRIG_RISING mode behavior is similar to digio.TRIG_RISINGM. Only use this setting if necessary for compatibility with other Keithley Instruments products."""  # noqa: E501
    TRIG_RISINGA = "digio.TRIG_RISINGA"
    """str: Sets the mode in which the trigger event detector and the output trigger generator operate on the specified trigger line to detect rising-edge triggers as input and assert a TTL-low pulse for output."""  # noqa: E501
    TRIG_RISINGM = "digio.TRIG_RISINGM"
    """str: Sets the mode in which the trigger event detector and the output trigger generator operate on the specified trigger line to assert a TTL-high pulse for output. Input edge detection is not possible in this mode."""  # noqa: E501
    TRIG_SYNCHRONOUS = "digio.TRIG_SYNCHRONOUS"
    """str: Sets the mode in which the trigger event detector and the output trigger generator operate on the specified trigger line to detect the falling-edge input triggers and automatically latch and drive the trigger line low. Asserts a TTL-low pulse as an output trigger."""  # noqa: E501
    TRIG_SYNCHRONOUSA = "digio.TRIG_SYNCHRONOUSA"
    """str: Sets the mode in which the trigger event detector and the output trigger generator operate on the specified trigger line to detect the falling-edge input triggers and automatically latch and drive the trigger line low. Asserting the output trigger releases the latched line."""  # noqa: E501
    TRIG_SYNCHRONOUSM = "digio.TRIG_SYNCHRONOUSM"
    """str: Sets the mode in which the trigger event detector and the output trigger generator operate on the specified trigger line to detect rising-edge triggers as input and assert a TTL-low pulse for output."""  # noqa: E501

    def __init__(self, device: Optional["TSPDevice"] = None, cmd_syntax: str = "digio") -> None:
        super().__init__(device, cmd_syntax)
        self._trigger: Dict[int, DigioTriggerItem] = DefaultDictPassKeyToFactory(
            lambda x: DigioTriggerItem(device, f"{self._cmd_syntax}.trigger[{x}]")
        )

    @property
    def trigger(self) -> Dict[int, DigioTriggerItem]:
        """Return the ``digio.trigger[N]`` command tree.

        Info:
            - ``N``, the digital I/O trigger line (1 to 14).

        Constants:
            - ``.EVENT_ID``: The trigger event generated by the digital I/O line N.

        Sub-properties and sub-methods:
            - ``.assert()``: The ``digio.trigger[N].assert()`` function.
            - ``.clear()``: The ``digio.trigger[N].clear()`` function.
            - ``.mode``: The ``digio.trigger[N].mode`` attribute.
            - ``.overrun``: The ``digio.trigger[N].overrun`` attribute.
            - ``.pulsewidth``: The ``digio.trigger[N].pulsewidth`` attribute.
            - ``.release()``: The ``digio.trigger[N].release()`` function.
            - ``.reset()``: The ``digio.trigger[N].reset()`` function.
            - ``.stimulus``: The ``digio.trigger[N].stimulus`` attribute.
            - ``.wait()``: The ``digio.trigger[N].wait()`` function.
        """
        return self._trigger

    @property
    def writeprotect(self) -> str:
        """Access the ``digio.writeprotect`` attribute.

        Description:
            - This attribute contains the write-protect mask that protects bits from changes from
              the digio.writebit() and digio.writeport() functions. This command is not available on
              the 2604B, 2614B, or 2634B.

        Usage:
            - Accessing this property will send the ``print(digio.writeprotect)`` query.
            - Setting this property to a value will send the ``digio.writeprotect = value`` command.

        TSP Syntax:
            ```
            - digio.writeprotect = value
            - print(digio.writeprotect)
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
            msg = f"No TSPDevice object was provided, unable to access the ``{self._cmd_syntax}.writeprotect`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @writeprotect.setter
    def writeprotect(self, value: Union[str, float]) -> None:
        """Access the ``digio.writeprotect`` attribute.

        Description:
            - This attribute contains the write-protect mask that protects bits from changes from
              the digio.writebit() and digio.writeport() functions. This command is not available on
              the 2604B, 2614B, or 2634B.

        Usage:
            - Accessing this property will send the ``print(digio.writeprotect)`` query.
            - Setting this property to a value will send the ``digio.writeprotect = value`` command.

        TSP Syntax:
            ```
            - digio.writeprotect = value
            - print(digio.writeprotect)
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
            msg = f"No TSPDevice object was provided, unable to access the ``{self._cmd_syntax}.writeprotect`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def readbit(self, n: int) -> str:
        """Run the ``digio.readbit()`` function.

        Description:
            - This function reads one digital I/O line. This command is not available on the 2604B,
              2614B, or 2634B.

        TSP Syntax:
            ```
            - digio.readbit()
            ```

        Args:
            n: Digital I/O line number to be read (1 to 14).

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
            msg = f"No TSPDevice object was provided, unable to run the ``{self._cmd_syntax}.readbit()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def readport(self) -> str:
        """Run the ``digio.readport()`` function.

        Description:
            - This function reads the digital I/O port. This command is not available on the 2604B,
              2614B, or 2634B.

        TSP Syntax:
            ```
            - digio.readport()
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
            msg = f"No TSPDevice object was provided, unable to run the ``{self._cmd_syntax}.readport()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def writebit(self, n: int, data: int) -> None:
        """Run the ``digio.writebit()`` function.

        Description:
            - This function sets a digital I/O line high or low. This command is not available on
              the 2604B, 2614B, or 2634B.

        TSP Syntax:
            ```
            - digio.writebit()
            ```

        Args:
            n: Digital I/O trigger line (1 to 14).
            data: The value to write to the bit.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.writebit({n}, {data})"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to run the ``{self._cmd_syntax}.writebit()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def writeport(self, data: int) -> None:
        """Run the ``digio.writeport()`` function.

        Description:
            - This function writes to all digital I/O lines. This command is not available on the
              2604B, 2614B, or 2634B.

        TSP Syntax:
            ```
            - digio.writeport()
            ```

        Args:
            data: Value to write to the port (0 to 16383).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.writeport({data})"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to run the ``{self._cmd_syntax}.writeport()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
