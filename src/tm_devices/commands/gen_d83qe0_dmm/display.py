# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The display commands module.

These commands are used in the following models:
DMM6500

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - display.activebuffer
    - display.changescreen()
    - display.clear()
    - display.delete()
    - display.input.number()
    - display.input.option()
    - display.input.prompt()
    - display.input.string()
    - display.lightstate
    - display.prompt()
    - display.readingformat
    - display.settext()
    - display.waitevent()
    - display.watchchannels
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class DisplayInput(BaseTSPCmd):
    """The ``display.input`` command tree.

    Properties and methods:
        - ``.number()``: The ``display.input.number()`` function.
        - ``.option()``: The ``display.input.option()`` function.
        - ``.prompt()``: The ``display.input.prompt()`` function.
        - ``.string()``: The ``display.input.string()`` function.
    """

    def number(
        self,
        dialog_title: str,
        number_format: Optional[str] = None,
        default_value: Optional[str] = None,
        minimum_value: Optional[str] = None,
        maximum_value: Optional[str] = None,
    ) -> str:
        """Run the ``display.input.number()`` function.

        Description:
            - This function allows you to create a prompt that requests a number from the user on
              the front-panel display.

        TSP Syntax:
            ```
            - display.input.number()
            ```

        Args:
            dialog_title: A string that contains the text to be displayed as the title of the dialog
                box on the front-panel display; can be up to 32 characters.
            number_format (optional): The format of the displayed number.
            default_value (optional): The value that is initially displayed in the displayed keypad.
            minimum_value (optional): The lowest value that can be entered.
            maximum_value (optional): The highest value that can be entered.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{dialog_title}"',
                    number_format,
                    default_value,
                    minimum_value,
                    maximum_value,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.number({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.number()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def option(self, dialog_title: str, button_title1: str, button_title2: str) -> str:
        """Run the ``display.input.option()`` function.

        Description:
            - This function allows you to create an option dialog box with customizable buttons on
              the front-panel display.

        TSP Syntax:
            ```
            - display.input.option()
            ```

        Args:
            dialog_title: A string that contains the text to be displayed as the title of the dialog
                box on the front-panel display; up to 32 characters.
            button_title1: A string that contains the name of the first button; up to 15 characters.
            button_title2: A string that contains the name of the second button; up to 15
                characters.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.option("{dialog_title}", '
                f'"{button_title1}", '
                f'"{button_title2}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.option()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def prompt(self, button_set: str, dialog_title: str) -> str:
        """Run the ``display.input.prompt()`` function.

        Description:
            - This function allows you to create a prompt that accepts a user response from the
              front-panel display.

        TSP Syntax:
            ```
            - display.input.prompt()
            ```

        Args:
            button_set: The set of buttons to display.
            dialog_title: A string that contains the text to be displayed as the title of the dialog
                box on the front-panel display; up to 63 characters.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.prompt({button_set}, "{dialog_title}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.prompt()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def string(self, dialog_title: str, text_format: Optional[str] = None) -> str:
        """Run the ``display.input.string()`` function.

        Description:
            - This function allows you to create a dialog box that requests text from the user
              through the front-panel display.

        TSP Syntax:
            ```
            - display.input.string()
            ```

        Args:
            dialog_title: A string that contains the text to be displayed as the title of the dialog
                box on the front-panel display; up to 32 characters.
            text_format (optional): The format of the entered text.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{dialog_title}"',
                    text_format,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.string({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.string()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class Display(BaseTSPCmd):
    """The ``display`` command tree.

    Constants:
        - ``.BUTTONS_CANCEL``: Display CANCEL on dialog.
        - ``.BUTTONS_NONE``: Display nothing on dialog.
        - ``.BUTTONS_OK``: Display OK on dialog.
        - ``.BUTTONS_OKCANCEL``: Display OK and CANCEL on dialog.
        - ``.BUTTONS_YESNO``: Display YES and NO on dialog.
        - ``.BUTTONS_YESNOCANCEL``: Display YES, NO, and CANCEL on dialog.
        - ``.BUTTON_CANCEL``: Return if CANCEL selected.
        - ``.BUTTON_NO``: Return if NO selected.
        - ``.BUTTON_OK``: Return if OK selected.
        - ``.BUTTON_YES``: Return if YES selected.
        - ``.DIGITS_4_5``: Set the front-panel display resolution to 4.5 digits.
        - ``.DIGITS_5_5``: Set the front-panel display resolution to 5.5 digits.
        - ``.DIGITS_6_5``: Set the front-panel display resolution to 6.5 digits.
        - ``.FORMAT_EXPONENT``: Use exponent format to display measurement readings on the
          front-panel display of
          the instrument.
        - ``.FORMAT_PREFIX``: Add a prefix to the units symbol, such as k, m, or u, to display
          measurement readings on the front-panel display of
          the instrument.
        - ``.NFORMAT_DECIMAL``: Allow decimal values.
        - ``.NFORMAT_EXPONENT``: Display numbers in exponent format.
        - ``.NFORMAT_INTEGER``: Allow integers (negative or positive) only.
        - ``.NFORMAT_PREFIX``: Display numbers with prefixes before the units symbol, such as n, m,
          or u.
        - ``.SCREEN_GRAPH``: Display the last selected graph screen tab.
        - ``.SCREEN_GRAPH_SWIPE``: Display graph swipe screen.
        - ``.SCREEN_HISTOGRAM``: Display Histogram.
        - ``.SCREEN_HOME``: Display Home screen.
        - ``.SCREEN_HOME_LARGE_READING``: Display Home screen with large readings.
        - ``.SCREEN_PROCESSING``: Open a screen that uses minimal CPU resources.
        - ``.SCREEN_READING_TABLE``: Display Reading Table screen.
        - ``.SCREEN_SETTINGS_SWIPE``: Display SETTINGS swipe screen.
        - ``.SCREEN_STATS_SWIPE``: Display STATISTICS swipe screen.
        - ``.SCREEN_USER_SWIPE``: Display USER swipe screen.
        - ``.SFORMAT_ANY``: Allow any characters.
        - ``.SFORMAT_BUFFER_NAME``: Allow both upper- and lower-case letters (no special
          characters).
        - ``.SFORMAT_UPPER``: Allow only upper-case letters.
        - ``.SFORMAT_UPPER_LOWER``: Allow both upper- and lower-case letters (no special
          characters).
        - ``.STATE_BLACKOUT``: Set display and all indicators off.
        - ``.STATE_LCD_100``: Set display to full brightness.
        - ``.STATE_LCD_25``: Set display to 25% brightness.
        - ``.STATE_LCD_50``: Set display to 50% brightness.
        - ``.STATE_LCD_75``: Set display to 75% brightness.
        - ``.STATE_LCD_OFF``: Set display to off.

    Properties and methods:
        - ``.activebuffer``: The ``display.activebuffer`` attribute.
        - ``.changescreen()``: The ``display.changescreen()`` function.
        - ``.clear()``: The ``display.clear()`` function.
        - ``.delete()``: The ``display.delete()`` function.
        - ``.input``: The ``display.input`` command tree.
        - ``.lightstate``: The ``display.lightstate`` attribute.
        - ``.prompt()``: The ``display.prompt()`` function.
        - ``.readingformat``: The ``display.readingformat`` attribute.
        - ``.settext()``: The ``display.settext()`` function.
        - ``.waitevent()``: The ``display.waitevent()`` function.
        - ``.watchchannels``: The ``display.watchchannels`` attribute.
    """

    BUTTONS_CANCEL = "display.BUTTONS_CANCEL"
    """str: Display CANCEL on dialog."""
    BUTTONS_NONE = "display.BUTTONS_NONE"
    """str: Display nothing on dialog."""
    BUTTONS_OK = "display.BUTTONS_OK"
    """str: Display OK on dialog."""
    BUTTONS_OKCANCEL = "display.BUTTONS_OKCANCEL"
    """str: Display OK and CANCEL on dialog."""
    BUTTONS_YESNO = "display.BUTTONS_YESNO"
    """str: Display YES and NO on dialog."""
    BUTTONS_YESNOCANCEL = "display.BUTTONS_YESNOCANCEL"
    """str: Display YES, NO, and CANCEL on dialog."""
    BUTTON_CANCEL = "display.BUTTON_CANCEL"
    """str: Return if CANCEL selected."""
    BUTTON_NO = "display.BUTTON_NO"
    """str: Return if NO selected."""
    BUTTON_OK = "display.BUTTON_OK"
    """str: Return if OK selected."""
    BUTTON_YES = "display.BUTTON_YES"
    """str: Return if YES selected."""
    DIGITS_4_5 = "display.DIGITS_4_5"
    """str: Set the front-panel display resolution to 4.5 digits."""
    DIGITS_5_5 = "display.DIGITS_5_5"
    """str: Set the front-panel display resolution to 5.5 digits."""
    DIGITS_6_5 = "display.DIGITS_6_5"
    """str: Set the front-panel display resolution to 6.5 digits."""
    FORMAT_EXPONENT = "display.FORMAT_EXPONENT"
    """str: Use exponent format to display measurement readings on the front-panel display of
the instrument."""
    FORMAT_PREFIX = "display.FORMAT_PREFIX"
    """str: Add a prefix to the units symbol, such as k, m, or u, to display measurement readings on the front-panel display of
the instrument."""  # noqa: E501
    NFORMAT_DECIMAL = "display.NFORMAT_DECIMAL"
    """str: Allow decimal values."""
    NFORMAT_EXPONENT = "display.NFORMAT_EXPONENT"
    """str: Display numbers in exponent format."""
    NFORMAT_INTEGER = "display.NFORMAT_INTEGER"
    """str: Allow integers (negative or positive) only."""
    NFORMAT_PREFIX = "display.NFORMAT_PREFIX"
    """str: Display numbers with prefixes before the units symbol, such as n, m, or u."""
    SCREEN_GRAPH = "display.SCREEN_GRAPH"
    """str: Display the last selected graph screen tab."""
    SCREEN_GRAPH_SWIPE = "display.SCREEN_GRAPH_SWIPE"
    """str: Display graph swipe screen."""
    SCREEN_HISTOGRAM = "display.SCREEN_HISTOGRAM"
    """str: Display Histogram."""
    SCREEN_HOME = "display.SCREEN_HOME"
    """str: Display Home screen."""
    SCREEN_HOME_LARGE_READING = "display.SCREEN_HOME_LARGE_READING"
    """str: Display Home screen with large readings."""
    SCREEN_PROCESSING = "display.SCREEN_PROCESSING"
    """str: Open a screen that uses minimal CPU resources."""
    SCREEN_READING_TABLE = "display.SCREEN_READING_TABLE"
    """str: Display Reading Table screen."""
    SCREEN_SETTINGS_SWIPE = "display.SCREEN_SETTINGS_SWIPE"
    """str: Display SETTINGS swipe screen."""
    SCREEN_STATS_SWIPE = "display.SCREEN_STATS_SWIPE"
    """str: Display STATISTICS swipe screen."""
    SCREEN_USER_SWIPE = "display.SCREEN_USER_SWIPE"
    """str: Display USER swipe screen."""
    SFORMAT_ANY = "display.SFORMAT_ANY"
    """str: Allow any characters."""
    SFORMAT_BUFFER_NAME = "display.SFORMAT_BUFFER_NAME"
    """str: Allow both upper- and lower-case letters (no special characters)."""
    SFORMAT_UPPER = "display.SFORMAT_UPPER"
    """str: Allow only upper-case letters."""
    SFORMAT_UPPER_LOWER = "display.SFORMAT_UPPER_LOWER"
    """str: Allow both upper- and lower-case letters (no special characters)."""
    STATE_BLACKOUT = "display.STATE_BLACKOUT"
    """str: Set display and all indicators off."""
    STATE_LCD_100 = "display.STATE_LCD_100"
    """str: Set display to full brightness."""
    STATE_LCD_25 = "display.STATE_LCD_25"
    """str: Set display to 25% brightness."""
    STATE_LCD_50 = "display.STATE_LCD_50"
    """str: Set display to 50% brightness."""
    STATE_LCD_75 = "display.STATE_LCD_75"
    """str: Set display to 75% brightness."""
    STATE_LCD_OFF = "display.STATE_LCD_OFF"
    """str: Set display to off."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "display") -> None:
        super().__init__(device, cmd_syntax)
        self._input = DisplayInput(device, f"{self._cmd_syntax}.input")

    @property
    def activebuffer(self) -> str:
        """Access the ``display.activebuffer`` attribute.

        Description:
            - This attribute determines which buffer is used for measurements that are displayed on
              the front panel.

        Usage:
            - Accessing this property will send the ``print(display.activebuffer)`` query.
            - Setting this property to a value will send the ``display.activebuffer = value``
              command.

        TSP Syntax:
            ```
            - display.activebuffer = value
            - print(display.activebuffer)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".activebuffer"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.activebuffer)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.activebuffer`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @activebuffer.setter
    def activebuffer(self, value: Union[str, float]) -> None:
        """Access the ``display.activebuffer`` attribute.

        Description:
            - This attribute determines which buffer is used for measurements that are displayed on
              the front panel.

        Usage:
            - Accessing this property will send the ``print(display.activebuffer)`` query.
            - Setting this property to a value will send the ``display.activebuffer = value``
              command.

        TSP Syntax:
            ```
            - display.activebuffer = value
            - print(display.activebuffer)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".activebuffer", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.activebuffer = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.activebuffer`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def input(self) -> DisplayInput:
        """Return the ``display.input`` command tree.

        Sub-properties and sub-methods:
            - ``.number()``: The ``display.input.number()`` function.
            - ``.option()``: The ``display.input.option()`` function.
            - ``.prompt()``: The ``display.input.prompt()`` function.
            - ``.string()``: The ``display.input.string()`` function.
        """
        return self._input

    @property
    def lightstate(self) -> str:
        """Access the ``display.lightstate`` attribute.

        Description:
            - This attribute sets the light output level of the front-panel display.

        Usage:
            - Accessing this property will send the ``print(display.lightstate)`` query.
            - Setting this property to a value will send the ``display.lightstate = value`` command.

        TSP Syntax:
            ```
            - display.lightstate = value
            - print(display.lightstate)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".lightstate"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.lightstate)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.lightstate`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @lightstate.setter
    def lightstate(self, value: Union[str, float]) -> None:
        """Access the ``display.lightstate`` attribute.

        Description:
            - This attribute sets the light output level of the front-panel display.

        Usage:
            - Accessing this property will send the ``print(display.lightstate)`` query.
            - Setting this property to a value will send the ``display.lightstate = value`` command.

        TSP Syntax:
            ```
            - display.lightstate = value
            - print(display.lightstate)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".lightstate", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.lightstate = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.lightstate`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def readingformat(self) -> str:
        """Access the ``display.readingformat`` attribute.

        Description:
            - This attribute determines the format that is used to display measurement readings on
              the front-panel display of the instrument.

        Usage:
            - Accessing this property will send the ``print(display.readingformat)`` query.
            - Setting this property to a value will send the ``display.readingformat = value``
              command.

        TSP Syntax:
            ```
            - display.readingformat = value
            - print(display.readingformat)
            ```

        Info:
            - ``format``, the use exponent format: display.FORMAT_EXPONENT
              Add a prefix to the units symbol, such as k, m, or µ: display.FORMAT_PREFIX.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".readingformat"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.readingformat)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.readingformat`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @readingformat.setter
    def readingformat(self, value: Union[str, float]) -> None:
        """Access the ``display.readingformat`` attribute.

        Description:
            - This attribute determines the format that is used to display measurement readings on
              the front-panel display of the instrument.

        Usage:
            - Accessing this property will send the ``print(display.readingformat)`` query.
            - Setting this property to a value will send the ``display.readingformat = value``
              command.

        TSP Syntax:
            ```
            - display.readingformat = value
            - print(display.readingformat)
            ```

        Info:
            - ``format``, the use exponent format: display.FORMAT_EXPONENT
              Add a prefix to the units symbol, such as k, m, or µ: display.FORMAT_PREFIX.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".readingformat", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.readingformat = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.readingformat`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def watchchannels(self) -> str:
        """Access the ``display.watchchannels`` attribute.

        Description:
            - This attribute determines which channels are set to be watch channels on the front
              panel.

        Usage:
            - Accessing this property will send the ``print(display.watchchannels)`` query.
            - Setting this property to a value will send the ``display.watchchannels = value``
              command.

        TSP Syntax:
            ```
            - display.watchchannels = value
            - print(display.watchchannels)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".watchchannels"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.watchchannels)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.watchchannels`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @watchchannels.setter
    def watchchannels(self, value: Union[str, float]) -> None:
        """Access the ``display.watchchannels`` attribute.

        Description:
            - This attribute determines which channels are set to be watch channels on the front
              panel.

        Usage:
            - Accessing this property will send the ``print(display.watchchannels)`` query.
            - Setting this property to a value will send the ``display.watchchannels = value``
              command.

        TSP Syntax:
            ```
            - display.watchchannels = value
            - print(display.watchchannels)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".watchchannels", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.watchchannels = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.watchchannels`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def changescreen(self, screen_name: str) -> None:
        """Run the ``display.changescreen()`` function.

        Description:
            - This function changes which front-panel screen is displayed.

        TSP Syntax:
            ```
            - display.changescreen()
            ```

        Args:
            screen_name: The screen to display.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.changescreen({screen_name})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.changescreen()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

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

    def delete(self, prompt_id: str) -> None:
        """Run the ``display.delete()`` function.

        Description:
            - This function allows you to remove a prompt on the front-panel display that was
              created with display.prompt().

        TSP Syntax:
            ```
            - display.delete()
            ```

        Args:
            prompt_id: The identifier defined by display.prompt().

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.delete({prompt_id})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.delete()`` function."  # noqa: E501
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

    def waitevent(self, timeout: Optional[float] = None) -> str:
        """Run the ``display.waitevent()`` function.

        Description:
            - This function causes the instrument to wait for a user to respond to a prompt that was
              created with a prompt command.

        TSP Syntax:
            ```
            - display.waitevent()
            ```

        Args:
            timeout (optional): The amount of time to wait before timing out; time is 0 to 300 s,
                where the default of 0 waits indefinitely.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (timeout,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.waitevent({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.waitevent()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
