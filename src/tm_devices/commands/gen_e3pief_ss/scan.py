# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The scan commands module.

These commands are used in the following models:
SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - scan.abort()
    - scan.add()
    - scan.addimagestep()
    - scan.addwrite()
    - scan.background()
    - scan.bypass
    - scan.create()
    - scan.execute()
    - scan.list()
    - scan.measurecount
    - scan.mode
    - scan.nobufferbackground()
    - scan.nobufferexecute()
    - scan.reset()
    - scan.scancount
    - scan.state()
    - scan.stepcount
    - scan.trigger.arm.clear()
    - scan.trigger.arm.set()
    - scan.trigger.arm.stimulus
    - scan.trigger.channel.clear()
    - scan.trigger.channel.set()
    - scan.trigger.channel.stimulus
    - scan.trigger.clear()
    - scan.trigger.measure.clear()
    - scan.trigger.measure.set()
    - scan.trigger.measure.stimulus
    - scan.trigger.sequence.clear()
    - scan.trigger.sequence.set()
    - scan.trigger.sequence.stimulus
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class ScanTriggerSequence(BaseTSPCmd):
    """The ``scan.trigger.sequence`` command tree.

    Properties and methods:
        - ``.clear()``: The ``scan.trigger.sequence.clear()`` function.
        - ``.set()``: The ``scan.trigger.sequence.set()`` function.
        - ``.stimulus``: The ``scan.trigger.sequence.stimulus`` attribute.
    """

    @property
    def stimulus(self) -> str:
        """Access the ``scan.trigger.sequence.stimulus`` attribute.

        Description:
            - This attribute selects the trigger stimulus for the sequence event detector.

        Usage:
            - Accessing this property will send the ``print(scan.trigger.sequence.stimulus)`` query.
            - Setting this property to a value will send the
              ``scan.trigger.sequence.stimulus = value`` command.

        TSP Syntax:
            ```
            - scan.trigger.sequence.stimulus = value
            - print(scan.trigger.sequence.stimulus)
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
        """Access the ``scan.trigger.sequence.stimulus`` attribute.

        Description:
            - This attribute selects the trigger stimulus for the sequence event detector.

        Usage:
            - Accessing this property will send the ``print(scan.trigger.sequence.stimulus)`` query.
            - Setting this property to a value will send the
              ``scan.trigger.sequence.stimulus = value`` command.

        TSP Syntax:
            ```
            - scan.trigger.sequence.stimulus = value
            - print(scan.trigger.sequence.stimulus)
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

    def clear(self) -> None:
        """Run the ``scan.trigger.sequence.clear()`` function.

        Description:
            - This function clears the sequence event detector.

        TSP Syntax:
            ```
            - scan.trigger.sequence.clear()
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

    def set_(self) -> None:
        """Run the ``scan.trigger.sequence.set()`` function.

        Description:
            - This function sets the sequence even detector to the detected state.

        TSP Syntax:
            ```
            - scan.trigger.sequence.set()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.set()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.set()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class ScanTriggerMeasure(BaseTSPCmd):
    """The ``scan.trigger.measure`` command tree.

    Properties and methods:
        - ``.clear()``: The ``scan.trigger.measure.clear()`` function.
        - ``.set()``: The ``scan.trigger.measure.set()`` function.
        - ``.stimulus``: The ``scan.trigger.measure.stimulus`` attribute.
    """

    @property
    def stimulus(self) -> str:
        """Access the ``scan.trigger.measure.stimulus`` attribute.

        Description:
            - This attribute selects the trigger stimulus of the event detector trigger.

        Usage:
            - Accessing this property will send the ``print(scan.trigger.measure.stimulus)`` query.
            - Setting this property to a value will send the
              ``scan.trigger.measure.stimulus = value`` command.

        TSP Syntax:
            ```
            - scan.trigger.measure.stimulus = value
            - print(scan.trigger.measure.stimulus)
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
        """Access the ``scan.trigger.measure.stimulus`` attribute.

        Description:
            - This attribute selects the trigger stimulus of the event detector trigger.

        Usage:
            - Accessing this property will send the ``print(scan.trigger.measure.stimulus)`` query.
            - Setting this property to a value will send the
              ``scan.trigger.measure.stimulus = value`` command.

        TSP Syntax:
            ```
            - scan.trigger.measure.stimulus = value
            - print(scan.trigger.measure.stimulus)
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

    def clear(self) -> None:
        """Run the ``scan.trigger.measure.clear()`` function.

        Description:
            - This function clears the measure event detector.

        TSP Syntax:
            ```
            - scan.trigger.measure.clear()
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

    def set_(self) -> None:
        """Run the ``scan.trigger.measure.set()`` function.

        Description:
            - This function sets the measurement event detector to the detected state.

        TSP Syntax:
            ```
            - scan.trigger.measure.set()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.set()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.set()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class ScanTriggerChannel(BaseTSPCmd):
    """The ``scan.trigger.channel`` command tree.

    Properties and methods:
        - ``.clear()``: The ``scan.trigger.channel.clear()`` function.
        - ``.set()``: The ``scan.trigger.channel.set()`` function.
        - ``.stimulus``: The ``scan.trigger.channel.stimulus`` attribute.
    """

    @property
    def stimulus(self) -> str:
        """Access the ``scan.trigger.channel.stimulus`` attribute.

        Description:
            - This attribute determines which trigger events cause the channel actions to occur.

        Usage:
            - Accessing this property will send the ``print(scan.trigger.channel.stimulus)`` query.
            - Setting this property to a value will send the
              ``scan.trigger.channel.stimulus = value`` command.

        TSP Syntax:
            ```
            - scan.trigger.channel.stimulus = value
            - print(scan.trigger.channel.stimulus)
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
        """Access the ``scan.trigger.channel.stimulus`` attribute.

        Description:
            - This attribute determines which trigger events cause the channel actions to occur.

        Usage:
            - Accessing this property will send the ``print(scan.trigger.channel.stimulus)`` query.
            - Setting this property to a value will send the
              ``scan.trigger.channel.stimulus = value`` command.

        TSP Syntax:
            ```
            - scan.trigger.channel.stimulus = value
            - print(scan.trigger.channel.stimulus)
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

    def clear(self) -> None:
        """Run the ``scan.trigger.channel.clear()`` function.

        Description:
            - This function clears the channel event detector.

        TSP Syntax:
            ```
            - scan.trigger.channel.clear()
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

    def set_(self) -> None:
        """Run the ``scan.trigger.channel.set()`` function.

        Description:
            - This function sets the channel event detector to the detected state.

        TSP Syntax:
            ```
            - scan.trigger.channel.set()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.set()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.set()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class ScanTriggerArm(BaseTSPCmd):
    """The ``scan.trigger.arm`` command tree.

    Properties and methods:
        - ``.clear()``: The ``scan.trigger.arm.clear()`` function.
        - ``.set()``: The ``scan.trigger.arm.set()`` function.
        - ``.stimulus``: The ``scan.trigger.arm.stimulus`` attribute.
    """

    @property
    def stimulus(self) -> str:
        """Access the ``scan.trigger.arm.stimulus`` attribute.

        Description:
            - This attribute determines which event starts the scan.

        Usage:
            - Accessing this property will send the ``print(scan.trigger.arm.stimulus)`` query.
            - Setting this property to a value will send the ``scan.trigger.arm.stimulus = value``
              command.

        TSP Syntax:
            ```
            - scan.trigger.arm.stimulus = value
            - print(scan.trigger.arm.stimulus)
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
        """Access the ``scan.trigger.arm.stimulus`` attribute.

        Description:
            - This attribute determines which event starts the scan.

        Usage:
            - Accessing this property will send the ``print(scan.trigger.arm.stimulus)`` query.
            - Setting this property to a value will send the ``scan.trigger.arm.stimulus = value``
              command.

        TSP Syntax:
            ```
            - scan.trigger.arm.stimulus = value
            - print(scan.trigger.arm.stimulus)
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

    def clear(self) -> None:
        """Run the ``scan.trigger.arm.clear()`` function.

        Description:
            - This function clears the arm event detector.

        TSP Syntax:
            ```
            - scan.trigger.arm.clear()
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

    def set_(self) -> None:
        """Run the ``scan.trigger.arm.set()`` function.

        Description:
            - This function sets the arm event detector to the detected state.

        TSP Syntax:
            ```
            - scan.trigger.arm.set()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.set()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.set()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class ScanTrigger(BaseTSPCmd):
    """The ``scan.trigger`` command tree.

    Properties and methods:
        - ``.arm``: The ``scan.trigger.arm`` command tree.
        - ``.channel``: The ``scan.trigger.channel`` command tree.
        - ``.clear()``: The ``scan.trigger.clear()`` function.
        - ``.measure``: The ``scan.trigger.measure`` command tree.
        - ``.sequence``: The ``scan.trigger.sequence`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._arm = ScanTriggerArm(device, f"{self._cmd_syntax}.arm")
        self._channel = ScanTriggerChannel(device, f"{self._cmd_syntax}.channel")
        self._measure = ScanTriggerMeasure(device, f"{self._cmd_syntax}.measure")
        self._sequence = ScanTriggerSequence(device, f"{self._cmd_syntax}.sequence")

    @property
    def arm(self) -> ScanTriggerArm:
        """Return the ``scan.trigger.arm`` command tree.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``scan.trigger.arm.clear()`` function.
            - ``.set()``: The ``scan.trigger.arm.set()`` function.
            - ``.stimulus``: The ``scan.trigger.arm.stimulus`` attribute.
        """
        return self._arm

    @property
    def channel(self) -> ScanTriggerChannel:
        """Return the ``scan.trigger.channel`` command tree.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``scan.trigger.channel.clear()`` function.
            - ``.set()``: The ``scan.trigger.channel.set()`` function.
            - ``.stimulus``: The ``scan.trigger.channel.stimulus`` attribute.
        """
        return self._channel

    @property
    def measure(self) -> ScanTriggerMeasure:
        """Return the ``scan.trigger.measure`` command tree.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``scan.trigger.measure.clear()`` function.
            - ``.set()``: The ``scan.trigger.measure.set()`` function.
            - ``.stimulus``: The ``scan.trigger.measure.stimulus`` attribute.
        """
        return self._measure

    @property
    def sequence(self) -> ScanTriggerSequence:
        """Return the ``scan.trigger.sequence`` command tree.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``scan.trigger.sequence.clear()`` function.
            - ``.set()``: The ``scan.trigger.sequence.set()`` function.
            - ``.stimulus``: The ``scan.trigger.sequence.stimulus`` attribute.
        """
        return self._sequence

    def clear(self) -> None:
        """Run the ``scan.trigger.clear()`` function.

        Description:
            - This function clears the trigger model.

        TSP Syntax:
            ```
            - scan.trigger.clear()
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


class Scan(BaseTSPCmd):
    """The ``scan`` command tree.

    Properties and methods:
        - ``.abort()``: The ``scan.abort()`` function.
        - ``.add()``: The ``scan.add()`` function.
        - ``.addimagestep()``: The ``scan.addimagestep()`` function.
        - ``.addwrite()``: The ``scan.addwrite()`` function.
        - ``.background()``: The ``scan.background()`` function.
        - ``.bypass``: The ``scan.bypass`` attribute.
        - ``.create()``: The ``scan.create()`` function.
        - ``.execute()``: The ``scan.execute()`` function.
        - ``.list()``: The ``scan.list()`` function.
        - ``.measurecount``: The ``scan.measurecount`` attribute.
        - ``.mode``: The ``scan.mode`` attribute.
        - ``.nobufferbackground()``: The ``scan.nobufferbackground()`` function.
        - ``.nobufferexecute()``: The ``scan.nobufferexecute()`` function.
        - ``.reset()``: The ``scan.reset()`` function.
        - ``.scancount``: The ``scan.scancount`` attribute.
        - ``.state()``: The ``scan.state()`` function.
        - ``.stepcount``: The ``scan.stepcount`` attribute.
        - ``.trigger``: The ``scan.trigger`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "scan") -> None:
        super().__init__(device, cmd_syntax)
        self._trigger = ScanTrigger(device, f"{self._cmd_syntax}.trigger")

    @property
    def bypass(self) -> str:
        """Access the ``scan.bypass`` attribute.

        Description:
            - This attribute indicates whether the first channel of the scan waits for the channel
              stimulus event to be satisfied before closing.

        Usage:
            - Accessing this property will send the ``print(scan.bypass)`` query.
            - Setting this property to a value will send the ``scan.bypass = value`` command.

        TSP Syntax:
            ```
            - scan.bypass = value
            - print(scan.bypass)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".bypass"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.bypass)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.bypass`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @bypass.setter
    def bypass(self, value: Union[str, float]) -> None:
        """Access the ``scan.bypass`` attribute.

        Description:
            - This attribute indicates whether the first channel of the scan waits for the channel
              stimulus event to be satisfied before closing.

        Usage:
            - Accessing this property will send the ``print(scan.bypass)`` query.
            - Setting this property to a value will send the ``scan.bypass = value`` command.

        TSP Syntax:
            ```
            - scan.bypass = value
            - print(scan.bypass)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".bypass", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.bypass = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.bypass`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def measurecount(self) -> str:
        """Access the ``scan.measurecount`` attribute.

        Description:
            - This attribute sets the number of iterations performed when a scanning measurement is
              requested.

        Usage:
            - Accessing this property will send the ``print(scan.measurecount)`` query.
            - Setting this property to a value will send the ``scan.measurecount = value`` command.

        TSP Syntax:
            ```
            - scan.measurecount = value
            - print(scan.measurecount)
            ```

        Info:
            - ``count``, the count value being used or read; valid range is 1 to 450000.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".measurecount"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.measurecount)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.measurecount`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @measurecount.setter
    def measurecount(self, value: Union[str, float]) -> None:
        """Access the ``scan.measurecount`` attribute.

        Description:
            - This attribute sets the number of iterations performed when a scanning measurement is
              requested.

        Usage:
            - Accessing this property will send the ``print(scan.measurecount)`` query.
            - Setting this property to a value will send the ``scan.measurecount = value`` command.

        TSP Syntax:
            ```
            - scan.measurecount = value
            - print(scan.measurecount)
            ```

        Info:
            - ``count``, the count value being used or read; valid range is 1 to 450000.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".measurecount", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.measurecount = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.measurecount`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def mode(self) -> str:
        """Access the ``scan.mode`` attribute.

        Description:
            - This attribute sets the relay action when the scan starts.

        Usage:
            - Accessing this property will send the ``print(scan.mode)`` query.
            - Setting this property to a value will send the ``scan.mode = value`` command.

        TSP Syntax:
            ```
            - scan.mode = value
            - print(scan.mode)
            ```

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
        """Access the ``scan.mode`` attribute.

        Description:
            - This attribute sets the relay action when the scan starts.

        Usage:
            - Accessing this property will send the ``print(scan.mode)`` query.
            - Setting this property to a value will send the ``scan.mode = value`` command.

        TSP Syntax:
            ```
            - scan.mode = value
            - print(scan.mode)
            ```

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
    def scancount(self) -> str:
        """Access the ``scan.scancount`` attribute.

        Description:
            - This attribute sets the number of times the scan is repeated.

        Usage:
            - Accessing this property will send the ``print(scan.scancount)`` query.
            - Setting this property to a value will send the ``scan.scancount = value`` command.

        TSP Syntax:
            ```
            - scan.scancount = value
            - print(scan.scancount)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".scancount"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.scancount)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.scancount`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @scancount.setter
    def scancount(self, value: Union[str, float]) -> None:
        """Access the ``scan.scancount`` attribute.

        Description:
            - This attribute sets the number of times the scan is repeated.

        Usage:
            - Accessing this property will send the ``print(scan.scancount)`` query.
            - Setting this property to a value will send the ``scan.scancount = value`` command.

        TSP Syntax:
            ```
            - scan.scancount = value
            - print(scan.scancount)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".scancount", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.scancount = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.scancount`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def stepcount(self) -> str:
        """Access the ``scan.stepcount`` attribute.

        Description:
            - This attribute returns the number of steps in the present scan.

        Usage:
            - Accessing this property will send the ``print(scan.stepcount)`` query.

        TSP Syntax:
            ```
            - print(scan.stepcount)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".stepcount"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.stepcount)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stepcount`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def trigger(self) -> ScanTrigger:
        """Return the ``scan.trigger`` command tree.

        Sub-properties and sub-methods:
            - ``.arm``: The ``scan.trigger.arm`` command tree.
            - ``.channel``: The ``scan.trigger.channel`` command tree.
            - ``.clear()``: The ``scan.trigger.clear()`` function.
            - ``.measure``: The ``scan.trigger.measure`` command tree.
            - ``.sequence``: The ``scan.trigger.sequence`` command tree.
        """
        return self._trigger

    def abort(self) -> None:
        """Run the ``scan.abort()`` function.

        Description:
            - This function aborts a running background scan.

        TSP Syntax:
            ```
            - scan.abort()
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

    def add(self, channel_list: str, width: Optional[str] = None) -> None:
        """Run the ``scan.add()`` function.

        Description:
            - This function adds channels to the scan list.

        TSP Syntax:
            ```
            - scan.add()
            ```

        Args:
            channel_list: String specifying channels to add using normal channel list syntax.
            width (optional): Value that specifies the width of the channel read to use with items
                in channelList.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{channel_list}"',
                    width,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.add({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.add()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def addimagestep(self, channel_list: str, dmm_config: Optional[str] = None) -> None:
        """Run the ``scan.addimagestep()`` function.

        Description:
            - This function allows you to include multiple channels in a single scan step.

        TSP Syntax:
            ```
            - scan.addimagestep()
            ```

        Args:
            channel_list: String specifying a list of channels.
            dmm_config (optional): String specifying a DMM configuration.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{channel_list}"',
                    f'"{dmm_config}"' if dmm_config is not None else None,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.addimagestep({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.addimagestep()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def addwrite(self, channel_list: str, write_value: str, width: Optional[str] = None) -> None:
        """Run the ``scan.addwrite()`` function.

        Description:
            - This function writes a specified value to a channel at the added step in the scan.

        TSP Syntax:
            ```
            - scan.addwrite()
            ```

        Args:
            channel_list: String specifying channels to add using normal channel list syntax.
            write_value: The value to write to the channel for this scan step.
            width (optional): Specifies the width of the channel write to use with items in
                channelList.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{channel_list}"',
                    write_value,
                    width,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.addwrite({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.addwrite()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def background(self, buffer_var: Optional[str] = None) -> str:
        """Run the ``scan.background()`` function.

        Description:
            - This function starts a scan and runs the scan in the background.

        TSP Syntax:
            ```
            - scan.background()
            ```

        Args:
            buffer_var (optional): The reading buffer used during scanning to store the readings; if
                a buffer is not specified, no readings are stored during the scan.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (buffer_var,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.background({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.background()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def create(self, channel_list: str, dmm_config: Optional[str] = None) -> None:
        """Run the ``scan.create()`` function.

        Description:
            - This function deletes the existing scan list and creates a new list of channels and
              channel patterns to scan.

        TSP Syntax:
            ```
            - scan.create()
            ```

        Args:
            channel_list: String specifying channels to add.
            dmm_config (optional): The DMM configuration to use with items in the channelList.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    channel_list,
                    dmm_config,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.create({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.create()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def execute(self, buffer_var: Optional[str] = None) -> str:
        """Run the ``scan.execute()`` function.

        Description:
            - This function starts the scan immediately in the foreground with a configured scan
              list.

        TSP Syntax:
            ```
            - scan.execute()
            ```

        Args:
            buffer_var (optional): A reading buffer used during scanning to store the readings; if a
                buffer is not specified, no readings are stored during the scan.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (buffer_var,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.execute({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.execute()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def list(self) -> str:
        """Run the ``scan.list()`` function.

        Description:
            - This function queries the active scan list.

        TSP Syntax:
            ```
            - scan.list()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.list())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.list()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def nobufferbackground(self) -> str:
        """Run the ``scan.nobufferbackground()`` function.

        Description:
            - This function starts a scan in background mode and specifies that no reading buffer is
              used during scanning.

        TSP Syntax:
            ```
            - scan.nobufferbackground()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.nobufferbackground())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.nobufferbackground()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def nobufferexecute(self) -> None:
        """Run the ``scan.nobufferexecute()`` function.

        Description:
            - This function starts a scan immediately and specifies that no reading buffer is used
              during scanning.

        TSP Syntax:
            ```
            - scan.nobufferexecute()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.nobufferexecute()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.nobufferexecute()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def reset(self) -> None:
        """Run the ``scan.reset()`` function.

        Description:
            - This function resets the trigger model and scan list settings to their factory default
              settings.

        TSP Syntax:
            ```
            - scan.reset()
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

    def state(self) -> str:
        """Run the ``scan.state()`` function.

        Description:
            - This function provides the present state of a running background scan.

        TSP Syntax:
            ```
            - scan.state()
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
