"""The mask commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MASK:DELete 'MASK<x>'
    - MASK:MASK<x>:COUNT:HITS?
    - MASK:MASK<x>:COUNT:SEG<x>:HITS?
    - MASK:MASK<x>:COUNT?
    - MASK:MASK<x>:DEFinedby {SEGments|TOLerances}
    - MASK:MASK<x>:DEFinedby?
    - MASK:MASK<x>:DISplay {ON|OFF}
    - MASK:MASK<x>:DISplay?
    - MASK:MASK<x>:LIST?
    - MASK:MASK<x>:SEG<x>:POINTS
    - MASK:MASK<x>:SEG<x>:POINTS?
    - MASK:MASK<x>:SOUrce {CH<x>|REF<x>|MATH<x>|RFvsTime}
    - MASK:MASK<x>:SOUrce?
    - MASK:MASK<x>:TESt:STATE {ON|OFF}
    - MASK:MASK<x>:TESt:STATE?
    - MASK:MASK<x>:TESt:STATUS?
    - MASK:MASK<x>:TESt:THReshold <NR1>
    - MASK:MASK<x>:TESt:THReshold?
    - MASK:MASK<x>:TOLerance:HORizontal <NR3>
    - MASK:MASK<x>:TOLerance:HORizontal?
    - MASK:MASK<x>:TOLerance:UPDatenow
    - MASK:MASK<x>:TOLerance:VERTical <NR3>
    - MASK:MASK<x>:TOLerance:VERTical?
    - MASK:TESt:WAVEforms <NR1>
    - MASK:TESt:WAVEforms?
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


class MaskTestWaveforms(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:WAVEforms`` command.

    Description:
        - This command sets or queries the number of waveform acquisitions to test during mask
          testing. The number of waveforms applies to all mask tests.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:WAVEforms?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:WAVEforms?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:WAVEforms value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:WAVEforms <NR1>
        - MASK:TESt:WAVEforms?
        ```

    Info:
        - ``<NR1>`` specifies the number of waveform acquisitions.
    """


class MaskTest(SCPICmdRead):
    """The ``MASK:TESt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.waveforms``: The ``MASK:TESt:WAVEforms`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._waveforms = MaskTestWaveforms(device, f"{self._cmd_syntax}:WAVEforms")

    @property
    def waveforms(self) -> MaskTestWaveforms:
        """Return the ``MASK:TESt:WAVEforms`` command.

        Description:
            - This command sets or queries the number of waveform acquisitions to test during mask
              testing. The number of waveforms applies to all mask tests.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:WAVEforms?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:WAVEforms?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:WAVEforms value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:WAVEforms <NR1>
            - MASK:TESt:WAVEforms?
            ```

        Info:
            - ``<NR1>`` specifies the number of waveform acquisitions.
        """
        return self._waveforms


class MaskMaskItemToleranceVertical(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASK<x>:TOLerance:VERTical`` command.

    Description:
        - This command sets or queries the mask vertical tolerance.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASK<x>:TOLerance:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:TOLerance:VERTical?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MASK<x>:TOLerance:VERTical value``
          command.

    SCPI Syntax:
        ```
        - MASK:MASK<x>:TOLerance:VERTical <NR3>
        - MASK:MASK<x>:TOLerance:VERTical?
        ```

    Info:
        - ``MASK<x>`` specifies the mask number.
        - ``<NR3>`` is the tolerance in units of graticule divisions. The maximum is 1 division.
    """


class MaskMaskItemToleranceUpdatenow(SCPICmdWriteNoArguments):
    """The ``MASK:MASK<x>:TOLerance:UPDatenow`` command.

    Description:
        - This command causes the tolerance mask to be recalculated with the current horizontal and
          vertical tolerances.

    Usage:
        - Using the ``.write()`` method will send the ``MASK:MASK<x>:TOLerance:UPDatenow`` command.

    SCPI Syntax:
        ```
        - MASK:MASK<x>:TOLerance:UPDatenow
        ```

    Info:
        - ``MASK<x>`` specifies the mask number.
    """


class MaskMaskItemToleranceHorizontal(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASK<x>:TOLerance:HORizontal`` command.

    Description:
        - This command sets or queries the mask horizontal tolerance.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASK<x>:TOLerance:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:TOLerance:HORizontal?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MASK:MASK<x>:TOLerance:HORizontal value`` command.

    SCPI Syntax:
        ```
        - MASK:MASK<x>:TOLerance:HORizontal <NR3>
        - MASK:MASK<x>:TOLerance:HORizontal?
        ```

    Info:
        - ``MASK<x>`` specifies the mask number.
        - ``<NR3>`` is the tolerance in units of graticule divisions. The maximum is 1 division.
    """


class MaskMaskItemTolerance(SCPICmdRead):
    """The ``MASK:MASK<x>:TOLerance`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASK<x>:TOLerance?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:TOLerance?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``MASK<x>`` specifies the mask number.

    Properties:
        - ``.horizontal``: The ``MASK:MASK<x>:TOLerance:HORizontal`` command.
        - ``.updatenow``: The ``MASK:MASK<x>:TOLerance:UPDatenow`` command.
        - ``.vertical``: The ``MASK:MASK<x>:TOLerance:VERTical`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._horizontal = MaskMaskItemToleranceHorizontal(device, f"{self._cmd_syntax}:HORizontal")
        self._updatenow = MaskMaskItemToleranceUpdatenow(device, f"{self._cmd_syntax}:UPDatenow")
        self._vertical = MaskMaskItemToleranceVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def horizontal(self) -> MaskMaskItemToleranceHorizontal:
        """Return the ``MASK:MASK<x>:TOLerance:HORizontal`` command.

        Description:
            - This command sets or queries the mask horizontal tolerance.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASK<x>:TOLerance:HORizontal?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MASK:MASK<x>:TOLerance:HORizontal?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MASK:MASK<x>:TOLerance:HORizontal value`` command.

        SCPI Syntax:
            ```
            - MASK:MASK<x>:TOLerance:HORizontal <NR3>
            - MASK:MASK<x>:TOLerance:HORizontal?
            ```

        Info:
            - ``MASK<x>`` specifies the mask number.
            - ``<NR3>`` is the tolerance in units of graticule divisions. The maximum is 1 division.
        """
        return self._horizontal

    @property
    def updatenow(self) -> MaskMaskItemToleranceUpdatenow:
        """Return the ``MASK:MASK<x>:TOLerance:UPDatenow`` command.

        Description:
            - This command causes the tolerance mask to be recalculated with the current horizontal
              and vertical tolerances.

        Usage:
            - Using the ``.write()`` method will send the ``MASK:MASK<x>:TOLerance:UPDatenow``
              command.

        SCPI Syntax:
            ```
            - MASK:MASK<x>:TOLerance:UPDatenow
            ```

        Info:
            - ``MASK<x>`` specifies the mask number.
        """
        return self._updatenow

    @property
    def vertical(self) -> MaskMaskItemToleranceVertical:
        """Return the ``MASK:MASK<x>:TOLerance:VERTical`` command.

        Description:
            - This command sets or queries the mask vertical tolerance.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASK<x>:TOLerance:VERTical?``
              query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:TOLerance:VERTical?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MASK:MASK<x>:TOLerance:VERTical value`` command.

        SCPI Syntax:
            ```
            - MASK:MASK<x>:TOLerance:VERTical <NR3>
            - MASK:MASK<x>:TOLerance:VERTical?
            ```

        Info:
            - ``MASK<x>`` specifies the mask number.
            - ``<NR3>`` is the tolerance in units of graticule divisions. The maximum is 1 division.
        """
        return self._vertical


class MaskMaskItemTestThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASK<x>:TESt:THReshold`` command.

    Description:
        - This command sets or queries the number of waveform violations needed for the specified
          mask test to change from PASS to FAIL.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASK<x>:TESt:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:TESt:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MASK<x>:TESt:THReshold value``
          command.

    SCPI Syntax:
        ```
        - MASK:MASK<x>:TESt:THReshold <NR1>
        - MASK:MASK<x>:TESt:THReshold?
        ```

    Info:
        - ``MASK<x>`` specifies the mask test.
        - ``<NR1>`` specifies the threshold value.
    """


class MaskMaskItemTestStatus(SCPICmdRead):
    """The ``MASK:MASK<x>:TESt:STATUS`` command.

    Description:
        - This command returns the status of the specified mask test.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASK<x>:TESt:STATUS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:TESt:STATUS?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:MASK<x>:TESt:STATUS?
        ```

    Info:
        - ``MASK<x>`` specifies the mask test.
    """


class MaskMaskItemTestState(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASK<x>:TESt:STATE`` command.

    Description:
        - This command sets or queries the state of the specified mask test.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASK<x>:TESt:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:TESt:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MASK<x>:TESt:STATE value``
          command.

    SCPI Syntax:
        ```
        - MASK:MASK<x>:TESt:STATE {ON|OFF}
        - MASK:MASK<x>:TESt:STATE?
        ```

    Info:
        - ``MASK<x>`` specifies the mask test.
        - ``ON`` sets the mask test state to ON. When the state is ON the Pass/Fail status and hit
          count information are reset and the mask test is started.
        - ``OFF`` sets the mask test state to OFF. When the mask test completes the state is set to
          OFF.
    """


class MaskMaskItemTest(SCPICmdRead):
    """The ``MASK:MASK<x>:TESt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASK<x>:TESt?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:TESt?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``MASK<x>`` specifies the mask test.

    Properties:
        - ``.state``: The ``MASK:MASK<x>:TESt:STATE`` command.
        - ``.status``: The ``MASK:MASK<x>:TESt:STATUS`` command.
        - ``.threshold``: The ``MASK:MASK<x>:TESt:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = MaskMaskItemTestState(device, f"{self._cmd_syntax}:STATE")
        self._status = MaskMaskItemTestStatus(device, f"{self._cmd_syntax}:STATUS")
        self._threshold = MaskMaskItemTestThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def state(self) -> MaskMaskItemTestState:
        """Return the ``MASK:MASK<x>:TESt:STATE`` command.

        Description:
            - This command sets or queries the state of the specified mask test.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASK<x>:TESt:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:TESt:STATE?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MASK<x>:TESt:STATE value``
              command.

        SCPI Syntax:
            ```
            - MASK:MASK<x>:TESt:STATE {ON|OFF}
            - MASK:MASK<x>:TESt:STATE?
            ```

        Info:
            - ``MASK<x>`` specifies the mask test.
            - ``ON`` sets the mask test state to ON. When the state is ON the Pass/Fail status and
              hit count information are reset and the mask test is started.
            - ``OFF`` sets the mask test state to OFF. When the mask test completes the state is set
              to OFF.
        """
        return self._state

    @property
    def status(self) -> MaskMaskItemTestStatus:
        """Return the ``MASK:MASK<x>:TESt:STATUS`` command.

        Description:
            - This command returns the status of the specified mask test.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASK<x>:TESt:STATUS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:TESt:STATUS?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:MASK<x>:TESt:STATUS?
            ```

        Info:
            - ``MASK<x>`` specifies the mask test.
        """
        return self._status

    @property
    def threshold(self) -> MaskMaskItemTestThreshold:
        """Return the ``MASK:MASK<x>:TESt:THReshold`` command.

        Description:
            - This command sets or queries the number of waveform violations needed for the
              specified mask test to change from PASS to FAIL.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASK<x>:TESt:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:TESt:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MASK<x>:TESt:THReshold value``
              command.

        SCPI Syntax:
            ```
            - MASK:MASK<x>:TESt:THReshold <NR1>
            - MASK:MASK<x>:TESt:THReshold?
            ```

        Info:
            - ``MASK<x>`` specifies the mask test.
            - ``<NR1>`` specifies the threshold value.
        """
        return self._threshold


class MaskMaskItemSource(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASK<x>:SOUrce`` command.

    Description:
        - This command sets or queries analog source for the specified mask test.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASK<x>:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:SOUrce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MASK<x>:SOUrce value`` command.

    SCPI Syntax:
        ```
        - MASK:MASK<x>:SOUrce {CH<x>|REF<x>|MATH<x>|RFvsTime}
        - MASK:MASK<x>:SOUrce?
        ```

    Info:
        - ``MASK<x>`` specifies the mask test.
        - ``CH<x>`` specifies an analog channel as source.
        - ``MATH<x>`` specifies a math channel as source.
        - ``REF<x>`` specifies a reference waveform as the source.
        - ``RFvsTime`` specifies a RF vs Time as the source.
    """


class MaskMaskItemSegItemPoints(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``MASK:MASK<x>:SEG<x>:POINTS`` command.

    Description:
        - This command sets or queries the X/Y coordinates of all points in the designated mask
          segment. Mask vertices are in time/volts (currently limited to 1024 characters). The set
          form defines new points in the mask, replacing any existing points.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASK<x>:SEG<x>:POINTS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:SEG<x>:POINTS?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``MASK:MASK<x>:SEG<x>:POINTS`` command.

    SCPI Syntax:
        ```
        - MASK:MASK<x>:SEG<x>:POINTS
        - MASK:MASK<x>:SEG<x>:POINTS?
        ```

    Info:
        - ``MASK<x>`` specifies the mask test.
        - ``SEG<x>`` specifies the mask segment.
    """


class MaskMaskItemSegItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MASK:MASK<x>:SEG<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASK<x>:SEG<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:SEG<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``MASK<x>`` specifies the mask test.
        - ``SEG<x>`` specifies the mask segment.

    Properties:
        - ``.points``: The ``MASK:MASK<x>:SEG<x>:POINTS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._points = MaskMaskItemSegItemPoints(device, f"{self._cmd_syntax}:POINTS")

    @property
    def points(self) -> MaskMaskItemSegItemPoints:
        """Return the ``MASK:MASK<x>:SEG<x>:POINTS`` command.

        Description:
            - This command sets or queries the X/Y coordinates of all points in the designated mask
              segment. Mask vertices are in time/volts (currently limited to 1024 characters). The
              set form defines new points in the mask, replacing any existing points.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASK<x>:SEG<x>:POINTS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:SEG<x>:POINTS?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``MASK:MASK<x>:SEG<x>:POINTS`` command.

        SCPI Syntax:
            ```
            - MASK:MASK<x>:SEG<x>:POINTS
            - MASK:MASK<x>:SEG<x>:POINTS?
            ```

        Info:
            - ``MASK<x>`` specifies the mask test.
            - ``SEG<x>`` specifies the mask segment.
        """
        return self._points


class MaskMaskItemList(SCPICmdRead):
    """The ``MASK:MASK<x>:LIST`` command.

    Description:
        - This command queries the list of segments in the mask used by the specified mask test.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASK<x>:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:LIST?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:MASK<x>:LIST?
        ```

    Info:
        - ``MASK<x>`` specifies the mask test.
    """


class MaskMaskItemDisplay(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASK<x>:DISplay`` command.

    Description:
        - This command sets or queries the display state of the mask used for the specified mask
          test.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASK<x>:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:DISplay?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MASK<x>:DISplay value`` command.

    SCPI Syntax:
        ```
        - MASK:MASK<x>:DISplay {ON|OFF}
        - MASK:MASK<x>:DISplay?
        ```

    Info:
        - ``MASK<x>`` specifies the mask test.
        - ``ON`` sets the display state of the specified mask to on.
        - ``OFF`` sets the display state of the specified mask to off.
    """


class MaskMaskItemDefinedby(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MASK<x>:DEFinedby`` command.

    Description:
        - This command sets or queries whether the specified mask is defined by segments or
          tolerances. Segment masks are defined by one or more polygons. Tolerance masks are defined
          by specified horizontal and vertical tolerances around the mask source.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASK<x>:DEFinedby?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:DEFinedby?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MASK<x>:DEFinedby value`` command.

    SCPI Syntax:
        ```
        - MASK:MASK<x>:DEFinedby {SEGments|TOLerances}
        - MASK:MASK<x>:DEFinedby?
        ```

    Info:
        - ``MASK<x>`` specifies the mask number.
        - ``SEGments`` defines the mask by segments.
        - ``TOLerances`` defines the mask by horizontal and vertical tolerances around mask source.
    """


class MaskMaskItemCountSegItemHits(SCPICmdRead):
    """The ``MASK:MASK<x>:COUNT:SEG<x>:HITS`` command.

    Description:
        - The command returns the total number of mask hits in the specified mask segment of the
          specified mask test.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASK<x>:COUNT:SEG<x>:HITS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:COUNT:SEG<x>:HITS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:MASK<x>:COUNT:SEG<x>:HITS?
        ```

    Info:
        - ``MASK<x>`` specifies the mask test.
        - ``SEG<x>`` specifies the mask segment.
    """


class MaskMaskItemCountSegItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MASK:MASK<x>:COUNT:SEG<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASK<x>:COUNT:SEG<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:COUNT:SEG<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``MASK<x>`` specifies the mask test.
        - ``SEG<x>`` specifies the mask segment.

    Properties:
        - ``.hits``: The ``MASK:MASK<x>:COUNT:SEG<x>:HITS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hits = MaskMaskItemCountSegItemHits(device, f"{self._cmd_syntax}:HITS")

    @property
    def hits(self) -> MaskMaskItemCountSegItemHits:
        """Return the ``MASK:MASK<x>:COUNT:SEG<x>:HITS`` command.

        Description:
            - The command returns the total number of mask hits in the specified mask segment of the
              specified mask test.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASK<x>:COUNT:SEG<x>:HITS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:COUNT:SEG<x>:HITS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:MASK<x>:COUNT:SEG<x>:HITS?
            ```

        Info:
            - ``MASK<x>`` specifies the mask test.
            - ``SEG<x>`` specifies the mask segment.
        """
        return self._hits


class MaskMaskItemCountHits(SCPICmdRead):
    """The ``MASK:MASK<x>:COUNT:HITS`` command.

    Description:
        - This command returns the total number of mask hits in all mask segments for the specified
          mask test.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASK<x>:COUNT:HITS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:COUNT:HITS?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:MASK<x>:COUNT:HITS?
        ```

    Info:
        - ``MASK<x>`` specifies the mask test.
    """


class MaskMaskItemCount(SCPICmdRead):
    """The ``MASK:MASK<x>:COUNT`` command.

    Description:
        - This command returns the total number of mask hits in all segments and the number of mask
          hits in each individual mask segment for the specified mask test.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASK<x>:COUNT?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:COUNT?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:MASK<x>:COUNT?
        ```

    Info:
        - ``MASK<x>`` specifies the mask test.

    Properties:
        - ``.hits``: The ``MASK:MASK<x>:COUNT:HITS`` command.
        - ``.seg``: The ``MASK:MASK<x>:COUNT:SEG<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hits = MaskMaskItemCountHits(device, f"{self._cmd_syntax}:HITS")
        self._seg: Dict[int, MaskMaskItemCountSegItem] = DefaultDictPassKeyToFactory(
            lambda x: MaskMaskItemCountSegItem(device, f"{self._cmd_syntax}:SEG{x}")
        )

    @property
    def hits(self) -> MaskMaskItemCountHits:
        """Return the ``MASK:MASK<x>:COUNT:HITS`` command.

        Description:
            - This command returns the total number of mask hits in all mask segments for the
              specified mask test.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASK<x>:COUNT:HITS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:COUNT:HITS?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:MASK<x>:COUNT:HITS?
            ```

        Info:
            - ``MASK<x>`` specifies the mask test.
        """
        return self._hits

    @property
    def seg(self) -> Dict[int, MaskMaskItemCountSegItem]:
        """Return the ``MASK:MASK<x>:COUNT:SEG<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASK<x>:COUNT:SEG<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:COUNT:SEG<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``MASK<x>`` specifies the mask test.
            - ``SEG<x>`` specifies the mask segment.

        Sub-properties:
            - ``.hits``: The ``MASK:MASK<x>:COUNT:SEG<x>:HITS`` command.
        """
        return self._seg


#  pylint: disable=too-many-instance-attributes
class MaskMaskItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MASK:MASK<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MASK<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``MASK<x>`` specifies the mask test.

    Properties:
        - ``.count``: The ``MASK:MASK<x>:COUNT`` command.
        - ``.definedby``: The ``MASK:MASK<x>:DEFinedby`` command.
        - ``.display``: The ``MASK:MASK<x>:DISplay`` command.
        - ``.list``: The ``MASK:MASK<x>:LIST`` command.
        - ``.seg``: The ``MASK:MASK<x>:SEG<x>`` command tree.
        - ``.source``: The ``MASK:MASK<x>:SOUrce`` command.
        - ``.test``: The ``MASK:MASK<x>:TESt`` command tree.
        - ``.tolerance``: The ``MASK:MASK<x>:TOLerance`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._count = MaskMaskItemCount(device, f"{self._cmd_syntax}:COUNT")
        self._definedby = MaskMaskItemDefinedby(device, f"{self._cmd_syntax}:DEFinedby")
        self._display = MaskMaskItemDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._list = MaskMaskItemList(device, f"{self._cmd_syntax}:LIST")
        self._seg: Dict[int, MaskMaskItemSegItem] = DefaultDictPassKeyToFactory(
            lambda x: MaskMaskItemSegItem(device, f"{self._cmd_syntax}:SEG{x}")
        )
        self._source = MaskMaskItemSource(device, f"{self._cmd_syntax}:SOUrce")
        self._test = MaskMaskItemTest(device, f"{self._cmd_syntax}:TESt")
        self._tolerance = MaskMaskItemTolerance(device, f"{self._cmd_syntax}:TOLerance")

    @property
    def count(self) -> MaskMaskItemCount:
        """Return the ``MASK:MASK<x>:COUNT`` command.

        Description:
            - This command returns the total number of mask hits in all segments and the number of
              mask hits in each individual mask segment for the specified mask test.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASK<x>:COUNT?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:COUNT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:MASK<x>:COUNT?
            ```

        Info:
            - ``MASK<x>`` specifies the mask test.

        Sub-properties:
            - ``.hits``: The ``MASK:MASK<x>:COUNT:HITS`` command.
            - ``.seg``: The ``MASK:MASK<x>:COUNT:SEG<x>`` command tree.
        """
        return self._count

    @property
    def definedby(self) -> MaskMaskItemDefinedby:
        """Return the ``MASK:MASK<x>:DEFinedby`` command.

        Description:
            - This command sets or queries whether the specified mask is defined by segments or
              tolerances. Segment masks are defined by one or more polygons. Tolerance masks are
              defined by specified horizontal and vertical tolerances around the mask source.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASK<x>:DEFinedby?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:DEFinedby?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MASK<x>:DEFinedby value``
              command.

        SCPI Syntax:
            ```
            - MASK:MASK<x>:DEFinedby {SEGments|TOLerances}
            - MASK:MASK<x>:DEFinedby?
            ```

        Info:
            - ``MASK<x>`` specifies the mask number.
            - ``SEGments`` defines the mask by segments.
            - ``TOLerances`` defines the mask by horizontal and vertical tolerances around mask
              source.
        """
        return self._definedby

    @property
    def display(self) -> MaskMaskItemDisplay:
        """Return the ``MASK:MASK<x>:DISplay`` command.

        Description:
            - This command sets or queries the display state of the mask used for the specified mask
              test.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASK<x>:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:DISplay?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MASK<x>:DISplay value``
              command.

        SCPI Syntax:
            ```
            - MASK:MASK<x>:DISplay {ON|OFF}
            - MASK:MASK<x>:DISplay?
            ```

        Info:
            - ``MASK<x>`` specifies the mask test.
            - ``ON`` sets the display state of the specified mask to on.
            - ``OFF`` sets the display state of the specified mask to off.
        """
        return self._display

    @property
    def list(self) -> MaskMaskItemList:
        """Return the ``MASK:MASK<x>:LIST`` command.

        Description:
            - This command queries the list of segments in the mask used by the specified mask test.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASK<x>:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:LIST?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:MASK<x>:LIST?
            ```

        Info:
            - ``MASK<x>`` specifies the mask test.
        """
        return self._list

    @property
    def seg(self) -> Dict[int, MaskMaskItemSegItem]:
        """Return the ``MASK:MASK<x>:SEG<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASK<x>:SEG<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:SEG<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``MASK<x>`` specifies the mask test.
            - ``SEG<x>`` specifies the mask segment.

        Sub-properties:
            - ``.points``: The ``MASK:MASK<x>:SEG<x>:POINTS`` command.
        """
        return self._seg

    @property
    def source(self) -> MaskMaskItemSource:
        """Return the ``MASK:MASK<x>:SOUrce`` command.

        Description:
            - This command sets or queries analog source for the specified mask test.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASK<x>:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MASK<x>:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - MASK:MASK<x>:SOUrce {CH<x>|REF<x>|MATH<x>|RFvsTime}
            - MASK:MASK<x>:SOUrce?
            ```

        Info:
            - ``MASK<x>`` specifies the mask test.
            - ``CH<x>`` specifies an analog channel as source.
            - ``MATH<x>`` specifies a math channel as source.
            - ``REF<x>`` specifies a reference waveform as the source.
            - ``RFvsTime`` specifies a RF vs Time as the source.
        """
        return self._source

    @property
    def test(self) -> MaskMaskItemTest:
        """Return the ``MASK:MASK<x>:TESt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASK<x>:TESt?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:TESt?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``MASK<x>`` specifies the mask test.

        Sub-properties:
            - ``.state``: The ``MASK:MASK<x>:TESt:STATE`` command.
            - ``.status``: The ``MASK:MASK<x>:TESt:STATUS`` command.
            - ``.threshold``: The ``MASK:MASK<x>:TESt:THReshold`` command.
        """
        return self._test

    @property
    def tolerance(self) -> MaskMaskItemTolerance:
        """Return the ``MASK:MASK<x>:TOLerance`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASK<x>:TOLerance?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>:TOLerance?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``MASK<x>`` specifies the mask number.

        Sub-properties:
            - ``.horizontal``: The ``MASK:MASK<x>:TOLerance:HORizontal`` command.
            - ``.updatenow``: The ``MASK:MASK<x>:TOLerance:UPDatenow`` command.
            - ``.vertical``: The ``MASK:MASK<x>:TOLerance:VERTical`` command.
        """
        return self._tolerance


class MaskDelete(SCPICmdWrite):
    """The ``MASK:DELete`` command.

    Description:
        - This command deletes all mask segments of the specified mask test.

    Usage:
        - Using the ``.write(value)`` method will send the ``MASK:DELete value`` command.

    SCPI Syntax:
        ```
        - MASK:DELete 'MASK<x>'
        ```

    Info:
        - ``MASK<x>`` specifies the mask test. This argument is enclosed in quotes.
    """


class Mask(SCPICmdRead):
    """The ``MASK`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.delete``: The ``MASK:DELete`` command.
        - ``.mask``: The ``MASK:MASK<x>`` command tree.
        - ``.test``: The ``MASK:TESt`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MASK") -> None:
        super().__init__(device, cmd_syntax)
        self._delete = MaskDelete(device, f"{self._cmd_syntax}:DELete")
        self._mask: Dict[int, MaskMaskItem] = DefaultDictPassKeyToFactory(
            lambda x: MaskMaskItem(device, f"{self._cmd_syntax}:MASK{x}")
        )
        self._test = MaskTest(device, f"{self._cmd_syntax}:TESt")

    @property
    def delete(self) -> MaskDelete:
        """Return the ``MASK:DELete`` command.

        Description:
            - This command deletes all mask segments of the specified mask test.

        Usage:
            - Using the ``.write(value)`` method will send the ``MASK:DELete value`` command.

        SCPI Syntax:
            ```
            - MASK:DELete 'MASK<x>'
            ```

        Info:
            - ``MASK<x>`` specifies the mask test. This argument is enclosed in quotes.
        """
        return self._delete

    @property
    def mask(self) -> Dict[int, MaskMaskItem]:
        """Return the ``MASK:MASK<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MASK<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MASK<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``MASK<x>`` specifies the mask test.

        Sub-properties:
            - ``.count``: The ``MASK:MASK<x>:COUNT`` command.
            - ``.definedby``: The ``MASK:MASK<x>:DEFinedby`` command.
            - ``.display``: The ``MASK:MASK<x>:DISplay`` command.
            - ``.list``: The ``MASK:MASK<x>:LIST`` command.
            - ``.seg``: The ``MASK:MASK<x>:SEG<x>`` command tree.
            - ``.source``: The ``MASK:MASK<x>:SOUrce`` command.
            - ``.test``: The ``MASK:MASK<x>:TESt`` command tree.
            - ``.tolerance``: The ``MASK:MASK<x>:TOLerance`` command tree.
        """
        return self._mask

    @property
    def test(self) -> MaskTest:
        """Return the ``MASK:TESt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.waveforms``: The ``MASK:TESt:WAVEforms`` command.
        """
        return self._test
