"""Common functions for verifying values and printing out errors and failures."""

import re

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
        message, verify_passed = _verify_numerical_value(
            expected_value, actual_value, tolerance, message, expect_fail
        )
    else:
        expected_value = str(expected_value)
        actual_value = str(actual_value)
        message, verify_passed = _verify_string_value(
            expected_value, actual_value, message, expect_fail, use_regex_match
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
            f"\n  exp{' != ' if expect_fail else ': '}{expected_value}"
            f"\n  act{' == ' if expect_fail else ': '}{actual_value}"
        )
        verify_passed = False

    return message, verify_passed
