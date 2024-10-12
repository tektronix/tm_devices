"""The setup_1 commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SETUp:NAMe <NR1>,<QString>
    - SETUp:NAMe? <NR1>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SetupName(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SETUp:NAMe`` command.

    Description:
        - This command allows you to create (or query) a name for your saved setups. The default
          name for all user setups is 'User.' The default name for factory setups is 'Factory.' This
          command is equivalent to selecting Save As from the File menu, pressing the Setup button,
          selecting the desired setup location, clicking the keyboard icon, and entering your setup
          name.

    Usage:
        - Using the ``.query(argument)`` method will send the ``SETUp:NAMe? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``SETUp:NAMe? argument`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SETUp:NAMe value`` command.

    SCPI Syntax:
        ```
        - SETUp:NAMe <NR1>,<QString>
        - SETUp:NAMe? <NR1>
        ```

    Info:
        - ``<NR1>`` specifies a location in which the setup label is stored. Location values range
          from 1 through 10.
        - ``<QString>`` is a string containing the setup label.
    """


class Setup(SCPICmdRead):
    """The ``SETUp`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SETUp?`` query.
        - Using the ``.verify(value)`` method will send the ``SETUp?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.name``: The ``SETUp:NAMe`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SETUp") -> None:
        super().__init__(device, cmd_syntax)
        self._name = SetupName(device, f"{self._cmd_syntax}:NAMe")

    @property
    def name(self) -> SetupName:
        """Return the ``SETUp:NAMe`` command.

        Description:
            - This command allows you to create (or query) a name for your saved setups. The default
              name for all user setups is 'User.' The default name for factory setups is 'Factory.'
              This command is equivalent to selecting Save As from the File menu, pressing the Setup
              button, selecting the desired setup location, clicking the keyboard icon, and entering
              your setup name.

        Usage:
            - Using the ``.query(argument)`` method will send the ``SETUp:NAMe? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the ``SETUp:NAMe? argument``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SETUp:NAMe value`` command.

        SCPI Syntax:
            ```
            - SETUp:NAMe <NR1>,<QString>
            - SETUp:NAMe? <NR1>
            ```

        Info:
            - ``<NR1>`` specifies a location in which the setup label is stored. Location values
              range from 1 through 10.
            - ``<QString>`` is a string containing the setup label.
        """
        return self._name
