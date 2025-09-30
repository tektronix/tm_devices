# pyright: reportPrivateUsage=none
"""Test the SMUs."""

import os
import socket
import sys

from pathlib import Path
from typing import TYPE_CHECKING
from unittest import mock

import pytest
import pyvisa as visa

from packaging.version import Version

from conftest import UNIT_TEST_TIMEOUT
from tm_devices import DeviceManager

if TYPE_CHECKING:
    from typing import Dict, List

    from tm_devices.drivers import SMU2401, SMU2460, SMU2601B, SMU6430


# pylint: disable=too-many-locals
def test_smu(  # noqa: PLR0915
    device_manager: DeviceManager,
    capsys: pytest.CaptureFixture[str],
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Test the SMU driver and TSP's IEEE commands.

    Args:
        device_manager: The DeviceManager object.
        capsys: The captured stdout and stderr.
        caplog: The captured log messages.
    """
    smu: SMU2601B = device_manager.add_smu("smu2601b-hostname", alias="smu-device")
    assert id(device_manager.get_smu(number_or_alias="smu-device")) == id(smu)
    assert id(device_manager.get_smu(number_or_alias=smu.device_number)) == id(smu)

    assert smu.manufacturer == "Keithley Instruments Inc."
    assert smu.model == "Model 2601B"
    assert smu.serial == "4498311"
    assert smu.sw_version == Version("3.3.5")

    with smu.command_syntax():
        assert smu.commands.status.node_enable == "status.node_enable"

    _ = capsys.readouterr()  # throw away any stdout
    with smu.command_verification():
        smu.commands.status.node_enable = 1
        stdout = capsys.readouterr().out
        assert "Write" in stdout
        assert "Query" in stdout

    smu.load_script(
        "loadfuncs",
        file_path=f"{Path(os.path.realpath(__file__)).parent}/samples/tsp_script.tsp",
        run_script=True,
        to_nv_memory=True,
    )
    stdout = capsys.readouterr().out
    assert "loadscript loadfuncs" in stdout
    assert "if loadfuncs ~= nil then script.delete('loadfuncs') end" in stdout
    assert "endscript" in stdout
    assert "loadfuncs.save()" in stdout
    assert "loadfuncs()" in stdout
    smu.expect_esr(0)
    smu.load_script(
        file_path=f"{Path(os.path.realpath(__file__)).parent}/samples/tsp_script.tsp",
        script_name="tsp_function",
    )
    stdout = capsys.readouterr().out
    assert "loadscript tsp_function" in stdout
    assert "if tsp_function ~= nil then script.delete('tsp_function') end" in stdout
    assert "endscript" in stdout
    assert "tsp_function.save()" not in stdout
    assert "tsp_function()" not in stdout
    smu.expect_esr(0)
    smu.load_script(
        script_name="loadfuncs",
        script_body=(Path(os.path.realpath(__file__)).parent / "samples" / "tsp_script.tsp")
        .read_text()
        .strip(),
        run_script=True,
    )
    stdout = capsys.readouterr().out
    assert "loadscript loadfuncs" in stdout
    assert "if loadfuncs ~= nil then script.delete('loadfuncs') end" in stdout
    assert "endscript" in stdout
    assert "loadfuncs.save()" not in stdout
    assert "loadfuncs()" in stdout
    smu.expect_esr(0)

    with mock.patch("pyvisa.highlevel.VisaLibraryBase.clear", mock.MagicMock(return_value=None)):
        assert smu.query_expect_timeout("INVALID?", timeout_ms=1) == ""
    with (
        mock.patch(
            "pyvisa.resources.messagebased.MessageBasedResource.query",
            mock.MagicMock(side_effect=visa.errors.Error("custom error")),
        ),
        pytest.raises(visa.errors.Error),
    ):
        smu.query_expect_timeout("INVALID?", timeout_ms=1)
    assert smu.expect_esr(32, ("Command error", "No Error"))

    with pytest.raises(AssertionError):
        smu.expect_esr(32, ("ERROR",))

    tspieee = smu._ieee_cmds  # noqa: SLF001

    # Currently there is no way to unit test the cls function. Called to get full coverage.
    tspieee.cls()
    with pytest.raises(
        ValueError, match=r"value=300 is not a valid value\. The value must be between 0 and 255\."
    ):
        tspieee.ese(300)
    assert tspieee.ese(1) == "1"
    assert tspieee.ese() == "1"
    assert tspieee.esr() == "0"
    assert tspieee.opc(True) == ""
    assert tspieee.opc() == "1"
    # Currently there is no way to unit test the rst function. Called to get full coverage.
    tspieee.rst()
    with pytest.raises(
        ValueError, match=r"value=300 is not a valid value\. The value must be between 0 and 255\."
    ):
        tspieee.sre(300)
    assert tspieee.sre(1) == "1"
    assert tspieee.sre() == "1"
    assert tspieee.stb() == "1"
    assert tspieee.tst() == "0"
    # Currently there is no way to unit test the wai function. Called to get full coverage.
    tspieee.wai()
    smu.expect_esr(0)

    # Test some generic device functionality
    capsys.readouterr()  # clear the buffer
    cmd_arg_constants_repr = (
        f"<tm_devices.commands.smu2601b_commands.SMU2601BCommandConstants object at "
        f"{str(smu.command_argument_constants).split(' at ', maxsplit=1)[-1]}"
    )
    cmds_repr = (
        f"<tm_devices.commands.smu2601b_commands.SMU2601BCommands object at "
        f"{str(smu.commands).split(' at ', maxsplit=1)[-1]}"
    )
    print(smu)  # noqa: T201
    expected_stdout = f"""{"=" * 45} SMU {smu.device_number} {"=" * 45}
  <class 'tm_devices.drivers.source_measure_units.smu26xx.smu2601b.SMU2601B'> object at {id(smu)}
    address='SMU2601B-HOSTNAME'
    alias='SMU-DEVICE'
    all_channel_names_list=('a',)
    command_argument_constants={cmd_arg_constants_repr}
    command_syntax_enabled=False
    command_verification_enabled=False
    commands={cmds_repr}
    config_entry={smu.config_entry!r}
    connection_type='TCPIP'
    default_visa_timeout={UNIT_TEST_TIMEOUT}
    device_number={smu.device_number}
    device_type='SMU'
    enable_verification=True
    hostname='SMU2601B-HOSTNAME'
    idn_string='Keithley Instruments Inc., Model 2601B, 4498311, 3.3.5'
    ieee_cmds={smu.ieee_cmds!r}
    ip_address=''
    is_open=True
    manufacturer='Keithley Instruments Inc.'
    model='Model 2601B'
    name='SMU {smu.device_number}'
    name_and_alias='SMU {smu.device_number} "SMU-DEVICE"'
    port=None
    resource_expression='TCPIP0::SMU2601B-HOSTNAME::inst0::INSTR'
    serial='4498311'
    series='SMU2601B'
    sw_version=<Version('3.3.5')>
    total_channels=1
    verbose=True
    visa_backend='{smu.visa_backend}'
    visa_resource=<'TCPIPInstrument'('TCPIP0::SMU2601B-HOSTNAME::inst0::INSTR')>
    visa_timeout={UNIT_TEST_TIMEOUT}
{"=" * (97 + len(str(smu.device_number)) - 1)}
"""
    stdout = capsys.readouterr().out
    assert stdout == expected_stdout
    assert smu.address == "SMU2601B-HOSTNAME"
    assert smu.alias == "SMU-DEVICE"
    assert smu.connection_type == "TCPIP"
    with (
        mock.patch("socket.socket.connect", mock.MagicMock(return_value=None)),
        mock.patch("socket.socket.shutdown", mock.MagicMock(return_value=None)),
    ):
        assert smu.wait_for_port_connection(
            4000, wait_time=0.05, sleep_seconds=0, accept_immediate_connection=True
        )
        assert (
            f"Successfully established a connection to port 4000 on {smu.ip_address}"
            in caplog.records[-1].message
        )
        assert caplog.records[-1].levelname == "INFO"
        with smu.temporary_verbose(False):
            assert smu.wait_for_port_connection(
                4000, wait_time=0.05, sleep_seconds=0, accept_immediate_connection=True
            )
        assert (
            f"Successfully established a connection to port 4000 on {smu.ip_address}"
            in caplog.records[-1].message
        )
        assert caplog.records[-1].levelname == "DEBUG"
        with pytest.raises(AssertionError):
            smu.wait_for_port_connection(
                4000,
                wait_time=0.05,
                sleep_seconds=0,
                accept_immediate_connection=False,
            )
    with mock.patch("socket.socket.connect", mock.MagicMock(side_effect=socket.error(""))):
        assert not smu.wait_for_port_connection(
            4000, wait_time=0.05, sleep_seconds=0, accept_immediate_connection=True
        )
        assert caplog.records[-1].message.startswith(
            f"Unable to establish a connection to port 4000 on {smu.ip_address} after"
        )
        assert caplog.records[-1].levelname == "WARNING"

    buffer = smu.get_buffers("smub.nvbuffer1")
    expected_buffer: Dict[str, List[float]] = {"smub.nvbuffer1": []}
    assert caplog.records[-1].message == "smub.nvbuffer1 was found to be empty"
    assert caplog.records[-1].levelname == "WARNING"
    assert buffer == expected_buffer

    buffer = smu.get_buffers("smua.nvbuffer1")
    expected_buffer = {"smua.nvbuffer1": [1.0, 2.0, 3.0, 4.0, 5.0]}
    assert buffer == expected_buffer

    buffer = smu.get_buffers("smua.nvbuffer1.timestamps")
    expected_buffer = {"smua.nvbuffer1.timestamps": [0.0, 0.1, 0.2, 0.3, 0.4]}
    assert buffer == expected_buffer

    smu.print_buffers("smua.nvbuffer1")
    stdout = capsys.readouterr().out
    assert "smua.nvbuffer1" in stdout
    for value in (1.0, 2.0, 3.0, 4.0, 5.0):
        assert str(value) in stdout

    filepath = Path(f"./temp_test_{sys.version_info.major}{sys.version_info.minor}.csv")

    try:
        smu.export_buffers(filepath.as_posix(), "smua.nvbuffer1")
        assert filepath.exists()
        with filepath.open(encoding="utf-8") as file:
            lines = file.readlines()
            for index, value in enumerate(["smua.nvbuffer1", "1.0", "2.0", "3.0", "4.0", "5.0"]):
                assert value in lines[index]
    finally:
        os.remove(filepath)

    smu.expect_esr(0)

    with pytest.raises(AssertionError) as error:
        smu.set_and_check("status.request_enable", 2, custom_message_prefix="Custom prefix")
    assert (
        str(error.value.args[0]).rsplit("SMU-DEVICE", maxsplit=1)[-1]
        == '") : Custom prefix, Failed to set status.request_enable to 2, '
        "Actual result does not match the expected result within a tolerance of 0, "
        "max: 2.0, act: 1.0, min: 2.0"
    )
    smu.enable_verification = False
    assert smu.set_and_check("status.request_enable", 1) == ""

    with pytest.raises(AssertionError, match="ESR value mismatch \\(Expected: 1, Actual: 0\\)"):
        smu.expect_esr(1)


def test_smu2450(device_manager: DeviceManager, capsys: pytest.CaptureFixture[str]) -> None:
    """Test the SMU2450 driver specific code.

    Args:
        device_manager: The DeviceManager object.
        capsys: The captured stdout and stderr.
    """
    smu: SMU2460 = device_manager.add_smu("SMU2460-HOSTNAME")
    smu.expect_esr(0)

    smu.commands.smu.source.sweeplinear("SolarCell", 0, 0.53, 56, 0.1)
    stdout = capsys.readouterr().out
    assert 'smu.source.sweeplinear("SolarCell", 0, 0.53, 56, 0.1)' in stdout

    with mock.patch("pyvisa.highlevel.VisaLibraryBase.clear", mock.MagicMock(return_value=None)):
        assert smu.query_expect_timeout("INVALID?", timeout_ms=1) == ""
    with (
        mock.patch(
            "pyvisa.resources.messagebased.MessageBasedResource.query",
            mock.MagicMock(side_effect=visa.errors.Error("custom error")),
        ),
        pytest.raises(visa.errors.Error),
    ):
        smu.query_expect_timeout("INVALID?", timeout_ms=1)
    assert smu.expect_esr(32, ("Command error", "No Error"))
    assert smu.all_channel_names_list == ("OUTPUT1",)


def test_smu2401(device_manager: DeviceManager) -> None:
    """Test the SMU2401 driver specific code.

    Args:
        device_manager: The DeviceManager object.
    """
    smu: SMU2401 = device_manager.add_smu("SMU2401-HOSTNAME")
    assert smu.get_errors() == (0, ('0,"No error"',))
    assert smu.set_and_check("OUTPUT1:STATE", 1) == "1"
    assert smu.all_channel_names_list == ("OUTPUT1",)


def test_smu6430(device_manager: DeviceManager) -> None:
    """Test the SMU6430 driver specific code.

    Args:
        device_manager: The DeviceManager object.
    """
    smu: SMU6430 = device_manager.add_smu("SMU6430-HOSTNAME")
    assert smu.get_errors() == (0, ('0,"No error"',))
    assert smu.set_and_check("OUTPUT1:STATE", 1) == "1"
    assert smu.all_channel_names_list == ("SOURCE1",)
