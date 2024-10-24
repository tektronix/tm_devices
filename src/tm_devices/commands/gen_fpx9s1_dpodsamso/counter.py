"""The counter commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB, MSO70KC,
MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - COUnter:RESULTs:AVGmean?
    - COUnter:RESULTs:DEViation?
    - COUnter:RESULTs:MAXimum?
    - COUnter:RESULTs:MINimum?
    - COUnter:RESULTs:NUMber?
    - COUnter:RESULTs:VALue?
    - COUnter:RESULTs?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class CounterResultsValue(SCPICmdRead):
    """The ``COUnter:RESULTs:VALue`` command.

    Description:
        - Queries the measured value obtained from the Trigger Source Frequency or A-B Trigger Time
          Interval Applications. The measured quantity is value.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:RESULTs:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:VALue?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - COUnter:RESULTs:VALue?
        ```
    """


class CounterResultsNumber(SCPICmdRead):
    """The ``COUnter:RESULTs:NUMber`` command.

    Description:
        - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger Time
          Interval Applications. The value is the number of acquisitions (NUMber) taken at the time
          the command was given.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:RESULTs:NUMber?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:NUMber?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - COUnter:RESULTs:NUMber?
        ```
    """


class CounterResultsMinimum(SCPICmdRead):
    """The ``COUnter:RESULTs:MINimum`` command.

    Description:
        - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger Time
          Interval Applications. The minimum is a statistical value accumulated over the number of
          acquisitions ('NUMber') taken at the time the command was given.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:RESULTs:MINimum?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:MINimum?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - COUnter:RESULTs:MINimum?
        ```
    """


class CounterResultsMaximum(SCPICmdRead):
    """The ``COUnter:RESULTs:MAXimum`` command.

    Description:
        - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger Time
          Interval Applications. The maximum is a statistical value accumulated over the number of
          acquisitions (NUMber) taken at the time the command was given.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:RESULTs:MAXimum?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:MAXimum?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - COUnter:RESULTs:MAXimum?
        ```
    """


class CounterResultsDeviation(SCPICmdRead):
    """The ``COUnter:RESULTs:DEViation`` command.

    Description:
        - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger Time
          Interval Applications. The Deviation is a statistical value accumulated over the number of
          acquisitions (NUMber) taken at the time the command was given.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:RESULTs:DEViation?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:DEViation?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - COUnter:RESULTs:DEViation?
        ```
    """


class CounterResultsAvgmean(SCPICmdRead):
    """The ``COUnter:RESULTs:AVGmean`` command.

    Description:
        - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger Time
          Interval Applications. The AVGmean is a statistical value accumulated over the number of
          acquisitions (NUMber) taken at the time the command was given.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:RESULTs:AVGmean?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:AVGmean?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - COUnter:RESULTs:AVGmean?
        ```
    """


class CounterResults(SCPICmdRead):
    """The ``COUnter:RESULTs`` command.

    Description:
        - Queries the measured and derived values obtained from the Trigger Source Frequency or A-B
          Trigger Time Interval Applications. The measured quantity is value. The minimum, maximum,
          AVGmean, and Deviation are statistical values accumulated over the number of acquisitions
          (NUMber) taken at the time the command is given. All results are returned with the single
          query ``COUnter:RESULTs?`` Individual results are returned by other queries

    Usage:
        - Using the ``.query()`` method will send the ``COUnter:RESULTs?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - COUnter:RESULTs?
        ```

    Properties:
        - ``.avgmean``: The ``COUnter:RESULTs:AVGmean`` command.
        - ``.deviation``: The ``COUnter:RESULTs:DEViation`` command.
        - ``.maximum``: The ``COUnter:RESULTs:MAXimum`` command.
        - ``.minimum``: The ``COUnter:RESULTs:MINimum`` command.
        - ``.number``: The ``COUnter:RESULTs:NUMber`` command.
        - ``.value``: The ``COUnter:RESULTs:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._avgmean = CounterResultsAvgmean(device, f"{self._cmd_syntax}:AVGmean")
        self._deviation = CounterResultsDeviation(device, f"{self._cmd_syntax}:DEViation")
        self._maximum = CounterResultsMaximum(device, f"{self._cmd_syntax}:MAXimum")
        self._minimum = CounterResultsMinimum(device, f"{self._cmd_syntax}:MINimum")
        self._number = CounterResultsNumber(device, f"{self._cmd_syntax}:NUMber")
        self._value = CounterResultsValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def avgmean(self) -> CounterResultsAvgmean:
        """Return the ``COUnter:RESULTs:AVGmean`` command.

        Description:
            - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger
              Time Interval Applications. The AVGmean is a statistical value accumulated over the
              number of acquisitions (NUMber) taken at the time the command was given.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:RESULTs:AVGmean?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:AVGmean?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - COUnter:RESULTs:AVGmean?
            ```
        """
        return self._avgmean

    @property
    def deviation(self) -> CounterResultsDeviation:
        """Return the ``COUnter:RESULTs:DEViation`` command.

        Description:
            - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger
              Time Interval Applications. The Deviation is a statistical value accumulated over the
              number of acquisitions (NUMber) taken at the time the command was given.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:RESULTs:DEViation?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:DEViation?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - COUnter:RESULTs:DEViation?
            ```
        """
        return self._deviation

    @property
    def maximum(self) -> CounterResultsMaximum:
        """Return the ``COUnter:RESULTs:MAXimum`` command.

        Description:
            - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger
              Time Interval Applications. The maximum is a statistical value accumulated over the
              number of acquisitions (NUMber) taken at the time the command was given.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:RESULTs:MAXimum?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:MAXimum?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - COUnter:RESULTs:MAXimum?
            ```
        """
        return self._maximum

    @property
    def minimum(self) -> CounterResultsMinimum:
        """Return the ``COUnter:RESULTs:MINimum`` command.

        Description:
            - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger
              Time Interval Applications. The minimum is a statistical value accumulated over the
              number of acquisitions ('NUMber') taken at the time the command was given.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:RESULTs:MINimum?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:MINimum?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - COUnter:RESULTs:MINimum?
            ```
        """
        return self._minimum

    @property
    def number(self) -> CounterResultsNumber:
        """Return the ``COUnter:RESULTs:NUMber`` command.

        Description:
            - Queries the derived value obtained from the Trigger Source Frequency or A-B Trigger
              Time Interval Applications. The value is the number of acquisitions (NUMber) taken at
              the time the command was given.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:RESULTs:NUMber?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:NUMber?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - COUnter:RESULTs:NUMber?
            ```
        """
        return self._number

    @property
    def value(self) -> CounterResultsValue:
        """Return the ``COUnter:RESULTs:VALue`` command.

        Description:
            - Queries the measured value obtained from the Trigger Source Frequency or A-B Trigger
              Time Interval Applications. The measured quantity is value.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:RESULTs:VALue?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs:VALue?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - COUnter:RESULTs:VALue?
            ```
        """
        return self._value


class Counter(SCPICmdRead):
    """The ``COUnter`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``COUnter?`` query.
        - Using the ``.verify(value)`` method will send the ``COUnter?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.results``: The ``COUnter:RESULTs`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "COUnter") -> None:
        super().__init__(device, cmd_syntax)
        self._results = CounterResults(device, f"{self._cmd_syntax}:RESULTs")

    @property
    def results(self) -> CounterResults:
        """Return the ``COUnter:RESULTs`` command.

        Description:
            - Queries the measured and derived values obtained from the Trigger Source Frequency or
              A-B Trigger Time Interval Applications. The measured quantity is value. The minimum,
              maximum, AVGmean, and Deviation are statistical values accumulated over the number of
              acquisitions (NUMber) taken at the time the command is given. All results are returned
              with the single query ``COUnter:RESULTs?`` Individual results are returned by other
              queries

        Usage:
            - Using the ``.query()`` method will send the ``COUnter:RESULTs?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter:RESULTs?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - COUnter:RESULTs?
            ```

        Sub-properties:
            - ``.avgmean``: The ``COUnter:RESULTs:AVGmean`` command.
            - ``.deviation``: The ``COUnter:RESULTs:DEViation`` command.
            - ``.maximum``: The ``COUnter:RESULTs:MAXimum`` command.
            - ``.minimum``: The ``COUnter:RESULTs:MINimum`` command.
            - ``.number``: The ``COUnter:RESULTs:NUMber`` command.
            - ``.value``: The ``COUnter:RESULTs:VALue`` command.
        """
        return self._results
