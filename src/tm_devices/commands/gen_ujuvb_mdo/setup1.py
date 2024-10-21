"""The setup1 commands module.

These commands are used in the following models:
MDO3

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SETUP1<x>:DATE?
    - SETUP1<x>:LABel <Qstring>
    - SETUP1<x>:TIMe?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, ValidatedDynamicNumberCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Setup1ItemTime(SCPICmdRead):
    """The ``SETUP1<x>:TIMe`` command.

    Description:
        - Returns the time when the oscilloscope setup was saved for the specified channel <x>,
          where x can be 1 through 10.

    Usage:
        - Using the ``.query()`` method will send the ``SETUP1<x>:TIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``SETUP1<x>:TIMe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SETUP1<x>:TIMe?
        ```
    """


class Setup1ItemLabel(SCPICmdWrite):
    """The ``SETUP1<x>:LABel`` command.

    Description:
        - This command specifies the setup label for the specified channel <x>, where x can be 1
          through 10.

    Usage:
        - Using the ``.write(value)`` method will send the ``SETUP1<x>:LABel value`` command.

    SCPI Syntax:
        ```
        - SETUP1<x>:LABel <Qstring>
        ```

    Info:
        - ``<Qstring>`` is an alphanumeric string of characters, enclosed in quotes, that defines
          the label text for SETUP<x>. The length of the string is limited to 30 characters.
    """


class Setup1ItemDate(SCPICmdRead):
    """The ``SETUP1<x>:DATE`` command.

    Description:
        - Returns the date when the oscilloscope setup was saved for the specified channel <x>,
          where x can be 1 through 10.

    Usage:
        - Using the ``.query()`` method will send the ``SETUP1<x>:DATE?`` query.
        - Using the ``.verify(value)`` method will send the ``SETUP1<x>:DATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SETUP1<x>:DATE?
        ```
    """


class Setup1Item(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``SETUP1<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SETUP1<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SETUP1<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.date``: The ``SETUP1<x>:DATE`` command.
        - ``.label``: The ``SETUP1<x>:LABel`` command.
        - ``.time``: The ``SETUP1<x>:TIMe`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SETUP1<x>") -> None:
        super().__init__(device, cmd_syntax)
        self._date = Setup1ItemDate(device, f"{self._cmd_syntax}:DATE")
        self._label = Setup1ItemLabel(device, f"{self._cmd_syntax}:LABel")
        self._time = Setup1ItemTime(device, f"{self._cmd_syntax}:TIMe")

    @property
    def date(self) -> Setup1ItemDate:
        """Return the ``SETUP1<x>:DATE`` command.

        Description:
            - Returns the date when the oscilloscope setup was saved for the specified channel <x>,
              where x can be 1 through 10.

        Usage:
            - Using the ``.query()`` method will send the ``SETUP1<x>:DATE?`` query.
            - Using the ``.verify(value)`` method will send the ``SETUP1<x>:DATE?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SETUP1<x>:DATE?
            ```
        """
        return self._date

    @property
    def label(self) -> Setup1ItemLabel:
        """Return the ``SETUP1<x>:LABel`` command.

        Description:
            - This command specifies the setup label for the specified channel <x>, where x can be 1
              through 10.

        Usage:
            - Using the ``.write(value)`` method will send the ``SETUP1<x>:LABel value`` command.

        SCPI Syntax:
            ```
            - SETUP1<x>:LABel <Qstring>
            ```

        Info:
            - ``<Qstring>`` is an alphanumeric string of characters, enclosed in quotes, that
              defines the label text for SETUP<x>. The length of the string is limited to 30
              characters.
        """
        return self._label

    @property
    def time(self) -> Setup1ItemTime:
        """Return the ``SETUP1<x>:TIMe`` command.

        Description:
            - Returns the time when the oscilloscope setup was saved for the specified channel <x>,
              where x can be 1 through 10.

        Usage:
            - Using the ``.query()`` method will send the ``SETUP1<x>:TIMe?`` query.
            - Using the ``.verify(value)`` method will send the ``SETUP1<x>:TIMe?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SETUP1<x>:TIMe?
            ```
        """
        return self._time
