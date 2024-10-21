"""The idnmultiscope commands module.

These commands are used in the following models:
DPO70KSX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - IDNMultiscope:A?
    - IDNMultiscope:B?
    - IDNMultiscope:C?
    - IDNMultiscope:D?
    - IDNMultiscope?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class IdnmultiscopeDigitalBit(SCPICmdRead):
    """The ``IDNMultiscope:D`` command.

    Description:
        - This query returns the ``*IDN?`` response for Extension 3. If the query is not run on the
          master instrument, data returned indicates that the instrument is running as a StandAlone
          Master. DPO70000SX Series only.

    Usage:
        - Using the ``.query()`` method will send the ``IDNMultiscope:D?`` query.
        - Using the ``.verify(value)`` method will send the ``IDNMultiscope:D?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - IDNMultiscope:D?
        ```
    """


class IdnmultiscopeC(SCPICmdRead):
    """The ``IDNMultiscope:C`` command.

    Description:
        - This query returns the ``*IDN?`` response for Extension 2. If the query is not run on the
          master instrument, data returned indicates that the instrument is running as a StandAlone
          Master. DPO70000SX Series only.

    Usage:
        - Using the ``.query()`` method will send the ``IDNMultiscope:C?`` query.
        - Using the ``.verify(value)`` method will send the ``IDNMultiscope:C?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - IDNMultiscope:C?
        ```
    """


class IdnmultiscopeB(SCPICmdRead):
    """The ``IDNMultiscope:B`` command.

    Description:
        - This query returns the ``*IDN?`` response for Extension 1. If the query is not run on the
          master instrument, data returned indicates that the instrument is running as a StandAlone
          Master. DPO70000SX Series only.

    Usage:
        - Using the ``.query()`` method will send the ``IDNMultiscope:B?`` query.
        - Using the ``.verify(value)`` method will send the ``IDNMultiscope:B?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - IDNMultiscope:B?
        ```
    """


class IdnmultiscopeA(SCPICmdRead):
    """The ``IDNMultiscope:A`` command.

    Description:
        - This query returns the ``*IDN?`` response for the Master instrument. If the query is not
          run on the master instrument, data returned indicates that the instrument is running as a
          StandAlone Master. DPO70000SX Series only.

    Usage:
        - Using the ``.query()`` method will send the ``IDNMultiscope:A?`` query.
        - Using the ``.verify(value)`` method will send the ``IDNMultiscope:A?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - IDNMultiscope:A?
        ```
    """


class Idnmultiscope(SCPICmdRead):
    """The ``IDNMultiscope`` command.

    Description:
        - This query returns instrument data on all MultiScope instruments. If the query is not run
          on the master instrument, data returned indicates that the instrument is running as a
          StandAlone Master. DPO70000SX Series only.

    Usage:
        - Using the ``.query()`` method will send the ``IDNMultiscope?`` query.
        - Using the ``.verify(value)`` method will send the ``IDNMultiscope?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - IDNMultiscope?
        ```

    Properties:
        - ``.a``: The ``IDNMultiscope:A`` command.
        - ``.b``: The ``IDNMultiscope:B`` command.
        - ``.c``: The ``IDNMultiscope:C`` command.
        - ``.d``: The ``IDNMultiscope:D`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "IDNMultiscope"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._a = IdnmultiscopeA(device, f"{self._cmd_syntax}:A")
        self._b = IdnmultiscopeB(device, f"{self._cmd_syntax}:B")
        self._c = IdnmultiscopeC(device, f"{self._cmd_syntax}:C")
        self._d = IdnmultiscopeDigitalBit(device, f"{self._cmd_syntax}:D")

    @property
    def a(self) -> IdnmultiscopeA:
        """Return the ``IDNMultiscope:A`` command.

        Description:
            - This query returns the ``*IDN?`` response for the Master instrument. If the query is
              not run on the master instrument, data returned indicates that the instrument is
              running as a StandAlone Master. DPO70000SX Series only.

        Usage:
            - Using the ``.query()`` method will send the ``IDNMultiscope:A?`` query.
            - Using the ``.verify(value)`` method will send the ``IDNMultiscope:A?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - IDNMultiscope:A?
            ```
        """
        return self._a

    @property
    def b(self) -> IdnmultiscopeB:
        """Return the ``IDNMultiscope:B`` command.

        Description:
            - This query returns the ``*IDN?`` response for Extension 1. If the query is not run on
              the master instrument, data returned indicates that the instrument is running as a
              StandAlone Master. DPO70000SX Series only.

        Usage:
            - Using the ``.query()`` method will send the ``IDNMultiscope:B?`` query.
            - Using the ``.verify(value)`` method will send the ``IDNMultiscope:B?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - IDNMultiscope:B?
            ```
        """
        return self._b

    @property
    def c(self) -> IdnmultiscopeC:
        """Return the ``IDNMultiscope:C`` command.

        Description:
            - This query returns the ``*IDN?`` response for Extension 2. If the query is not run on
              the master instrument, data returned indicates that the instrument is running as a
              StandAlone Master. DPO70000SX Series only.

        Usage:
            - Using the ``.query()`` method will send the ``IDNMultiscope:C?`` query.
            - Using the ``.verify(value)`` method will send the ``IDNMultiscope:C?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - IDNMultiscope:C?
            ```
        """
        return self._c

    @property
    def d(self) -> IdnmultiscopeDigitalBit:
        """Return the ``IDNMultiscope:D`` command.

        Description:
            - This query returns the ``*IDN?`` response for Extension 3. If the query is not run on
              the master instrument, data returned indicates that the instrument is running as a
              StandAlone Master. DPO70000SX Series only.

        Usage:
            - Using the ``.query()`` method will send the ``IDNMultiscope:D?`` query.
            - Using the ``.verify(value)`` method will send the ``IDNMultiscope:D?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - IDNMultiscope:D?
            ```
        """
        return self._d
