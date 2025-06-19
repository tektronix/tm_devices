"""Tests for the device_manager.py file."""

import os
import subprocess
import sys

from pathlib import Path
from unittest import mock

import pytest
import pyvisa as visa
import pyvisa.constants

from conftest import SIMULATED_VISA_LIB, UNIT_TEST_TIMEOUT
from tm_devices import DeviceManager
from tm_devices.helpers import ConnectionTypes, DeviceTypes, PYVISA_PY_BACKEND, SerialConfig


class TestDeviceManager:  # pylint: disable=no-self-use
    """Device Manager test class."""

    @pytest.mark.parametrize(
        # Get the list of device types, ignore the unit test ones since
        # this test only applies to actual supported devices.
        "device_type",
        list(
            filter(
                lambda x: "UNIT_TEST" not in x and "UNSUPPORTED" not in x,  # pyright: ignore[reportOperatorIssue]
                (y.name for y in DeviceTypes),
            )
        ),
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
            text = Path("./temp_config.toml").read_text(encoding="utf-8")
            assert (
                text
                == f"""[[devices]]
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
default_visa_timeout = {UNIT_TEST_TIMEOUT}
setup_cleanup = false
standalone = false
teardown_cleanup = false
verbose_mode = true
verbose_visa = false
"""
            )
            text = Path("./temp_config.yaml").read_text(encoding="utf-8")
            print(text)  # noqa: T201
            assert (
                text
                == f"""---
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
  default_visa_timeout: {UNIT_TEST_TIMEOUT}
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
            == f"TM_OPTIONS=DEFAULT_VISA_TIMEOUT={UNIT_TEST_TIMEOUT},VERBOSE_MODE\n"
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
            device_manager.default_visa_timeout = 1500
            assert device_manager.default_visa_timeout == 1500
        finally:
            # Reset properties
            device_manager.teardown_cleanup_enabled = saved_teardown
            device_manager.setup_cleanup_enabled = saved_setup
            device_manager.verbose = saved_verbose
            device_manager.visa_library = saved_visa_lib

    def test_failed_cleanup(self, device_manager: DeviceManager) -> None:
        """Test what happens when a device manager cleanup fails.

        Args:
            device_manager: The DeviceManager object.
        """
        device_manager.add_afg("afg3kc-timeout", alias="bad-afg")
        with pytest.raises(visa.Error):
            device_manager.cleanup_all_devices()
        device_manager.remove_device(alias="bad-afg")

    def test_warnings(self, device_manager: DeviceManager) -> None:
        """Verify some of the warning printouts that the DeviceManager can log.

        Args:
            device_manager: The DeviceManager object.
        """
        # Remove all previous devices
        device_manager.remove_all_devices()
        # Test the warning logged with bad read_stb() call
        with (
            mock.patch(
                "pyvisa.resources.messagebased.MessageBasedResource.read_stb",
                mock.MagicMock(side_effect=visa.VisaIOError(pyvisa.constants.VI_ERROR_INV_SETUP)),
            ),
            pytest.warns(
                UserWarning,
                match="A VISA IO error occurred when attempting to read the status byte or "
                "clear the output buffer of the resource",
            ),
        ):
            device_manager.add_afg("afg3252c-hostname", alias="warning_bad_read_stb")
        device_manager.remove_device(alias="warning_bad_read_stb")

        # Test the warning logged with message available (MAV) bit set
        # patched the stb to return 16 (message available)
        with (
            mock.patch(
                "pyvisa.resources.messagebased.MessageBasedResource.read_stb",
                mock.MagicMock(return_value=16),
            ),
            pytest.warns(
                UserWarning, match="had data sitting in the VISA Output Buffer on first connection."
            ),
        ):
            device_manager.add_afg("afg3252c-hostname", alias="warning_mav")
        device_manager.remove_device(alias="warning_mav")

    def test_exceptions(self, device_manager: DeviceManager) -> None:
        """Verify some of the exceptions that the DeviceManager can raise.

        Args:
            device_manager: The DeviceManager object.
        """
        # Remove all previous devices
        device_manager.remove_all_devices()

        # Test getting a device type that was not the specified type
        device_manager.add_afg("afg3252c-hostname", alias="my-device")
        with pytest.raises(TypeError):
            device_manager.get_scope("my-device")
        device_manager.remove_all_devices()

        # Test the error raised with bad *idn? return data
        # patched the stb to return 80 = 64 (Service Request) + 16 (message available)
        with (
            mock.patch(
                "pyvisa.resources.messagebased.MessageBasedResource.read_stb",
                mock.MagicMock(return_value=80),
            ),
            mock.patch(
                "pyvisa.resources.messagebased.MessageBasedResource.write",
                mock.MagicMock(return_value=5),
            ),
            mock.patch(
                "pyvisa.resources.messagebased.MessageBasedResource.read",
                mock.MagicMock(return_value="data"),
            ),
        ):
            with (
                pytest.warns(
                    UserWarning,
                    match="had data sitting in the VISA Output Buffer on first connection",
                ),
                pytest.raises(SystemError) as error,
            ):
                device_manager.add_afg("afg3252c-hostname")
            assert str(error.value) == (
                "Unable to read *IDN? response.\n"
                "\tThe device `TCPIP0::AFG3252C-HOSTNAME::inst0::INSTR` likely has data sitting "
                "in the VISA Output Buffer that survived device_clear()."
            )

        # Test the error raised with timeout on *idn? query
        with (
            mock.patch(
                "pyvisa.resources.messagebased.MessageBasedResource.read_stb",
                mock.MagicMock(return_value=16),
            ),
            mock.patch(
                "pyvisa.resources.messagebased.MessageBasedResource.write",
                mock.MagicMock(return_value=5),
            ),
            mock.patch(
                "pyvisa.resources.messagebased.MessageBasedResource.read",
                mock.MagicMock(side_effect=visa.VisaIOError(pyvisa.constants.VI_ERROR_TMO)),
            ),
        ):
            # patched the stb to return 16 (message available)
            with (
                pytest.warns(
                    UserWarning, match="Detected data in the buffer via the Status Byte register"
                ),
                pytest.raises(SystemError) as error,
            ):
                device_manager.add_afg("afg3252c-hostname")
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
                device_manager.add_afg("afg3252c-hostname")
            assert (
                str(error.value)
                == "Unable to determine which device driver to use. *IDN? returned 'bad IDN'"
            )

        with pytest.raises(LookupError):
            device_manager.get_afg(10)

        with (
            pytest.raises(NotImplementedError),
            pytest.warns(UserWarning, match='The "UNKNOWN" model is not supported by tm_devices'),
        ):
            device_manager.add_smu("UNKNOWN-SMU", connection_type="USB")

        with pytest.raises(
            ValueError, match=r"Either a name or alias must be specified when fetching a device."
        ):
            device_manager.get_device(device_number=1)

        with (
            pytest.raises(SystemError),
            pytest.warns(UserWarning, match='The "UNKNOWN" model is not supported by tm_devices'),
        ):
            device_manager.add_afg("UNKNOWN")

        with pytest.raises(SystemError):
            device_manager.add_afg("BAD-IDN")

        with (
            mock.patch("pyvisa.ResourceManager", mock.MagicMock(side_effect=visa.Error())),
            pytest.raises(AssertionError),
        ):
            device_manager.get_available_devices()

        with (
            mock.patch(
                "pyvisa.ResourceManager.list_resources", mock.MagicMock(side_effect=visa.Error())
            ),
            pytest.raises(AssertionError),
        ):
            device_manager.get_available_devices()

        with pytest.raises(TypeError):
            device_manager.add_awg("afg3252c-hostname", alias="mismatch")

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
        with (  # noqa: PT031
            pytest.warns(
                UserWarning,
                match=(
                    "The DeviceManager has already been created and is "
                    "not allowed to be instantiated twice"
                ),
            ),
            DeviceManager() as dev_mgr,
        ):
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
        afg = device_manager.add_afg("afg3252c-hostname")
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
            "address=AFG3252C-HOSTNAME,connection_type=TCPIP,device_type=AFG",
        )

    def test_deleting_device_manager(self) -> None:
        """Test the behavior of deleting the DeviceManager instance.

        The script tests manually deleting, manually closing, and just leaving the DeviceManager
        open.
        """
        num_closes = 1  # Only a single closing log message is expected
        args = [
            sys.executable,
            str(Path(__file__).parent / "validate_device_manager_delete.py"),
        ]
        stdout = subprocess.check_output(args).decode("utf-8")  # noqa: S603

        assert stdout.count("Closing Connections to Devices") == num_closes
        assert stdout.count("Closing Connection to AFG 1") == num_closes + 1
        assert stdout.count("AFG 1 was previously closed, no need to close it again") == 1
        assert stdout.count("DeviceManager Closed") == num_closes

    # noinspection PyUnresolvedReferences
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
        assert device_manager.default_visa_timeout == UNIT_TEST_TIMEOUT
        assert list(device_manager.devices.values())[-1].default_visa_timeout == UNIT_TEST_TIMEOUT  # pyright: ignore[reportUnknownMemberType,reportAttributeAccessIssue]
        _ = capsys.readouterr()  # clear the output

        expected_new_default_timeout = 1000
        device_manager.load_config_file(Path(__file__).parent / "samples/simulated_config.yaml")
        assert len(device_manager.devices) == 3
        stdout = capsys.readouterr().out
        assert "Beginning Device Cleanup on AFG " in stdout
        assert "Finished Device Cleanup on AFG " in stdout
        assert device_manager.default_visa_timeout == expected_new_default_timeout
        assert next(iter(device_manager.devices.values())).default_visa_timeout == UNIT_TEST_TIMEOUT  # pyright: ignore[reportUnknownMemberType,reportAttributeAccessIssue]
        assert (
            list(device_manager.devices.values())[-1].default_visa_timeout  # pyright: ignore[reportUnknownMemberType,reportAttributeAccessIssue]
            == expected_new_default_timeout
        )

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
        assert device_manager.default_visa_timeout == expected_new_default_timeout

        # Test adding no devices
        device_manager.remove_all_devices()
        _ = capsys.readouterr()  # clear the output
        device_manager.load_config_file(
            Path(__file__).parent / "samples/simulated_config_no_devices.yaml"
        )
        assert not device_manager.devices
        stdout = capsys.readouterr().out
        assert "Opening Connections to Devices" not in stdout
        assert device_manager.default_visa_timeout == expected_new_default_timeout

        # Reset things
        device_manager.remove_all_devices()
        device_manager.setup_cleanup_enabled = saved_setup_enable
        device_manager.teardown_cleanup_enabled = saved_teardown_enable
