"""The source commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SOURce:ROSCillator:SOURce {INTernal|EXTernal}
    - SOURce:ROSCillator:SOURce?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SourceRoscillatorSource(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce:ROSCillator:SOURce`` command.

    Description:
        - This command sets the reference clock to either internal or external.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce:ROSCillator:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce:ROSCillator:SOURce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOURce:ROSCillator:SOURce value``
          command.

    SCPI Syntax:
        ```
        - SOURce:ROSCillator:SOURce {INTernal|EXTernal}
        - SOURce:ROSCillator:SOURce?
        ```
    """


class SourceRoscillator(SCPICmdRead):
    """The ``SOURce:ROSCillator`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce:ROSCillator?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce:ROSCillator?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``SOURce:ROSCillator:SOURce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = SourceRoscillatorSource(device, f"{self._cmd_syntax}:SOURce")

    @property
    def source(self) -> SourceRoscillatorSource:
        """Return the ``SOURce:ROSCillator:SOURce`` command.

        Description:
            - This command sets the reference clock to either internal or external.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce:ROSCillator:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce:ROSCillator:SOURce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOURce:ROSCillator:SOURce value``
              command.

        SCPI Syntax:
            ```
            - SOURce:ROSCillator:SOURce {INTernal|EXTernal}
            - SOURce:ROSCillator:SOURce?
            ```
        """
        return self._source


class Source(SCPICmdRead):
    """The ``SOURce`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.roscillator``: The ``SOURce:ROSCillator`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SOURce") -> None:
        super().__init__(device, cmd_syntax)
        self._roscillator = SourceRoscillator(device, f"{self._cmd_syntax}:ROSCillator")

    @property
    def roscillator(self) -> SourceRoscillator:
        """Return the ``SOURce:ROSCillator`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce:ROSCillator?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce:ROSCillator?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``SOURce:ROSCillator:SOURce`` command.
        """
        return self._roscillator
