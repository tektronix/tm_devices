"""Common functions for verifying values and printing out errors and failures."""

from typing import Tuple, Union

from tm_devices.helpers.functions import get_timestamp_string


def raise_error(unique_identifier: str, message: str) -> None:
    """Raise an AssertionError with the provided message indicating there was an error.

    Args:
        unique_identifier: A unique identifier to add to the AssertionError, e.g. the device name.
        message: The message to add to the AssertionError.

    Raises:
        AssertionError: Prints out the error message with a traceback.
    """
    # TODO: integrate this with logging
    #  https://github.com/tektronix/tm_devices/issues/316
    # Make the message smaller
    message = ", ".join([x.strip() for x in message.split("\n")])
    message = f"{get_timestamp_string()} - ERROR: ({unique_identifier}) : {message}"
    raise AssertionError(message)


def raise_failure(unique_identifier: str, message: str) -> None:
    """Raise an AssertionError with the provided message indicating there was a failure.

    Args:
        unique_identifier: A unique identifier to add to the AssertionError, e.g. the device name.
        message: The message to add to the AssertionError.

    Raises:
        AssertionError: Prints out the failure message with a traceback.
    """
    # TODO: integrate this with logging
    #  https://github.com/tektronix/tm_devices/issues/316
    # Make the message smaller
    message = ", ".join([x.strip() for x in message.split("\n")])
    message = f"{get_timestamp_string()} - FAILURE: ({unique_identifier}) : {message}"
    raise AssertionError(message)


def verify_values(  # noqa: PLR0913
    unique_identifier: str,
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
            expected_value, actual_value, message, expect_fail
        )
    # Mark as pass/fail
    if not verify_passed:
        if log_error:
            raise_error(unique_identifier, message)
        else:
            raise_failure(unique_identifier, message)

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
