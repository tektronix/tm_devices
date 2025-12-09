"""Common functions for verifying values and printing out errors and failures."""

import re

from decimal import Decimal, InvalidOperation
from typing import Tuple, Union


def raise_error(unique_identifier: str, message: str, *, condense_printout: bool = True) -> None:
    """Raise an AssertionError with the provided message indicating there was an error.

    Args:
        unique_identifier: A unique identifier to add to the AssertionError, e.g. the device name.
        message: The message to add to the AssertionError.
        condense_printout: A boolean indicating if the printout should be condensed.

    Raises:
        AssertionError: Prints out the error message with a traceback.
    """
    if condense_printout:
        # Make the message smaller
        message = ", ".join([x.strip() for x in message.split("\n")])
    message = f"ERROR: ({unique_identifier}) : {message}"
    raise AssertionError(message)


def raise_failure(unique_identifier: str, message: str, *, condense_printout: bool = True) -> None:
    """Raise an AssertionError with the provided message indicating there was a failure.

    Args:
        unique_identifier: A unique identifier to add to the AssertionError, e.g. the device name.
        message: The message to add to the AssertionError.
        condense_printout: A boolean indicating if the printout should be condensed.

    Raises:
        AssertionError: Prints out the failure message with a traceback.
    """
    if condense_printout:
        # Make the message smaller
        message = ", ".join([x.strip() for x in message.split("\n")])
    message = f"FAILURE: ({unique_identifier}) : {message}"
    raise AssertionError(message)


def verify_values(  # noqa: PLR0913
    unique_identifier: str,
    expected_value: Union[str, float],
    actual_value: Union[str, float],
    *,
    tolerance: float = 0,
    percentage: bool = False,
    custom_message_prefix: str = "",
    log_error: bool = False,
    expect_fail: bool = False,
    use_regex_match: bool = False,
    condense_printout: bool = True,
) -> bool:
    """Compare and verify actual value with expected value.

    Args:
        unique_identifier: A unique identifier to add to the AssertionError, e.g. the device name.
        expected_value: The expected value.
        actual_value: The actual value.
        tolerance: The acceptable difference between two floating point values, e.g. 0.0005
        percentage: A boolean indicating what kind of tolerance check to perform.
            False means absolute tolerance: +/- tolerance.
            True means percent tolerance: +/- (tolerance / 100) * value.
        custom_message_prefix: A custom message to be prepended to the failure message.
        log_error: Indicate if an error should be logged instead of a failure
        expect_fail: Indicate if a failure is expected and should be treated as a pass
        use_regex_match: A boolean indicating if the strings should be compared
            using regular expressions.
        condense_printout: A boolean indicating if the printout should be condensed.

    Returns:
        Boolean indicating whether the check passed or failed.
    """
    message = custom_message_prefix + "\n" if custom_message_prefix else ""

    try:
        if not tolerance and isinstance(expected_value, str) and isinstance(actual_value, str):
            # treat "1.000" vs "1" as pure string comparison when no tolerance is given
            raise ValueError  # noqa: TRY301

        # Try to convert to Decimal for number comparison
        tolerance_decimal = Decimal(str(tolerance))
        expected_value_decimal = Decimal(str(expected_value))
        actual_value_decimal = Decimal(str(actual_value))

        # Made it this far without an exception, do number comparison
        if percentage:
            tolerance_decimal = abs((tolerance_decimal / Decimal("100.0")) * expected_value_decimal)
        message, verify_passed = _verify_numerical_value(
            expected_value_decimal, actual_value_decimal, tolerance_decimal, message, expect_fail
        )

    except (ValueError, InvalidOperation):
        # Not a number, do string comparison
        message, verify_passed = _verify_string_value(
            str(expected_value), str(actual_value), message, expect_fail, use_regex_match
        )
    # Mark as pass/fail
    if not verify_passed:
        if log_error:
            raise_error(unique_identifier, message, condense_printout=condense_printout)
        else:
            raise_failure(unique_identifier, message, condense_printout=condense_printout)

    return verify_passed


################################################################################################
# Private Methods
################################################################################################
def _verify_numerical_value(
    expected_value: Decimal,
    actual_value: Decimal,
    tolerance: Decimal,
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

    # Use min/max for tolerance check
    match = min_value <= actual_value <= max_value

    if not (verify_passed := (not expect_fail and match) or (expect_fail and not match)):
        if max_value == min_value:
            # No tolerance, mirror string comparison message for consistency
            message += (
                f"Actual result {'does not match' if not expect_fail else 'matches'} "
                f"the expected result"
                f"\n  expect{' != ' if expect_fail else ': '}{expected_value}"
                f"\n  actual{' == ' if expect_fail else ': '}{actual_value}"
            )
        else:
            # Visual range format
            in_range = match and expect_fail
            inside_outside = (
                "INSIDE" if in_range else "BELOW" if actual_value < min_value else "ABOVE"
            )
            message += (
                f"Actual result {'does not match' if not expect_fail else 'matches'} "
                f"the expected result within a tolerance of {tolerance}"
                f"\n  range: [{min_value}, {max_value}]"
                f"\n  expect: {expected_value}"
                f"\n  actual: {actual_value}  <-- {inside_outside} range"
            )

    return message, verify_passed


def _verify_string_value(
    expected_value: str,
    actual_value: str,
    message: str,
    expect_fail: bool,
    use_regex_match: bool = False,
) -> Tuple[str, bool]:
    """Compare and verify a string value with expected value.

    Args:
        expected_value: The expected value.
        actual_value: The actual value.
        message: The failure message to edit and return.
        expect_fail: Indicate if a failure is expected and should be treated as a pass
        use_regex_match: A boolean indicating if the strings should be compared
            using regular expressions.

    Returns:
        Tuple containing the failure message and a boolean indicating if the check passed.
    """
    if use_regex_match:
        match = re.match(expected_value, actual_value) is not None
    else:
        match = expected_value == actual_value

    if (not expect_fail and match) or (expect_fail and not match):
        verify_passed = True
    else:
        message += (
            f"Actual result {'does not match' if not expect_fail else 'matches'} "
            f"the expected result"
            f"\n  expect{' != ' if expect_fail else ': '}{expected_value}"
            f"\n  actual{' == ' if expect_fail else ': '}{actual_value}"
        )
        verify_passed = False

    return message, verify_passed
