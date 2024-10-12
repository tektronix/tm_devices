"""The limit commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - LIMit:BEEP {ON|OFF|<NR1>}
    - LIMit:BEEP?
    - LIMit:COMpare {RESet}
    - LIMit:COMpare:CH<x> {NONe|REF<x>}
    - LIMit:COMpare:CH<x>?
    - LIMit:COMpare:MATH<x> {NONe|REF<x>}
    - LIMit:COMpare:MATH<x>?
    - LIMit:COMpare:REF<x> {NONe|REF<x>}
    - LIMit:COMpare:REF<x>?
    - LIMit:EMail {ON|OFF|<NR1>}
    - LIMit:EMail?
    - LIMit:HARDCopy {ON|OFF|<NR1>}
    - LIMit:HARDCopy?
    - LIMit:HIGHLIGHTHits {ON|OFF|<NR1>}
    - LIMit:HIGHLIGHTHits:RESet
    - LIMit:HIGHLIGHTHits?
    - LIMit:LOCk {ON|OFF|<NR1>}
    - LIMit:LOCk?
    - LIMit:LOG {ON|OFF|<NR1>}
    - LIMit:LOG?
    - LIMit:SAVEWFM {ON|OFF|<NR1>}
    - LIMit:SAVEWFM:FILEName <QString>
    - LIMit:SAVEWFM:FILEName?
    - LIMit:SAVEWFM?
    - LIMit:SRQ {ON|OFF|<NR1>}
    - LIMit:SRQ?
    - LIMit:STATE {ON|OFF|<NR1>}
    - LIMit:STATE?
    - LIMit:STATus?
    - LIMit:STOPOnviolation {ON|OFF|<NR1>}
    - LIMit:STOPOnviolation?
    - LIMit:TEMPlate:DESTination {REF<x>}
    - LIMit:TEMPlate:DESTination?
    - LIMit:TEMPlate:SOUrce {CH<x>|MATH<x>|REF<x>}
    - LIMit:TEMPlate:SOUrce?
    - LIMit:TEMPlate:STORe <wfm>,{REF<x>|<file path>}
    - LIMit:TEMPlate:TOLerance:HORizontal <NR3>
    - LIMit:TEMPlate:TOLerance:HORizontal?
    - LIMit:TEMPlate:TOLerance:VERTical <NR3>
    - LIMit:TEMPlate:TOLerance:VERTical?
    - LIMit?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedChannel,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class LimitTemplateToleranceVertical(SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:TEMPlate:TOLerance:VERTical`` command.

    Description:
        - This command sets or queries the amount in units of vertical divisions, by which the
          source waveform is varied vertically when creating the destination waveform.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:TEMPlate:TOLerance:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:TEMPlate:TOLerance:VERTical?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``LIMit:TEMPlate:TOLerance:VERTical value`` command.

    SCPI Syntax:
        ```
        - LIMit:TEMPlate:TOLerance:VERTical <NR3>
        - LIMit:TEMPlate:TOLerance:VERTical?
        ```

    Info:
        - ``<NR3>`` is the amount in vertical divisions, by which the current source waveform is
          allowed to deviate from the template waveform without exceeding the limits set in the
          limit test. The range is 0 to 5 divisions.
    """


class LimitTemplateToleranceHorizontal(SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:TEMPlate:TOLerance:HORizontal`` command.

    Description:
        - This command sets or queries the amount in units of horizontal divisions, by which the
          source waveform is varied horizontally when creating the destination waveform.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:TEMPlate:TOLerance:HORizontal?``
          query.
        - Using the ``.verify(value)`` method will send the ``LIMit:TEMPlate:TOLerance:HORizontal?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``LIMit:TEMPlate:TOLerance:HORizontal value`` command.

    SCPI Syntax:
        ```
        - LIMit:TEMPlate:TOLerance:HORizontal <NR3>
        - LIMit:TEMPlate:TOLerance:HORizontal?
        ```

    Info:
        - ``<NR3>`` is the amount in horizontal divisions, by which the current source waveform is
          allowed to deviate from the template waveform without exceeding the limits set in the
          limit test. The range is 0 to 5 divisions.
    """


class LimitTemplateTolerance(SCPICmdRead):
    """The ``LIMit:TEMPlate:TOLerance`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:TEMPlate:TOLerance?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:TEMPlate:TOLerance?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.horizontal``: The ``LIMit:TEMPlate:TOLerance:HORizontal`` command.
        - ``.vertical``: The ``LIMit:TEMPlate:TOLerance:VERTical`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._horizontal = LimitTemplateToleranceHorizontal(
            device, f"{self._cmd_syntax}:HORizontal"
        )
        self._vertical = LimitTemplateToleranceVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def horizontal(self) -> LimitTemplateToleranceHorizontal:
        """Return the ``LIMit:TEMPlate:TOLerance:HORizontal`` command.

        Description:
            - This command sets or queries the amount in units of horizontal divisions, by which the
              source waveform is varied horizontally when creating the destination waveform.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:TEMPlate:TOLerance:HORizontal?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``LIMit:TEMPlate:TOLerance:HORizontal?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``LIMit:TEMPlate:TOLerance:HORizontal value`` command.

        SCPI Syntax:
            ```
            - LIMit:TEMPlate:TOLerance:HORizontal <NR3>
            - LIMit:TEMPlate:TOLerance:HORizontal?
            ```

        Info:
            - ``<NR3>`` is the amount in horizontal divisions, by which the current source waveform
              is allowed to deviate from the template waveform without exceeding the limits set in
              the limit test. The range is 0 to 5 divisions.
        """
        return self._horizontal

    @property
    def vertical(self) -> LimitTemplateToleranceVertical:
        """Return the ``LIMit:TEMPlate:TOLerance:VERTical`` command.

        Description:
            - This command sets or queries the amount in units of vertical divisions, by which the
              source waveform is varied vertically when creating the destination waveform.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:TEMPlate:TOLerance:VERTical?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``LIMit:TEMPlate:TOLerance:VERTical?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``LIMit:TEMPlate:TOLerance:VERTical value`` command.

        SCPI Syntax:
            ```
            - LIMit:TEMPlate:TOLerance:VERTical <NR3>
            - LIMit:TEMPlate:TOLerance:VERTical?
            ```

        Info:
            - ``<NR3>`` is the amount in vertical divisions, by which the current source waveform is
              allowed to deviate from the template waveform without exceeding the limits set in the
              limit test. The range is 0 to 5 divisions.
        """
        return self._vertical


class LimitTemplateStore(SCPICmdWrite):
    """The ``LIMit:TEMPlate:STORe`` command.

    Description:
        - This command (no query form) saves the specified source waveform to the specified
          reference or file name.

    Usage:
        - Using the ``.write(value)`` method will send the ``LIMit:TEMPlate:STORe value`` command.

    SCPI Syntax:
        ```
        - LIMit:TEMPlate:STORe <wfm>,{REF<x>|<file path>}
        ```

    Info:
        - ``<wfm>`` specifies the waveform that will be saved as the template. The source of the
          waveform can be CH<x> (where x is 1 through 4 for four channel instruments), MATH<x>, or
          Ref<x> (where x is 1 through 4).
        - ``REF<x>`` specifies a reference location in which the template waveform will be stored.
          The reference waveform specified by x, which can be 1 through 4.
        - ``<file path>`` specifies a file path where the template waveform will be stored. This
          argument is a quoted string.
    """


class LimitTemplateSource(SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:TEMPlate:SOUrce`` command.

    Description:
        - This command sets or queries the channel, math waveform, or reference waveform that the
          ``LIMIT:TEMPLATE:STORE`` command will use.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:TEMPlate:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:TEMPlate:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LIMit:TEMPlate:SOUrce value`` command.

    SCPI Syntax:
        ```
        - LIMit:TEMPlate:SOUrce {CH<x>|MATH<x>|REF<x>}
        - LIMit:TEMPlate:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies the channel used by the ``LIMIT:TEMPLATE:STORE`` command. x has a
          minimum of 1 and a maximum of 4.
        - ``MATH<x>`` specifies the math waveform used by the ``LIMIT:TEMPLATE:STORE`` command. x
          has a minimum of 1 and a maximum of 4.
        - ``REF<x>`` specifies the reference waveform used by the ``LIMIT:TEMPLATE:STORE`` command.
          x has a minimum of 1 and a maximum of 4.
    """


class LimitTemplateDestination(SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:TEMPlate:DESTination`` command.

    Description:
        - This command sets or queries the destination reference waveform that the
          ``LIMIT:TEMPLATE:STORE`` command will use.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:TEMPlate:DESTination?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:TEMPlate:DESTination?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LIMit:TEMPlate:DESTination value``
          command.

    SCPI Syntax:
        ```
        - LIMit:TEMPlate:DESTination {REF<x>}
        - LIMit:TEMPlate:DESTination?
        ```

    Info:
        - ``REF<x>`` specifies the reference waveform destination in which the template waveform is
          to be stored.
    """


class LimitTemplate(SCPICmdRead):
    """The ``LIMit:TEMPlate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:TEMPlate?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:TEMPlate?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.destination``: The ``LIMit:TEMPlate:DESTination`` command.
        - ``.source``: The ``LIMit:TEMPlate:SOUrce`` command.
        - ``.store``: The ``LIMit:TEMPlate:STORe`` command.
        - ``.tolerance``: The ``LIMit:TEMPlate:TOLerance`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._destination = LimitTemplateDestination(device, f"{self._cmd_syntax}:DESTination")
        self._source = LimitTemplateSource(device, f"{self._cmd_syntax}:SOUrce")
        self._store = LimitTemplateStore(device, f"{self._cmd_syntax}:STORe")
        self._tolerance = LimitTemplateTolerance(device, f"{self._cmd_syntax}:TOLerance")

    @property
    def destination(self) -> LimitTemplateDestination:
        """Return the ``LIMit:TEMPlate:DESTination`` command.

        Description:
            - This command sets or queries the destination reference waveform that the
              ``LIMIT:TEMPLATE:STORE`` command will use.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:TEMPlate:DESTination?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:TEMPlate:DESTination?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LIMit:TEMPlate:DESTination value``
              command.

        SCPI Syntax:
            ```
            - LIMit:TEMPlate:DESTination {REF<x>}
            - LIMit:TEMPlate:DESTination?
            ```

        Info:
            - ``REF<x>`` specifies the reference waveform destination in which the template waveform
              is to be stored.
        """
        return self._destination

    @property
    def source(self) -> LimitTemplateSource:
        """Return the ``LIMit:TEMPlate:SOUrce`` command.

        Description:
            - This command sets or queries the channel, math waveform, or reference waveform that
              the ``LIMIT:TEMPLATE:STORE`` command will use.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:TEMPlate:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:TEMPlate:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LIMit:TEMPlate:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - LIMit:TEMPlate:SOUrce {CH<x>|MATH<x>|REF<x>}
            - LIMit:TEMPlate:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies the channel used by the ``LIMIT:TEMPLATE:STORE`` command. x has a
              minimum of 1 and a maximum of 4.
            - ``MATH<x>`` specifies the math waveform used by the ``LIMIT:TEMPLATE:STORE`` command.
              x has a minimum of 1 and a maximum of 4.
            - ``REF<x>`` specifies the reference waveform used by the ``LIMIT:TEMPLATE:STORE``
              command. x has a minimum of 1 and a maximum of 4.
        """
        return self._source

    @property
    def store(self) -> LimitTemplateStore:
        """Return the ``LIMit:TEMPlate:STORe`` command.

        Description:
            - This command (no query form) saves the specified source waveform to the specified
              reference or file name.

        Usage:
            - Using the ``.write(value)`` method will send the ``LIMit:TEMPlate:STORe value``
              command.

        SCPI Syntax:
            ```
            - LIMit:TEMPlate:STORe <wfm>,{REF<x>|<file path>}
            ```

        Info:
            - ``<wfm>`` specifies the waveform that will be saved as the template. The source of the
              waveform can be CH<x> (where x is 1 through 4 for four channel instruments), MATH<x>,
              or Ref<x> (where x is 1 through 4).
            - ``REF<x>`` specifies a reference location in which the template waveform will be
              stored. The reference waveform specified by x, which can be 1 through 4.
            - ``<file path>`` specifies a file path where the template waveform will be stored. This
              argument is a quoted string.
        """
        return self._store

    @property
    def tolerance(self) -> LimitTemplateTolerance:
        """Return the ``LIMit:TEMPlate:TOLerance`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:TEMPlate:TOLerance?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:TEMPlate:TOLerance?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.horizontal``: The ``LIMit:TEMPlate:TOLerance:HORizontal`` command.
            - ``.vertical``: The ``LIMit:TEMPlate:TOLerance:VERTical`` command.
        """
        return self._tolerance


class LimitStoponviolation(SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:STOPOnviolation`` command.

    Description:
        - This command sets or queries whether acquisitions are stopped when the waveform data
          exceeds the test limits.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:STOPOnviolation?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:STOPOnviolation?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LIMit:STOPOnviolation value`` command.

    SCPI Syntax:
        ```
        - LIMit:STOPOnviolation {ON|OFF|<NR1>}
        - LIMit:STOPOnviolation?
        ```

    Info:
        - ``<NR1>`` = 0 disables the stop on violation feature; any other value enables the stop on
          violation feature so that when the waveform data exceeds the limits set by the limit test,
          acquisitions are stopped. For queries, a 0 is returned if the stop on violation feature is
          off; a 1 is returned if the stop on violation feature is on.
        - ``OFF`` disables the stop on violation feature.
        - ``ON`` enables the stop on violation feature so that when the waveform data exceeds the
          limits set by the limit test, acquisitions are stopped.
    """


class LimitStatus(SCPICmdRead):
    """The ``LIMit:STATus`` command.

    Description:
        - This command queries the state of limit testing.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:STATus?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - LIMit:STATus?
        ```
    """


class LimitState(SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:STATE`` command.

    Description:
        - This command sets limit testing on or off or queries whether limit testing is in effect.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LIMit:STATE value`` command.

    SCPI Syntax:
        ```
        - LIMit:STATE {ON|OFF|<NR1>}
        - LIMit:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 disables the limit testing operation; any other value turns on limit testing
          of waveforms. For queries, a 0 is returned if limit testing is off; a 1 is returned if the
          limit testing is on.
        - ``OFF`` disables limit testing.
        - ``ON`` turns on limit testing of waveforms.
    """


class LimitSrq(SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:SRQ`` command.

    Description:
        - This command sets or queries whether a Service Request Interrupt (SRQ) is generated when
          the waveform data falls outside of the test limits.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:SRQ?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:SRQ?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LIMit:SRQ value`` command.

    SCPI Syntax:
        ```
        - LIMit:SRQ {ON|OFF|<NR1>}
        - LIMit:SRQ?
        ```

    Info:
        - ``<NR1>`` = 0 disables sending an SRQ when the waveform data falls outside of the limits
          set by the limit test; any other value enables generation of an SRQ when the waveform data
          falls outside of the limits set by the limit test. For queries, a 0 is returned if SRQ is
          off; a 1 is returned if the SRQ is on.
        - ``OFF`` disables generation of an SRQ when the waveform data falls outside of the limits
          set by the limit test.
        - ``ON`` enables generation of an SRQ when the waveform data falls outside of the limits set
          by the limit test. If an SRQ is generated, the instrument sends the status event 'Limit
          testing failed.'.
    """


class LimitSavewfmFilename(SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:SAVEWFM:FILEName`` command.

    Description:
        - This command sets or queries the path where waveforms or log files will be saved when the
          waveform data exceeds the limits set by the limit test.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:SAVEWFM:FILEName?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:SAVEWFM:FILEName?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LIMit:SAVEWFM:FILEName value`` command.

    SCPI Syntax:
        ```
        - LIMit:SAVEWFM:FILEName <QString>
        - LIMit:SAVEWFM:FILEName?
        ```

    Info:
        - ``<QString>`` argument is a string containing the path of where the waveform will be
          saved.
    """

    _WRAP_ARG_WITH_QUOTES = True


class LimitSavewfm(SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:SAVEWFM`` command.

    Description:
        - This command sets or queries whether the source waveform is saved when the source waveform
          data exceeds the test limits.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:SAVEWFM?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:SAVEWFM?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LIMit:SAVEWFM value`` command.

    SCPI Syntax:
        ```
        - LIMit:SAVEWFM {ON|OFF|<NR1>}
        - LIMit:SAVEWFM?
        ```

    Info:
        - ``<NR1>`` = 0 disables the save waveform feature so that when the source waveform data
          exceeds the limits set by the limit test, the source waveform is not saved; any other
          value enables the save waveform feature so that when the source waveform data exceeds the
          limits set by the limit test, the source waveform is saved. For queries, a 0 is returned
          if the save waveform feature is off; a 1 is returned if the save waveform feature is on.
        - ``OFF`` disables saving the source waveform when it exceeds the test limits.
        - ``ON`` enables saving the source waveform when it exceeds the test limits.

    Properties:
        - ``.filename``: The ``LIMit:SAVEWFM:FILEName`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._filename = LimitSavewfmFilename(device, f"{self._cmd_syntax}:FILEName")

    @property
    def filename(self) -> LimitSavewfmFilename:
        """Return the ``LIMit:SAVEWFM:FILEName`` command.

        Description:
            - This command sets or queries the path where waveforms or log files will be saved when
              the waveform data exceeds the limits set by the limit test.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:SAVEWFM:FILEName?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:SAVEWFM:FILEName?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LIMit:SAVEWFM:FILEName value``
              command.

        SCPI Syntax:
            ```
            - LIMit:SAVEWFM:FILEName <QString>
            - LIMit:SAVEWFM:FILEName?
            ```

        Info:
            - ``<QString>`` argument is a string containing the path of where the waveform will be
              saved.
        """
        return self._filename


class LimitLog(SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:LOG`` command.

    Description:
        - This command sets or queries whether a log file is saved when the source waveform data
          exceeds the test limits.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:LOG?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:LOG?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LIMit:LOG value`` command.

    SCPI Syntax:
        ```
        - LIMit:LOG {ON|OFF|<NR1>}
        - LIMit:LOG?
        ```

    Info:
        - ``<NR1>`` = 0 disables the save log file feature so that when the source waveform data
          exceeds the limits set by the limit test, a log file is not saved; any other value enables
          the save log file feature so that when the source waveform data exceeds the limits set by
          the limit test, a log file is saved. For queries, a 0 is returned if the save log file
          feature is off; a 1 is returned if the save log file feature is on.
        - ``OFF`` disables saving a log file when the source waveform exceeds the test limits.
        - ``ON`` enables saving a log file when the source waveform exceeds the test limits.
    """


class LimitLock(SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:LOCk`` command.

    Description:
        - This command sets or queries whether vertical scaling and positioning affect both source
          and template for template comparison pairs.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:LOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:LOCk?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LIMit:LOCk value`` command.

    SCPI Syntax:
        ```
        - LIMit:LOCk {ON|OFF|<NR1>}
        - LIMit:LOCk?
        ```

    Info:
        - ``<NR1>`` = 0 disables the lock feature; any other value enables the lock feature. For
          queries, a 0 is returned if the lock feature is off; a 1 is returned if the lock feature
          is on.
        - ``OFF`` disables the lock feature.
        - ``ON`` enables the lock feature.
    """


class LimitHighlighthitsReset(SCPICmdWriteNoArguments):
    """The ``LIMit:HIGHLIGHTHits:RESet`` command.

    Description:
        - This command resets the hits highlighting for limit testing.

    Usage:
        - Using the ``.write()`` method will send the ``LIMit:HIGHLIGHTHits:RESet`` command.

    SCPI Syntax:
        ```
        - LIMit:HIGHLIGHTHits:RESet
        ```
    """


class LimitHighlighthits(SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:HIGHLIGHTHits`` command.

    Description:
        - This command sets or queries whether violation highlighting occurs when limit testing is
          active, and, if the RESET argument is set, clears the highlighting.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:HIGHLIGHTHits?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:HIGHLIGHTHits?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LIMit:HIGHLIGHTHits value`` command.

    SCPI Syntax:
        ```
        - LIMit:HIGHLIGHTHits {ON|OFF|<NR1>}
        - LIMit:HIGHLIGHTHits?
        ```

    Info:
        - ``<NR1>`` = 0 disables the violation highlighting when limit testing is active; any other
          value enables the violation highlighting feature when limit testing is active. For
          queries, a 0 is returned if the violation highlighting feature is off; a 1 is returned if
          the violation highlighting feature is on.
        - ``OFF`` disables violation highlighting when limit testing is active.
        - ``ON`` enables violation highlighting when limit testing is active.

    Properties:
        - ``.reset``: The ``LIMit:HIGHLIGHTHits:RESet`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._reset = LimitHighlighthitsReset(device, f"{self._cmd_syntax}:RESet")

    @property
    def reset(self) -> LimitHighlighthitsReset:
        """Return the ``LIMit:HIGHLIGHTHits:RESet`` command.

        Description:
            - This command resets the hits highlighting for limit testing.

        Usage:
            - Using the ``.write()`` method will send the ``LIMit:HIGHLIGHTHits:RESet`` command.

        SCPI Syntax:
            ```
            - LIMit:HIGHLIGHTHits:RESet
            ```
        """
        return self._reset


class LimitHardcopy(SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:HARDCopy`` command.

    Description:
        - This command sets or queries whether a hard copy operation is executed on the waveform
          when any waveform data exceeds the limit set in the limit test. ``LIMit:STATE`` must be
          set to ON for the hard copy operation to execute. The hard copy operation uses the port
          and prints in the format and layout specified by the HARDCopy commands.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:HARDCopy?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:HARDCopy?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LIMit:HARDCopy value`` command.

    SCPI Syntax:
        ```
        - LIMit:HARDCopy {ON|OFF|<NR1>}
        - LIMit:HARDCopy?
        ```

    Info:
        - ``<NR1>`` = 0 disables the hard copy operation; any other value turns on the hard copy
          operation for the waveform when any waveform data exceeds the limits set by the limit
          test. For queries, a 0 is returned if the hard copy operation is off; a 1 is returned if
          the hard copy operation is on.
        - ``OFF`` disables the hard copy operation.
        - ``ON`` turns on the hard copy operation for the waveform when any waveform data exceeds
          the limits set by the limit test.
    """


class LimitEmail(SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:EMail`` command.

    Description:
        - This command sets or queries whether an e-mail is generated when the source waveform data
          exceeds the limits specified for the limit test.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:EMail?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:EMail?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LIMit:EMail value`` command.

    SCPI Syntax:
        ```
        - LIMit:EMail {ON|OFF|<NR1>}
        - LIMit:EMail?
        ```

    Info:
        - ``<NR1>`` = 0 disables the e-mail feature so that when the source waveform data exceeds
          the limits set by the limit test, an e-mail is not generated; any other value enables the
          e-mail feature so that when the source waveform data exceeds the limits set by the limit
          test, an e-mail is generated. For queries, a 0 is returned if the e-mail feature is off; a
          1 is returned if the e-mail feature is on.
        - ``OFF`` disables generating an e-mail when the source waveform exceeds the test limits.
        - ``ON`` enables generating an e-mail when the source waveform exceeds the test limits.
    """


class LimitCompareRefItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:COMpare:REF<x>`` command.

    Description:
        - This command sets or queries the template against which to compare the reference waveform
          specified by x, which can be 1 through 4. The template can be a waveform saved in any of
          the reference locations (REF1 through REF4) or none.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:COMpare:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:COMpare:REF<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LIMit:COMpare:REF<x> value`` command.

    SCPI Syntax:
        ```
        - LIMit:COMpare:REF<x> {NONe|REF<x>}
        - LIMit:COMpare:REF<x>?
        ```

    Info:
        - ``NONe`` argument turns off template testing for the reference waveform specified by
          REF<x>.
        - ``REF<x>`` argument selects which reference waveform to use as the template against which
          to compare the reference waveform specified by REF<x>.
    """


class LimitCompareMathItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:COMpare:MATH<x>`` command.

    Description:
        - This command sets or queries the template against which to compare the math waveform
          specified by x, which can be 1 through 4. The template can be a waveform saved in any of
          the reference locations (REF1 through REF4) or none.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:COMpare:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:COMpare:MATH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LIMit:COMpare:MATH<x> value`` command.

    SCPI Syntax:
        ```
        - LIMit:COMpare:MATH<x> {NONe|REF<x>}
        - LIMit:COMpare:MATH<x>?
        ```

    Info:
        - ``NONe`` argument turns off template testing for the math waveform specified by MATH<x>.
        - ``REF<x>`` argument selects which reference waveform to use as the template against which
          to compare the math waveform specified by MATH<x>.
    """


class LimitCompareChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:COMpare:CH<x>`` command.

    Description:
        - This command sets or queries the template against which to compare the waveform acquired
          from the channel specified by x. The template can be a waveform saved in any of the
          reference locations (REF1 through REF4) or none.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:COMpare:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:COMpare:CH<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LIMit:COMpare:CH<x> value`` command.

    SCPI Syntax:
        ```
        - LIMit:COMpare:CH<x> {NONe|REF<x>}
        - LIMit:COMpare:CH<x>?
        ```

    Info:
        - ``NONe`` turns off template testing for the channel specified by CH<x>.
        - ``REF<x>`` selects which channel waveform to use as the template against which to compare
          the waveforms acquired by the specified channel (CH<x>).
    """


class LimitCompare(SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:COMpare`` command.

    Description:
        - This command resets the Limit Test comparison template.

    Usage:
        - Using the ``.write(value)`` method will send the ``LIMit:COMpare value`` command.

    SCPI Syntax:
        ```
        - LIMit:COMpare {RESet}
        ```

    Info:
        - ``RESet`` resets the Limit template to 'None.'.

    Properties:
        - ``.ch``: The ``LIMit:COMpare:CH<x>`` command.
        - ``.math``: The ``LIMit:COMpare:MATH<x>`` command.
        - ``.ref``: The ``LIMit:COMpare:REF<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, LimitCompareChannel] = DefaultDictPassKeyToFactory(
            lambda x: LimitCompareChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._math: Dict[int, LimitCompareMathItem] = DefaultDictPassKeyToFactory(
            lambda x: LimitCompareMathItem(device, f"{self._cmd_syntax}:MATH{x}")
        )
        self._ref: Dict[int, LimitCompareRefItem] = DefaultDictPassKeyToFactory(
            lambda x: LimitCompareRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )

    @property
    def ch(self) -> Dict[int, LimitCompareChannel]:
        """Return the ``LIMit:COMpare:CH<x>`` command.

        Description:
            - This command sets or queries the template against which to compare the waveform
              acquired from the channel specified by x. The template can be a waveform saved in any
              of the reference locations (REF1 through REF4) or none.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:COMpare:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:COMpare:CH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LIMit:COMpare:CH<x> value``
              command.

        SCPI Syntax:
            ```
            - LIMit:COMpare:CH<x> {NONe|REF<x>}
            - LIMit:COMpare:CH<x>?
            ```

        Info:
            - ``NONe`` turns off template testing for the channel specified by CH<x>.
            - ``REF<x>`` selects which channel waveform to use as the template against which to
              compare the waveforms acquired by the specified channel (CH<x>).
        """
        return self._ch

    @property
    def math(self) -> Dict[int, LimitCompareMathItem]:
        """Return the ``LIMit:COMpare:MATH<x>`` command.

        Description:
            - This command sets or queries the template against which to compare the math waveform
              specified by x, which can be 1 through 4. The template can be a waveform saved in any
              of the reference locations (REF1 through REF4) or none.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:COMpare:MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:COMpare:MATH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LIMit:COMpare:MATH<x> value``
              command.

        SCPI Syntax:
            ```
            - LIMit:COMpare:MATH<x> {NONe|REF<x>}
            - LIMit:COMpare:MATH<x>?
            ```

        Info:
            - ``NONe`` argument turns off template testing for the math waveform specified by
              MATH<x>.
            - ``REF<x>`` argument selects which reference waveform to use as the template against
              which to compare the math waveform specified by MATH<x>.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, LimitCompareRefItem]:
        """Return the ``LIMit:COMpare:REF<x>`` command.

        Description:
            - This command sets or queries the template against which to compare the reference
              waveform specified by x, which can be 1 through 4. The template can be a waveform
              saved in any of the reference locations (REF1 through REF4) or none.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:COMpare:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:COMpare:REF<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LIMit:COMpare:REF<x> value``
              command.

        SCPI Syntax:
            ```
            - LIMit:COMpare:REF<x> {NONe|REF<x>}
            - LIMit:COMpare:REF<x>?
            ```

        Info:
            - ``NONe`` argument turns off template testing for the reference waveform specified by
              REF<x>.
            - ``REF<x>`` argument selects which reference waveform to use as the template against
              which to compare the reference waveform specified by REF<x>.
        """
        return self._ref


class LimitBeep(SCPICmdWrite, SCPICmdRead):
    """The ``LIMit:BEEP`` command.

    Description:
        - This command causes the instrument to beep when the waveform data exceeds the limits set
          in the limit test ( ``LIMit:STATE`` must be on).

    Usage:
        - Using the ``.query()`` method will send the ``LIMit:BEEP?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit:BEEP?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LIMit:BEEP value`` command.

    SCPI Syntax:
        ```
        - LIMit:BEEP {ON|OFF|<NR1>}
        - LIMit:BEEP?
        ```

    Info:
        - ``<NR1>`` = 0 disables the beep; any other value enables the beep.
        - ``OFF`` disables the beep.
        - ``ON`` enables the beep.
    """


#  pylint: disable=too-many-instance-attributes
class Limit(SCPICmdRead):
    """The ``LIMit`` command.

    Description:
        - This query-only command returns all settings for the Limit commands.

    Usage:
        - Using the ``.query()`` method will send the ``LIMit?`` query.
        - Using the ``.verify(value)`` method will send the ``LIMit?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - LIMit?
        ```

    Properties:
        - ``.beep``: The ``LIMit:BEEP`` command.
        - ``.compare``: The ``LIMit:COMpare`` command.
        - ``.email``: The ``LIMit:EMail`` command.
        - ``.hardcopy``: The ``LIMit:HARDCopy`` command.
        - ``.highlighthits``: The ``LIMit:HIGHLIGHTHits`` command.
        - ``.lock``: The ``LIMit:LOCk`` command.
        - ``.log``: The ``LIMit:LOG`` command.
        - ``.savewfm``: The ``LIMit:SAVEWFM`` command.
        - ``.srq``: The ``LIMit:SRQ`` command.
        - ``.state``: The ``LIMit:STATE`` command.
        - ``.status``: The ``LIMit:STATus`` command.
        - ``.stoponviolation``: The ``LIMit:STOPOnviolation`` command.
        - ``.template``: The ``LIMit:TEMPlate`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "LIMit") -> None:
        super().__init__(device, cmd_syntax)
        self._beep = LimitBeep(device, f"{self._cmd_syntax}:BEEP")
        self._compare = LimitCompare(device, f"{self._cmd_syntax}:COMpare")
        self._email = LimitEmail(device, f"{self._cmd_syntax}:EMail")
        self._hardcopy = LimitHardcopy(device, f"{self._cmd_syntax}:HARDCopy")
        self._highlighthits = LimitHighlighthits(device, f"{self._cmd_syntax}:HIGHLIGHTHits")
        self._lock = LimitLock(device, f"{self._cmd_syntax}:LOCk")
        self._log = LimitLog(device, f"{self._cmd_syntax}:LOG")
        self._savewfm = LimitSavewfm(device, f"{self._cmd_syntax}:SAVEWFM")
        self._srq = LimitSrq(device, f"{self._cmd_syntax}:SRQ")
        self._state = LimitState(device, f"{self._cmd_syntax}:STATE")
        self._status = LimitStatus(device, f"{self._cmd_syntax}:STATus")
        self._stoponviolation = LimitStoponviolation(device, f"{self._cmd_syntax}:STOPOnviolation")
        self._template = LimitTemplate(device, f"{self._cmd_syntax}:TEMPlate")

    @property
    def beep(self) -> LimitBeep:
        """Return the ``LIMit:BEEP`` command.

        Description:
            - This command causes the instrument to beep when the waveform data exceeds the limits
              set in the limit test ( ``LIMit:STATE`` must be on).

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:BEEP?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:BEEP?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LIMit:BEEP value`` command.

        SCPI Syntax:
            ```
            - LIMit:BEEP {ON|OFF|<NR1>}
            - LIMit:BEEP?
            ```

        Info:
            - ``<NR1>`` = 0 disables the beep; any other value enables the beep.
            - ``OFF`` disables the beep.
            - ``ON`` enables the beep.
        """
        return self._beep

    @property
    def compare(self) -> LimitCompare:
        """Return the ``LIMit:COMpare`` command.

        Description:
            - This command resets the Limit Test comparison template.

        Usage:
            - Using the ``.write(value)`` method will send the ``LIMit:COMpare value`` command.

        SCPI Syntax:
            ```
            - LIMit:COMpare {RESet}
            ```

        Info:
            - ``RESet`` resets the Limit template to 'None.'.

        Sub-properties:
            - ``.ch``: The ``LIMit:COMpare:CH<x>`` command.
            - ``.math``: The ``LIMit:COMpare:MATH<x>`` command.
            - ``.ref``: The ``LIMit:COMpare:REF<x>`` command.
        """
        return self._compare

    @property
    def email(self) -> LimitEmail:
        """Return the ``LIMit:EMail`` command.

        Description:
            - This command sets or queries whether an e-mail is generated when the source waveform
              data exceeds the limits specified for the limit test.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:EMail?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:EMail?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LIMit:EMail value`` command.

        SCPI Syntax:
            ```
            - LIMit:EMail {ON|OFF|<NR1>}
            - LIMit:EMail?
            ```

        Info:
            - ``<NR1>`` = 0 disables the e-mail feature so that when the source waveform data
              exceeds the limits set by the limit test, an e-mail is not generated; any other value
              enables the e-mail feature so that when the source waveform data exceeds the limits
              set by the limit test, an e-mail is generated. For queries, a 0 is returned if the
              e-mail feature is off; a 1 is returned if the e-mail feature is on.
            - ``OFF`` disables generating an e-mail when the source waveform exceeds the test
              limits.
            - ``ON`` enables generating an e-mail when the source waveform exceeds the test limits.
        """
        return self._email

    @property
    def hardcopy(self) -> LimitHardcopy:
        """Return the ``LIMit:HARDCopy`` command.

        Description:
            - This command sets or queries whether a hard copy operation is executed on the waveform
              when any waveform data exceeds the limit set in the limit test. ``LIMit:STATE`` must
              be set to ON for the hard copy operation to execute. The hard copy operation uses the
              port and prints in the format and layout specified by the HARDCopy commands.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:HARDCopy?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:HARDCopy?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LIMit:HARDCopy value`` command.

        SCPI Syntax:
            ```
            - LIMit:HARDCopy {ON|OFF|<NR1>}
            - LIMit:HARDCopy?
            ```

        Info:
            - ``<NR1>`` = 0 disables the hard copy operation; any other value turns on the hard copy
              operation for the waveform when any waveform data exceeds the limits set by the limit
              test. For queries, a 0 is returned if the hard copy operation is off; a 1 is returned
              if the hard copy operation is on.
            - ``OFF`` disables the hard copy operation.
            - ``ON`` turns on the hard copy operation for the waveform when any waveform data
              exceeds the limits set by the limit test.
        """
        return self._hardcopy

    @property
    def highlighthits(self) -> LimitHighlighthits:
        """Return the ``LIMit:HIGHLIGHTHits`` command.

        Description:
            - This command sets or queries whether violation highlighting occurs when limit testing
              is active, and, if the RESET argument is set, clears the highlighting.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:HIGHLIGHTHits?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:HIGHLIGHTHits?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LIMit:HIGHLIGHTHits value``
              command.

        SCPI Syntax:
            ```
            - LIMit:HIGHLIGHTHits {ON|OFF|<NR1>}
            - LIMit:HIGHLIGHTHits?
            ```

        Info:
            - ``<NR1>`` = 0 disables the violation highlighting when limit testing is active; any
              other value enables the violation highlighting feature when limit testing is active.
              For queries, a 0 is returned if the violation highlighting feature is off; a 1 is
              returned if the violation highlighting feature is on.
            - ``OFF`` disables violation highlighting when limit testing is active.
            - ``ON`` enables violation highlighting when limit testing is active.

        Sub-properties:
            - ``.reset``: The ``LIMit:HIGHLIGHTHits:RESet`` command.
        """
        return self._highlighthits

    @property
    def lock(self) -> LimitLock:
        """Return the ``LIMit:LOCk`` command.

        Description:
            - This command sets or queries whether vertical scaling and positioning affect both
              source and template for template comparison pairs.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:LOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:LOCk?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LIMit:LOCk value`` command.

        SCPI Syntax:
            ```
            - LIMit:LOCk {ON|OFF|<NR1>}
            - LIMit:LOCk?
            ```

        Info:
            - ``<NR1>`` = 0 disables the lock feature; any other value enables the lock feature. For
              queries, a 0 is returned if the lock feature is off; a 1 is returned if the lock
              feature is on.
            - ``OFF`` disables the lock feature.
            - ``ON`` enables the lock feature.
        """
        return self._lock

    @property
    def log(self) -> LimitLog:
        """Return the ``LIMit:LOG`` command.

        Description:
            - This command sets or queries whether a log file is saved when the source waveform data
              exceeds the test limits.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:LOG?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:LOG?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LIMit:LOG value`` command.

        SCPI Syntax:
            ```
            - LIMit:LOG {ON|OFF|<NR1>}
            - LIMit:LOG?
            ```

        Info:
            - ``<NR1>`` = 0 disables the save log file feature so that when the source waveform data
              exceeds the limits set by the limit test, a log file is not saved; any other value
              enables the save log file feature so that when the source waveform data exceeds the
              limits set by the limit test, a log file is saved. For queries, a 0 is returned if the
              save log file feature is off; a 1 is returned if the save log file feature is on.
            - ``OFF`` disables saving a log file when the source waveform exceeds the test limits.
            - ``ON`` enables saving a log file when the source waveform exceeds the test limits.
        """
        return self._log

    @property
    def savewfm(self) -> LimitSavewfm:
        """Return the ``LIMit:SAVEWFM`` command.

        Description:
            - This command sets or queries whether the source waveform is saved when the source
              waveform data exceeds the test limits.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:SAVEWFM?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:SAVEWFM?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LIMit:SAVEWFM value`` command.

        SCPI Syntax:
            ```
            - LIMit:SAVEWFM {ON|OFF|<NR1>}
            - LIMit:SAVEWFM?
            ```

        Info:
            - ``<NR1>`` = 0 disables the save waveform feature so that when the source waveform data
              exceeds the limits set by the limit test, the source waveform is not saved; any other
              value enables the save waveform feature so that when the source waveform data exceeds
              the limits set by the limit test, the source waveform is saved. For queries, a 0 is
              returned if the save waveform feature is off; a 1 is returned if the save waveform
              feature is on.
            - ``OFF`` disables saving the source waveform when it exceeds the test limits.
            - ``ON`` enables saving the source waveform when it exceeds the test limits.

        Sub-properties:
            - ``.filename``: The ``LIMit:SAVEWFM:FILEName`` command.
        """
        return self._savewfm

    @property
    def srq(self) -> LimitSrq:
        """Return the ``LIMit:SRQ`` command.

        Description:
            - This command sets or queries whether a Service Request Interrupt (SRQ) is generated
              when the waveform data falls outside of the test limits.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:SRQ?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:SRQ?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LIMit:SRQ value`` command.

        SCPI Syntax:
            ```
            - LIMit:SRQ {ON|OFF|<NR1>}
            - LIMit:SRQ?
            ```

        Info:
            - ``<NR1>`` = 0 disables sending an SRQ when the waveform data falls outside of the
              limits set by the limit test; any other value enables generation of an SRQ when the
              waveform data falls outside of the limits set by the limit test. For queries, a 0 is
              returned if SRQ is off; a 1 is returned if the SRQ is on.
            - ``OFF`` disables generation of an SRQ when the waveform data falls outside of the
              limits set by the limit test.
            - ``ON`` enables generation of an SRQ when the waveform data falls outside of the limits
              set by the limit test. If an SRQ is generated, the instrument sends the status event
              'Limit testing failed.'.
        """
        return self._srq

    @property
    def state(self) -> LimitState:
        """Return the ``LIMit:STATE`` command.

        Description:
            - This command sets limit testing on or off or queries whether limit testing is in
              effect.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:STATE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LIMit:STATE value`` command.

        SCPI Syntax:
            ```
            - LIMit:STATE {ON|OFF|<NR1>}
            - LIMit:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 disables the limit testing operation; any other value turns on limit
              testing of waveforms. For queries, a 0 is returned if limit testing is off; a 1 is
              returned if the limit testing is on.
            - ``OFF`` disables limit testing.
            - ``ON`` turns on limit testing of waveforms.
        """
        return self._state

    @property
    def status(self) -> LimitStatus:
        """Return the ``LIMit:STATus`` command.

        Description:
            - This command queries the state of limit testing.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:STATus?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:STATus?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - LIMit:STATus?
            ```
        """
        return self._status

    @property
    def stoponviolation(self) -> LimitStoponviolation:
        """Return the ``LIMit:STOPOnviolation`` command.

        Description:
            - This command sets or queries whether acquisitions are stopped when the waveform data
              exceeds the test limits.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:STOPOnviolation?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:STOPOnviolation?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LIMit:STOPOnviolation value``
              command.

        SCPI Syntax:
            ```
            - LIMit:STOPOnviolation {ON|OFF|<NR1>}
            - LIMit:STOPOnviolation?
            ```

        Info:
            - ``<NR1>`` = 0 disables the stop on violation feature; any other value enables the stop
              on violation feature so that when the waveform data exceeds the limits set by the
              limit test, acquisitions are stopped. For queries, a 0 is returned if the stop on
              violation feature is off; a 1 is returned if the stop on violation feature is on.
            - ``OFF`` disables the stop on violation feature.
            - ``ON`` enables the stop on violation feature so that when the waveform data exceeds
              the limits set by the limit test, acquisitions are stopped.
        """
        return self._stoponviolation

    @property
    def template(self) -> LimitTemplate:
        """Return the ``LIMit:TEMPlate`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit:TEMPlate?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit:TEMPlate?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.destination``: The ``LIMit:TEMPlate:DESTination`` command.
            - ``.source``: The ``LIMit:TEMPlate:SOUrce`` command.
            - ``.store``: The ``LIMit:TEMPlate:STORe`` command.
            - ``.tolerance``: The ``LIMit:TEMPlate:TOLerance`` command tree.
        """
        return self._template
