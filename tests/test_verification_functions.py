"""Tests for the verification_functions.py module."""

import re

from typing import Union

import pytest

from tm_devices.helpers import verify_values


def test_verify_values_pass() -> None:
    """Test the verify_values function."""
    assert verify_values(
        unique_identifier="passing-check", expected_value="True", actual_value="True"
    )


@pytest.mark.parametrize(
    (
        "expected_value",
        "actual_value",
        "tolerance",
        "percentage",
        "expect_fail",
        "expected_message",
    ),
    [
        (
            0.1,
            0.1,
            0,
            False,
            True,
            "matches the expected result, expect != 0.1, actual == 0.1",
        ),
        (
            0.1,
            0.2,
            0.05,
            False,
            False,
            "does not match the expected result within a tolerance of 0.05, "
            "range: [0.05, 0.15], expect: 0.1, actual: 0.2  <-- ABOVE range",
        ),
        (
            0.1,
            0.2,
            0.1,
            False,
            True,
            "matches the expected result within a tolerance of 0.1, "
            "range: [0.0, 0.2], expect: 0.1, actual: 0.2  <-- INSIDE range",
        ),
        (
            0.1,
            "0.2",
            0,
            True,
            False,
            "does not match the expected result, expect: 0.1, actual: 0.2",
        ),
        # Test strings with different decimal places, zero tolerance means treated as string match
        (
            "0.100",
            "0.1",
            0,
            False,
            False,
            "does not match the expected result, expect: 0.100, actual: 0.1",
        ),
        (
            "0.1",
            "0.05",
            5,
            True,
            False,
            "does not match the expected result within a tolerance of 0.005, "
            "range: [0.095, 0.105], expect: 0.1, actual: 0.05  <-- BELOW range",
        ),
        (
            "0.1",
            "0.1",
            0.01,
            False,
            True,
            "matches the expected result within a tolerance of 0.01, "
            "range: [0.09, 0.11], expect: 0.1, actual: 0.1  <-- INSIDE range",
        ),
        (
            "0.1",
            "0.1",
            0,
            False,
            True,
            "matches the expected result, expect != 0.1, actual == 0.1",
        ),
    ],
)
def test_verify_values_fail(
    expected_value: Union[float, str],
    actual_value: Union[float, str],
    tolerance: float,
    percentage: bool,
    expect_fail: bool,
    expected_message: str,
) -> None:
    """Test the verify_values function with an expected failing check (parameterized)."""
    expected_message_condensed = "ERROR: (failing-check) : Actual result " + expected_message
    with pytest.raises(AssertionError) as assertion_info:
        verify_values(
            unique_identifier="failing-check",
            expected_value=expected_value,
            actual_value=actual_value,
            tolerance=tolerance,
            percentage=percentage,
            expect_fail=expect_fail,
            log_error=True,
            condense_printout=True,
        )
    assert assertion_info.value.args[0] == expected_message_condensed

    # check it again with condense_printout=False

    def replace_outside_brackets(match: re.Match[str]) -> str:
        """Replace ', ' with indented newline, but only if not inside []."""
        # Count open brackets '[' minus close brackets ']' before the match
        prefix = match.string[: match.start()]
        open_brackets = prefix.count("[") - prefix.count("]")
        # Only replace if not inside brackets
        return "\n  " if not open_brackets else match.group(0)

    expected_message_uncondensed = "ERROR: (failing-check-uncondensed) : Actual result " + re.sub(
        r", ", replace_outside_brackets, expected_message
    )
    with pytest.raises(AssertionError) as assertion_info:
        verify_values(
            unique_identifier="failing-check-uncondensed",
            expected_value=expected_value,
            actual_value=actual_value,
            tolerance=tolerance,
            percentage=percentage,
            expect_fail=expect_fail,
            log_error=True,
            condense_printout=False,
        )
    assert assertion_info.value.args[0] == expected_message_uncondensed


def test_verify_values_regex_match_pass() -> None:
    """Test the verify_values function with regex matching that should pass."""
    assert verify_values(
        unique_identifier="regex-pass-check",
        expected_value=r"^test.*value$",
        actual_value="test123value",
        use_regex_match=True,
    )


def test_verify_values_regex_match_fail() -> None:
    """Test the verify_values function with regex matching that should fail."""
    with pytest.raises(AssertionError) as assertion_info:
        verify_values(
            unique_identifier="regex-fail-check",
            expected_value=r"^test.*value$",
            actual_value="fail123value",
            use_regex_match=True,
        )
    assert assertion_info.value.args[0] == (
        "FAILURE: (regex-fail-check) : Actual result does not match the expected result, "
        "expect: ^test.*value$, actual: fail123value"
    )


@pytest.mark.parametrize(
    ("log_error", "message_level"),
    [
        (True, "ERROR"),
        (False, "FAILURE"),
    ],
)
def test_verify_values_condense_printout(log_error: bool, message_level: str) -> None:
    """Test the verify_values function with condense_printout set to True."""
    with pytest.raises(AssertionError) as assertion_info:
        verify_values(
            unique_identifier="condense-printout-check",
            expected_value="expect",
            actual_value="actual",
            condense_printout=False,
            log_error=log_error,
        )
    assert assertion_info.value.args[0] == (
        f"{message_level}: (condense-printout-check) : "
        f"Actual result does not match the expected result"
        "\n  expect: expect"
        "\n  actual: actual"
    )
