"""The mark commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MARK {NEXT|PREVious}
    - MARK:CREATE {CH<x>|MATH|B<x>|REF<x>|COLUMN|DIGItal}
    - MARK:DELEte {CH<x>|MATH|B<x>|REF<x>|COLUMN|DIGItal}
    - MARK:FREE?
    - MARK:SELected:END?
    - MARK:SELected:FOCUS?
    - MARK:SELected:MARKSINCOLumn?
    - MARK:SELected:OWNer?
    - MARK:SELected:SOURCE?
    - MARK:SELected:STARt?
    - MARK:SELected:STATe?
    - MARK:SELected:ZOOm:POSition?
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


class MarkSelectedZoomPosition(SCPICmdRead):
    """The ``MARK:SELected:ZOOm:POSition`` command.

    Description:
        - Returns the position of the selected mark, 0 to 100% of the zoom overview window.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELected:ZOOm:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELected:ZOOm:POSition?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARK:SELected:ZOOm:POSition?
        ```
    """


class MarkSelectedZoom(SCPICmdRead):
    """The ``MARK:SELected:ZOOm`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELected:ZOOm?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELected:ZOOm?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``MARK:SELected:ZOOm:POSition`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = MarkSelectedZoomPosition(device, f"{self._cmd_syntax}:POSition")

    @property
    def position(self) -> MarkSelectedZoomPosition:
        """Return the ``MARK:SELected:ZOOm:POSition`` command.

        Description:
            - Returns the position of the selected mark, 0 to 100% of the zoom overview window.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELected:ZOOm:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELected:ZOOm:POSition?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARK:SELected:ZOOm:POSition?
            ```
        """
        return self._position


class MarkSelectedState(SCPICmdRead):
    """The ``MARK:SELected:STATe`` command.

    Description:
        - Returns the on or off state of the selected mark. The selected mark is at or near the
          center of the screen. If you press the front-panel Set/Clear button, this mark will
          disappear.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELected:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELected:STATe?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARK:SELected:STATe?
        ```
    """


class MarkSelectedStart(SCPICmdRead):
    """The ``MARK:SELected:STARt`` command.

    Description:
        - Returns the starting point of the selected mark, 0 to 100% of the waveform.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELected:STARt?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELected:STARt?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARK:SELected:STARt?
        ```
    """


class MarkSelectedSource(SCPICmdRead):
    """The ``MARK:SELected:SOURCE`` command.

    Description:
        - Returns the source waveform for the selected mark.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELected:SOURCE?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELected:SOURCE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARK:SELected:SOURCE?
        ```
    """


class MarkSelectedOwner(SCPICmdRead):
    """The ``MARK:SELected:OWNer`` command.

    Description:
        - Returns the owner of the selected mark.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELected:OWNer?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELected:OWNer?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARK:SELected:OWNer?
        ```
    """


class MarkSelectedMarksincolumn(SCPICmdRead):
    """The ``MARK:SELected:MARKSINCOLumn`` command.

    Description:
        - Returns the number of marks in the current zoom pixel column.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELected:MARKSINCOLumn?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELected:MARKSINCOLumn?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARK:SELected:MARKSINCOLumn?
        ```
    """


class MarkSelectedFocus(SCPICmdRead):
    """The ``MARK:SELected:FOCUS`` command.

    Description:
        - Returns the focus of the selected mark, 0 to 100% of the waveform.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELected:FOCUS?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELected:FOCUS?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARK:SELected:FOCUS?
        ```
    """


class MarkSelectedEnd(SCPICmdRead):
    """The ``MARK:SELected:END`` command.

    Description:
        - Returns the end of the selected mark, 0 to 100% of the waveform.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELected:END?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELected:END?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARK:SELected:END?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class MarkSelected(SCPICmdRead):
    """The ``MARK:SELected`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MARK:SELected?`` query.
        - Using the ``.verify(value)`` method will send the ``MARK:SELected?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.end``: The ``MARK:SELected:END`` command.
        - ``.focus``: The ``MARK:SELected:FOCUS`` command.
        - ``.marksincolumn``: The ``MARK:SELected:MARKSINCOLumn`` command.
        - ``.owner``: The ``MARK:SELected:OWNer`` command.
        - ``.source``: The ``MARK:SELected:SOURCE`` command.
        - ``.start``: The ``MARK:SELected:STARt`` command.
        - ``.state``: The ``MARK:SELected:STATe`` command.
        - ``.zoom``: The ``MARK:SELected:ZOOm`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._end = MarkSelectedEnd(device, f"{self._cmd_syntax}:END")
        self._focus = MarkSelectedFocus(device, f"{self._cmd_syntax}:FOCUS")
        self._marksincolumn = MarkSelectedMarksincolumn(device, f"{self._cmd_syntax}:MARKSINCOLumn")
        self._owner = MarkSelectedOwner(device, f"{self._cmd_syntax}:OWNer")
        self._source = MarkSelectedSource(device, f"{self._cmd_syntax}:SOURCE")
        self._start = MarkSelectedStart(device, f"{self._cmd_syntax}:STARt")
        self._state = MarkSelectedState(device, f"{self._cmd_syntax}:STATe")
        self._zoom = MarkSelectedZoom(device, f"{self._cmd_syntax}:ZOOm")

    @property
    def end(self) -> MarkSelectedEnd:
        """Return the ``MARK:SELected:END`` command.

        Description:
            - Returns the end of the selected mark, 0 to 100% of the waveform.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELected:END?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELected:END?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARK:SELected:END?
            ```
        """
        return self._end

    @property
    def focus(self) -> MarkSelectedFocus:
        """Return the ``MARK:SELected:FOCUS`` command.

        Description:
            - Returns the focus of the selected mark, 0 to 100% of the waveform.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELected:FOCUS?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELected:FOCUS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARK:SELected:FOCUS?
            ```
        """
        return self._focus

    @property
    def marksincolumn(self) -> MarkSelectedMarksincolumn:
        """Return the ``MARK:SELected:MARKSINCOLumn`` command.

        Description:
            - Returns the number of marks in the current zoom pixel column.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELected:MARKSINCOLumn?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELected:MARKSINCOLumn?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARK:SELected:MARKSINCOLumn?
            ```
        """
        return self._marksincolumn

    @property
    def owner(self) -> MarkSelectedOwner:
        """Return the ``MARK:SELected:OWNer`` command.

        Description:
            - Returns the owner of the selected mark.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELected:OWNer?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELected:OWNer?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARK:SELected:OWNer?
            ```
        """
        return self._owner

    @property
    def source(self) -> MarkSelectedSource:
        """Return the ``MARK:SELected:SOURCE`` command.

        Description:
            - Returns the source waveform for the selected mark.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELected:SOURCE?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELected:SOURCE?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARK:SELected:SOURCE?
            ```
        """
        return self._source

    @property
    def start(self) -> MarkSelectedStart:
        """Return the ``MARK:SELected:STARt`` command.

        Description:
            - Returns the starting point of the selected mark, 0 to 100% of the waveform.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELected:STARt?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELected:STARt?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARK:SELected:STARt?
            ```
        """
        return self._start

    @property
    def state(self) -> MarkSelectedState:
        """Return the ``MARK:SELected:STATe`` command.

        Description:
            - Returns the on or off state of the selected mark. The selected mark is at or near the
              center of the screen. If you press the front-panel Set/Clear button, this mark will
              disappear.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELected:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELected:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARK:SELected:STATe?
            ```
        """
        return self._state

    @property
    def zoom(self) -> MarkSelectedZoom:
        """Return the ``MARK:SELected:ZOOm`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELected:ZOOm?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELected:ZOOm?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``MARK:SELected:ZOOm:POSition`` command.
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
        - Deletes a mark on a particular waveform, all waveforms in a column, the selected mark, or
          all marks.

    Usage:
        - Using the ``.write(value)`` method will send the ``MARK:DELEte value`` command.

    SCPI Syntax:
        ```
        - MARK:DELEte {CH<x>|MATH|B<x>|REF<x>|COLUMN|DIGItal}
        ```

    Info:
        - ``CH<x>`` deletes the mark on a channel waveform, where <x> is the channel number.
        - ``MATH`` deletes the mark on the math waveform.
        - ``B<x>`` deletes the mark on a bus waveform, where <x> is the bus number.
        - ``REF<x>`` deletes the mark on a reference waveform, where <x> is the reference waveform
          number.
        - ``COLUMN`` deletes marks on all waveforms in the current zoom pixel column.
        - ``DIGItal`` deletes all marks on all digital channels.
    """


class MarkCreate(SCPICmdWrite):
    """The ``MARK:CREATE`` command.

    Description:
        - Creates a mark on a specified waveform or all waveforms in a column.

    Usage:
        - Using the ``.write(value)`` method will send the ``MARK:CREATE value`` command.

    SCPI Syntax:
        ```
        - MARK:CREATE {CH<x>|MATH|B<x>|REF<x>|COLUMN|DIGItal}
        ```

    Info:
        - ``CH<x>`` creates the mark on a channel waveform, where <x> is the channel number.
        - ``MATH`` creates the mark on the math waveform.
        - ``B<x>`` creates the mark on a bus waveform, where <x> is the bus number.
        - ``REF<x>`` creates the mark on a reference waveform, where <x> is the reference waveform
          number.
        - ``COLUMN`` creates marks on all waveforms in the current zoom pixel column.
        - ``DIGItal`` creates marks on a digital waveform. (An error will result if no digital
          channel is turned on.).
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
        - ``.selected``: The ``MARK:SELected`` command tree.
        - ``.total``: The ``MARK:TOTal`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MARK") -> None:
        super().__init__(device, cmd_syntax)
        self._create = MarkCreate(device, f"{self._cmd_syntax}:CREATE")
        self._delete = MarkDelete(device, f"{self._cmd_syntax}:DELEte")
        self._free = MarkFree(device, f"{self._cmd_syntax}:FREE")
        self._selected = MarkSelected(device, f"{self._cmd_syntax}:SELected")
        self._total = MarkTotal(device, f"{self._cmd_syntax}:TOTal")

    @property
    def create(self) -> MarkCreate:
        """Return the ``MARK:CREATE`` command.

        Description:
            - Creates a mark on a specified waveform or all waveforms in a column.

        Usage:
            - Using the ``.write(value)`` method will send the ``MARK:CREATE value`` command.

        SCPI Syntax:
            ```
            - MARK:CREATE {CH<x>|MATH|B<x>|REF<x>|COLUMN|DIGItal}
            ```

        Info:
            - ``CH<x>`` creates the mark on a channel waveform, where <x> is the channel number.
            - ``MATH`` creates the mark on the math waveform.
            - ``B<x>`` creates the mark on a bus waveform, where <x> is the bus number.
            - ``REF<x>`` creates the mark on a reference waveform, where <x> is the reference
              waveform number.
            - ``COLUMN`` creates marks on all waveforms in the current zoom pixel column.
            - ``DIGItal`` creates marks on a digital waveform. (An error will result if no digital
              channel is turned on.).
        """
        return self._create

    @property
    def delete(self) -> MarkDelete:
        """Return the ``MARK:DELEte`` command.

        Description:
            - Deletes a mark on a particular waveform, all waveforms in a column, the selected mark,
              or all marks.

        Usage:
            - Using the ``.write(value)`` method will send the ``MARK:DELEte value`` command.

        SCPI Syntax:
            ```
            - MARK:DELEte {CH<x>|MATH|B<x>|REF<x>|COLUMN|DIGItal}
            ```

        Info:
            - ``CH<x>`` deletes the mark on a channel waveform, where <x> is the channel number.
            - ``MATH`` deletes the mark on the math waveform.
            - ``B<x>`` deletes the mark on a bus waveform, where <x> is the bus number.
            - ``REF<x>`` deletes the mark on a reference waveform, where <x> is the reference
              waveform number.
            - ``COLUMN`` deletes marks on all waveforms in the current zoom pixel column.
            - ``DIGItal`` deletes all marks on all digital channels.
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
        """Return the ``MARK:SELected`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MARK:SELected?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK:SELected?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.end``: The ``MARK:SELected:END`` command.
            - ``.focus``: The ``MARK:SELected:FOCUS`` command.
            - ``.marksincolumn``: The ``MARK:SELected:MARKSINCOLumn`` command.
            - ``.owner``: The ``MARK:SELected:OWNer`` command.
            - ``.source``: The ``MARK:SELected:SOURCE`` command.
            - ``.start``: The ``MARK:SELected:STARt`` command.
            - ``.state``: The ``MARK:SELected:STATe`` command.
            - ``.zoom``: The ``MARK:SELected:ZOOm`` command tree.
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
