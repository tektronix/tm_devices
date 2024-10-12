# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The localnode commands module.

These commands are used in the following models:
SMU2601B_Pulse

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - localnode.model
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Localnode(BaseTSPCmd):
    """The ``localnode`` command tree.

    Constants:
        - ``.PASSWORD_ALL``: Use passwords on the web interface and all remote command interfaces.
        - ``.PASSWORD_LAN``: Use passwords on the web interface and all LAN interfaces.
        - ``.PASSWORD_NONE``: Disable passwords everywhere.
        - ``.PASSWORD_WEB``: Use passwords on the web interface only.

    Properties and methods:
        - ``.model``: The ``localnode.model`` attribute.
    """

    PASSWORD_ALL = "localnode.PASSWORD_ALL"
    """str: Use passwords on the web interface and all remote command interfaces."""
    PASSWORD_LAN = "localnode.PASSWORD_LAN"
    """str: Use passwords on the web interface and all LAN interfaces."""
    PASSWORD_NONE = "localnode.PASSWORD_NONE"
    """str: Disable passwords everywhere."""
    PASSWORD_WEB = "localnode.PASSWORD_WEB"
    """str: Use passwords on the web interface only."""

    def __init__(
        self, device: Optional["TSPControl"] = None, cmd_syntax: str = "localnode"
    ) -> None:
        super().__init__(device, cmd_syntax)

    @property
    def model(self) -> str:
        """Access the ``localnode.model`` attribute.

        Description:
            - This attribute stores the model number.

        Usage:
            - Accessing this property will send the ``print(localnode.model)`` query.

        TSP Syntax:
            ```
            - print(localnode.model)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".model"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.model)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.model`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
