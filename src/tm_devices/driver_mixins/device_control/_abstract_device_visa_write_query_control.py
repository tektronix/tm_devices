"""A class defining methods that VISA devices and control mixins must have."""

import logging

from abc import abstractmethod
from typing import Any, final, Tuple

from tm_devices.driver_mixins.device_control._abstract_device_control import (
    _AbstractDeviceControl,  # pyright: ignore[reportPrivateUsage]
)
from tm_devices.helpers import raise_failure, verify_values

_logger: logging.Logger = logging.getLogger(__name__)


class _AbstractDeviceVISAWriteQueryControl(_AbstractDeviceControl):  # pyright: ignore[reportUnusedClass]
    """Abstract class defining methods that VISA devices and control mixins must have."""

    @property
    def _no_error_string(self) -> str:
        """A string containing the expected error message when no error is present."""
        return ""

    @abstractmethod
    def query(self, *args: Any, **kwargs: Any) -> str:
        """Query the device."""

    @abstractmethod
    def write(self, *args: Any, **kwargs: Any) -> None:
        """Write to the device."""

    @final
    def expect_esr(
        self, esr: int, error_messages: Tuple[str, ...] = (), *, use_regex_match: bool = False
    ) -> bool:
        r"""Check for the expected error code and messages.

        Args:
            esr: Expected ``*ESR?`` value
            error_messages: Expected error buffer messages in a tuple.
            use_regex_match: A boolean indicating if the error messages should be matched
                using regular expressions.

        Returns:
            A boolean indicating if the check passed or failed, True means the check passed,
                False means the check failed (however, failing the check will always result in an
                AssertionError being raised, so the result will not really be usable).

        Raises:
            AssertionError: Indicating that the device's error code and messages don't match the
                expected values.
        """
        check_passed = True

        if not error_messages:
            error_messages = tuple(filter(None, (self._no_error_string,)))

        actual_esr, actual_error_messages = self._get_errors()

        # Compare the esr value
        try:
            verify_values(
                self.name_and_alias,
                esr,
                actual_esr,
                custom_message_prefix="expect_esr() error code check:",
                condense_printout=False,
            )
        except AssertionError as exc:
            check_passed &= False
            _logger.warning(exc)

        # Compare the error messages
        for expected_message, actual_message in zip(error_messages, actual_error_messages):
            try:
                verify_values(
                    self.name_and_alias,
                    expected_message,
                    actual_message,
                    use_regex_match=use_regex_match,
                    custom_message_prefix="expect_esr() error message check:",
                    condense_printout=False,
                )
            except AssertionError as exc:  # noqa: PERF203
                check_passed &= False
                _logger.warning(exc)

        if not check_passed:
            failure_message = (
                f"expect_esr() failed: error code {actual_esr!r} != {esr!r}; "
                f"error messages {actual_error_messages!r} != {error_messages!r}"
            )
            raise_failure(self.name_and_alias, failure_message, condense_printout=False)

        return check_passed
