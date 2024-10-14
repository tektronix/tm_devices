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
        " - ERROR: (failing-check) : Actual result does not match the expected "
        "result within a tolerance of 0.0, max: 0.1, act: 0.2, min: 0.1"
    ) in str(assertion_info.value)
