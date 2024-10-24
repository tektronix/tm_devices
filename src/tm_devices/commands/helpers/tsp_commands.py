"""A collection of classes and other helpful objects to use when generating TSP drivers.

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

from typing import Any, Dict, Optional, TYPE_CHECKING

from .generic_commands import BaseCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


####################################################################################################
# Classes
####################################################################################################
class BaseTSPCmd(BaseCmd):  # pylint: disable=too-few-public-methods
    """A class to better type hint a member of a TSP command tree."""

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._device: Optional["TSPControl"] = device

    def _get_tsp_table_dict(self, table: str) -> Dict[Any, Any]:
        """Get the full content of a TSP table variable.

        Args:
            table: The name of the TSP table variable

        Returns:
            A dict with all the table content.
        """
        keys = self._device.query(  # type: ignore[union-attr]
            f's="" for k,v in pairs({table}) do s = s..k.."; " end print(s)'
        ).split("; ")
        table_dict: Dict[Any, Any] = {}
        for key in filter(None, keys):
            if (
                self._device.query(f"print(type({table}.{key}))")  # type: ignore[union-attr]
                == "table"
            ):
                table_dict[key] = self._get_tsp_table_dict(f"{table}.{key}")
            else:
                table_dict[key] = self._device.query(  # type: ignore[union-attr]
                    f"print({table}.{key})"
                )
        return table_dict
