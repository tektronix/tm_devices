# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The display commands module.

These commands are used in the following models:
SS3706A

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
    - display.prompt()
    - display.screen
    - display.sendkey()
    - display.setcursor()
    - display.settext()
    - display.waitkey()
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


# pylint: disable=too-few-public-methods
class DisplayTrigger(BaseTSPCmd):
    """The ``display.trigger`` command tree.

    Constants:
        - ``.EVENT_ID``: The event ID of the event generated when the front-panel TRIG key is
          pressed.
    """

    EVENT_ID = "display.trigger.EVENT_ID"
    """str: The event ID of the event generated when the front-panel TRIG key is pressed."""


class DisplayLoadmenu(BaseTSPCmd):
    """The ``display.loadmenu`` command tree.

    Properties and methods:
        - ``.add()``: The ``display.loadmenu.add()`` function.
        - ``.delete()``: The ``display.loadmenu.delete()`` function.
    """

    def add(self, display_name: str, code: str, memory: Optional[str] = None) -> None:
        """Run the ``display.loadmenu.add()`` function.

        Description:
            - This function adds an entry to the USER TESTS menu, which can be accessed by pressing
              the LOAD key on the front panel.

        TSP Syntax:
            ```
            - display.loadmenu.add()
            ```

        Args:
            display_name: The name that is added to the USER TESTS menu.
            code: The code that is run from the USER TESTS menu.
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
            - This function removes an entry from the USER TESTS menu, which can be accessed using
              the LOAD key on the front panel.

        TSP Syntax:
            ```
            - display.loadmenu.delete()
            ```

        Args:
            display_name: The name to be deleted from the USER TESTS menu.

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
        - ``.prompt()``: The ``display.prompt()`` function.
        - ``.screen``: The ``display.screen`` attribute.
        - ``.sendkey()``: The ``display.sendkey()`` function.
        - ``.setcursor()``: The ``display.setcursor()`` function.
        - ``.settext()``: The ``display.settext()`` function.
        - ``.trigger``: The ``display.trigger`` command tree.
        - ``.waitkey()``: The ``display.waitkey()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "display") -> None:
        super().__init__(device, cmd_syntax)
        self._loadmenu = DisplayLoadmenu(device, f"{self._cmd_syntax}.loadmenu")
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
            - This attribute describes whether or not the EXIT (LOCAL) key on the instrument
              virtualfront panel is enabled.

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
            - This attribute describes whether or not the EXIT (LOCAL) key on the instrument
              virtualfront panel is enabled.

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
    def trigger(self) -> DisplayTrigger:
        """Return the ``display.trigger`` command tree.

        Constants:
            - ``.EVENT_ID``: The event ID of the event generated when the front-panel TRIG key is
              pressed.
        """
        return self._trigger

    def clear(self) -> None:
        """Run the ``display.clear()`` function.

        Description:
            - This function clears the text from the front-panel USER swipe screen.

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
            - This function reads the present position of the cursor on the virtualfront-panel
              display.

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
            - This function reads the text displayed on the virtualfront panel.

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
            - This function displays a formatted input field on the virtualfront-panel display that
              the operator can edit.

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
            - This function presents a menu on the virtualfront-panel display.

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

    def prompt(self, button_id: str, prompt_text: str) -> str:
        """Run the ``display.prompt()`` function.

        Description:
            - This function allows you to create an interactive dialog prompt that displays a custom
              message on the front-panel display.

        TSP Syntax:
            ```
            - display.prompt()
            ```

        Args:
            button_id: The type of prompt to display; choose one of the following options.
            prompt_text: A string that contains the text that is displayed above the prompts.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.prompt({button_id}, "{prompt_text}"))'
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

    def settext(
        self, user_display_text1: Optional[str] = None, user_display_text2: Optional[str] = None
    ) -> None:
        """Run the ``display.settext()`` function.

        Description:
            - This function defines the text that is displayed on the front-panel USER swipe screen.

        TSP Syntax:
            ```
            - display.settext()
            ```

        Args:
            user_display_text1 (optional): String that contains the message for the top line of the
                USER swipe screen (up to 20 characters).
            user_display_text2 (optional): String that contains the message for the bottom line of
                the USER swipe screen (up to 32 characters).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{user_display_text1}"' if user_display_text1 is not None else None,
                    f'"{user_display_text2}"' if user_display_text2 is not None else None,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.settext({function_args})"
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
