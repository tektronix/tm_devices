"""Base REST Application Programming Interface (API) device driver module."""
import json
import time

from abc import ABC, abstractmethod
from types import MappingProxyType
from typing import Any, cast, Dict, Mapping, Optional, Tuple, Union

import requests

from tm_devices.drivers.api.api_device import APIDevice
from tm_devices.helpers import DeviceConfigEntry, print_with_timestamp, SupportedRequestTypes


class RESTAPIDevice(APIDevice, ABC):
    """Base REST Application Programming Interface (API) device driver."""

    API_VERSIONS: "MappingProxyType[int, str]" = MappingProxyType({})
    """Dict[int, str]: A mapping of supported API version numbers with the corresponding API URL."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(self, config_entry: DeviceConfigEntry, verbose: bool) -> None:
        """Create a REST API device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
        """
        super().__init__(config_entry, verbose)

        # The URL to use for REST API requests
        self._base_url = f"https://{self.ip_address}"
        self._api_url = ""

    ################################################################################################
    # Properties
    ################################################################################################
    @property
    def api_url(self) -> str:
        """Return the base API url of the device."""
        return self._api_url

    @property
    def base_url(self) -> str:
        """Return the base url of the device."""
        return self._base_url

    ################################################################################################
    # Public Methods
    ################################################################################################
    def delete(  # noqa: PLR0913
        self,
        url: str,
        headers: Optional[Mapping[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        return_bytes: bool = False,
        allow_errors: bool = False,
        verbose: bool = True,
    ) -> Tuple[bool, Union[Dict[str, Any], bytes], int, Optional[requests.RequestException]]:
        """Perform a DELETE request with the given url and headers.

        Args:
            url: The url to DELETE.
            headers: The headers to use during the request.
            auth: A tuple containing the username and password to use in the request.
            timeout: How many seconds to wait for the server to send data before giving up.
            return_bytes: A boolean indicating if the response content should be returned
                instead of the response json.
            allow_errors: A boolean indicating if errors are allowed.
            verbose: Set this to False in order to disable printouts.

        Returns:
            A tuple containing a success boolean, the response data, status code, and any errors
        """
        return self._send_request(
            SupportedRequestTypes.DELETE,
            url,
            headers=headers,
            auth=auth,
            timeout=timeout,
            return_bytes=return_bytes,
            allow_errors=allow_errors,
            verbose=verbose,
        )

    def get(  # noqa: PLR0913
        self,
        url: str,
        headers: Optional[Mapping[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        return_bytes: bool = False,
        allow_errors: bool = False,
        verbose: bool = True,
    ) -> Tuple[bool, Union[Dict[str, Any], bytes], int, Optional[requests.RequestException]]:
        """Perform a GET request with the given url and headers.

        Args:
            url: The url to GET.
            headers: The headers to use during the request.
            auth: A tuple containing the username and password to use in the request.
            timeout: How many seconds to wait for the server to send data before giving up.
            return_bytes: A boolean indicating if the response content should be returned
                instead of the response json.
            allow_errors: A boolean indicating if errors are allowed.
            verbose: Set this to False in order to disable printouts.

        Returns:
            A tuple containing a success boolean, the response data, status code, and any errors
        """
        return self._send_request(
            SupportedRequestTypes.GET,
            url,
            headers=headers,
            auth=auth,
            timeout=timeout,
            return_bytes=return_bytes,
            allow_errors=allow_errors,
            verbose=verbose,
        )

    def patch(  # noqa: PLR0913
        self,
        url: str,
        json_body: Dict[str, Any],
        headers: Optional[Mapping[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        return_bytes: bool = False,
        allow_errors: bool = False,
        verbose: bool = True,
    ) -> Tuple[bool, Union[Dict[str, Any], bytes], int, Optional[requests.RequestException]]:
        """Perform a PATCH request with the given url and headers.

        Args:
            url: The url to PATCH.
            json_body: Any data to send to the url.
            headers: The headers to use during the request.
            auth: A tuple containing the username and password to use in the request.
            timeout: How many seconds to wait for the server to send data before giving up.
            return_bytes: A boolean indicating if the response content should be returned
                instead of the response json.
            allow_errors: A boolean indicating if errors are allowed.
            verbose: Set this to False in order to disable printouts.

        Returns:
            A tuple containing a success boolean, the response data, status code, and any errors
        """
        return self._send_request(
            SupportedRequestTypes.PATCH,
            url,
            json_body=json_body,
            headers=headers,
            auth=auth,
            timeout=timeout,
            return_bytes=return_bytes,
            allow_errors=allow_errors,
            verbose=verbose,
        )

    def post(  # noqa: PLR0913
        self,
        url: str,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        return_bytes: bool = False,
        allow_errors: bool = False,
        verbose: bool = True,
    ) -> Tuple[bool, Union[Dict[str, Any], bytes], int, Optional[requests.RequestException]]:
        """Perform a POST request with the given url and headers.

        Args:
            url: The url to POST.
            json_body: Any data to send to the url.
            headers: The headers to use during the request.
            auth: A tuple containing the username and password to use in the request.
            timeout: How many seconds to wait for the server to send data before giving up.
            return_bytes: A boolean indicating if the response content should be returned
                instead of the response json.
            allow_errors: A boolean indicating if errors are allowed.
            verbose: Set this to False in order to disable printouts.

        Returns:
            A tuple containing a success boolean, the response data, status code, and any errors
        """
        return self._send_request(
            SupportedRequestTypes.POST,
            url,
            json_body=json_body,
            headers=headers,
            auth=auth,
            timeout=timeout,
            return_bytes=return_bytes,
            allow_errors=allow_errors,
            verbose=verbose,
        )

    def put(  # noqa: PLR0913
        self,
        url: str,
        json_body: Dict[str, Any],
        headers: Optional[Mapping[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        return_bytes: bool = False,
        allow_errors: bool = False,
        verbose: bool = True,
    ) -> Tuple[bool, Union[Dict[str, Any], bytes], int, Optional[requests.RequestException]]:
        """Perform a PUT request with the given url and headers.

        Args:
            url: The url to PUT.
            json_body: Any data to send to the url.
            headers: The headers to use during the request.
            auth: A tuple containing the username and password to use in the request.
            timeout: How many seconds to wait for the server to send data before giving up.
            return_bytes: A boolean indicating if the response content should be returned
                instead of the response json.
            allow_errors: A boolean indicating if errors are allowed.
            verbose: Set this to False in order to disable printouts.

        Returns:
            A tuple containing a success boolean, the response data, status code, and any errors
        """
        return self._send_request(
            SupportedRequestTypes.PUT,
            url,
            json_body=json_body,
            headers=headers,
            auth=auth,
            timeout=timeout,
            return_bytes=return_bytes,
            allow_errors=allow_errors,
            verbose=verbose,
        )

    def set_api_version(self, api_version: int, verbose: bool = True) -> None:
        """Set the API version used by the device.

        Args:
            api_version: The API version to use for this device
            verbose: Set this to False in order to disable printouts.
        """
        self._api_url = self._base_url + self.API_VERSIONS[api_version]
        if self._verbose and verbose:
            print(f"{self._name_and_alias} API version set to: {api_version} ({self._api_url})")

    def wait_for_api_connection(
        self,
        wait_time: float,
        sleep_seconds: int = 5,
        accept_immediate_connection: bool = False,
        verbose: bool = True,
    ) -> bool:
        """Wait for an API call to go through to the device.

        Using wait_for_network_connection does not ensure that the API network is also up.

        Args:
            wait_time: The number of seconds to wait for the API connection.
            sleep_seconds: The number of seconds to sleep in between connection attempts.
            accept_immediate_connection: A boolean indicating if a connection on the
                                         first attempt is a valid connection.
            verbose: Set this to False in order to disable printouts.

        Returns:
            A boolean indicating if an API connection was made within the given time limit.

        Raises:
            AssertionError: Indicating that the device erroneously connected on the first try.
        """
        attempt_num = 0
        api_connection = False
        if verbose:
            print_with_timestamp(f"Attempting to establish an API connection with {self._api_url}")
        start_time = time.perf_counter()
        while (time.perf_counter() - start_time) <= wait_time:
            if api_connection := self._check_api_connection():
                # pylint: disable=compare-to-zero
                if attempt_num != 0 or accept_immediate_connection:
                    break
                msg = (
                    f"An API connection was established with "
                    f"{self._api_url} on the first attempt "
                    f"when it should not have been."
                )
                raise AssertionError(msg)
            time.sleep(sleep_seconds)
            attempt_num += 1

        end_time = time.perf_counter()
        total_time = end_time - start_time

        if verbose:
            if api_connection:
                print_with_timestamp(
                    f"Successfully established an API connection with {self._api_url} "
                    f"after {total_time:.2f} seconds"
                )
            else:
                print_with_timestamp(
                    f"Unable to establish an API connection with {self._api_url} "
                    f"after {total_time:.2f} seconds"
                )
        return api_connection

    ################################################################################################
    # Private Methods
    ################################################################################################
    @abstractmethod
    def _check_api_connection(self) -> bool:
        """Make any call to the API to check if there is a connection.

        Returns:
            A boolean indicating if the call was successful.
        """
        raise NotImplementedError

    # pylint: disable=too-many-branches
    def _send_request(  # noqa: PLR0913,PLR0912,C901
        self,
        request_type: SupportedRequestTypes,
        url: str,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        return_bytes: bool = False,
        allow_errors: bool = False,
        verbose: bool = True,
    ) -> Tuple[bool, Union[Dict[str, Any], bytes], int, Optional[requests.RequestException]]:
        """Perform a request with the given url and headers.

        Args:
            request_type: The type of request to send.
            url: The url to use.
            json_body: Any data to send to the url.
            headers: The headers to use during the request.
            auth: A tuple containing the username and password to use in the request.
            timeout: How many seconds to wait for the server to send data before giving up.
            return_bytes: A boolean indicating if the response content should be returned
                instead of the response json.
            allow_errors: A boolean indicating if errors are allowed.
            verbose: Set this to False in order to disable printouts.

        Returns:
            A tuple containing a success boolean, the response data, status code, and any errors

        Raises:
            ValueError: Indicates that an unsupported request type was provided.
        """
        # Sanitize the url by prepending the api url if necessary
        if not url.startswith(self._base_url):
            if not url.startswith("/"):
                url = "/" + url
            if any(url.startswith(api) for api in self.API_VERSIONS.values()):
                url = self._base_url + url
            else:
                url = self._api_url + url

        response = cast(requests.Response, None)
        retval: Union[Dict[str, Any], bytes] = {}
        if self._verbose and verbose:
            print_with_timestamp(f"({self._name_and_alias}) {request_type.value} >> {url}", end="")
            if headers:
                print(f", {headers=}", end="")
            if json_body:
                print(f", {json_body=}", end="")
            print("")

        try:
            if request_type == SupportedRequestTypes.DELETE:
                response = requests.delete(url, headers=headers, auth=auth, timeout=timeout)
            elif request_type == SupportedRequestTypes.GET:
                response = requests.get(url, headers=headers, auth=auth, timeout=timeout)
            elif request_type == SupportedRequestTypes.PATCH:
                response = requests.patch(
                    url, headers=headers, auth=auth, json=json_body, timeout=timeout
                )
            elif request_type == SupportedRequestTypes.POST:
                response = requests.post(
                    url, headers=headers, auth=auth, json=json_body, timeout=timeout
                )
            elif request_type == SupportedRequestTypes.PUT:
                response = requests.put(
                    url, headers=headers, auth=auth, json=json_body, timeout=timeout
                )
            else:
                msg = f"{request_type} is an unsupported request type."
                raise ValueError(msg)
            if self._verbose and verbose:
                print_with_timestamp(f"Response from {request_type.value} >>")
                if not return_bytes:
                    print(f"{json.dumps(response.json(), indent=2)}")
                else:
                    # Print .zip files as byte strings, response.content.decode() throws errors
                    print(f"\n{response.text}")
            retval = response.content if return_bytes else response.json()
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.exceptions.RequestException as error:
            if not allow_errors:
                self.raise_failure(
                    f"A RequestException occurred (status code {response.status_code}): {error}"
                )
            try:
                status_code = response.status_code
            except AttributeError:
                try:
                    status_code = (
                        error.response.status_code  # pyright: ignore[reportOptionalMemberAccess]
                    )
                except AttributeError:
                    status_code = 503
            return False, retval, status_code, error

        return True, retval, response.status_code, None
