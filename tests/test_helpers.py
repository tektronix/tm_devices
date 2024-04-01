# pyright: reportPrivateUsage=none
"""Tests for the helpers subpackage."""

import datetime
import random
import socket

from collections import OrderedDict
from contextlib import redirect_stdout
from io import StringIO
from subprocess import CalledProcessError, SubprocessError
from typing import Any, ClassVar, Dict, List, Optional, Tuple
from unittest import mock

import dateutil.parser
import pytest
import pyvisa as visa

from dateutil.tz import tzlocal
from packaging.version import InvalidVersion, Version
from requests import Response

from conftest import SIMULATED_VISA_LIB
from tm_devices.helpers import (
    check_for_update,
    check_network_connection,
    check_port_connection,
    check_visa_connection,
    ConnectionTypes,
    create_visa_connection,
    detect_visa_resource_expression,
    DeviceConfigEntry,
    DeviceTypes,
    get_model_series,
    get_version,
    get_visa_backend,
    ping_address,
    print_with_timestamp,
    sanitize_enum,
    SupportedModels,
    VALID_DEVICE_CONNECTION_TYPES,
)

# noinspection PyPep8Naming
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

MODEL_SERIES_LIST = SupportedModels.list_values()


def test_create_ping_command() -> None:
    """Test the creation of the ping command."""
    # pylint: disable=import-outside-toplevel,import-private-name,useless-suppression
    from tm_devices.helpers.functions import _create_ping_command

    with mock.patch("platform.system", mock.MagicMock(return_value="Windows")):
        assert _create_ping_command("127.0.0.1") == "ping 127.0.0.1 -n 1 -w 2000"
    with mock.patch("platform.system", mock.MagicMock(return_value="Linux")):
        assert _create_ping_command("localhost") == "ping localhost -c 1 -w 2"
    with mock.patch("platform.system", mock.MagicMock(return_value="Darwin")):
        assert _create_ping_command("localhost") == "ping localhost -c 1 -W 2"

    # Invalid addresses
    with pytest.raises(
        ValueError,
        match=r"address='0.0.0.0.0.0.0.0.0.0.0.0.0.' is not a valid IP address or hostname.",
    ):
        _create_ping_command("0.0.0.0.0.0.0.0.0.0.0.0.0.")


@pytest.mark.parametrize(
    ("input_string", "expected_abbrev_model"),
    [
        ("TEKSCOPESW", "TekScopeSW"),
        ("MSO54-123456", "MSO5"),
        ("MSO58B", "MSO5B"),
        ("MSO58LP", "MSO5LP"),
        ("LPD64", "LPD6"),
        ("MSO66B", "MSO6B"),
        ("MSO70604C", "MSO70KC"),
        ("MSO70604", "MSO70K"),
        ("AWG5204", "AWG5200"),
        ("AWG5012C", "AWG5KC"),
        ("AWG5012B", "AWG5KB"),
        ("AWG5012", "AWG5K"),
        ("AWG70002B", "AWG70KB"),
        ("AFG3252", "AFG3K"),
        ("AFG31021", "AFG31K"),
        ("AFG3152C", "AFG3KC"),
        ("TSOVu", "TSOVu"),
        ("MODEL 2470", "SMU2470"),
        ("2470", "SMU2470"),
        (" Model 2606B", "SMU2606B"),
        (" Model 2612B", "SMU2612B"),
        (" 2612b", "SMU2612B"),
        (" 2230G-30-6", "PSU2230"),
        ("PROTOTYPE", "PROTOTYPE"),
        ("MODEL 2601B-PULSE", "SMU2601BPulse"),
        ("MODEL 2611B-L", "SMU2611B"),
        ("MODEL DAQ6510", "DAQ6510"),
        ("DAQ6510", "DAQ6510"),
        ("MODEL DMM6500", "DMM6500"),
        ("DMM6500", "DMM6500"),
        ("MODEL 6517B", "SMU6517B"),
        ("2231A-30-3", "PSU2231A"),
    ],
)
def test_get_model_series(input_string: str, expected_abbrev_model: str) -> None:
    """Test the model series creation function.

    Args:
        input_string: The input string to the function being tested.
        expected_abbrev_model: The expected output of the function being tested.
    """
    if expected_abbrev_model not in MODEL_SERIES_LIST:
        with pytest.warns(UserWarning):
            assert get_model_series(input_string) == expected_abbrev_model
    else:
        assert get_model_series(input_string) == expected_abbrev_model


def test_ping_address() -> None:
    """Test pinging an address."""
    assert "ttl=" in ping_address("127.0.0.1", timeout=1).lower()
    with mock.patch(
        "subprocess.check_output", mock.MagicMock(side_effect=CalledProcessError(1, "error"))
    ):
        retval = ping_address("127.0.0.1", timeout=1)
        assert retval == ""


def test_check_network_connection() -> None:
    """Test checking a network connection."""
    stdout = StringIO()
    with redirect_stdout(stdout):
        assert check_network_connection("name", "127.0.0.1")[0]
    message = stdout.getvalue()
    assert "ping >> 127.0.0.1" in message
    assert "Response from ping >>" in message

    stdout = StringIO()
    with redirect_stdout(stdout):
        assert check_network_connection("name", "127.0.0.1", verbose=False)[0]
    assert stdout.getvalue() == ""


def test_check_port_connection() -> None:
    """Test checking a port connection."""
    stdout = StringIO()
    with redirect_stdout(stdout), mock.patch(
        "socket.socket.connect", mock.MagicMock(return_value=None)
    ), mock.patch("socket.socket.shutdown", mock.MagicMock(return_value=None)):
        assert check_port_connection("name", "127.0.0.1", 80, timeout_seconds=1)
    message = stdout.getvalue()
    assert "(name) >> checking if port 80 is open on 127.0.0.1" in message
    assert message.endswith("Result >> True\n")

    stdout = StringIO()
    with redirect_stdout(stdout), mock.patch(
        "socket.socket.connect", mock.MagicMock(side_effect=socket.error(""))
    ):
        assert not check_port_connection(
            "name", "127.0.0.1", 55555, timeout_seconds=1, verbose=False
        )
    assert stdout.getvalue() == ""


def test_print_with_timestamp() -> None:
    """Test the print_with_timestamp helper function."""
    stdout = StringIO()
    with redirect_stdout(stdout):
        now = datetime.datetime.now(tz=tzlocal())
        print_with_timestamp("message")

    message = stdout.getvalue()
    message_parts = message.split(" - ")
    assert len(message_parts) == 2
    assert message_parts[1] == "message\n"
    parsed_datetime = dateutil.parser.parse(message_parts[0].strip())
    allowed_difference = datetime.timedelta(
        days=0,
        hours=0,
        minutes=0,
        seconds=1,
        microseconds=0,
    )
    calculated_difference = abs(parsed_datetime - now)
    assert calculated_difference <= allowed_difference


def test_sanitizing_enums() -> None:
    """Verify that the sanitization functions work."""
    assert sanitize_enum("SCOPE", DeviceTypes) == DeviceTypes.SCOPE

    with pytest.raises(TypeError):
        sanitize_enum("INVALID", DeviceTypes)


def test_enum_list_values() -> None:
    """Test that the method to list enum values works."""
    assert ConnectionTypes.list_values() == [
        "REST_API",
        "SERIAL",
        "SOCKET",
        "TCPIP",
        "USB",
        "GPIB",
        "MOCK",
        "_UNIT_TEST_ONLY_CONNECTION_DO_NOT_USE",
    ]


def test_device_types_in_valid_device_connection_types() -> None:
    """Verify that all supported types are in the device connection mapping and vice versa."""
    supported_models_list = [x for x in DeviceTypes if "UNIT_TEST" not in x.value]
    device_driver_list = list(VALID_DEVICE_CONNECTION_TYPES)

    assert supported_models_list == device_driver_list


def test_create_and_check_visa_connection(capsys: pytest.CaptureFixture[str]) -> None:
    """Test creating a VISA connection to a device.

    Args:
        capsys: The captured stdout and stderr.
    """
    dev_config_1 = DeviceConfigEntry(
        device_type=DeviceTypes.SCOPE,
        connection_type=ConnectionTypes.TCPIP,
        address="127.0.0.1",
    )
    dev_config_2 = DeviceConfigEntry(
        device_type=DeviceTypes.SCOPE,
        connection_type=ConnectionTypes.USB,
        address="MSO5-SERIAL",
    )
    with mock.patch("pyvisa.ResourceManager", mock.MagicMock(side_effect=visa.Error())):
        with pytest.raises(ConnectionError) as error:
            create_visa_connection(dev_config_1, "", retry_connection=True)
        assert "Unable to establish a VISA connection to " in str(error.value)
        assert "This is the current ping output" in str(error.value)
        with pytest.raises(ConnectionError) as error:
            create_visa_connection(dev_config_1, "", retry_connection=False)
        assert "Unable to establish a VISA connection to " in str(error.value)
        assert "This is the current ping output" not in str(error.value)
        with pytest.raises(ConnectionError) as error:
            create_visa_connection(dev_config_2, "", retry_connection=True)
        assert "Unable to establish a VISA connection to " in str(error.value)
        assert "This is the current ping output" not in str(error.value)
    dev_config_3 = DeviceConfigEntry(
        device_type=DeviceTypes.AFG,
        connection_type=ConnectionTypes.SOCKET,
        address="AFG3252C-HOSTNAME",
        lan_port=10001,
    )
    visa_obj = create_visa_connection(dev_config_3, SIMULATED_VISA_LIB)
    assert visa_obj.read_termination == "\n"
    assert visa_obj.write_termination == "\n"

    assert check_visa_connection(dev_config_3, SIMULATED_VISA_LIB, "dev_config_3")
    stdout = capsys.readouterr().out
    assert "checking if a VISA connection can be made to " in stdout
    assert "Result >> True" in stdout

    assert check_visa_connection(dev_config_3, SIMULATED_VISA_LIB, "dev_config_3", verbose=False)
    stdout = capsys.readouterr().out
    assert "checking if a VISA connection can be made to " not in stdout
    assert "Result >> True" not in stdout

    with mock.patch("pyvisa.ResourceManager", mock.MagicMock(side_effect=visa.Error())):
        assert not check_visa_connection(
            dev_config_3, SIMULATED_VISA_LIB, "dev_config_3", verbose=False
        )


def test_check_for_update(capsys: pytest.CaptureFixture[str]) -> None:
    """Test checking for a package update.

    Args:
        capsys: The captured stdout and stderr.
    """
    # Check for a package that isn't installed locally
    check_for_update("doesn't-exist")
    stdout = capsys.readouterr().out
    assert "doesn't-exist is not installed, unable to check for updates." in stdout

    # Check for a package that isn't available on PyPI
    response = Response()
    response._content = b">no version here<"  # noqa: SLF001
    with mock.patch("requests.get", mock.MagicMock(return_value=response)):
        check_for_update("pytest")
    stdout = capsys.readouterr().out
    assert "pytest is not available on pypi.org, unable to check for updates." in stdout

    # Test when an update is available
    response = Response()
    response._content = b'{"releases": {"0.0.0": []}}'  # noqa: SLF001
    with mock.patch("requests.get", mock.MagicMock(return_value=response)):
        check_for_update("pytest")
    stdout = capsys.readouterr().out
    assert "Version 0.0.0 of pytest is available on pypi.org." in stdout
    assert f"Version {pytest.__version__} of pytest is currently installed." in stdout
    assert "To upgrade pytest run the following command: python -m pip install -U pytest" in stdout

    # Test when the versions match
    response = Response()
    response._content = f'{{"releases": {{"{pytest.__version__}": []}}}}'.encode()  # noqa: SLF001
    with mock.patch("requests.get", mock.MagicMock(return_value=response)):
        check_for_update("pytest")
    stdout = capsys.readouterr().out
    assert stdout == ""


def test_get_visa_backend() -> None:
    """Verify that the VISA backend can be determined properly."""
    # pylint: disable=import-outside-toplevel,import-private-name,useless-suppression
    from tm_devices.helpers.functions import (
        _get_system_visa_info,
    )

    testing_system_details: Dict[Any, Any] = {
        "pyvisa": "1.12.0",
        "backends": OrderedDict(
            [
                (
                    "ivi",
                    OrderedDict(
                        [
                            ("Version", "1.12.0 (bundled with PyVISA)"),
                            (
                                "#1: C:\\WINDOWS\\system32\\visa32.dll",
                                OrderedDict(
                                    [
                                        ("found by", "auto"),
                                        ("bitness", "64"),
                                        ("Vendor", "National Instruments"),
                                    ]
                                ),
                            ),
                            (
                                "#3: C:\\WINDOWS\\system32\\visa.dll",
                                OrderedDict(
                                    [
                                        ("found by", "auto"),
                                        ("bitness", "64"),
                                        ("Vendor", "Custom Vendor"),
                                    ]
                                ),
                            ),
                        ]
                    ),
                ),
                (
                    "py",
                    OrderedDict(
                        [
                            ("Version", "0.5.3"),
                            ("ASRL INSTR", "Available via PySerial (3.5)"),
                            ("USB INSTR", "Available via PyUSB (1.2.1). Backend: libusb1"),
                            ("USB RAW", "Available via PyUSB (1.2.1). Backend: libusb1"),
                            ("TCPIP INSTR", "Available "),
                            ("TCPIP SOCKET", "Available "),
                        ]
                    ),
                ),
                ("sim", OrderedDict([("Version", "0.5.1"), ("Spec version", "1.1")])),
            ]
        ),
    }

    try:
        _get_system_visa_info.cache_clear()
        with mock.patch(
            "pyvisa.util.get_system_details",
            mock.MagicMock(return_value=testing_system_details),
        ), mock.patch(
            "platform.system",
            mock.MagicMock(return_value="windows"),
        ):
            assert get_visa_backend("tests/sim_devices/devices.yaml") == "PyVISA-sim"
            assert get_visa_backend("py") == "PyVISA-py"
            assert get_visa_backend("C:\\WINDOWS\\system32\\visa32.dll") == "NI-VISA"
            assert get_visa_backend("C:\\WINDOWS\\system32\\visa.dll") == "Custom Vendor VISA"
            assert get_visa_backend("nothing") == ""

        with mock.patch(
            "platform.system",
            mock.MagicMock(return_value="darwin"),
        ):
            _get_system_visa_info.cache_clear()
            with mock.patch(
                "subprocess.check_output",
                mock.MagicMock(return_value=b"System Integrity Protection status: enabled."),
            ):
                assert get_visa_backend("tests/sim_devices/devices.yaml") == ""
                assert get_visa_backend("py") == "PyVISA-py"

            _get_system_visa_info.cache_clear()
            with mock.patch(
                "subprocess.check_output",
                mock.MagicMock(return_value=b"System Integrity Protection status: disabled."),
            ):
                assert get_visa_backend("tests/sim_devices/devices.yaml") == "PyVISA-sim"
                assert get_visa_backend("py") == "PyVISA-py"

            _get_system_visa_info.cache_clear()
            with mock.patch(
                "subprocess.check_output",
                mock.MagicMock(side_effect=SubprocessError()),
            ):
                assert get_visa_backend("tests/sim_devices/devices.yaml") == "PyVISA-sim"
                assert get_visa_backend("py") == "PyVISA-py"
    finally:
        _get_system_visa_info.cache_clear()


@pytest.mark.parametrize(
    ("input_str", "expected_result"),
    [
        ("SMU2450-HOSTNAME", None),
        ("127.0.0.9", None),
        ("2450-01419964", None),
        ("USB0::0x05E6::0x2450::01419964::INSTR", ("USB", "2450-01419964")),
        ("USB::0x05E6::0x2450::01419964::INSTR", ("USB", "2450-01419964")),
        ("USB::0x05E6::0x2450::01419964::inst0::INSTR", ("USB", "2450-01419964")),
        ("USB::0x05E6::0x2450::01419964::inst::INSTR", ("USB", "2450-01419964")),
        ("TCPIP0::SMU2450-HOSTNAME::INSTR", ("TCPIP", "SMU2450-HOSTNAME")),
        ("TCPIP::SMU2450-HOSTNAME::INSTR", ("TCPIP", "SMU2450-HOSTNAME")),
        ("TCPIP0::SMU2450-HOSTNAME::inst0::INSTR", ("TCPIP", "SMU2450-HOSTNAME")),
        ("TCPIP0::127.0.0.9::inst0::INSTR", ("TCPIP", "127.0.0.9")),
        ("TCPIP::127.0.0.9::inst::INST", ("TCPIP", "127.0.0.9")),
        ("USB0::0x0699::0x0522::SERIAL1::INSTR", ("USB", "MSO5-SERIAL1")),
        ("TCPIP0::127.0.0.9::4000::SOCKET", ("SOCKET", "127.0.0.9:4000")),
        ("GPIB0::1::INSTR", ("GPIB", "1")),
        ("ASRL1::INSTR", ("SERIAL", "1")),
        ("MOCK0::127.0.0.9::INSTR", ("MOCK", "127.0.0.9")),
    ],
)
def test_detect_visa_resource_expression(
    input_str: str, expected_result: Optional[Tuple[str, str]]
) -> None:
    """Verify that a VISA resource expression can be properly detected."""
    assert detect_visa_resource_expression(input_str) == expected_result


@pytest.mark.parametrize(
    ("version_string", "expected_result"),
    [
        ("1.2.3", Version("1.2.3")),
        ("1.265.301", Version("1.265.301")),
        ("1.2.3.abc", Version("1.2.3+abc")),
        ("1.2.3.4abc", Version("1.2.3.4+abc")),
        ("1.20.345.abc", Version("1.20.345+abc")),
        ("1.20.345.4abc123", Version("1.20.345.4+abc123")),
    ],
)
def test_get_version(version_string: str, expected_result: Version) -> None:
    """Verify version strings can be correctly generated."""
    assert get_version(version_string) == expected_result


def test_get_version_error() -> None:
    """Verify invalid version strings still raise an error."""
    with pytest.raises(InvalidVersion):
        get_version("1a.2.3.abc")
    with pytest.raises(InvalidVersion):
        get_version("invalid-version")


def test_read_only_cached_property() -> None:
    """Verify the implementation of the read-only cached_property decorator."""

    # pylint: disable=missing-class-docstring,missing-function-docstring,too-few-public-methods
    class ClassWithReadOnlyCachedProperty:
        counter = 0
        previous_values: ClassVar[List[int]] = []

        @cached_property
        def c(self) -> int:
            self.counter += 1
            while True:
                if (val := random.randint(1, 1_000_000)) not in self.previous_values:  # noqa: S311
                    self.previous_values.append(val)
                    return val

    instance = ClassWithReadOnlyCachedProperty()
    val_1 = instance.c
    assert instance.counter == 1
    val_2 = instance.c
    assert instance.counter == 1
    assert val_1 == val_2

    with pytest.raises(AttributeError):
        # noinspection PyPropertyAccess
        instance.c = -1234
    assert instance.c == val_1
    assert instance.counter == 1
    # noinspection PyPropertyAccess
    del instance.c
    assert instance.c != val_1
    assert instance.counter == 2
