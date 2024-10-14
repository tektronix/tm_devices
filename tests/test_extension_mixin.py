# pyright: reportUnusedFunction=none
# pyright: reportUnknownMemberType=none
# pyright: reportAttributeAccessIssue=none
# pyright: reportUnknownVariableType=none
# pyright: reportArgumentType=none
"""Test the extension mixin mechanisms, including the stub file modification."""

import contextlib
import os
import subprocess
import sys

from pathlib import Path
from typing import Iterator, List
from unittest import mock

import pytest

from tm_devices import DeviceManager
from tm_devices.driver_mixins.device_control.pi_control import PIControl
from tm_devices.driver_mixins.device_control.tsp_control import TSPControl
from tm_devices.driver_mixins.shared_implementations.tek_afg_awg_mixin import TekAFGAWG
from tm_devices.drivers import AFG3K, AFG3KC
from tm_devices.drivers.afgs.afg import AFG
from tm_devices.drivers.device import Device
from tm_devices.drivers.scopes.scope import Scope

INITIAL_DEVICE_INPUT = '''import abc
from abc import ABC

from tm_devices.helpers import DeviceConfigEntry

class Device(ABC, metaclass=abc.ABCMeta):
    class NestedClass:
        """This is a nested class."""
    def __init__(self, config_entry: DeviceConfigEntry, verbose: bool) -> None: ...
    def already_exists(self) -> None:
        """Return nothing."""
    @property
    def existing_property(self) -> int:
        """Return an int."""

def function_1(arg1: str, arg2: int = 1) -> bool: ...

class OtherDevice(ABC, metaclass=abc.ABCMeta):
    def __init__(self, config_entry: DeviceConfigEntry, verbose: bool) -> None: ...

def function_2(arg1: str, arg2: int = 2) -> bool: ...
'''
INITIAL_PI_DEVICE_INPUT = '''import abc

from abc import ABC

from tm_devices.helpers import DeviceConfigEntry

class PIControl(ABC, metaclass=abc.ABCMeta):
    def __init__(self, config_entry: DeviceConfigEntry, verbose: bool) -> None: ...
    def already_exists(self) -> None:
        """Return nothing."""

class OtherDevice(ABC, metaclass=abc.ABCMeta):
    def __init__(self, config_entry: DeviceConfigEntry, verbose: bool) -> None: ...
'''
INITIAL_TSP_DEVICE_INPUT = '''import abc

from abc import ABC
from dataclasses import dataclass
from tm_devices.helpers import DeviceConfigEntry

class TSPControl(ABC, metaclass=abc.ABCMeta):
    def __init__(self, config_entry: DeviceConfigEntry, verbose: bool) -> None: ...
    def already_exists(self) -> None:
        """Return nothing."""

@dataclass(frozen=True)
class CustomDataclass:

    value1: str
    value2: int = 1

'''


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
        (TekAFGAWG, "custom_model_getter_sg"),
        (AFG, "custom_model_getter_afg"),
        (AFG3K, "custom_model_getter_afg3k"),
        (AFG3KC, "custom_model_getter_afg3kc"),
        (PIControl, "added_method"),
        (TSPControl, "added_tsp_method"),
    ):
        with contextlib.suppress(AttributeError):
            delattr(obj, name)


# pylint: disable=too-many-locals
def test_visa_device_methods_and_method_adding(  # noqa: C901,PLR0915
    device_manager: DeviceManager, capsys: pytest.CaptureFixture[str]
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

    golden_stub_dir = Path(__file__).parent / "samples" / "golden_stubs"
    stub_device_filepath = Path("drivers/device.pyi")
    stub_pi_control_filepath = Path("driver_mixins/device_control/pi_control.pyi")
    stub_tsp_control_filepath = Path("driver_mixins/device_control/tsp_control.pyi")
    generated_stub_dir = (
        Path(__file__).parent
        / "samples/generated_stubs"
        / f"output_{sys.version_info.major}{sys.version_info.minor}/tm_devices"
    )
    generated_device_stub_file = generated_stub_dir / stub_device_filepath
    generated_device_stub_file.parent.mkdir(parents=True, exist_ok=True)
    generated_pi_control_stub_file = generated_stub_dir / stub_pi_control_filepath
    generated_tsp_control_stub_file = generated_stub_dir / stub_tsp_control_filepath
    generated_pi_control_stub_file.parent.mkdir(parents=True, exist_ok=True)
    generated_device_stub_file.write_text(INITIAL_DEVICE_INPUT, encoding="utf-8")
    generated_pi_control_stub_file.write_text(INITIAL_PI_DEVICE_INPUT, encoding="utf-8")
    generated_tsp_control_stub_file.write_text(INITIAL_TSP_DEVICE_INPUT, encoding="utf-8")
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

        @PIControl.add_method
        def added_method() -> None:
            """Return nothing."""

        @TSPControl.add_method
        def added_tsp_method() -> None:
            """Return nothing."""

        with pytest.raises(AssertionError):

            @Scope.add_method
            def custom_return() -> None:
                """Return nothing."""

    @Scope.add_method
    def custom_model_getter_scope(device: Scope, value: str) -> str:
        """Return the model."""
        return f"Scope {device.model} {value}"

    @TekAFGAWG.add_method
    def custom_model_getter_sg(device: TekAFGAWG, value: str) -> str:
        """Return the model."""
        return f"TekAFGAWG {device.model} {value}"

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
        os.chdir(generated_stub_dir)
        subprocess.check_call(  # noqa: S603
            [
                sys.executable,
                "-m",
                "ruff",
                "format",
                "--quiet",
                generated_stub_dir,
            ]
        )
        subprocess.check_call(  # noqa: S603
            [
                sys.executable,
                "-m",
                "ruff",
                "check",
                "--quiet",
                "--select=I",
                "--fix",
                generated_stub_dir,
            ]
        )
    finally:
        os.chdir(start_dir)

    # Compare the file contents
    golden_device_contents = (golden_stub_dir / stub_device_filepath).read_text(encoding="utf-8")
    generated_device_contents = generated_device_stub_file.read_text(encoding="utf-8")
    assert generated_device_contents == golden_device_contents
    golden_pi_control_contents = (golden_stub_dir / stub_pi_control_filepath).read_text(
        encoding="utf-8"
    )
    generated_pi_control_contents = generated_pi_control_stub_file.read_text(encoding="utf-8")
    assert generated_pi_control_contents == golden_pi_control_contents
    golden_tsp_control_contents = (golden_stub_dir / stub_tsp_control_filepath).read_text(
        encoding="utf-8"
    )
    generated_tsp_control_contents = generated_tsp_control_stub_file.read_text(encoding="utf-8")
    assert generated_tsp_control_contents == golden_tsp_control_contents

    # Test the custom added properties
    afg = device_manager.add_afg("afg3252c-hostname", alias="testing")
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
    assert afg.custom_model_getter_sg("hello") == "TekAFGAWG AFG3252C hello"
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
