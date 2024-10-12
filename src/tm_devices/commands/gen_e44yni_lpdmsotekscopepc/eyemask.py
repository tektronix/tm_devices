"""The eyemask commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - EYEMASK:MASK<x>:COUNt:HITS?
    - EYEMASK:MASK<x>:COUNt:SEG<y>:HITS?
    - EYEMASK:MASK<x>:CREATor?
    - EYEMASK:MASK<x>:ENAbled {ON|OFF}
    - EYEMASK:MASK<x>:ENAbled?
    - EYEMASK:MASK<x>:MASKOffset:HORizontal:AUTOfit?
    - EYEMASK:MASK<x>:MASKfile <Qstring>
    - EYEMASK:MASK<x>:MASKfile?
    - EYEMASK:MASK<x>:TESt:SAMple:THReshold <NR1>
    - EYEMASK:MASK<x>:TESt:SAMple:THReshold?
    - EYEMASK:MASK<x>:TESt:STATUS?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class EyemaskMaskItemTestStatus(SCPICmdRead):
    """The ``EYEMASK:MASK<x>:TESt:STATUS`` command.

    Description:
        - This query-only command returns the mask hit test status.

    Usage:
        - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:TESt:STATUS?`` query.
        - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:TESt:STATUS?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - EYEMASK:MASK<x>:TESt:STATUS?
        ```

    Info:
        - ``MASK<x>`` is the number of the specified mask test (or mask test plot?).
    """


class EyemaskMaskItemTestSampleThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``EYEMASK:MASK<x>:TESt:SAMple:THReshold`` command.

    Description:
        - This command sets or queries the total number of hit violations that will cause a mask
          test failure.

    Usage:
        - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:TESt:SAMple:THReshold?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``EYEMASK:MASK<x>:TESt:SAMple:THReshold?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``EYEMASK:MASK<x>:TESt:SAMple:THReshold value`` command.

    SCPI Syntax:
        ```
        - EYEMASK:MASK<x>:TESt:SAMple:THReshold <NR1>
        - EYEMASK:MASK<x>:TESt:SAMple:THReshold?
        ```

    Info:
        - ``MASK<x>`` is the number of the specified mask test (or mask test plot?).
        - ``<NR1>`` is a positive integer indicating the number of mask hits required to cause a
          fail condition for that mask test.
    """


class EyemaskMaskItemTestSample(SCPICmdRead):
    """The ``EYEMASK:MASK<x>:TESt:SAMple`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:TESt:SAMple?`` query.
        - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:TESt:SAMple?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``MASK<x>`` is the number of the specified mask test (or mask test plot?).

    Properties:
        - ``.threshold``: The ``EYEMASK:MASK<x>:TESt:SAMple:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = EyemaskMaskItemTestSampleThreshold(
            device, f"{self._cmd_syntax}:THReshold"
        )

    @property
    def threshold(self) -> EyemaskMaskItemTestSampleThreshold:
        """Return the ``EYEMASK:MASK<x>:TESt:SAMple:THReshold`` command.

        Description:
            - This command sets or queries the total number of hit violations that will cause a mask
              test failure.

        Usage:
            - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:TESt:SAMple:THReshold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``EYEMASK:MASK<x>:TESt:SAMple:THReshold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``EYEMASK:MASK<x>:TESt:SAMple:THReshold value`` command.

        SCPI Syntax:
            ```
            - EYEMASK:MASK<x>:TESt:SAMple:THReshold <NR1>
            - EYEMASK:MASK<x>:TESt:SAMple:THReshold?
            ```

        Info:
            - ``MASK<x>`` is the number of the specified mask test (or mask test plot?).
            - ``<NR1>`` is a positive integer indicating the number of mask hits required to cause a
              fail condition for that mask test.
        """
        return self._threshold


class EyemaskMaskItemTest(SCPICmdRead):
    """The ``EYEMASK:MASK<x>:TESt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:TESt?`` query.
        - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:TESt?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``MASK<x>`` is the number of the specified mask test (or mask test plot?).

    Properties:
        - ``.sample``: The ``EYEMASK:MASK<x>:TESt:SAMple`` command tree.
        - ``.status``: The ``EYEMASK:MASK<x>:TESt:STATUS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._sample = EyemaskMaskItemTestSample(device, f"{self._cmd_syntax}:SAMple")
        self._status = EyemaskMaskItemTestStatus(device, f"{self._cmd_syntax}:STATUS")

    @property
    def sample(self) -> EyemaskMaskItemTestSample:
        """Return the ``EYEMASK:MASK<x>:TESt:SAMple`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:TESt:SAMple?`` query.
            - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:TESt:SAMple?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``MASK<x>`` is the number of the specified mask test (or mask test plot?).

        Sub-properties:
            - ``.threshold``: The ``EYEMASK:MASK<x>:TESt:SAMple:THReshold`` command.
        """
        return self._sample

    @property
    def status(self) -> EyemaskMaskItemTestStatus:
        """Return the ``EYEMASK:MASK<x>:TESt:STATUS`` command.

        Description:
            - This query-only command returns the mask hit test status.

        Usage:
            - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:TESt:STATUS?`` query.
            - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:TESt:STATUS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - EYEMASK:MASK<x>:TESt:STATUS?
            ```

        Info:
            - ``MASK<x>`` is the number of the specified mask test (or mask test plot?).
        """
        return self._status


class EyemaskMaskItemMaskfile(SCPICmdWrite, SCPICmdRead):
    """The ``EYEMASK:MASK<x>:MASKfile`` command.

    Description:
        - This command sets or queries the current mask definition file name for the specified mask
          test.

    Usage:
        - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:MASKfile?`` query.
        - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:MASKfile?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EYEMASK:MASK<x>:MASKfile value``
          command.

    SCPI Syntax:
        ```
        - EYEMASK:MASK<x>:MASKfile <Qstring>
        - EYEMASK:MASK<x>:MASKfile?
        ```

    Info:
        - ``<x>`` is the number of the specified mask test (or mask test plot?).
        - ``<Qstring>`` is a quoted string that defines the file path that specifies the location of
          the mask file to use, in the format '[<path>]<filename.ext>'. Specifying a path is
          optional. If no path is entered, the instrument will search in the current working
          directory as set in ``FILESYSTEM:CWD``.
    """


class EyemaskMaskItemMaskoffsetHorizontalAutofit(SCPICmdRead):
    """The ``EYEMASK:MASK<x>:MASKOffset:HORizontal:AUTOfit`` command.

    Description:
        - This command returns the mask offset value in the specified mask in seconds. The mask test
          number is specified by <x>

    Usage:
        - Using the ``.query()`` method will send the
          ``EYEMASK:MASK<x>:MASKOffset:HORizontal:AUTOfit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``EYEMASK:MASK<x>:MASKOffset:HORizontal:AUTOfit?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - EYEMASK:MASK<x>:MASKOffset:HORizontal:AUTOfit?
        ```
    """


class EyemaskMaskItemMaskoffsetHorizontal(SCPICmdRead):
    """The ``EYEMASK:MASK<x>:MASKOffset:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:MASKOffset:HORizontal?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``EYEMASK:MASK<x>:MASKOffset:HORizontal?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.autofit``: The ``EYEMASK:MASK<x>:MASKOffset:HORizontal:AUTOfit`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autofit = EyemaskMaskItemMaskoffsetHorizontalAutofit(
            device, f"{self._cmd_syntax}:AUTOfit"
        )

    @property
    def autofit(self) -> EyemaskMaskItemMaskoffsetHorizontalAutofit:
        """Return the ``EYEMASK:MASK<x>:MASKOffset:HORizontal:AUTOfit`` command.

        Description:
            - This command returns the mask offset value in the specified mask in seconds. The mask
              test number is specified by <x>

        Usage:
            - Using the ``.query()`` method will send the
              ``EYEMASK:MASK<x>:MASKOffset:HORizontal:AUTOfit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``EYEMASK:MASK<x>:MASKOffset:HORizontal:AUTOfit?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - EYEMASK:MASK<x>:MASKOffset:HORizontal:AUTOfit?
            ```
        """
        return self._autofit


class EyemaskMaskItemMaskoffset(SCPICmdRead):
    """The ``EYEMASK:MASK<x>:MASKOffset`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:MASKOffset?`` query.
        - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:MASKOffset?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.horizontal``: The ``EYEMASK:MASK<x>:MASKOffset:HORizontal`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._horizontal = EyemaskMaskItemMaskoffsetHorizontal(
            device, f"{self._cmd_syntax}:HORizontal"
        )

    @property
    def horizontal(self) -> EyemaskMaskItemMaskoffsetHorizontal:
        """Return the ``EYEMASK:MASK<x>:MASKOffset:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:MASKOffset:HORizontal?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``EYEMASK:MASK<x>:MASKOffset:HORizontal?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.autofit``: The ``EYEMASK:MASK<x>:MASKOffset:HORizontal:AUTOfit`` command.
        """
        return self._horizontal


class EyemaskMaskItemEnabled(SCPICmdWrite, SCPICmdRead):
    """The ``EYEMASK:MASK<x>:ENAbled`` command.

    Description:
        - This command enables or disables eye mask testing in the specified plot.

    Usage:
        - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:ENAbled?`` query.
        - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:ENAbled?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EYEMASK:MASK<x>:ENAbled value``
          command.

    SCPI Syntax:
        ```
        - EYEMASK:MASK<x>:ENAbled {ON|OFF}
        - EYEMASK:MASK<x>:ENAbled?
        ```

    Info:
        - ``MASK<x>`` is the number of the specified mask test (or mask test plot?).
    """


class EyemaskMaskItemCreator(SCPICmdRead):
    """The ``EYEMASK:MASK<x>:CREATor`` command.

    Description:
        - This query-only command returns the name of the eye diagram plot that created the mask.

    Usage:
        - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:CREATor?`` query.
        - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:CREATor?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - EYEMASK:MASK<x>:CREATor?
        ```

    Info:
        - ``MASK<x>`` is the number of the specified mask test (or mask test plot?).
    """


class EyemaskMaskItemCountSegItemHits(SCPICmdRead):
    """The ``EYEMASK:MASK<x>:COUNt:SEG<y>:HITS`` command.

    Description:
        - This command returns the number of hit violations for the specified segment (area).

    Usage:
        - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:COUNt:SEG<y>:HITS?`` query.
        - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:COUNt:SEG<y>:HITS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - EYEMASK:MASK<x>:COUNt:SEG<y>:HITS?
        ```

    Info:
        - ``MASK<x>`` is the number of the specified mask test (or mask test plot?).
        - ``SEG<y>`` is the number of the mask segment for which to return hit violations data.
    """


class EyemaskMaskItemCountSegItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``EYEMASK:MASK<x>:COUNt:SEG<y>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:COUNt:SEG<y>?`` query.
        - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:COUNt:SEG<y>?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``MASK<x>`` is the number of the specified mask test (or mask test plot?).
        - ``SEG<y>`` is the number of the mask segment for which to return hit violations data.

    Properties:
        - ``.hits``: The ``EYEMASK:MASK<x>:COUNt:SEG<y>:HITS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hits = EyemaskMaskItemCountSegItemHits(device, f"{self._cmd_syntax}:HITS")

    @property
    def hits(self) -> EyemaskMaskItemCountSegItemHits:
        """Return the ``EYEMASK:MASK<x>:COUNt:SEG<y>:HITS`` command.

        Description:
            - This command returns the number of hit violations for the specified segment (area).

        Usage:
            - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:COUNt:SEG<y>:HITS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``EYEMASK:MASK<x>:COUNt:SEG<y>:HITS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - EYEMASK:MASK<x>:COUNt:SEG<y>:HITS?
            ```

        Info:
            - ``MASK<x>`` is the number of the specified mask test (or mask test plot?).
            - ``SEG<y>`` is the number of the mask segment for which to return hit violations data.
        """
        return self._hits


class EyemaskMaskItemCountHits(SCPICmdRead):
    """The ``EYEMASK:MASK<x>:COUNt:HITS`` command.

    Description:
        - This command returns the total number of hit violations for all segments in the specified
          mask test.

    Usage:
        - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:COUNt:HITS?`` query.
        - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:COUNt:HITS?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - EYEMASK:MASK<x>:COUNt:HITS?
        ```

    Info:
        - ``MASK<x>`` is the number of the specified mask test in an eye diagram plot.
    """


class EyemaskMaskItemCount(SCPICmdRead):
    """The ``EYEMASK:MASK<x>:COUNt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:COUNt?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``MASK<x>`` is the number of the specified mask test in an eye diagram plot.

    Properties:
        - ``.hits``: The ``EYEMASK:MASK<x>:COUNt:HITS`` command.
        - ``.seg``: The ``EYEMASK:MASK<x>:COUNt:SEG<y>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hits = EyemaskMaskItemCountHits(device, f"{self._cmd_syntax}:HITS")
        self._seg: Dict[int, EyemaskMaskItemCountSegItem] = DefaultDictPassKeyToFactory(
            lambda x: EyemaskMaskItemCountSegItem(device, f"{self._cmd_syntax}:SEG{x}")
        )

    @property
    def hits(self) -> EyemaskMaskItemCountHits:
        """Return the ``EYEMASK:MASK<x>:COUNt:HITS`` command.

        Description:
            - This command returns the total number of hit violations for all segments in the
              specified mask test.

        Usage:
            - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:COUNt:HITS?`` query.
            - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:COUNt:HITS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - EYEMASK:MASK<x>:COUNt:HITS?
            ```

        Info:
            - ``MASK<x>`` is the number of the specified mask test in an eye diagram plot.
        """
        return self._hits

    @property
    def seg(self) -> Dict[int, EyemaskMaskItemCountSegItem]:
        """Return the ``EYEMASK:MASK<x>:COUNt:SEG<y>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:COUNt:SEG<y>?`` query.
            - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:COUNt:SEG<y>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``MASK<x>`` is the number of the specified mask test (or mask test plot?).
            - ``SEG<y>`` is the number of the mask segment for which to return hit violations data.

        Sub-properties:
            - ``.hits``: The ``EYEMASK:MASK<x>:COUNt:SEG<y>:HITS`` command.
        """
        return self._seg


class EyemaskMaskItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``EYEMASK:MASK<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``MASK<x>`` is the number of the specified mask test in an eye diagram plot.

    Properties:
        - ``.count``: The ``EYEMASK:MASK<x>:COUNt`` command tree.
        - ``.creator``: The ``EYEMASK:MASK<x>:CREATor`` command.
        - ``.enabled``: The ``EYEMASK:MASK<x>:ENAbled`` command.
        - ``.maskoffset``: The ``EYEMASK:MASK<x>:MASKOffset`` command tree.
        - ``.maskfile``: The ``EYEMASK:MASK<x>:MASKfile`` command.
        - ``.test``: The ``EYEMASK:MASK<x>:TESt`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._count = EyemaskMaskItemCount(device, f"{self._cmd_syntax}:COUNt")
        self._creator = EyemaskMaskItemCreator(device, f"{self._cmd_syntax}:CREATor")
        self._enabled = EyemaskMaskItemEnabled(device, f"{self._cmd_syntax}:ENAbled")
        self._maskoffset = EyemaskMaskItemMaskoffset(device, f"{self._cmd_syntax}:MASKOffset")
        self._maskfile = EyemaskMaskItemMaskfile(device, f"{self._cmd_syntax}:MASKfile")
        self._test = EyemaskMaskItemTest(device, f"{self._cmd_syntax}:TESt")

    @property
    def count(self) -> EyemaskMaskItemCount:
        """Return the ``EYEMASK:MASK<x>:COUNt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:COUNt?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``MASK<x>`` is the number of the specified mask test in an eye diagram plot.

        Sub-properties:
            - ``.hits``: The ``EYEMASK:MASK<x>:COUNt:HITS`` command.
            - ``.seg``: The ``EYEMASK:MASK<x>:COUNt:SEG<y>`` command tree.
        """
        return self._count

    @property
    def creator(self) -> EyemaskMaskItemCreator:
        """Return the ``EYEMASK:MASK<x>:CREATor`` command.

        Description:
            - This query-only command returns the name of the eye diagram plot that created the
              mask.

        Usage:
            - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:CREATor?`` query.
            - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:CREATor?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - EYEMASK:MASK<x>:CREATor?
            ```

        Info:
            - ``MASK<x>`` is the number of the specified mask test (or mask test plot?).
        """
        return self._creator

    @property
    def enabled(self) -> EyemaskMaskItemEnabled:
        """Return the ``EYEMASK:MASK<x>:ENAbled`` command.

        Description:
            - This command enables or disables eye mask testing in the specified plot.

        Usage:
            - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:ENAbled?`` query.
            - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:ENAbled?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EYEMASK:MASK<x>:ENAbled value``
              command.

        SCPI Syntax:
            ```
            - EYEMASK:MASK<x>:ENAbled {ON|OFF}
            - EYEMASK:MASK<x>:ENAbled?
            ```

        Info:
            - ``MASK<x>`` is the number of the specified mask test (or mask test plot?).
        """
        return self._enabled

    @property
    def maskoffset(self) -> EyemaskMaskItemMaskoffset:
        """Return the ``EYEMASK:MASK<x>:MASKOffset`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:MASKOffset?`` query.
            - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:MASKOffset?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.horizontal``: The ``EYEMASK:MASK<x>:MASKOffset:HORizontal`` command tree.
        """
        return self._maskoffset

    @property
    def maskfile(self) -> EyemaskMaskItemMaskfile:
        """Return the ``EYEMASK:MASK<x>:MASKfile`` command.

        Description:
            - This command sets or queries the current mask definition file name for the specified
              mask test.

        Usage:
            - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:MASKfile?`` query.
            - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:MASKfile?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EYEMASK:MASK<x>:MASKfile value``
              command.

        SCPI Syntax:
            ```
            - EYEMASK:MASK<x>:MASKfile <Qstring>
            - EYEMASK:MASK<x>:MASKfile?
            ```

        Info:
            - ``<x>`` is the number of the specified mask test (or mask test plot?).
            - ``<Qstring>`` is a quoted string that defines the file path that specifies the
              location of the mask file to use, in the format '[<path>]<filename.ext>'. Specifying a
              path is optional. If no path is entered, the instrument will search in the current
              working directory as set in ``FILESYSTEM:CWD``.
        """
        return self._maskfile

    @property
    def test(self) -> EyemaskMaskItemTest:
        """Return the ``EYEMASK:MASK<x>:TESt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>:TESt?`` query.
            - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>:TESt?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``MASK<x>`` is the number of the specified mask test (or mask test plot?).

        Sub-properties:
            - ``.sample``: The ``EYEMASK:MASK<x>:TESt:SAMple`` command tree.
            - ``.status``: The ``EYEMASK:MASK<x>:TESt:STATUS`` command.
        """
        return self._test


class Eyemask(SCPICmdRead):
    """The ``EYEMASK`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``EYEMASK?`` query.
        - Using the ``.verify(value)`` method will send the ``EYEMASK?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mask``: The ``EYEMASK:MASK<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "EYEMASK") -> None:
        super().__init__(device, cmd_syntax)
        self._mask: Dict[int, EyemaskMaskItem] = DefaultDictPassKeyToFactory(
            lambda x: EyemaskMaskItem(device, f"{self._cmd_syntax}:MASK{x}")
        )

    @property
    def mask(self) -> Dict[int, EyemaskMaskItem]:
        """Return the ``EYEMASK:MASK<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``EYEMASK:MASK<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``EYEMASK:MASK<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``MASK<x>`` is the number of the specified mask test in an eye diagram plot.

        Sub-properties:
            - ``.count``: The ``EYEMASK:MASK<x>:COUNt`` command tree.
            - ``.creator``: The ``EYEMASK:MASK<x>:CREATor`` command.
            - ``.enabled``: The ``EYEMASK:MASK<x>:ENAbled`` command.
            - ``.maskoffset``: The ``EYEMASK:MASK<x>:MASKOffset`` command tree.
            - ``.maskfile``: The ``EYEMASK:MASK<x>:MASKfile`` command.
            - ``.test``: The ``EYEMASK:MASK<x>:TESt`` command tree.
        """
        return self._mask
