"""Test the SSs."""

from typing import TYPE_CHECKING
from unittest import mock

import pytest
import pyvisa as visa

from tm_devices import DeviceManager

if TYPE_CHECKING:
    from tm_devices.drivers import SS3706A


def test_ss(device_manager: DeviceManager) -> None:
    """Test the SS3706A driver.

    Args:
        device_manager: The DeviceManager object.
    """
    switch: SS3706A = device_manager.add_ss("ss3706a-hostname", alias="ss-device")
    assert id(device_manager.get_ss(number_or_alias="ss-device")) == id(switch)
    assert id(device_manager.get_ss(number_or_alias=switch.device_number)) == id(switch)
    assert switch.get_errors() == (0, ())

    switch.expect_esr(0)

    with mock.patch("pyvisa.highlevel.VisaLibraryBase.clear", mock.MagicMock(return_value=None)):
        assert switch.query_expect_timeout("INVALID?", timeout_ms=1) == ""
    with mock.patch(
        "pyvisa.resources.messagebased.MessageBasedResource.query",
        mock.MagicMock(side_effect=visa.errors.Error("custom error")),
    ), pytest.raises(visa.errors.Error):
        switch.query_expect_timeout("INVALID?", timeout_ms=1)
    assert switch.expect_esr(32, "Command error,No Error")[0]
    assert switch.total_channels == 576
