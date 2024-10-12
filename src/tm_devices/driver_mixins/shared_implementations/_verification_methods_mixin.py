"""A class that provides common methods for verifying values."""

from abc import ABC, abstractmethod
from typing import final, Tuple, Union

from tm_devices.helpers import get_timestamp_string


# TODO: nfelt14: convert this entire class to a set of helper functions
class VerificationMethodsMixin(ABC):
    """A mixin class providing common methods for verifying values."""

    ################################################################################################
    # Abstract Properties
    ################################################################################################
    @property
    @abstractmethod
    def _name_and_alias(self) -> str:
        """Return the name and alias of the device."""

    ################################################################################################
    # Public Methods
    ################################################################################################
    @final
    def raise_error(self, message: str) -> None:
        """Raise an AssertionError with the provided message indicating there was an error.

        Args:
            message: The message to add to the AssertionError.

        Raises:
            AssertionError: Prints out the error message with a traceback.
        """
        # Make the message smaller
        message = ", ".join([x.strip() for x in message.split("\n")])
        message = f"{get_timestamp_string()} - ERROR: ({self._name_and_alias}) : {message}"
        raise AssertionError(message)

    @final
    def raise_failure(self, message: str) -> None:
        """Raise an AssertionError with the provided message indicating there was a failure.

        Args:
            message: The message to add to the AssertionError.

        Raises:
            AssertionError: Prints out the failure message with a traceback.
        """
        # Make the message smaller
        message = ", ".join([x.strip() for x in message.split("\n")])
        message = f"{get_timestamp_string()} - FAILURE: ({self._name_and_alias}) : {message}"
        raise AssertionError(message)

    @final
    def verify_values(
        self,
        expected_value: Union[str, float],
        actual_value: Union[str, float],
        tolerance: float = 0,
        percentage: bool = False,
        custom_message_prefix: str = "",
        log_error: bool = False,
        expect_fail: bool = False,
    ) -> bool:
        """Compare and verify actual value with expected value.

        Args:
            expected_value: The expected value.
            actual_value: The actual value.
            tolerance: The acceptable difference between two floating point values, e.g. 0.0005
            percentage: A boolean indicating what kind of tolerance check to perform.
                False means absolute tolerance: +/- tolerance.
                True means percent tolerance: +/- (tolerance / 100) * value.
            custom_message_prefix: A custom message to be prepended to the failure message.
            log_error: Indicate if an error should be logged instead of a failure
            expect_fail: Indicate if a failure is expected and should be treated as a pass

        Returns:
            Boolean indicating whether the check passed or failed.
        """
        message = custom_message_prefix + "\n" if custom_message_prefix else ""

        try:
            _ = float(tolerance)
            _ = float(expected_value)
            _ = float(actual_value)
            number_comparison = True
        except ValueError:
            number_comparison = False

        if number_comparison:
            expected_value = float(expected_value)
            actual_value = float(actual_value)
            if percentage:
                tolerance = abs((tolerance / 100.0) * expected_value)
            message, verify_passed = self._verify_numerical_value(
                expected_value, actual_value, tolerance, message, expect_fail
            )
        else:
            expected_value = str(expected_value)
            actual_value = str(actual_value)
            message, verify_passed = self._verify_string_value(
                expected_value, actual_value, message, expect_fail
            )
        # Mark as pass/fail
        if not verify_passed:
            if log_error:
                self.raise_error(message)
            else:
                self.raise_failure(message)

        return verify_passed

    ################################################################################################
    # Private Methods
    ################################################################################################
    @staticmethod
    @final
    def _verify_numerical_value(
        expected_value: float,
        actual_value: float,
        tolerance: float,
        message: str,
        expect_fail: bool,
    ) -> Tuple[str, bool]:
        """Compare and verify a numerical value with expected value.

        Args:
             expected_value: The expected value.
             actual_value: The actual value.
             tolerance: The acceptable difference between two floating point values, e.g. 0.0005
             message: The failure message to edit and return.
             expect_fail: Indicate if a failure is expected and should be treated as a pass

        Returns:
            Tuple containing the failure message and a boolean indicating if the check passed.
        """
        max_value = expected_value + tolerance
        min_value = expected_value - tolerance
        # Verify that the number is within the tolerance.
        # Also check to make sure that the string of each number is
        # identical, this prevents issues from returned values that have
        # a trailing zero or some other non-contributing character that
        # will cause comparison issues.
        if (
            not expect_fail
            and (
                abs(expected_value - actual_value) <= tolerance
                or str(expected_value) == str(actual_value)
            )
        ) or (
            expect_fail
            and not (
                abs(expected_value - actual_value) <= tolerance
                or str(expected_value) == str(actual_value)
            )
        ):
            verify_passed = True
        else:
            message += (
                f"Actual result {'does not match' if not expect_fail else 'matches'} "
                f"the expected result within a tolerance of {tolerance}"
                f"\n  max: {max_value}"
                f"\n  act: {actual_value}"
                f"\n  min: {min_value}"
            )
            verify_passed = False

        return message, verify_passed

    @staticmethod
    @final
    def _verify_string_value(
        expected_value: str,
        actual_value: str,
        message: str,
        expect_fail: bool,
    ) -> Tuple[str, bool]:
        """Compare and verify a string value with expected value.

        Args:
             expected_value: The expected value.
             actual_value: The actual value.
             message: The failure message to edit and return.
             expect_fail: Indicate if a failure is expected and should be treated as a pass

        Returns:
            Tuple containing the failure message and a boolean indicating if the check passed.
        """
        if (not expect_fail and expected_value == actual_value) or (
            expect_fail and expected_value != actual_value
        ):
            verify_passed = True
        else:
            message += (
                f"Actual result {'does not match' if not expect_fail else 'matches'} "
                f"the expected result"
                f"\n  exp{' != ' if expect_fail else ': '}{expected_value}"
                f"\n  act{' == ' if expect_fail else ': '}{actual_value}"
            )
            verify_passed = False

        return message, verify_passed
