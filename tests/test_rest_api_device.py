# pyright: reportPrivateUsage=none
"""Unit tests for rest_api_device.py."""
from types import MappingProxyType
from unittest import mock

import pytest
import requests

from packaging.version import Version

from mock_server import INDEX_RESPONSE, PORT
from tm_devices.drivers.api.rest_api.rest_api_device import RESTAPIDevice, SupportedRequestTypes
from tm_devices.drivers.device import family_base_class
from tm_devices.helpers import ReadOnlyCachedProperty
from tm_devices.helpers.constants_and_dataclasses import DeviceConfigEntry
from tm_devices.helpers.enums import ConnectionTypes, DeviceTypes


################################################################################################
# Classes
################################################################################################
# noinspection PyAbstractClass
@family_base_class
class CustomRestApiDevice(RESTAPIDevice):
    """Custom Rest API Device class."""

    _DEVICE_TYPE = "CUSTOM"

    def _check_api_connection(self) -> bool:
        """Define abstract method _check_api_connection."""
        return self.get("/api", verbose=False, allow_errors=True)[0]

    def _close(self) -> None:
        """Define abstract method _close."""

    def _cleanup(self) -> None:
        """Define abstract method _cleanup."""

    def _has_errors(self) -> bool:
        """Define abstract method _has_errors."""
        return False

    def _open(self) -> bool:
        """Define abstract method _open."""
        return True

    def _reboot(self) -> None:
        """Perform the actual rebooting code."""

    @ReadOnlyCachedProperty
    def manufacturer(self) -> str:
        """Return the manufacturer of the device."""
        return "foo"

    @ReadOnlyCachedProperty
    def model(self) -> str:
        """Return the full model of the device."""
        return "bar"

    @ReadOnlyCachedProperty
    def serial(self) -> str:
        """Return the serial number of the device."""
        return "123"

    @ReadOnlyCachedProperty
    def sw_version(self) -> Version:
        """Return the software version of the device."""
        return Version("0")


################################################################################################
# Fixtures
################################################################################################
@pytest.fixture(scope="module", name="rest_api_device")
def fixture_rest_api_device(mock_http_server: None) -> CustomRestApiDevice:  # noqa: ARG001
    """Fixture that connects the Rest API Device to the mock server.

    Returns:
       The Rest API device.
    """
    rest_api_device = CustomRestApiDevice(
        config_entry=DeviceConfigEntry(
            device_type=DeviceTypes.MT,
            device_driver="TMT4",  # needed to create the custom device, not actually used
            connection_type=ConnectionTypes.REST_API,
            address="127.0.0.1",
            lan_port=PORT,
            alias="TMT4",
        ),
        verbose=False,
    )
    # noinspection PyProtectedMember
    # Change base_url from https to http as the mock server
    # can only handle http requests. Also add port number.
    rest_api_device._base_url = (  # noqa: SLF001
        rest_api_device._base_url.replace("https", "http") + f":{PORT}"  # noqa: SLF001
    )
    rest_api_device._api_url = rest_api_device.base_url + "/api"  # noqa: SLF001
    return rest_api_device


################################################################################################
# Test Code
################################################################################################
def test_delete(rest_api_device: CustomRestApiDevice) -> None:
    """Test DELETE request.

    Args:
        rest_api_device: Rest API Device.
    """
    _, res_json, _, _ = rest_api_device.delete(url="/delete")
    assert not isinstance(res_json, bytes)
    assert res_json["message"] == str(SupportedRequestTypes.DELETE)


def test_patch(rest_api_device: CustomRestApiDevice) -> None:
    """Test PATCH request.

    Args:
        rest_api_device: Rest API Device.
    """
    _, res_json, _, _ = rest_api_device.patch(
        url="/update", json_body={"message": str(SupportedRequestTypes.PATCH)}
    )
    assert not isinstance(res_json, bytes)
    assert res_json["message"] == str(SupportedRequestTypes.PATCH)


def test_post(rest_api_device: CustomRestApiDevice) -> None:
    """Test POST request.

    Args:
        rest_api_device: Rest API Device.
    """
    _, res_json, _, _ = rest_api_device.post(
        url="/update", json_body={"message": str(SupportedRequestTypes.POST)}
    )
    assert not isinstance(res_json, bytes)
    assert res_json["message"] == str(SupportedRequestTypes.POST)


def test_put(rest_api_device: CustomRestApiDevice) -> None:
    """Test PUT request.

    Args:
        rest_api_device: Rest API Device.
    """
    _, res_json, _, _ = rest_api_device.put(
        url="/update", json_body={"message": str(SupportedRequestTypes.PUT)}
    )
    assert not isinstance(res_json, bytes)
    assert res_json["message"] == str(SupportedRequestTypes.PUT)


def test_unsupported_request_type(rest_api_device: CustomRestApiDevice) -> None:
    """Verify sending an unsupported request type raises a ValueError.

    Args:
        rest_api_device: Rest API Device.
    """
    with pytest.raises(ValueError, match="UNSUPPORTED is an unsupported request type."):
        rest_api_device._send_request(  # noqa: SLF001
            request_type="UNSUPPORTED",  # type: ignore[arg-type]
            url="/api",
        )


def test_api_url(rest_api_device: CustomRestApiDevice) -> None:
    """Verify API URL is the Base URL with /api at the end.

    Args:
        rest_api_device: Rest API Device.
    """
    assert rest_api_device.api_url == rest_api_device.base_url + "/api"


def test_set_api_version_non_verbose(rest_api_device: CustomRestApiDevice) -> None:
    """Verify switching API versions changes the API URL.

    Args:
        rest_api_device: Rest API Device.
    """
    rest_api_device.API_VERSIONS = MappingProxyType({1: "/api", 2: "/api2"})
    rest_api_device.set_api_version(api_version=2, verbose=False)
    assert rest_api_device.api_url == rest_api_device.base_url + rest_api_device.API_VERSIONS[2]


def test_send_request(rest_api_device: CustomRestApiDevice) -> None:
    """Test send_request with different url args.

    Args:
        rest_api_device: Rest API Device.
    """
    # Test with url parameter that includes the base url. Include return_bytes arg as True.
    rest_api_device._verbose = True  # noqa: SLF001
    _, res, _, _ = rest_api_device._send_request(  # noqa: SLF001
        request_type=SupportedRequestTypes.GET,
        url=f"{rest_api_device.base_url}/api",
        headers={"headers": "headers"},
        json_body={"body": "body"},
        return_bytes=True,
    )
    assert res == b'{"message":"home"}\n'

    # Test with url parameter that does not start with '/'.
    _, res, _, _ = rest_api_device._send_request(  # noqa: SLF001
        request_type=SupportedRequestTypes.GET, url="api"
    )
    assert not isinstance(res, bytes)
    assert res["message"] == INDEX_RESPONSE

    # Test with url parameter that start with API_VERSIONS.
    _, res, _, _ = rest_api_device._send_request(  # noqa: SLF001
        request_type=SupportedRequestTypes.GET, url=f"{rest_api_device.API_VERSIONS[1]}"
    )
    assert not isinstance(res, bytes)
    assert res["message"] == INDEX_RESPONSE


def test_wait_for_api_connection(
    rest_api_device: CustomRestApiDevice, capsys: pytest.CaptureFixture[str]
) -> None:
    """Test waiting for an API connection.

    Args:
        rest_api_device: Rest API Device.
        capsys: The captured stdout and stderr.
    """
    # Test an immediate connection
    rest_api_device.wait_for_api_connection(5, accept_immediate_connection=True)
    stdout = capsys.readouterr().out
    assert "Attempting to establish an API connection with " in stdout
    assert "Successfully established an API connection with " in stdout

    # Test when unable to connect
    with mock.patch("requests.get", mock.MagicMock(side_effect=requests.RequestException())):
        rest_api_device.wait_for_api_connection(0.01, accept_immediate_connection=False)
        stdout = capsys.readouterr().out
        assert "Attempting to establish an API connection with " in stdout
        assert "Unable to establish an API connection with " in stdout

    # Test connecting on the first try when it shouldn't happen
    with pytest.raises(AssertionError):
        rest_api_device.wait_for_api_connection(10, accept_immediate_connection=False)


def test_send_request_exceptions(rest_api_device: CustomRestApiDevice) -> None:
    """Verify send_request handles bad urls.

    Args:
        rest_api_device: Rest API Device.
    """
    with pytest.raises(AssertionError):
        rest_api_device._send_request(  # noqa: SLF001
            request_type=SupportedRequestTypes.GET, url="/error"
        )

    # Same as above but with 'allow_errors' arg set to True.
    success, _, status_code, _ = rest_api_device._send_request(  # noqa: SLF001
        request_type=SupportedRequestTypes.GET, url="/error", allow_errors=True
    )
    assert not success
    assert status_code == 404
