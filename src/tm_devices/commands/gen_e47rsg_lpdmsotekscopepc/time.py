"""The time commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - TIMe <QString>
    - TIMe:ZONe <QString>
    - TIMe:ZONe:UTCDELTa <NR3>
    - TIMe:ZONe:UTCDELTa?
    - TIMe:ZONe?
    - TIMe?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class TimeZoneUtcdelta(SCPICmdWrite, SCPICmdRead):
    """The ``TIMe:ZONe:UTCDELTa`` command.

    Description:
        - This command sets or queries the time zone using the difference between the desired time
          zone and UTC.

    Usage:
        - Using the ``.query()`` method will send the ``TIMe:ZONe:UTCDELTa?`` query.
        - Using the ``.verify(value)`` method will send the ``TIMe:ZONe:UTCDELTa?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TIMe:ZONe:UTCDELTa value`` command.

    SCPI Syntax:
        ```
        - TIMe:ZONe:UTCDELTa <NR3>
        - TIMe:ZONe:UTCDELTa?
        ```

    Info:
        - ``<NR3>`` is the specified number of hours difference between the desired time zone and
          UTC which is equivalent to GMT. The deltas supported are: -12.00, -11.00, -10.00, -9.30,
          -9.00, -8.30, -8.00, -7.00, -6.00, -5.00, -4.00, -3.30, -3.00, -2.00, -1.00, 0.0, 1.00,
          2.00, 3.00, 3.30, 4.00, 4.30, 5.00, 5.30, 6.00, 6.30, 7.00, 8.00, 9.00, 9.30, 10.00,
          10.30, 11.00, 11.30, 12.00.
    """


class TimeZone(SCPICmdWrite, SCPICmdRead):
    """The ``TIMe:ZONe`` command.

    Description:
        - This command sets the time zone to the one specified.

    Usage:
        - Using the ``.query()`` method will send the ``TIMe:ZONe?`` query.
        - Using the ``.verify(value)`` method will send the ``TIMe:ZONe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TIMe:ZONe value`` command.

    SCPI Syntax:
        ```
        - TIMe:ZONe <QString>
        - TIMe:ZONe?
        ```

    Info:
        - ``<QString>`` is a quoted string representing the desired time zone.

    Properties:
        - ``.utcdelta``: The ``TIMe:ZONe:UTCDELTa`` command.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._utcdelta = TimeZoneUtcdelta(device, f"{self._cmd_syntax}:UTCDELTa")

    @property
    def utcdelta(self) -> TimeZoneUtcdelta:
        """Return the ``TIMe:ZONe:UTCDELTa`` command.

        Description:
            - This command sets or queries the time zone using the difference between the desired
              time zone and UTC.

        Usage:
            - Using the ``.query()`` method will send the ``TIMe:ZONe:UTCDELTa?`` query.
            - Using the ``.verify(value)`` method will send the ``TIMe:ZONe:UTCDELTa?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TIMe:ZONe:UTCDELTa value`` command.

        SCPI Syntax:
            ```
            - TIMe:ZONe:UTCDELTa <NR3>
            - TIMe:ZONe:UTCDELTa?
            ```

        Info:
            - ``<NR3>`` is the specified number of hours difference between the desired time zone
              and UTC which is equivalent to GMT. The deltas supported are: -12.00, -11.00, -10.00,
              -9.30, -9.00, -8.30, -8.00, -7.00, -6.00, -5.00, -4.00, -3.30, -3.00, -2.00, -1.00,
              0.0, 1.00, 2.00, 3.00, 3.30, 4.00, 4.30, 5.00, 5.30, 6.00, 6.30, 7.00, 8.00, 9.00,
              9.30, 10.00, 10.30, 11.00, 11.30, 12.00.
        """
        return self._utcdelta


class Time(SCPICmdWrite, SCPICmdRead):
    """The ``TIMe`` command.

    Description:
        - This command sets the time in the form ``hh:mm:ss`` where hh refers to a two-digit hour
          number, mm refers to a two-digit minute number from 01 to 60, and ss refers to a two-digit
          second number from 01 to 60.

    Usage:
        - Using the ``.query()`` method will send the ``TIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``TIMe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TIMe value`` command.

    SCPI Syntax:
        ```
        - TIMe <QString>
        - TIMe?
        ```

    Info:
        - ``<QString>`` is a quoted string representing the desired time.

    Properties:
        - ``.zone``: The ``TIMe:ZONe`` command.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "TIMe") -> None:
        super().__init__(device, cmd_syntax)
        self._zone = TimeZone(device, f"{self._cmd_syntax}:ZONe")

    @property
    def zone(self) -> TimeZone:
        """Return the ``TIMe:ZONe`` command.

        Description:
            - This command sets the time zone to the one specified.

        Usage:
            - Using the ``.query()`` method will send the ``TIMe:ZONe?`` query.
            - Using the ``.verify(value)`` method will send the ``TIMe:ZONe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TIMe:ZONe value`` command.

        SCPI Syntax:
            ```
            - TIMe:ZONe <QString>
            - TIMe:ZONe?
            ```

        Info:
            - ``<QString>`` is a quoted string representing the desired time zone.

        Sub-properties:
            - ``.utcdelta``: The ``TIMe:ZONe:UTCDELTa`` command.
        """
        return self._zone
