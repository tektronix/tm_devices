"""The setup_1 commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2K, MSO2KB, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SETUP<x>:DATE?
    - SETUP<x>:LABEL <Qstring>
    - SETUP<x>:TIME?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, ValidatedDynamicNumberCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SetupItemTime(SCPICmdRead):
    """The ``SETUP<x>:TIME`` command.

    Description:
        - Returns the time when the oscilloscope setup was saved for the specified channel <x>,
          where x can be 1 through 10.

    Usage:
        - Using the ``.query()`` method will send the ``SETUP<x>:TIME?`` query.
        - Using the ``.verify(value)`` method will send the ``SETUP<x>:TIME?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SETUP<x>:TIME?
        ```
    """


class SetupItemLabel(SCPICmdWrite):
    """The ``SETUP<x>:LABEL`` command.

    Description:
        - This command specifies the setup label for the specified channel <x>, where x can be 1
          through 10.

    Usage:
        - Using the ``.write(value)`` method will send the ``SETUP<x>:LABEL value`` command.

    SCPI Syntax:
        ```
        - SETUP<x>:LABEL <Qstring>
        ```

    Info:
        - ``<Qstring>`` is an alphanumeric string of characters, enclosed in quotes, that defines
          the label text for SETUP<x>. The length of the string is limited to 30 characters.
    """


class SetupItemDate(SCPICmdRead):
    """The ``SETUP<x>:DATE`` command.

    Description:
        - Returns the date when the oscilloscope setup was saved for the specified channel <x>,
          where x can be 1 through 10.

    Usage:
        - Using the ``.query()`` method will send the ``SETUP<x>:DATE?`` query.
        - Using the ``.verify(value)`` method will send the ``SETUP<x>:DATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SETUP<x>:DATE?
        ```
    """


class SetupItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``SETUP<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SETUP<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SETUP<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.date``: The ``SETUP<x>:DATE`` command.
        - ``.label``: The ``SETUP<x>:LABEL`` command.
        - ``.time``: The ``SETUP<x>:TIME`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SETUP<x>") -> None:
        super().__init__(device, cmd_syntax)
        self._date = SetupItemDate(device, f"{self._cmd_syntax}:DATE")
        self._label = SetupItemLabel(device, f"{self._cmd_syntax}:LABEL")
        self._time = SetupItemTime(device, f"{self._cmd_syntax}:TIME")

    @property
    def date(self) -> SetupItemDate:
        """Return the ``SETUP<x>:DATE`` command.

        Description:
            - Returns the date when the oscilloscope setup was saved for the specified channel <x>,
              where x can be 1 through 10.

        Usage:
            - Using the ``.query()`` method will send the ``SETUP<x>:DATE?`` query.
            - Using the ``.verify(value)`` method will send the ``SETUP<x>:DATE?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SETUP<x>:DATE?
            ```
        """
        return self._date

    @property
    def label(self) -> SetupItemLabel:
        """Return the ``SETUP<x>:LABEL`` command.

        Description:
            - This command specifies the setup label for the specified channel <x>, where x can be 1
              through 10.

        Usage:
            - Using the ``.write(value)`` method will send the ``SETUP<x>:LABEL value`` command.

        SCPI Syntax:
            ```
            - SETUP<x>:LABEL <Qstring>
            ```

        Info:
            - ``<Qstring>`` is an alphanumeric string of characters, enclosed in quotes, that
              defines the label text for SETUP<x>. The length of the string is limited to 30
              characters.
        """
        return self._label

    @property
    def time(self) -> SetupItemTime:
        """Return the ``SETUP<x>:TIME`` command.

        Description:
            - Returns the time when the oscilloscope setup was saved for the specified channel <x>,
              where x can be 1 through 10.

        Usage:
            - Using the ``.query()`` method will send the ``SETUP<x>:TIME?`` query.
            - Using the ``.verify(value)`` method will send the ``SETUP<x>:TIME?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SETUP<x>:TIME?
            ```
        """
        return self._time
