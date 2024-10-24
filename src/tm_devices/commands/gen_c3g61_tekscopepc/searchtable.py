"""The searchtable commands module.

These commands are used in the following models:
TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SEARCHTABle {ADDNew|DELete} <qstring>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Searchtable(SCPICmdWrite):
    """The ``SEARCHTABle`` command.

    Description:
        - This command adds or deletes a new search event table in an Option 5-WIN (Microsoft
          Windows 10 OS) TekExpress compliance testing application.

    Usage:
        - Using the ``.write(value)`` method will send the ``SEARCHTABle value`` command.

    SCPI Syntax:
        ```
        - SEARCHTABle {ADDNew|DELete} <qstring>
        ```

    Info:
        - ``ADDNew`` adds a new search events table in the display area.
        - ``DELete`` removes a displayed search events table from the display area.
        - ``<qstring>`` contains the name of the search table.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "SEARCHTABle"
    ) -> None:
        super().__init__(device, cmd_syntax)
