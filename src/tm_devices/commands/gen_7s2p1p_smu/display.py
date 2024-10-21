# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The display commands module.

These commands are used in the following models:
SMU2601B_Pulse

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - display.getlastkey()
    - display.screen
    - display.sendkey()
    - display.smuX.digits
    - display.smuX.limit.func
    - display.smuX.measure.func
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


# pylint: disable=too-few-public-methods
class DisplayTrigger(BaseTSPCmd):
    """The ``display.trigger`` command tree.

    Constants:
        - ``.EVENT_ID``: Selects the event that causes a trigger to be asserted on the digital
          output line when the TRIG key on the front panel is pressed.
    """

    EVENT_ID = "display.trigger.EVENT_ID"
    """str: Selects the event that causes a trigger to be asserted on the digital output line when the TRIG key on the front panel is pressed."""  # noqa: E501


class DisplaySmuxItemMeasure(BaseTSPCmd):
    """The ``display.smuX.measure`` command tree.

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

    Properties and methods:
        - ``.func``: The ``display.smuX.limit.func`` attribute.
    """

    @property
    def func(self) -> str:
        """Access the ``display.smuX.limit.func`` attribute.

        Description:
            - This attribute specifies the type of limit value setting displayed for the SMU.

        Usage:
            - Accessing this property will send the ``print(display.smuX.limit.func)`` query.
            - Setting this property to a value will send the ``display.smuX.limit.func = value``
              command.

        TSP Syntax:
            ```
            - display.smuX.limit.func = value
            - print(display.smuX.limit.func)
            ```

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
            - This attribute specifies the type of limit value setting displayed for the SMU.

        Usage:
            - Accessing this property will send the ``print(display.smuX.limit.func)`` query.
            - Setting this property to a value will send the ``display.smuX.limit.func = value``
              command.

        TSP Syntax:
            ```
            - display.smuX.limit.func = value
            - print(display.smuX.limit.func)
            ```

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

        Sub-properties and sub-methods:
            - ``.func``: The ``display.smuX.limit.func`` attribute.
        """
        return self._limit

    @property
    def measure(self) -> DisplaySmuxItemMeasure:
        """Return the ``display.smuX.measure`` command tree.

        Sub-properties and sub-methods:
            - ``.func``: The ``display.smuX.measure.func`` attribute.
        """
        return self._measure


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
        - ``.KEY_DISPLAY``: Represents the DISPLAY key.
        - ``.KEY_ENTER``: Represents the ENTER key.
        - ``.KEY_EXIT``: Represents the EXIT key.
        - ``.KEY_FILTERA``: Represents the FILTER key.
          For two-channel products, this is the FILTER key for Channel A.
        - ``.KEY_LEFT``: Represents the left CURSOR key.
        - ``.KEY_LIMITA``: Represents the LIMIT key.
          For two-channel products, this is the LIMIT key for Channel A.
        - ``.KEY_LOAD``: Represents the LOAD (load test) key.
        - ``.KEY_MEASA``: Represents the MEAS (Measure) key.
          For two-channel products, this is the MEAS key for Channel A.
        - ``.KEY_MENU``: Represents the MENU key.
        - ``.KEY_MODEA``: Represents the MODE (meter mode) key
          For two-channel products, this is the MODE key for Channel A.
        - ``.KEY_NONE``: No key was pressed.
        - ``.KEY_OUTPUTA``: Represents the OUTPUT ON/OFF key.
          For two-channel products, this is the OUTPUT ON/OFF key for Channel A.
        - ``.KEY_RANGEDOWN``: Represents the RANGE down key.
        - ``.KEY_RANGEUP``: Represents the RANGE up key.
        - ``.KEY_RECALL``: Represents the RECALL key.
        - ``.KEY_RELA``: Represents the REL key.
          For two-channel products, this is the REL key for Channel A.
        - ``.KEY_RIGHT``: Represents the right CURSOR key.
        - ``.KEY_RUN``: Represents the RUN key.
        - ``.KEY_SPEEDA``: Represents the SPEED key.
          For two-channel products, this is the SPEED key for Channel A.
        - ``.KEY_SRCA``: Represents the SRC (Source) key.
          For two-channel products, this is the SRC key for Channel A.
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
        - ``.SMUA``: Displays source-measure and compliance screen for SMU A.
        - ``.UNLOCK``: Lock out the EXIT (LOCAL) key.
        - ``.USER``: Displays the user screen.
        - ``.WHEEL_ENTER``: Represents pressing the navigation wheel.
        - ``.WHEEL_LEFT``: Represents turning the Navigation wheel left.
        - ``.WHEEL_RIGHT``: Represents turning the Navigation wheel right.

    Properties and methods:
        - ``.getlastkey()``: The ``display.getlastkey()`` function.
        - ``.screen``: The ``display.screen`` attribute.
        - ``.sendkey()``: The ``display.sendkey()`` function.
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
    KEY_DISPLAY = "display.KEY_DISPLAY"
    """str: Represents the DISPLAY key."""
    KEY_ENTER = "display.KEY_ENTER"
    """str: Represents the ENTER key."""
    KEY_EXIT = "display.KEY_EXIT"
    """str: Represents the EXIT key."""
    KEY_FILTERA = "display.KEY_FILTERA"
    """str: Represents the FILTER key.
For two-channel products, this is the FILTER key for Channel A."""
    KEY_LEFT = "display.KEY_LEFT"
    """str: Represents the left CURSOR key."""
    KEY_LIMITA = "display.KEY_LIMITA"
    """str: Represents the LIMIT key.
For two-channel products, this is the LIMIT key for Channel A."""
    KEY_LOAD = "display.KEY_LOAD"
    """str: Represents the LOAD (load test) key."""
    KEY_MEASA = "display.KEY_MEASA"
    """str: Represents the MEAS (Measure) key.
For two-channel products, this is the MEAS key for Channel A."""
    KEY_MENU = "display.KEY_MENU"
    """str: Represents the MENU key."""
    KEY_MODEA = "display.KEY_MODEA"
    """str: Represents the MODE (meter mode) key
For two-channel products, this is the MODE key for Channel A."""
    KEY_NONE = "display.KEY_NONE"
    """str: No key was pressed."""
    KEY_OUTPUTA = "display.KEY_OUTPUTA"
    """str: Represents the OUTPUT ON/OFF key.
For two-channel products, this is the OUTPUT ON/OFF key for Channel A."""
    KEY_RANGEDOWN = "display.KEY_RANGEDOWN"
    """str: Represents the RANGE down key."""
    KEY_RANGEUP = "display.KEY_RANGEUP"
    """str: Represents the RANGE up key."""
    KEY_RECALL = "display.KEY_RECALL"
    """str: Represents the RECALL key."""
    KEY_RELA = "display.KEY_RELA"
    """str: Represents the REL key.
For two-channel products, this is the REL key for Channel A."""
    KEY_RIGHT = "display.KEY_RIGHT"
    """str: Represents the right CURSOR key."""
    KEY_RUN = "display.KEY_RUN"
    """str: Represents the RUN key."""
    KEY_SPEEDA = "display.KEY_SPEEDA"
    """str: Represents the SPEED key.
For two-channel products, this is the SPEED key for Channel A."""
    KEY_SRCA = "display.KEY_SRCA"
    """str: Represents the SRC (Source) key.
For two-channel products, this is the SRC key for Channel A."""
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
    SMUA = "display.SMUA"
    """str: Displays source-measure and compliance screen for SMU A."""
    UNLOCK = "display.UNLOCK"
    """str: Lock out the EXIT (LOCAL) key."""
    USER = "display.USER"
    """str: Displays the user screen."""
    WHEEL_ENTER = "display.WHEEL_ENTER"
    """str: Represents pressing the navigation wheel."""
    WHEEL_LEFT = "display.WHEEL_LEFT"
    """str: Represents turning the Navigation wheel left."""
    WHEEL_RIGHT = "display.WHEEL_RIGHT"
    """str: Represents turning the Navigation wheel right."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "display") -> None:
        super().__init__(device, cmd_syntax)
        self._smu: Dict[str, DisplaySmuxItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplaySmuxItem(device, f"{self._cmd_syntax}.smu{x}")
        )
        self._trigger = DisplayTrigger(device, f"{self._cmd_syntax}.trigger")

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
            - ``.EVENT_ID``: Selects the event that causes a trigger to be asserted on the digital
              output line when the TRIG key on the front panel is pressed.
        """
        return self._trigger

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
