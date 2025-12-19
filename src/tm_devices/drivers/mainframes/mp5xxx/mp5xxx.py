"""Base MF 5xxx device driver module."""

from __future__ import annotations

import inspect
import logging

from abc import ABC
from typing import List, Tuple, TYPE_CHECKING, Union

from tm_devices.driver_mixins.device_control.tsp_control import TSPControl
from tm_devices.driver_mixins.shared_implementations import CommonTSPErrorCheckMixin
from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.mainframes.mainframe import Mainframe

# noinspection PyPep8Naming
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

if TYPE_CHECKING:
    from tm_devices.commands import MPSU50_2STCommands, MSMU60_2Commands
    from tm_devices.commands.gen_3skc3w_mp.slot import SlotItem


_POWER_SUPPLY_UNIT_MODULES = ["MPSU50-2ST"]
_SOURCE_MEASUREMENT_UNIT_MODULES = ["MSMU60-2"]

_logger: logging.Logger = logging.getLogger(__name__)


@family_base_class
class MP5xxx(CommonTSPErrorCheckMixin, TSPControl, Mainframe, ABC):
    """Base MP5xxx device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def all_slot_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the slot names."""
        return tuple(f"{x + 1}" for x in range(self.total_slots))

    @cached_property
    def total_slots(self) -> int:
        """Return the total number of slots."""
        return int(self.model[5])

    @property
    def all_channel_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the channel names of a module."""
        return tuple(f"{x + 1}" for x in range(self.total_channels))

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels across all modules."""
        total_channels = 0
        for slot in range(1, self.total_slots + 1):
            model_returned = self.query(f"print(slot[{slot}].model)")
            # TODO: Modify the logic to determine channel based on return type
            channels_in_module = int(
                next((char for char in reversed(str(model_returned)) if char.isdigit()), 0)
            )
            total_channels += channels_in_module
        return total_channels

    ################################################################################################
    # Public Methods
    ################################################################################################
    def get_module_commands_psu(self, slot: int) -> Union[MPSU50_2STCommands, SlotItem]:
        """Get a power supply unit (PSU) module commands object from the mainframe.

        Args:
            slot (int): The slot number of the PSU module.

        Returns:
            The PSU commands associated with the specified slot.

        Raises:
            ValueError: If no module is available in the specified slot.
            TypeError: If the module in the slot is not one of the supported PSU modules.
        """
        return self._get_module_commands_api("PSU", _POWER_SUPPLY_UNIT_MODULES, slot)

    def get_module_commands_smu(self, slot: int) -> Union[MSMU60_2Commands, SlotItem]:
        """Get a Source Measure Unit (SMU) module commands object from the mainframe.

        Args:
            slot (int): The slot number of the SMU module.

        Returns:
            The SMU commands associated with the specified slot.

        Raises:
            ValueError: If no module is available in the specified slot.
            TypeError: If the module in the slot is not one of the supported SMU modules.
        """
        return self._get_module_commands_api("SMU", _SOURCE_MEASUREMENT_UNIT_MODULES, slot)

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _get_module_commands_api(
        self, module_type: str, module_alias: List[str], slot: int
    ) -> SlotItem:
        """Get the module commands object for the specific module_type.

        Args:
            module_type : The type of module being accessed.
            module_alias: List of supported module aliases.
            slot: The slot number of the module.

        Returns:
            The commands API for the module in the given slot.

        Raises:
            ValueError: If the slot number is not between one and the total
                        number of slots (inclusive), if no module is available
                        in the specified slot, or if an invalid module is detected.
            TypeError: If the slot number is not an integer, or
                       if the module in the slot is not supported.
        """
        if not isinstance(slot, int):  # pyright: ignore[reportUnnecessaryIsInstance]
            msg = (
                f"{slot} of type {type(slot).__name__} is not a valid slot number."
                " A valid slot number must be an integer."
            )
            raise TypeError(msg)

        if not 1 <= slot <= self.total_slots:
            msg = (
                f"Slot number {slot} is out of range. It must be between 1 and {self.total_slots}."
            )
            raise ValueError(msg)

        try:
            model_returned = self.query(f"print(slot[{slot}].model)")
            if model_returned.find("-") == -1:
                msg = f"{model_returned} Module in slot {slot} is an invalid module."
                raise ValueError(msg)  # noqa: TRY301

            if model_returned in module_alias:
                _logger.debug("Module '%s' commands are accessible.", model_returned)
                return self.commands.slot[slot]

            supported_modules = ", ".join(module_alias)

            installed_module = self.query(f"print(slot[{slot}].model)")
            msg = (
                f"No supported {module_type} module found in slot {slot}. "
                f"The supported {module_type} modules are: {supported_modules}. "
                f"Currently installed module: {installed_module}."
            )
            raise TypeError(msg)
        except ValueError as error:
            msg = f"Error encountered while accessing module commands object: {error}"
            raise ValueError(msg) from error

    ################################################################################################
    # Private Methods
    ################################################################################################
    def _reboot(self) -> None:
        """Perform the actual rebooting code.

        Raises:
            NotImplementedError: Indicates the current driver has not implemented this method.
        """
        # TODO: implement
        raise NotImplementedError(
            f"``.{inspect.currentframe().f_code.co_name}()``"  # pyright: ignore[reportOptionalMemberAccess]  # noqa: EM102
            f" is not yet implemented for the {self.__class__.__name__} driver"
        )
