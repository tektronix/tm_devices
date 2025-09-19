"""The recall commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - RECAll:SETUp {FACtory|<NR1>|<file path>}
    - RECAll:WAVEform <file path>,REF<x>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class RecallWaveform(SCPICmdWrite):
    r"""The ``RECAll:WAVEform`` command.

    Description:
        - This command (no query form) recalls a stored waveform to a reference location. This
          command is equivalent to selecting Recall from the File menu, and then pressing the
          Waveform button.

    Usage:
        - Using the ``.write(value)`` method will send the ``RECAll:WAVEform value`` command.

    SCPI Syntax:
        ```
        - RECAll:WAVEform <file path>,REF<x>
        ```

    Info:
        - ``<file path>`` specifies a location for a stored waveform file. <file path> is a quoted
          string that defines the file name and path. Input the file path using the form
          ``<drive>:<dir>``/<filename>.<drive> and one or more <dir>s are optional. If you do not
          specify them, the instrument will read the waveform from the default directory
          (C:UsersPublicTektronixTekScope\|Waveforms). <filename> stands for a file name of up to
          128 characters (use of wildcard characters in filenames is not supported). File name
          extensions are not required but are highly recommended.
        - ``REF<x>`` specifies a location in internal reference memory. Reference memory location
          values range from 1 through 4.
    """


class RecallSetup(SCPICmdWrite):
    """The ``RECAll:SETUp`` command.

    Description:
        - Restores the state of the oscilloscope from a copy of the settings stored in memory. The
          settings are stored using the ``*SAV`` command.

    Usage:
        - Using the ``.write(value)`` method will send the ``RECAll:SETUp value`` command.

    SCPI Syntax:
        ```
        - RECAll:SETUp {FACtory|<NR1>|<file path>}
        ```

    Info:
        - ``FACtory`` restores the factory setup.
        - ``<NR1>`` is a value in the range from 1 to 10, which specifies a saved setup storage
          location.
        - ``<file path>`` specifies a location for an oscilloscope setup file. <file path> is a
          quoted string that defines the file name and path. Input the file path using the form
          <drive>:/<dir>/<filename>.<extension> and one or <dir>s are optional. If you do not
          specify them, the oscilloscope will read the file from the default directory (see
          ``FILESYSTEM:CWD``). <filename> stands for a filename; the use of wildcard characters in
          filenames is not supported. Filename extensions are not required, but highly recommended.
    """


class Recall(SCPICmdRead):
    """The ``RECAll`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RECAll?`` query.
        - Using the ``.verify(value)`` method will send the ``RECAll?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.setup``: The ``RECAll:SETUp`` command.
        - ``.waveform``: The ``RECAll:WAVEform`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "RECAll") -> None:
        super().__init__(device, cmd_syntax)
        self._setup = RecallSetup(device, f"{self._cmd_syntax}:SETUp")
        self._waveform = RecallWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def setup(self) -> RecallSetup:
        """Return the ``RECAll:SETUp`` command.

        Description:
            - Restores the state of the oscilloscope from a copy of the settings stored in memory.
              The settings are stored using the ``*SAV`` command.

        Usage:
            - Using the ``.write(value)`` method will send the ``RECAll:SETUp value`` command.

        SCPI Syntax:
            ```
            - RECAll:SETUp {FACtory|<NR1>|<file path>}
            ```

        Info:
            - ``FACtory`` restores the factory setup.
            - ``<NR1>`` is a value in the range from 1 to 10, which specifies a saved setup storage
              location.
            - ``<file path>`` specifies a location for an oscilloscope setup file. <file path> is a
              quoted string that defines the file name and path. Input the file path using the form
              <drive>:/<dir>/<filename>.<extension> and one or <dir>s are optional. If you do not
              specify them, the oscilloscope will read the file from the default directory (see
              ``FILESYSTEM:CWD``). <filename> stands for a filename; the use of wildcard characters
              in filenames is not supported. Filename extensions are not required, but highly
              recommended.
        """
        return self._setup

    @property
    def waveform(self) -> RecallWaveform:
        r"""Return the ``RECAll:WAVEform`` command.

        Description:
            - This command (no query form) recalls a stored waveform to a reference location. This
              command is equivalent to selecting Recall from the File menu, and then pressing the
              Waveform button.

        Usage:
            - Using the ``.write(value)`` method will send the ``RECAll:WAVEform value`` command.

        SCPI Syntax:
            ```
            - RECAll:WAVEform <file path>,REF<x>
            ```

        Info:
            - ``<file path>`` specifies a location for a stored waveform file. <file path> is a
              quoted string that defines the file name and path. Input the file path using the form
              ``<drive>:<dir>``/<filename>.<drive> and one or more <dir>s are optional. If you do
              not specify them, the instrument will read the waveform from the default directory
              (C:UsersPublicTektronixTekScope\|Waveforms). <filename> stands for a file name of up
              to 128 characters (use of wildcard characters in filenames is not supported). File
              name extensions are not required but are highly recommended.
            - ``REF<x>`` specifies a location in internal reference memory. Reference memory
              location values range from 1 through 4.
        """
        return self._waveform
