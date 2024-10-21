"""The mark commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MARK {NEXT|PREVious}
    - MARK:CREATE {CH<x>|MATH<x>|REF<x>|COLUMN}
    - MARK:DELEte {CH<x>|MATH<x>|SELECTED|REF<x>|ALL|COLUMN}
    - MARK:FREE?
    - MARK:SELECTED:END?
    - MARK:SELECTED:FOCUS?
    - MARK:SELECTED:LABel <QString>
    - MARK:SELECTED:LABel?
    - MARK:SELECTED:MARKSINCOLumn?
    - MARK:SELECTED:OWNer?
    - MARK:SELECTED:SOUrce?
    - MARK:SELECTED:STARt?
    - MARK:SELECTED:STATE {ON|OFF|<NR1>}
    - MARK:SELECTED:STATE?
    - MARK:SELECTED:ZOOm:POSition?
    - MARK:SELECTED:ZOOm:SCAle?
    - MARK:TOTal?
    - MARK?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MarkTotal(SCPICmdRead):
    """The ``MARK:TOTal`` command.

    Description:
        - Returns how many marks are currently in use. There can be a total of 1,024 marks returned.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:TOTal?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:TOTal?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARK:TOTal?
        ```
    """


class MarkSelectedZoomScale(SCPICmdRead):
    """The ``MARK:SELECTED:ZOOm:SCAle`` command.

    Description:
        - This query-only command returns the scale of the selected mark of the zoom overview
          window. The returned value might be < 0 (for example from Search), which means that the
          zoom scale will not be changed when Next or Prev makes this the selected mark.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELECTED:ZOOm:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:ZOOm:SCAle?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARK:SELECTED:ZOOm:SCAle?
        ```
    """


class MarkSelectedZoomPosition(SCPICmdRead):
    """The ``MARK:SELECTED:ZOOm:POSition`` command.

    Description:
        - This query-only command returns the position of the selected mark, of the zoom overview
          window. If the return value is less than zero then the zoom scale will not be changed when
          Next or Prev makes this the selected mark.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELECTED:ZOOm:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:ZOOm:POSition?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARK:SELECTED:ZOOm:POSition?
        ```
    """


class MarkSelectedZoom(SCPICmdRead):
    """The ``MARK:SELECTED:ZOOm`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELECTED:ZOOm?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:ZOOm?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``MARK:SELECTED:ZOOm:POSition`` command.
        - ``.scale``: The ``MARK:SELECTED:ZOOm:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = MarkSelectedZoomPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = MarkSelectedZoomScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> MarkSelectedZoomPosition:
        """Return the ``MARK:SELECTED:ZOOm:POSition`` command.

        Description:
            - This query-only command returns the position of the selected mark, of the zoom
              overview window. If the return value is less than zero then the zoom scale will not be
              changed when Next or Prev makes this the selected mark.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELECTED:ZOOm:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:ZOOm:POSition?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARK:SELECTED:ZOOm:POSition?
            ```
        """
        return self._position

    @property
    def scale(self) -> MarkSelectedZoomScale:
        """Return the ``MARK:SELECTED:ZOOm:SCAle`` command.

        Description:
            - This query-only command returns the scale of the selected mark of the zoom overview
              window. The returned value might be < 0 (for example from Search), which means that
              the zoom scale will not be changed when Next or Prev makes this the selected mark.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELECTED:ZOOm:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:ZOOm:SCAle?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARK:SELECTED:ZOOm:SCAle?
            ```
        """
        return self._scale


class MarkSelectedState(SCPICmdWrite, SCPICmdRead):
    """The ``MARK:SELECTED:STATE`` command.

    Description:
        - This command sets or queries the on or off state of the selected mark. The selected mark
          is at or near the center of the display. If you push the Set/Clear button, this mark will
          disappear.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELECTED:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:STATE?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MARK:SELECTED:STATE value`` command.

    SCPI Syntax:
        ```
        - MARK:SELECTED:STATE {ON|OFF|<NR1>}
        - MARK:SELECTED:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 disables the selected mark; any other value enables the selected mark. For
          queries, a 0 is returned if the selected mark state is off; a 1 is returned if the
          selected mark state is on.
        - ``OFF`` argument disables selected mark.
        - ``ON`` argument enables the selected mark.
    """


class MarkSelectedStart(SCPICmdRead):
    """The ``MARK:SELECTED:STARt`` command.

    Description:
        - This query-only command returns the starting point of the selected mark, 0 to 100% of the
          waveform.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELECTED:STARt?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:STARt?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARK:SELECTED:STARt?
        ```
    """


class MarkSelectedSource(SCPICmdRead):
    """The ``MARK:SELECTED:SOUrce`` command.

    Description:
        - This query-only command returns the source waveform for the selected mark.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELECTED:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARK:SELECTED:SOUrce?
        ```
    """


class MarkSelectedOwner(SCPICmdRead):
    """The ``MARK:SELECTED:OWNer`` command.

    Description:
        - This query-only command returns the owner of the selected mark.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELECTED:OWNer?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:OWNer?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARK:SELECTED:OWNer?
        ```
    """


class MarkSelectedMarksincolumn(SCPICmdRead):
    """The ``MARK:SELECTED:MARKSINCOLumn`` command.

    Description:
        - This query-only command returns the number of marks in the current zoom pixel column.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELECTED:MARKSINCOLumn?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:MARKSINCOLumn?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARK:SELECTED:MARKSINCOLumn?
        ```

    Info:
        - ``MARK:SELECTED:MARKSINCOLUMN?`` might return ``:MARK:SELECTED:MARKSINCOLUMN 1``,
          indicating there is 1 mark in the pixel column.
    """


class MarkSelectedLabel(SCPICmdWrite, SCPICmdRead):
    """The ``MARK:SELECTED:LABel`` command.

    Description:
        - This command sets or queries the label for the selected mark.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELECTED:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:LABel?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MARK:SELECTED:LABel value`` command.

    SCPI Syntax:
        ```
        - MARK:SELECTED:LABel <QString>
        - MARK:SELECTED:LABel?
        ```

    Info:
        - ``<QString>`` is the quoted string label for the mark.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MarkSelectedFocus(SCPICmdRead):
    """The ``MARK:SELECTED:FOCUS`` command.

    Description:
        - This query-only command returns the focus of the selected mark, 0 to 100% of the waveform.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELECTED:FOCUS?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:FOCUS?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARK:SELECTED:FOCUS?
        ```
    """


class MarkSelectedEnd(SCPICmdRead):
    """The ``MARK:SELECTED:END`` command.

    Description:
        - This query-only command returns the end of the selected mark, 0 to 100% of the waveform.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELECTED:END?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:END?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARK:SELECTED:END?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class MarkSelected(SCPICmdRead):
    """The ``MARK:SELECTED`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELECTED?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELECTED?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.end``: The ``MARK:SELECTED:END`` command.
        - ``.focus``: The ``MARK:SELECTED:FOCUS`` command.
        - ``.label``: The ``MARK:SELECTED:LABel`` command.
        - ``.marksincolumn``: The ``MARK:SELECTED:MARKSINCOLumn`` command.
        - ``.owner``: The ``MARK:SELECTED:OWNer`` command.
        - ``.source``: The ``MARK:SELECTED:SOUrce`` command.
        - ``.start``: The ``MARK:SELECTED:STARt`` command.
        - ``.state``: The ``MARK:SELECTED:STATE`` command.
        - ``.zoom``: The ``MARK:SELECTED:ZOOm`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._end = MarkSelectedEnd(device, f"{self._cmd_syntax}:END")
        self._focus = MarkSelectedFocus(device, f"{self._cmd_syntax}:FOCUS")
        self._label = MarkSelectedLabel(device, f"{self._cmd_syntax}:LABel")
        self._marksincolumn = MarkSelectedMarksincolumn(device, f"{self._cmd_syntax}:MARKSINCOLumn")
        self._owner = MarkSelectedOwner(device, f"{self._cmd_syntax}:OWNer")
        self._source = MarkSelectedSource(device, f"{self._cmd_syntax}:SOUrce")
        self._start = MarkSelectedStart(device, f"{self._cmd_syntax}:STARt")
        self._state = MarkSelectedState(device, f"{self._cmd_syntax}:STATE")
        self._zoom = MarkSelectedZoom(device, f"{self._cmd_syntax}:ZOOm")

    @property
    def end(self) -> MarkSelectedEnd:
        """Return the ``MARK:SELECTED:END`` command.

        Description:
            - This query-only command returns the end of the selected mark, 0 to 100% of the
              waveform.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELECTED:END?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:END?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARK:SELECTED:END?
            ```
        """
        return self._end

    @property
    def focus(self) -> MarkSelectedFocus:
        """Return the ``MARK:SELECTED:FOCUS`` command.

        Description:
            - This query-only command returns the focus of the selected mark, 0 to 100% of the
              waveform.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELECTED:FOCUS?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:FOCUS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARK:SELECTED:FOCUS?
            ```
        """
        return self._focus

    @property
    def label(self) -> MarkSelectedLabel:
        """Return the ``MARK:SELECTED:LABel`` command.

        Description:
            - This command sets or queries the label for the selected mark.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELECTED:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:LABel?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MARK:SELECTED:LABel value``
              command.

        SCPI Syntax:
            ```
            - MARK:SELECTED:LABel <QString>
            - MARK:SELECTED:LABel?
            ```

        Info:
            - ``<QString>`` is the quoted string label for the mark.
        """
        return self._label

    @property
    def marksincolumn(self) -> MarkSelectedMarksincolumn:
        """Return the ``MARK:SELECTED:MARKSINCOLumn`` command.

        Description:
            - This query-only command returns the number of marks in the current zoom pixel column.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELECTED:MARKSINCOLumn?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:MARKSINCOLumn?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARK:SELECTED:MARKSINCOLumn?
            ```

        Info:
            - ``MARK:SELECTED:MARKSINCOLUMN?`` might return ``:MARK:SELECTED:MARKSINCOLUMN 1``,
              indicating there is 1 mark in the pixel column.
        """
        return self._marksincolumn

    @property
    def owner(self) -> MarkSelectedOwner:
        """Return the ``MARK:SELECTED:OWNer`` command.

        Description:
            - This query-only command returns the owner of the selected mark.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELECTED:OWNer?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:OWNer?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARK:SELECTED:OWNer?
            ```
        """
        return self._owner

    @property
    def source(self) -> MarkSelectedSource:
        """Return the ``MARK:SELECTED:SOUrce`` command.

        Description:
            - This query-only command returns the source waveform for the selected mark.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELECTED:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARK:SELECTED:SOUrce?
            ```
        """
        return self._source

    @property
    def start(self) -> MarkSelectedStart:
        """Return the ``MARK:SELECTED:STARt`` command.

        Description:
            - This query-only command returns the starting point of the selected mark, 0 to 100% of
              the waveform.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELECTED:STARt?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:STARt?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARK:SELECTED:STARt?
            ```
        """
        return self._start

    @property
    def state(self) -> MarkSelectedState:
        """Return the ``MARK:SELECTED:STATE`` command.

        Description:
            - This command sets or queries the on or off state of the selected mark. The selected
              mark is at or near the center of the display. If you push the Set/Clear button, this
              mark will disappear.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELECTED:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MARK:SELECTED:STATE value``
              command.

        SCPI Syntax:
            ```
            - MARK:SELECTED:STATE {ON|OFF|<NR1>}
            - MARK:SELECTED:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 disables the selected mark; any other value enables the selected mark.
              For queries, a 0 is returned if the selected mark state is off; a 1 is returned if the
              selected mark state is on.
            - ``OFF`` argument disables selected mark.
            - ``ON`` argument enables the selected mark.
        """
        return self._state

    @property
    def zoom(self) -> MarkSelectedZoom:
        """Return the ``MARK:SELECTED:ZOOm`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELECTED:ZOOm?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELECTED:ZOOm?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``MARK:SELECTED:ZOOm:POSition`` command.
            - ``.scale``: The ``MARK:SELECTED:ZOOm:SCAle`` command.
        """
        return self._zoom


class MarkFree(SCPICmdRead):
    """The ``MARK:FREE`` command.

    Description:
        - Returns how many marks are available for use. There can be a total of 1,024 marks
          returned.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:FREE?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:FREE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARK:FREE?
        ```
    """


class MarkDelete(SCPICmdWrite):
    """The ``MARK:DELEte`` command.

    Description:
        - This command deletes a mark on a particular waveform, all waveforms in a column, the
          selected mark, or all marks.

    Usage:
        - Using the ``.write(value)`` method will send the ``MARK:DELEte value`` command.

    SCPI Syntax:
        ```
        - MARK:DELEte {CH<x>|MATH<x>|SELECTED|REF<x>|ALL|COLUMN}
        ```

    Info:
        - ``CH<x>`` deletes the mark on a channel waveform, where <x> is the channel number and can
          be 1, 2, 3, or 4.
        - ``MATH<x>`` deletes the mark on the math waveform, where <x> is the channel number and can
          be 1, 2, 3, or 4.
        - ``SELECTED`` deletes the mark on the selected waveform.
        - ``REF<x>`` deletes the mark on a reference waveform, where <x> is the reference waveform
          number and can be 1, 2, 3, or 4.
        - ``ALL`` deletes all marks on all waveforms.
        - ``COLUMN`` deletes marks on all waveforms in the current zoom pixel column.
    """


class MarkCreate(SCPICmdWrite):
    """The ``MARK:CREATE`` command.

    Description:
        - This command creates a mark on a specified waveform or all waveforms in a column.

    Usage:
        - Using the ``.write(value)`` method will send the ``MARK:CREATE value`` command.

    SCPI Syntax:
        ```
        - MARK:CREATE {CH<x>|MATH<x>|REF<x>|COLUMN}
        ```

    Info:
        - ``CH<x>`` creates the mark on a channel waveform, where <x> is the channel number and can
          be 1, 2, 3, or 4.
        - ``MATH<x>`` creates the mark on the math waveform, where <x> is the channel number and can
          be 1, 2, 3, or 4.
        - ``REF<x>`` creates the mark on a reference waveform, where <x> is the reference waveform
          number can be 1, 2, 3, or 4.
        - ``COLUMN`` creates marks on all waveforms in the current zoom pixel column.
    """


class Mark(SCPICmdWrite, SCPICmdRead):
    """The ``MARK`` command.

    Description:
        - Moves to the next or previous reference mark on the waveform. Returns the current mark
          position.

    Usage:
        - Using the ``.query()`` method will send the ``MARK?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MARK value`` command.

    SCPI Syntax:
        ```
        - MARK {NEXT|PREVious}
        - MARK?
        ```

    Info:
        - ``NEXT`` moves to the next reference mark on the right.
        - ``PREVious`` moves to the next reference mark on the left.

    Properties:
        - ``.create``: The ``MARK:CREATE`` command.
        - ``.delete``: The ``MARK:DELEte`` command.
        - ``.free``: The ``MARK:FREE`` command.
        - ``.selected``: The ``MARK:SELECTED`` command tree.
        - ``.total``: The ``MARK:TOTal`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MARK") -> None:
        super().__init__(device, cmd_syntax)
        self._create = MarkCreate(device, f"{self._cmd_syntax}:CREATE")
        self._delete = MarkDelete(device, f"{self._cmd_syntax}:DELEte")
        self._free = MarkFree(device, f"{self._cmd_syntax}:FREE")
        self._selected = MarkSelected(device, f"{self._cmd_syntax}:SELECTED")
        self._total = MarkTotal(device, f"{self._cmd_syntax}:TOTal")

    @property
    def create(self) -> MarkCreate:
        """Return the ``MARK:CREATE`` command.

        Description:
            - This command creates a mark on a specified waveform or all waveforms in a column.

        Usage:
            - Using the ``.write(value)`` method will send the ``MARK:CREATE value`` command.

        SCPI Syntax:
            ```
            - MARK:CREATE {CH<x>|MATH<x>|REF<x>|COLUMN}
            ```

        Info:
            - ``CH<x>`` creates the mark on a channel waveform, where <x> is the channel number and
              can be 1, 2, 3, or 4.
            - ``MATH<x>`` creates the mark on the math waveform, where <x> is the channel number and
              can be 1, 2, 3, or 4.
            - ``REF<x>`` creates the mark on a reference waveform, where <x> is the reference
              waveform number can be 1, 2, 3, or 4.
            - ``COLUMN`` creates marks on all waveforms in the current zoom pixel column.
        """
        return self._create

    @property
    def delete(self) -> MarkDelete:
        """Return the ``MARK:DELEte`` command.

        Description:
            - This command deletes a mark on a particular waveform, all waveforms in a column, the
              selected mark, or all marks.

        Usage:
            - Using the ``.write(value)`` method will send the ``MARK:DELEte value`` command.

        SCPI Syntax:
            ```
            - MARK:DELEte {CH<x>|MATH<x>|SELECTED|REF<x>|ALL|COLUMN}
            ```

        Info:
            - ``CH<x>`` deletes the mark on a channel waveform, where <x> is the channel number and
              can be 1, 2, 3, or 4.
            - ``MATH<x>`` deletes the mark on the math waveform, where <x> is the channel number and
              can be 1, 2, 3, or 4.
            - ``SELECTED`` deletes the mark on the selected waveform.
            - ``REF<x>`` deletes the mark on a reference waveform, where <x> is the reference
              waveform number and can be 1, 2, 3, or 4.
            - ``ALL`` deletes all marks on all waveforms.
            - ``COLUMN`` deletes marks on all waveforms in the current zoom pixel column.
        """
        return self._delete

    @property
    def free(self) -> MarkFree:
        """Return the ``MARK:FREE`` command.

        Description:
            - Returns how many marks are available for use. There can be a total of 1,024 marks
              returned.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:FREE?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:FREE?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARK:FREE?
            ```
        """
        return self._free

    @property
    def selected(self) -> MarkSelected:
        """Return the ``MARK:SELECTED`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELECTED?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELECTED?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.end``: The ``MARK:SELECTED:END`` command.
            - ``.focus``: The ``MARK:SELECTED:FOCUS`` command.
            - ``.label``: The ``MARK:SELECTED:LABel`` command.
            - ``.marksincolumn``: The ``MARK:SELECTED:MARKSINCOLumn`` command.
            - ``.owner``: The ``MARK:SELECTED:OWNer`` command.
            - ``.source``: The ``MARK:SELECTED:SOUrce`` command.
            - ``.start``: The ``MARK:SELECTED:STARt`` command.
            - ``.state``: The ``MARK:SELECTED:STATE`` command.
            - ``.zoom``: The ``MARK:SELECTED:ZOOm`` command tree.
        """
        return self._selected

    @property
    def total(self) -> MarkTotal:
        """Return the ``MARK:TOTal`` command.

        Description:
            - Returns how many marks are currently in use. There can be a total of 1,024 marks
              returned.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:TOTal?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:TOTal?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARK:TOTal?
            ```
        """
        return self._total
