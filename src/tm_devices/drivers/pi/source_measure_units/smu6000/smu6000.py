"""Base SMU 6000 device driver module."""
from __future__ import annotations

import inspect

from abc import ABC
from functools import cached_property
from typing import Optional, Tuple, TYPE_CHECKING, Union

from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.pi._ieee488_2_commands import IEEE4882Commands
from tm_devices.drivers.pi.pi_device import PIDevice
from tm_devices.drivers.pi.signal_sources.signal_source import SignalSource
from tm_devices.drivers.pi.source_measure_units.source_measure_unit import SourceMeasureUnit

if TYPE_CHECKING:
    import os


@family_base_class
class SMU6000(SourceMeasureUnit, ABC):
    """Base SMU6000 device driver."""

    _IEEE_COMMANDS_CLASS = IEEE4882Commands

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def all_channel_names_list(self) -> Tuple[str, ...]:
        """Return a tuple containing all the channel names."""
        return tuple(f"SOURCE{x+1}" for x in range(self.total_channels))

    @property
    def ieee_cmds(self) -> IEEE4882Commands:  # pyright: ignore [reportIncompatibleMethodOverride]
        """Return an internal class containing methods for the standard IEEE 488.2 command set."""
        return self._ieee_cmds

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of channels (all types)."""
        return 1

    ################################################################################################
    # Public Methods
    ################################################################################################
    def expect_esr(self, esr: Union[int, str], error_string: str = "") -> Tuple[bool, str]:
        r"""Check for the expected number of errors and output string.

        Sends the ``*ESR?`` and SYSTEM:ERROR? queries.

        Args:
            esr: Expected ``*ESR?`` value
            error_string: Expected error buffer string.
                Multiple errors should be separated by a \n character

        Returns:
            Boolean indicating if the check passed or failed and a string with the results.
        """
        return SignalSource.expect_esr(self, esr, error_string)  # type: ignore

    def get_eventlog_status(self) -> Tuple[bool, str]:
        """Help function for getting the eventlog status.

        Returns:
            Boolean indicating no error, String containing concatenated contents of event log.
        """
        return SignalSource.get_eventlog_status(self)  # type: ignore

    def run_script(self, script_name: str) -> None:  # noqa: ARG002
        """Not Implemented."""
        msg = f"This functionality is not available on the {self.__class__.__name__} instrument."
        raise NotImplementedError(msg)

    def set_and_check(  # noqa: PLR0913
        self,
        command: str,
        value: Union[str, float],
        tolerance: float = 0,
        percentage: bool = False,
        remove_quotes: bool = False,
        custom_message_prefix: str = "",
        *,
        expected_value: Optional[Union[str, float]] = None,
    ) -> str:
        """Send the given command with the given value and then verify the results.

        Args:
            command: The command to send.
                For example: ``:AFG:FUNCTION``
            value: The value being set by the command.
                For example: ``SINE``
            tolerance: The acceptable difference between two floating point values.
            percentage: A boolean indicating what kind of tolerance check to perform.
                 False means absolute tolerance: +/- tolerance.
                 True means percent tolerance: +/- (tolerance / 100) * value.
            remove_quotes: Set this to True to remove all double quotes from the returned value.
            custom_message_prefix: A custom message to be prepended to the failure message.
            expected_value: An optional, alternative value expected to be returned.

        Returns:
            The output of the query portion of the method.
        """
        return PIDevice.set_and_check(
            self,
            command,
            value,
            tolerance,
            percentage,
            remove_quotes,
            custom_message_prefix,
            expected_value=expected_value,
        )

    def load_script(
        self,
        file_path: Union[str, os.PathLike[str]],  # noqa: ARG002
        script_name: str = "",  # noqa: ARG002
        *,
        run_script: bool = False,  # noqa: ARG002
        to_nv_memory: bool = False,  # noqa: ARG002
    ) -> None:
        """Not Implemented."""
        msg = f"This functionality is not available on the {self.__class__.__name__} instrument."
        raise NotImplementedError(msg)

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
            f"``.{inspect.currentframe().f_code.co_name}()``"  # pyright: ignore
            f" is not yet implemented for the {self.__class__.__name__} driver"
        )
