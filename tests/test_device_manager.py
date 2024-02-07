# pyright: reportUnusedFunction=none
# pyright: reportUnknownMemberType=none
# pyright: reportAttributeAccessIssue=none
# pyright: reportUnknownVariableType=none
# pyright: reportArgumentType=none
"""Tests for the device_manager.py file."""
import contextlib
import os
import subprocess
import sys

from pathlib import Path
from typing import Generator, Iterator, List
from unittest import mock

import pytest
import pyvisa as visa
import pyvisa.constants

from conftest import SIMULATED_VISA_LIB
from tm_devices import DeviceManager
from tm_devices.drivers import AFG3K, AFG3KC
from tm_devices.drivers.device import Device
from tm_devices.drivers.pi.scopes.scope import Scope
from tm_devices.drivers.pi.signal_sources.afgs.afg import AFG
from tm_devices.drivers.pi.signal_sources.signal_source import SignalSource
from tm_devices.helpers import ConnectionTypes, DeviceTypes, PYVISA_PY_BACKEND, SerialConfig


@pytest.fixture(scope="module", autouse=True)
def _remove_added_methods() -> Iterator[None]:
    """Remove custom added methods from devices."""
    yield
    for obj, name in (
        (Device, "inc_cached_count"),
        (Device, "inc_count"),
        (Device, "class_name"),
        (Device, "custom_model_getter"),
        (Device, "custom_list"),
        (Device, "custom_return_none"),
        (Device, "already_exists"),
        (Scope, "custom_model_getter_scope"),
        (Scope, "custom_return"),
        (SignalSource, "custom_model_getter_ss"),
        (AFG, "custom_model_getter_afg"),
        (AFG3K, "custom_model_getter_afg3k"),
        (AFG3KC, "custom_model_getter_afg3kc"),
    ):
        with contextlib.suppress(AttributeError):
            delattr(obj, name)


@pytest.fixture(autouse=True)
def _reset_dm(device_manager: DeviceManager) -> Generator[None, None, None]:
    """Reset the device_manager settings after each test.

    Args:
        device_manager: The device manager fixture.
    """
    saved_setup_enable = device_manager.setup_cleanup_enabled
    saved_teardown_enable = device_manager.teardown_cleanup_enabled
    yield
    device_manager.setup_cleanup_enabled = saved_setup_enable
    device_manager.teardown_cleanup_enabled = saved_teardown_enable


class TestDeviceManager:  # pylint: disable=no-self-use
    """Device Manager test class."""

    @pytest.mark.parametrize(
        # Get the list of device types, ignore the unit test ones since
        # this test only applies to actual supported devices.
        "device_type",
        list(filter(lambda x: "UNIT_TEST" not in x, (y.name for y in DeviceTypes))),
    )
    def test_supported_device_type_methods(self, device_type: str) -> None:
        """Test that all supported device types have a getter method in the DeviceManager.

        Args:
            device_type: The device type being tested.
        """
        assert hasattr(DeviceManager, f"add_{device_type}".lower())
        assert hasattr(DeviceManager, f"get_{device_type}".lower())

    def test_get_config_methods_with_devices(self, device_manager: DeviceManager) -> None:
        """Test the serial_config when adding to the DeviceManager.

        Needed for coverage with creating visa connection and updating serial settings.

        Args:
            device_manager: The DeviceManager object.
        """
        # use a serial device for coverage with updating visa_object serial settings.
        device_manager.remove_all_devices()
        device_manager.add_smu(
            "1",
            alias="testing",
            connection_type=ConnectionTypes.SERIAL.value,
            serial_config=SerialConfig(
                baud_rate=115200,
                data_bits=8,
                parity=SerialConfig.Parity.none,
                stop_bits=SerialConfig.StopBits.one,
                flow_control=SerialConfig.FlowControl.xon_xoff,
                end_input=SerialConfig.Termination.none,
            ),
        )
        device_manager.add_scope("MSO56-HOSTNAME")
        try:
            with mock.patch.dict("os.environ", {"TM_DEVICES_CONFIG": "./temp_config.toml"}):
                # respect the env var if no path is given
                device_manager.write_current_configuration_to_config_file()
                # respect the env var if no path is given
                device_manager.write_current_configuration_to_config_file("./temp_config.yaml")
            with open("./temp_config.toml", encoding="utf-8") as temp_config:
                text = temp_config.read()
            assert (
                text
                == """[[devices]]
address = "1"
alias = "TESTING"
connection_type = "SERIAL"
device_type = "SMU"

[devices.serial_config]
baud_rate = 115200
data_bits = 8
end_input = "none"
flow_control = "xon_xoff"
parity = "none"
stop_bits = "one"

[[devices]]
address = "MSO56-HOSTNAME"
connection_type = "TCPIP"
device_type = "SCOPE"

[options]
setup_cleanup = false
standalone = false
teardown_cleanup = false
verbose_mode = true
verbose_visa = false
"""
            )
            with open("./temp_config.yaml", encoding="utf-8") as temp_config:
                text = temp_config.read()
                print(text)
            assert (
                text
                == """---
devices:
  - address: '1'
    alias: TESTING
    connection_type: SERIAL
    device_type: SMU
    serial_config:
      baud_rate: 115200
      data_bits: 8
      end_input: none
      flow_control: xon_xoff
      parity: none
      stop_bits: one
  - address: MSO56-HOSTNAME
    connection_type: TCPIP
    device_type: SCOPE
options:
  setup_cleanup: false
  standalone: false
  teardown_cleanup: false
  verbose_mode: true
  verbose_visa: false
"""
            )
        finally:
            os.remove("./temp_config.toml")
            os.remove("./temp_config.yaml")

        assert (
            device_manager.get_current_configuration_as_environment_variable_strings()
            == "TM_OPTIONS=VERBOSE_MODE\n"
            "TM_DEVICES=~~~address=1,alias=TESTING,connection_type=SERIAL,device_type=SMU,"
            "serial_baud_rate=115200,serial_data_bits=8,serial_end_input=none,"
            "serial_flow_control=xon_xoff,serial_parity=none,serial_stop_bits=one"
            "~~~address=MSO56-HOSTNAME,connection_type=TCPIP,device_type=SCOPE~~~"
        )

    def test_dm_properties(self, device_manager: DeviceManager) -> None:
        """Test the editable properties of the DeviceManager.

        Args:
            device_manager: The DeviceManager object.
        """
        device_manager.remove_all_devices()
        saved_teardown = device_manager.teardown_cleanup_enabled
        saved_setup = device_manager.setup_cleanup_enabled
        saved_verbose = device_manager.verbose
        saved_visa_lib = device_manager.visa_library

        try:
            assert device_manager.is_open
            assert not device_manager.devices
            # Test the property setters and getters
            device_manager.teardown_cleanup_enabled = not saved_teardown
            assert device_manager.teardown_cleanup_enabled != saved_teardown
            device_manager.setup_cleanup_enabled = not saved_setup
            assert device_manager.setup_cleanup_enabled != saved_setup
            device_manager.verbose = not saved_verbose
            assert device_manager.verbose != saved_verbose
            device_manager.visa_library = PYVISA_PY_BACKEND
            assert device_manager.visa_library == PYVISA_PY_BACKEND
        finally:
            # Reset properties
            device_manager.teardown_cleanup_enabled = saved_teardown
            device_manager.setup_cleanup_enabled = saved_setup
            device_manager.verbose = saved_verbose
            device_manager.visa_library = saved_visa_lib

    # pylint: disable=too-many-locals
    def test_visa_device_methods_and_method_adding(  # noqa: C901,PLR0915
        self, device_manager: DeviceManager, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Test methods pertaining to VISA devices.

        Args:
            device_manager: The DeviceManager object.
            capsys: The captured stdout and stderr.
        """
        # Remove all previous devices
        device_manager.remove_all_devices()
        # Read the captured stdout to clear it
        _ = capsys.readouterr().out
        saved_setup_enable = device_manager.setup_cleanup_enabled
        saved_teardown_enable = device_manager.teardown_cleanup_enabled
        device_manager.setup_cleanup_enabled = True
        device_manager.teardown_cleanup_enabled = True

        ############################################################################################
        # Make sure to add all methods to the remove_added_methods() fixture
        # at the top of this test module.

        def gen_count() -> Iterator[int]:
            """Local counter."""
            count = 0
            while True:
                count += 1
                yield count

        local_count = gen_count()

        initial_input = '''import abc
from abc import ABC

from tm_devices.helpers import DeviceConfigEntry

class Device(ABC, metaclass=abc.ABCMeta):
    def __init__(self, config_entry: DeviceConfigEntry, verbose: bool) -> None: ...
    def already_exists(self) -> None:
        """Return nothing."""
'''
        sub_filepath = Path("drivers/device.pyi")
        generated_stub_dir = (
            Path(__file__).parent
            / "samples/generated_stubs"
            / f"output_{sys.version_info.major}{sys.version_info.minor}/tm_devices"
        )
        generated_stub_file = generated_stub_dir / sub_filepath
        golden_stub_dir = Path(__file__).parent / "samples" / "golden_stubs"
        generated_stub_file.parent.mkdir(parents=True, exist_ok=True)
        with open(generated_stub_file, "w", encoding="utf-8") as generated_file:
            generated_file.write(initial_input)
        with mock.patch.dict("os.environ", {"TM_DEVICES_STUB_DIR": str(generated_stub_dir)}):
            # noinspection PyUnusedLocal,PyShadowingNames
            @Device.add_property(is_cached=True)
            def inc_cached_count(self: Device) -> int:  # noqa: ARG001
                """Increment a local counter."""
                return next(local_count)

            # noinspection PyUnusedLocal,PyShadowingNames
            @Device.add_property(is_cached=False)
            def inc_count(self: Device) -> int:  # noqa: ARG001
                """Increment a local counter."""
                return next(local_count)

            # noinspection PyShadowingNames
            @Device.add_property
            def class_name(self: Device) -> str:
                """Return the class name."""
                return self.__class__.__name__

            # noinspection PyShadowingNames
            @Device.add_method
            def custom_model_getter(
                self: Device,
                value1: str,
                value2: str = "add",
                value3: str = "",
                value4: float = 0.1,
            ) -> str:
                """Return the model."""
                return " ".join(["Device", self.model, value1, value2, value3, str(value4)])

            # noinspection PyShadowingNames
            @Device.add_method
            def custom_list(self: Device) -> List[str]:
                """Return the model and serial in a list."""
                return [self.model, self.serial]

            @Device.add_method
            def custom_return_none() -> None:
                """Return nothing.

                This has a multi-line description.
                """

            @Device.add_method
            def already_exists() -> None:
                """Return nothing."""

            with pytest.raises(AssertionError):

                @Scope.add_method
                def custom_return() -> None:
                    """Return nothing."""

        @Scope.add_method
        def custom_model_getter_scope(device: Scope, value: str) -> str:
            """Return the model."""
            return f"Scope {device.model} {value}"

        @SignalSource.add_method
        def custom_model_getter_ss(device: SignalSource, value: str) -> str:
            """Return the model."""
            return f"SignalSource {device.model} {value}"

        @AFG.add_method
        def custom_model_getter_afg(device: AFG, value: str) -> str:
            """Return the model."""
            return f"AFG {device.model} {value}"

        @AFG3K.add_method
        def custom_model_getter_afg3k(device: AFG3K, value: str) -> str:
            """Return the model."""
            return f"AFG3K {device.model} {value}"

        @AFG3KC.add_method
        def custom_model_getter_afg3kc(device: AFG3KC, value: str) -> str:
            """Return the model."""
            return f"AFG3KC {device.model} {value}"

        ############################################################################################
        start_dir = os.getcwd()
        try:
            os.chdir(generated_stub_file.parent)
            subprocess.check_call(
                [  # noqa: S603
                    sys.executable,
                    "-m",
                    "ruff",
                    "format",
                    "--quiet",
                    generated_stub_file.name,
                ]
            )
            subprocess.check_call(
                [  # noqa: S603
                    sys.executable,
                    "-m",
                    "ruff",
                    "--quiet",
                    "check",
                    "--select=I",
                    "--fix",
                    generated_stub_file.name,
                ]
            )
        finally:
            os.chdir(start_dir)
        with open(golden_stub_dir / sub_filepath, encoding="utf-8") as golden_file:
            golden_contents = golden_file.read()
        with open(generated_stub_file, encoding="utf-8") as generated_file:
            generated_contents = generated_file.read()
        assert generated_contents == golden_contents

        # Test the custom added properties
        afg = device_manager.add_afg("afg3kc-hostname", alias="testing")
        # noinspection PyUnresolvedReferences
        assert afg.class_name == "AFG3KC"
        # noinspection PyUnresolvedReferences
        _ = afg.inc_cached_count
        # noinspection PyUnresolvedReferences
        assert afg.inc_cached_count == 1, "cached property is not working"
        # noinspection PyUnresolvedReferences
        _ = afg.inc_count
        # noinspection PyUnresolvedReferences
        assert afg.inc_count == 3, "uncached property is not working"

        # Test the custom added methods
        # noinspection PyUnresolvedReferences
        assert afg.custom_model_getter("a", "b", "c", 0.1) == "Device AFG3252C a b c 0.1"
        # noinspection PyUnresolvedReferences
        assert afg.custom_model_getter_ss("hello") == "SignalSource AFG3252C hello"
        # noinspection PyUnresolvedReferences
        assert afg.custom_model_getter_afg("hello") == "AFG AFG3252C hello"
        # noinspection PyUnresolvedReferences
        assert afg.custom_model_getter_afg3k("hello") == "AFG3K AFG3252C hello"
        # noinspection PyUnresolvedReferences
        assert afg.custom_model_getter_afg3kc("hello") == "AFG3KC AFG3252C hello"
        with pytest.raises(AttributeError):
            # noinspection PyUnresolvedReferences
            afg.custom_model_getter_scope("hello")

        # Test VISA methods
        assert afg.set_and_check("OUTPUT1:STATE", "1", custom_message_prefix="Custom prefix") == "1"
        device_manager.disable_device_command_checking()
        assert afg.set_and_check("OUTPUT1:STATE", "0") == ""
        device_manager.cleanup_all_devices()
        console_output = capsys.readouterr()
        assert "Beginning Device Cleanup on AFG " in console_output.out
        assert "Response from 'OUTPUT1:STATE?' >>  '1'" in console_output.out
        assert "Response from 'OUTPUT1:STATE?' >>  '0'" not in console_output.out
        assert console_output.err == ""

        assert len(device_manager.devices) == 1
        device_manager.close()
        assert "Beginning Device Cleanup" in capsys.readouterr().out
        assert len(device_manager.devices) == 1

        device_manager.setup_cleanup_enabled = False
        device_manager.open()
        device_manager.verbose_visa = True
        afg = device_manager.get_afg(number_or_alias="testing")
        afg.ieee_cmds.idn()
        assert "pyvisa - DEBUG" in capsys.readouterr().err
        device_manager.verbose_visa = False
        assert not device_manager.verbose_visa
        afg.ieee_cmds.idn()
        assert "pyvisa - DEBUG" not in capsys.readouterr().err
        device_manager.teardown_cleanup_enabled = False
        assert len(device_manager.devices) == 1
        device_manager.close()
        assert "Beginning Device Cleanup" not in capsys.readouterr().out
        assert len(device_manager.devices) == 1

        device_manager.open()
        device_manager.remove_device(alias="testing")
        device_manager.setup_cleanup_enabled = saved_setup_enable
        device_manager.teardown_cleanup_enabled = saved_teardown_enable

    def test_failed_cleanup(self, device_manager: DeviceManager) -> None:
        """Test what happens when a device manager cleanup fails.

        Args:
            device_manager: The DeviceManager object.
        """
        device_manager.add_afg("afg3kc-timeout", alias="bad-afg")
        with pytest.raises(visa.Error):
            device_manager.cleanup_all_devices()
        device_manager.remove_device(alias="bad-afg")

    def test_exceptions(self, device_manager: DeviceManager) -> None:
        """Verify some of the exceptions that the DeviceManager can raise.

        Args:
            device_manager: The DeviceManager object.
        """
        device_manager.remove_all_devices()

        # Test getting a device type that was not the specified type
        device_manager.add_afg("afg3kc-hostname", alias="my-device")
        with pytest.raises(TypeError):
            device_manager.get_scope("my-device")
        device_manager.remove_all_devices()

        # Test the error raised with bad *idn? return data
        # patched the stb to return 80 = 64 (Service Request) + 16 (message available)
        with mock.patch(
            "pyvisa.resources.messagebased.MessageBasedResource.read_stb",
            mock.MagicMock(return_value=80),
        ), mock.patch(
            "pyvisa.resources.messagebased.MessageBasedResource.write",
            mock.MagicMock(return_value=5),
        ), mock.patch(
            "pyvisa.resources.messagebased.MessageBasedResource.read",
            mock.MagicMock(return_value="data"),
        ):
            with pytest.warns(UserWarning), pytest.raises(SystemError) as error:
                device_manager.add_afg("afg3kc-hostname")
            assert str(error.value) == (
                "Unable to read *IDN? response.\n"
                "\tThe device `TCPIP0::AFG3KC-HOSTNAME::inst0::INSTR` likely has data sitting "
                "in the VISA Output Buffer that survived device_clear()."
            )

        # Test the error raised with timeout on *idn? query
        with mock.patch(
            "pyvisa.resources.messagebased.MessageBasedResource.read_stb",
            mock.MagicMock(return_value=16),
        ), mock.patch(
            "pyvisa.resources.messagebased.MessageBasedResource.write",
            mock.MagicMock(return_value=5),
        ), mock.patch(
            "pyvisa.resources.messagebased.MessageBasedResource.read",
            mock.MagicMock(side_effect=visa.VisaIOError(pyvisa.constants.StatusCode.error_timeout)),
        ):
            # patched the stb to return 16 (message available)
            with pytest.warns(UserWarning), pytest.raises(SystemError) as error:
                device_manager.add_afg("afg3kc-hostname")
            assert str(error.value) == (
                "VI_ERROR_TMO (-1073807339): Timeout expired before operation completed.\n"
                "\tUnable to read data after 2s.\n"
                "\t\n"
                "\tPlease reboot or read/clear the VISA output buffer on your device and try "
                "again."
            )

        # Test that if a badly formatted IDN is returned from __clear_visa_output_buffer_and_get_idn
        # that an exceptions is still caught during creation in __select_visa_device_driver
        with mock.patch(
            "tm_devices.device_manager.DeviceManager."
            "_DeviceManager__clear_visa_output_buffer_and_get_idn",
            mock.MagicMock(return_value="bad IDN"),
        ):
            with pytest.raises(SystemError) as error:
                device_manager.add_afg("afg3kc-hostname")
            assert (
                str(error.value)
                == "Unable to determine which device driver to use. *IDN? returned 'bad IDN'"
            )

        with pytest.raises(LookupError):
            device_manager.get_afg(10)

        with pytest.raises(NotImplementedError), pytest.warns(UserWarning):
            device_manager.add_smu("UNKNOWN-SMU", connection_type="USB")

        with pytest.raises(
            ValueError, match=r"Either a name or alias must be specified when fetching a device."
        ):
            device_manager.get_device(device_number=1)

        with pytest.raises(SystemError), pytest.warns(UserWarning):
            device_manager.add_afg("UNKNOWN")

        with pytest.raises(SystemError):
            device_manager.add_afg("BAD-IDN")

        with mock.patch(
            "pyvisa.ResourceManager", mock.MagicMock(side_effect=visa.Error())
        ), pytest.raises(AssertionError):
            device_manager.get_available_devices()

        with mock.patch(
            "pyvisa.ResourceManager.list_resources", mock.MagicMock(side_effect=visa.Error())
        ), pytest.raises(AssertionError):
            device_manager.get_available_devices()

        with pytest.raises(TypeError):
            device_manager.add_awg("afg3kc-hostname", alias="mismatch")

        device_manager.close()
        with pytest.raises(AttributeError):
            device_manager.get_available_devices()
        device_manager.open()

        assert device_manager.is_open
        with pytest.raises(
            AssertionError,
            match="The .* method should only be used if the DeviceManager has already been closed",
        ):
            device_manager.open()

        device_manager.close()
        with pytest.warns(UserWarning), DeviceManager() as dev_mgr:
            assert dev_mgr.is_open
            dev_mgr.close()
        assert not device_manager.is_open
        device_manager.open()
        assert device_manager.is_open

    def test_get_available_devices(self, device_manager: DeviceManager) -> None:
        """Test the get_available_devices() method.

        Args:
            device_manager: The DeviceManager object.
        """
        local_rm = visa.ResourceManager(SIMULATED_VISA_LIB)
        device_tuple = local_rm.list_resources()
        local_rm.close()

        device_manager.remove_all_devices()
        afg = device_manager.add_afg("afg3kc-hostname")
        assert afg.query("*IDN?") == "TEKTRONIX,AFG3252C,SERIAL1,SCPI:99.0 FV:3.2.3"

        available_devices = device_manager.get_available_devices(
            search="::", configured=False, local=False
        )
        assert afg.query("*IDN?") == "TEKTRONIX,AFG3252C,SERIAL1,SCPI:99.0 FV:3.2.3"
        assert available_devices == {}

        available_devices = device_manager.get_available_devices(search="::")
        assert afg.query("*IDN?") == "TEKTRONIX,AFG3252C,SERIAL1,SCPI:99.0 FV:3.2.3"
        assert available_devices["local"] == device_tuple
        assert available_devices["configured"] == ()

        available_devices = device_manager.get_available_devices()
        assert afg.query("*IDN?") == "TEKTRONIX,AFG3252C,SERIAL1,SCPI:99.0 FV:3.2.3"
        assert available_devices["local"] == device_tuple
        assert available_devices["configured"] == (
            "address=AFG3KC-HOSTNAME,connection_type=TCPIP,device_type=AFG",
        )

    def test_deleting_device_manager(self) -> None:
        """Test the behavior of deleting the DeviceManager instance.

        The script tests manually deleting, manually closing, and just leaving the DeviceManager
        open.
        """
        num_closes = 3
        args = [
            sys.executable,
            str(Path(__file__).parent / "validate_device_manager_delete.py"),
        ]
        stdout = subprocess.check_output(args).decode("utf-8")  # noqa: S603

        assert stdout.count("Closing Connections to Devices") == num_closes
        assert stdout.count("Closing Connection to AFG 1") == num_closes
        assert stdout.count("DeviceManager Closed") == num_closes

    def test_loading_isolated_config_file(
        self, device_manager: DeviceManager, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Test the behavior of loading an isolated config file.

        Args:
            device_manager: The DeviceManager object.
            capsys: The captured stdout and stderr.
        """
        # Test adding with pre-existing devices
        device_manager.remove_all_devices()
        saved_setup_enable = device_manager.setup_cleanup_enabled
        saved_teardown_enable = device_manager.teardown_cleanup_enabled
        device_manager.add_scope("MSO56-HOSTNAME")
        assert len(device_manager.devices) == 1
        _ = capsys.readouterr()  # clear the output

        device_manager.load_config_file(Path(__file__).parent / "samples/simulated_config.yaml")
        assert len(device_manager.devices) == 3
        stdout = capsys.readouterr().out
        assert "Beginning Device Cleanup on AFG " in stdout
        assert "Finished Device Cleanup on AFG " in stdout

        # Test with an option set in the file
        device_manager.remove_all_devices()
        _ = capsys.readouterr()  # clear the output
        device_manager.load_config_file(
            Path(__file__).parent / "samples/simulated_config_no_cleanup.yaml"
        )
        assert len(device_manager.devices) == 3
        stdout = capsys.readouterr().out
        assert "Beginning Device Cleanup on AFG " not in stdout
        assert "Finished Device Cleanup on AFG " not in stdout

        # Test adding no devices
        device_manager.remove_all_devices()
        _ = capsys.readouterr()  # clear the output
        device_manager.load_config_file(
            Path(__file__).parent / "samples/simulated_config_no_devices.yaml"
        )
        assert not device_manager.devices
        stdout = capsys.readouterr().out
        assert "Opening Connections to Devices" not in stdout

        # Reset things
        device_manager.remove_all_devices()
        device_manager.setup_cleanup_enabled = saved_setup_enable
        device_manager.teardown_cleanup_enabled = saved_teardown_enable
