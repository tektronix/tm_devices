"""Tests for the verification_functions.py module."""

import pytest

from tm_devices.helpers import verify_values


def test_verify_values_pass() -> None:
    """Test the verify_values function."""
    assert verify_values(
        unique_identifier="passing-check", expected_value="True", actual_value="True"
    )


def test_verify_values_fail() -> None:
    """Test the verify_values function with an expected failing check."""
    with pytest.raises(AssertionError) as assertion_info:
        verify_values(
            unique_identifier="failing-check",
            expected_value="0.1",
            actual_value="0.2",
            percentage=True,
            log_error=True,
        )
    assert (
        "ERROR: (failing-check) : Actual result does not match the expected "
        "result within a tolerance of 0.0, max: 0.1, act: 0.2, min: 0.1"
    ) in str(assertion_info.value)


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
