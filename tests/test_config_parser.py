# pyright: reportPrivateUsage=none
"""Tests for the config_parser.py file."""

from pathlib import Path
from types import MappingProxyType
from typing import Dict, Mapping, Optional, Type
from unittest import mock

import pytest

from tm_devices.components import DMConfigParser
from tm_devices.helpers import (
    ConfigFileType,
    ConnectionTypes,
    DeviceConfigEntry,
    DeviceTypes,
    DMConfigOptions,
    SerialConfig,
)
from tm_devices.helpers.constants_and_dataclasses import CONFIG_CLASS_STR_PREFIX_MAPPING


def test_nested_config_prefix_mapping() -> None:
    """Test the DMConfigParser knows about all the things in CONFIG_CLASS_STR_PREFIX_MAPPING."""
    assert set(CONFIG_CLASS_STR_PREFIX_MAPPING.keys()) == set(
        DMConfigParser._CONFIG_NESTED_DICT_MAPPING.keys()  # noqa: SLF001
    ), (
        "Every class in CONFIG_CLASS_STR_PREFIX_MAPPING.keys() must have a reciprocal value in "
        "DMConfigParser._CONFIG_NESTED_DICT_MAPPING."
    )


def test_environment_variable_config(capsys: pytest.CaptureFixture[str]) -> None:
    """Test the environment variable config method."""
    options = ["STANDALONE"]
    expected_device_string = "address=MSO54-123456,connection_type=TCPIP,device_type=SCOPE"
    expected_device = DeviceConfigEntry(
        address="MSO54-123456",
        connection_type=ConnectionTypes.TCPIP,
        device_type=DeviceTypes.SCOPE,
    )
    expected_entry = MappingProxyType({"SCOPE 1": expected_device})

    with mock.patch.dict(
        "os.environ",
        {"TM_OPTIONS": ",".join(options), "TM_DEVICES": expected_device_string},
        clear=True,
    ):
        config = DMConfigParser()
    # string should be the env vars to recreate, this will also test that
    assert str(expected_device) == expected_device_string
    assert not config.options.teardown_cleanup
    assert config.options.standalone
    assert (
        config.devices == expected_entry
    ), f"\nDevice dictionaries don't match:\n{expected_entry}\n{config.devices}"

    # test that the config string representation looks like env declaration
    expected_entry_string = f"TM_OPTIONS=STANDALONE\nTM_DEVICES=~~~{expected_device_string}~~~"
    print(config)
    assert capsys.readouterr().out.strip() == expected_entry_string

    # test smu with serial properties
    expected_device_string = (
        "address=1,connection_type=SERIAL,device_type=SMU,serial_baud_rate=115200,"
        "serial_end_input=none,serial_flow_control=none,serial_parity=none,serial_stop_bits=one"
    )
    expected_device = DeviceConfigEntry(
        device_type=DeviceTypes.SMU,
        address="1",
        connection_type=ConnectionTypes.SERIAL,
        serial_config=SerialConfig(
            baud_rate=115200,
            end_input=SerialConfig.Termination.none,
            flow_control=SerialConfig.FlowControl.none,
            parity=SerialConfig.Parity.none,
            stop_bits=SerialConfig.StopBits.one,
        ),
    )
    expected_entry = MappingProxyType({"SMU 1": expected_device})

    with mock.patch.dict(
        "os.environ",
        {
            "TM_OPTIONS": ",".join(options),
            "TM_DEVICES": expected_device_string,
        },
        clear=True,
    ):
        config = DMConfigParser()

    assert str(expected_device) == expected_device_string
    assert (
        config.devices == expected_entry
    ), f"\nDevice dictionaries don't match:\n{expected_entry}\n{config.devices}"
    expected_entry_string = f"TM_OPTIONS=STANDALONE\nTM_DEVICES=~~~{expected_device_string}~~~"
    print(config)
    assert capsys.readouterr().out.strip() == expected_entry_string

    expected_device = DeviceConfigEntry(
        device_type=DeviceTypes.MT,
        device_driver="TMT4",
        address="127.0.0.1",
        connection_type=ConnectionTypes.REST_API,
    )
    expected_entry = MappingProxyType({"MT 1": expected_device})
    # string should be the env vars to recreate, this will also test that
    with mock.patch.dict(
        "os.environ",
        {"TM_OPTIONS": ",".join(options), "TM_DEVICES": str(expected_device)},
        clear=True,
    ):
        config = DMConfigParser()
    assert (
        expected_entry == config.devices
    ), f"\nDevice dictionaries don't match:\n{expected_entry}\n{config.devices}"


def test_file_config_default_path() -> None:
    """Test the default path to the config file."""
    file_contents = """
devices:
# This is a scope
- address: MSO54-123456
  connection_type: USB
  device_type: SCOPE
# This is a SMU
- address: 192.168.0.101
  connection_type: TCPIP
  device_type: SMU
# This is an AFG
- address: 123.45.6.789
  connection_type: TCPIP
  device_type: AFG
options:
  setup_cleanup: true
  teardown_cleanup: true
  standalone: false
  verbose_mode: false
  verbose_visa: false
  """
    expected_options = DMConfigOptions(
        standalone=False,
        setup_cleanup=True,
        teardown_cleanup=True,
        verbose_mode=False,
        verbose_visa=False,
    )
    expected_devices = {
        "SCOPE 1": DeviceConfigEntry(
            address="MSO54-123456",
            connection_type=ConnectionTypes.USB,
            device_type=DeviceTypes.SCOPE,
        ),
        "SMU 1": DeviceConfigEntry(
            address="192.168.0.101",
            connection_type=ConnectionTypes.TCPIP,
            device_type=DeviceTypes.SMU,
        ),
        "AFG 1": DeviceConfigEntry(
            address="123.45.6.789",
            connection_type=ConnectionTypes.TCPIP,
            lan_port=None,
            device_type=DeviceTypes.AFG,
            alias=None,
        ),
    }
    with mock.patch.dict("os.environ", {}, clear=True), mock.patch(
        "pathlib.Path.is_file", mock.MagicMock(return_value=True)
    ), mock.patch("builtins.open", mock.mock_open(read_data=file_contents)):
        config = DMConfigParser()

    assert expected_options == config.options
    assert (
        expected_devices == config.devices
    ), f"\nDevice dictionaries don't match:\n{expected_devices}\n{config.devices}"


@pytest.mark.parametrize(
    ("os_environ", "file_type"),
    [
        # test with toml
        (
            {"TM_DEVICES_CONFIG": str(Path(__file__).parent / "samples/sample_devices.toml")},
            DMConfigParser.FileType.TOML,
        ),
        # test with yaml
        (
            {"TM_DEVICES_CONFIG": str(Path(__file__).parent / "samples/sample_devices.yaml")},
            DMConfigParser.FileType.YAML,
        ),
    ],
)
def test_file_config_non_default_path(
    os_environ: Dict[str, str], file_type: ConfigFileType
) -> None:
    """Test the non-default path to the config file."""
    expected_options = DMConfigOptions(
        standalone=True,
        setup_cleanup=False,
        teardown_cleanup=False,
        verbose_mode=False,
        verbose_visa=False,
    )
    expected_devices = {
        "SCOPE 1": DeviceConfigEntry(
            address="MSO54-123456",
            connection_type=ConnectionTypes.TCPIP,
            device_type=DeviceTypes.SCOPE,
        ),
        "SCOPE 2": DeviceConfigEntry(
            address="789.56.4.123",
            connection_type=ConnectionTypes.SOCKET,
            lan_port=4000,
            device_type=DeviceTypes.SCOPE,
            alias="foo",
        ),
        "AFG 1": DeviceConfigEntry(
            address="123.45.6.789",
            connection_type=ConnectionTypes.TCPIP,
            device_type=DeviceTypes.AFG,
            alias="afg",
        ),
        "SMU 1": DeviceConfigEntry(
            address="1",
            connection_type=ConnectionTypes.SERIAL,
            device_type=DeviceTypes.SMU,
            alias="serial_smu",
            serial_config=SerialConfig(baud_rate=9600, end_input=SerialConfig.Termination.none),
        ),
    }
    with mock.patch.dict("os.environ", os_environ, clear=True):
        config = DMConfigParser()

    # Test explicitly loading file
    config_2 = DMConfigParser()
    config_2.load_config_file(os_environ["TM_DEVICES_CONFIG"])

    # Read in the golden files
    with open(os_environ["TM_DEVICES_CONFIG"], encoding="utf-8") as config_file:
        text = config_file.read()

    assert config.to_config_file_text(file_type) == text, "issue generating config file text"
    assert config_2.to_config_file_text(file_type) == text, "issue generating config file text"

    assert expected_options == config.options
    assert (
        expected_devices == config.devices
    ), f"\nDevice dictionaries don't match:\n{expected_devices}\n{config.devices}"
    assert expected_options == config_2.options
    assert (
        expected_devices == config_2.devices
    ), f"\nDevice dictionaries don't match:\n{expected_devices}\n{config_2.devices}"


# TODO: test with duplicated device address, one with domain name, one without
@pytest.mark.parametrize(
    ("os_environ", "expected_exception"),
    [
        # test with an unrecognized option
        ({"TM_OPTIONS": "INVALID", "TM_DEVICES": ""}, KeyError),
        # test with duplicate device alias names
        (
            {
                "TM_DEVICES": "device_type=SCOPE,address=MSO54-123456.unit.test.domain,alias=foo"
                "~~~device_type=SCOPE,address=MSO54-654321.unit.test.domain,alias=foo"
            },
            KeyError,
        ),
        # test with duplicated device address
        (
            {
                "TM_DEVICES": "device_type=SCOPE,address=MSO54-123456~~~"
                "device_type=SCOPE,address=MSO54-123456"
            },
            ValueError,
        ),
        # test with invalid entry
        (
            {"TM_DEVICES": "device_type=SCOPE,address#MSO54-123456,connection_type==TCPIP"},
            ValueError,
        ),
        # test with invalid device type entry
        (
            {"TM_DEVICES": "device_type=INVALID,address=MSO54-123456,connection_type=TCPIP"},
            TypeError,
        ),
        # test with invalid connection type for the device
        ({"TM_DEVICES": "device_type=AFG,connection_type=REST_API,address=123.4.5.678"}, TypeError),
        # test with connection type that doesn't exist
        ({"TM_DEVICES": "device_type=AFG,connection_type=INVALID,address=123.4.5.678"}, TypeError),
        # test with device type that doesn't exist
        (
            {
                "TM_DEVICES": "device_type=_UNIT_TEST_ONLY_DEVICE_DO_NOT_USE,"
                "connection_type=REST_API,address=123.4.5.678"
            },
            TypeError,
        ),
        # Test socket connection without port
        (
            {"TM_DEVICES": "device_type=SCOPE,connection_type=SOCKET,address=MSO54-123456"},
            ValueError,
        ),
        # Test USB connection with invalid address format
        ({"TM_DEVICES": "device_type=SCOPE,connection_type=USB,address=MSO54 123456"}, ValueError),
        # Test USB connection with STANDALONE
        (
            {
                "TM_OPTIONS": "STANDALONE",
                "TM_DEVICES": "device_type=SCOPE,connection_type=USB,address=MSO54-123456",
            },
            ValueError,
        ),
        # Test SERIAL connection with invalid address format
        ({"TM_DEVICES": "device_type=SCOPE,connection_type=SERIAL,address=COM1"}, ValueError),
        # Test SERIAL connection with invalid baud rate
        (
            {
                "TM_OPTIONS": "STANDALONE",
                "TM_DEVICES": "device_type=SCOPE,connection_type=SERIAL,address=1,"
                "serial_baud_rate=100",
            },
            ValueError,
        ),
        # Test SERIAL connection with invalid data bits rate
        (
            {
                "TM_DEVICES": "device_type=SCOPE,connection_type=SERIAL,address=1,"
                "serial_data_bits=4",
            },
            ValueError,
        ),
        # Test GPIB connection with invalid address
        (
            {"TM_DEVICES": "device_type=SCOPE,connection_type=GPIB,address=99"},
            ValueError,
        ),
        # Test REST_API connection with no device driver
        (
            {"TM_DEVICES": "device_type=MT,connection_type=REST_API,address=localhost"},
            ValueError,
        ),
    ],
)
def test_invalid_config_creation(
    os_environ: Dict[str, str], expected_exception: Type[Exception]
) -> None:
    """Test creating invalid configs.

    Args:
        os_environ: The dict to patch to os.environ.
        expected_exception: The exception that is expected to be raised.
    """
    with mock.patch.dict("os.environ", os_environ, clear=True), pytest.raises(expected_exception):
        DMConfigParser()


def test_invalid_config_creation_from_file() -> None:
    """Test loading a config file with an invalid option."""
    with mock.patch.dict(
        "os.environ",
        {"TM_DEVICES_CONFIG": str(Path(__file__).parent / "samples/invalid_config_option.yaml")},
        clear=True,
    ):
        with pytest.raises(KeyError) as error:
            DMConfigParser()
        assert str(error.value.args[0]) == "Invalid configuration options found: ['invalid_option']"


def test_sequential_env_var_devices() -> None:
    """Test environment variable idiosyncrasies."""
    device_string = (
        "address=MSO64-654321,connection_type=TCPIP,"
        "device_type=SCOPE~~~"
        "address=MSO54-123456,alias=MY-ALIAS,connection_type=TCPIP,"
        "device_type=SCOPE"
    )

    expected_devices = MappingProxyType(
        {
            "SCOPE 1": DeviceConfigEntry(
                device_type=DeviceTypes.SCOPE,
                address="MSO64-654321",
                connection_type=ConnectionTypes.TCPIP,
            ),
            "SCOPE 2": DeviceConfigEntry(
                device_type=DeviceTypes.SCOPE,
                address="MSO54-123456",
                connection_type=ConnectionTypes.TCPIP,
                alias="MY-ALIAS",
            ),
        }
    )

    with mock.patch.dict("os.environ", {"TM_DEVICES": device_string}, clear=True):
        config = DMConfigParser()
    assert (
        expected_devices == config.devices
    ), f"\nDevice dictionaries don't match:\n{expected_devices}\n{config.devices}"
    assert expected_devices["SCOPE 2"] == config.devices["MY-ALIAS"]


def test_add_device() -> None:
    """Verify a device can be added to an empty config."""
    with mock.patch.dict("os.environ", {}, clear=True), mock.patch(
        "os.path.isfile", mock.MagicMock(return_value=False)
    ):
        config = DMConfigParser()
    expected_devices_1: Mapping[str, DeviceConfigEntry] = MappingProxyType({})
    assert (
        expected_devices_1 == config.devices
    ), f"\nDevice dictionaries don't match:\n{expected_devices_1}\n{config.devices}"
    config.add_device(
        device_type="SCOPE",
        connection_type="TCPIP",
        address="MSO54-123456",
        alias="ALIAS",
    )
    expected_devices_2 = MappingProxyType(
        {
            "SCOPE 1": DeviceConfigEntry(
                device_type=DeviceTypes.SCOPE,
                address="MSO54-123456",
                connection_type=ConnectionTypes.TCPIP,
                alias="ALIAS",
            )
        }
    )
    assert (
        expected_devices_2 == config.devices
    ), f"\nDevice dictionaries don't match:\n{expected_devices_2}\n{config.devices}"

    # Verify that adding a device with a duplicate alias is not allowed
    with pytest.raises(KeyError):
        config.add_device(device_type="AWG", address="127.0.0.1", alias="ALIAS")


def test_remove_device() -> None:
    """Verify a device can be removed."""
    device_string = "device_type=SCOPE,address=MSO54-123456.unit.test.domain"
    expected_devices: Mapping[str, DeviceConfigEntry] = MappingProxyType({})
    with mock.patch.dict(
        "os.environ", {"TM_OPTIONS": "STANDALONE", "TM_DEVICES": device_string}, clear=True
    ):
        config = DMConfigParser()
    config.remove_device("SCOPE 1")
    assert (
        expected_devices == config.devices
    ), f"\nDevice dictionaries don't match:\n{expected_devices}\n{config.devices}"


@pytest.mark.parametrize(
    ("instrument_string", "device_name", "expected_expr"),
    [
        (
            "device_type=SCOPE,address=MSO58-3000260",
            "SCOPE 1",
            "TCPIP0::MSO58-3000260::inst0::INSTR",
        ),
        (
            "device_type=SCOPE,connection_type=SOCKET,address=192.168.0.1,lan_port=4000",
            "SCOPE 1",
            "TCPIP0::192.168.0.1::4000::SOCKET",
        ),
        (
            "device_type=SCOPE,connection_type=USB,address=MSO58-3000260000",
            "SCOPE 1",
            "USB0::0x0699::0x0522::3000260000::0::INSTR",
        ),
        (
            "device_type=SCOPE,connection_type=USB,address=MSO64B-3000260000",
            "SCOPE 1",
            "USB0::0x0699::0x0530::3000260000::0::INSTR",
        ),
        (
            "device_type=SCOPE,connection_type=USB,address=MSO58LP-3000260000",
            "SCOPE 1",
            "USB0::0x0699::0x0529::3000260000::0::INSTR",
        ),
        (
            "device_type=SCOPE,address=MSO58-3000260~~~device_type=AFG,connection_type=USB,address=AFG3252-C0123123",
            "AFG 1",
            "USB0::0x0699::0x0345::C0123123::0::INSTR",
        ),
        (
            "device_type=SCOPE,address=3,connection_type=SERIAL",
            "SCOPE 1",
            "ASRL3::INSTR",
        ),
        (
            "device_type=MT,device_driver=TMT4,address=1.2.3.4,connection_type=REST_API",
            "MT 1",
            None,
        ),
    ],
)
def test_get_visa_resource_expression(
    instrument_string: str, device_name: str, expected_expr: Optional[str]
) -> None:
    """Test creating a resource expression.

    Args:
        instrument_string: The configuration string being tested.
        device_name: The device name to fetch from the config.
        expected_expr: The expected output of the function being tested.
    """
    with mock.patch.dict("os.environ", {"TM_DEVICES": instrument_string}, clear=True):
        config = DMConfigParser()
        device = config.devices[device_name]
        if expected_expr is not None:
            returned_expr = device.get_visa_resource_expression()
            assert returned_expr == expected_expr
        else:
            with pytest.raises(
                ValueError, match=r"[A-Z_]+ is not a valid connection type for a VISA resource\."
            ):
                device.get_visa_resource_expression()


def test_get_visa_resource_expression_errors() -> None:
    """Test creating a resource expression throws the proper errors."""
    # Test trying to connect to a USB device that doesn't exist
    with mock.patch.dict(
        "os.environ",
        {"TM_DEVICES": "device_type=SCOPE,connection_type=USB,address=MSO123456-3000260000"},
        clear=True,
    ), pytest.warns(UserWarning):
        config = DMConfigParser()
        device = config.devices["SCOPE 1"]
        with pytest.raises(NotImplementedError):
            device.get_visa_resource_expression()

    with pytest.raises(TypeError):
        _ = DeviceConfigEntry(
            device_type=DeviceTypes.SCOPE,
            connection_type=ConnectionTypes._UNIT_TEST_ONLY_CONNECTION_DO_NOT_USE,  # noqa: SLF001
            address="127.0.0.1",
        )
