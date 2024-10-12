"""The recall commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - RECAll:MASK <QString>
    - RECAll:SETUp {FACtory|<NR1>|<file path>}
    - RECAll:SETUp:DESKew {LOCK|UNLOCK}
    - RECAll:SETUp:DESKew?
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


class RecallSetupDeskew(SCPICmdWrite, SCPICmdRead):
    """The ``RECAll:SETUp:DESKew`` command.

    Description:
        - This command sets or queries the deskew values that are affected by a default setup or a
          recalled setup.

    Usage:
        - Using the ``.query()`` method will send the ``RECAll:SETUp:DESKew?`` query.
        - Using the ``.verify(value)`` method will send the ``RECAll:SETUp:DESKew?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RECAll:SETUp:DESKew value`` command.

    SCPI Syntax:
        ```
        - RECAll:SETUp:DESKew {LOCK|UNLOCK}
        - RECAll:SETUp:DESKew?
        ```

    Info:
        - ``LOCK`` a default or a recall setup will not change the deskew settings when this option
          is selected.
        - ``UNLOCK`` a default setup will reset the deskew settings to factory values and a recall
          setup will apply the setup deskew values to the recalled oscilloscope state.
    """


class RecallSetup(SCPICmdWrite, SCPICmdRead):
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

    Properties:
        - ``.deskew``: The ``RECAll:SETUp:DESKew`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._deskew = RecallSetupDeskew(device, f"{self._cmd_syntax}:DESKew")

    @property
    def deskew(self) -> RecallSetupDeskew:
        """Return the ``RECAll:SETUp:DESKew`` command.

        Description:
            - This command sets or queries the deskew values that are affected by a default setup or
              a recalled setup.

        Usage:
            - Using the ``.query()`` method will send the ``RECAll:SETUp:DESKew?`` query.
            - Using the ``.verify(value)`` method will send the ``RECAll:SETUp:DESKew?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RECAll:SETUp:DESKew value``
              command.

        SCPI Syntax:
            ```
            - RECAll:SETUp:DESKew {LOCK|UNLOCK}
            - RECAll:SETUp:DESKew?
            ```

        Info:
            - ``LOCK`` a default or a recall setup will not change the deskew settings when this
              option is selected.
            - ``UNLOCK`` a default setup will reset the deskew settings to factory values and a
              recall setup will apply the setup deskew values to the recalled oscilloscope state.
        """
        return self._deskew


class RecallMask(SCPICmdWrite):
    """The ``RECAll:MASK`` command.

    Description:
        - This command recalls the mask from a specified file that was saved to the current working
          directory using the ``SAVE:MASK`` command. A series of examples showing how to use mask
          commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.write(value)`` method will send the ``RECAll:MASK value`` command.

    SCPI Syntax:
        ```
        - RECAll:MASK <QString>
        ```

    Info:
        - ``QString`` is a quoted string that is the name of the mask definition being recalled from
          the current working directory.
    """

    _WRAP_ARG_WITH_QUOTES = True


class Recall(SCPICmdRead):
    """The ``RECAll`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RECAll?`` query.
        - Using the ``.verify(value)`` method will send the ``RECAll?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mask``: The ``RECAll:MASK`` command.
        - ``.setup``: The ``RECAll:SETUp`` command.
        - ``.waveform``: The ``RECAll:WAVEform`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "RECAll") -> None:
        super().__init__(device, cmd_syntax)
        self._mask = RecallMask(device, f"{self._cmd_syntax}:MASK")
        self._setup = RecallSetup(device, f"{self._cmd_syntax}:SETUp")
        self._waveform = RecallWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def mask(self) -> RecallMask:
        """Return the ``RECAll:MASK`` command.

        Description:
            - This command recalls the mask from a specified file that was saved to the current
              working directory using the ``SAVE:MASK`` command. A series of examples showing how to
              use mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.write(value)`` method will send the ``RECAll:MASK value`` command.

        SCPI Syntax:
            ```
            - RECAll:MASK <QString>
            ```

        Info:
            - ``QString`` is a quoted string that is the name of the mask definition being recalled
              from the current working directory.
        """
        return self._mask

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

        Sub-properties:
            - ``.deskew``: The ``RECAll:SETUp:DESKew`` command.
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
