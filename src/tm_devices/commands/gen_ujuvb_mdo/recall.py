"""The recall commands module.

These commands are used in the following models:
MDO3

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - RECAll:MASK <QString>
    - RECAll:SETUp {FACtory|<NR1>|<file path>}
    - RECAll:SETUp:DEMO3<x>
    - RECAll:WAVEform <Source>, <Destination>
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class RecallWaveform(SCPICmdWrite):
    """The ``RECAll:WAVEform`` command.

    Description:
        - This command (no query form) recalls a stored waveform to a reference memory location,
          and, for instruments with the arbitrary waveform feature, to arbitrary waveform edit
          memory (EMEM). Only the first waveform in a .CSV file is recalled for multiple waveform
          .CSV files. Recall of digital waveforms (D0 through D15) is not supported.

    Usage:
        - Using the ``.write(value)`` method will send the ``RECAll:WAVEform value`` command.

    SCPI Syntax:
        ```
        - RECAll:WAVEform <Source>, <Destination>
        ```

    Info:
        - ``<file path>``
        - ``ARB<x>`` - x has a minimum of 1 and a maximum of 4.
        - ``<QString>`` is a quoted string that specifies a location for an oscilloscope file. The
          file name and path should be input using the form <drive>:/<dir>/<filename>.<extension>.
        - ``REF<x>`` - Specifies a reference memory location to receive the saved ISF or CSV data.
          ARB1-ARB4 cannot be recalled to reference memory locations and attempting to do so on an
          instrument with the arbitrary waveform feature results in an error event. x has a minimum
          of 1 and a maximum of 4.
        - ``EMEM`` - For instruments with the arbitrary waveform feature, specifies arbitrary
          waveform edit memory (EMEM). If the source is a file, the file can be either an ISF or CSV
          file with the following restrictions.
    """


class RecallSetupDemo3Item(ValidatedDynamicNumberCmd, SCPICmdWriteNoArguments):
    """The ``RECAll:SETUp:DEMO3<x>`` command.

    Description:
        - This command recalls one of up to 22 built-in demonstration setups of oscilloscope
          functionality. <x> varies by model.

    Usage:
        - Using the ``.write()`` method will send the ``RECAll:SETUp:DEMO3<x>`` command.

    SCPI Syntax:
        ```
        - RECAll:SETUp:DEMO3<x>
        ```
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
        - ``.demo3``: The ``RECAll:SETUp:DEMO3<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._demo3: Dict[int, RecallSetupDemo3Item] = DefaultDictPassKeyToFactory(
            lambda x: RecallSetupDemo3Item(device, f"{self._cmd_syntax}:DEMO3{x}")
        )

    @property
    def demo3(self) -> Dict[int, RecallSetupDemo3Item]:
        """Return the ``RECAll:SETUp:DEMO3<x>`` command.

        Description:
            - This command recalls one of up to 22 built-in demonstration setups of oscilloscope
              functionality. <x> varies by model.

        Usage:
            - Using the ``.write()`` method will send the ``RECAll:SETUp:DEMO3<x>`` command.

        SCPI Syntax:
            ```
            - RECAll:SETUp:DEMO3<x>
            ```
        """
        return self._demo3


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
            - ``.demo3``: The ``RECAll:SETUp:DEMO3<x>`` command.
        """
        return self._setup

    @property
    def waveform(self) -> RecallWaveform:
        """Return the ``RECAll:WAVEform`` command.

        Description:
            - This command (no query form) recalls a stored waveform to a reference memory location,
              and, for instruments with the arbitrary waveform feature, to arbitrary waveform edit
              memory (EMEM). Only the first waveform in a .CSV file is recalled for multiple
              waveform .CSV files. Recall of digital waveforms (D0 through D15) is not supported.

        Usage:
            - Using the ``.write(value)`` method will send the ``RECAll:WAVEform value`` command.

        SCPI Syntax:
            ```
            - RECAll:WAVEform <Source>, <Destination>
            ```

        Info:
            - ``<file path>``
            - ``ARB<x>`` - x has a minimum of 1 and a maximum of 4.
            - ``<QString>`` is a quoted string that specifies a location for an oscilloscope file.
              The file name and path should be input using the form
              <drive>:/<dir>/<filename>.<extension>.
            - ``REF<x>`` - Specifies a reference memory location to receive the saved ISF or CSV
              data. ARB1-ARB4 cannot be recalled to reference memory locations and attempting to do
              so on an instrument with the arbitrary waveform feature results in an error event. x
              has a minimum of 1 and a maximum of 4.
            - ``EMEM`` - For instruments with the arbitrary waveform feature, specifies arbitrary
              waveform edit memory (EMEM). If the source is a file, the file can be either an ISF or
              CSV file with the following restrictions.
        """
        return self._waveform
