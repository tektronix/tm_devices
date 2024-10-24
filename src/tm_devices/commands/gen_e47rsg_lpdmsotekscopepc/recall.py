"""The recall commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - RECAll:MASK <source file>,MASK<x>
    - RECAll:SESsion <file_path>
    - RECAll:SETUp {FACtory|<file_path>}
    - RECAll:WAVEform <source file>,<destination>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class RecallWaveform(SCPICmdWrite):
    """The ``RECAll:WAVEform`` command.

    Description:
        - This command recalls a stored waveform to a reference memory location.

    Usage:
        - Using the ``.write(value)`` method will send the ``RECAll:WAVEform value`` command.

    SCPI Syntax:
        ```
        - RECAll:WAVEform <source file>,<destination>
        ```

    Info:
        - ``<source file>`` is the source file. The file is expected to be located in a directory
          relative to the current working directory (specified by ``FILESYSTEM:CWD``) unless a
          complete path is specified.
        - ``<destination>`` is REF<x> which specifies a reference to create from the recalled
          waveform data file.
    """


class RecallSetup(SCPICmdWrite):
    """The ``RECAll:SETUp`` command.

    Description:
        - This command (no query form) returns stored or factory settings to the instrument from a
          copy of the settings stored in memory. This command performs the same function as
          selecting Recall from the File menu, and then choosing the Setup button.

    Usage:
        - Using the ``.write(value)`` method will send the ``RECAll:SETUp value`` command.

    SCPI Syntax:
        ```
        - RECAll:SETUp {FACtory|<file_path>}
        ```

    Info:
        - ``FACtory`` restores the factory setup. Performs the same operation as the ``:FACtory``
          command.
        - ``<file_path>`` specifies a location for an instrument setup file. <file path> is a quoted
          string that defines the file name and path. If a file name or path is specified, the file
          is expected to be located in a directory relative to the current working directory
          (specified by ``FILESYSTEM:CWD``) unless a complete path is specified.
    """


class RecallSession(SCPICmdWrite):
    """The ``RECAll:SESsion`` command.

    Description:
        - Restores the state of the instrument, including reference waveforms, from a saved session
          file.

    Usage:
        - Using the ``.write(value)`` method will send the ``RECAll:SESsion value`` command.

    SCPI Syntax:
        ```
        - RECAll:SESsion <file_path>
        ```

    Info:
        - ``<file_path>`` is the file path that specifies the location of the specified instrument
          session file.
    """


class RecallMask(SCPICmdWrite):
    """The ``RECAll:MASK`` command.

    Description:
        - This command recalls a saved mask definition from a Mask File. File suffixes can be xml or
          msk. If the specified mask test already exists the mask associated with that mask test
          will be replaced, otherwise a new mask test is created.

    Usage:
        - Using the ``.write(value)`` method will send the ``RECAll:MASK value`` command.

    SCPI Syntax:
        ```
        - RECAll:MASK <source file>,MASK<x>
        ```

    Info:
        - ``MASK<x>`` is the destination mask.
        - ``<source file>`` is the source file. The file is expected to be located in a directory
          relative to the current working directory (specified by ``FILESYSTEM:CWD``) unless a
          complete path is specified.
    """


class Recall(SCPICmdRead):
    """The ``RECAll`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RECAll?`` query.
        - Using the ``.verify(value)`` method will send the ``RECAll?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mask``: The ``RECAll:MASK`` command.
        - ``.session``: The ``RECAll:SESsion`` command.
        - ``.setup``: The ``RECAll:SETUp`` command.
        - ``.waveform``: The ``RECAll:WAVEform`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "RECAll") -> None:
        super().__init__(device, cmd_syntax)
        self._mask = RecallMask(device, f"{self._cmd_syntax}:MASK")
        self._session = RecallSession(device, f"{self._cmd_syntax}:SESsion")
        self._setup = RecallSetup(device, f"{self._cmd_syntax}:SETUp")
        self._waveform = RecallWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def mask(self) -> RecallMask:
        """Return the ``RECAll:MASK`` command.

        Description:
            - This command recalls a saved mask definition from a Mask File. File suffixes can be
              xml or msk. If the specified mask test already exists the mask associated with that
              mask test will be replaced, otherwise a new mask test is created.

        Usage:
            - Using the ``.write(value)`` method will send the ``RECAll:MASK value`` command.

        SCPI Syntax:
            ```
            - RECAll:MASK <source file>,MASK<x>
            ```

        Info:
            - ``MASK<x>`` is the destination mask.
            - ``<source file>`` is the source file. The file is expected to be located in a
              directory relative to the current working directory (specified by ``FILESYSTEM:CWD``)
              unless a complete path is specified.
        """
        return self._mask

    @property
    def session(self) -> RecallSession:
        """Return the ``RECAll:SESsion`` command.

        Description:
            - Restores the state of the instrument, including reference waveforms, from a saved
              session file.

        Usage:
            - Using the ``.write(value)`` method will send the ``RECAll:SESsion value`` command.

        SCPI Syntax:
            ```
            - RECAll:SESsion <file_path>
            ```

        Info:
            - ``<file_path>`` is the file path that specifies the location of the specified
              instrument session file.
        """
        return self._session

    @property
    def setup(self) -> RecallSetup:
        """Return the ``RECAll:SETUp`` command.

        Description:
            - This command (no query form) returns stored or factory settings to the instrument from
              a copy of the settings stored in memory. This command performs the same function as
              selecting Recall from the File menu, and then choosing the Setup button.

        Usage:
            - Using the ``.write(value)`` method will send the ``RECAll:SETUp value`` command.

        SCPI Syntax:
            ```
            - RECAll:SETUp {FACtory|<file_path>}
            ```

        Info:
            - ``FACtory`` restores the factory setup. Performs the same operation as the
              ``:FACtory`` command.
            - ``<file_path>`` specifies a location for an instrument setup file. <file path> is a
              quoted string that defines the file name and path. If a file name or path is
              specified, the file is expected to be located in a directory relative to the current
              working directory (specified by ``FILESYSTEM:CWD``) unless a complete path is
              specified.
        """
        return self._setup

    @property
    def waveform(self) -> RecallWaveform:
        """Return the ``RECAll:WAVEform`` command.

        Description:
            - This command recalls a stored waveform to a reference memory location.

        Usage:
            - Using the ``.write(value)`` method will send the ``RECAll:WAVEform value`` command.

        SCPI Syntax:
            ```
            - RECAll:WAVEform <source file>,<destination>
            ```

        Info:
            - ``<source file>`` is the source file. The file is expected to be located in a
              directory relative to the current working directory (specified by ``FILESYSTEM:CWD``)
              unless a complete path is specified.
            - ``<destination>`` is REF<x> which specifies a reference to create from the recalled
              waveform data file.
        """
        return self._waveform
