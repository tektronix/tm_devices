"""A class defining methods that VISA devices and control mixins must have."""

import logging

from abc import abstractmethod
from itertools import zip_longest
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
    def expect_esr(  # noqa: C901, # pylint: disable=too-many-locals
        self, esr: int, error_messages: Tuple[str, ...] = (), *, use_regex_match: bool = False
    ) -> bool:
        r"""Checks for the expected esr value and queued error messages.

        Args:
            esr: Expected ``*ESR?`` value as a decimal-weighted integer.
            error_messages: Expected error buffer messages in a tuple.
            use_regex_match: A boolean indicating if the messages should be compared
                using regular expressions. Does not affect the esr value comparison.

        Returns:
            Boolean ``True`` when all checks pass. ``False`` means the checks failed (however,
                failing a check will always result in an AssertionError being raised, so the
                result will not really be usable).

        Raises:
            AssertionError: Indicating that the device's error code and messages don't match the
                expected values.
        """
        check_passed = True
        actual_esr, actual_error_messages = self._get_errors()

        failure_message = (
            f"expect_esr() failed; ESR value {'mis' if esr != actual_esr else ''}match "
            f"(Expected: {esr!r}, Actual: {actual_esr!r})"
        )

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

        index_to_check_zero_error_string = len(error_messages)  # index after last expected message
        # can only check for "No Errors" at end of queue if string pattern defined
        if (check_zero_error_string_once := bool(self._no_error_string)) and error_messages:
            check_zero_error_string_once = error_messages[-1] != self._no_error_string

        # allow zip_longest to pad with None so we can handle it in the loop.
        message_pairs = list(zip_longest(error_messages, actual_error_messages))

        # If ESR is non-zero, there should always be at least one error message pair to check.
        if not message_pairs and actual_esr:
            # Force one loop to use same validation logic
            message_pairs = [(None, None)]
            if not self._no_error_string:
                failure_message += (
                    f"; expected `error_messages` parameter defined (or {self.__class__.__name__}"
                    "._no_error_string defined) when ESR is non-zero"
                )

        # Compare the error messages sequentially
        for pair_index, (expected_message, actual_message) in enumerate(message_pairs):
            # Avoid overwriting loop variables directly
            exp_msg = expected_message
            act_msg = actual_message
            if exp_msg is None:
                # Handle the case where there are more actual messages than expected.
                exp_msg = (
                    f"{self.__class__.__name__}._get_errors() returned more error messages "
                    "than expected"
                )
                if pair_index == index_to_check_zero_error_string and check_zero_error_string_once:
                    # If _no_error_string is defined, use it ONCE (with regex matching enabled).
                    # This allows for implicit handling of the "No Errors" string, but only for
                    # the first unmatched "actual" message after expected_messages is exhausted.
                    # Helpful when "No Errors" is always at the end of the error queue, and as
                    # the default when expected_messages is left empty.
                    exp_msg = self._no_error_string
                    check_zero_error_string_once = False

                if act_msg is None:
                    # Non-zero ESR iff both messages are None
                    # so force a failure with a meaningful message.
                    exp_msg = "None"
                    act_msg = (
                        f"{self.__class__.__name__}._get_errors() must return the response "
                        "from the error message queue query for any non-zero ESR"
                    )

            elif act_msg is None:
                # Handle the case where there are fewer actual messages than expected.
                act_msg = (
                    f"{self.__class__.__name__}._get_errors() did not return enough error messages"
                )

            try:
                verify_values(
                    self.name_and_alias,
                    exp_msg,
                    act_msg,
                    use_regex_match=bool(
                        use_regex_match
                        or (self._no_error_string and exp_msg == self._no_error_string)
                    ),
                    custom_message_prefix=f"expect_esr() error message check #{pair_index + 1}:",
                    condense_printout=False,
                )
            except AssertionError as exc:
                check_passed &= False
                # pad the failure messages with spaces for better readability of multi-line messages
                failure_message += "\n" + exc.args[0].replace("\n", "\n  ")
                _logger.warning(exc)

        if not check_passed:
            raise_failure(self.name_and_alias, failure_message, condense_printout=False)

        return check_passed
