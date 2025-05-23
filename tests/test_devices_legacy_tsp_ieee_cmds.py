"""Test the DMMs."""

from typing import TYPE_CHECKING
from unittest import mock

import pytest
import pyvisa as visa

from tm_devices import DeviceManager

if TYPE_CHECKING:
    from tm_devices.drivers import DAQ6510, DMM6500, DMM7510


def test_dmm6500(device_manager: DeviceManager) -> None:
    """Test the DMM drivers.

    Args:
        device_manager: The DeviceManager object.
    """
    dmm: DMM6500 = device_manager.add_dmm("DMM6500-hostname", alias="dmm-device")
    assert id(device_manager.get_dmm(number_or_alias="dmm-device")) == id(dmm)
    assert id(device_manager.get_dmm(number_or_alias=dmm.device_number)) == id(dmm)

    with mock.patch("pyvisa.highlevel.VisaLibraryBase.clear", mock.MagicMock(return_value=None)):
        assert dmm.query_expect_timeout("INVALID?", timeout_ms=1) == ""
    with (
        mock.patch(
            "pyvisa.resources.messagebased.MessageBasedResource.query",
            mock.MagicMock(side_effect=visa.errors.Error("custom error")),
        ),
        pytest.raises(visa.errors.Error),
    ):
        dmm.query_expect_timeout("INVALID?", timeout_ms=1)
    assert dmm.expect_esr(32, ("Command error", "No Error"))


def test_dmm75xx(device_manager: DeviceManager) -> None:
    """Test the DMM drivers.

    Args:
        device_manager: The DeviceManager object.
    """
    dmm: DMM7510 = device_manager.add_dmm("DMM7510-hostname")

    with mock.patch("pyvisa.highlevel.VisaLibraryBase.clear", mock.MagicMock(return_value=None)):
        assert dmm.query_expect_timeout("INVALID?", timeout_ms=1) == ""
    with (
        mock.patch(
            "pyvisa.resources.messagebased.MessageBasedResource.query",
            mock.MagicMock(side_effect=visa.errors.Error("custom error")),
        ),
        pytest.raises(visa.errors.Error),
    ):
        dmm.query_expect_timeout("INVALID?", timeout_ms=1)
    assert dmm.expect_esr(32, ("Command error", "No Error"))


def test_daq6510(device_manager: DeviceManager) -> None:
    """Test the DAQ drivers.

    Args:
        device_manager: The DeviceManager object.
    """
    daq: DAQ6510 = device_manager.add_daq("DAQ6510-hostname", alias="daq-device")
    assert id(device_manager.get_daq(number_or_alias="daq-device")) == id(daq)
    assert id(device_manager.get_daq(number_or_alias=daq.device_number)) == id(daq)

    with mock.patch("pyvisa.highlevel.VisaLibraryBase.clear", mock.MagicMock(return_value=None)):
        assert daq.query_expect_timeout("INVALID?", timeout_ms=1) == ""
    with (
        mock.patch(
            "pyvisa.resources.messagebased.MessageBasedResource.query",
            mock.MagicMock(side_effect=visa.errors.Error("custom error")),
        ),
        pytest.raises(visa.errors.Error),
    ):
        daq.query_expect_timeout("INVALID?", timeout_ms=1)
    assert daq.expect_esr(32, ("Command error", "No Error"))
    assert daq.total_channels == 1
