"""The auxoutput commands module.

These commands are used in the following models:
AWG70KA, AWG70KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AUXoutput[n]:SOURce {AFLag|BFLag|CFLag|DFLag|TIMer}
    - AUXoutput[n]:SOURce:CMAPping <channel>
    - AUXoutput[n]:SOURce:CMAPping?
    - AUXoutput[n]:SOURce?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, ValidatedDynamicNumberCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class AuxoutputItemSourceCmapping(SCPICmdWrite, SCPICmdRead):
    """The ``AUXoutput[n]:SOURce:CMAPping`` command.

    Description:
        - This command sets or returns the Auxiliary Output channel mapping.

    Usage:
        - Using the ``.query()`` method will send the ``AUXoutput[n]:SOURce:CMAPping?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXoutput[n]:SOURce:CMAPping?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXoutput[n]:SOURce:CMAPping value``
          command.

    SCPI Syntax:
        ```
        - AUXoutput[n]:SOURce:CMAPping <channel>
        - AUXoutput[n]:SOURce:CMAPping?
        ```
    """


class AuxoutputItemSource(SCPICmdWrite, SCPICmdRead):
    """The ``AUXoutput[n]:SOURce`` command.

    Description:
        - This command sets or returns the signal source for the specified Auxiliary Output
          connector.

    Usage:
        - Using the ``.query()`` method will send the ``AUXoutput[n]:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXoutput[n]:SOURce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXoutput[n]:SOURce value`` command.

    SCPI Syntax:
        ```
        - AUXoutput[n]:SOURce {AFLag|BFLag|CFLag|DFLag|TIMer}
        - AUXoutput[n]:SOURce?
        ```

    Properties:
        - ``.cmapping``: The ``AUXoutput[n]:SOURce:CMAPping`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._cmapping = AuxoutputItemSourceCmapping(device, f"{self._cmd_syntax}:CMAPping")

    @property
    def cmapping(self) -> AuxoutputItemSourceCmapping:
        """Return the ``AUXoutput[n]:SOURce:CMAPping`` command.

        Description:
            - This command sets or returns the Auxiliary Output channel mapping.

        Usage:
            - Using the ``.query()`` method will send the ``AUXoutput[n]:SOURce:CMAPping?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXoutput[n]:SOURce:CMAPping?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``AUXoutput[n]:SOURce:CMAPping value`` command.

        SCPI Syntax:
            ```
            - AUXoutput[n]:SOURce:CMAPping <channel>
            - AUXoutput[n]:SOURce:CMAPping?
            ```
        """
        return self._cmapping


class AuxoutputItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``AUXoutput[n]`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AUXoutput[n]?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXoutput[n]?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``AUXoutput[n]:SOURce`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "AUXoutput[n]"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._source = AuxoutputItemSource(device, f"{self._cmd_syntax}:SOURce")

    @property
    def source(self) -> AuxoutputItemSource:
        """Return the ``AUXoutput[n]:SOURce`` command.

        Description:
            - This command sets or returns the signal source for the specified Auxiliary Output
              connector.

        Usage:
            - Using the ``.query()`` method will send the ``AUXoutput[n]:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXoutput[n]:SOURce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXoutput[n]:SOURce value``
              command.

        SCPI Syntax:
            ```
            - AUXoutput[n]:SOURce {AFLag|BFLag|CFLag|DFLag|TIMer}
            - AUXoutput[n]:SOURce?
            ```

        Sub-properties:
            - ``.cmapping``: The ``AUXoutput[n]:SOURce:CMAPping`` command.
        """
        return self._source
