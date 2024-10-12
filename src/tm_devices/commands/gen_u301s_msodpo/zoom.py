"""The zoom commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ZOOm:MODe {ON|OFF|<NR1>}
    - ZOOm:STATE {ON|OFF|<NR1>}
    - ZOOm:ZOOM1:FACtor?
    - ZOOm:ZOOM1:HORizontal:POSition <NR3>
    - ZOOm:ZOOM1:HORizontal:POSition?
    - ZOOm:ZOOM1:HORizontal:SCAle <NR3>
    - ZOOm:ZOOM1:HORizontal:SCAle?
    - ZOOm:ZOOM1:POSition <NR3>
    - ZOOm:ZOOM1:POSition?
    - ZOOm:ZOOM1:SCAle <NR3>
    - ZOOm:ZOOM1:SCAle?
    - ZOOm:ZOOM1:STATE {ON|OFF|<NR1>}
    - ZOOm:ZOOM1:STATE?
    - ZOOm:ZOOM1?
    - ZOOm?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ZoomZoom1State(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:STATE`` command.

    Description:
        - Sets or returns the specified zoom on or off, where x is the integer 1 representing the
          single zoom window.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:STATE value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:STATE {ON|OFF|<NR1>}
        - ZOOm:ZOOM1:STATE?
        ```

    Info:
        - ``ON`` turns Zoom 1 on.
        - ``OFF`` turns Zoom 1 off.
        - ``<NR1>`` = 0 disables the specified zoom; any other value enables the specified zoom.
    """


class ZoomZoom1Scale(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:SCAle`` command.

    Description:
        - Sets or returns the zoom horizontal scale for the specified zoom.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:SCAle?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:SCAle value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:SCAle <NR3>
        - ZOOm:ZOOM1:SCAle?
        ```

    Info:
        - ``<NR3>`` is the amount of expansion in the horizontal direction and ranges from 1.0E-3 to
          5.0.
    """


class ZoomZoom1Position(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:POSition`` command.

    Description:
        - Sets or returns the horizontal position for the specified zoom.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:POSition?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:POSition value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:POSition <NR3>
        - ZOOm:ZOOM1:POSition?
        ```

    Info:
        - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the upper window that is to
          the left of screen center, when the zoom factor is 1× or greater.
    """


class ZoomZoom1HorizontalScale(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:HORizontal:SCAle`` command.

    Description:
        - Sets or returns the zoom horizontal scale for the specified zoom.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:HORizontal:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:HORizontal:SCAle?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:HORizontal:SCAle value``
          command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:HORizontal:SCAle <NR3>
        - ZOOm:ZOOM1:HORizontal:SCAle?
        ```

    Info:
        - ``<NR3>`` is the amount of expansion in the horizontal direction and ranges from 1.0E-3 to
          5.0.
    """


class ZoomZoom1HorizontalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:HORizontal:POSition`` command.

    Description:
        - Sets or returns the horizontal position for the specified zoom.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:HORizontal:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:HORizontal:POSition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:HORizontal:POSition value``
          command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:HORizontal:POSition <NR3>
        - ZOOm:ZOOM1:HORizontal:POSition?
        ```

    Info:
        - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the upper window that is to
          the left of screen center, when the zoom factor is 1× or greater.
    """


class ZoomZoom1Horizontal(SCPICmdRead):
    """The ``ZOOm:ZOOM1:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:HORizontal?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``ZOOm:ZOOM1:HORizontal:POSition`` command.
        - ``.scale``: The ``ZOOm:ZOOM1:HORizontal:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = ZoomZoom1HorizontalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = ZoomZoom1HorizontalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> ZoomZoom1HorizontalPosition:
        """Return the ``ZOOm:ZOOM1:HORizontal:POSition`` command.

        Description:
            - Sets or returns the horizontal position for the specified zoom.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:HORizontal:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:HORizontal:POSition?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:ZOOM1:HORizontal:POSition value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:HORizontal:POSition <NR3>
            - ZOOm:ZOOM1:HORizontal:POSition?
            ```

        Info:
            - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the upper window that is
              to the left of screen center, when the zoom factor is 1× or greater.
        """
        return self._position

    @property
    def scale(self) -> ZoomZoom1HorizontalScale:
        """Return the ``ZOOm:ZOOM1:HORizontal:SCAle`` command.

        Description:
            - Sets or returns the zoom horizontal scale for the specified zoom.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:HORizontal:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:HORizontal:SCAle?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:HORizontal:SCAle value``
              command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:HORizontal:SCAle <NR3>
            - ZOOm:ZOOM1:HORizontal:SCAle?
            ```

        Info:
            - ``<NR3>`` is the amount of expansion in the horizontal direction and ranges from
              1.0E-3 to 5.0.
        """
        return self._scale


class ZoomZoom1Factor(SCPICmdRead):
    """The ``ZOOm:ZOOM1:FACtor`` command.

    Description:
        - Returns the zoom factor of a particular zoom box.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:FACtor?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:FACtor?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:FACtor?
        ```
    """


class ZoomZoom1(SCPICmdRead):
    """The ``ZOOm:ZOOM1`` command.

    Description:
        - Returns the current horizontal positioning and scaling of the display.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1?
        ```

    Properties:
        - ``.factor``: The ``ZOOm:ZOOM1:FACtor`` command.
        - ``.horizontal``: The ``ZOOm:ZOOM1:HORizontal`` command tree.
        - ``.position``: The ``ZOOm:ZOOM1:POSition`` command.
        - ``.scale``: The ``ZOOm:ZOOM1:SCAle`` command.
        - ``.state``: The ``ZOOm:ZOOM1:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._factor = ZoomZoom1Factor(device, f"{self._cmd_syntax}:FACtor")
        self._horizontal = ZoomZoom1Horizontal(device, f"{self._cmd_syntax}:HORizontal")
        self._position = ZoomZoom1Position(device, f"{self._cmd_syntax}:POSition")
        self._scale = ZoomZoom1Scale(device, f"{self._cmd_syntax}:SCAle")
        self._state = ZoomZoom1State(device, f"{self._cmd_syntax}:STATE")

    @property
    def factor(self) -> ZoomZoom1Factor:
        """Return the ``ZOOm:ZOOM1:FACtor`` command.

        Description:
            - Returns the zoom factor of a particular zoom box.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:FACtor?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:FACtor?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:FACtor?
            ```
        """
        return self._factor

    @property
    def horizontal(self) -> ZoomZoom1Horizontal:
        """Return the ``ZOOm:ZOOM1:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:HORizontal?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:HORizontal?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``ZOOm:ZOOM1:HORizontal:POSition`` command.
            - ``.scale``: The ``ZOOm:ZOOM1:HORizontal:SCAle`` command.
        """
        return self._horizontal

    @property
    def position(self) -> ZoomZoom1Position:
        """Return the ``ZOOm:ZOOM1:POSition`` command.

        Description:
            - Sets or returns the horizontal position for the specified zoom.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:POSition?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:POSition value``
              command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:POSition <NR3>
            - ZOOm:ZOOM1:POSition?
            ```

        Info:
            - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the upper window that is
              to the left of screen center, when the zoom factor is 1× or greater.
        """
        return self._position

    @property
    def scale(self) -> ZoomZoom1Scale:
        """Return the ``ZOOm:ZOOM1:SCAle`` command.

        Description:
            - Sets or returns the zoom horizontal scale for the specified zoom.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:SCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:SCAle value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:SCAle <NR3>
            - ZOOm:ZOOM1:SCAle?
            ```

        Info:
            - ``<NR3>`` is the amount of expansion in the horizontal direction and ranges from
              1.0E-3 to 5.0.
        """
        return self._scale

    @property
    def state(self) -> ZoomZoom1State:
        """Return the ``ZOOm:ZOOM1:STATE`` command.

        Description:
            - Sets or returns the specified zoom on or off, where x is the integer 1 representing
              the single zoom window.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:STATE value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:STATE {ON|OFF|<NR1>}
            - ZOOm:ZOOM1:STATE?
            ```

        Info:
            - ``ON`` turns Zoom 1 on.
            - ``OFF`` turns Zoom 1 off.
            - ``<NR1>`` = 0 disables the specified zoom; any other value enables the specified zoom.
        """
        return self._state


class ZoomState(SCPICmdWrite):
    """The ``ZOOm:STATE`` command.

    Description:
        - Turns Zoom mode on or off. The Zoom query returns the current state of Zoom mode. This
          command is equivalent to pressing the zoom button located on the front panel.

    Usage:
        - Using the ``.write(value)`` method will send the ``ZOOm:STATE value`` command.

    SCPI Syntax:
        ```
        - ZOOm:STATE {ON|OFF|<NR1>}
        ```

    Info:
        - ``ON`` turns on Zoom mode.
        - ``OFF`` turns off Zoom mode.
        - ``<NR1>`` is an integer. 0 turns off Zoom mode; any other value turns on Zoom mode.
    """


class ZoomMode(SCPICmdWrite):
    """The ``ZOOm:MODe`` command.

    Description:
        - Turns Zoom mode on or off. The Zoom query returns the current state of Zoom mode. This
          command is equivalent to pressing the zoom button located on the front panel.

    Usage:
        - Using the ``.write(value)`` method will send the ``ZOOm:MODe value`` command.

    SCPI Syntax:
        ```
        - ZOOm:MODe {ON|OFF|<NR1>}
        ```

    Info:
        - ``ON`` turns on Zoom mode.
        - ``OFF`` turns off Zoom mode.
        - ``<NR1>`` is an integer. 0 turns off Zoom mode; any other value turns on Zoom mode.
    """


class Zoom(SCPICmdRead):
    """The ``ZOOm`` command.

    Description:
        - Returns the current vertical and horizontal positioning and scaling of the display.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ZOOm?
        ```

    Properties:
        - ``.zoom1``: The ``ZOOm:ZOOM1`` command.
        - ``.mode``: The ``ZOOm:MODe`` command.
        - ``.state``: The ``ZOOm:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "ZOOm") -> None:
        super().__init__(device, cmd_syntax)
        self._zoom1 = ZoomZoom1(device, f"{self._cmd_syntax}:ZOOM1")
        self._mode = ZoomMode(device, f"{self._cmd_syntax}:MODe")
        self._state = ZoomState(device, f"{self._cmd_syntax}:STATE")

    @property
    def zoom1(self) -> ZoomZoom1:
        """Return the ``ZOOm:ZOOM1`` command.

        Description:
            - Returns the current horizontal positioning and scaling of the display.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1?
            ```

        Sub-properties:
            - ``.factor``: The ``ZOOm:ZOOM1:FACtor`` command.
            - ``.horizontal``: The ``ZOOm:ZOOM1:HORizontal`` command tree.
            - ``.position``: The ``ZOOm:ZOOM1:POSition`` command.
            - ``.scale``: The ``ZOOm:ZOOM1:SCAle`` command.
            - ``.state``: The ``ZOOm:ZOOM1:STATE`` command.
        """
        return self._zoom1

    @property
    def mode(self) -> ZoomMode:
        """Return the ``ZOOm:MODe`` command.

        Description:
            - Turns Zoom mode on or off. The Zoom query returns the current state of Zoom mode. This
              command is equivalent to pressing the zoom button located on the front panel.

        Usage:
            - Using the ``.write(value)`` method will send the ``ZOOm:MODe value`` command.

        SCPI Syntax:
            ```
            - ZOOm:MODe {ON|OFF|<NR1>}
            ```

        Info:
            - ``ON`` turns on Zoom mode.
            - ``OFF`` turns off Zoom mode.
            - ``<NR1>`` is an integer. 0 turns off Zoom mode; any other value turns on Zoom mode.
        """
        return self._mode

    @property
    def state(self) -> ZoomState:
        """Return the ``ZOOm:STATE`` command.

        Description:
            - Turns Zoom mode on or off. The Zoom query returns the current state of Zoom mode. This
              command is equivalent to pressing the zoom button located on the front panel.

        Usage:
            - Using the ``.write(value)`` method will send the ``ZOOm:STATE value`` command.

        SCPI Syntax:
            ```
            - ZOOm:STATE {ON|OFF|<NR1>}
            ```

        Info:
            - ``ON`` turns on Zoom mode.
            - ``OFF`` turns off Zoom mode.
            - ``<NR1>`` is an integer. 0 turns off Zoom mode; any other value turns on Zoom mode.
        """
        return self._state
