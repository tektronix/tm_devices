# pyright: reportPrivateUsage=none
"""Unit tests for tmt4.py."""
from pathlib import Path
from unittest import mock

import pytest

from packaging.version import Version

from mock_server import MOCK_ABOUT_INFO, PORT
from tm_devices import DeviceManager
from tm_devices.drivers.api.rest_api.margin_testers.margin_tester import MarginTester

AUTH_TOKEN_FILE_PATH = f"{Path(__file__).parent}/samples/token.auth_token_file_path"  # nosec


################################################################################################
# Fixtures
################################################################################################
@pytest.fixture(scope="module", name="tmt4")
def fixture_tmt4(
    device_manager: DeviceManager,
    mock_http_server: None,  # noqa: ARG001
) -> MarginTester:
    """Fixture that adds to device manager a margin tester connected to the mock server.

    Args:
        device_manager: Empty DeviceManager.
        mock_http_server: The mock HTTP server.

    Returns:
        The margin tester device.
    """
    return device_manager.add_mt("127.0.0.1", "TMT4", alias="tmt4", port=PORT)


################################################################################################
# Test Code
################################################################################################
def test_margin_tester(tmt4: MarginTester, device_manager: DeviceManager) -> None:
    """Verify the getter of the DeviceManager.

    Args:
        tmt4: Margin Tester device.
        device_manager: The DeviceManager object.
    """
    assert id(device_manager.get_mt(number_or_alias="tmt4")) == id(tmt4)
    assert id(device_manager.get_mt(number_or_alias=tmt4.device_number)) == id(tmt4)

    assert tmt4.commands == NotImplemented
    assert tmt4.command_argument_constants == NotImplemented
    assert tmt4.series == "TMT4"
    assert tmt4.adapter == MOCK_ABOUT_INFO["adapter"]

    # cover what happens when there is a string in the fw_version/fpga_version field
    with mock.patch.dict(
        tmt4._about_info,  # type: ignore[attr-defined]  # noqa: SLF001
        {"fpga_version": "UNIT TEST STRING", "fw_version": "UNIT TEST STRING"},
    ):
        assert tmt4.fw_version == Version("0")
        assert tmt4.fpga_version == Version("0")
        # clear the cache
        # noinspection PyPropertyAccess
        del tmt4.fw_version
        # noinspection PyPropertyAccess
        del tmt4.fpga_version
    # should be same as mocked version
    assert tmt4.sw_version == Version("1.0.0.0")
    assert tmt4.fw_version == Version("1.0.0.1")
    assert tmt4.fpga_version == Version("1")
    assert tmt4.manufacturer == "UNIT_TEST manufacturer"
    assert tmt4.model == "UNIT_TEST model"
    assert tmt4.serial == "UNIT_TEST serialNumber"

    assert tmt4.supported_technologies == tuple(MOCK_ABOUT_INFO["supportedTechnologies"].split(","))


def test_wait_till_unlocked(tmt4: MarginTester) -> None:
    """Test wait_till_unlocked.

    Args:
        tmt4: Margin Tester device.
    """
    # cover timeout case
    with pytest.raises(TimeoutError, match="waited more than 2 seconds"):
        tmt4.wait_till_unlocked(timeout=2)
    # cover regular unlocked case
    with mock.patch.object(
        tmt4, "get", mock.MagicMock(return_value=(None, {"usage": "NOT LOCKED"}, None, None))
    ):
        tmt4.wait_till_unlocked()


def test_open(tmt4: MarginTester) -> None:
    """Verify _open returns True.

    Args:
        tmt4: Margin Tester device.
    """
    assert tmt4._open()  # noqa: SLF001


def test_generate_headers_raises_assertion(tmt4: MarginTester) -> None:
    """Verify _generate_headers raises an AssertionError when auth_token_file_path is not set.

    Args:
        tmt4: Margin Tester device.
    """
    tmt4.auth_token_file_path = ""
    with pytest.raises(AssertionError):
        tmt4._generate_headers()  # noqa: SLF001


def test_generate_headers(tmt4: MarginTester) -> None:
    """Verify _generate_headers returns the contents in 'token.auth_token_file_path' file.

    Args:
        tmt4: Margin Tester device.
    """
    tmt4.auth_token_file_path = AUTH_TOKEN_FILE_PATH
    assert tmt4.auth_token_file_path == AUTH_TOKEN_FILE_PATH
    headers = tmt4._generate_headers()  # noqa: SLF001
    assert headers["Authorization"] == "Bearer UNIT-TEST"
