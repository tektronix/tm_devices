"""The mock server used during unit tests."""

import sys

from typing import Any, Dict

from flask import request
from http_server_mock import HttpServerMock  # pyright: ignore[reportMissingTypeStubs]

from tm_devices.drivers.api.rest_api.rest_api_device import SupportedRequestTypes

################################################################################################
# Mock Data
################################################################################################
MOCK_ABOUT_INFO = {
    "model": "UNIT_TEST model",
    "serialNumber": "UNIT_TEST serialNumber",
    "manufacturer": "UNIT_TEST manufacturer",
    "sw_version": "1.0.0.0",
    "adapter": "UNIT_TEST adapter",
    "supportedTechnologies": "UNIT_TEST supportedTechnologies",
    "fpga_version": "1",
    "fw_version": "invalid",  # invalid fw_version. self._app_version will be set to Version("0")
}
INDEX_RESPONSE = "home"

################################################################################################
# Mock Server
################################################################################################
mocker_server = HttpServerMock(__name__)
PORT = int(f"60{sys.version_info.minor:02}")


@mocker_server.route("/api", methods=["GET"])
def index() -> Dict[str, str]:
    """GET endpoint for /api.

    Returns:
        Dict[str, str]: index response.
    """
    return {"message": INDEX_RESPONSE}


@mocker_server.route("/api/delete", methods=["DELETE"])
def delete_endpoint() -> Dict[str, str]:
    """DELETE endpoint for /api/delete.

    Returns:
        Dict[str, str]: delete response.
    """
    return {"message": str(SupportedRequestTypes.DELETE)}


@mocker_server.route("/api/update", methods=["PATCH", "POST", "PUT"])
def update_endpoint() -> Any:
    """PATCH, POST, and PUT endpoints for /api/update.

    Returns:
        Any: request body.
    """
    return request.json


@mocker_server.route("/api/device/about", methods=["GET"])
def device_about() -> Dict[str, str]:
    """GET endpoint for /api/device/about.

    Returns:
        Dict[str, str]: Mock device info.
    """
    return MOCK_ABOUT_INFO


@mocker_server.route("/api/device/version", methods=["GET"])
def device_version() -> Dict[str, str]:
    """GET endpoint for /api/device/version.

    Returns:
        Dict[str, str]: Mock fw_version info.
    """
    return {"fw_version": "1.0.0.1"}


@mocker_server.route("/api/device/status", methods=["GET"])
def device_status() -> Dict[str, str]:
    """GET endpoint for /api/device/status.

    Returns:
        Dict[str, str]: Mock status info.
    """
    return {"usage": "LOCKED"}
