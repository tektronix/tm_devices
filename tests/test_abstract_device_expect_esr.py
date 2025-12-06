"""Unit tests for the _AbstractDeviceVISAWriteQueryControl.expect_esr method."""

import re

from typing import List, Tuple

import pytest

# Use the actual implementation
from tm_devices.driver_mixins.device_control._abstract_device_visa_write_query_control import (
    _AbstractDeviceVISAWriteQueryControl,  # pyright: ignore[reportPrivateUsage]
)


class DummyDevice:  # pylint: disable=too-few-public-methods
    """A dummy device for testing the expect_esr method."""

    get_errors_return: Tuple[int, Tuple[str, ...]] = (0, ())

    def __init__(self) -> None:
        """Initialize the dummy device."""
        self.name_and_alias = 'DUMMY 1 "DUT"'

    @property
    def _no_error_string(self) -> str:
        return ""

    def _get_errors(self) -> Tuple[int, Tuple[str, ...]]:
        return self.get_errors_return

    def expect_esr(
        self, esr: int, error_messages: Tuple[str, ...] = (), *, use_regex_match: bool = False
    ) -> bool:
        """A wrapper to call the expect_esr method from _AbstractDeviceVISAWriteQueryControl."""
        # Patch self into the class
        return _AbstractDeviceVISAWriteQueryControl.expect_esr(
            self,  # pyright: ignore[reportArgumentType]
            esr,
            error_messages,
            use_regex_match=use_regex_match,
        )


class DummyDeviceCustomNoError(DummyDevice):  # pylint: disable=too-few-public-methods
    """A dummy device with a custom no error string for testing the expect_esr method."""

    @property
    def _no_error_string(self) -> str:
        # Custom no error string, regex to not be too specific
        return "No E\\w+s"


def test_expect_esr_param_just_esr_arg(  # noqa: PLR0915
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Test the expect_esr method with various parameters and return values.

    Reason:
        If there are fewer actual error messages than expected, pad actual_error_messages using
        zip_longest so all expected messages are checked and reported.

        Devices typically implement _get_errors() to read from an error queue. If the queue is empty,
        a string like "No Errors" is usually returned. Some devices may check the error count and,
        if zero, skip querying for that string, resulting in no actual error messages.

    Examples:
        With errors:
          8, ("error1", "error2", "error3", "No Errors")
          8, ("error1", "error2", "error3")
          1, ("Operation Complete", "No Errors")
          1, ("Operation Complete",)
        Without errors:
          0, ("No Errors",)
          0, ()
          1, ("No Errors")
        ESR bits can be set without generating an error message.
        When ESR is non-zero, devices must always query for error strings, even if queue is known empty.
          (This is where defining a _no_error_string will help (e.g. simplify usage to expect_esr(1))

        Device drivers can define their _no_error_string pattern as the default when error_messages is empty;
          simplifies usage from `expect_esr( 1, ("No Errors"))` to just `expect_esr(1)`


        Using zip will result in an empty message_pairs if both actual and expected errors are empty,
        which can occur when _no_error_string is an empty string.

        For example:
          expect_esr(8) with no custom error messages should fail if ESR is not 8 or if any error message is present.
          If ESR is 8 and there are no error messages, it should pass, assuming a suitable _no_error_string.

        Typical cases:
          dut.expect_esr(0) passes if ESR is 0 and there are no error messages or "No Errors".
          dut.expect_esr(1) passes if ESR is 1 and the error message is "No Errors".
          dut.expect_esr(1, ("Operation Complete",)) passes if ESR is 1 and the event/error string matches.
    """  # noqa: E501
    device1 = DummyDevice()
    device2 = DummyDeviceCustomNoError()

    failure_msg_start = 'FAILURE: (DUMMY 1 "DUT") : '

    def get_assertion_msg(
        log_msgs: List[str], *, esr: Tuple[int, int] = (0, 0), extra_assert_msg: str = ""
    ) -> str:
        """Helper to create the expected assertion message string."""
        esr_match = esr[0] == esr[1]
        assertion_msg = (
            f"{failure_msg_start}expect_esr() failed; ESR value {'' if esr_match else 'mis'}match "
            f"(Expected: {esr[0]}, Actual: {esr[1]}){extra_assert_msg}"
        )

        if not esr_match and log_msgs[0].startswith(
            "Actual result does not match the expected result"
        ):
            # Remove the ESR mismatch warning log, already handled above in the assertion message
            log_msgs = log_msgs[1:]

        for i, msg in enumerate(log_msgs, start=1):
            if msg == "":
                continue
            # logged message will be indented in assertion message for readability
            assertion_msg += (
                f"\n{failure_msg_start}expect_esr() error message check #{i}:\n"
                f"  {msg.replace(chr(10), chr(10) + '  ')}"
            )
        return assertion_msg

    def get_raised_assert_match(match: str) -> str:
        """Helper to create the expected match string for pytest.raises."""
        retval = re.escape(match).replace(r"\#", "#").replace(r"\ ", " ").replace("\\\n", "\n")
        return f"^{retval}$"

    def verify_caplog_matches_expected(log_msgs: List[str]) -> None:
        """Helper to verify caplog records match expected log messages."""
        log_msgs = [msg for msg in log_msgs if msg]  # Filter out empty messages
        assert len(caplog.records) == len(log_msgs)
        for record, expected_msg in zip(caplog.records, log_msgs):
            assert record.levelname == "WARNING"
            assert record.message.endswith(expected_msg), (
                f"logged message:\n{record.message!r}\n was expected to end with:\n{expected_msg!r}"
            )
        caplog.clear()

    def convert_log_msgs_for_device2(msg: List[str]) -> List[str]:
        """Helper to convert a log message for device2's custom no error string."""
        return [msg.replace("DummyDevice", "DummyDeviceCustomNoError") for msg in msg]

    # the only time no returned error messages can be an empty is when ESR is 0
    DummyDevice.get_errors_return = (0, ())

    device1.expect_esr(0)
    device2.expect_esr(0)

    assert not bool(len(caplog.records))

    ###
    # Test usage: device.expect_esr(0) with (0, ("No Errors",))
    ###
    DummyDevice.get_errors_return = (0, ("No Errors",))

    # Passes since it has a definition for error_messages
    device1.expect_esr(0, ("No Errors",))
    # Passes since it has the _no_error_string definition
    device2.expect_esr(0)

    assert not bool(len(caplog.records))
    # Now on device1, without an error_messages definition,
    # it should fail with AssertionError and log a warning
    expected_log_warning = [
        """Actual result does not match the expected result
  exp: DummyDevice._get_errors() returned more error messages than expected
  act: No Errors"""
    ]

    expected_assertion_msg = get_assertion_msg(expected_log_warning)
    match_str = get_raised_assert_match(expected_assertion_msg)
    with pytest.raises(AssertionError, match=match_str):
        device1.expect_esr(0)
    verify_caplog_matches_expected(expected_log_warning)

    ###
    # Test usage with invalid returns: device.expect_esr(1)
    ###

    # invalid return since ESR is non-zero but no error messages
    DummyDevice.get_errors_return = (1, ())  # Non-zero ESR with no error messages should fail

    # Test the ESR mismatch + logging
    expected_log_warning = [
        """Actual result does not match the expected result
  exp: 8
  act: 1""",
        """Actual result does not match the expected result
  exp: None
  act: DummyDevice._get_errors() must return the response from the error message queue query for any non-zero ESR""",  # noqa: E501
    ]

    expected_assertion_msg = get_assertion_msg(
        expected_log_warning,
        esr=(8, 1),
        extra_assert_msg="; expected `error_messages` parameter defined (or DummyDevice._no_error_string defined) when ESR is non-zero",  # noqa: E501
    )
    match_str = get_raised_assert_match(expected_assertion_msg)
    with pytest.raises(AssertionError, match=match_str):
        device1.expect_esr(8)
    verify_caplog_matches_expected(expected_log_warning)

    # Now test device2 with the custom no error string defined
    expected_log_warning = convert_log_msgs_for_device2(expected_log_warning)
    # Want "exp: None" instead of "No E\w+s" to better highlight the missing return from error query
    expected_log_warning[1] = """Actual result does not match the expected result
  exp: None
  act: DummyDeviceCustomNoError._get_errors() must return the response from the error message queue query for any non-zero ESR"""  # noqa: E501

    # Note: the extra_assert_msg is not included since device2 has a _no_error_string defined
    expected_assertion_msg = get_assertion_msg(expected_log_warning, esr=(8, 1))
    match_str = get_raised_assert_match(expected_assertion_msg)
    with pytest.raises(AssertionError, match=match_str):
        device2.expect_esr(8)
    verify_caplog_matches_expected(expected_log_warning)

    DummyDevice.get_errors_return = (1, ("error 1", "error 2", "error 3"))

    assert device1.expect_esr(1, ("error 1", "error 2", "error 3"))
    assert device2.expect_esr(1, ("error 1", "error 2", "error 3"))

    # Now test that assertion message works with multiple error messages
    expected_log_warning = [
        """Actual result does not match the expected result
  exp: error A
  act: error 1""",
        """Actual result does not match the expected result
  exp: error B
  act: error 2""",
        """Actual result does not match the expected result
  exp: error C
  act: error 3""",
    ]
    expected_assertion_msg = get_assertion_msg(expected_log_warning, esr=(1, 1))
    match_str = get_raised_assert_match(expected_assertion_msg)
    with pytest.raises(AssertionError, match=match_str):
        device1.expect_esr(1, ("error A", "error B", "error C"))

    expected_log_warning = convert_log_msgs_for_device2(expected_log_warning)
    expected_assertion_msg = get_assertion_msg(expected_log_warning, esr=(1, 1))
    match_str = get_raised_assert_match(expected_assertion_msg)
    with pytest.raises(AssertionError, match=match_str):
        device2.expect_esr(1, ("error A", "error B", "error C"))

    # Now test that assertion message works with multiple error messages
    expected_log_warning = [
        "",
        """Actual result does not match the expected result
  exp: DummyDevice._get_errors() returned more error messages than expected
  act: error 2""",
        """Actual result does not match the expected result
  exp: DummyDevice._get_errors() returned more error messages than expected
  act: error 3""",
    ]
    expected_assertion_msg = get_assertion_msg(expected_log_warning, esr=(1, 1))
    match_str = get_raised_assert_match(expected_assertion_msg)
    with pytest.raises(AssertionError, match=match_str):
        device1.expect_esr(1, ("error 1",))

    expected_log_warning = [
        "",
        """Actual result does not match the expected result
  exp: No E\\w+s
  act: error 2""",
        """Actual result does not match the expected result
  exp: DummyDeviceCustomNoError._get_errors() returned more error messages than expected
  act: error 3""",
    ]
    expected_assertion_msg = get_assertion_msg(expected_log_warning, esr=(1, 1))
    match_str = get_raised_assert_match(expected_assertion_msg)
    with pytest.raises(AssertionError, match=match_str):
        device2.expect_esr(1, ("error 1",))

    # Test that explicitly using _no_error_string behaves same as implicit usage above
    with pytest.raises(AssertionError, match=match_str):
        device2.expect_esr(1, ("error 1", "No E\\w+s"))

    DummyDevice.get_errors_return = (1, ("error 1", "error 2", "error 3", "No Errors"))
    assert device2.expect_esr(1, ("error 1", "error 2", "error 3"))

    DummyDevice.get_errors_return = (1, ("error 1", "error 2", "error 3", "No Errors", "No Errors"))

    match_str = get_raised_assert_match(
        f"""{failure_msg_start}expect_esr() failed; ESR value match (Expected: 1, Actual: 1)
{failure_msg_start}expect_esr() error message check #5:
  Actual result does not match the expected result
    exp: DummyDeviceCustomNoError._get_errors() returned more error messages than expected
    act: No Errors"""
    )
    with pytest.raises(AssertionError, match=match_str):
        device2.expect_esr(1, ("error 1", "error 2", "error 3"))
    with pytest.raises(AssertionError, match=match_str):
        device2.expect_esr(1, ("error 1", "error 2", "error 3", "No E\\w+s"))
