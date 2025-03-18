"""A collection of classes and other helpful objects to use when generating SCPI drivers.

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

import re
import string
import sys

from collections import defaultdict
from typing import Any, cast, DefaultDict, Optional, Set, Tuple, Type, TYPE_CHECKING, Union

from .generic_commands import BaseCmd, END_OF_STRING_DIGITS, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl

MAX_CHANNELS = 8
MAX_DIGITAL_BITS = 16
END_OF_STRING_NUMBER = re.compile(r"(\d+)$")
# TODO: Drop Python 3.8: Once Python 3.8 is no longer supported,
#  the dynamic parent class can be removed
# pylint: disable=unsubscriptable-object,useless-suppression
ParentDefaultDictClass: Type[DefaultDict[Any, Any]] = (
    defaultdict if sys.version_info < (3, 9) else defaultdict[Any, Any]
)


####################################################################################################
# Classes
####################################################################################################
class BaseSCPICmd(BaseCmd):  # pylint: disable=too-few-public-methods
    """A class to better type hint a member of a SCPI command tree."""

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._device: Optional["PIControl"] = device


class SCPICmdRead(BaseSCPICmd):
    """A class defining a queryable SCPI command."""

    def query(self) -> str:
        """Return the result of the SCPI query.

        Sends the query ``.cmd_syntax + '?'``.

        This method will query the device using the ``device.query()`` method and return the result
        after stripping out leading and trailing whitespace.

        Returns:
            The query response from the device.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(self._cmd_syntax + "?")  # type: ignore[union-attr]
        except AttributeError as error:
            msg = "No PIControl object was provided, the .query() method cannot be used."
            raise NoDeviceProvidedError(msg) from error

    def verify(self, value: Union[float, str]) -> Tuple[bool, str]:
        """Verify the return value from the SCPI query matches the value.

        Sends the query ``.cmd_syntax + '?'``.

        This method will use the ``device.query_response()`` method to verify that the value
        returned by the device matches the expected value. An ``AssertionError`` will be raised by
        default if the values don't match.

        Args:
            value: The value to verify against the returned value from the device.

        Returns:
            A tuple containing a boolean indicating if the values match and a string with the actual
            return value from the device.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query_response(  # type: ignore[union-attr]
                self._cmd_syntax + "?", value
            )
        except AttributeError as error:
            msg = "No PIControl object was provided, the .verify() method cannot be used."
            raise NoDeviceProvidedError(msg) from error


class SCPICmdReadWithArguments(BaseSCPICmd):
    """A class defining a SCPI command that can be queried with arguments."""

    _WRAP_ARG_WITH_QUOTES = False

    def query(self, argument: str) -> str:
        """Return the result of the SCPI query.

        Sends the query ``.cmd_syntax + '? argument'``.

        This method will query the device using the ``device.query()`` method and return the result
        after stripping out leading and trailing whitespace.

        Args:
            argument: The argument to send with the query.

        Returns:
            The query response from the device.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        argument = '"' + argument.strip('"') + '"' if self._WRAP_ARG_WITH_QUOTES else argument
        try:
            return self._device.query(  # type: ignore[union-attr]
                self._cmd_syntax + f"? {argument}".strip()
            )
        except AttributeError as error:
            msg = "No PIControl object was provided, the .query() method cannot be used."
            raise NoDeviceProvidedError(msg) from error

    def verify(self, argument: str, value: Union[float, str]) -> Tuple[bool, str]:
        """Verify the return value from the SCPI query matches the value.

        Sends the query ``.cmd_syntax + '? argument'``.

        This method will use the ``device.query_response()`` method to verify that the value
        returned by the device matches the expected value. An ``AssertionError`` will be raised by
        default if the values don't match.

        Args:
            argument: The argument to send with the query.
            value: The value to verify against the returned value from the device.

        Returns:
            A tuple containing a boolean indicating if the values match and a string with the actual
            return value from the device.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        argument = '"' + argument.strip('"') + '"' if self._WRAP_ARG_WITH_QUOTES else argument
        try:
            return self._device.query_response(  # type: ignore[union-attr]
                self._cmd_syntax + f"? {argument}".strip(), value
            )
        except AttributeError as error:
            msg = "No PIControl object was provided, the .verify() method cannot be used."
            raise NoDeviceProvidedError(msg) from error


class SCPICmdWrite(BaseSCPICmd):
    """A class defining a writable SCPI command."""

    _WRAP_ARG_WITH_QUOTES = False

    def write(self, value: Union[float, str], verify: bool = False) -> str:
        """Send the SCPI command (``.cmd_syntax``) with the provided value to the device.

        Args:
            value: The value to write to the device.
            verify: A boolean indicating that ``device.set_and_check()`` should be used.

        Returns:
            The value from the query when verification is enabled, otherwise an empty string.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        value = (
            '"' + value.strip('"') + '"'
            if self._WRAP_ARG_WITH_QUOTES and isinstance(value, str)
            else value
        )
        try:
            if verify or self._device.command_verification_enabled:  # type: ignore[union-attr]
                return self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax, value
                )
            self._device.write(f"{self._cmd_syntax} {value}")  # type: ignore[union-attr]
        except AttributeError as error:
            msg = "No PIControl object was provided, the .write() method cannot be used."
            raise NoDeviceProvidedError(msg) from error
        return ""


class SCPICmdWriteNoArguments(BaseSCPICmd):
    """A class defining a writable SCPI command which doesn't have any arguments."""

    def write(self) -> None:
        """Send the SCPI command (``.cmd_syntax``) to the device.

        This method will use the ``device.write()`` method to send the command.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(self._cmd_syntax)  # type: ignore[union-attr]
        except AttributeError as error:
            msg = "No PIControl object was provided, the .write() method cannot be used."
            raise NoDeviceProvidedError(msg) from error


class ValidatedDigitalBit(BaseSCPICmd):  # pylint: disable=too-few-public-methods
    """A mixin class that is used to validate the digital bit is valid.

    This class checks the digital bit number at the end of the SCPI syntax (``.cmd_syntax``
    attribute) to determine if it is a valid digital bit number (within the range of 0 to the
    maximum number of digital bits on the device).
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)

        # Validate the bit number is correct
        bit_number_list = set(range(getattr(device, "num_dig_bits_in_ch", MAX_DIGITAL_BITS)))
        bit_num = int(
            END_OF_STRING_DIGITS.search(self._cmd_syntax).group(1)  # type: ignore[union-attr]
        )
        if bit_num not in bit_number_list:
            msg = f"{bit_num=} is not a valid bit number, valid bit numbers: {bit_number_list}"
            raise ValueError(msg)


class ValidatedChannel(BaseCmd):  # pylint: disable=too-few-public-methods
    """A mixin class that is used to validate the channel is valid.

    This class checks the channel number (or string) at the end of the syntax (``.cmd_syntax``
    attribute) to determine if it is a valid channel number (within the range of the available
    channels on the device).
    """

    def __init__(self, device: Optional["Any"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)

        # Validate the channel
        channel: Union[str, int]
        valid_channels: Set[Union[str, int]]
        if device is not None and hasattr(device, "all_channel_names_list"):
            valid_channel_strings: Set[str] = set(device.all_channel_names_list)
        else:
            valid_channel_numbers = set(range(1, MAX_CHANNELS + 1))
            valid_channel_strings = {f"CH{x}" for x in valid_channel_numbers}

        # Find the current channel
        uses_integer_channels = all(ch_name[-1].isdigit() for ch_name in valid_channel_strings)
        if uses_integer_channels:
            valid_channels: Set[Union[str, int]] = {
                int(number_match)
                for ch_name in valid_channel_strings
                for number_match in END_OF_STRING_NUMBER.findall(ch_name)
            }
            if (digit_match := END_OF_STRING_DIGITS.search(self._cmd_syntax)) is not None:
                channel = int(digit_match.group(1))
            else:
                msg = f"No channel number was detected in the command syntax '{self._cmd_syntax}'"
                raise ValueError(msg)
        else:
            valid_channels = cast("Set[Union[str, int]]", valid_channel_strings)
            # Check if the channel "number" is actually a letter
            if (last_letter := self._cmd_syntax[-1]) in string.ascii_lowercase:
                channel = last_letter
            else:
                msg = f"No channel was detected in the command syntax '{self._cmd_syntax}'"
                raise ValueError(msg)

        # Check if the channel is valid
        if channel not in valid_channels:
            msg = f"{channel=} is not a valid channel, valid channels: {valid_channels}"
            raise ValueError(msg)


class DefaultDictDeviceCommunication(ParentDefaultDictClass):
    """A custom default dictionary that can be used to send/receive commands to/from a device.

    The ``.query()`` method is used when ``__getitem__()`` is called and the result of the query is
    returned instead of a standard value.

    The ``.write()`` method is used when ``__setitem__()`` is called.
    """

    def __init__(
        self,
        cmd_syntax: str,
        query_syntax: str,
        write_syntax: Optional[str] = None,
        device: Optional["PIControl"] = None,
        **kwargs: Any,
    ) -> None:
        """Create an instance of the class.

        Args:
            cmd_syntax: The general syntax of the command, the substring that will need
                to be replaced with the key's value should be ``{key}``.
            query_syntax: The syntax to send to the device as a query, the substring that will need
                to be replaced with the key's value should be ``{key}``.
            write_syntax: The syntax to write to the device, the substring that will need
                to be replaced with the key's value should be ``{key}``.
            device: The device to send the query to.
            kwargs: The keyword arguments.
        """
        super().__init__(**kwargs)
        self._cmd_syntax = cmd_syntax
        self._query_syntax = query_syntax
        self._write_syntax = write_syntax
        self._device = device

    def __setitem__(self, key: Any, value: Any) -> None:
        """Send a command to the device if possible.

        Args:
            key: The mapping item to use to modify the syntax.
            value: The value to write to the device.

        Raises:
            AttributeError: Indicates that the attribute is read-only.
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        if self._write_syntax is None:
            msg = f"``{self._cmd_syntax.format(key=key)}`` is a read-only attribute"
            raise AttributeError(msg)
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax.format(key=key), value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    self._write_syntax.format(key=key).strip() + " " + str(value)
                )
        except AttributeError as error:
            msg = "No Device object was provided, unable to write the command to the device."
            raise NoDeviceProvidedError(msg) from error

    def __getitem__(self, key: Any) -> str:
        """Query the device and return the result.

        Args:
            key: The mapping item to include in the query.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax.format(key=key)
            return self._device.query(  # type: ignore[union-attr]
                self._query_syntax.format(key=key)
            )
        except AttributeError as error:
            msg = "No Device object was provided, unable to send query."
            raise NoDeviceProvidedError(msg) from error
