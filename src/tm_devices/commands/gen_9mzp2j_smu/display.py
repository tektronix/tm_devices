# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The display commands module.

These commands are used in the following models:
SMU2604B, SMU2614B, SMU2634B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - display.clear()
    - display.getannunciators()
    - display.getcursor()
    - display.getlastkey()
    - display.gettext()
    - display.inputvalue()
    - display.loadmenu.add()
    - display.loadmenu.delete()
    - display.locallockout
    - display.menu()
    - display.numpad
    - display.prompt()
    - display.screen
    - display.sendkey()
    - display.setcursor()
    - display.settext()
    - display.smuX.digits
    - display.smuX.limit.func
    - display.smuX.measure.func
    - display.trigger.clear()
    - display.trigger.overrun
    - display.trigger.wait()
    - display.waitkey()
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING, Union

from ..helpers import (
    BaseTSPCmd,
    DefaultDictPassKeyToFactory,
    NoDeviceProvidedError,
    ValidatedChannel,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class DisplayTrigger(BaseTSPCmd):
    """The ``display.trigger`` command tree.

    Constants:
        - ``.EVENT_ID``: The event ID of the event generated when the front-panel TRIG key is
          pressed.

    Properties and methods:
        - ``.clear()``: The ``display.trigger.clear()`` function.
        - ``.overrun``: The ``display.trigger.overrun`` attribute.
        - ``.wait()``: The ``display.trigger.wait()`` function.
    """

    EVENT_ID = "display.trigger.EVENT_ID"
    """str: The event ID of the event generated when the front-panel TRIG key is pressed."""

    @property
    def overrun(self) -> str:
        """Access the ``display.trigger.overrun`` attribute.

        Description:
            - This attribute contains the event detector overrun status.

        Usage:
            - Accessing this property will send the ``print(display.trigger.overrun)`` query.

        TSP Syntax:
            ```
            - print(display.trigger.overrun)
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
        """Run the ``display.trigger.clear()`` function.

        Description:
            - This function clears the front-panel trigger event detector.

        TSP Syntax:
            ```
            - display.trigger.clear()
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
        """Run the ``display.trigger.wait()`` function.

        Description:
            - This function waits for the TRIG key on the front panel to be pressed.

        TSP Syntax:
            ```
            - display.trigger.wait()
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


class DisplaySmuxItemMeasure(BaseTSPCmd):
    """The ``display.smuX.measure`` command tree.

    Info:
        - ``X``, the source-measure unit (SMU) channel (for example, display.smua.measure.func
          applies to SMU channel A).

    Properties and methods:
        - ``.func``: The ``display.smuX.measure.func`` attribute.
    """

    @property
    def func(self) -> str:
        """Access the ``display.smuX.measure.func`` attribute.

        Description:
            - This attribute specifies the type of measurement that is being displayed.

        Usage:
            - Accessing this property will send the ``print(display.smuX.measure.func)`` query.
            - Setting this property to a value will send the ``display.smuX.measure.func = value``
              command.

        TSP Syntax:
            ```
            - display.smuX.measure.func = value
            - print(display.smuX.measure.func)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, display.smua.measure.func
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".func"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.func)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.func`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @func.setter
    def func(self, value: Union[str, float]) -> None:
        """Access the ``display.smuX.measure.func`` attribute.

        Description:
            - This attribute specifies the type of measurement that is being displayed.

        Usage:
            - Accessing this property will send the ``print(display.smuX.measure.func)`` query.
            - Setting this property to a value will send the ``display.smuX.measure.func = value``
              command.

        TSP Syntax:
            ```
            - display.smuX.measure.func = value
            - print(display.smuX.measure.func)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, display.smua.measure.func
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".func", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.func = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.func`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class DisplaySmuxItemLimit(BaseTSPCmd):
    """The ``display.smuX.limit`` command tree.

    Info:
        - ``X``, the source-measure unit (SMU) channel (for example, display.smua.limit.func applies
          to SMU channel A).

    Properties and methods:
        - ``.func``: The ``display.smuX.limit.func`` attribute.
    """

    @property
    def func(self) -> str:
        """Access the ``display.smuX.limit.func`` attribute.

        Description:
            - If you are using a display mode that shows a single channel, this attribute specifies
              the type of limit value setting displayed.

        Usage:
            - Accessing this property will send the ``print(display.smuX.limit.func)`` query.
            - Setting this property to a value will send the ``display.smuX.limit.func = value``
              command.

        TSP Syntax:
            ```
            - display.smuX.limit.func = value
            - print(display.smuX.limit.func)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, display.smua.limit.func
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".func"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.func)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.func`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @func.setter
    def func(self, value: Union[str, float]) -> None:
        """Access the ``display.smuX.limit.func`` attribute.

        Description:
            - If you are using a display mode that shows a single channel, this attribute specifies
              the type of limit value setting displayed.

        Usage:
            - Accessing this property will send the ``print(display.smuX.limit.func)`` query.
            - Setting this property to a value will send the ``display.smuX.limit.func = value``
              command.

        TSP Syntax:
            ```
            - display.smuX.limit.func = value
            - print(display.smuX.limit.func)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, display.smua.limit.func
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".func", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.func = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.func`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class DisplaySmuxItem(ValidatedChannel, BaseTSPCmd):
    """The ``display.smuX`` command tree.

    Info:
        - ``X``, the source-measure unit (SMU) channel (for example, display.smua.digits applies to
          SMU channel A).

    Properties and methods:
        - ``.digits``: The ``display.smuX.digits`` attribute.
        - ``.limit``: The ``display.smuX.limit`` command tree.
        - ``.measure``: The ``display.smuX.measure`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._limit = DisplaySmuxItemLimit(device, f"{self._cmd_syntax}.limit")
        self._measure = DisplaySmuxItemMeasure(device, f"{self._cmd_syntax}.measure")

    @property
    def digits(self) -> str:
        """Access the ``display.smuX.digits`` attribute.

        Description:
            - This attribute sets the front-panel display resolution of the selected measurement.

        Usage:
            - Accessing this property will send the ``print(display.smuX.digits)`` query.
            - Setting this property to a value will send the ``display.smuX.digits = value``
              command.

        TSP Syntax:
            ```
            - display.smuX.digits = value
            - print(display.smuX.digits)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, display.smua.digits applies
              to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".digits"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.digits)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.digits`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @digits.setter
    def digits(self, value: Union[str, float]) -> None:
        """Access the ``display.smuX.digits`` attribute.

        Description:
            - This attribute sets the front-panel display resolution of the selected measurement.

        Usage:
            - Accessing this property will send the ``print(display.smuX.digits)`` query.
            - Setting this property to a value will send the ``display.smuX.digits = value``
              command.

        TSP Syntax:
            ```
            - display.smuX.digits = value
            - print(display.smuX.digits)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, display.smua.digits applies
              to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".digits", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.digits = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.digits`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def limit(self) -> DisplaySmuxItemLimit:
        """Return the ``display.smuX.limit`` command tree.

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, display.smua.limit.func
              applies to SMU channel A).

        Sub-properties and sub-methods:
            - ``.func``: The ``display.smuX.limit.func`` attribute.
        """
        return self._limit

    @property
    def measure(self) -> DisplaySmuxItemMeasure:
        """Return the ``display.smuX.measure`` command tree.

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, display.smua.measure.func
              applies to SMU channel A).

        Sub-properties and sub-methods:
            - ``.func``: The ``display.smuX.measure.func`` attribute.
        """
        return self._measure


class DisplayLoadmenu(BaseTSPCmd):
    """The ``display.loadmenu`` command tree.

    Properties and methods:
        - ``.add()``: The ``display.loadmenu.add()`` function.
        - ``.delete()``: The ``display.loadmenu.delete()`` function.
    """

    def add(self, display_name: str, code: str, memory: Optional[str] = None) -> None:
        """Run the ``display.loadmenu.add()`` function.

        Description:
            - This function adds an entry to the USER menu, which can be accessed by pressing the
              LOAD key on the front panel.

        TSP Syntax:
            ```
            - display.loadmenu.add()
            ```

        Args:
            display_name: The name that is added to the USER menu.
            code: The code that is run from the USER menu.
            memory (optional): Determines if code is saved to nonvolatile memory.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{display_name}"',
                    f'"{code}"',
                    memory,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.add({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.add()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def delete(self, display_name: str) -> None:
        """Run the ``display.loadmenu.delete()`` function.

        Description:
            - This function removes an entry from the USER menu, which can be accessed using the
              LOAD key on the front panel.

        TSP Syntax:
            ```
            - display.loadmenu.delete()
            ```

        Args:
            display_name: The name to be deleted from the USER menu.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.delete("{display_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.delete()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class Display(BaseTSPCmd):
    """The ``display`` command tree.

    Constants:
        - ``.ANNUNCIATOR_4_WIRE``: 4W indicator on.
        - ``.ANNUNCIATOR_ARM``: ARM indicator on.
        - ``.ANNUNCIATOR_AUTO``: AUTO indicator on.
        - ``.ANNUNCIATOR_EDIT``: EDIT indicator on.
        - ``.ANNUNCIATOR_ERROR``: ERR indicator on.
        - ``.ANNUNCIATOR_FILTER``: FILT indicator on.
        - ``.ANNUNCIATOR_LISTEN``: LSTN indicator on.
        - ``.ANNUNCIATOR_MATH``: MATH indicator on.
        - ``.ANNUNCIATOR_REAR``: REAR indicator on.
        - ``.ANNUNCIATOR_REL``: REL indicator on.
        - ``.ANNUNCIATOR_REMOTE``: REM indicator on.
        - ``.ANNUNCIATOR_SAMPLE``: SMPL indicator on.
        - ``.ANNUNCIATOR_SRQ``: SRQ indicator on.
        - ``.ANNUNCIATOR_STAR``: * (asterisk) indicator on.
        - ``.ANNUNCIATOR_TALK``: TALK indicator on.
        - ``.ANNUNCIATOR_TRIGGER``: TRIG indicator on.
        - ``.DIGITS_4_5``: Set the front-panel display resolution to 4.5 digits.
        - ``.DIGITS_5_5``: Set the front-panel display resolution to 5.5 digits.
        - ``.DIGITS_6_5``: Set the front-panel display resolution to 6.5 digits.
        - ``.DISABLE``: Disable the front-panel keys for numeric entry when entering a value.
        - ``.DONT_SAVE``: Do not save code to nonvolatile memory.
        - ``.ENABLE``: Enable the front-panel keys for numeric entry when entering a value.
        - ``.KEY_AUTO``: Represents the range AUTO key.
        - ``.KEY_CONFIG``: Represents the CONFIG key.
        - ``.KEY_DIGITSA``: Represents the DIGITS (display resolution) key.
          For two-channel products, this is the DIGITS key for Channel A.
        - ``.KEY_DIGITSB``: Represents the DIGITS (display resolution) key for Channel B.
        - ``.KEY_DISPLAY``: Represents the DISPLAY key.
        - ``.KEY_ENTER``: Represents the ENTER key.
        - ``.KEY_EXIT``: Represents the EXIT key.
        - ``.KEY_FILTERA``: Represents the FILTER key.
          For two-channel products, this is the FILTER key for Channel A.
        - ``.KEY_FILTERB``: Represents the FILTER key for Channel B.
        - ``.KEY_LEFT``: Represents the left CURSOR key.
        - ``.KEY_LIMITA``: Represents the LIMIT key.
          For two-channel products, this is the LIMIT key for Channel A.
        - ``.KEY_LIMITB``: Represents the LIMIT key.
          For two-channel products, this is the LIMIT key for Channel B.
        - ``.KEY_LOAD``: Represents the LOAD (load test) key.
        - ``.KEY_MEASA``: Represents the MEAS (Measure) key.
          For two-channel products, this is the MEAS key for Channel A.
        - ``.KEY_MEASB``: Represents the MEAS (Measure) key for Channel B.
        - ``.KEY_MENU``: Represents the MENU key.
        - ``.KEY_MODEA``: Represents the MODE (meter mode) key
          For two-channel products, this is the MODE key for Channel A.
        - ``.KEY_MODEB``: Represents the MODE (meter mode) key for Channel B.
        - ``.KEY_NONE``: No key was pressed.
        - ``.KEY_OUTPUTA``: Represents the OUTPUT ON/OFF key.
          For two-channel products, this is the OUTPUT ON/OFF key for Channel A.
        - ``.KEY_OUTPUTB``: Represents the OUTPUT ON/OFF key.
          For two-channel products, this is the OUTPUT ON/OFF key for Channel B.
        - ``.KEY_RANGEDOWN``: Represents the RANGE down key.
        - ``.KEY_RANGEUP``: Represents the RANGE up key.
        - ``.KEY_RECALL``: Represents the RECALL key.
        - ``.KEY_RELA``: Represents the REL key.
          For two-channel products, this is the REL key for Channel A.
        - ``.KEY_RELB``: Represents the REL key for Channel B.
        - ``.KEY_RIGHT``: Represents the right CURSOR key.
        - ``.KEY_RUN``: Represents the RUN key.
        - ``.KEY_SPEEDA``: Represents the SPEED key.
          For two-channel products, this is the SPEED key for Channel A.
        - ``.KEY_SPEEDB``: Represents the SPEED key.
          For two-channel products, this is the SPEED key for Channel B.
        - ``.KEY_SRCA``: Represents the SRC (Source) key.
          For two-channel products, this is the SRC key for Channel A.
        - ``.KEY_SRCB``: Represents the SRC (Source) key for Channel B.
        - ``.KEY_STORE``: Represents the STORE key.
        - ``.KEY_TRIG``: Represents the TRIG key.
        - ``.LIMIT_IV``: Display the primary limit value.
        - ``.LIMIT_P``: Display the power limit value.
        - ``.LOCK``: Unlock the EXIT (LOCAL) key.
        - ``.MEASURE_DCAMPS``: Display the current measurement function.
        - ``.MEASURE_DCVOLTS``: Display the voltage measurement function.
        - ``.MEASURE_OHMS``: Display the resistance measurement function.
        - ``.MEASURE_WATTS``: Display the power measurement function.
        - ``.SAVE``: Save code to nonvolatile memory.
        - ``.SMUA_SMUB``: Displays source-measure screen for SMU A and SMU B.
        - ``.SMUB``: Displays source-measure and compliance screen for SMU B.
        - ``.UNLOCK``: Lock out the EXIT (LOCAL) key.
        - ``.WHEEL_ENTER``: Represents pressing the navigation wheel.
        - ``.WHEEL_LEFT``: Represents turning the Navigation wheel left.
        - ``.WHEEL_RIGHT``: Represents turning the Navigation wheel right.

    Properties and methods:
        - ``.clear()``: The ``display.clear()`` function.
        - ``.getannunciators()``: The ``display.getannunciators()`` function.
        - ``.getcursor()``: The ``display.getcursor()`` function.
        - ``.getlastkey()``: The ``display.getlastkey()`` function.
        - ``.gettext()``: The ``display.gettext()`` function.
        - ``.inputvalue()``: The ``display.inputvalue()`` function.
        - ``.loadmenu``: The ``display.loadmenu`` command tree.
        - ``.locallockout``: The ``display.locallockout`` attribute.
        - ``.menu()``: The ``display.menu()`` function.
        - ``.numpad``: The ``display.numpad`` attribute.
        - ``.prompt()``: The ``display.prompt()`` function.
        - ``.screen``: The ``display.screen`` attribute.
        - ``.sendkey()``: The ``display.sendkey()`` function.
        - ``.setcursor()``: The ``display.setcursor()`` function.
        - ``.settext()``: The ``display.settext()`` function.
        - ``.smu``: The ``display.smuX`` command tree.
        - ``.trigger``: The ``display.trigger`` command tree.
        - ``.waitkey()``: The ``display.waitkey()`` function.
    """

    ANNUNCIATOR_4_WIRE = "display.ANNUNCIATOR_4_WIRE"
    """str: 4W indicator on."""
    ANNUNCIATOR_ARM = "display.ANNUNCIATOR_ARM"
    """str: ARM indicator on."""
    ANNUNCIATOR_AUTO = "display.ANNUNCIATOR_AUTO"
    """str: AUTO indicator on."""
    ANNUNCIATOR_EDIT = "display.ANNUNCIATOR_EDIT"
    """str: EDIT indicator on."""
    ANNUNCIATOR_ERROR = "display.ANNUNCIATOR_ERROR"
    """str: ERR indicator on."""
    ANNUNCIATOR_FILTER = "display.ANNUNCIATOR_FILTER"
    """str: FILT indicator on."""
    ANNUNCIATOR_LISTEN = "display.ANNUNCIATOR_LISTEN"
    """str: LSTN indicator on."""
    ANNUNCIATOR_MATH = "display.ANNUNCIATOR_MATH"
    """str: MATH indicator on."""
    ANNUNCIATOR_REAR = "display.ANNUNCIATOR_REAR"
    """str: REAR indicator on."""
    ANNUNCIATOR_REL = "display.ANNUNCIATOR_REL"
    """str: REL indicator on."""
    ANNUNCIATOR_REMOTE = "display.ANNUNCIATOR_REMOTE"
    """str: REM indicator on."""
    ANNUNCIATOR_SAMPLE = "display.ANNUNCIATOR_SAMPLE"
    """str: SMPL indicator on."""
    ANNUNCIATOR_SRQ = "display.ANNUNCIATOR_SRQ"
    """str: SRQ indicator on."""
    ANNUNCIATOR_STAR = "display.ANNUNCIATOR_STAR"
    """str: * (asterisk) indicator on."""
    ANNUNCIATOR_TALK = "display.ANNUNCIATOR_TALK"
    """str: TALK indicator on."""
    ANNUNCIATOR_TRIGGER = "display.ANNUNCIATOR_TRIGGER"
    """str: TRIG indicator on."""
    DIGITS_4_5 = "display.DIGITS_4_5"
    """str: Set the front-panel display resolution to 4.5 digits."""
    DIGITS_5_5 = "display.DIGITS_5_5"
    """str: Set the front-panel display resolution to 5.5 digits."""
    DIGITS_6_5 = "display.DIGITS_6_5"
    """str: Set the front-panel display resolution to 6.5 digits."""
    DISABLE = "display.DISABLE"
    """str: Disable the front-panel keys for numeric entry when entering a value."""
    DONT_SAVE = "display.DONT_SAVE"
    """str: Do not save code to nonvolatile memory."""
    ENABLE = "display.ENABLE"
    """str: Enable the front-panel keys for numeric entry when entering a value."""
    KEY_AUTO = "display.KEY_AUTO"
    """str: Represents the range AUTO key."""
    KEY_CONFIG = "display.KEY_CONFIG"
    """str: Represents the CONFIG key."""
    KEY_DIGITSA = "display.KEY_DIGITSA"
    """str: Represents the DIGITS (display resolution) key.
For two-channel products, this is the DIGITS key for Channel A."""
    KEY_DIGITSB = "display.KEY_DIGITSB"
    """str: Represents the DIGITS (display resolution) key for Channel B."""
    KEY_DISPLAY = "display.KEY_DISPLAY"
    """str: Represents the DISPLAY key."""
    KEY_ENTER = "display.KEY_ENTER"
    """str: Represents the ENTER key."""
    KEY_EXIT = "display.KEY_EXIT"
    """str: Represents the EXIT key."""
    KEY_FILTERA = "display.KEY_FILTERA"
    """str: Represents the FILTER key.
For two-channel products, this is the FILTER key for Channel A."""
    KEY_FILTERB = "display.KEY_FILTERB"
    """str: Represents the FILTER key for Channel B."""
    KEY_LEFT = "display.KEY_LEFT"
    """str: Represents the left CURSOR key."""
    KEY_LIMITA = "display.KEY_LIMITA"
    """str: Represents the LIMIT key.
For two-channel products, this is the LIMIT key for Channel A."""
    KEY_LIMITB = "display.KEY_LIMITB"
    """str: Represents the LIMIT key.
For two-channel products, this is the LIMIT key for Channel B."""
    KEY_LOAD = "display.KEY_LOAD"
    """str: Represents the LOAD (load test) key."""
    KEY_MEASA = "display.KEY_MEASA"
    """str: Represents the MEAS (Measure) key.
For two-channel products, this is the MEAS key for Channel A."""
    KEY_MEASB = "display.KEY_MEASB"
    """str: Represents the MEAS (Measure) key for Channel B."""
    KEY_MENU = "display.KEY_MENU"
    """str: Represents the MENU key."""
    KEY_MODEA = "display.KEY_MODEA"
    """str: Represents the MODE (meter mode) key
For two-channel products, this is the MODE key for Channel A."""
    KEY_MODEB = "display.KEY_MODEB"
    """str: Represents the MODE (meter mode) key for Channel B."""
    KEY_NONE = "display.KEY_NONE"
    """str: No key was pressed."""
    KEY_OUTPUTA = "display.KEY_OUTPUTA"
    """str: Represents the OUTPUT ON/OFF key.
For two-channel products, this is the OUTPUT ON/OFF key for Channel A."""
    KEY_OUTPUTB = "display.KEY_OUTPUTB"
    """str: Represents the OUTPUT ON/OFF key.
For two-channel products, this is the OUTPUT ON/OFF key for Channel B."""
    KEY_RANGEDOWN = "display.KEY_RANGEDOWN"
    """str: Represents the RANGE down key."""
    KEY_RANGEUP = "display.KEY_RANGEUP"
    """str: Represents the RANGE up key."""
    KEY_RECALL = "display.KEY_RECALL"
    """str: Represents the RECALL key."""
    KEY_RELA = "display.KEY_RELA"
    """str: Represents the REL key.
For two-channel products, this is the REL key for Channel A."""
    KEY_RELB = "display.KEY_RELB"
    """str: Represents the REL key for Channel B."""
    KEY_RIGHT = "display.KEY_RIGHT"
    """str: Represents the right CURSOR key."""
    KEY_RUN = "display.KEY_RUN"
    """str: Represents the RUN key."""
    KEY_SPEEDA = "display.KEY_SPEEDA"
    """str: Represents the SPEED key.
For two-channel products, this is the SPEED key for Channel A."""
    KEY_SPEEDB = "display.KEY_SPEEDB"
    """str: Represents the SPEED key.
For two-channel products, this is the SPEED key for Channel B."""
    KEY_SRCA = "display.KEY_SRCA"
    """str: Represents the SRC (Source) key.
For two-channel products, this is the SRC key for Channel A."""
    KEY_SRCB = "display.KEY_SRCB"
    """str: Represents the SRC (Source) key for Channel B."""
    KEY_STORE = "display.KEY_STORE"
    """str: Represents the STORE key."""
    KEY_TRIG = "display.KEY_TRIG"
    """str: Represents the TRIG key."""
    LIMIT_IV = "display.LIMIT_IV"
    """str: Display the primary limit value."""
    LIMIT_P = "display.LIMIT_P"
    """str: Display the power limit value."""
    LOCK = "display.LOCK"
    """str: Unlock the EXIT (LOCAL) key."""
    MEASURE_DCAMPS = "display.MEASURE_DCAMPS"
    """str: Display the current measurement function."""
    MEASURE_DCVOLTS = "display.MEASURE_DCVOLTS"
    """str: Display the voltage measurement function."""
    MEASURE_OHMS = "display.MEASURE_OHMS"
    """str: Display the resistance measurement function."""
    MEASURE_WATTS = "display.MEASURE_WATTS"
    """str: Display the power measurement function."""
    SAVE = "display.SAVE"
    """str: Save code to nonvolatile memory."""
    SMUA_SMUB = "display.SMUA_SMUB"
    """str: Displays source-measure screen for SMU A and SMU B."""
    SMUB = "display.SMUB"
    """str: Displays source-measure and compliance screen for SMU B."""
    UNLOCK = "display.UNLOCK"
    """str: Lock out the EXIT (LOCAL) key."""
    WHEEL_ENTER = "display.WHEEL_ENTER"
    """str: Represents pressing the navigation wheel."""
    WHEEL_LEFT = "display.WHEEL_LEFT"
    """str: Represents turning the Navigation wheel left."""
    WHEEL_RIGHT = "display.WHEEL_RIGHT"
    """str: Represents turning the Navigation wheel right."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "display") -> None:
        super().__init__(device, cmd_syntax)
        self._loadmenu = DisplayLoadmenu(device, f"{self._cmd_syntax}.loadmenu")
        self._smu: Dict[str, DisplaySmuxItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplaySmuxItem(device, f"{self._cmd_syntax}.smu{x}")
        )
        self._trigger = DisplayTrigger(device, f"{self._cmd_syntax}.trigger")

    @property
    def loadmenu(self) -> DisplayLoadmenu:
        """Return the ``display.loadmenu`` command tree.

        Sub-properties and sub-methods:
            - ``.add()``: The ``display.loadmenu.add()`` function.
            - ``.delete()``: The ``display.loadmenu.delete()`` function.
        """
        return self._loadmenu

    @property
    def locallockout(self) -> str:
        """Access the ``display.locallockout`` attribute.

        Description:
            - This attribute describes whether or not the EXIT (LOCAL) key on the instrument front
              panel is enabled.

        Usage:
            - Accessing this property will send the ``print(display.locallockout)`` query.
            - Setting this property to a value will send the ``display.locallockout = value``
              command.

        TSP Syntax:
            ```
            - display.locallockout = value
            - print(display.locallockout)
            ```

        Info:
            - ``lockout``, the 0 or display.UNLOCK: Unlocks EXIT (LOCAL) key
              1 or display.LOCK: Locks out EXIT (LOCAL) key.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".locallockout"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.locallockout)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.locallockout`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @locallockout.setter
    def locallockout(self, value: Union[str, float]) -> None:
        """Access the ``display.locallockout`` attribute.

        Description:
            - This attribute describes whether or not the EXIT (LOCAL) key on the instrument front
              panel is enabled.

        Usage:
            - Accessing this property will send the ``print(display.locallockout)`` query.
            - Setting this property to a value will send the ``display.locallockout = value``
              command.

        TSP Syntax:
            ```
            - display.locallockout = value
            - print(display.locallockout)
            ```

        Info:
            - ``lockout``, the 0 or display.UNLOCK: Unlocks EXIT (LOCAL) key
              1 or display.LOCK: Locks out EXIT (LOCAL) key.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".locallockout", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.locallockout = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.locallockout`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def numpad(self) -> str:
        """Access the ``display.numpad`` attribute.

        Description:
            - This attribute controls whether the front panel keys act as a numeric keypad during
              value entry.

        Usage:
            - Accessing this property will send the ``print(display.numpad)`` query.
            - Setting this property to a value will send the ``display.numpad = value`` command.

        TSP Syntax:
            ```
            - display.numpad = value
            - print(display.numpad)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".numpad"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.numpad)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.numpad`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @numpad.setter
    def numpad(self, value: Union[str, float]) -> None:
        """Access the ``display.numpad`` attribute.

        Description:
            - This attribute controls whether the front panel keys act as a numeric keypad during
              value entry.

        Usage:
            - Accessing this property will send the ``print(display.numpad)`` query.
            - Setting this property to a value will send the ``display.numpad = value`` command.

        TSP Syntax:
            ```
            - display.numpad = value
            - print(display.numpad)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".numpad", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.numpad = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.numpad`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def screen(self) -> str:
        """Access the ``display.screen`` attribute.

        Description:
            - This attribute contains the selected display screen.

        Usage:
            - Accessing this property will send the ``print(display.screen)`` query.
            - Setting this property to a value will send the ``display.screen = value`` command.

        TSP Syntax:
            ```
            - display.screen = value
            - print(display.screen)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".screen"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.screen)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.screen`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @screen.setter
    def screen(self, value: Union[str, float]) -> None:
        """Access the ``display.screen`` attribute.

        Description:
            - This attribute contains the selected display screen.

        Usage:
            - Accessing this property will send the ``print(display.screen)`` query.
            - Setting this property to a value will send the ``display.screen = value`` command.

        TSP Syntax:
            ```
            - display.screen = value
            - print(display.screen)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".screen", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.screen = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.screen`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def smu(self) -> Dict[str, DisplaySmuxItem]:
        """Return the ``display.smuX`` command tree.

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, display.smua.digits applies
              to SMU channel A).

        Sub-properties and sub-methods:
            - ``.digits``: The ``display.smuX.digits`` attribute.
            - ``.limit``: The ``display.smuX.limit`` command tree.
            - ``.measure``: The ``display.smuX.measure`` command tree.
        """
        return self._smu

    @property
    def trigger(self) -> DisplayTrigger:
        """Return the ``display.trigger`` command tree.

        Constants:
            - ``.EVENT_ID``: The event ID of the event generated when the front-panel TRIG key is
              pressed.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``display.trigger.clear()`` function.
            - ``.overrun``: The ``display.trigger.overrun`` attribute.
            - ``.wait()``: The ``display.trigger.wait()`` function.
        """
        return self._trigger

    def clear(self) -> None:
        """Run the ``display.clear()`` function.

        Description:
            - This function clears all lines of the front-panel display.

        TSP Syntax:
            ```
            - display.clear()
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

    def getannunciators(self) -> str:
        """Run the ``display.getannunciators()`` function.

        Description:
            - This function reads the annunciators (indicators) that are presently turned on.

        TSP Syntax:
            ```
            - display.getannunciators()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.getannunciators())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getannunciators()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getcursor(self) -> str:
        """Run the ``display.getcursor()`` function.

        Description:
            - This function reads the present position of the cursor on the front-panel display.

        TSP Syntax:
            ```
            - display.getcursor()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.getcursor())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getcursor()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getlastkey(self) -> str:
        """Run the ``display.getlastkey()`` function.

        Description:
            - This function retrieves the key code for the last pressed key.

        TSP Syntax:
            ```
            - display.getlastkey()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.getlastkey())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getlastkey()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def gettext(
        self,
        embellished: Optional[str] = None,
        row: Optional[str] = None,
        column_start: Optional[str] = None,
        column_end: Optional[int] = None,
    ) -> str:
        """Run the ``display.gettext()`` function.

        Description:
            - This function reads the text displayed on the front panel.

        TSP Syntax:
            ```
            - display.gettext()
            ```

        Args:
            embellished (optional): Indicates type of returned text.
            row (optional): Selects the row from which to read the text.
            column_start (optional): Selects the first column from which to read text; for row 1,
                the valid column numbers are 1 to 20; for row 2, the valid column numbers are 1 to
                32; if nothing is selected, 1 is used.
            column_end (optional): Selects the last column from which to read text; for row 1, the
                valid column numbers are 1 to 20; for row 2, the valid column numbers are 1 to 32;
                the default is 20 for row 1, and 32 for row 2.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    embellished,
                    row,
                    column_start,
                    column_end,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.gettext({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.gettext()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def inputvalue(
        self,
        format_: str,
        default: Optional[str] = None,
        minimum: Optional[str] = None,
        maximum: Optional[str] = None,
    ) -> str:
        """Run the ``display.inputvalue()`` function.

        Description:
            - This function displays a formatted input field on the front-panel display that the
              operator can edit.

        TSP Syntax:
            ```
            - display.inputvalue()
            ```

        Args:
            format_: A string that defines how the input field is formatted; see Details for more
                information.
            default (optional): The default value for the input value.
            minimum (optional): The minimum input value.
            maximum (optional): The maximum input value.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{format_}"',
                    default,
                    minimum,
                    maximum,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.inputvalue({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.inputvalue()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def menu(self, name: str, items: str) -> str:
        """Run the ``display.menu()`` function.

        Description:
            - This function presents a menu on the front-panel display.

        TSP Syntax:
            ```
            - display.menu()
            ```

        Args:
            name: Menu name to display on the top line.
            items: Menu items to display on the bottom line.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.menu("{name}", "{items}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.menu()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def prompt(
        self,
        format_: str,
        units: str,
        help_: str,
        default: Optional[str] = None,
        minimum: Optional[str] = None,
        maximum: Optional[str] = None,
    ) -> str:
        """Run the ``display.prompt()`` function.

        Description:
            - This function prompts the user to enter a parameter from the front panel of the
              instrument.

        TSP Syntax:
            ```
            - display.prompt()
            ```

        Args:
            format_: A string that defines how the input field is formatted; see Details for more
                information.
            units: Set the units text string for the top line (eight characters maximum); this
                indicates the units (for example, 'V' or 'A') for the value.
            help_: Text string to display on the bottom line (32 characters maximum).
            default (optional): The value that is shown when the value is first displayed.
            minimum (optional): The minimum input value that can be entered.
            maximum (optional): The maximum input value that can be entered (must be more than
                minimum).

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{format_}"',
                    f'"{units}"',
                    f'"{help_}"',
                    default,
                    minimum,
                    maximum,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.prompt({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.prompt()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def sendkey(self, key_code: str) -> None:
        """Run the ``display.sendkey()`` function.

        Description:
            - This function sends a code that simulates the action of a front-panel control.

        TSP Syntax:
            ```
            - display.sendkey()
            ```

        Args:
            key_code: A parameter that specifies the key press to simulate; see Details for more
                information.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.sendkey({key_code})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.sendkey()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setcursor(self, row: str, column: str, style: Optional[str] = None) -> None:
        """Run the ``display.setcursor()`` function.

        Description:
            - This function sets the position of the cursor.

        TSP Syntax:
            ```
            - display.setcursor()
            ```

        Args:
            row: The row number for the cursor (1 or 2).
            column: The active column position to set; row 1 has columns 1 to 20, row 2 has columns
                1 to 32.
            style (optional): Set the cursor to invisible (0, default) or blinking (1).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    row,
                    column,
                    style,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setcursor({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setcursor()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def settext(self, text: str) -> None:
        """Run the ``display.settext()`` function.

        Description:
            - This function displays text on the front-panel user screen.

        TSP Syntax:
            ```
            - display.settext()
            ```

        Args:
            text: Text message to be displayed, with optional character codes.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.settext("{text}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.settext()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def waitkey(self) -> str:
        """Run the ``display.waitkey()`` function.

        Description:
            - This function captures the key code value for the next front-panel action.

        TSP Syntax:
            ```
            - display.waitkey()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.waitkey())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.waitkey()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
