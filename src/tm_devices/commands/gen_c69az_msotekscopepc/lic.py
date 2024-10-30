"""The lic commands module.

These commands are used in the following models:
MSO2, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - LIC:UNINSTALL? <QString>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class LicUninstall(SCPICmdReadWithArguments):
    """The ``LIC:UNINSTALL`` command.

    Description:
        - Returns the exit license indicated for the user to return to their TekAMS account. Active
          licenses can be specified by their nomenclature. TransactionIDs can be used to specify an
          active license or a previously uninstalled license. In either case, the exit-license is
          returned as block-data.

    Usage:
        - Using the ``.query(argument)`` method will send the ``LIC:UNINSTALL? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``LIC:UNINSTALL? argument``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - LIC:UNINSTALL? <QString>
        ```

    Info:
        - ``<QString>`` is the nomenclature of an active license or a TransactionIDs to specify an
          active license or a previously uninstalled license.
    """


class Lic(SCPICmdRead):
    """The ``LIC`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``LIC?`` query.
        - Using the ``.verify(value)`` method will send the ``LIC?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.uninstall``: The ``LIC:UNINSTALL`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "LIC") -> None:
        super().__init__(device, cmd_syntax)
        self._uninstall = LicUninstall(device, f"{self._cmd_syntax}:UNINSTALL")

    @property
    def uninstall(self) -> LicUninstall:
        """Return the ``LIC:UNINSTALL`` command.

        Description:
            - Returns the exit license indicated for the user to return to their TekAMS account.
              Active licenses can be specified by their nomenclature. TransactionIDs can be used to
              specify an active license or a previously uninstalled license. In either case, the
              exit-license is returned as block-data.

        Usage:
            - Using the ``.query(argument)`` method will send the ``LIC:UNINSTALL? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``LIC:UNINSTALL? argument`` query and raise an AssertionError if the returned value
              does not match ``value``.

        SCPI Syntax:
            ```
            - LIC:UNINSTALL? <QString>
            ```

        Info:
            - ``<QString>`` is the nomenclature of an active license or a TransactionIDs to specify
              an active license or a previously uninstalled license.
        """
        return self._uninstall
