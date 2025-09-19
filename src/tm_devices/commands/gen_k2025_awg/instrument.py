"""The instrument commands module.

These commands are used in the following models:
AWG5K, AWG5KC, AWG7K, AWG7KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - INSTrument:COUPle:SOURce <state>
    - INSTrument:COUPle:SOURce?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class InstrumentCoupleSource(SCPICmdWrite, SCPICmdRead):
    r"""The ``INSTrument:COUPle:SOURce`` command.

    Description:
        - This command and query sets or returns the coupled state for a channel.

    Usage:
        - Using the ``.query()`` method will send the ``INSTrument:COUPle:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``INSTrument:COUPle:SOURce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``INSTrument:COUPle:SOURce value``
          command.

    SCPI Syntax:
        ```
        - INSTrument:COUPle:SOURce <state>
        - INSTrument:COUPle:SOURce?
        ```

    Info:
        - ``<state>`` ::={NONE\|PAIR\|ALL}.
        - ``NONE``
        - ``PAIR`` - CH1 to CH2 and CH3 to CH4.
        - ``ALL`` - CH1 to CH2, CH3, and CH4.
    """


class InstrumentCouple(SCPICmdRead):
    """The ``INSTrument:COUPle`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``INSTrument:COUPle?`` query.
        - Using the ``.verify(value)`` method will send the ``INSTrument:COUPle?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``INSTrument:COUPle:SOURce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = InstrumentCoupleSource(device, f"{self._cmd_syntax}:SOURce")

    @property
    def source(self) -> InstrumentCoupleSource:
        r"""Return the ``INSTrument:COUPle:SOURce`` command.

        Description:
            - This command and query sets or returns the coupled state for a channel.

        Usage:
            - Using the ``.query()`` method will send the ``INSTrument:COUPle:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``INSTrument:COUPle:SOURce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``INSTrument:COUPle:SOURce value``
              command.

        SCPI Syntax:
            ```
            - INSTrument:COUPle:SOURce <state>
            - INSTrument:COUPle:SOURce?
            ```

        Info:
            - ``<state>`` ::={NONE\|PAIR\|ALL}.
            - ``NONE``
            - ``PAIR`` - CH1 to CH2 and CH3 to CH4.
            - ``ALL`` - CH1 to CH2, CH3, and CH4.
        """
        return self._source


class Instrument(SCPICmdRead):
    """The ``INSTrument`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``INSTrument?`` query.
        - Using the ``.verify(value)`` method will send the ``INSTrument?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.couple``: The ``INSTrument:COUPle`` command tree.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "INSTrument"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._couple = InstrumentCouple(device, f"{self._cmd_syntax}:COUPle")

    @property
    def couple(self) -> InstrumentCouple:
        """Return the ``INSTrument:COUPle`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``INSTrument:COUPle?`` query.
            - Using the ``.verify(value)`` method will send the ``INSTrument:COUPle?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``INSTrument:COUPle:SOURce`` command.
        """
        return self._couple
