"""The errlog commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2K, MSO2KB, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ERRlog {CLEar}
    - ERRlog:FIRst?
    - ERRlog:NEXt?
    - ERRlog:NUMENTries?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ErrlogNumentries(SCPICmdRead):
    """The ``ERRlog:NUMENTries`` command.

    Description:
        - Returns the specified number of entries in the error log.

    Usage:
        - Using the ``.query()`` method will send the ``ERRlog:NUMENTries?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRlog:NUMENTries?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRlog:NUMENTries?
        ```
    """


class ErrlogNext(SCPICmdRead):
    """The ``ERRlog:NEXt`` command.

    Description:
        - Returns the next entry in the error log (auto-incrementing).

    Usage:
        - Using the ``.query()`` method will send the ``ERRlog:NEXt?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRlog:NEXt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRlog:NEXt?
        ```
    """


class ErrlogFirst(SCPICmdRead):
    """The ``ERRlog:FIRst`` command.

    Description:
        - Returns the first entry in the Error Log.

    Usage:
        - Using the ``.query()`` method will send the ``ERRlog:FIRst?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRlog:FIRst?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRlog:FIRst?
        ```
    """


class Errlog(SCPICmdWrite, SCPICmdRead):
    """The ``ERRlog`` command.

    Description:
        - Clears the oscilloscope error log.

    Usage:
        - Using the ``.write(value)`` method will send the ``ERRlog value`` command.

    SCPI Syntax:
        ```
        - ERRlog {CLEar}
        ```

    Info:
        - ``CLear``

    Properties:
        - ``.first``: The ``ERRlog:FIRst`` command.
        - ``.next``: The ``ERRlog:NEXt`` command.
        - ``.numentries``: The ``ERRlog:NUMENTries`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "ERRlog") -> None:
        super().__init__(device, cmd_syntax)
        self._first = ErrlogFirst(device, f"{self._cmd_syntax}:FIRst")
        self._next = ErrlogNext(device, f"{self._cmd_syntax}:NEXt")
        self._numentries = ErrlogNumentries(device, f"{self._cmd_syntax}:NUMENTries")

    @property
    def first(self) -> ErrlogFirst:
        """Return the ``ERRlog:FIRst`` command.

        Description:
            - Returns the first entry in the Error Log.

        Usage:
            - Using the ``.query()`` method will send the ``ERRlog:FIRst?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRlog:FIRst?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRlog:FIRst?
            ```
        """
        return self._first

    @property
    def next(self) -> ErrlogNext:
        """Return the ``ERRlog:NEXt`` command.

        Description:
            - Returns the next entry in the error log (auto-incrementing).

        Usage:
            - Using the ``.query()`` method will send the ``ERRlog:NEXt?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRlog:NEXt?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRlog:NEXt?
            ```
        """
        return self._next

    @property
    def numentries(self) -> ErrlogNumentries:
        """Return the ``ERRlog:NUMENTries`` command.

        Description:
            - Returns the specified number of entries in the error log.

        Usage:
            - Using the ``.query()`` method will send the ``ERRlog:NUMENTries?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRlog:NUMENTries?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRlog:NUMENTries?
            ```
        """
        return self._numentries
