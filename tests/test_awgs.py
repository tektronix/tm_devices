# pyright: reportPrivateUsage=none
"""Test the AWGs."""
import pytest

from tm_devices import DeviceManager
from tm_devices.drivers.pi.signal_sources.awgs.awg import AWGSourceDeviceConstants


def test_awg5200(device_manager: DeviceManager, capsys: pytest.CaptureFixture[str]) -> None:
    """Test the AWG5200 driver.

    Args:
        device_manager: The DeviceManager object.
        capsys: The captured stdout and stderr.
    """
    awg5200 = device_manager.add_awg("awg5200-hostname", alias="awg5200")
    assert id(device_manager.get_awg(number_or_alias="awg5200")) == id(awg5200)
    assert id(device_manager.get_awg(number_or_alias=awg5200.device_number)) == id(awg5200)
    assert awg5200.total_channels == 4
    assert awg5200.all_channel_names_list == ("SOURCE1", "SOURCE2", "SOURCE3", "SOURCE4")
    awg5200.write("*SRE 256")
    awg5200.expect_esr(32, '1, "Command error"\n0,"No error"')
    with pytest.raises(AssertionError):
        awg5200.expect_esr(32, '1, Command error\n0,"No error"')
    awg5200.load_waveform("test", "file_path.txt", "TXT")
    assert 'MMEMory:IMPort "test", "file_path.txt", TXT' in capsys.readouterr().out
    awg5200.load_waveform("test", '"file_path.txt"', "TXT")
    assert 'MMEMory:IMPort "test", "file_path.txt", TXT' in capsys.readouterr().out
    assert awg5200.source_device_constants == AWGSourceDeviceConstants(
        memory_page_size=1,
        memory_max_record_length=16200000,
        memory_min_record_length=1,
    )
    assert awg5200.opt_string == "0"
