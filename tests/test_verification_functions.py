"""Tests for the verification_functions.py module."""

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
            "matches the expected result, exp != 0.1, act == 0.1",
        ),
        (
            0.1,
            0.2,
            0.05,
            False,
            False,
            "does not match the expected result within a tolerance of 0.05, "
            "max: 0.15, act: 0.2, min: 0.05",
        ),
        (
            0.1,
            0.2,
            0.1,
            False,
            True,
            "matches the expected result within a tolerance of 0.1, max: 0.2, act: 0.2, min: 0.0",
        ),
        (
            0.1,
            "0.2",
            0,
            True,
            False,
            "does not match the expected result, exp: 0.1, act: 0.2",
        ),
        (
            "0.100",
            "0.1",
            0,
            False,
            False,
            "does not match the expected result, exp: 0.100, act: 0.1",
        ),
        (
            "0.1",
            "0.2",
            5,
            True,
            False,
            "does not match the expected result within a tolerance of 0.005, "
            "max: 0.105, act: 0.2, min: 0.095",
        ),
        (
            "0.1",
            "0.1",
            0.01,
            False,
            True,
            "matches the expected result within a tolerance of 0.01, "
            "max: 0.11, act: 0.1, min: 0.09",
        ),
        (
            "0.1",
            "0.1",
            0,
            False,
            True,
            "matches the expected result, exp != 0.1, act == 0.1",
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
    assert expected_message_condensed in str(assertion_info.value)

    # just for fun check it again with condense_printout=False
    expected_message_uncondensed = (
        "ERROR: (failing-check-uncondensed) : Actual result "
        + expected_message.replace(", ", "\n  ")
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
    assert expected_message_uncondensed in str(assertion_info.value)


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
    assert (
        "FAILURE: (regex-fail-check) : Actual result does not match the expected result, "
        "exp: ^test.*value$, act: fail123value"
    ) in str(assertion_info.value)


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
            expected_value="expected",
            actual_value="actual",
            condense_printout=False,
            log_error=log_error,
        )
    assert (
        f"{message_level}: (condense-printout-check) : "
        f"Actual result does not match the expected result"
        "\n  exp: expected"
        "\n  act: actual"
    ) in str(assertion_info.value)
