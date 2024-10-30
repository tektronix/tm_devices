"""The matharbflt commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MATHArbflt<x>:FILepath <QString>
    - MATHArbflt<x>:FILepath?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, ValidatedDynamicNumberCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MatharbfltItemFilepath(SCPICmdWrite, SCPICmdRead):
    """The ``MATHArbflt<x>:FILepath`` command.

    Description:
        - This command or query sets the file path for a file of filter coefficients for the
          specified arbitrary filter. Setting a path will read that file and load the filter for
          ARBFLT<x>. Access these filters using a Math with an expression of the form 'ARBFlt<x>()'.

    Usage:
        - Using the ``.query()`` method will send the ``MATHArbflt<x>:FILepath?`` query.
        - Using the ``.verify(value)`` method will send the ``MATHArbflt<x>:FILepath?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATHArbflt<x>:FILepath value`` command.

    SCPI Syntax:
        ```
        - MATHArbflt<x>:FILepath <QString>
        - MATHArbflt<x>:FILepath?
        ```

    Info:
        - ``<QString>`` specifies the path to the file of filter coefficients.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MatharbfltItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MATHArbflt<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATHArbflt<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MATHArbflt<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.filepath``: The ``MATHArbflt<x>:FILepath`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "MATHArbflt<x>"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._filepath = MatharbfltItemFilepath(device, f"{self._cmd_syntax}:FILepath")

    @property
    def filepath(self) -> MatharbfltItemFilepath:
        """Return the ``MATHArbflt<x>:FILepath`` command.

        Description:
            - This command or query sets the file path for a file of filter coefficients for the
              specified arbitrary filter. Setting a path will read that file and load the filter for
              ARBFLT<x>. Access these filters using a Math with an expression of the form
              'ARBFlt<x>()'.

        Usage:
            - Using the ``.query()`` method will send the ``MATHArbflt<x>:FILepath?`` query.
            - Using the ``.verify(value)`` method will send the ``MATHArbflt<x>:FILepath?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATHArbflt<x>:FILepath value``
              command.

        SCPI Syntax:
            ```
            - MATHArbflt<x>:FILepath <QString>
            - MATHArbflt<x>:FILepath?
            ```

        Info:
            - ``<QString>`` specifies the path to the file of filter coefficients.
        """
        return self._filepath
