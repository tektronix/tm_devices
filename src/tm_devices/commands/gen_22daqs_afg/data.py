# pylint: disable=line-too-long
"""The data commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DATA:CATalog?
    - DATA:COPY <trace_name>,{EMEMory[1]|EMEMory2}{EMEMory[1]|EMEMory2},{USER[1]|USER<x>}
    - DATA:DATA {EMEMory|EMEMory<x>},<binary_block_data>
    - DATA:DATA:LINE {EMEMory|EMEMory<x>},<start_point>,<point_data1>, <end_point>,<point_data2>
    - DATA:DATA:VALue {EMEMory|EMEMory<x>},<point>,<data>
    - DATA:DATA:VALue? {EMEMory[1]|EMEMory2},<points>
    - DATA:DATA? {EMEMory[1]|EMEMory2}
    - DATA:DEFine {EMEMory|EMEMory<x>}[,{<points>|<trace_name>}]
    - DATA:DELete:NAME <trace_name>
    - DATA:EMEMCOPY {EMEMory[1]|EMEMory2}, {EMEMory[1]|EMEMory2}
    - DATA:LOCK:STATe {USER[1]|USER<x>},{ON|OFF|<NR1>}
    - DATA:LOCK:STATe? {USER[1]|USER2|USER3|USER4}
    - DATA:POINts {EMEMory|EMEMory<x>}[,<points>|MINimum|MAXimum]
    - DATA:POINts? {EMEMory[1]|EMEMory2}{,MIN|MAX}
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DataPoints(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``DATA:POINts`` command.

    Description:
        - This command sets or queries the number of data points for the waveform created in the
          edit memory.

    Usage:
        - Using the ``.query(argument)`` method will send the ``DATA:POINts? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``DATA:POINts? argument``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATA:POINts value`` command.

    SCPI Syntax:
        ```
        - DATA:POINts {EMEMory|EMEMory<x>}[,<points>|MINimum|MAXimum]
        - DATA:POINts? {EMEMory[1]|EMEMory2}{,MIN|MAX}
        ```

    Info:
        - ``EMEMory`` refers to the command arguments column in the table in Appendix B.
        - ``EMEMory1`` refers to the command arguments column in the table in Appendix B.
        - ``EMEMory2`` refers to the command arguments column in the table in Appendix B.
        - ``<points>::=<NR1>``
        - ``EMEMory[1]`` refers to the query arguments column in the table in Appendix B.
        - ``EMEMory2`` refers to the query arguments column in the table in Appendix B.
    """


class DataLockState(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``DATA:LOCK:STATe`` command.

    Description:
        - This command sets or queries whether to lock or unlock the user waveform memory.

    Usage:
        - Using the ``.query(argument)`` method will send the ``DATA:LOCK:STATe? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``DATA:LOCK:STATe? argument``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATA:LOCK:STATe value`` command.

    SCPI Syntax:
        ```
        - DATA:LOCK:STATe {USER[1]|USER<x>},{ON|OFF|<NR1>}
        - DATA:LOCK:STATe? {USER[1]|USER2|USER3|USER4}
        ```

    Info:
        - ``ON`` or <NR1>≠0 locks the specified user waveform memory.
        - ``OFF`` or <NR1>=0 unlocks the specified user waveform memory.
    """


class DataLock(SCPICmdRead):
    """The ``DATA:LOCK`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DATA:LOCK?`` query.
        - Using the ``.verify(value)`` method will send the ``DATA:LOCK?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``DATA:LOCK:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = DataLockState(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> DataLockState:
        """Return the ``DATA:LOCK:STATe`` command.

        Description:
            - This command sets or queries whether to lock or unlock the user waveform memory.

        Usage:
            - Using the ``.query(argument)`` method will send the ``DATA:LOCK:STATe? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``DATA:LOCK:STATe? argument`` query and raise an AssertionError if the returned value
              does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATA:LOCK:STATe value`` command.

        SCPI Syntax:
            ```
            - DATA:LOCK:STATe {USER[1]|USER<x>},{ON|OFF|<NR1>}
            - DATA:LOCK:STATe? {USER[1]|USER2|USER3|USER4}
            ```

        Info:
            - ``ON`` or <NR1>≠0 locks the specified user waveform memory.
            - ``OFF`` or <NR1>=0 unlocks the specified user waveform memory.
        """
        return self._state


class DataEmemcopy(SCPICmdWrite):
    """The ``DATA:EMEMCOPY`` command.

    Description:
        - This command copies the contents of edit memory1 (or edit memory2) to edit memory2 (or
          edit memory1). If your arbitrary/function generator is a single-channel model, this
          command is not supported.

    Usage:
        - Using the ``.write(value)`` method will send the ``DATA:EMEMCOPY value`` command.

    SCPI Syntax:
        ```
        - DATA:EMEMCOPY {EMEMory[1]|EMEMory2}, {EMEMory[1]|EMEMory2}
        ```

    Info:
        - ``EMEMory[1]``
        - ``EMEMory2``
    """


class DataDeleteName(SCPICmdWrite):
    """The ``DATA:DELete:NAME`` command.

    Description:
        - This command deletes the contents of specified user waveform memory.

    Usage:
        - Using the ``.write(value)`` method will send the ``DATA:DELete:NAME value`` command.

    SCPI Syntax:
        ```
        - DATA:DELete:NAME <trace_name>
        ```

    Info:
        - ``<trace_name>::={USER[1]``
        - ``USER2``
        - ``USER3``
        - ``USER4}``
    """


class DataDelete(SCPICmdRead):
    """The ``DATA:DELete`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DATA:DELete?`` query.
        - Using the ``.verify(value)`` method will send the ``DATA:DELete?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.name``: The ``DATA:DELete:NAME`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._name = DataDeleteName(device, f"{self._cmd_syntax}:NAME")

    @property
    def name(self) -> DataDeleteName:
        """Return the ``DATA:DELete:NAME`` command.

        Description:
            - This command deletes the contents of specified user waveform memory.

        Usage:
            - Using the ``.write(value)`` method will send the ``DATA:DELete:NAME value`` command.

        SCPI Syntax:
            ```
            - DATA:DELete:NAME <trace_name>
            ```

        Info:
            - ``<trace_name>::={USER[1]``
            - ``USER2``
            - ``USER3``
            - ``USER4}``
        """
        return self._name


class DataDefine(SCPICmdWrite):
    """The ``DATA:DEFine`` command.

    Description:
        - This command resets the contents of edit memory.

    Usage:
        - Using the ``.write(value)`` method will send the ``DATA:DEFine value`` command.

    SCPI Syntax:
        ```
        - DATA:DEFine {EMEMory|EMEMory<x>}[,{<points>|<trace_name>}]
        ```

    Info:
        - ``EMEMory`` refers to the command arguments column in the table in Appendix B.
        - ``EMEMory1`` refers to the command arguments column in the table in Appendix B.
        - ``EMEMory2`` refers to the command arguments column in the table in Appendix B.
        - ``<points>::=<NR1>``
        - ``<trace_name>::={SINusoid``
        - ``SQUare``
        - ``PULSe``
        - ``RAMP``
        - ``NOISe}``
    """


class DataDataValue(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``DATA:DATA:VALue`` command.

    Description:
        - This command sets or queries the data value at the specified point in the edit memory.

    Usage:
        - Using the ``.query(argument)`` method will send the ``DATA:DATA:VALue? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``DATA:DATA:VALue? argument``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATA:DATA:VALue value`` command.

    SCPI Syntax:
        ```
        - DATA:DATA:VALue {EMEMory|EMEMory<x>},<point>,<data>
        - DATA:DATA:VALue? {EMEMory[1]|EMEMory2},<points>
        ```

    Info:
        - ``EMEMory`` refers to the command arguments column in the table in Appendix B.
        - ``EMEMory1`` refers to the command arguments column in the table in Appendix B.
        - ``EMEMory2`` refers to the command arguments column in the table in Appendix B.
        - ``<point>::=<NR1>``
        - ``<data>::=<NR1>``
        - ``EMEMory`` refers to the query arguments column in the table in Appendix B.
        - ``EMEMory1`` refers to the query arguments column in the table in Appendix B.
        - ``EMEMory2`` refers to the query arguments column in the table in Appendix B.
    """


class DataDataLine(SCPICmdWrite):
    """The ``DATA:DATA:LINE`` command.

    Description:
        - This command writes line data to the edit memory. The data between the specified points is
          interpolated linearly.

    Usage:
        - Using the ``.write(value)`` method will send the ``DATA:DATA:LINE value`` command.

    SCPI Syntax:
        ```
        - DATA:DATA:LINE {EMEMory|EMEMory<x>},<start_point>,<point_data1>, <end_point>,<point_data2>
        ```

    Info:
        - ``EMEMory`` refers to the command arguments column in the table in Appendix B.
        - ``EMEMory1`` refers to the command arguments column in the table in Appendix B.
        - ``EMEMory2`` refers to the command arguments column in the table in Appendix B.
        - ``<start_point>::=<NR1>``
        - ``<point_data1>::=<NR1>``
        - ``<end_point>::=<NR1>``
        - ``<point_data2>::=<NR1>``
    """


class DataData(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``DATA:DATA`` command.

    Description:
        - This command transfers the waveform data from the external controller to the edit memory
          in the arbitrary function generator. The query command returns the binary block data.

    Usage:
        - Using the ``.query(argument)`` method will send the ``DATA:DATA? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``DATA:DATA? argument`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATA:DATA value`` command.

    SCPI Syntax:
        ```
        - DATA:DATA {EMEMory|EMEMory<x>},<binary_block_data>
        - DATA:DATA? {EMEMory[1]|EMEMory2}
        ```

    Info:
        - ``EMEMory`` refers to the command arguments column in the table in Appendix B.
        - ``EMEMory1`` refers to the command arguments column in the table in Appendix B.
        - ``EMEMory2`` refers to the command arguments column in the table in Appendix B.
        - ``EMEMory`` refers to the query arguments column in the table in Appendix B.
        - ``EMEMory1`` refers to the query arguments column in the table in Appendix B.
        - ``EMEMory2`` refers to the query arguments column in the table in Appendix B.

    Properties:
        - ``.line``: The ``DATA:DATA:LINE`` command.
        - ``.value``: The ``DATA:DATA:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._line = DataDataLine(device, f"{self._cmd_syntax}:LINE")
        self._value = DataDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def line(self) -> DataDataLine:
        """Return the ``DATA:DATA:LINE`` command.

        Description:
            - This command writes line data to the edit memory. The data between the specified
              points is interpolated linearly.

        Usage:
            - Using the ``.write(value)`` method will send the ``DATA:DATA:LINE value`` command.

        SCPI Syntax:
            ```
            - DATA:DATA:LINE {EMEMory|EMEMory<x>},<start_point>,<point_data1>, <end_point>,<point_data2>
            ```

        Info:
            - ``EMEMory`` refers to the command arguments column in the table in Appendix B.
            - ``EMEMory1`` refers to the command arguments column in the table in Appendix B.
            - ``EMEMory2`` refers to the command arguments column in the table in Appendix B.
            - ``<start_point>::=<NR1>``
            - ``<point_data1>::=<NR1>``
            - ``<end_point>::=<NR1>``
            - ``<point_data2>::=<NR1>``
        """  # noqa: E501
        return self._line

    @property
    def value(self) -> DataDataValue:
        """Return the ``DATA:DATA:VALue`` command.

        Description:
            - This command sets or queries the data value at the specified point in the edit memory.

        Usage:
            - Using the ``.query(argument)`` method will send the ``DATA:DATA:VALue? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``DATA:DATA:VALue? argument`` query and raise an AssertionError if the returned value
              does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATA:DATA:VALue value`` command.

        SCPI Syntax:
            ```
            - DATA:DATA:VALue {EMEMory|EMEMory<x>},<point>,<data>
            - DATA:DATA:VALue? {EMEMory[1]|EMEMory2},<points>
            ```

        Info:
            - ``EMEMory`` refers to the command arguments column in the table in Appendix B.
            - ``EMEMory1`` refers to the command arguments column in the table in Appendix B.
            - ``EMEMory2`` refers to the command arguments column in the table in Appendix B.
            - ``<point>::=<NR1>``
            - ``<data>::=<NR1>``
            - ``EMEMory`` refers to the query arguments column in the table in Appendix B.
            - ``EMEMory1`` refers to the query arguments column in the table in Appendix B.
            - ``EMEMory2`` refers to the query arguments column in the table in Appendix B.
        """
        return self._value


class DataCopy(SCPICmdWrite):
    """The ``DATA:COPY`` command.

    Description:
        - This command copies the contents of edit memory (or user waveform memory) to a specified
          user waveform memory (or edit memory).

    Usage:
        - Using the ``.write(value)`` method will send the ``DATA:COPY value`` command.

    SCPI Syntax:
        ```
        - DATA:COPY <trace_name>,{EMEMory[1]|EMEMory2}{EMEMory[1]|EMEMory2},{USER[1]|USER<x>}
        ```
    """


class DataCatalog(SCPICmdRead):
    """The ``DATA:CATalog`` command.

    Description:
        - This query-only command returns the names of user waveform memory and edit memory.

    Usage:
        - Using the ``.query()`` method will send the ``DATA:CATalog?`` query.
        - Using the ``.verify(value)`` method will send the ``DATA:CATalog?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DATA:CATalog?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class Data(SCPICmdRead):
    """The ``DATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``DATA?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.catalog``: The ``DATA:CATalog`` command.
        - ``.copy``: The ``DATA:COPY`` command.
        - ``.define``: The ``DATA:DEFine`` command.
        - ``.delete``: The ``DATA:DELete`` command tree.
        - ``.ememcopy``: The ``DATA:EMEMCOPY`` command.
        - ``.lock``: The ``DATA:LOCK`` command tree.
        - ``.points``: The ``DATA:POINts`` command.
        - ``.data``: The ``DATA:DATA`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DATA") -> None:
        super().__init__(device, cmd_syntax)
        self._catalog = DataCatalog(device, f"{self._cmd_syntax}:CATalog")
        self._copy = DataCopy(device, f"{self._cmd_syntax}:COPY")
        self._define = DataDefine(device, f"{self._cmd_syntax}:DEFine")
        self._delete = DataDelete(device, f"{self._cmd_syntax}:DELete")
        self._ememcopy = DataEmemcopy(device, f"{self._cmd_syntax}:EMEMCOPY")
        self._lock = DataLock(device, f"{self._cmd_syntax}:LOCK")
        self._points = DataPoints(device, f"{self._cmd_syntax}:POINts")
        self._data = DataData(device, f"{self._cmd_syntax}:DATA")

    @property
    def catalog(self) -> DataCatalog:
        """Return the ``DATA:CATalog`` command.

        Description:
            - This query-only command returns the names of user waveform memory and edit memory.

        Usage:
            - Using the ``.query()`` method will send the ``DATA:CATalog?`` query.
            - Using the ``.verify(value)`` method will send the ``DATA:CATalog?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DATA:CATalog?
            ```
        """
        return self._catalog

    @property
    def copy(self) -> DataCopy:
        """Return the ``DATA:COPY`` command.

        Description:
            - This command copies the contents of edit memory (or user waveform memory) to a
              specified user waveform memory (or edit memory).

        Usage:
            - Using the ``.write(value)`` method will send the ``DATA:COPY value`` command.

        SCPI Syntax:
            ```
            - DATA:COPY <trace_name>,{EMEMory[1]|EMEMory2}{EMEMory[1]|EMEMory2},{USER[1]|USER<x>}
            ```
        """
        return self._copy

    @property
    def define(self) -> DataDefine:
        """Return the ``DATA:DEFine`` command.

        Description:
            - This command resets the contents of edit memory.

        Usage:
            - Using the ``.write(value)`` method will send the ``DATA:DEFine value`` command.

        SCPI Syntax:
            ```
            - DATA:DEFine {EMEMory|EMEMory<x>}[,{<points>|<trace_name>}]
            ```

        Info:
            - ``EMEMory`` refers to the command arguments column in the table in Appendix B.
            - ``EMEMory1`` refers to the command arguments column in the table in Appendix B.
            - ``EMEMory2`` refers to the command arguments column in the table in Appendix B.
            - ``<points>::=<NR1>``
            - ``<trace_name>::={SINusoid``
            - ``SQUare``
            - ``PULSe``
            - ``RAMP``
            - ``NOISe}``
        """
        return self._define

    @property
    def delete(self) -> DataDelete:
        """Return the ``DATA:DELete`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DATA:DELete?`` query.
            - Using the ``.verify(value)`` method will send the ``DATA:DELete?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.name``: The ``DATA:DELete:NAME`` command.
        """
        return self._delete

    @property
    def ememcopy(self) -> DataEmemcopy:
        """Return the ``DATA:EMEMCOPY`` command.

        Description:
            - This command copies the contents of edit memory1 (or edit memory2) to edit memory2 (or
              edit memory1). If your arbitrary/function generator is a single-channel model, this
              command is not supported.

        Usage:
            - Using the ``.write(value)`` method will send the ``DATA:EMEMCOPY value`` command.

        SCPI Syntax:
            ```
            - DATA:EMEMCOPY {EMEMory[1]|EMEMory2}, {EMEMory[1]|EMEMory2}
            ```

        Info:
            - ``EMEMory[1]``
            - ``EMEMory2``
        """
        return self._ememcopy

    @property
    def lock(self) -> DataLock:
        """Return the ``DATA:LOCK`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DATA:LOCK?`` query.
            - Using the ``.verify(value)`` method will send the ``DATA:LOCK?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``DATA:LOCK:STATe`` command.
        """
        return self._lock

    @property
    def points(self) -> DataPoints:
        """Return the ``DATA:POINts`` command.

        Description:
            - This command sets or queries the number of data points for the waveform created in the
              edit memory.

        Usage:
            - Using the ``.query(argument)`` method will send the ``DATA:POINts? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the ``DATA:POINts? argument``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATA:POINts value`` command.

        SCPI Syntax:
            ```
            - DATA:POINts {EMEMory|EMEMory<x>}[,<points>|MINimum|MAXimum]
            - DATA:POINts? {EMEMory[1]|EMEMory2}{,MIN|MAX}
            ```

        Info:
            - ``EMEMory`` refers to the command arguments column in the table in Appendix B.
            - ``EMEMory1`` refers to the command arguments column in the table in Appendix B.
            - ``EMEMory2`` refers to the command arguments column in the table in Appendix B.
            - ``<points>::=<NR1>``
            - ``EMEMory[1]`` refers to the query arguments column in the table in Appendix B.
            - ``EMEMory2`` refers to the query arguments column in the table in Appendix B.
        """
        return self._points

    @property
    def data(self) -> DataData:
        """Return the ``DATA:DATA`` command.

        Description:
            - This command transfers the waveform data from the external controller to the edit
              memory in the arbitrary function generator. The query command returns the binary block
              data.

        Usage:
            - Using the ``.query(argument)`` method will send the ``DATA:DATA? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the ``DATA:DATA? argument``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATA:DATA value`` command.

        SCPI Syntax:
            ```
            - DATA:DATA {EMEMory|EMEMory<x>},<binary_block_data>
            - DATA:DATA? {EMEMory[1]|EMEMory2}
            ```

        Info:
            - ``EMEMory`` refers to the command arguments column in the table in Appendix B.
            - ``EMEMory1`` refers to the command arguments column in the table in Appendix B.
            - ``EMEMory2`` refers to the command arguments column in the table in Appendix B.
            - ``EMEMory`` refers to the query arguments column in the table in Appendix B.
            - ``EMEMory1`` refers to the query arguments column in the table in Appendix B.
            - ``EMEMory2`` refers to the query arguments column in the table in Appendix B.

        Sub-properties:
            - ``.line``: The ``DATA:DATA:LINE`` command.
            - ``.value``: The ``DATA:DATA:VALue`` command.
        """
        return self._data
