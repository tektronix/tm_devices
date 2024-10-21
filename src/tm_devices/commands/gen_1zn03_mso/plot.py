"""The plot commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - PLOT:ADDNew <QString>
    - PLOT:DELete <QString>
    - PLOT:LIST?
    - PLOT:PLOT<x>:SOUrce1 MEAS<x>
    - PLOT:PLOT<x>:SOUrce1?
    - PLOT:PLOT<x>:TYPe {NONE|XY}
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


class PlotPlotItemType(SCPICmdWrite):
    """The ``PLOT:PLOT<x>:TYPe`` command.

    Description:
        - This command sets or returns the current plot type of the specified plot.

    Usage:
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:TYPe value`` command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:TYPe {NONE|XY}
        ```

    Info:
        - ``<x>`` is the plot number. This is the equivalent of the number shown on a plot heading
          in the UI.
        - ``NONE`` does not create a plot.
        - ``XY`` creates a XY plot.
    """


class PlotPlotItemSource1(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:SOUrce1`` command.

    Description:
        - This command sets or queries the plot source.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:SOUrce1?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:SOUrce1?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:SOUrce1 value`` command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:SOUrce1 MEAS<x>
        - PLOT:PLOT<x>:SOUrce1?
        ```

    Info:
        - ``MEAS<x>`` is the specified measurement source for the specified plot.
    """


class PlotPlotItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``PLOT:PLOT<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source1``: The ``PLOT:PLOT<x>:SOUrce1`` command.
        - ``.type``: The ``PLOT:PLOT<x>:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source1 = PlotPlotItemSource1(device, f"{self._cmd_syntax}:SOUrce1")
        self._type = PlotPlotItemType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def source1(self) -> PlotPlotItemSource1:
        """Return the ``PLOT:PLOT<x>:SOUrce1`` command.

        Description:
            - This command sets or queries the plot source.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:SOUrce1?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:SOUrce1?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:SOUrce1 value``
              command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:SOUrce1 MEAS<x>
            - PLOT:PLOT<x>:SOUrce1?
            ```

        Info:
            - ``MEAS<x>`` is the specified measurement source for the specified plot.
        """
        return self._source1

    @property
    def type(self) -> PlotPlotItemType:
        """Return the ``PLOT:PLOT<x>:TYPe`` command.

        Description:
            - This command sets or returns the current plot type of the specified plot.

        Usage:
            - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:TYPe value`` command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:TYPe {NONE|XY}
            ```

        Info:
            - ``<x>`` is the plot number. This is the equivalent of the number shown on a plot
              heading in the UI.
            - ``NONE`` does not create a plot.
            - ``XY`` creates a XY plot.
        """
        return self._type


class PlotList(SCPICmdRead):
    """The ``PLOT:LIST`` command.

    Description:
        - This command lists all currently defined plots.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:LIST?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - PLOT:LIST?
        ```
    """


class PlotDelete(SCPICmdWrite):
    """The ``PLOT:DELete`` command.

    Description:
        - This command deletes the specified plot.

    Usage:
        - Using the ``.write(value)`` method will send the ``PLOT:DELete value`` command.

    SCPI Syntax:
        ```
        - PLOT:DELete <QString>
        ```

    Info:
        - ``<QString>`` is the specified plot. Argument is of the form 'PLOT<NR1>, where <NR1> is ≥
          1).
    """

    _WRAP_ARG_WITH_QUOTES = True


class PlotAddnew(SCPICmdWrite):
    """The ``PLOT:ADDNew`` command.

    Description:
        - This command adds the specified plot.

    Usage:
        - Using the ``.write(value)`` method will send the ``PLOT:ADDNew value`` command.

    SCPI Syntax:
        ```
        - PLOT:ADDNew <QString>
        ```

    Info:
        - ``<QString>`` is the specified plot. The argument is of the form 'PLOT<NR1>', where <NR1>
          ≥ 1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class Plot(SCPICmdRead):
    """The ``PLOT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.addnew``: The ``PLOT:ADDNew`` command.
        - ``.delete``: The ``PLOT:DELete`` command.
        - ``.list``: The ``PLOT:LIST`` command.
        - ``.plot``: The ``PLOT:PLOT<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "PLOT") -> None:
        super().__init__(device, cmd_syntax)
        self._addnew = PlotAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._delete = PlotDelete(device, f"{self._cmd_syntax}:DELete")
        self._list = PlotList(device, f"{self._cmd_syntax}:LIST")
        self._plot: Dict[int, PlotPlotItem] = DefaultDictPassKeyToFactory(
            lambda x: PlotPlotItem(device, f"{self._cmd_syntax}:PLOT{x}")
        )

    @property
    def addnew(self) -> PlotAddnew:
        """Return the ``PLOT:ADDNew`` command.

        Description:
            - This command adds the specified plot.

        Usage:
            - Using the ``.write(value)`` method will send the ``PLOT:ADDNew value`` command.

        SCPI Syntax:
            ```
            - PLOT:ADDNew <QString>
            ```

        Info:
            - ``<QString>`` is the specified plot. The argument is of the form 'PLOT<NR1>', where
              <NR1> ≥ 1.
        """
        return self._addnew

    @property
    def delete(self) -> PlotDelete:
        """Return the ``PLOT:DELete`` command.

        Description:
            - This command deletes the specified plot.

        Usage:
            - Using the ``.write(value)`` method will send the ``PLOT:DELete value`` command.

        SCPI Syntax:
            ```
            - PLOT:DELete <QString>
            ```

        Info:
            - ``<QString>`` is the specified plot. Argument is of the form 'PLOT<NR1>, where <NR1>
              is ≥ 1).
        """
        return self._delete

    @property
    def list(self) -> PlotList:
        """Return the ``PLOT:LIST`` command.

        Description:
            - This command lists all currently defined plots.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:LIST?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - PLOT:LIST?
            ```
        """
        return self._list

    @property
    def plot(self) -> Dict[int, PlotPlotItem]:
        """Return the ``PLOT:PLOT<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source1``: The ``PLOT:PLOT<x>:SOUrce1`` command.
            - ``.type``: The ``PLOT:PLOT<x>:TYPe`` command.
        """
        return self._plot
