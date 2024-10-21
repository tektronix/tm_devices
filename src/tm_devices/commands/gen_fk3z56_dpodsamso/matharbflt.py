"""The matharbflt commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MATHArbflt<x>:FILepath <QString>
    - MATHArbflt<x>:FILepath?
    - MATHArbflt<x>:READFile FORCe
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, ValidatedDynamicNumberCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MatharbfltItemReadfile(SCPICmdWrite):
    """The ``MATHArbflt<x>:READFile`` command.

    Description:
        - This command forces a reread of the filter file for each arbitrary filter in use. The <x>
          specifies the filter and can be 1 to 8.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATHArbflt<x>:READFile value`` command.

    SCPI Syntax:
        ```
        - MATHArbflt<x>:READFile FORCe
        ```

    Info:
        - ``FORCe`` forces a reread of the filter file.
    """


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
        - ``.readfile``: The ``MATHArbflt<x>:READFile`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "MATHArbflt<x>"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._filepath = MatharbfltItemFilepath(device, f"{self._cmd_syntax}:FILepath")
        self._readfile = MatharbfltItemReadfile(device, f"{self._cmd_syntax}:READFile")

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

    @property
    def readfile(self) -> MatharbfltItemReadfile:
        """Return the ``MATHArbflt<x>:READFile`` command.

        Description:
            - This command forces a reread of the filter file for each arbitrary filter in use. The
              <x> specifies the filter and can be 1 to 8.

        Usage:
            - Using the ``.write(value)`` method will send the ``MATHArbflt<x>:READFile value``
              command.

        SCPI Syntax:
            ```
            - MATHArbflt<x>:READFile FORCe
            ```

        Info:
            - ``FORCe`` forces a reread of the filter file.
        """
        return self._readfile
